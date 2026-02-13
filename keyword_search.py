

import os
import re
from pathlib import Path

# def keyword_search(md_filepath, search_phrases, vector_size=30):
#     output_file = "category_occurrences.py"
    
#     # 1. Extract mode and index from filename
#     # Matches "..._ego_11.md", "..._coords_12.md", etc.
#     match = re.search(r'reasoning_(ego|allo|coords)_(\d+)\.md$', str(md_filepath))
#     if not match:
#         print(f"Skipping {md_filepath}: Could not find mode (ego/allo/coords) or index.")
#         return
    
#     file_mode = match.group(1) # 'ego', 'allo', or 'coords'
#     file_idx = int(match.group(2))

#     # 2. Define the base names for the 11 categories
#     base_categories = [
#         "line_R_{mode}_adj_json_15", "line_R_{mode}_adj_txt_15", "line_R_{mode}_jpg_15", 
#         "line_R_{mode}_json__15", "line_R_{mode}_tokenized_txt_15", "occupancy_R_{mode}_adj_json_15", 
#         "occupancy_R_{mode}_adj_txt_15", "occupancy_R_{mode}_ascii_txt_15", "occupancy_R_{mode}_jpg_15", 
#         "occupancy_R_{mode}_json_15", "occupancy_R_{mode}_tokenized_txt_15"
#     ]

#     # Generate all 33 possible target vectors (11 for each mode) to ensure persistence
#     all_modes = ['ego', 'allo', 'coords']
#     all_target_vectors = []
#     for m in all_modes:
#         all_target_vectors.extend([template.format(mode=m) for template in base_categories])

#     # 3. Load existing vectors from the file
#     vector_data = {vec: [0] * vector_size for vec in all_target_vectors}
#     if os.path.exists(output_file):
#         with open(output_file, "r") as f:
#             content = f.read()
#             for vec in all_target_vectors:
#                 list_match = re.search(fr"{vec}\s*=\s*(\[.*?\])", content, re.DOTALL)
#                 if list_match:
#                     try:
#                         vector_data[vec] = eval(list_match.group(1))
#                     except:
#                         pass

#     # 4. Helper to map MD headers to Vector Names using the detected mode
#     def get_vector_name(header_str, mode):
#         h = header_str.lower().strip("` ")
#         # Prefix now dynamically includes the mode from the filename
#         prefix = f"line_R_{mode}" if "line" in h else f"occupancy_R_{mode}"
        
#         if "adj" in h:
#             subtype = "adj_json" if "json" in h else "adj_txt"
#         elif "tokenized" in h:
#             subtype = "tokenized_txt"
#         elif "ascii" in h:
#             subtype = "ascii_txt"
#         elif "json" in h:
#             subtype = "json"
#         elif "jpg" in h:
#             subtype = "jpg"
#         else:
#             return None
#         return f"{prefix}_{subtype}_15"

#     # 5. Parsing the File
#     current_vector = None
#     in_internal_thoughts = False
    
#     with open(md_filepath, "r", encoding="utf-8") as f:
#         for line in f:
#             clean_line = line.strip()
            
#             # Start of a new category (e.g., ### `maze_line_...`)
#             if clean_line.startswith("###"):
#                 header_val = clean_line.replace("###", "").strip()
#                 current_vector = get_vector_name(header_val, file_mode)
#                 in_internal_thoughts = False
#                 continue
            
#             # Start of thoughts
#             if clean_line == "**Internal Thoughts:**":
#                 in_internal_thoughts = True
#                 continue
            
#             # Stop at the specific "Unfiltered Response" section
#             if in_internal_thoughts and clean_line.startswith("**Unfiltered Response:**"):
#                 in_internal_thoughts = False
#                 continue
            
#             # Search phrases within the specific section
#             if in_internal_thoughts and current_vector:
#                 if any(phrase.lower() in clean_line.lower() for phrase in search_phrases):
#                     if current_vector in vector_data:
#                         # Indexing logic: File 11 -> Index 10
#                         vector_data[current_vector][file_idx-1] = 1

