"""
@author: Gemini 2.5 Pro, 8 October 16:20:04 2025
This script stores the scores from tesT.py and tesT_2.py in a numpy array in a file called 'scores_nonreasoning_Dataset01.py.
These arrays can be used to create charts.
The score is saved to an array with a name similar to the tested file's name. 
The score is saved to the [row-2]'nd index of the array, so a 2x2 maze score is saved on the 0th index, 3x3 score on the 1st index, etc.
"""

import numpy as np
from pathlib import Path
import re
import os


def save_score(filename: str, score: float, output_file: str = 'scores_nonreasoning_Dataset01.py'):
    """
    Parses a maze filename to update a specific NumPy array with a new score.

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
    current_array[index] = score
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

