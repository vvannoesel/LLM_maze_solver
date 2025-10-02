"""
@author: valer and Gemini 2.5 Pro, 3 september 16:28:15 2025
This script generates a maze, prompts a large language model (LLM) to solve it
using various maze representations, compares the LLM's solutions to the
correct solution, and saves the results in a markdown file.
DOES NOT INCLUDE INTERNAL THOUGHTS. USE ONLY FOR NON-REASONING LLMS.
Updated to new SDK call structure of call_llm. 
"""

import os
import re
import base64 # converts binary data to ASCII string format and back
from pathlib import Path
# import google.generativeai as genai   # old library, replaced with the new one below  
from google import genai
from dotenv import load_dotenv
from PIL import Image
from maze_generator_ext_v3 import Maze, OccupancyGridMaze

# --- Configuration ---
MAZE_ROWS = 3
MAZE_COLS = 3
MODEL_NAME = "gemini-2.5-pro"
PROMPT = (
    "You are a maze-solving expert.Your goal is to find the path from start to end. Do not use external tools. "
    "Instructions: " \
    "1. You can only move up, down, left, or right. " \
    "2. You cannot move diagonally or through walls. " \
    "3. Your output must be a single, comma-separated sequence of steps. For example: up, down, right, right, down. " \
    "4. Provide only the final list of moves in your response.")

def setup_api_key():
    """
    Loads the Google API key from a .env file and configures the genai library.
    """
    load_dotenv()
    my_api_key = os.getenv("TEST_API_KEY")
    if not my_api_key:
        raise ValueError("API_KEY not found in .env file.")
    # genai.configure(api_key=my_api_key) # Old method of configuration. New method below in call_llm
    # client = genai.Client(api_key=my_api_key) #can i split this up or should it be in call_llm?
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
        file_path = script_dir / "Dataset 01" / f"Dataset 01 {MAZE_ROWS}x{MAZE_COLS}" #/ "maze_line_3x3_ascii.txt"

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


def call_llm(prompt: str, file_path: Path, api_key: str):
    """
    Sends a prompt and a file to the model.

    Args:
        prompt (str): The prompt to send to the model.
        file_path (Path): The path to the file to be included in the prompt.

    Returns:
        string: A string containing the final text response
    """
    print(f"Querying LLM with: {file_path.name}...")
    try:
        # model = genai.GenerativeModel(MODEL_NAME)
        # content = [prompt]
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            # content.append(Image.open(file_path))
            maze_input = Image.open(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                maze_input = f.read()
            # content.append(file_content)
        print("Content for LLM is: ", maze_input)
        # response = model.generate_content(f"{prompt}\n\n{maze_input}") # old method, replaced with new one below
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(  # FOR 2.5 FL THE DEFAULT THINKING BUDGET IS 0
            model = MODEL_NAME,
            contents=f'{PROMPT}\n\n{maze_input}')
        # print("response shape:", type(response))

        return response.text 

    except Exception as e:
        print(f"An error occurred while calling the API: {e}")
        error_message = f"Error: Could not get a response from the LLM. Details: {e}"
        return error_message

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


def score_llm_output_strict(llm_steps: list, solution_steps: list) -> float:
    """
    Scores LLM output, stopping at the first mismatch.
    The score is the percentage of consecutive matching steps.
    """
    consecutive_matches = 0
    # Use zip to iterate through both lists in parallel
    for llm_step, sol_step in zip(llm_steps, solution_steps):
        if llm_step == sol_step:
            consecutive_matches += 1
        else:
            break  # Stop counting on the first mismatch

    # Calculate score based on the total steps in the ground truth. Use max to avoid division by zero.
    return consecutive_matches / max(len(solution_steps), 1)

def main():
    """
    Main function to run the full maze generation, solving, and comparison process.
    """
    try:
        my_api_key = setup_api_key()
        
        # Import the specific maze file and directory path
        maze_file = import_maze_file() 
        script_dir = Path(__file__).parent
        test_dir = script_dir / "Dataset 01" / f"Dataset 01 {MAZE_ROWS}x{MAZE_COLS}" 

        # Get list of files to test, excluding solutions
        files_to_test = [
            f for f in test_dir.iterdir() if "_solution_steps.txt" not in f.name
        ]

        results = []
        print("\n--- Starting LLM Maze Solving ---")
        
        for file in files_to_test:
            # Dynamically find the correct solution file for the current maze type 
            solution_pattern = ""
            if file.name.startswith("maze_line_"):
                solution_pattern = f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_solution_steps.txt"
            elif file.name.startswith("maze_occupancy_"):
                solution_pattern = f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_solution_steps.txt"
            else:
                print(f"Warning: Skipping file with unhandled type: {file.name}")
                continue

            solution_file_path = test_dir / solution_pattern # Construct the full path to the solution file (solution_pattern is a dynamic filename)
            solution_steps = []
            correct_solution_str = "Solution file not found" # Default message if solution file is missing. Replaced with actual solution if found.
            
            if solution_file_path.exists():
                with open(solution_file_path, 'r', encoding='utf-8') as f:
                    correct_solution_str = f.read().strip()
                solution_steps = [s.strip().lower() for s in correct_solution_str.split(',') if s.strip()] # Process the solution steps into a lowercase list
            else:
                print(f"Warning: Could not find solution file matching '{solution_pattern}'")
            
            # Call the LLM with the current maze file
            response = call_llm(PROMPT, file, my_api_key)
           
            # Prepare the LLM's answer using the new function
            llm_steps = prepare_llm_answer_steps(response)
            
            # Score the answer against the dynamically found solution
            score = score_llm_output_strict(llm_steps, solution_steps)

            # Store all relevant information for the report as dictionary entries
            results.append({
                "file": file.name,
                "response": response,
                "extracted_answer": ", ".join(llm_steps),
                "score": score * 100,  # Store as percentage
                "ground_truth": correct_solution_str
            })

        print("--- LLM Maze Solving Complete ---")

        # Generate markdown report
        report_path = test_dir / "comparison_results.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# LLM Maze Solving Comparison Report\n\n")
            f.write(f"**Maze Dimensions:** {MAZE_ROWS}x{MAZE_COLS}\n")
            f.write(f"**Model Used:** `{MODEL_NAME}`\n\n")
            f.write("## Comparison Results\n\n")
            f.write("| Representation File | Score (%) | Extracted LLM Answer |\n")
            f.write("|---|---|---|\n")
            for res in sorted(results, key=lambda x: x['file']):
                f.write(f"| `{res['file']}` | **{res['score']:.2f}%** | `{res['extracted_answer']}` |\n")

            f.write("\n---\n\n")
            f.write("## Full LLM Responses\n\n")
            for res in sorted(results, key=lambda x: x['file']):
                f.write(f"### `{res['file']}`\n\n")
                f.write(f"**Score:** {res['score']:.2f}%\n\n")

                f.write("**Ground Truth Solution:**\n")
                f.write(f"```\n{res['ground_truth']}\n```\n\n")

                f.write("**Extracted Answer:**\n")
                f.write(f"```\n{res['extracted_answer']}\n```\n\n")

                f.write("**Full Response:**\n") # Keep this section to show the entire response in case LLM disobeys format
                f.write(f"```text\n{res['response']}\n```\n\n")
                
        print(f"\nComparison report saved to: {report_path}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()