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

        j = 13

        # Save navigation directions to file inside preferred folder
        script_dir = Path(__file__).parent.resolve()
        dataset_root = script_dir / "Dataset 03"    
        base_name = f"Dataset 03 15x15 {j}"
        directory = dataset_root / base_name
        with open(directory/f"maze_line_15x15_solution_ego_{j}.txt", "w", encoding="utf-8") as f:
        # with open(directory/f"maze_occupancy_15x15_solution_ego_{j}.txt", "w", encoding="utf-8") as f:
            f.write(", ".join(steps))

    return ", ".join(steps)




path=[(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (9, 2), (9, 3), (8, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 4), (4, 4), (4, 5), (3, 5), (3, 6), (4, 6), (5, 6), (5, 7), (6, 7), (6, 8), (6, 9), (6, 10), (5, 10), (5, 11), (6, 11), (7, 11), (7, 12), (6, 12), (5, 12), (4, 12), (4, 11), (4, 10), (4, 9), (5, 9), (5, 8), (4, 8), (4, 7), (3, 7), (3, 8), (2, 8), (1, 8), (0, 8), (0, 9), (0, 10), (1, 10), (1, 9), (2, 9), (2, 10), (3, 10), (3, 11), (2, 11), (1, 11), (1, 12), (2, 12), (3, 12), (3, 13), (3, 14), (4, 14), (4, 13), (5, 13), (6, 13), (7, 13), (7, 14), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (9, 9), (9, 8), (9, 7), (10, 7), (10, 6), (11, 6), (11, 5), (12, 5), (12, 4), (11, 4), (10, 4), (10, 3), (11, 3), (12, 3), (13, 3), (13, 4), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (13, 8), (13, 7), (12, 7), (12, 8), (11, 8), (11, 9), (11, 10), (12, 10), (12, 11), (12, 12), (11, 12), (11, 13), (11, 14), (12, 14), (12, 13), (13, 13), (13, 12), (13, 11), (14, 11), (14, 12), (14, 13), (14, 14)]













print (coordinates_to_navigation(path))
