import os
from dotenv import load_dotenv
import maze_generator_ext_v3 as maze_gen
import google.generativeai as genai
from google.genai import types
from PIL import Image
import base64

# --- Load API Key ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Make sure it's in your .env file.")
genai.configure(api_key=API_KEY)

PROMPT = (
    "Solve this maze. The answer should be a sequence of steps from a birds-eye view, choose from up, down, left, right. "
    "Start the final answer with 'Final answer:' and end the final answer with 'End of final sequence'. "
    "Do not write a script or use external tools. Show your reasoning."
)
LLM_NAME = "gemini-pro"
MAZE_COLS = 5
MAZE_ROWS = 5

# def call_gemini_with_text(model, prompt, maze_input):
#     chat = genai.GenerativeModel(model)
#     response = chat.generate_content(f"{prompt}\n\nMaze:\n{maze_input}")
#     return response.text

def call_gemini_with_text(model, prompt, maze_input):
    """
    Calls the Gemini API and includes error handling to catch and display issues.
    """
    try:
        chat = genai.GenerativeModel(model)  #genai.Client(model) #
        response = chat.generate_content(f"{prompt}\n\nMaze:\n{maze_input}")
        return response.text
    except Exception as e:
        # This will print the actual error from the API call
        print(f"An error occurred while calling the Gemini API: {e}")
        # This provides a fallback message to be written to the results file
        return f"Error: Could not get a response from the LLM. Details: {e}"


def call_gemini_with_image(model, prompt, image_path):
    chat = genai.GenerativeModel(model)
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()
    response = chat.generate_content([prompt, Image.open(image_path)])
    return response.text





# --- Utility Functions ---
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
    # ASCII
    ascii_path = os.path.join(folder, f"{prefix}maze_ascii.txt")
    with open(ascii_path, "w", encoding="utf-8") as f:
        f.write(maze.to_ascii())
    maze_files.append((f"{prefix}ascii", ascii_path))
    # # JPEG
    # jpg_path = os.path.join(folder, f"{prefix}maze.jpg")
    # maze.to_jpeg(jpg_path)
    # maze_files.append((f"{prefix}jpg", jpg_path))
    # # JSON
    # json_path = os.path.join(folder, f"{prefix}maze.json")
    # maze.to_json(json_path)
    # maze_files.append((f"{prefix}json", json_path))
    # # Adjacency JSON
    # adj_json_path = os.path.join(folder, f"{prefix}maze_adj.json")
    # maze.to_adjacency_list(adj_json_path)
    # maze_files.append((f"{prefix}adj_json", adj_json_path))
    # # Adjacency TXT
    # adj_path = os.path.join(folder, f"{prefix}maze_adj.txt")
    # maze.to_custom_adjacency_list(adj_path)
    # maze_files.append((f"{prefix}adjacency", adj_path))
    # # Tokenized
    # token_path = os.path.join(folder, f"{prefix}maze_tokenized.txt")
    # maze.to_tokenized_representation(token_path)
    # maze_files.append((f"{prefix}tokenized", token_path))
    # Solution steps
    sol_steps_path = os.path.join(folder, f"{prefix}maze_solution_steps.txt")
    with open(sol_steps_path, "w", encoding="utf-8") as f:
        f.write(", ".join(maze.get_solution_steps()))
    maze_files.append((f"{prefix}solution_steps", sol_steps_path))
    return maze_files

def read_file_content(path, binary=False):  # = True for images
    if binary: 
        with open(path, "rb") as f:  # Open in binary mode
            return f.read()
    else: 
        with open(path, "r", encoding="utf-8") as f:  # Open in text mode
            return f.read()

def extract_final_answer(text): # Extracts text between "Final answer:" and "End of final sequence"
    start = text.find("Final answer:")
    end = text.find("End of final sequence")
    if start != -1 and end != -1:  # Both markers found
        return text[start+len("Final answer:"):end].strip()
    return ""

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





def main():
    base_dir = os.path.dirname(os.path.abspath(__file__)) # Current script directory
    test_folder = get_next_test_folder(base_dir) # Create new test folder
    maze = maze_gen.Maze(MAZE_COLS, MAZE_ROWS) # Generate new maze
    occ_maze = maze_gen.OccupancyGridMaze(maze) # Create occupancy grid version
    maze_files = save_maze_outputs(maze, test_folder, prefix="") # Save maze outputs
    # occ_files = save_maze_outputs(occ_maze, test_folder, prefix="occupancy_") # Save occupancy grid outputs
    all_files = maze_files #+ occ_files # Combine all files

    # Find solution steps file
    solution_file = [p for t, p in all_files if t.endswith("solution_steps")][0]
    solution_steps = [s.strip() for s in read_file_content(solution_file).split(",")]

    # Prepare markdown output
    md_path = os.path.join(test_folder, "llm_maze_results.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# LLM Maze Results\n\n")
        f.write(f"**Test folder:** {test_folder}\n\n")
        f.write(f"**Maze size:** {MAZE_COLS}x{MAZE_ROWS}\n\n")
        for maze_type, maze_path in all_files:
            if maze_path.endswith("solution_steps.txt"):
                continue
            f.write(f"## Maze Representation: {maze_type}\n")
            if maze_path.endswith(".jpg"):
                llm_response = call_gemini_with_image(LLM_NAME, PROMPT, maze_path)
                img_rel_path = os.path.relpath(maze_path, test_folder)
                f.write(f"![Maze Image]({img_rel_path})\n\n")
            else:
                maze_input = read_file_content(maze_path)
                f.write("""```
{} 
```
""".format(maze_input))
                llm_response = call_gemini_with_text(LLM_NAME, PROMPT, maze_input)
            f.write(f"**LLM Response:**\n\n{llm_response}\n\n")
            final_answer = extract_final_answer(llm_response)
            llm_steps = [line for line in final_answer.splitlines() if any(x in line.lower() for x in ["up", "down", "left", "right"])]
            score = score_llm_output_strict(llm_steps, solution_steps)
            f.write(f"**Score vs solution:** {score:.2%}\n\n")
            f.write(f"---\n\n")
        f.write("""### Ground Truth Solution steps
```
{}
```
""".format(', '.join(solution_steps)))
    print(f"Results saved to {md_path}")

if __name__ == "__main__":
    main()
