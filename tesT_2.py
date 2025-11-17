"""
@author: valer and Gemini 2.5 Pro, 1 october 15:57:23 2025
This script generates a maze, prompts a large language model (LLM) to solve it
using various maze representations, compares the LLM's solutions to the
correct solution, and saves the results in a markdown file.
DOES include internal thought summary. use only for REASONING LLMS.
"""

import os
import re
import time
import base64 # converts binary data to ASCII string format and back
from pathlib import Path
# import google.generativeai as genai
from google import genai
from google.genai import types 
# from google.generativeai.types import Tool # old version of API SDK
from dotenv import load_dotenv
from PIL import Image
import PIL.Image
from maze_generator_ext_v3 import Maze, OccupancyGridMaze
from score_saver import save_score, collect_and_save_scores, export_score, export_output_tokens, export_prompt_tokens, export_raw_score
from token_count_extracter import extract_prompt_token_count, extract_output_token_count


# --- Configuration ---
MAZE_ROWS = 3
MAZE_COLS = 3
OCC_ROWS = MAZE_ROWS * 2 + 1  # Occupancy grid rows
OCC_COLS = MAZE_COLS * 2 + 1  # Occupancy grid columns
MODEL_NAME = "gemini-2.5-pro"

# # PROMPT 1: BEV
instructions_allo = ("Instructions:\n" \
    "1. You can only move up, down, left, or right.\n" \
    "2. You cannot move diagonally or through walls, only from one cell to an adjacent cell.\n" \
    "3. Your output must be a single, comma-separated sequence of steps. For example: up, down, right, right, down.\n" \
    "4. Provide only the final list of moves in your response.")

# PROMPT 2: EGO
instructions_ego = ("Instructions:\n" \
    "1. Give instructions to an agent in the maze. The agent begins by facing south. You can only use the following four actions:\n" \
    "Forward: this moves the agent 1 step in the direction it is facing.\n" \
    "Left: this turns the agent 90° to the left and then moves the agent 1 step in the new direction it is facing.\n" \
    "Right: this turns the agent 90° to the right and then moves the agent 1 step in the new direction it is facing.\n" \
    "Backward: this turns the agent 180° and then moves the agent 1 step in the new direction it is facing.\n" \
    "2. You cannot move diagonally or through walls, only from one cell to an adjacent cell.\n" \
    "3. Your output must be a single, comma-separated sequence of steps. For example: forward, left, right, forward, right.\n" \
    "4. Provide only the final list of instructions in your response.")


# PROMPT 3: COORDINATES
instructions_coords = ("Instructions:\n" \
    "1. You cannot move diagonally or through walls, only from one cell to an adjacent cell.\n" \
    "2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).\n" \
    "3. Provide only the final list of coordinates from start to end in your response." )


def setup_api_key():
    """
    Loads the Google API key from a .env file and configures the genai library.
    """
    load_dotenv()
    my_api_key = os.getenv("GEMINI_API_KEY")
    if not my_api_key:
        raise ValueError("API_KEY not found in .env file.")
    # genai.configure(api_key=my_api_key) # Old method of configuration. New method below in call_llm
    print("API key configured successfully.")
    return my_api_key

def import_maze_file() -> Path:
    """
    Imports a specific maze file from a subdirectory.

    Returns:
        Path: The path object for the maze file.
    
    Raises:
        FileNotFoundError: If the specified maze file does not exist.
    """
    try:
        # Construct the path relative to the script's directory
        script_dir = Path(__file__).parent
        file_path = script_dir / "Dataset 03" / f"Dataset 03 {MAZE_ROWS}x{MAZE_COLS} {i}" #/ "maze_line_3x3_ascii.txt"
        # file_path = script_dir / "Dataset 01" / f"Dataset 01 {MAZE_ROWS}x{MAZE_COLS}" #/ "maze_line_3x3_ascii.txt"
        # file_path  = script_dir / f"PROMPT TEST Dataset 01 {MAZE_ROWS}x{MAZE_COLS}"
        # file_path = script_dir / "Dataset 01" / "extra 20x20"
        # file_path = script_dir / "Dataset 02.1 - ASCII analysis" / f"Dataset 02.1 {MAZE_ROWS}x{MAZE_COLS} {i}"
        

        if not file_path.exists():
            raise FileNotFoundError(f"The specified maze file was not found at: {file_path}")
        
        print(f"Successfully found maze file: {file_path.name}")
        return file_path
    except Exception as e:
        print(f"An error occurred while trying to import the maze file: {e}")
        raise

