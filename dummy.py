import os
from dotenv import load_dotenv
import maze_generator_ext_v3 as maze_gen
import google.generativeai as genai
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()

# Access your API key
my_api_key = os.getenv("TEST_API_KEY")

if not my_api_key:
    raise ValueError("API key not found. make sure it's in your .env file.")

print("my api key is: ", my_api_key)
genai.configure(api_key=my_api_key)


# # --- User Variables ---
# MAZE_SIZES = [(5, 5), (6, 6)]  # List of (cols, rows) tuples
# NUM_MAZES = 2                  # Number of mazes to generate
# LLMS = ["gemini-pro", "gemini-lite"]          # List of Gemini model names
# PROMPTS = [
#     "Solve this maze. The answer should be a sequence of steps from a birds-eye view, choose from up, down, left, right. Do not write a script or use external tools. Show your reasoning.",
#     "Solve this maze. The answer should be a sequence of steps that can be followed by a person in the maze. The person is always facing in the direction of the last step, and starts facing down. Choose from forward, left (90 deg turn + forward step), right (90 deg turn + forward step), or backwards (180 deg turn + forward step). Do not write a script or use external tools. Show your reasoning. "
# ]

# # --- Output File ---
# RESULTS_FILE = f"llm_maze_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# def get_maze_inputs(maze_gen: maze_gen.Maze, occupancy_grid: maze_gen.OccupancyGridMaze):
#     """Return all maze outputs except solution steps/coordinates."""
#     return {
#         "ascii_line": maze_gen.Maze.to_ascii(),
#         "json_line":maze_gen.Maze.to_json(), 
#         "adjacency_line_txt": maze_gen.Maze.to_custom_adjacency_list(),
#         "adjacency_line_json": maze_gen.Maze.to_adjacency_list(),
#         "tokenized_line": maze_gen.Maze.to_tokenized_representation(),
#         "JPG_line": maze_gen.Maze.to_jpg(),
#         "ascii_occupancy": occupancy_grid.to_ascii(),
#         "json_occupancy": occupancy_grid.to_json(),
#         "adjacency_occupancy_txt": occupancy_grid.to_custom_adjacency_list(),
#         "adjacency_occupancy_json": occupancy_grid.to_adjacency_list(),
#         "tokenized_occupancy_line": occupancy_grid.to_tokenized_representation(),
#         "JPG_occupancy_line": occupancy_grid.to_jpg(),

#     }

# # def score_llm_output(llm_steps, solution_steps):
# #     """Simple scoring: percent of steps matching solution. Continues counting after a mismatch. """
# #     llm_seq = [s.strip().lower() for s in llm_steps if s.strip()]
# #     sol_seq = [s.strip().lower() for s in solution_steps if s.strip()]
# #     match = sum(1 for a, b in zip(llm_seq, sol_seq) if a == b)
# #     return match / max(len(sol_seq), 1)

# def score_llm_output_strict(llm_steps, solution_steps):
#     """
#     Scores LLM output, stopping at the first mismatch.
#     The score is the percentage of consecutive matching steps.
#     """
#     llm_seq = [s.strip().lower() for s in llm_steps if s.strip()]
#     sol_seq = [s.strip().lower() for s in solution_steps if s.strip()]
    
#     consecutive_matches = 0
#     # Use zip to iterate through both lists in parallel, up to the length of the shorter one
#     for llm_step, sol_step in zip(llm_seq, sol_seq):
#         if llm_step == sol_step:
#             consecutive_matches += 1
#         else:
#             break # Stop counting on the first mismatch

#     # Calculate the score based on the total steps in the ground truth
#     return consecutive_matches / max(len(sol_seq), 1)

# def call_gemini(model, prompt, maze_input):
#     chat = genai.GenerativeModel(model)
#     response = chat.generate_content(f"{prompt}\n\nMaze:\n{maze_input}")
#     return response.text

# def main():
#     with open(RESULTS_FILE, "w", encoding="utf-8") as f:
#         for maze_idx in range(NUM_MAZES):
#             cols, rows = MAZE_SIZES[maze_idx % len(MAZE_SIZES)]
#             maze = maze_gen.Maze(cols, rows)
#             maze_inputs = get_maze_inputs(maze_gen=maze, occupancy_grid=maze_gen.OccupancyGridMaze)
#             solution_steps = maze.get_solution_steps()
#             f.write(f"\n{'='*40}\nMaze {maze_idx+1} ({cols}x{rows})\n{'='*40}\n")
#             f.write("Maze ASCII:\n" + maze_inputs["ascii"] + "\n")
#             for llm_name in LLMS:
#                 for prompt_idx, prompt in enumerate(PROMPTS):
#                     f.write(f"\n--- LLM: {llm_name}, Prompt {prompt_idx+1} ---\n")
#                     llm_response = call_gemini(llm_name, prompt, maze_inputs["ascii"])
#                     f.write("Prompt:\n" + prompt + "\n")
#                     f.write("LLM Response:\n" + llm_response + "\n")
#                     # Extract steps from LLM response (simple heuristic)
#                     llm_steps = [line for line in llm_response.splitlines() if any(x in line.lower() for x in ["up", "down", "left", "right", "forward", "backwards"])]
#                     score = score_llm_output(llm_steps, solution_steps)
#                     f.write(f"Score vs solution: {score:.2%}\n")
#             f.write(f"Solution steps: {', '.join(solution_steps)}\n")
#     print(f"Results saved to {RESULTS_FILE}")

# if __name__ == "__main__":
#     main()


