import re

def extract_prompt_token_count(text: str) -> str: 
    """
    Extracts the sequence of moves from the LLM's response after "prompt_token_count=' marker.

    Args:
        text (str): The full response from the LLM.

    Returns:
        text (str): number of output tokens
    """

    match = re.search(r"prompt_token_count\s*=\s*(\d+)", text)
    count= match.group(1).strip()
    if match:
        return count
    return "" # Return whitespace if none is found to avoid error



def extract_output_token_count(text: str, prompt_token_count) -> tuple: 
    """
    Extracts the sequence of moves from the LLM's response after "total_token_count=' marker.

    Args:
        text (str): The full response from the LLM.

    Returns:
        tuple: a tuple of two strings (str, str)
    """
    
    match1 = re.search(r"total_token_count\s*=\s*(\d+)", text) 
    count = match1.group(1).strip()
    number_of_output_tokens = str(int(count) - int(prompt_token_count) )
    if match1:
        return count, number_of_output_tokens
    return "" # Return whitespace if none is found to avoid error

def extract_final_answer_token_count(text: str) -> str: 
    """
    Extracts the sequence of moves from the LLM's response between the
    "Final answer:" and "End of final sequence" markers.

    Args:
        text (str): The full response from the LLM.

    Returns:
        tuple: a tuple of two strings (str, str)
    """
    
    match1 = re.search(r"candidates_token_count\s*=\s*(\d+)", text) 
    count = match1.group(1).strip()
    if match1:
        return count
    return "" # Return whitespace if none is found to avoid error

# Below is a code that must be run on its own bc it has a main(). It extracts the token output count from .md files. 

"""
extract_outputs.py

Searches files:
  ./Dataset02 - Statistical analysis/Dataset02 5x5 {i}/comparison_results_reasoning_ego_{i}.md
for i in 1..30 and extracts the first occurrence of the pattern:
  ", ouput: {number}`"
The extracted {number} is saved into a numpy array at index i-1.

Output:
  - prints the final array to terminal
"""

from pathlib import Path
import re
import numpy as np
import sys

# Regex:
#   looks for ", output: <number>`"
#   supports integer, decimal, and scientific notation (e.g. 1.23e-4)
RE_OUTPUT = re.compile(r",\s*ouput:\s(.*?)`")

# number of files
N = 30

def main():
    # Determine base directory (script location if available, else cwd)
    try:
        base_dir = Path(__file__).parent
    except NameError:
        base_dir = Path.cwd()

    results = np.full(N, np.nan, dtype=float)

    for i in range(1, N + 1):
        rel_path = Path("Dataset 02 - Statistical analysis") / f"Dataset 02 5x5 {i}" / f"comparison_results_nonreasoning_coords_{i}.md"
        file_path = (base_dir / rel_path).resolve()

        if not file_path.exists():
            print(f"[WARN] File not found for i={i}: {file_path}", file=sys.stderr)
            continue

        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"[ERROR] Could not read file for i={i}: {file_path} -> {e}", file=sys.stderr)
            continue

        m = RE_OUTPUT.search(text)
        if m:
            num_str = m.group(1)
            try:
                value = float(num_str)
                results[i - 1] = value
                print(f"[OK] i={i}: extracted {value}")
            except ValueError:
                print(f"[WARN] i={i}: found numeric string but failed to parse: '{num_str}'", file=sys.stderr)
        else:
            print(f"[WARN] i={i}: pattern not found in file: {file_path}", file=sys.stderr)

    # Final array
    print("\nFinal NumPy array (length = {}):".format(N))
    print(results)


if __name__ == "__main__":
    main()

















# DO NOT DELETE CODE BELOW. 
    # If you want to extract the number of thoughts tokens from .md files: use the code below!! Mute everything above. 


# import numpy as np
# import re
# import ast
# import os
# from pathlib import Path

# def extract_thought_tokens(md_filepath, vector_size):
#     output_file = "thought_token_count.py"
    
