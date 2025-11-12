import re

def extract_prompt_token_count(text: str) -> str: 
    """
    Extracts the sequence of moves from the LLM's response between the
    "Final answer:" and "End of final sequence" markers.

    Args:
        text (str): The full response from the LLM.

    Returns:
        text (str): number of output tokens
    """

    match = re.search(r"prompt_token_count\s*=\s*(\d+)", text)
    count= match.group(1).strip()
    if match:
        return count
    return "" # Return whitespace if none is found to avoid error



def extract_output_token_count(text: str, prompt_token_count) -> tuple: 
    """
    Extracts the sequence of moves from the LLM's response between the
    "Final answer:" and "End of final sequence" markers.

    Args:
        text (str): The full response from the LLM.

    Returns:
        tuple: a tuple of two strings (str, str)
    """
    
    match1 = re.search(r"total_token_count\s*=\s*(\d+)", text) 
    count = match1.group(1).strip()
    number_of_output_tokens = str(int(count) - int(prompt_token_count) )
    if match1:
        return count, number_of_output_tokens
    return "" # Return whitespace if none is found to avoid error

# A code that must be run on its own bc it has a main(). It extracts the token output count from .md files. 

"""
extract_outputs.py

Searches files:
  ./Dataset02 - Statistical analysis/Dataset02 5x5 {i}/comparison_results_reasoning_ego_{i}.md
for i in 1..30 and extracts the first occurrence of the pattern:
  ", ouput: {number}`"
The extracted {number} is saved into a numpy array at index i-1.

Output:
  - prints the final array to terminal
"""

from pathlib import Path
import re
import numpy as np
import sys

# Regex:
#   looks for ", output: <number>`"
#   supports integer, decimal, and scientific notation (e.g. 1.23e-4)
RE_OUTPUT = re.compile(r",\s*ouput:\s(.*?)`")

# number of files
N = 30

def main():
    # Determine base directory (script location if available, else cwd)
    try:
        base_dir = Path(__file__).parent
    except NameError:
        base_dir = Path.cwd()

    results = np.full(N, np.nan, dtype=float)

    for i in range(1, N + 1):
        rel_path = Path("Dataset 02 - Statistical analysis") / f"Dataset 02 5x5 {i}" / f"comparison_results_nonreasoning_coords_{i}.md"
        file_path = (base_dir / rel_path).resolve()

        if not file_path.exists():
            print(f"[WARN] File not found for i={i}: {file_path}", file=sys.stderr)
            continue

        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"[ERROR] Could not read file for i={i}: {file_path} -> {e}", file=sys.stderr)
            continue

        m = RE_OUTPUT.search(text)
        if m:
            num_str = m.group(1)
            try:
                value = float(num_str)
                results[i - 1] = value
                print(f"[OK] i={i}: extracted {value}")
            except ValueError:
                print(f"[WARN] i={i}: found numeric string but failed to parse: '{num_str}'", file=sys.stderr)
        else:
            print(f"[WARN] i={i}: pattern not found in file: {file_path}", file=sys.stderr)

    # Final array
    print("\nFinal NumPy array (length = {}):".format(N))
    print(results)


if __name__ == "__main__":
    main()