def create_test_directory(): #this function is only needed when generating new mazes and saving them in a new directory and then prompting the LLM with those files
    """
    Creates a new, uniquely named directory to store maze files and results.

    Returns:
        Path: The path to the newly created directory.
    """
    base_name = "Test Maze gemini"
    i = 1
    while True:
        dir_path = Path(f"{base_name} {i}")
        if not dir_path.exists():
            dir_path.mkdir()
            print(f"Created directory: {dir_path}")
            return dir_path
        i += 1

def generate_and_save_mazes(directory: Path, cols: int, rows: int): #this function is only needed when generating new mazes and saving them in a new directory and then prompting the LLM with those files
    """
    Generates a maze and its occupancy grid version, then saves all
    representations to the specified directory.

    Args:
        directory (Path): The directory to save the files in.
        cols (int): The number of columns for the maze.
        rows (int): The number of rows for the maze.
    """
    print(f"--- Generating {cols}x{rows} Maze ---")
    line_maze = Maze(cols, rows)
    # occupancy_maze = OccupancyGridMaze(line_maze)
    print("Maze generation complete.")

    mazes_to_save = {
        "line": line_maze,
        # "occupancy": occupancy_maze
    }

    for name, maze_obj in mazes_to_save.items():
        prefix = directory / f"maze_{name}_{cols}x{rows}"
        # maze_obj.to_jpeg(f"{prefix}.jpg")
        # maze_obj.to_json(f"{prefix}.json")
        # maze_obj.to_adjacency_list(f"{prefix}_adj.json")
        # maze_obj.to_custom_adjacency_list(f"{prefix}_adj.txt")
        maze_obj.to_tokenized_representation(f"{prefix}_tokenized.txt")
        # with open(f"{prefix}_ascii.txt", "w", encoding="utf-8") as f:
        #     f.write(maze_obj.to_ascii())

        solution_steps = maze_obj.get_solution_steps()
        with open(f"{prefix}_solution_steps.txt", "w", encoding="utf-8") as f:
            f.write(", ".join(solution_steps))

    print(f"All maze representations saved to '{directory}'.")


def call_llm(prompt: str, file_path: Path, api_key: str) -> tuple[str, str , str, str]: # The first 2 values in the tuple are not str but GenerateContentResponse and CountTokensResponse.
    """
    Sends a prompt and a file to the model and returns the response and thoughts.

    Args:
        prompt (str): The prompt to send to the model.
        file_path (Path): The path to the file to be included in the prompt.

    Returns:
        tuple: A tuple containing the response metadata (str), total amount of tokens in the prompt (str), final text response (str) and internal thoughts (str). 
    """
    print(f"Querying LLM with: {file_path.name}...")
    try:
        # model = genai.GenerativeModel(MODEL_NAME)
        
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            # maze_input = Image.open(file_path)

            # Enable internal thoughts in the generation config
            # generation_config = genai.types.GenerationConfig(include_internal_texts=True)
            client = genai.Client(api_key=api_key)

            # Open the image file
            your_image_file = PIL.Image.open(file_path)

            # Count prompt tokens
            total_tokens = client.models.count_tokens(  # This only gives the prompt tokens, and calls it 'total_tokens' 
                model=MODEL_NAME, contents=[prompt, your_image_file])
            # print('count:', total_tokens )



            # Generate content and enable thinking
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=[prompt, your_image_file],
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(
                        include_thoughts=True
                    )
                )
            )
            # print('response metadata:', response.usage_metadata)  # the metadata shows token count of each input modality, and output. 

        else:
            with open(file_path, 'r', encoding='cp1252') as f:  #previously utf-8
                maze_input = f.read()

            

            # Enable internal thoughts in the generation config
            # generation_config = genai.types.GenerationConfig(include_internal_texts=True)
            client = genai.Client(api_key=api_key)

            # Count tokens using the new client method.
            total_tokens = client.models.count_tokens(
                model=MODEL_NAME, contents=prompt)
            
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=f'{maze_input}\n\n{prompt}',
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(
                        include_thoughts=True
                    )
                )
            )
        # Initialize variables with a default value so they exist in the error case
        thought_summary = ""
        final_answer = ""
        # Extract internal thoughts if available
        for part in response.candidates[0].content.parts: # the response object is a container for candidates, each candidate has content, which has parts
            if not part.text:   # skip any empty or non-text parts
                continue
            if part.thought:    # check if the part has a thought associated with it. If so, it's an internal thought
                thought_summary = part.text
            else:               # if there's no thought, it's the final answer
                final_answer = part.text

        return response, total_tokens, final_answer, thought_summary # return both final answer and internal thoughts as a tuple

    except Exception as e:
        print(f"An error occurred while calling the API: {e}")
        error_message = f"Error: Could not get a response from the LLM. Details: {e}"
        # Return a tuple in the error case as well for consistency
        return error_message, "Error during API call."


