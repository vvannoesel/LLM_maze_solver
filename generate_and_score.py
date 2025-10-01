
"""
This script generates a maze, creates and saves it in a directory, then prompts a large language model (LLM) to solve it
using various maze representations, compares the LLM's solutions to the correct solution, 
and saves the results in a markdown file. 
Will probably not be used for testing, but is useful to run small, single tests. 

CHECK: does the internal reasoning save correctly? 
ADD: old code for call_llm (and main) so it can be used for non-reasoning llm's too.
"""

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
MAZE_COLS = 5
MAZE_ROWS = 5
MODEL_NAME = "gemini-2.5-pro"
PROMPT = (
    "You are a maze-solving expert.Your goal is to find the path from start to end. "
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
    genai.configure(api_key=my_api_key)
    print("API key configured successfully.")


def create_test_directory():
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

def generate_and_save_mazes(directory: Path, cols: int, rows: int):
    """
    Generates a maze and its occupancy grid version, then saves all
    representations to the specified directory.

    Args:
        directory (Path): The directory to save the files in.
        cols (int): The number of columns for the maze.
        rows (int): The number of rows for the maze.
    """
    print(f"--- Generating {rows}x{cols} Maze ---")
    line_maze = Maze(cols, rows)
    occupancy_maze = OccupancyGridMaze(line_maze)
    print("Maze generation complete.")

    mazes_to_save = {
        "line": line_maze,
        "occupancy": occupancy_maze
    }

    for name, maze_obj in mazes_to_save.items():
        prefix = directory / f"maze_{name}_{rows}x{cols}"
        maze_obj.to_jpeg(f"{prefix}.jpg")
        maze_obj.to_json(f"{prefix}.json")
        maze_obj.to_adjacency_list(f"{prefix}_adj.json")
        maze_obj.to_custom_adjacency_list(f"{prefix}_adj.txt")
        maze_obj.to_tokenized_representation(f"{prefix}_tokenized.txt")
        with open(f"{prefix}_ascii.txt", "w", encoding="utf-8") as f:
            f.write(maze_obj.to_ascii())

        solution_steps = maze_obj.get_solution_steps()
        with open(f"{prefix}_solution_steps.txt", "w", encoding="utf-8") as f:
            f.write(", ".join(solution_steps))

    print(f"All maze representations saved to '{directory}'.")


# def call_llm(prompt: str, file_path: Path):
#     """
#     Sends a prompt and a file (text or image) to the generative model.

#     Args:
#         prompt (str): The prompt to send to the model.
#         file_path (Path): The path to the file to be included in the prompt.

#     Returns:
#         str: The text response from the model.
#     """
#     print(f"  Querying LLM with: {file_path.name}...")
#     try:
#         model = genai.GenerativeModel(MODEL_NAME)
#         content = [prompt]
#         if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
#             content.append(Image.open(file_path))
#         else:
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 file_content = f.read()
#             content.append(file_content)

#         response = model.generate_content(content)
#         return response.text
#     except Exception as e:
#         print(f"  An error occurred while calling the API: {e}")
#         return f"Error: Could not get a response from the LLM. Details: {e}"

def call_llm(prompt: str, file_path: Path):
    """
    Sends a prompt and a file to the model and captures its internal thinking.

    Args:
        prompt (str): The prompt to send to the model.
        file_path (Path): The path to the file to be included in the prompt.

    Returns:
        tuple[str, str]: A tuple containing the final text response and the
                         model's internal thinking process.
    """
    print(f"Querying LLM with: {file_path.name}...")
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        content = [prompt]
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            content.append(Image.open(file_path))
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            content.append(file_content)

        # 1. Define the tool to capture the model's thoughts
        # This tool acts as a "scratchpad" for the model.
        save_thoughts_tool = Tool(
            function_declarations=[
                genai.protos.FunctionDeclaration( # Define the tool schema
                    name="save_internal_thoughts",
                    description=(
                        "An internal tool for the model to save its step-by-step "
                        "reasoning or thought process before providing the final answer. "
                        "Use this to structure your thoughts."
                    ),
                    parameters=genai.protos.Schema( # Define the parameters the tool accepts
                        type=genai.protos.Type.OBJECT, # The tool takes an object
                        properties={
                            "thoughts": genai.protos.Schema( 
                                type=genai.protos.Type.STRING,  # The 'thoughts' parameter is a string
                                description="Your detailed, step-by-step thinking process."
                            )
                        }
                    )
                )
            ]
        )


        # 2. Call the model with the tool
        response = model.generate_content(content, tools=[save_thoughts_tool])

        # 3. Process the multi-part response
        internal_thoughts = ""      # This will hold the model's internal reasoning
        final_answer = ""           # This will hold the final text answer

        # The response may contain a function call (the thoughts) and text (the answer)
        for part in response.parts:
            if part.function_call:
                if part.function_call.name == "save_internal_thoughts": 
                    # Extract the thinking process from the tool's arguments
                    internal_thoughts = part.function_call.args.get("thoughts", "")
            elif part.text:
                final_answer = part.text

        # If the model only returned a tool call without a final text part
        if not final_answer and internal_thoughts:
            final_answer = "The model provided a thought process but no final answer."
            
        return final_answer, internal_thoughts

    except Exception as e:
        print(f"An error occurred while calling the API: {e}")
        error_message = f"Error: Could not get a response from the LLM. Details: {e}"
        return error_message, ""

def extract_final_answer_steps(text: str) -> list:
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
        setup_api_key()
        test_dir = create_test_directory()
        generate_and_save_mazes(test_dir, MAZE_COLS, MAZE_ROWS)

        # Get the ground truth solution
        solution_file = next(test_dir.glob("*_solution_steps.txt"))
        with open(solution_file, 'r', encoding='utf-8') as f:
            correct_solution_str = f.read().strip()
        
        solution_steps = [s.strip().lower() for s in correct_solution_str.split(',') if s.strip()]


        # Get list of files to test, excluding solutions
        files_to_test = [
            f for f in test_dir.iterdir() if "_solution_steps.txt" not in f.name
        ]

        results = []
        print("\n--- Starting LLM Maze Solving ---")
        # for file in files_to_test: # DEZE FOR-LOOP IS DE OUDE CODE, DIE NIET DE INTERNAL THOUGHTS OPSLAAT. DEZE SLAAT ALLEEN DE RESPONSE OP.
        #     llm_response = call_llm(PROMPT, file)
        #     llm_steps = extract_final_answer_steps(llm_response)
        #     score = score_llm_output_strict(llm_steps, solution_steps)

        #     results.append({
        #         "file": file.name,
        #         "response": llm_response,
        for file in files_to_test:
            # 1. Unpack the two return values from the updated call_llm function
            final_answer, internal_thoughts = call_llm(PROMPT, file)
            
            # 2. Use the 'final_answer' for processing
            llm_steps = extract_final_answer_steps(final_answer)
            score = score_llm_output_strict(llm_steps, solution_steps)

            # 3. Store both the final answer and the thoughts in the results
            results.append({
                "file": file.name,
                "final_answer": final_answer,
                "internal_thoughts": internal_thoughts, #tot en met hier is mn test stukje
                "extracted_answer": ", ".join(llm_steps),
                "score": score * 100  # Store as percentage
            })
        print("--- LLM Maze Solving Complete ---")

        # Generate markdown report
        report_path = test_dir / "comparison_results.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# LLM Maze Solving Comparison Report\n\n")
            f.write(f"**Maze Dimensions:** {MAZE_COLS}x{MAZE_ROWS}\n")
            f.write(f"**Model Used:** `{MODEL_NAME}`\n\n")
            f.write(f"## Ground Truth Solution\n\n")
            f.write(f"`{correct_solution_str}`\n\n")
            f.write("---\n\n")
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
                f.write("**Extracted Answer:**\n")
                f.write(f"```\n{res['extracted_answer']}\n```\n\n")
                # f.write("**Full Response:**\n")
                # f.write(f"```text\n{res['response']}\n```\n\n")
                # 4. Add the internal thoughts to the report
                # Only write the section if there are thoughts to show
                if res['internal_thoughts']: #alles in deze if is deel van mn test stukje
                    f.write("**Internal Thinking:**\n")
                    f.write(f"```text\n{res['internal_thoughts']}\n```\n\n")
                
                f.write("**Final Answer:**\n") #deel van mn test stukje
                f.write(f"```text\n{res['final_answer']}\n```\n\n") #deel van mn test stukje

        print(f"\nComparison report saved to: {report_path}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


