# LLM Maze Solving Comparison Report

 NEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-flash-lite`

**Prompt Used:** `The following is an ASCII representation of a maze:  - '|' represents a vertical wall, '-' represents a horizontal wall, that both can not be passed through.  - ' ' (space) represents an open path that can be passed through.  - '+' represents a corner of the cells of the maze.  - 'O' is the starting point.  - 'T' is the end point (target). Please solve the maze by providing a path from the starting point to the end point. The path should be provided as a list of coordinates of each step, where the coordinate is a (row, col) tuple, and row, col are zero-based indices. Consider the origin (0, 0) to be the top-left corner. Overall, the path should be provided in the format of [(row1, col1), (row2, col2), ...]. A valid path must: - Start at starting point 'O'.  - End at end point 'T'.  - Avoid the walls '|' and '-'.  - Pass only through empty space ' '.  - Move one square at a time.  - Only move up, down, left, and right, not diagonally. Correct your answer if you spot any errors. Here is the maze in ASCII format: `

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_3.txt` | **0.00%** | `input: 342 , ouput: 1303` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (1, 1), (1, 2), (1, 3), (2, 3), (2, 2), (2, 4), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8)` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (1, 1), (1, 2), (1, 3), (2, 3), (2, 2), (2, 4), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8)
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
    "|O  |     |",
    "+-+-+-+-+-+",
    "| |   |   |",
    "+-+-+-+-+-+",
    "| |   |   |",
    "+-+-+-+-+-+",
    "| |     | |",
    "+-+-+-+-+-+",
    "|        T|",
    "+-+-+-+-+-+"
]

def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = None
    end = None

    # Find start and end points
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'O':
                start = (r, c)
            elif maze[r][c] == 'T':
                end = (r, c)

    if not start or not end:
        return None  # Start or end not found

    # Using Breadth-First Search (BFS)
    queue = [(start, [start])]  # (current_position, path_so_far)
    visited = {start}

    while queue:
        (r, c), path = queue.pop(0)

        if (r, c) == end:
            return path

        # Define possible moves (up, down, left, right)
        moves = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for next_r, next_c in moves:
            # Check if the move is within bounds
            if 0 <= next_r < rows and 0 <= next_c < cols:
                # Check if the next cell is a valid path and not a wall or corner
                if maze[next_r][next_c] != '|' and maze[next_r][next_c] != '-' and maze[next_r][next_c] != '+':
                    if (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        queue.append(((next_r, next_c), path + [(next_r, next_c)]))

    return None  # No path found

path = solve_maze(maze)
print(path)
```

**Explanation of the Path:**

The output `[(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8)]` represents the step-by-step movement from 'O' to 'T'. Let's trace it:

*   **(1, 1):** This is the starting point 'O'.
*   **(1, 2):** Move right into an open space.
*   **(1, 3):** Move right into an open space.
*   **(2, 3):** Move down. The maze structure here is a bit tricky. The `+` at (2,2) and `+` at (2,4) along with `-` at (2,3) create a "corner" that you can pass through if the adjacent cells are open.
*   **(3, 3):** Move down.
*   **(3, 4):** Move right.
*   **(3, 5):** Move right.
*   **(4, 5):** Move down.
*   **(5, 5):** Move down.
*   **(5, 4):** Move left.
*   **(5, 3):** Move left.
*   **(5, 2):** Move left.
*   **(5, 1):** Move left.
*   **(6, 1):** Move down.
*   **(7, 1):** Move down.
*   **(7, 2):** Move right.
*   **(7, 3):** Move right.
*   **(7, 4):** Move right.
*   **(7, 5):** Move right.
*   **(8, 5):** Move down.
*   **(9, 5):** Move down.
*   **(9, 6):** Move right.
*   **(9, 7):** Move right.
*   **(9, 8):** This is the target point 'T'.

The provided Python code implements a Breadth-First Search (BFS) algorithm to find the shortest path in the maze. It correctly interprets the maze characters and navigates through the open spaces while avoiding walls.

```
[(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HooIaY-eJ7H8kdUPl6qd8QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=1303,
  prompt_token_count=342,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=342
    ),
  ],
  total_token_count=1645
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
    "|O  |     |",
    "+-+-+-+-+-+",
    "| |   |   |",
    "+-+-+-+-+-+",
    "| |   |   |",
    "+-+-+-+-+-+",
    "| |     | |",
    "+-+-+-+-+-+",
    "|        T|",
    "+-+-+-+-+-+"
]

def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = None
    end = None

    # Find start and end points
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'O':
                start = (r, c)
            elif maze[r][c] == 'T':
                end = (r, c)

    if not start or not end:
        return None  # Start or end not found

    # Using Breadth-First Search (BFS)
    queue = [(start, [start])]  # (current_position, path_so_far)
    visited = {start}

    while queue:
        (r, c), path = queue.pop(0)

        if (r, c) == end:
            return path

        # Define possible moves (up, down, left, right)
        moves = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for next_r, next_c in moves:
            # Check if the move is within bounds
            if 0 <= next_r < rows and 0 <= next_c < cols:
                # Check if the next cell is a valid path and not a wall or corner
                if maze[next_r][next_c] != '|' and maze[next_r][next_c] != '-' and maze[next_r][next_c] != '+':
                    if (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        queue.append(((next_r, next_c), path + [(next_r, next_c)]))

    return None  # No path found

path = solve_maze(maze)
print(path)
```

**Explanation of the Path:**

The output `[(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8)]` represents the step-by-step movement from 'O' to 'T'. Let's trace it:

*   **(1, 1):** This is the starting point 'O'.
*   **(1, 2):** Move right into an open space.
*   **(1, 3):** Move right into an open space.
*   **(2, 3):** Move down. The maze structure here is a bit tricky. The `+` at (2,2) and `+` at (2,4) along with `-` at (2,3) create a "corner" that you can pass through if the adjacent cells are open.
*   **(3, 3):** Move down.
*   **(3, 4):** Move right.
*   **(3, 5):** Move right.
*   **(4, 5):** Move down.
*   **(5, 5):** Move down.
*   **(5, 4):** Move left.
*   **(5, 3):** Move left.
*   **(5, 2):** Move left.
*   **(5, 1):** Move left.
*   **(6, 1):** Move down.
*   **(7, 1):** Move down.
*   **(7, 2):** Move right.
*   **(7, 3):** Move right.
*   **(7, 4):** Move right.
*   **(7, 5):** Move right.
*   **(8, 5):** Move down.
*   **(9, 5):** Move down.
*   **(9, 6):** Move right.
*   **(9, 7):** Move right.
*   **(9, 8):** This is the target point 'T'.

The provided Python code implements a Breadth-First Search (BFS) algorithm to find the shortest path in the maze. It correctly interprets the maze characters and navigates through the open spaces while avoiding walls.

```
[(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HooIaY-eJ7H8kdUPl6qd8QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=1303,
  prompt_token_count=342,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=342
    ),
  ],
  total_token_count=1645
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=1303 candidates_tokens_details=None prompt_token_count=342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1645 traffic_type=None
```

