

import re
import os
from pathlib import Path
import ast

def keyword_search(md_filepath, search_phrases, category_label, exclude_phrases, vector_size): # this function hasbeen validated. 
    output_file = "category_occurrences.py"
    if exclude_phrases is None:
        exclude_phrases = []

    # 1. Extract mode and index from filename
    filename = Path(md_filepath).name
    match = re.search(r'reasoning_(ego|allo|coords)_(\d+)\.md$', filename)
    if not match:
        print(f"Skipping {md_filepath}: Filename pattern not matched.")
        return
    
    file_mode = match.group(1) 
    file_idx = int(match.group(2))
    
    # Ensure vector_size is at least large enough for the current file index
    required_size = max(vector_size, file_idx)

    # 2. Define templates
    base_templates = [
        "line_R_{mode}_adj_json_{cat}_15", "line_R_{mode}_adj_txt_{cat}_15", "line_R_{mode}_jpg_{cat}_15", 
        "line_R_{mode}_json_{cat}_15", "line_R_{mode}_tokenized_txt_{cat}_15", "occupancy_R_{mode}_adj_json_{cat}_15", 
        "occupancy_R_{mode}_adj_txt_{cat}_15", "occupancy_R_{mode}_ascii_txt_{cat}_15", "occupancy_R_{mode}_jpg_{cat}_15", 
        "occupancy_R_{mode}_json_{cat}_15", "occupancy_R_{mode}_tokenized_txt_{cat}_15"
    ]



    # Testing if i can add all output types as vecs.
    all_modes = ['ego', 'allo', 'coords']
    all_target_vectors = []
    for m in all_modes:
        all_target_vectors.extend([template.format(mode=m, cat=category_label) for template in base_templates])

    # all_target_vectors = [t.format(mode=file_mode, cat=category_label) for t in base_templates]

    # 3. Load existing vectors
    vector_data = {vec: [0] * required_size for vec in all_target_vectors}
    if os.path.exists(output_file):
        try:
            with open(output_file, "r") as f:
                content = f.read()
                existing_vars = re.findall(r"(\w+)\s*=\s*(\[.*?\])", content, re.DOTALL)
                for var_name, var_value in existing_vars:
                    val = ast.literal_eval(var_value)
                    # Extend existing lists if they are shorter than what we need
                    if len(val) < required_size:
                        val.extend([0] * (required_size - len(val)))
                    
                    if var_name in vector_data:
                        vector_data[var_name] = val
                    else:
                        # Keep other existing category vectors in the file
                        vector_data[var_name] = val
        except Exception as e:
            print(f"Error loading existing vectors: {e}")

    # 4. Improved Mapping helper
    def get_vector_name(header_str, mode, cat):
        h = header_str.lower().strip("`# ")
        prefix = f"line_R_{mode}" if "line" in h else f"occupancy_R_{mode}"
        
        # Priority-based subtype matching
        if "adj" in h and "json" in h: subtype = "adj_json"
        elif "adj" in h and "txt" in h: subtype = "adj_txt"
        elif "tokenized" in h: subtype = "tokenized_txt"
        elif "ascii" in h: subtype = "ascii_txt"
        elif "json" in h: subtype = "json"
        elif "jpg" in h: subtype = "jpg"
        else: subtype = None
        
        return f"{prefix}_{subtype}_{cat}_15" if subtype else None

    # 5. Parsing logic
    with open(md_filepath, "r", encoding="utf-8") as f:
        full_content = f.read()

    # Split by representation headers (###). 
    # Use \s* to handle cases where there might be no space or multiple spaces.
    sections = re.split(r'(?m)^###\s*', full_content)
    
    search_phrases = [p.lower() for p in search_phrases]
    exclude_phrases = [e.lower() for e in exclude_phrases]

    # Robust regex for markers: handles potential whitespace variations
    # r'\*\*Internal Thoughts:\*\*\s*(.*?)\s*\*\*Unfiltered Response:\*\*'
    pattern = re.compile(r'\*\*Internal Thoughts:\*\*\s*(.*?)\s*\*\*Unfiltered Response:\*\*', re.DOTALL | re.IGNORECASE)

    for section in sections[1:]: 
        lines = section.split('\n')
        if not lines: continue
        
        header_line = lines[0]
        current_vector = get_vector_name(header_line, file_mode, category_label)
        
        if not current_vector:
            continue

        # Use finditer to scan ALL occurrences of thoughts in this section
        thought_matches = pattern.finditer(section)
        
        section_total_count = 0
        for match_thought in thought_matches:
            thought_text = match_thought.group(1).lower()
            
            for p in search_phrases:
                p_count = thought_text.count(p)
                for exclude in exclude_phrases:
                    if p in exclude:
                        p_in_exclude = exclude.count(p)
                        exclude_in_text = thought_text.count(exclude)
                        p_count -= (p_in_exclude * exclude_in_text)
                
                section_total_count += max(0, p_count)
        
        # Final safety check on vector length
        if current_vector not in vector_data:
            vector_data[current_vector] = [0] * required_size
        while len(vector_data[current_vector]) < file_idx:
            vector_data[current_vector].append(0)

        vector_data[current_vector][file_idx-1] += section_total_count

    # 6. Save updated vectors
    with open(output_file, "w") as f:
        f.write("# Persistent Category Occurrences\n\n")
        for vec in sorted(vector_data.keys()):
            f.write(f"{vec} = {vector_data[vec]}\n")

