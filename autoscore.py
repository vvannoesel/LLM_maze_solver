"""
This is a throwaway doc where i test pieces of code before integrating them into tesT.py
"""

import os
import re
import base64 # converts binary data to ASCII string format and back
from pathlib import Path
# import google.generativeai as genai
from google import genai
from google.genai import types 
# from google.generativeai.types import Tool # old version of API SDK
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

def call_llm(prompt: str, file_path: Path, api_key: str) -> tuple[str, str]:
    """
    Sends a prompt and a file to the model and returns the response and thoughts.

    Args:
        prompt (str): The prompt to send to the model.
        file_path (Path): The path to the file to be included in the prompt.

    Returns:
        tuple: A tuple containing the final text response (str) and internal thoughts (str). 
    """
    print(f"Querying LLM with: {file_path.name}...")
    try:
        # model = genai.GenerativeModel(MODEL_NAME)
        
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            maze_input = Image.open(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                maze_input = f.read()

        # Initialize variables with a default value so they exist in the error case
        thought_summary = ""
        final_answer = ""

        # Enable internal thoughts in the generation config
        # generation_config = genai.types.GenerationConfig(include_internal_texts=True)
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f'{maze_input}\n\n{prompt}',
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    include_thoughts=True
                )
            )
        )

        # Extract internal thoughts if available
        for part in response.candidates[0].content.parts: # the response object is a container for candidates, each candidate has content, which has parts
            if not part.text:   # skip any empty or non-text parts
                continue
            if part.thought:    # check if the part has a thought associated with it. If so, it's an internal thought
                thought_summary = part.text
            else:               # if there's no thought, it's the final answer
                final_answer = part.text

        return final_answer, thought_summary # return both final answer and internal thoughts as a tuple

    except Exception as e:
        print(f"An error occurred while calling the API: {e}")
        error_message = f"Error: Could not get a response from the LLM. Details: {e}"
        # Return a tuple in the error case as well for consistency
        return error_message, "Error during API call."
        # return error_message
    

def main():
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
        #     # Dynamically find the correct solution file for the current maze type 
        #     solution_pattern = ""
        #     if file.name.startswith("maze_line_"):
        #         solution_pattern = f"maze_line_{MAZE_ROWS}x{MAZE_COLS}_solution_steps.txt"
        #     elif file.name.startswith("maze_occupancy_"):
        #         solution_pattern = f"maze_occupancy_{MAZE_ROWS}x{MAZE_COLS}_solution_steps.txt"
        #     else:
        #         print(f"Warning: Skipping file with unhandled type: {file.name}")
        #         continue

        #     solution_file_path = test_dir / solution_pattern 
        #     solution_steps = []
        #     correct_solution_str = "Solution file not found"
            
        #     if solution_file_path.exists():
        #         with open(solution_file_path, 'r', encoding='utf-8') as f:
        #             correct_solution_str = f.read().strip()
        #         solution_steps = [s.strip().lower() for s in correct_solution_str.split(',') if s.strip()] 
        #     else:
        #         print(f"Warning: Could not find solution file matching '{solution_pattern}'")
            
            # Unpack the tuple returned by call_llm
            # final_answer, internal_thoughts = call_llm(PROMPT, file, my_api_key)
            final_answer, thought_summary = call_llm(PROMPT, file, my_api_key)
            print(f"LLM Response: {final_answer}")
            print(f'thoughts: {thought_summary}')

            # Prepare the LLM's answer using the new function
            # llm_steps = prepare_llm_answer_steps(final_answer)
            
            # Score the answer against the dynamically found solution
            # score = score_llm_output_strict(llm_steps, solution_steps)

            # Store all relevant information, including internal thoughts
        #     results.append({
        #         "file": file.name,
        #         "response": final_answer, # Renamed from 'response' to 'final_answer' for clarity
        #         "internal_thoughts": internal_thoughts,
        #         "extracted_answer": ", ".join(llm_steps),
        #         # "score": score * 100,
        #         "ground_truth": correct_solution_str
        #     })

        # print("--- LLM Maze Solving Complete ---")

        # # Generate markdown report
        # report_path = test_dir / "comparison_results.md"
        # with open(report_path, 'w', encoding='utf-8') as f:
        #     f.write(f"# LLM Maze Solving Comparison Report\n\n")
        #     f.write(f"**Maze Dimensions:** {MAZE_ROWS}x{MAZE_COLS}\n")
        #     f.write(f"**Model Used:** `{MODEL_NAME}`\n\n")
        #     f.write("## Comparison Results\n\n")
        #     f.write("| Representation File | Score (%) | Extracted LLM Answer |\n")
        #     f.write("|---|---|---|\n")
        #     # for res in sorted(results, key=lambda x: x['file']):
        #         # f.write(f"| `{res['file']}` | **{res['score']:.2f}%** | `{res['extracted_answer']}` |\n")

        #     f.write("\n---\n\n")
        #     f.write("## Full LLM Responses\n\n")
        #     for res in sorted(results, key=lambda x: x['file']):
        #         f.write(f"### `{res['file']}`\n\n")
        #         # f.write(f"**Score:** {res['score']:.2f}%\n\n")

        #         # f.write("**Ground Truth Solution:**\n")
        #         # f.write(f"```\n{res['ground_truth']}\n```\n\n")
                
        #         # Add Internal Thoughts section to the report
        #         f.write("**Internal Thoughts:**\n")
        #         f.write(f"```text\n{res['internal_thoughts']}\n```\n\n")

        #         f.write("**Full Response (Final Answer):**\n")
        #         f.write(f"```text\n{res['response']}\n```\n\n")
                
        # print(f"\nComparison report saved to: {report_path}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
if __name__ == "__main__":
    main()