import os
from dotenv import load_dotenv
import google.generativeai as genai

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

def call_gemini(model, prompt, maze_input):
    chat = genai.GenerativeModel(model)
    response = chat.generate_content(f"{prompt}\n\nMaze:\n{maze_input}")
    return response.text

def read_file_content(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # --- User variables ---
    TEST_FOLDER = input("Enter the path to the Test Maze X folder: ").strip()
    MAZE_FILE = input("Enter the filename to use as LLM input (e.g. maze_ascii.txt): ").strip()
    PROMPT = input("Enter the prompt to use: ").strip()
    SOLUTION_FILE = input("Enter the solution steps filename (e.g. maze_solution_steps.txt): ").strip()
    LLM_NAME = "gemini-pro"

    # --- Load API Key ---
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        raise ValueError("API key not found. Make sure it's in your .env file.")
    genai.configure(api_key=API_KEY)

    maze_path = os.path.join(TEST_FOLDER, MAZE_FILE)
    solution_path = os.path.join(TEST_FOLDER, SOLUTION_FILE)
    maze_input = read_file_content(maze_path)
    solution_steps = [s.strip() for s in read_file_content(solution_path).split(",")]

    results_path = os.path.join(TEST_FOLDER, f"llm_single_result_{MAZE_FILE}.txt")
    with open(results_path, "w", encoding="utf-8") as f:
        f.write(f"Test folder: {TEST_FOLDER}\nMaze file: {MAZE_FILE}\nPrompt: {PROMPT}\n\n")
        f.write(f"{'='*30}\nMaze input\n{'='*30}\n")
        f.write(maze_input + "\n")
        llm_response = call_gemini(LLM_NAME, PROMPT, maze_input)
        f.write(f"\n--- LLM: {LLM_NAME} ---\n")
        f.write("LLM Response:\n" + llm_response + "\n")
        llm_steps = [line for line in llm_response.splitlines() if any(x in line.lower() for x in ["up", "down", "left", "right", "forward", "backwards"])]
        score = score_llm_output_strict(llm_steps, solution_steps)
        f.write(f"Score vs solution: {score:.2%}\n")
        f.write(f"\nSolution steps: {', '.join(solution_steps)}\n")
    print(f"Results saved to {results_path}")

if __name__ == "__main__":
    main()
