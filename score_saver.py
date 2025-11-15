"""
@author: Gemini 2.5 Pro, 8 October 16:20:04 2025
This script stores the scores from tesT.py and tesT_2.py in a numpy array in a file called 'scores_Dataset01.py.
These arrays can be used to create charts.
The score is saved to an array with a name similar to the tested file's name. 
The score is saved to the [row-2]'nd index of the array, so a 2x2 maze score is saved on the 0th index, 3x3 score on the 1st index, etc.
"""

import numpy as np
from pathlib import Path
import re
import os


def export_output_tokens(filename: str, output_tokens: int, output_file: str = 'output_tokens_Dataset03_3x3.py'):
    """
    Parses a maze filename to update a specific NumPy array with a new output token count.
    The index of the score in the score tensor is based on the trailing 
    number in the filename (e.g., 'maze_..._adj_3.txt' -> index 2).

    The function determines the correct array and the correct index within that
    array based on the filename. It reads all existing arrays from the output
    file, updates the data in memory, and writes the complete dataset back.

    Args:
        filename (str): The name of the maze file that was scored.
                        e.g., 'maze_line_3x3_adj_1.txt' or 'maze_line_3x3_3.json'
        output_tokens (int): The score to save.
        output_file (str): The path to the .py file where score arrays are stored.
    """
    # --- 1. Parse the filename to get array name and index ---
    
    # This regex captures the key parts of the filename to create a unique variable name
    # It captures: 1: type, 2: rows, 3: representation (optional), 4: index_num (i), 5: extension
    pattern = r"maze_(line|occupancy)_(\d+)x\d+(?:_(none|tokenized|ascii|adj))?_(\d+)\.(jpg|json|txt)"
    match = re.match(pattern, os.path.basename(filename))

    if not match:
        print(f"Warning: Filename '{filename}' did not match expected pattern (e.g., ..._adj_3.txt). Skipping.")
        return

    # Unpack all groups
    type_str, rows_str, representation_str, i_str, extension_str = match.groups()
    
    # If the representation part is missing in the filename, default to 'none'.
    # This handles cases like 'maze_line_3x3_3.jpg'.
    if representation_str is None:
        # representation_str = 'none'
        array_name = f"{type_str}_{extension_str}_output_tokens"
    else:
        # Create a unique and valid Python variable name
        # e.g., 'line_adj_txt', 'occupancy_tokenized_json'
        array_name = f"{type_str}_{representation_str}_{extension_str}_output_tokens"
    
    # Determine the index based on the {i} part (e.g., _3 -> index 2)
    try:
        i_val = int(i_str)
        if i_val < 1: # Assuming 'i' must be at least 1
            print(f"Warning: Filename index part '{i_val}' must be 1 or greater. Skipping.")
            return
        index = i_val - 1  # New indexing logic
    except ValueError:
        print(f"Error: Could not parse index from '{i_str}'. Skipping.")
        return

    # --- 2. Load existing scores from the output file ---
    tokens_data = {}
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                content = f.read()
                # Find all array assignments in the file
                # This regex is robust to whitespace variations
                found_arrays = re.findall(r"(\w+)\s*=\s*np\.array\(\[([^\]]*)\]\)", content)
                for name, values_str in found_arrays:
                    if values_str:
                        # Convert the string of values into a list of floats, handling 'nan'
                        values = [float(v.strip()) for v in values_str.split(',') if v.strip()]
                        tokens_data[name] = values
                    else:
                        tokens_data[name] = []
        except Exception as e:
            print(f"Error reading or parsing {output_file}: {e}")
            return

    # --- 3. Update the specific score array in memory ---
    
    # Get the current list of scores for our array, or an empty list if it's new
    current_array = tokens_data.get(array_name, [])
    
    # Ensure the array is long enough to place the score at the new index
    # If the new index is beyond the current end, pad with np.nan
    if len(current_array) <= index:
        padding_size = index - len(current_array) + 1
        current_array.extend([np.nan] * padding_size)
    
    # Place the new score at the correct index
    current_array[index] = output_tokens
    tokens_data[array_name] = current_array

    # --- 4. Write all updated data back to the file ---
    try:
        with open(output_file, 'w') as f:
            f.write("import numpy as np\n\n")
            # Sort the keys to ensure the file order is consistent every time
            for name in sorted(tokens_data.keys()):
                # The str() of a list containing np.nan will correctly produce 'nan'
                f.write(f"{name} = np.array({tokens_data[name]})\n")
        
        print(f"Saved score {output_tokens:.2f} for '{filename}' to '{array_name}' at index {index}.")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")


