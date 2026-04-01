"""
@author: valer 29 september 11:52:06 2025
Script to automatically generate multiple mazes of a specified size and save their various representations
"""

from pathlib import Path
from maze_generator_ext_v3 import Maze, OccupancyGridMaze


def create_test_directory(rows, cols):
    """
    Creates a new, uniquely named directory to store maze files and results.

    Returns:
        Path: The path to the newly created directory.
    """

    # Define paths so Data folders are saved relative to this script
    give_your_dataset_a_name = "Dataset 02 - Statistical analysis"
    script_dir = Path(__file__).parent.resolve()    # Get the directory of the current script
    dataset_root = script_dir / give_your_dataset_a_name        # Define the root dataset directory
    dataset_root.mkdir(exist_ok=True)               # Create the root directory if it doesn't exist

    base_name = give_your_dataset_a_name
    dir_name = f"{base_name} {rows}x{cols}"
    dir_path = dataset_root / dir_name
    if not dir_path.exists():
        dir_path.mkdir()
        print(f"Created directory: {dir_path}")
        return dir_path

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
    line_maze = Maze(cols, rows) # Not a mistake. Maze takes (cols, rows)
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

    # Save solution for line-based maze
    with open(directory / f"maze_line_{rows}x{cols}_solution_coords.txt", "w") as f:
        f.write(str(line_maze.get_solution_coordinates()))

    # Save solution for occupancy grid maze, which is created inside the Maze() class. Therefore, its name is maze_line_row_col_maze_occ_solution_coords.txt . 
    with open(directory / f"maze_occupancy_{rows}x{cols}_solution_coords.txt", "w") as f:
        f.write(str(line_maze.get_occ_solution_coordinates()))

    print(f"All maze representations saved to '{directory}'.")



def main():
    """
    Main function to run the full maze generation and saving in "current directory"\Dataset 01 .
    """
    i = 2 # Starting size for rows and columns. Minimum maze is 2x2
    j = 4 # Maximum size for rows and columns. Change if needed
    
    while i<=j: # Setting minimum and maximum size for rows and columns
        ROWS = i
        COLS = i
        try:
            test_dir = create_test_directory(i, i)
            generate_and_save_mazes(test_dir, i,i)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
        i+=1            

if __name__ == "__main__":
    main()


