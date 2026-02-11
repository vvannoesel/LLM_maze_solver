

import os
import re
import numpy as np
from pathlib import Path

def keyword_search(md_filepath, search_phrases, vector_size=30):
    output_file = "category_occurrences.py"
    
    # 1. Extract mode and index from filename
    # Matches "..._ego_11.md", "..._coords_12.md", etc.
    match = re.search(r'reasoning_(ego|allo|coords)_(\d+)\.md$', str(md_filepath))
    if not match:
        print(f"Skipping {md_filepath}: Could not find mode (ego/allo/coords) or index.")
        return
    
    file_mode = match.group(1) # 'ego', 'allo', or 'coords'
    file_idx = int(match.group(2))

    # 2. Define the base names for the 11 categories
    base_categories = [
        "line_R_{mode}_adj_json_15", "line_R_{mode}_adj_txt_15", "line_R_{mode}_jpg_15", 
        "line_R_{mode}_json_15", "line_R_{mode}_tokenized_txt_15", "occupancy_R_{mode}_adj_json_15", 
        "occupancy_R_{mode}_adj_txt_15", "occupancy_R_{mode}_ascii_txt_15", "occupancy_R_{mode}_jpg_15", 
        "occupancy_R_{mode}_json_15", "occupancy_R_{mode}_tokenized_txt_15"
    ]

    # Generate all 33 possible target vectors (11 for each mode) to ensure persistence
    all_modes = ['ego', 'allo', 'coords']
    all_target_vectors = []
    for m in all_modes:
        all_target_vectors.extend([template.format(mode=m) for template in base_categories])

    # 3. Load existing vectors from the file
    vector_data = {vec: [0] * vector_size for vec in all_target_vectors}
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            content = f.read()
            for vec in all_target_vectors:
                list_match = re.search(fr"{vec}\s*=\s*(\[.*?\])", content, re.DOTALL)
                if list_match:
                    try:
                        vector_data[vec] = eval(list_match.group(1))
                    except:
                        pass

    # 4. Helper to map MD headers to Vector Names using the detected mode
    def get_vector_name(header_str, mode):
        h = header_str.lower().strip("` ")
        # Prefix now dynamically includes the mode from the filename
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
        return f"{prefix}_{subtype}_15"

    # 5. Parsing the File
    current_vector = None
    in_internal_thoughts = False
    
    with open(md_filepath, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            
            # Start of a new category (e.g., ### `maze_line_...`)
            if clean_line.startswith("###"):
                header_val = clean_line.replace("###", "").strip()
                current_vector = get_vector_name(header_val, file_mode)
                in_internal_thoughts = False
                continue
            
            # Start of thoughts
            if clean_line == "**Internal Thoughts:**":
                in_internal_thoughts = True
                continue
            
            # Stop at the specific "Unfiltered Response" section
            if in_internal_thoughts and clean_line.startswith("**Unfiltered Response:**"):
                in_internal_thoughts = False
                continue
            
            # Search phrases within the specific section
            if in_internal_thoughts and current_vector:
                if any(phrase.lower() in clean_line.lower() for phrase in search_phrases):
                    if current_vector in vector_data:
                        # Indexing logic: File 11 -> Index 10
                        vector_data[current_vector][file_idx-1] = 1

    # 6. Save updated vectors back to the .py file
    with open(output_file, "w") as f:
        f.write("# Persistent Category Occurrences\n\n")
        # Sort keys to keep the file organized (allo, then coords, then ego)
        for vec in sorted(vector_data.keys()):
            f.write(f"{vec} = {vector_data[vec]}\n")

# --- Example Run ---
script_dir = Path(__file__).parent
phrases = ["mistake"]

# This list can now contain any mixture of ego, allo, or coords files


files = [
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_1.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_2.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_3.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_4.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_5.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_6.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_7.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_8.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_9.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_10.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_12.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_13.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_14.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_15.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_16.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_17.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_18.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_19.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_20.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_21.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_22.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_23.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_24.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_25.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_26.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_27.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_28.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_coords_29.md",
    script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_30.md",
    
]

for f in files:
    if f.exists():
        keyword_search(f, phrases)