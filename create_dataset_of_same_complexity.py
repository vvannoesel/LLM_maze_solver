"""
@author: valer 29 september 11:52:06 2025
Script to automatically generate multiple mazes of a specified size and save their various representations
"""

from pathlib import Path
from maze_generator_ext_v3 import Maze, OccupancyGridMaze
from coords_to_ego_solution import coordinates_to_navigation


def create_test_directory(rows, cols, k):
    """
    Creates a new, uniquely named directory to store maze files and results.

    Returns:
        Path: The path to the newly created directory.
    """

    # Define paths so Data folders are saved relative to this script
    give_your_dataset_a_name = "Dataset 03"         # Change this to your desired dataset folder name
    script_dir = Path(__file__).parent.resolve()    # Get the directory of the current script
    dataset_root = script_dir / give_your_dataset_a_name        # Define the root dataset directory
    dataset_root.mkdir(exist_ok=True)               # Create the root directory if it doesn't exist


    postfix = f"{k}"
    base_name = give_your_dataset_a_name
    dir_name = f"{base_name} {rows}x{cols} {k}"  #Adds 'k' to name so every folder has a different name. Otherwise it throws an error beacause each saved maze will overwrite the next. 
    print(dir_name)
    dir_path = dataset_root / dir_name
    if not dir_path.exists():
        dir_path.mkdir()
        print(f"Created directory: {dir_path}")

    return dir_path

def generate_and_save_mazes(directory: Path, cols: int, rows: int, k: int):
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
        postfix = k #f"{k}"

        # Comment out any representations that you do not want to save
        maze_obj.to_jpeg(f"{prefix}_{postfix}.jpg")
        maze_obj.to_json(f"{prefix}_{postfix}.json")
        maze_obj.to_adjacency_list(f"{prefix}_adj_{postfix}.json")
        maze_obj.to_custom_adjacency_list(f"{prefix}_adj_{postfix}.txt")
        maze_obj.to_tokenized_representation(f"{prefix}_tokenized_{postfix}.txt")
        with open(f"{prefix}_ascii_{postfix}.txt", "w", encoding="utf-8") as f:
            f.write(maze_obj.to_ascii())

        solution_steps = maze_obj.get_solution_steps()
        with open(f"{prefix}_solution_steps_{postfix}.txt", "w", encoding="utf-8") as f:
            f.write(", ".join(solution_steps))

    # Save solution for line-based maze
    with open(directory / f"maze_line_{rows}x{cols}_solution_coords_{postfix}.txt", "w") as f:
        f.write(str(line_maze.get_solution_coordinates()))

    # Create line-maze egocentric navigation solution and save to file
    coords_sol = line_maze.get_solution_coordinates()
    coordinates_to_navigation(coords_sol, postfix, rows, cols, mazetype="line")


    # Save solution for occupancy grid maze, which is created inside the Maze() class. Therefore, its name is maze_line_row_col_maze_occ_solution_coords.txt . 
    with open(directory / f"maze_occupancy_{rows}x{cols}_solution_coords_{postfix}.txt", "w") as f:
        f.write(str(line_maze.get_occ_solution_coordinates()))

    # Create occupancy-maze egocentric navigation solution and save to file
    coords_sol = line_maze.get_occ_solution_coordinates()
    coordinates_to_navigation(coords_sol, postfix, rows, cols, mazetype="occupancy")

    print(f"All maze representations saved to '{directory}'.")




def main():
    """
    Main function to run the full maze generation and saving in "current directory"\Dataset 03 .
    """

    ROWS = 3
    COLS = 3
    low_postfix =  42 # Change this to your desired postfix value /// This is the lower value for 'k' 
    high_postfix = 71 # Change this to your desired postfix value /// This is the upper value for 'k'

    for i in range(low_postfix, high_postfix):  # Repeat, each time with a different 'k' value
        print(f"\n=== Run {i} ===")
        try:
            test_dir = create_test_directory(ROWS, COLS, i)
            generate_and_save_mazes(test_dir, ROWS, COLS, i)
        except Exception as e:
            print(f"An unexpected error occurred in run {i}: {e}")

if __name__ == "__main__":
    main()