# -------------- All functions below are specifically for parsing and scoring solution STEPS outputted by an LLM. --------------
def extract_final_answer_steps(text: str) -> list: # this function works but it extracts the final answer from a larger text block (unnecessary). It uses markers to find the solution steps.
    """
    Extracts the sequence of moves from the LLM's response between the
    "Final answer:" and "End of final sequence" markers.

    Args:
        text (str): The full response from the LLM.

    Returns:
        list: A list of lowercase steps (e.g., ['down', 'right']).
              Returns an empty list if the pattern isn't matched.
    """
    match = re.search( # Find the block of text between the markers 'Final answer:' and 'End of final sequence'
        r"Final answer: (.*?)End of final sequence",
        text,
        re.DOTALL | re.IGNORECASE # Make the search case-insensitive and allow newlines
    )
    if match: # If a match is found, process the extracted text, otherwise skip and return empty list
        answer_block = match.group(1).strip().lower()
        # Replace commas and newlines with spaces, then split
        steps = re.split(r'[\s,]+', answer_block)
        # Filter out any empty strings that might result from multiple spaces
        return [step for step in steps if step]
    return []

def prepare_llm_answer_steps(text: str) -> list: # This function has been tested. It processes the entire text input, assuming it contains only the steps and returns the string normalized and split into a list.
    """
    Takes the LLM's answer string, normalizes it, and splits it into a list of steps.

    Args:
        text (str): The answer string from the LLM, containing only the steps.

    Returns:
        list: A list of lowercase steps (e.g., ['down', 'right']).
    """
    if not text: # If the input text is empty or None, return an empty list 
        return []
    # Convert to lowercase, remove leading/trailing whitespace
    processed_text = text.strip().lower()
    # Split by any combination of commas or whitespace (spaces, newlines, etc.)
    steps = re.split(r'[\s,]+', processed_text)
    # Filter out any empty strings that may result from the split
    return [step for step in steps if step]

def score_llm_output_strict(llm_steps: list, solution_steps: list) -> tuple[float, int]:
    """
    Scores LLM output, stopping at the first mismatch.
    The score is the percentage of consecutive matching steps.

    Returns:
        tuple[float, int]: A tuple containing:
        - float: the score from 0.0 to 1.0 (or 1.1 if llm path exceeds goal or nan if LLM path is empty).
        - int: the raw number of consecutive matching steps.
    """
    #Check if any steps are given in the answer. If not, return 'NaN'
    if len(llm_steps) == 0:
        return float('NaN'),0 # returns NaN and ends function. If not, continues to score normally 
    
    consecutive_matches = 0
    # Use zip to iterate through both lists in parallel
    for llm_step, sol_step in zip(llm_steps, solution_steps):
        if llm_step == sol_step:
            consecutive_matches += 1
        else:
            break  # Stop counting on the first mismatch

    # If LLM steps keep moving after reaching goal (number of consecutive_matches is as long as the solution), LLM exceeds the task and function returns 110%. 
    if consecutive_matches == len(solution_steps) and len(llm_steps) > len(solution_steps): 
        return float(1.1), consecutive_matches

    # Calculate score based on the total steps in the ground truth. Use max to avoid division by zero.
    return consecutive_matches / max(len(solution_steps), 1) , consecutive_matches