def export_prompt_tokens(filename: str, prompt_tokens: int, output_file: str = 'prompt_tokens_Dataset03_3x3.py'):
    """
    Parses a maze filename to update a specific NumPy array with a new prompt token count.
    The index of the score in the score tensor is based on the trailing 
    number in the filename (e.g., 'maze_..._adj_3.txt' -> index 2).

    The function determines the correct array and the correct index within that
    array based on the filename. It reads all existing arrays from the output
    file, updates the data in memory, and writes the complete dataset back.

    Args:
        filename (str): The name of the maze file that was scored.
                        e.g., 'maze_line_3x3_adj_1.txt' or 'maze_line_3x3_3.json'
        prompt_tokens (int): The score to save.
        output_file (str): The path to the .py file where score arrays are stored.
    """
    # --- 1. Parse the filename to get array name and index ---
    
    # This regex captures the key parts of the filename to create a unique variable name
    # It captures: 1: type, 2: rows, 3: representation (optional), 4: index_num (i), 5: extension
    pattern = r"maze_(line|occupancy)_(\d+)x\d+(?:_(none|tokenized|ascii|adj))?_(\d+)\.(jpg|json|txt)"
    match = re.match(pattern, os.path.basename(filename))

    if not match:
        print(f"Warning: Filename '{filename}' did not match expected pattern (e.g., ..._adj_3.txt). Skipping.")
        return

    # Unpack all groups
    type_str, rows_str, representation_str, i_str, extension_str = match.groups()
    
    # If the representation part is missing in the filename, default to 'none'.
    # This handles cases like 'maze_line_3x3_3.jpg'.
    if representation_str is None:
        # representation_str = 'none'
        array_name = f"{type_str}_{extension_str}_input_tokens"
    else:
        # Create a unique and valid Python variable name
        # e.g., 'line_adj_txt', 'occupancy_tokenized_json'
        array_name = f"{type_str}_{representation_str}_{extension_str}_input_tokens"
    
    # Determine the index based on the {i} part (e.g., _3 -> index 2)
    try:
        i_val = int(i_str)
        if i_val < 1: # Assuming 'i' must be at least 1
            print(f"Warning: Filename index part '{i_val}' must be 1 or greater. Skipping.")
            return
        index = i_val - 1  # New indexing logic
    except ValueError:
        print(f"Error: Could not parse index from '{i_str}'. Skipping.")
        return

    # --- 2. Load existing scores from the output file ---
    tokens_data = {}
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                content = f.read()
                # Find all array assignments in the file
                # This regex is robust to whitespace variations
                found_arrays = re.findall(r"(\w+)\s*=\s*np\.array\(\[([^\]]*)\]\)", content)
                for name, values_str in found_arrays:
                    if values_str:
                        # Convert the string of values into a list of floats, handling 'nan'
                        values = [float(v.strip()) for v in values_str.split(',') if v.strip()]
                        tokens_data[name] = values
                    else:
                        tokens_data[name] = []
        except Exception as e:
            print(f"Error reading or parsing {output_file}: {e}")
            return

    # --- 3. Update the specific score array in memory ---
    
    # Get the current list of scores for our array, or an empty list if it's new
    current_array = tokens_data.get(array_name, [])
    
    # Ensure the array is long enough to place the score at the new index
    # If the new index is beyond the current end, pad with np.nan
    if len(current_array) <= index:
        padding_size = index - len(current_array) + 1
        current_array.extend([np.nan] * padding_size)
    
    # Place the new score at the correct index
    current_array[index] = prompt_tokens
    tokens_data[array_name] = current_array

    # --- 4. Write all updated data back to the file ---
    try:
        with open(output_file, 'w') as f:
            f.write("import numpy as np\n\n")
            # Sort the keys to ensure the file order is consistent every time
            for name in sorted(tokens_data.keys()):
                # The str() of a list containing np.nan will correctly produce 'nan'
                f.write(f"{name} = np.array({tokens_data[name]})\n")
        
        print(f"Saved score {prompt_tokens:.2f} for '{filename}' to '{array_name}' at index {index}.")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")