#     # 1. Extract mode and index from filename
#     filename = Path(md_filepath).name
#     match = re.search(r'reasoning_(ego|allo|coords)_(\d+)\.md$', filename)
#     if not match:
#         print(f"Skipping {md_filepath}: Filename pattern not matched.")
#         return
    
#     file_mode = match.group(1) 
#     file_idx = int(match.group(2))
#     required_size = max(vector_size, file_idx)

#     # 2. Define templates (using 'tokens' as the category label)
#     base_templates = [
#         "line_R_{mode}_adj_json_reasoning_tokens_15", "line_R_{mode}_adj_txt_reasoning_tokens_15", "line_R_{mode}_jpg_reasoning_tokens_15", 
#         "line_R_{mode}_json_reasoning_tokens_15", "line_R_{mode}_tokenized_txt_reasoning_tokens_15", "occupancy_R_{mode}_adj_json_reasoning_tokens_15", 
#         "occupancy_R_{mode}_adj_txt_reasoning_tokens_15", "occupancy_R_{mode}_ascii_txt_reasoning_tokens_15", "occupancy_R_{mode}_jpg_reasoning_tokens_15", 
#         "occupancy_R_{mode}_json_reasoning_tokens_15", "occupancy_R_{mode}_tokenized_txt_reasoning_tokens_15"
#     ]

#     all_modes = ['ego', 'allo', 'coords']
#     all_target_vectors = []
#     for m in all_modes:
#         all_target_vectors.extend([template.format(mode=m) for template in base_templates])

#     # 3. Load existing vectors from the output file
#     vector_data = {vec: [0] * required_size for vec in all_target_vectors}
#     if os.path.exists(output_file):
#         try:
#             with open(output_file, "r") as f:
#                 content = f.read()
#                 existing_vars = re.findall(r"(\w+)\s*=\s*(\[.*?\])", content, re.DOTALL)
#                 for var_name, var_value in existing_vars:
#                     val = ast.literal_eval(var_value)
#                     if len(val) < required_size:
#                         val.extend([0] * (required_size - len(val)))
#                     vector_data[var_name] = val
#         except Exception as e:
#             print(f"Error loading existing vectors: {e}")

#     # 4. Mapping helper (matches headers to vector names)
#     def get_vector_name(header_str, mode):
#         h = header_str.lower().strip("`# ")
#         prefix = f"line_R_{mode}" if "line" in h else f"occupancy_R_{mode}"
        
#         if "adj" in h and "json" in h: subtype = "adj_json"
#         elif "adj" in h and "txt" in h: subtype = "adj_txt"
#         elif "tokenized" in h: subtype = "tokenized_txt"
#         elif "ascii" in h: subtype = "ascii_txt"
#         elif "json" in h: subtype = "json"
#         elif "jpg" in h: subtype = "jpg"
#         else: subtype = None
        
#         return f"{prefix}_{subtype}_tokens_15" if subtype else None

#     # 5. Parsing logic
#     with open(md_filepath, "r", encoding="utf-8") as f:
#         full_content = f.read()

#     # Split by representation headers (###)
#     sections = re.split(r'(?m)^###\s*', full_content)
    
#     # Regex to find the token count within the Metadata block
#     # Looks for **Metadata:** followed by thoughts_token_count=VALUE
#     token_pattern = re.compile(r'\*\*Metadata:\*\*.*?thoughts_token_count=(\d+)', re.DOTALL | re.IGNORECASE)

#     for section in sections[1:]: 
#         lines = section.split('\n')
#         if not lines: continue
        
#         header_line = lines[0]
#         current_vector = get_vector_name(header_line, file_mode)
        
#         if not current_vector:
#             continue

#         match_token = token_pattern.search(section)
#         if match_token:
#             count = int(match_token.group(1))
            
#             # Ensure vector is ready for this index
#             if current_vector not in vector_data:
#                 vector_data[current_vector] = [0] * required_size
#             while len(vector_data[current_vector]) < file_idx:
#                 vector_data[current_vector].append(0)