# -------------- All functions below are specifically for parsing and scoring solution COORDINATES outputted by an LLM. --------------
def parse_coordinate_string(text: str) -> list[tuple[int, int]]: # This function is necessary only when collecting coordinates as an answer from the LLM
    """
    Parses a string of coordinates into a list of integer tuples.

    This function is robust and can handle various formatting, including
    different spacing within the string. For example, "(0,1)", "( 0,  1 )",
    and "(0, 1)" are all parsed correctly.

    Args:
        text (str): A string containing coordinates, e.g., "(0,1), (1,1)".

    Returns:
        list[tuple[int, int]]: A list of coordinate tuples, e.g., [(0, 1), (1, 1)].
                               Returns an empty list if the input is empty or no
                               coordinates are found.
    """
    if not text:
        return []

    # Regex to find all pairs of numbers inside parentheses (e.g., '(x, y)')
    # \(\s* -> Matches an opening parenthesis followed by optional whitespace.
    # (\d+)   -> Captures one or more digits (the x-coordinate).
    # \s*,\s* -> Matches the comma between coordinates, with optional whitespace.
    # (\d+)   -> Captures one or more digits (the y-coordinate).
    # \s*\)   -> Matches optional whitespace and a closing parenthesis.
    matches = re.findall(r'\(\s*(\d+)\s*,\s*(\d+)\s*\)', text)

    # Convert the captured string pairs into integer tuples
    return [(int(x), int(y)) for x, y in matches]