def export_score(filename: str, score: float, output_file: str = 'scores_Dataset03_3x3.py'):
    """
    Parses a maze filename to update a specific NumPy array with a new score.
    The index of the score in the score tensor is based on the trailing 
    number in the filename (e.g., 'maze_..._adj_3.txt' -> index 2).

    The function determines the correct array and the correct index within that
    array based on the filename. It reads all existing arrays from the output
    file, updates the data in memory, and writes the complete dataset back.

    Args:
        filename (str): The name of the maze file that was scored.
                        e.g., 'maze_line_3x3_adj_1.txt' or 'maze_line_3x3_3.json'
        score (float): The score to save.
        output_file (str): The path to the .py file where score arrays are stored.
    """
    # --- 1. Parse the filename to get array name and index ---
    
    # This regex captures the key parts of the filename to create a unique variable name
    # It captures: 1: type, 2: rows, 3: representation (optional), 4: index_num (i), 5: extension
    pattern = r"maze_(line|occupancy)_(\d+)x\d+(?:_(none|tokenized|ascii|adj))?_(\d+)\.(jpg|json|txt)"
    match = re.match(pattern, os.path.basename(filename))

    if not match:
        print(f"Warning: Filename '{filename}' did not match expected pattern (e.g., ..._adj_3.txt). Skipping.")
        return

    # Unpack all groups
    type_str, rows_str, representation_str, i_str, extension_str = match.groups()
    
    # If the representation part is missing in the filename, default to 'none'.
    # This handles cases like 'maze_line_3x3_3.jpg'.
    if representation_str is None:
        # representation_str = 'none'
        array_name = f"{type_str}_{extension_str}"
    else:
        # Create a unique and valid Python variable name
        # e.g., 'line_adj_txt', 'occupancy_tokenized_json'
        array_name = f"{type_str}_{representation_str}_{extension_str}"
    
    # Determine the index based on the {i} part (e.g., _3 -> index 2)
    try:
        i_val = int(i_str)
        if i_val < 1: # Assuming 'i' must be at least 1
            print(f"Warning: Filename index part '{i_val}' must be 1 or greater. Skipping.")
            return
        index = i_val - 1  # New indexing logic
    except ValueError:
        print(f"Error: Could not parse index from '{i_str}'. Skipping.")
        return

    # --- 2. Load existing scores from the output file ---
    scores_data = {}
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                content = f.read()
                # Find all array assignments in the file
                # This regex is robust to whitespace variations
                found_arrays = re.findall(r"(\w+)\s*=\s*np\.array\(\[([^\]]*)\]\)", content)
                for name, values_str in found_arrays:
                    if values_str:
                        # Convert the string of values into a list of floats, handling 'nan'
                        values = [float(v.strip()) for v in values_str.split(',') if v.strip()]
                        scores_data[name] = values
                    else:
                        scores_data[name] = []
        except Exception as e:
            print(f"Error reading or parsing {output_file}: {e}")
            return

    # --- 3. Update the specific score array in memory ---
    
    # Get the current list of scores for our array, or an empty list if it's new
    current_array = scores_data.get(array_name, [])
    
    # Ensure the array is long enough to place the score at the new index
    # If the new index is beyond the current end, pad with np.nan
    if len(current_array) <= index:
        padding_size = index - len(current_array) + 1
        current_array.extend([np.nan] * padding_size)
    
    # Place the new score at the correct index
    current_array[index] = score * 100
    scores_data[array_name] = current_array

    # --- 4. Write all updated data back to the file ---
    try:
        with open(output_file, 'w') as f:
            f.write("import numpy as np\n\n")
            # Sort the keys to ensure the file order is consistent every time
            for name in sorted(scores_data.keys()):
                # The str() of a list containing np.nan will correctly produce 'nan'
                f.write(f"{name} = np.array({scores_data[name]})\n")
        
        print(f"Saved score {score:.2f} for '{filename}' to '{array_name}' at index {index}.")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")