#     # 6. Save updated vectors back to the .py file
#     with open(output_file, "w") as f:
#         f.write("# Persistent Category Occurrences\n\n")
#         # Sort keys to keep the file organized (allo, then coords, then ego)
#         for vec in sorted(vector_data.keys()):
#             f.write(f"{vec} = {vector_data[vec]}\n")

# # --- Example Run ---
# script_dir = Path(__file__).parent


# # files to test. This list can now contain any mixture of ego, allo, or coords files


# files = [
#     script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_1.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_2.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_3.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 4" / "comparison_report_reasoning_coords_4.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 5" / "comparison_report_reasoning_coords_5.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 6" / "comparison_report_reasoning_coords_6.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 7" / "comparison_report_reasoning_coords_7.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 8" / "comparison_report_reasoning_coords_8.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 9" / "comparison_report_reasoning_coords_9.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 10" / "comparison_report_reasoning_coords_10.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 11" / "comparison_report_reasoning_coords_11.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 12" / "comparison_report_reasoning_coords_12.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 13" / "comparison_report_reasoning_coords_13.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 14" / "comparison_report_reasoning_coords_14.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 15" / "comparison_report_reasoning_coords_15.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 16" / "comparison_report_reasoning_coords_16.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 17" / "comparison_report_reasoning_coords_17.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 18" / "comparison_report_reasoning_coords_18.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 19" / "comparison_report_reasoning_coords_19.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 20" / "comparison_report_reasoning_coords_20.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 21" / "comparison_report_reasoning_coords_21.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 22" / "comparison_report_reasoning_coords_22.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 23" / "comparison_report_reasoning_coords_23.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 24" / "comparison_report_reasoning_coords_24.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 25" / "comparison_report_reasoning_coords_25.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 26" / "comparison_report_reasoning_coords_26.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 27" / "comparison_report_reasoning_coords_27.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 28" / "comparison_report_reasoning_coords_28.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 29" / "comparison_report_reasoning_coords_29.md",
#     script_dir / "Dataset 03" / "Dataset 03 15x15 30" / "comparison_report_reasoning_coords_30.md",
    
# ]
# categories = "algorithm_mention"
# phrases = ["DFS", "BFS", "dfs", "bfs", "Breadth-First", "Depth-First", "breadth-first", "depth-first", 
#            "dictionary", "visited", "queue", "queuing", "dequeuing", "enqueuing", "parent" ]
# category = 'algorithm_naming'
# for f in files:
#     if f.exists():
#         keyword_search(f, phrases)


# # results
line_R_coords_adj_txt_15 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
line_R_coords_adj_txt_algorithm_mention_15 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]






import os
import re
from pathlib import Path