def extract_coordinates(text: str) -> list[tuple[int, int]]: # This function is necessary to extract coordinates from a larger LLM output-text and return them as tuples
    """
    Extracts a sequence of coordinates from a larger text block that is
    marked by "Path:".

    Args:
        text (str): The full response from the LLM.

    Returns:
        list[tuple[int, int]]: A list of coordinate tuples. Returns an empty
                               list if the "Path:" marker isn't found or
                               the path is empty.
    """
    # Search for the content following the "Coordinates:" marker, case-insensitively
    match = re.search(
        r"Coordinates:*(.*)",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        # Extract the coordinate string from the matched group
        path_string = match.group(1).strip()
        # Use the dedicated parser to process the extracted string
        return parse_coordinate_string(path_string)
    
    return []

def score_coordinate_solution( # This function works the same as score_llm_output_strict but for coordinate tuples. Make sure to use a coordinate parsing function on the LLMs answer first
    llm_path: list[tuple[int, int]],
    solution_coords: list[tuple[int, int]]
) -> tuple[float, int]:
    """
    Scores the LLM's generated path against the solution path, stopping at the
    first mismatch. The score is the percentage of consecutively matching
    coordinates from the start of the path.

    Args:
        llm_path (list[tuple[int, int]]): The path generated by the LLM.
        solution_path (list[tuple[int, int]]): The ground truth solution path.

    Returns:
        tuple[float, int]: A tuple containing:
        - float: the score from 0.0 to 1.0 (or 1.1 if llm path exceeds goal or nan if LLM path is empty).
        - int: the raw number of consecutive matching steps.
    """
    #Check if the steps are given in the answer. If not, return 'NaN'
    if len(llm_path) == 0:
        return float('NaN'), 0 # returns NaN and ends function. If not, continues to score normally .

    consecutive_matches = 0
    # Use zip to iterate through both paths, comparing each coordinate tuple.
    for llm_coord, solution_coord in zip(llm_path, solution_coords):
        if llm_coord == solution_coord:
            consecutive_matches += 1
        else:
            # Stop counting at the first coordinate that doesn't match.
            break
    # If LLM coordinates keep moving after reaching goal (number of consecutive_matches is as long as the solution), LLM exceeds the task and function returns 110%. 
    if consecutive_matches == len(solution_coords) and len(llm_path) > len(solution_coords): 
        return float(1.1), consecutive_matches

    # Calculate the score as the fraction of the correct path that was matched.
    # The max() function prevents division by zero if the solution path is empty.
    return consecutive_matches / max(len(solution_coords), 1) , consecutive_matches
    



def main():
    """
    Main function to run the full maze generation, solving, and comparison process.
    """
    try:
        my_api_key = setup_api_key()
        
        # Import the specific maze file and directory path
        maze_file = import_maze_file() 
        script_dir = Path(__file__).parent
        test_dir = script_dir / "Dataset 03" / f"Dataset 03 {MAZE_ROWS}x{MAZE_COLS} {i}" 
        # test_dir = script_dir / "Dataset 01" / f"Dataset 01 {MAZE_ROWS}x{MAZE_COLS}" 
        # test_dir  = script_dir / f"PROMPT TEST Dataset 01 {MAZE_ROWS}x{MAZE_COLS}"
        # test_dir = script_dir / "Dataset 01" / "extra 20x20"
        # test_dir = script_dir / "Dataset 02.1 - ASCII analysis" / f"Dataset 02.1 {MAZE_ROWS}x{MAZE_COLS} {i}" 

        # Get list of files to test, excluding solutions
        files_to_test = [
            f for f in test_dir.iterdir() if "_solution_" not in f.name
        ]

        results = []
        print("\n--- Starting LLM Maze Solving ---")
        
        # -------------- Use this for-loop when scoring solution in ALLO STEPS --------------------

        for file in files_to_test:
            # Dynamically find the correct solution file for the current maze type and add extra info to prompt for each representation
            solution_pattern = ""
            insert_line = ""
            if file.name.startswith("maze_line_"):
                solution_pattern = f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_solution_steps_{i}.txt"
                if file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_{i}.jpg":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {MAZE_ROWS}x{MAZE_COLS} maze is shown as an image, where thick black lines are impassable walls, thin light gray lines are passable cell borders, the circle is the start and the star is the end; the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_{i}.json":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a JSON grid, which describes each cell as a set of four (N/E/S/W) walls with boolean 'True' (impassable) or 'False' (passable) values and includes start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.json":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.txt":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_tokenized_{i}.txt":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a grid in a tokenized manner, where each cell is described by its walls (e.g., <|updownleft_wall|>) and the start and end cells are marked with <|origin|> and <|target|>, respectively; the top-left corner is (0,0) in (row, col).\n" )
                else:
                    print(f"Warning: not changing prompt for file with unhandled type: {file.name}")
                    continue

            elif file.name.startswith("maze_occupancy_"):
                solution_pattern = f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_solution_steps_{i}.txt"
                if file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_{i}.jpg":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {OCC_ROWS}x{OCC_COLS} maze is shown as an image, where white cells are passable, black cells are impassable walls, thin light gray lines are traversable cell borders, the circle is the start and the star is the end; the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_{i}.json":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a JSON grid, where cells are '1' (inaccessible) or '0' (accessible), and start/end coordinates are provided; the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.json":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.txt":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_ascii_{i}.txt":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The maze is represented as a {OCC_ROWS}x{OCC_COLS} ASCII grid using '#' for walls, ' ' for corridors, 'S' for the start, and 'E' for the end; the top-left corner is (0,0) in (row, col).\n" )
                elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_tokenized_{i}.txt":
                    insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
                                    f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a grid in a tokenized manner, where inaccessible cells are tagged as <|occupied_wall|>,  accessible cells are tagged as <|blank|>, and the start and end cells are tagged with <|origin|> and <|target|>, respectively; the top-left corner is (0,0) in (row, col).\n" )
                else:
                    print(f"Warning: not changing prompt for file with unhandled type: {file.name}")
                    continue
            else:
                print(f"Warning: Skipping file with unhandled type: {file.name}")
                continue

            solution_file_path = test_dir / solution_pattern 
            solution_steps = []
            correct_solution_str = "Solution file not found"
            
            if solution_file_path.exists():
                with open(solution_file_path, 'r', encoding='utf-8') as f:
                    correct_solution_str = f.read().strip()
                solution_steps = [s.strip().lower() for s in correct_solution_str.split(',') if s.strip()] # Process the solution steps into a lowercase list
            else:
                print(f"Warning: Could not find solution file matching '{solution_pattern}'")

            # Put specialized prompt together
            representation_prompt = (f'{insert_line}\n{instructions_allo}')
            
            # Call the llm with the current maze file and unpack the tuple returned by call_llm
            response, total_tokens, final_answer, thought_summary = call_llm(representation_prompt, file, my_api_key)

            # Prepare the LLM's answer using the new function
            llm_steps = prepare_llm_answer_steps(final_answer)
            
            # Score the answer against the dynamically found solution
            score, raw_score = score_llm_output_strict(llm_steps, solution_steps)

            # Save the number of tokens to display in the report. Outputs a string and a tuple of strings
            prompt_tokens = extract_prompt_token_count(str(response.usage_metadata))
            total_token_count , output_tokens = extract_output_token_count(str(response.usage_metadata) , prompt_tokens)
        
            type = 'allo'

            # Store all relevant information, including internal thoughts
            results.append({
                "file": file.name,
                "response": final_answer, # Renamed from 'response' to 'final_answer' for clarity
                "internal_thoughts": thought_summary,
                "extracted_answer": ", ".join(llm_steps),
                "score": score * 100,
                "ground_truth": correct_solution_str, 
                "unfiltered_response" : response,
                "total_tokens": total_tokens,
                "metadata" : response.usage_metadata, 
                "candidates" : response.candidates, 
                "prompt_tokens" : prompt_tokens,
                "output_tokens" : output_tokens
            })
        # ------------------------------------------------------------------------------------


        # -------------- Use this for-loop when scoring solution in EGO STEPS --------------------

        # for file in files_to_test:
        # # Dynamically find the correct solution file for the current maze type and add extra info to prompt for each representation
        #     solution_pattern = ""
        #     insert_line = ""
        #     if file.name.startswith("maze_line_"):
        #         solution_pattern = f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_solution_ego_{i}.txt"
        #         if file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_{i}.jpg":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is shown as an image, where thick black lines are impassable walls, thin light gray lines are passable cell borders, the circle is the start and the star is the end; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a JSON grid, which describes each cell as a set of four (N/E/S/W) walls with boolean 'True' (impassable) or 'False' (passable) values and includes start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_tokenized_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a grid in a tokenized manner, where each cell is described by its walls (e.g., <|updownleft_wall|>) and the start and end cells are marked with <|origin|> and <|target|>, respectively; the top-left corner is (0,0) in (row, col).\n" )
        #         else:
        #             print(f"Warning: not changing prompt for file with unhandled type: {file.name}")
        #             continue

        #     elif file.name.startswith("maze_occupancy_"):
        #         solution_pattern = f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_solution_ego_{i}.txt"
        #         if file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_{i}.jpg":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is shown as an image, where white cells are passable, black cells are impassable walls, thin light gray lines are traversable cell borders, the circle is the start and the star is the end; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a JSON grid, where cells are '1' (inaccessible) or '0' (accessible), and start/end coordinates are provided; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_ascii_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The maze is represented as a {OCC_ROWS}x{OCC_COLS} ASCII grid using '#' for walls, ' ' for corridors, 'S' for the start, and 'E' for the end; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_tokenized_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a grid in a tokenized manner, where inaccessible cells are tagged as <|occupied_wall|>,  accessible cells are tagged as <|blank|>, and the start and end cells are tagged with <|origin|> and <|target|>, respectively; the top-left corner is (0,0) in (row, col).\n" )
        #         else:
        #             print(f"Warning: not changing prompt for file with unhandled type: {file.name}")
        #             continue
        #     else:
        #         print(f"Warning: Skipping file with unhandled type: {file.name}")
        #         continue

        #     solution_file_path = test_dir / solution_pattern 
        #     solution_steps = []
        #     correct_solution_str = "Solution file not found"
            
        #     if solution_file_path.exists():
        #         with open(solution_file_path, 'r', encoding='utf-8') as f:
        #             correct_solution_str = f.read().strip()
        #         solution_steps = [s.strip().lower() for s in correct_solution_str.split(',') if s.strip()] # Process the solution steps into a lowercase list
        #     else:
        #         print(f"Warning: Could not find solution file matching '{solution_pattern}'")
            
        #     # Put specialized prompt together
        #     representation_prompt = (f'{insert_line}\n{instructions_ego}')
            
        #     # Call the llm with the current maze file and unpack the tuple returned by call_llm
        #     response, total_tokens, final_answer, thought_summary = call_llm(representation_prompt, file, my_api_key)

        #     # Prepare the LLM's answer using the new function
        #     llm_steps = prepare_llm_answer_steps(final_answer)
            
        #     # Score the answer against the dynamically found solution
        #     score, raw_score = score_llm_output_strict(llm_steps, solution_steps)

        #     # Save the number of tokens to display in the report. Outputs a string and a tuple of strings
        #     prompt_tokens = extract_prompt_token_count(str(response.usage_metadata))
        #     total_token_count , output_tokens = extract_output_token_count(str(response.usage_metadata) , prompt_tokens)
        
        #     type = 'ego'

        #     # Store all relevant information, including internal thoughts
        #     results.append({
        #         "file": file.name,
        #         "response": final_answer, # Renamed from 'response' to 'final_answer' for clarity
        #         "internal_thoughts": thought_summary,
        #         "extracted_answer": ", ".join(llm_steps),
        #         "score": score * 100,
        #         "ground_truth": correct_solution_str, 
        #         "unfiltered_response" : response,
        #         "total_tokens": total_tokens,
        #         "metadata" : response.usage_metadata, 
        #         "candidates" : response.candidates, 
        #         "prompt_tokens" : prompt_tokens,
        #         "output_tokens" : output_tokens
        #     })

        # ------------------------------------------------------------------------------------


        
        # -------------- Use this for-loop when scoring solution in COORDINATES --------------

        # for file in files_to_test:
        #     # Dynamically find the correct solution file for the current maze type and add extra info to prompt for each representation
        #     solution_pattern = ""
        #     insert_line = ""
        #     if file.name.startswith("maze_line_"):
        #         solution_pattern = f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_solution_coords_{i}.txt"
        #         if file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_{i}.jpg":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is shown as an image, where thick black lines are impassable walls, thin light gray lines are passable cell borders, the circle is the start and the star is the end; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a JSON grid, which describes each cell as a set of four (N/E/S/W) walls with boolean 'True' (impassable) or 'False' (passable) values and includes start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_tokenized_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {MAZE_ROWS}x{MAZE_COLS} maze is represented as a grid in a tokenized manner, where each cell is described by its walls (e.g., <|updownleft_wall|>) and the start and end cells are marked with <|origin|> and <|target|>, respectively; the top-left corner is (0,0) in (row, col).\n" )
        #         else:
        #             print(f"Warning: not changing prompt for file with unhandled type: {file.name}")
        #             continue

        #     elif file.name.startswith("maze_occupancy_"):
        #         solution_pattern = f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_solution_coords_{i}.txt"
        #         if file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_{i}.jpg":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is shown as an image, where white cells are passable, black cells are impassable walls, thin light gray lines are traversable cell borders, the circle is the start and the star is the end; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a JSON grid, where cells are '1' (inaccessible) or '0' (accessible), and start/end coordinates are provided; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.json":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_adj_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_ascii_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The maze is represented as a {OCC_ROWS}x{OCC_COLS} ASCII grid using '#' for walls, ' ' for corridors, 'S' for the start, and 'E' for the end; the top-left corner is (0,0) in (row, col).\n" )
        #         elif file.name == f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_tokenized_{i}.txt":
        #             insert_line = ("You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools."\
        #                             f"The {OCC_ROWS}x{OCC_COLS} maze is represented as a grid in a tokenized manner, where inaccessible cells are tagged as <|occupied_wall|>,  accessible cells are tagged as <|blank|>, and the start and end cells are tagged with <|origin|> and <|target|>, respectively; the top-left corner is (0,0) in (row, col).\n" )
        #         else:
        #             print(f"Warning: not changing prompt for file with unhandled type: {file.name}")
        #             continue
        #     else:
        #         print(f"Warning: Skipping file with unhandled type: {file.name}")
        #         continue

        #     solution_file_path = test_dir / solution_pattern 
        #     solution_steps = []
        #     correct_solution_str = "Solution file not found"
            
        #     if solution_file_path.exists():
        #         with open(solution_file_path, 'r', encoding='utf-8') as f:
        #             solution_steps = parse_coordinate_string(f.read())  # Read coordinate solution file and convert to list of tuples
        #             correct_solution_str = str(solution_steps).strip('[]')  # Create a string from the tuple, so it can be used in the dictionary to write in .md file
        #     else:
        #         print(f"Warning: Could not find solution file matching '{solution_pattern}'")

        #     # Put specialized prompt together
        #     representation_prompt = (f'{insert_line}\n{instructions_coords}')
            
        #     # Call the llm with the current maze file and unpack the tuple returned by call_llm
        #     response, total_tokens, final_answer, thought_summary = call_llm(representation_prompt, file, my_api_key)

        #     # Prepare the LLM's answer using the new function
        #     llm_steps = parse_coordinate_string(final_answer)
        
        #     # Score the answer against the dynamically found solution
        #     score, raw_score = score_coordinate_solution(llm_steps, solution_steps)

        #   # Save the number of tokens to display in the report. Outputs a string and a tuple of strings
        #     prompt_tokens = extract_prompt_token_count(str(response.usage_metadata))
        #     total_token_count , output_tokens = extract_output_token_count(str(response.usage_metadata) , prompt_tokens)

        #     type = 'coords'


        #     # Store all relevant information, including internal thoughts
        #     results.append({
        #         "file": file.name,
        #         "response": final_answer, 
        #         "internal_thoughts": thought_summary,
        #         "extracted_answer": llm_steps,
        #         "score": score * 100,
        #         "ground_truth": correct_solution_str, 
        #         "unfiltered_response" : response,
        #         "total_tokens": total_tokens,
        #         "metadata" : response.usage_metadata,
        #         "candidates" : response.candidates, 
        #         "prompt_tokens" : prompt_tokens,
        #         "output_tokens" : output_tokens,
        #         # "prompt_as_used" : representation_prompt
        #     })
        # ------------------------------------------------------------------------------------
           
           
            try:
                # Save the scores to a numpy array in a separate file to create charts after testing. 
                # save_score(filename= file, score = score)
                # collect_and_save_scores(filename= str(file), score = score)
                export_score(filename= file, score = score)
                export_prompt_tokens(filename= file, prompt_tokens = int(prompt_tokens))
                export_output_tokens(filename = file, output_tokens = int(output_tokens))
                export_raw_score(filename= file, score = raw_score)
            except Exception as e:
                print(f"\nAn unexpected error occurred during exporting token and score values: {e}")

    
    # The except needs to be here to save progress in .md file even when api errors occur
    except Exception as e: 
        print(f"\nAn unexpected error occurred: {e}")
        
    print("--- LLM Maze Solving Complete ---")

    try:
        # Generate markdown report
        report_path = test_dir / f"comparison_report_reasoning_{type}_{i}.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# LLM Maze Solving Comparison Report\n\n")
            f.write(f"**Maze Dimensions:** {MAZE_ROWS}x{MAZE_COLS}\n")
            f.write(f"**Model Used:** `{MODEL_NAME}`\n\n")
            f.write("## Comparison Results\n\n")
            f.write("| Representation File | Score (%) | Token count |Extracted LLM Answer |\n")
            f.write("|---|---|---|---|\n")
            for res in sorted(results, key=lambda x: x['file']):
                f.write(f"| `{res['file']}` | **{res['score']:.2f}%** | `input: {res['prompt_tokens']} , ouput: {res['output_tokens']}` | `{res['extracted_answer']}` |\n")

            f.write("\n---\n\n")
            f.write("## Full LLM Responses\n\n")
            for res in sorted(results, key=lambda x: x['file']):
                f.write(f"### `{res['file']}`\n\n")
                f.write(f"**Score:** {res['score']:.2f}%\n\n")
                # f.write("**Prompt:**\n")
                # f.write(f"```\n{res['prompt_as_used']}\n```\n\n")

                f.write("**Ground Truth Solution:**\n")
                f.write(f"```\n{res['ground_truth']}\n```\n\n")
                
                f.write("**Full User-Facing Response (Final Answer):**\n")
                f.write(f"```\n{res['response']}\n```\n\n")

                # Add Internal Thoughts section to the report
                f.write("**Internal Thoughts:**\n")
                f.write(f"```\n{res['internal_thoughts']}\n```\n")

                f.write("**Unfiltered Response:**\n")
                f.write(f"```\n{res['unfiltered_response']}\n```\n")

                f.write("**total_tokens:**\n") 
                f.write(f"```\n{res['total_tokens']}\n```\n")

                f.write("**Metadata:**\n") 
                f.write(f"```\n{res['metadata']}\n```\n")

                f.write("**Candidates:**\n") 
                f.write(f"```\n{res['candidates']}\n```\n\n")

                
        print(f"\nComparison report saved to: {report_path}")

    except Exception as e:
        print(f"\nAn unexpected error occurred during markdown creation: {e}")
if __name__ == "__main__":
    for i in range (4,5):
        main()
        i+=1