# ----------------------------------------------------------------------------------------------------------------------

import numpy as np
from pathlib import Path
import re
import os


def save_score(filename: str, score: float, output_file: str = 'scores_Dataset03.py'):
    """
    Parses a maze filename to update a specific NumPy array with a new score.
    The index of the score in the score tensor is based on maze complexity (eg. [2x2, 3x3, 4x4, 5x5, 6x6, etc])

    The function determines the correct array and the correct index within that
    array based on the filename. It reads all existing arrays from the output
    file, updates the data in memory, and writes the complete dataset back.

    Args:
        filename (str): The name of the maze file that was scored.
                        e.g., 'maze_line_3x3_none.jpg' or 'maze_line_3x3.jpg'
        score (float): The score to save.
        output_file (str): The path to the .py file where score arrays are stored.
    """
    # --- 1. Parse the filename to get array name and index ---
    
    # This regex captures the key parts of the filename to create a unique variable name
    # It captures: 1: type, 2: rows, 3: representation (optional), 4: extension
    pattern = r"maze_(line|occupancy)_(\d+)x\d+(?:_(none|tokenized|ascii|adj))?\.(jpg|json|txt)"
    match = re.match(pattern, os.path.basename(filename))

    if not match:
        print(f"Warning: Filename '{filename}' did not match expected pattern. Skipping.")
        return

    type_str, rows_str, representation_str, extension_str = match.groups()
    
    # If the representation part is missing in the filename, default to 'none'.
    # This handles cases like 'maze_line_3x3.jpg'.
    if representation_str is None:
        # representation_str = 'none'
        array_name = f"{type_str}_{extension_str}"
    else:
        # Create a unique and valid Python variable name
        # e.g., 'line_none_jpg', 'occupancy_tokenized_json'
        array_name = f"{type_str}_{representation_str}_{extension_str}"
    
    # Determine the index based on the number of rows (e.g., 2 rows -> index 0)
    try:
        maze_rows = int(rows_str)
        if maze_rows < 2:
            print(f"Warning: Maze rows must be 2 or greater. Found {maze_rows}. Skipping.")
            return
        index = maze_rows - 2
    except ValueError:
        print(f"Error: Could not parse rows from '{rows_str}'. Skipping.")
        return

    # --- 2. Load existing scores from the output file ---
    scores_data = {}
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                content = f.read()
                # Find all array assignments in the file
                # This regex is robust to whitespace variations
                found_arrays = re.findall(r"(\w+)\s*=\s*np\.array\(\[([^\]]*)\]\)", content)
                for name, values_str in found_arrays:
                    if values_str:
                        # Convert the string of values into a list of floats, handling 'nan'
                        values = [float(v.strip()) for v in values_str.split(',') if v.strip()]
                        scores_data[name] = values
                    else:
                        scores_data[name] = []
        except Exception as e:
            print(f"Error reading or parsing {output_file}: {e}")
            return

    # --- 3. Update the specific score array in memory ---
    
    # Get the current list of scores for our array, or an empty list if it's new
    current_array = scores_data.get(array_name, [])
    
    # Ensure the array is long enough to place the score at the new index
    # If the new index is beyond the current end, pad with np.nan
    if len(current_array) <= index:
        padding_size = index - len(current_array) + 1
        current_array.extend([np.nan] * padding_size)
    
    # Place the new score at the correct index
    current_array[index] = score * 100
    scores_data[array_name] = current_array

    # --- 4. Write all updated data back to the file ---
    try:
        with open(output_file, 'w') as f:
            f.write("import numpy as np\n\n")
            # Sort the keys to ensure the file order is consistent every time
            for name in sorted(scores_data.keys()):
                # The str() of a list containing np.nan will correctly produce 'nan'
                f.write(f"{name} = np.array({scores_data[name]})\n")
        
        print(f"Saved score {score:.2f} for '{filename}' to '{array_name}' at index {index}.")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")


