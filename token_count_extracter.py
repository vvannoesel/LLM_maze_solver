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
