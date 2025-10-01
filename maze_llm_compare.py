import os
from dotenv import load_dotenv
import maze_generator_ext_v3 as maze_gen
import google.generativeai as genai
from datetime import datetime

# # --- Load API Key ---
load_dotenv()
API_KEY = os.getenv("TEST_API_KEY")
print("API Key loaded:", bool(API_KEY))
if not API_KEY:
    raise ValueError("API key not found. Make sure it's in your .env file.")
genai.configure(api_key=API_KEY) # Configure the API key

# --- Adjustable Maze Size ---
MAZE_COLS = 5
MAZE_ROWS = 5
LLMS = ["gemini-2.5-pro-exp-03-25"]
PROMPTS = [
    "Solve this maze. The answer should be a sequence of steps from a birds-eye view, choose from up, down, left, right. Do not write a script or use external tools. Show your reasoning.",
    "Solve this maze. The answer should be a sequence of steps that can be followed by a person in the maze. The person is always facing in the direction of the last step, and starts facing down. Choose from forward, left (90 deg turn + forward step), right (90 deg turn + forward step), or backwards (180 deg turn + forward step). Do not write a script or use external tools. Show your reasoning. "
]

def get_next_test_folder(base_dir):
    i = 1
    while True:
        folder = os.path.join(base_dir, f"Test Maze {i}")
        if not os.path.exists(folder):
            os.makedirs(folder)
            return folder
        i += 1

def save_maze_outputs(maze, folder, prefix=""):
    maze_files = []
    # Save ASCII
    ascii_path = os.path.join(folder, f"{prefix}maze_ascii.txt")
    with open(ascii_path, "w", encoding="utf-8") as f:
        f.write(maze.to_ascii())
    maze_files.append((f"{prefix}ascii", ascii_path))
    # Save JPEG
    jpg_path = os.path.join(folder, f"{prefix}maze.jpg")
    maze.to_jpeg(jpg_path)
    maze_files.append((f"{prefix}jpg", jpg_path))
    # Save JSON
    json_path = os.path.join(folder, f"{prefix}maze.json")
    maze.to_json(json_path)
    maze_files.append((f"{prefix}json", json_path))
    # Save adjacency list (JSON)
    adj_json_path = os.path.join(folder, f"{prefix}maze_adj.json")
    maze.to_adjacency_list(adj_json_path)
    maze_files.append((f"{prefix}adj_json", adj_json_path))
    # Save adjacency list (custom TXT)
    adj_path = os.path.join(folder, f"{prefix}maze_adj.txt")
    maze.to_custom_adjacency_list(adj_path)
    maze_files.append((f"{prefix}adjacency", adj_path))
    # Save tokenized
    token_path = os.path.join(folder, f"{prefix}maze_tokenized.txt")
    maze.to_tokenized_representation(token_path)
    maze_files.append((f"{prefix}tokenized", token_path))
    # Save solution steps (for scoring, not for LLM)
    sol_steps_path = os.path.join(folder, f"{prefix}maze_solution_steps.txt")
    with open(sol_steps_path, "w", encoding="utf-8") as f:
        f.write(", ".join(maze.get_solution_steps()))
    return maze_files, sol_steps_path

# def score_llm_output(llm_steps, solution_steps):
#     llm_seq = [s.strip().lower() for s in llm_steps if s.strip()]
#     sol_seq = [s.strip().lower() for s in solution_steps if s.strip()]
#     match = sum(1 for a, b in zip(llm_seq, sol_seq) if a == b)
#     return match / max(len(sol_seq), 1)

def score_llm_output_strict(llm_steps, solution_steps):
    """
    Scores LLM output, stopping at the first mismatch.
    The score is the percentage of consecutive matching steps.
    """
    llm_seq = [s.strip().lower() for s in llm_steps if s.strip()]
    sol_seq = [s.strip().lower() for s in solution_steps if s.strip()]
    
    consecutive_matches = 0
    # Use zip to iterate through both lists in parallel, up to the length of the shorter one
    for llm_step, sol_step in zip(llm_seq, sol_seq):
        if llm_step == sol_step:
            consecutive_matches += 1
        else:
            break # Stop counting on the first mismatch

    # Calculate the score based on the total steps in the ground truth
    return consecutive_matches / max(len(sol_seq), 1)


# def call_gemini(model, prompt, maze_input):
#     chat = genai.GenerativeModel(model)
#     response = chat.generate_content(f"{prompt}\n\nMaze:\n{maze_input}")
#     return response.text