# --- Example Run ---
if __name__ == "__main__":


    script_dir = Path(__file__).parent 
    # Update this path if the Maze ID or Dataset changes
    files = [ # wATCH OUT with adding files when count vectors already exists. Rerunning adds to existing vectors and does not reset them.
        script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_1.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_2.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_3.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 4" / "comparison_report_reasoning_coords_4.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 5" / "comparison_report_reasoning_coords_5.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 6" / "comparison_report_reasoning_coords_6.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 7" / "comparison_report_reasoning_coords_7.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 8" / "comparison_report_reasoning_coords_8.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 9" / "comparison_report_reasoning_coords_9.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 10" / "comparison_report_reasoning_coords_10.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 11" / "comparison_report_reasoning_coords_11.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 12" / "comparison_report_reasoning_coords_12.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 13" / "comparison_report_reasoning_coords_13.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 14" / "comparison_report_reasoning_coords_14.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 15" / "comparison_report_reasoning_coords_15.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 16" / "comparison_report_reasoning_coords_16.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 17" / "comparison_report_reasoning_coords_17.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 18" / "comparison_report_reasoning_coords_18.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 19" / "comparison_report_reasoning_coords_19.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 20" / "comparison_report_reasoning_coords_20.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 21" / "comparison_report_reasoning_coords_21.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 22" / "comparison_report_reasoning_coords_22.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 23" / "comparison_report_reasoning_coords_23.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 24" / "comparison_report_reasoning_coords_24.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 25" / "comparison_report_reasoning_coords_25.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 26" / "comparison_report_reasoning_coords_26.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 27" / "comparison_report_reasoning_coords_27.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 28" / "comparison_report_reasoning_coords_28.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 29" / "comparison_report_reasoning_coords_29.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 30" / "comparison_report_reasoning_coords_30.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 31" / "comparison_report_reasoning_coords_31.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 32" / "comparison_report_reasoning_coords_32.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 33" / "comparison_report_reasoning_coords_33.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 34" / "comparison_report_reasoning_coords_34.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 35" / "comparison_report_reasoning_coords_35.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 36" / "comparison_report_reasoning_coords_36.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 37" / "comparison_report_reasoning_coords_37.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 38" / "comparison_report_reasoning_coords_38.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 39" / "comparison_report_reasoning_coords_39.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 40" / "comparison_report_reasoning_coords_40.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 41" / "comparison_report_reasoning_coords_41.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 42" / "comparison_report_reasoning_coords_42.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 43" / "comparison_report_reasoning_coords_43.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 44" / "comparison_report_reasoning_coords_44.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 45" / "comparison_report_reasoning_coords_45.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 46" / "comparison_report_reasoning_coords_46.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 47" / "comparison_report_reasoning_coords_47.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 48" / "comparison_report_reasoning_coords_48.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 49" / "comparison_report_reasoning_coords_49.md",
        script_dir / "Dataset 03" / "Dataset 03 15x15 50" / "comparison_report_reasoning_coords_50.md",
]

      
    
    # phrases_algorithm = [ 'DFS', 'BFS', 'dfs', 'bfs', 'Breadth-First', 'Depth-First', 'breadth-first', 'depth-first', 'algorithm', 'visited',
                        #   'queue', 'queuing', 'dequeuing', 'enqueuing', 'parent','A*']
    phrases_algorithm = [ 'visited', 'queue', 'queuing', 'dequeuing', 'enqueuing', 'parent',]
    
    phrases_heuristic = ['down-right', 'right-down', 'down and right', 'downwards and to the right', 
                         'downward and to the right', 'down then right', 'right then down', 
                         'to the right and down', 'right then down', 'to the right and down', 
                         'right-hand', 'wall-following', 'heuristic',  'visually tracing', 'visual', 'eyes',
                         'down, right', 'right, down', 'southeast']
    phrases_sbs = [') to (', 
                   '), (',
                   ') and (',
                   ') or (',
                   ') has (', 
                   '), then (',
                   ') then (', 
                   '), and then (', 
                   ') and then (',
                   'Path: `(',
                   'options are ('
                   ]
    exclusions_sbs = ['(0,0) to (14,14)', "(1,1) to (29,29)", '(0,0) to (5,5)', "(1,1) to 11,11)", '(0,0) to (2,2)', "(1,1) to (5,5)"]
    phrases_backtracking = ['dead-end', 'backtrack', 'retracing', 'I go back', 'track back', 'backtrack when', 'backtracked when'
                            'recalculate', 'over and over', 'stuck', 'retrace', 'loops']
    phrases_frustration = ['complicated', 'challenge', 'confusing' ,'confused', 'stuck', 'struggling', 
                           'struggle', 'difficult', 'difficult to parse', 'suspect', 'suspicion', 'no solution', 'typo', 'twists', 
                           'proving to be a challenge', 'proves to be a challenge' ,'twisty', 'careful', 'complex', 
                           'more elaborate than I expected', 'more intricate than I anticipated', 'trap', 'is the problem flawed?' , 'oversight']
    phrases_restart  =["I'll need to visualize the maze in a different way", "I'll begin from the starting node again", 
                       "I'll begin from the start again", "I did it again", 'restart', 'several attempts', 'trial and error',
                         'I had to go back', 'rethink', 'more systematic', 'retrace', 'new method', 'try again', 're-routing', 
                         're-evaluate', 'switch', 'I start again', 'start fresh', 'disconnect', 'change my approach', 'another approach', 'change my tactic', 
                         'refining the approach', 'strategy shift' ]
    phrases_reverse_search = ['tracing from the end', 'working backward', 'from the target', 'from the end', 
                              'starting at (14,14)', 'starting at (29,29)', 'starting at (2,2)','starting at (11,11)', 'starting at (5,5)', 
                              'working backward', 'meeting in the middle', 'trace a path backward', 'from (14,14) to (0,0)', 
                              'from (29,29) to (1,1)', 'from (5,5) to (0,0)', 'from (2,2) to (0,0)', 'from (11,11) to (0,0)', 'from (5,5) to (1,1)',
                              'path from the end point', 'both ends tracing']
    phrases_verification = ['check the path step by step','review', 'carefully ensure', ' meticulous', 'catch any error', 'examin', 'comparing',
                            'confirmed', 'check', 'go back over each step', 'verify', 'sanity check', 'valid', 'retrace', 'verified', 'double-check' ]
    phrases_false_confidence = ['I made it', 'confident', 'it works', 'paid off', 'solved', 'correct', 'complete', 'this is the solution', 'easy, right?','no problem']
    
    exclusions_false_confidence = ['not confident']



    categories = ['algorithm', 'heuristic', 'step_by_step', 'backtracking', 'frustration', 'restart', 'reverse_search', 'verification', 'false_confidence' ]

    phrases = [phrases_algorithm,
               phrases_heuristic, 
               phrases_sbs,
               phrases_backtracking,
               phrases_frustration,
               phrases_restart,
               phrases_reverse_search,
               phrases_verification,
               phrases_false_confidence]
    exclusions = [None, None, exclusions_sbs, None, None, None, None, None, exclusions_false_confidence]



for f in files:
        if f.exists():
            for a in range(len(categories)):
                keyword_search(f, phrases[a], category_label= categories[a], exclude_phrases=exclusions[a], vector_size=len(files))
                print(f"Processed {f.name} for category {categories[a]}. Results saved to category_occurrences.py.")
        else:
            print(f"File not found: {f}")