#             # Save the count (Overwrite or add? Here we set the value for that specific file index)
#             vector_data[current_vector][file_idx-1] = count

#     # 6. Save updated vectors
#     with open(output_file, "w") as f:
#         f.write("# Thought Token Counts\n\n")
#         for vec in sorted(vector_data.keys()):
#             f.write(f"{vec} = {vector_data[vec]}\n")

# # --- Example Run ---
# if __name__ == "__main__":
#     script_dir = Path(__file__).parent 
#     # Adjust paths as necessary
#     files = [ 
#         script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_coords_1.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_coords_2.md",
#     ]

#     for f in files:
#         if f.exists():
#             extract_thought_tokens(f, vector_size=len(files))
#             print(f"Processed {f.name}. Tokens saved to thought_token_count.py.")
#         else:
#             print(f"File not found: {f}")









#     files = [ # wATCH OUT with adding files when count vectors already exists. Rerunning adds to existing vectors and does not reset them.
#         script_dir / "Dataset 03" / "Dataset 03 15x15 1" / "comparison_report_reasoning_ego_1.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 2" / "comparison_report_reasoning_ego_2.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 3" / "comparison_report_reasoning_ego_3.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 4" / "comparison_report_reasoning_ego_4.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 5" / "comparison_report_reasoning_ego_5.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 6" / "comparison_report_reasoning_ego_6.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 7" / "comparison_report_reasoning_ego_7.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 8" / "comparison_report_reasoning_ego_8.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 9" / "comparison_report_reasoning_ego_9.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 10" / "comparison_report_reasoning_ego_10.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 11" / "comparison_report_reasoning_ego_11.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 12" / "comparison_report_reasoning_ego_12.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 13" / "comparison_report_reasoning_ego_13.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 14" / "comparison_report_reasoning_ego_14.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 15" / "comparison_report_reasoning_ego_15.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 16" / "comparison_report_reasoning_ego_16.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 17" / "comparison_report_reasoning_ego_17.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 18" / "comparison_report_reasoning_ego_18.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 19" / "comparison_report_reasoning_ego_19.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 20" / "comparison_report_reasoning_ego_20.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 21" / "comparison_report_reasoning_ego_21.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 22" / "comparison_report_reasoning_ego_22.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 23" / "comparison_report_reasoning_ego_23.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 24" / "comparison_report_reasoning_ego_24.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 25" / "comparison_report_reasoning_ego_25.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 26" / "comparison_report_reasoning_ego_26.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 27" / "comparison_report_reasoning_ego_27.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 28" / "comparison_report_reasoning_ego_28.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 29" / "comparison_report_reasoning_ego_29.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 30" / "comparison_report_reasoning_ego_30.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 31" / "comparison_report_reasoning_ego_31.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 32" / "comparison_report_reasoning_ego_32.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 33" / "comparison_report_reasoning_ego_33.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 34" / "comparison_report_reasoning_ego_34.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 35" / "comparison_report_reasoning_ego_35.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 36" / "comparison_report_reasoning_ego_36.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 37" / "comparison_report_reasoning_ego_37.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 38" / "comparison_report_reasoning_ego_38.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 39" / "comparison_report_reasoning_ego_39.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 40" / "comparison_report_reasoning_ego_40.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 41" / "comparison_report_reasoning_ego_41.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 42" / "comparison_report_reasoning_ego_42.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 43" / "comparison_report_reasoning_ego_43.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 44" / "comparison_report_reasoning_ego_44.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 45" / "comparison_report_reasoning_ego_45.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 46" / "comparison_report_reasoning_ego_46.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 47" / "comparison_report_reasoning_ego_47.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 48" / "comparison_report_reasoning_ego_48.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 49" / "comparison_report_reasoning_ego_49.md",
#         script_dir / "Dataset 03" / "Dataset 03 15x15 50" / "comparison_report_reasoning_ego_50.md",
# ]



# for f in files:
#     if f.exists():
#         extract_thought_tokens(f, vector_size=len(files))