def call_gemini(model, prompt, maze_input):
    """
    Calls the Gemini API and includes error handling to catch and display issues.
    """
    try:
        chat = genai.GenerativeModel(model) # or genai.Client(model)
        response = chat.generate_content(f"{prompt}\n\nMaze:\n{maze_input}")
        return response.text
    except Exception as e:
        # This will print the actual error from the API call
        print(f"An error occurred while calling the Gemini API: {e}")
        # This provides a fallback message to be written to the results file
        return f"Error: Could not get a response from the LLM. Details: {e}"

def read_file_content(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# def main():
#     base_dir = os.path.dirname(os.path.abspath(__file__))   # Determine directory of the current script
#     test_folder = get_next_test_folder(base_dir)            # Create new test folder within current directory
#     maze = maze_gen.Maze(MAZE_COLS, MAZE_ROWS)              # Generate new maze
#     occ_maze = maze_gen.OccupancyGridMaze(maze)             # Create occupancy grid version of the maze
#     maze_files, sol_steps_path = save_maze_outputs(maze, test_folder, prefix="")                    # Save maze outputs
#     occ_files, occ_sol_steps_path = save_maze_outputs(occ_maze, test_folder, prefix="occupancy_")   # Save occupancy grid outputs
    
#     solution_steps = [s.strip() for s in read_file_content(sol_steps_path).split(",")] # Use Maze solution steps for scoring (could also use occ_maze.get_solution_steps())
#     results_path = os.path.join(test_folder, "llm_results.txt")  # LLM results file path
    
#     # Exclude solution files from LLM loop
#     def is_solution_file(path):
#         return path.endswith("solution_steps.txt")
#     # def is_jpg_file(path):
#     #     return path.endswith(".jpg")
#     with open(results_path, "w", encoding="utf-8") as f:
#         f.write(f"Test folder: {test_folder}\nMaze size: {MAZE_COLS}x{MAZE_ROWS}\n\n")
#         all_files = maze_files + occ_files
#         for maze_type, maze_path in all_files:
#             # Only include text-based, JPG and JSON outputs for LLM, not solution steps
#             if is_solution_file(maze_path) : # or is_jpg_file(maze_path):
#                 continue
#             maze_input = read_file_content(maze_path)                       # Read maze input from file
#             f.write(f"{'='*30}\nMaze output type: {maze_type}\n{'='*30}\n") # Write header in response file
#             f.write(maze_input + "\n")                                      # Write maze input to response file
#             for llm_name in LLMS: 
#                 for prompt_idx, prompt in enumerate(PROMPTS):               # Iterate through prompts
#                     f.write(f"\n--- LLM: {llm_name}, Prompt {prompt_idx+1} ---\n") # Write LLM and prompt header
#                     llm_response = call_gemini(llm_name, prompt, maze_input)    # Call Gemini API, sending the content of the current maze file and the current prompt to the API
#                     f.write("Prompt:\n" + prompt + "\n")                        # Write prompt to response file
#                     f.write("LLM Response:\n" + llm_response + "\n")            # Write LLM response to file
#                     llm_steps = [line for line in llm_response.splitlines() if any(x in line.lower() for x in ["up", "down", "left", "right", "forward", "backwards"])] # Extract steps from LLM response (simple heuristic)
#                     score = score_llm_output_strict(llm_steps, solution_steps)  # Score LLM output
#                     f.write(f"Score vs solution: {score:.2%}\n")                # Write score to file
#         f.write(f"\nSolution steps: {', '.join(solution_steps)}\n")             # Write solution steps at the end
#     print(f"Results saved to {results_path}") 








# def main_test():
#     """
#     A simplified version of main() that runs only one iteration for testing.
#     It uses the ASCII representation of the maze and the first (BEV) prompt.
#     """
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     test_folder = get_next_test_folder(base_dir)

#     print("Generating maze...")
#     maze = maze_gen.Maze(MAZE_COLS, MAZE_ROWS)
#     maze_files, sol_steps_path = save_maze_outputs(maze, test_folder, prefix="")
    
#     # --- Single Test Case ---
#     # We will use the ASCII maze file for this test.
#     # The path to the ascii file is the first element in the list of tuples.
#     maze_type_to_test = "ascii" # Change to "jpg", "json", "adj_json", "adjacency", or "tokenized" to test other formats
#     maze_path_to_test = next((path for type, path in maze_files if type == maze_type_to_test), None) # Find the path for the desired maze type
    
#     if not maze_path_to_test:
#         print(f"Could not find the maze file of type: {maze_type_to_test}")
#         return

#     # We will use the first LLM and the first prompt.
#     llm_name_to_test = LLMS[0]
#     prompt_to_test = PROMPTS[0]

#     print(f"Using maze file: {maze_path_to_test}")
#     print(f"Using LLM: {llm_name_to_test}")
    
#     # Read the ground truth solution for scoring
#     solution_steps = [s.strip() for s in read_file_content(sol_steps_path).split(",")]
#     results_path = os.path.join(test_folder, "llm_results_TEST.txt")

#     with open(results_path, "w", encoding="utf-8") as f:
#         f.write(f"Test folder: {test_folder}\nMaze size: {MAZE_COLS}x{MAZE_ROWS}\n\n")
        
#         maze_input = read_file_content(maze_path_to_test)
#         f.write(f"{'='*30}\nMaze output type: {maze_type_to_test}\n{'='*30}\n")
#         f.write(maze_input + "\n")

#         f.write(f"\n--- LLM: {llm_name_to_test}, Prompt 1 ---\n")
        
#         print("Calling the LLM API...")
#         llm_response = call_gemini(llm_name_to_test, prompt_to_test, maze_input)
#         print("Response received.")

#         f.write("Prompt:\n" + prompt_to_test + "\n")
#         f.write("LLM Response:\n" + llm_response + "\n")
        
#         # Extract steps from the response
#         llm_steps = [line for line in llm_response.splitlines() if any(x in line.lower() for x in ["up", "down", "left", "right", "forward", "backwards"])]
        
#         # Score the response
#         score = score_llm_output_strict(llm_steps, solution_steps)
#         f.write(f"Score vs solution: {score:.2%}\n")
        
#         f.write(f"\nSolution steps: {', '.join(solution_steps)}\n")

#     print(f"Single test complete. Results saved to {results_path}")


def main_minitest():
    """
    A simplified version of main() that runs only one iteration for testing.
    It uses the ASCII representation of the maze and the first (BEV) prompt.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_folder = get_next_test_folder(base_dir)

    print("Generating maze...")
    maze = maze_gen.Maze(MAZE_COLS, MAZE_ROWS)
    maze_files, sol_steps_path = save_maze_outputs(maze, test_folder, prefix="")
    
    # --- Single Test Case ---
    # We will use the ASCII maze file for this test.
    # The path to the ascii file is the first element in the list of tuples.
    maze_type_to_test = "tokenized" # Change to "jpg", "json", "adj_json", "adjacency", or "tokenized" to test other formats
    maze_path_to_test = next((path for type, path in maze_files if type == maze_type_to_test), None) # Find the path for the desired maze type
    
    if not maze_path_to_test:
        print(f"Could not find the maze file of type: {maze_type_to_test}")
        return

    # We will use the first LLM and the first prompt.
    llm_name_to_test = LLMS[0]
    prompt_to_test = PROMPTS[0]

    print(f"Using prompt: {prompt_to_test}")
    print(f"Using maze file: {maze_path_to_test}")
    print(f"Using LLM: {llm_name_to_test}")
    
    # Read the ground truth solution for scoring
    solution_steps = [s.strip() for s in read_file_content(sol_steps_path).split(",")]
    results_path = os.path.join(test_folder, "llm_results_TEST.txt")

    with open(results_path, "w", encoding="utf-8") as f:
        f.write(f"Test folder: {test_folder}\nMaze size: {MAZE_COLS}x{MAZE_ROWS}\n\n")
        
        maze_input = read_file_content(maze_path_to_test)
        f.write(f"{'='*30}\nMaze output type: {maze_type_to_test}\n{'='*30}\n")
        f.write(maze_input + "\n")

        f.write(f"\n--- LLM: {llm_name_to_test}, Prompt 1 ---\n")
        
        print("Calling the LLM API...")
        llm_response = call_gemini(llm_name_to_test, prompt_to_test, maze_input)
        print("Response received.")

        f.write("Prompt:\n" + prompt_to_test + "\n")
        f.write("LLM Response:\n" + llm_response + "\n")
        
        # Extract steps from the response
        llm_steps = [line for line in llm_response.splitlines() if any(x in line.lower() for x in ["up", "down", "left", "right", "forward", "backwards"])]
        
        # Score the response
        score = score_llm_output_strict(llm_steps, solution_steps)
        f.write(f"Score vs solution: {score:.2%}\n")
        
        f.write(f"\nSolution steps: {', '.join(solution_steps)}\n")

    print(f"Single test complete. Results saved to {results_path}")




if __name__ == "__main__":
    main_minitest()
