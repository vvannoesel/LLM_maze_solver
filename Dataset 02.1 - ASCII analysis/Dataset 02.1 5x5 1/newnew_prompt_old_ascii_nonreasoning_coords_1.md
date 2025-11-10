# LLM Maze Solving Comparison Report

 NEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-flash-lite`

**Prompt Used:** `The following is an ASCII representation of a maze:  - '|' represents a vertical wall, '-' represents a horizontal wall, that both can not be passed through.  - ' ' (space) represents an open path that can be passed through.  - '+' represents a corner of the cells of the maze.  - 'O' is the starting point.  - 'T' is the end point (target). Please solve the maze by providing a path from the starting point to the end point. The path should be provided as a list of coordinates of each step, where the coordinate is a (row, col) tuple, and row, col are zero-based indices. Consider the origin (0, 0) to be the top-left corner. Overall, the path should be provided in the format of [(row1, col1), (row2, col2), ...]. A valid path must: - Start at starting point 'O'.  - End at end point 'T'.  - Avoid the walls '|' and '-'.  - Pass only through empty space ' '.  - Move one square at a time.  - Only move up, down, left, and right, not diagonally. Correct your answer if you spot any errors. Here is the maze in ASCII format: `

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_1.txt` | **0.00%** | `input: 341 , ouput: 1176` | `(1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 6), (9, 6), (9, 7)` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)
```

**Extracted Answer:**
```
(1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 6), (9, 6), (9, 7)
```

**Full Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""```python
maze = [
    "+-+-+-+-+-+",
    "|O|   |   |",
    "+ + + +-+ +",
    "|   |     |",
    "+-+-+-+-+ +",
    "|       | |",
    "+ +-+-+-+ +",
    "|       | |",
    "+ +-+-+ + +",
    "|     |  T|",
    "+-+-+-+-+-+"
]

# Convert maze to a 2D grid for easier processing
grid = [list(row) for row in maze]

# Find start and target coordinates
start = None
target = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            start = (r, c)
        elif grid[r][c] == 'T':
            target = (r, c)

# --- Maze Solving Algorithm (Breadth-First Search) ---

def solve_maze(grid, start, target):
    rows = len(grid)
    cols = len(grid[0])

    # Queue for BFS: (current_row, current_col, path_to_here)
    queue = [(start[0], start[1], [start])]

    # Set to keep track of visited cells
    visited = set()
    visited.add(start)

    while queue:
        r, c, path = queue.pop(0)

        # If we reached the target, return the path
        if (r, c) == target:
            return path

        # Define possible moves (up, down, left, right)
        moves = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for nr, nc in moves:
            # Check if the move is within bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                # Check if the next cell is not a wall and hasn't been visited
                if grid[nr][nc] != '|' and grid[nr][nc] != '-' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    queue.append((nr, nc, new_path))

    # If no path is found
    return None

# Solve the maze
path = solve_maze(grid, start, target)

# Print the path
if path:
    print(path)
else:
    print("No path found.")