def keyword_search(md_filepath, search_phrases, category_label, vector_size=30):
    output_file = "category_occurrences.py"
    
    # 1. Extract mode and index from filename
    match = re.search(r'reasoning_(ego|allo|coords)_(\d+)\.md$', str(md_filepath))
    if not match:
        return
    
    file_mode = match.group(1) 
    file_idx = int(match.group(2))

    # 2. Define templates and include the category_label in the formatting
    base_templates = [
        "line_R_{mode}_adj_json_{cat}_15", "line_R_{mode}_adj_txt_{cat}_15", "line_R_{mode}_jpg_{cat}_15", 
        "line_R_{mode}_json_{cat}_15", "line_R_{mode}_tokenized_txt_{cat}_15", "occupancy_R_{mode}_adj_json_{cat}_15", 
        "occupancy_R_{mode}_adj_txt_{cat}_15", "occupancy_R_{mode}_ascii_txt_{cat}_15", "occupancy_R_{mode}_jpg_{cat}_15", 
        "occupancy_R_{mode}_json_{cat}_15", "occupancy_R_{mode}_tokenized_txt_{cat}_15"
    ]

    # Generate the vector names for ALL modes to ensure we don't delete data when writing
    all_modes = ['coords']#['ego', 'allo', 'coords']
    all_target_vectors = []
    for m in all_modes:
        # FIX: Pass both mode and the category label here
        all_target_vectors.extend([t.format(mode=m, cat=category_label) for t in base_templates])

    # 3. Load existing vectors
    vector_data = {vec: [0] * vector_size for vec in all_target_vectors}
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            content = f.read()
            # We look for ANY vector matching our naming pattern in the file
            # This ensures we don't overwrite other categories previously saved
            existing_vars = re.findall(r"(\w+)\s*=\s*(\[.*?\])", content, re.DOTALL)
            for var_name, var_value in existing_vars:
                if var_name in all_target_vectors:
                    vector_data[var_name] = eval(var_value)
                else:
                    # Keep data for other categories/labels already in the file
                    vector_data[var_name] = eval(var_value)

    # 4. Helper to map MD headers to Vector Names
    def get_vector_name(header_str, mode, cat):
        h = header_str.lower().strip("` ")
        prefix = f"line_R_{mode}" if "line" in h else f"occupancy_R_{mode}"
        
        if "adj" in h:
            subtype = "adj_json" if "json" in h else "adj_txt"
        elif "tokenized" in h:
            subtype = "tokenized_txt"
        elif "ascii" in h:
            subtype = "ascii_txt"
        elif "json" in h:
            subtype = "json"
        elif "jpg" in h:
            subtype = "jpg"
        else:
            return None
        return f"{prefix}_{subtype}_{cat}_15"

    # 5. Parsing the File
    current_vector = None
    in_internal_thoughts = False
    
    with open(md_filepath, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line.startswith("###"):
                header_val = clean_line.replace("###", "").strip()
                current_vector = get_vector_name(header_val, file_mode, category_label)
                in_internal_thoughts = False
                continue
            
            if clean_line == "**Internal Thoughts:**":
                in_internal_thoughts = True
                continue
            
            if in_internal_thoughts and clean_line.startswith("**Unfiltered Response:**"):
                in_internal_thoughts = False
                continue
            
            if in_internal_thoughts and current_vector:
                if any(phrase.lower() in clean_line.lower() for phrase in search_phrases):
                    if current_vector in vector_data:
                        vector_data[current_vector][file_idx-1] = 1

    # 6. Save updated vectors (Sorted alphabetically so they are easy to read)
    with open(output_file, "w") as f:
        f.write("# Persistent Category Occurrences\n\n")
        for vec in sorted(vector_data.keys()):
            f.write(f"{vec} = {vector_data[vec]}\n")

# --- Optimized Execution Loop ---
script_dir = Path(__file__).parent
category_label = "algorithm_mention"
phrases = ["DFS", "BFS", "Breadth-First", "Depth-First", "dictionary", 
           "visited", "queue", "queuing", "dequeuing", "enqueuing", "parent"]

# Instead of listing 30 files, we use a loop to find them all
for k in range(1, 31):
    # This searches for the coords file for each index 1-30
    file_path = script_dir / "Dataset 03" / f"Dataset 03 15x15 {k}" / f"comparison_report_reasoning_coords_{k}.md"
    
    if file_path.exists():
        print(f"Analyzing File {k} for {category_label}...")
        keyword_search(file_path, phrases, category_label)

print("Processing Complete.")


# --- Example Run ---
script_dir = Path(__file__).parent


# files to test. This list can now contain any mixture of ego, allo, or coords files


files = [
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
    
]
categories = "algorithm_mention"
phrases = ["DFS", "BFS", "dfs", "bfs", "Breadth-First", "Depth-First", "breadth-first", "depth-first", 
           "dictionary", "visited", "queue", "queuing", "dequeuing", "enqueuing", "parent" ]
category = 'algorithm_naming'
for f in files:
    if f.exists():
        keyword_search(f, phrases, categories)