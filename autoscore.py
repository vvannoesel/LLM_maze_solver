"""
This is a throwaway doc where i test pieces of code before integrating them into tesT.py
"""
# import os
# from dotenv import load_dotenv
# import maze_generator_ext_v3 as maze_gen
# import google.generativeai as generativeai
# from google import genai
# from google.genai import types
# from PIL import Image


# # --- Load API Key ---
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")
# print("API Key loaded:", bool(API_KEY))
# if not API_KEY:
#     raise ValueError("API key not found. Make sure it's in your .env file.")
# generativeai.configure(api_key=API_KEY)

# PROMPT = "Can you hear me?"
# LLM_NAME = "gemini-pro"


# try:
#     chat = genai.Client(LLM_NAME)  #genai.Client(model) 
#     print("chat initiated", bool(chat))
#     response = chat.generate_content(PROMPT)
#     print("response received", bool(response))
#     print(response)
# except Exception as e:
#     # This will print the actual error from the API call
#     print(f"An error occurred while calling the Gemini API: {e}")
    
    
# -*- coding: utf-8 -*-

import os
import re
import base64
from pathlib import Path
import google.generativeai as genai
from google.generativeai.types import Tool
from dotenv import load_dotenv
from PIL import Image
from maze_generator_ext_v3 import Maze, OccupancyGridMaze

# --- Configuration ---
MAZE_COLS = 4
MAZE_ROWS = 4
MODEL_NAME = "gemini-2.5-pro"
PROMPT = (
    "You are a maze-solving expert.Your goal is to find the path from start to end. "
    "Instructions: " \
    "1. You can only move up, down, left, or right. " \
    "2. You cannot move diagonally or through walls. " \
    "3. Your output must be a single, comma-separated sequence of steps. For example: up, down, right, right, down. " \
    "4. Provide only the final list of moves in your response.")



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
        file_path = script_dir / "Dataset 01" / f"Dataset 01 {MAZE_COLS}x{MAZE_ROWS}" #/ "maze_line_3x3_ascii.txt"

        if not file_path.exists():
            raise FileNotFoundError(f"The specified maze file was not found at: {file_path}")
        
        print(f"Successfully found maze file: {file_path.name}")
        return file_path
    except Exception as e:
        print(f"An error occurred while trying to import the maze file: {e}")
        raise

# def main():
#     """
#     Main function to run the full maze generation, solving, and comparison process.
#     """
#     try:
#         # setup_api_key()
        
#         # 1. Import the specific maze file instead of generating new ones
#         maze_file = import_maze_file() 
#         script_dir = Path(__file__).parent
#         test_dir = script_dir / "Dataset 01" / "Dataset 01 3x3" 
#         print(f"Using test directory: {test_dir}")

#         # 2. Call the LLM with the imported file
#         # final_answer, internal_thoughts = call_llm(PROMPT, maze_file)

#         # 3. Get the ground truth solution
#         solution_file = next(test_dir.glob("*_solution_steps.txt"))
#         with open(solution_file, 'r', encoding='utf-8') as f:
#             correct_solution_str = f.read().strip()
        
#         solution_steps = [s.strip().lower() for s in correct_solution_str.split(',') if s.strip()]


#         # Get list of files to test, excluding solutions
#         files_to_test = [
#             f for f in test_dir.iterdir() if "_solution_steps.txt" not in f.name]
#         print(f"Files to test: {[f.name for f in files_to_test]}")

    
#         # Generate markdown report
#         report_path = test_dir / "comparison_results.md"
#         with open(report_path, 'w', encoding='utf-8') as f:
#             f.write(f"# LLM Maze Solving Comparison Report\n\n")
           
#         print(f"\nComparison report saved to: {report_path}")

#     except Exception as e:
#         print(f"\nAn unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()

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
        # setup_api_key()
        
        # Import the specific maze file and directory path
        maze_file = import_maze_file() 
        script_dir = Path(__file__).parent
        test_dir = script_dir / "Dataset 01" / f"Dataset 01 {MAZE_ROWS}x{MAZE_COLS}" 

        # Call the LLM with the imported file and save the final response and internal thinking 
        # final_answer, internal_thoughts = call_llm(PROMPT, maze_file)

        # Get the ground truth solution -> this block only uses 1 solution file, so only works for 1 type of maze. 
        # solution_file = next(test_dir.glob("*_solution_steps.txt"))
        # with open(solution_file, 'r', encoding='utf-8') as f:
        #     correct_solution_str = f.read().strip()
        
        # solution_steps = [s.strip().lower() for s in correct_solution_str.split(',') if s.strip()]


        # Get list of files to test, excluding solutions
        files_to_test = [
            f for f in test_dir.iterdir() if "_solution_steps.txt" not in f.name
        ]

        results = []
        print("\n--- Starting LLM Maze Solving ---")
        # for file in files_to_test:
        #     llm_response = call_llm(PROMPT, file)
        #     llm_steps = extract_final_answer_steps(llm_response)
        #     score = score_llm_output_strict(llm_steps, solution_steps)

        #     results.append({
        #         "file": file.name,
        #         "response": llm_response,
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
            # final_answer, internal_thoughts = call_llm(PROMPT, file)
            
            # Prepare the LLM's answer using the new function
            final_answer = "down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, down, down, down, down"  # Placeholder for actual LLM output
            internal_thoughts = "I analyzed the maze and determined the optimal path."  # Placeholder for actual internal thoughts
            llm_steps = prepare_llm_answer_steps(final_answer)
            
            # Score the answer against the dynamically found solution
            score = score_llm_output_strict(llm_steps, solution_steps)

            # Store all relevant information for the report
            results.append({
                "file": file.name,
                "final_answer": final_answer,
                "internal_thoughts": internal_thoughts,
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
            # f.write(f"## Ground Truth Solution\n\n")
            # f.write(f"`{correct_solution_str}`\n\n")
            # f.write("---\n\n")
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
                # f.write(f"```\n{res['response']}\n```\n\n")
                # 4. Add the internal thoughts to the report
                # Only write the section if there are thoughts to show
                if res['internal_thoughts']: #alles in deze if is deel van mn test stukje
                    f.write("**Internal Thinking:**\n")
                    f.write(f"```\n{res['internal_thoughts']}\n```\n\n")
                
                f.write("**Final Answer:**\n") #deel van mn test stukje
                f.write(f"```\n{res['final_answer']}\n```\n\n") #deel van mn test stukje

        print(f"\nComparison report saved to: {report_path}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()