#----------------------------------------------------------------------------------------------------------------------------------------------------

"""
@author: Gemini 2.5 Pro, 8 October 16:20:04 2025
This script stores the scores from tesT.py and tesT_2.py in a numpy array in a file called 'scores_Dataset01.py.
These arrays can be used to create charts.
The score is saved to an array with a name similar to the tested file's name. 
The score is saved to the [row-2]'nd index of the array, so a 2x2 maze score is saved on the 0th index, 3x3 score on the 1st index, etc.
"""

from pathlib import Path
import os
import re
import runpy
import numpy as np

def collect_and_save_scores(filename: str, score: float, output_file: str = 'scores_Dataset03.py'):
    """
    Update (or create) a NumPy array of scores stored in a Python file.
    Each call updates a single index (derived from the filename) while preserving
    any previously stored values.
    This function only works if 1 maze representation is used. 

    Args:
        filename (str): e.g. 'maze_line_5x5_ascii_4.txt'
        score (float): score to store at the index (maze_number - 1)
        output_file (str): file to save the scores in (Python file). Default 'scores_Dataset03.py', can change in function def

    Returns:
        np.ndarray: the updated scores array
    """
    # Extract maze number from filename
    match = re.search(r"maze_line_5x5_ascii_(\d+)\.txt", filename)
    if not match:
        raise ValueError(f"Filename '{filename}' does not match the expected pattern.")
    maze_number = int(match.group(1))
    index = maze_number - 1  # 0-based index

    # Path to save the score file (same directory as this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = Path(script_dir) / output_file

    # Default size (30) but we'll allow expansion if needed
    min_size = 30

    # Load existing scores by executing the Python file (avoids import caching)
    scores = None
    if output_path.exists():
        try:
            loaded = runpy.run_path(str(output_path))
            existing = loaded.get("scores", None)
            if existing is None:
                # No 'scores' variable in file
                scores = np.full(min_size, np.nan)
            else:
                # Convert existing to numpy array
                scores = np.array(existing, dtype=float)
        except Exception as e:
            # If anything goes wrong, start with NaNs but warn user
            print(f"Warning: could not load existing scores from {output_path}: {e}")
            scores = np.full(min_size, np.nan)
    else:
        # File doesn't exist yet
        scores = np.full(min_size, np.nan)

    # Ensure array is big enough for the index
    required_size = max(min_size, index + 1, scores.size)
    if scores.size < required_size:
        new_scores = np.full(required_size, np.nan)
        new_scores[:scores.size] = scores
        scores = new_scores

    # Update the index
    scores[index] = float(score*100) # make score into a percentage

    # Write the Python file so it can be reloaded later
    # Use np.nan for NaN values so the file is valid Python
    entries = []
    for v in scores:
        if np.isnan(v):
            entries.append("np.nan")
        else:
            # Use repr(float(v)) to ensure numeric literal (e.g. 8.25, 10.0)
            entries.append(repr(float(v)))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("import numpy as np\n")
        f.write("scores = np.array([" + ", ".join(entries) + "], dtype=float)\n")

    print(f"Score for maze {maze_number} saved at index {index} in {output_path}")
    return scores


# collect_and_save_scores("maze_line_5x5_ascii_1.txt", 0.99)