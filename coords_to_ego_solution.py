from pathlib import Path


def coordinates_to_navigation(coords):
    """
    Converts a sequence of coordinates into navigation steps.
    The agent starts at (0, 0) facing SOUTH.
    
    Directions:
        - forward: move one step forward
        - left: turn left 90° and move one step
        - right: turn right 90° and move one step
        - back: turn 180° and move one step

    Args:
        coords (list of tuples): e.g. [(0,0), (0,1), (1,1), (1,0)]

    Returns:
        str: comma-separated list of navigation steps
    """
    if not coords or coords[0] != (0, 0):
        raise ValueError("Coordinates must start at (0, 0).")
    
    # Define direction order: N=0, E=1, S=2, W=3 (clockwise)
    direction_order = ['N', 'E', 'S', 'W']
    
    # Start facing South
    current_dir = 2  # index for 'S'
    steps = []

    for i in range(1, len(coords)):
        row1, col1 = coords[i-1]    # current location
        row2, col2 = coords[i]      # next location

        # Determine movement direction
        if (row2, col2) == (row1 - 1, col1):
            target_dir = 0  # North
        elif (row2, col2) == (row1, col1 + 1):
            target_dir = 1  # East
        elif (row2, col2) == (row1 + 1, col1):
            target_dir = 2  # South
        elif (row2, col2) == (row1, col1 - 1):
            target_dir = 3  # West
        else:
            raise ValueError(f"Invalid move from {(row1, col1)} to {(row2, col2)} — must be adjacent.")

        # Determine turn type
        diff = (target_dir - current_dir) % 4
        if diff == 0:
            steps.append("forward")
        elif diff == 1:
            steps.append("right")
        elif diff == 2:
            steps.append("backward")
        elif diff == 3:
            steps.append("left")

        # Update facing direction
        current_dir = target_dir


        # Save navigation directions to file inside preferred folder
        script_dir = Path(__file__).parent.resolve()
        dataset_root = script_dir / "Dataset 02 - Statistical analysis"    
        base_name = "Dataset 02 5x5 30"
        directory = dataset_root / base_name
        with open(directory/f"maze_line_solution_nav_30.txt", "w", encoding="utf-8") as f:
            f.write(", ".join(steps))

    return ", ".join(steps)




# path=[(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]



# print (coordinates_to_navigation(path))