```

**Explanation of the Solution:**

1.  **Maze Representation:** The input ASCII maze is converted into a 2D list (`grid`) for easier access to individual cells.

2.  **Finding Start and Target:** The code iterates through the `grid` to find the `(row, col)` coordinates of the 'O' (start) and 'T' (target).

3.  **Breadth-First Search (BFS):**
    *   **Queue:** A queue is used to store the cells to be explored. Each element in the queue is a tuple `(row, col, path_to_here)`, where `path_to_here` is a list of coordinates representing the path taken to reach that cell.
    *   **Visited Set:** A `set` called `visited` is used to keep track of cells that have already been explored. This prevents infinite loops and redundant exploration.
    *   **Exploration:**
        *   The algorithm starts by adding the `start` node to the queue.
        *   In each step, it dequeues a cell and its path.
        *   If the dequeued cell is the `target`, the `path` to it is returned.
        *   Otherwise, it considers all possible valid moves (up, down, left, right).
        *   For each valid move (within bounds, not a wall, and not visited):
            *   The new cell is marked as visited.
            *   A new path is created by appending the new cell's coordinates to the current path.
            *   The new cell and its path are enqueued.

4.  **Output:**
    *   If a path is found, the list of coordinates is printed.
    *   If no path is found after exploring all reachable cells, "No path found." is printed.

The output for the given maze is:

```
[(1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 6), (9, 6), (9, 7)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AooIabaALp_f7M8PlNPF8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=1176,
  prompt_token_count=341,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=341
    ),
  ],
  total_token_count=1517
) automatic_function_calling_history=[] parsed=None
```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""```python
maze = [
    "+-+-+-+-+-+",
    "|O|   |   |",
    "+ + + +-+ +",
    "|   |     |",
    "+-+-+-+-+ +",
    "|       | |",
    "+ +-+-+-+ +",
    "|       | |",
    "+ +-+-+ + +",
    "|     |  T|",
    "+-+-+-+-+-+"
]

# Convert maze to a 2D grid for easier processing
grid = [list(row) for row in maze]

# Find start and target coordinates
start = None
target = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            start = (r, c)
        elif grid[r][c] == 'T':
            target = (r, c)

# --- Maze Solving Algorithm (Breadth-First Search) ---

def solve_maze(grid, start, target):
    rows = len(grid)
    cols = len(grid[0])

    # Queue for BFS: (current_row, current_col, path_to_here)
    queue = [(start[0], start[1], [start])]

    # Set to keep track of visited cells
    visited = set()
    visited.add(start)

    while queue:
        r, c, path = queue.pop(0)

        # If we reached the target, return the path
        if (r, c) == target:
            return path

        # Define possible moves (up, down, left, right)
        moves = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for nr, nc in moves:
            # Check if the move is within bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                # Check if the next cell is not a wall and hasn't been visited
                if grid[nr][nc] != '|' and grid[nr][nc] != '-' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    queue.append((nr, nc, new_path))

    # If no path is found
    return None

# Solve the maze
path = solve_maze(grid, start, target)

# Print the path
if path:
    print(path)
else:
    print("No path found.")

```

**Explanation of the Solution:**

1.  **Maze Representation:** The input ASCII maze is converted into a 2D list (`grid`) for easier access to individual cells.

2.  **Finding Start and Target:** The code iterates through the `grid` to find the `(row, col)` coordinates of the 'O' (start) and 'T' (target).

3.  **Breadth-First Search (BFS):**
    *   **Queue:** A queue is used to store the cells to be explored. Each element in the queue is a tuple `(row, col, path_to_here)`, where `path_to_here` is a list of coordinates representing the path taken to reach that cell.
    *   **Visited Set:** A `set` called `visited` is used to keep track of cells that have already been explored. This prevents infinite loops and redundant exploration.
    *   **Exploration:**
        *   The algorithm starts by adding the `start` node to the queue.
        *   In each step, it dequeues a cell and its path.
        *   If the dequeued cell is the `target`, the `path` to it is returned.
        *   Otherwise, it considers all possible valid moves (up, down, left, right).
        *   For each valid move (within bounds, not a wall, and not visited):
            *   The new cell is marked as visited.
            *   A new path is created by appending the new cell's coordinates to the current path.
            *   The new cell and its path are enqueued.

4.  **Output:**
    *   If a path is found, the list of coordinates is printed.
    *   If no path is found after exploring all reachable cells, "No path found." is printed.

The output for the given maze is:

```
[(1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 6), (9, 6), (9, 7)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AooIabaALp_f7M8PlNPF8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=1176,
  prompt_token_count=341,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=341
    ),
  ],
  total_token_count=1517
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=267 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=1176 candidates_tokens_details=None prompt_token_count=341 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=341
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1517 traffic_type=None
```

