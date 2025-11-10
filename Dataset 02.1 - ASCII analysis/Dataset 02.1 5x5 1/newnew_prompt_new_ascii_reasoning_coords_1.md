# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `The following is an ASCII representation of a maze:  - '|' represents a vertical wall, '-' represents a horizontal wall, that both can not be passed through.  - ' ' (space) represents an open path that can be passed through.  - '+' represents a corner of the cells of the maze.  - 'O' is the starting point.  - 'T' is the end point (target). Please solve the maze by providing a path from the starting point to the end point. The path should be provided as a list of coordinates of each step, where the coordinate is a (row, col) tuple, and row, col are zero-based indices. Consider the origin (0, 0) to be the top-left corner. Overall, the path should be provided in the format of [(row1, col1), (row2, col2), ...]. A valid path must: - Start at starting point 'O'.  - End at end point 'T'.  - Avoid the walls '|' and '-'.  - Pass only through empty space ' '.  - Move one square at a time.  - Only move up, down, left, and right, not diagonally. Correct your answer if you spot any errors. Here is the maze in ASCII format: `

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_1.txt` | **9.09%** | `input: 340 , ouput: 8342` | `[(0, 0), (4, 4), (0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_1.txt`

**Score:** 9.09%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
An elegant path from 'O' to 'T' can be found by navigating through the open passages of the maze. The path is determined by moving from one cell to an adjacent cell (up, down, left, or right) where no wall obstructs the way. The solution provided below represents the shortest possible path.

Here is the step-by-step path from the start point 'O' at (0, 0) to the target 'T' at (4, 4), represented as a list of (row, col) coordinates:

```json
[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]
```
```

**Internal Thoughts:**
```
**Maze Solving and Pathfinding**

Okay, here's what I'm thinking. I've got this ASCII maze, and my job is to get from the 'O' to the 'T'. First, I've got to understand how this ASCII representation translates into something I can work with. The walls are pipes and dashes, the paths are spaces, and the corners are plus signs – got it. I'm going to convert this ASCII grid into a regular 2D grid of cells. The key insight is that the cell contents are at odd row and odd column indices in the ASCII grid. Specifically, cell `(r, c)` corresponds to the character at `ASCII_grid[2*r + 1][2*c + 1]`. That makes the start at `(0, 0)` and the target at `(4, 4)`.

Now, how do I find the path? Breadth-First Search (BFS) is perfect for this. It'll give me the shortest path because it explores systematically.  I'll use a queue and a visited set to keep track of where I've been. For each cell, I'll check its neighbors. I need to make sure I don't run into walls, and I haven't been there already.  I'll translate this into code.

Let's trace it manually, to be sure. I'm imagining starting at `O`, and then checking if a move is blocked by a wall.  I'll make moves step by step, keeping track of how the queue and visited set will evolve. It's a bit tedious, but it gives me confidence that I'm getting a correct and optimal path.

After tracing, it is clear that my algorithm will work. I'm confident about my neighbor checking and wall detection logic. It should be able to handle all possible paths and find the shortest one. The main function will parse the ASCII maze, setup the BFS algorithm, execute BFS algorithm, and finally return the path.

The simulation and plan seem solid. I will now prepare the code.

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Solving and Pathfinding**

Okay, here's what I'm thinking. I've got this ASCII maze, and my job is to get from the 'O' to the 'T'. First, I've got to understand how this ASCII representation translates into something I can work with. The walls are pipes and dashes, the paths are spaces, and the corners are plus signs – got it. I'm going to convert this ASCII grid into a regular 2D grid of cells. The key insight is that the cell contents are at odd row and odd column indices in the ASCII grid. Specifically, cell `(r, c)` corresponds to the character at `ASCII_grid[2*r + 1][2*c + 1]`. That makes the start at `(0, 0)` and the target at `(4, 4)`.

Now, how do I find the path? Breadth-First Search (BFS) is perfect for this. It'll give me the shortest path because it explores systematically.  I'll use a queue and a visited set to keep track of where I've been. For each cell, I'll check its neighbors. I need to make sure I don't run into walls, and I haven't been there already.  I'll translate this into code.

Let's trace it manually, to be sure. I'm imagining starting at `O`, and then checking if a move is blocked by a wall.  I'll make moves step by step, keeping track of how the queue and visited set will evolve. It's a bit tedious, but it gives me confidence that I'm getting a correct and optimal path.

After tracing, it is clear that my algorithm will work. I'm confident about my neighbor checking and wall detection logic. It should be able to handle all possible paths and find the shortest one. The main function will parse the ASCII maze, setup the BFS algorithm, execute BFS algorithm, and finally return the path.

The simulation and plan seem solid. I will now prepare the code.
""",
        thought=True
      ),
      Part(
        text="""An elegant path from 'O' to 'T' can be found by navigating through the open passages of the maze. The path is determined by moving from one cell to an adjacent cell (up, down, left, or right) where no wall obstructs the way. The solution provided below represents the shortest possible path.

Here is the step-by-step path from the start point 'O' at (0, 0) to the target 'T' at (4, 4), represented as a list of (row, col) coordinates:

```json
[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='vHwIacinIpDzxN8PleaJ0Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=174,
  prompt_token_count=340,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=340
    ),
  ],
  thoughts_token_count=8168,
  total_token_count=8682
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=174 candidates_tokens_details=None prompt_token_count=340 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=340
)] thoughts_token_count=8168 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8682 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Solving and Pathfinding**

Okay, here's what I'm thinking. I've got this ASCII maze, and my job is to get from the 'O' to the 'T'. First, I've got to understand how this ASCII representation translates into something I can work with. The walls are pipes and dashes, the paths are spaces, and the corners are plus signs – got it. I'm going to convert this ASCII grid into a regular 2D grid of cells. The key insight is that the cell contents are at odd row and odd column indices in the ASCII grid. Specifically, cell `(r, c)` corresponds to the character at `ASCII_grid[2*r + 1][2*c + 1]`. That makes the start at `(0, 0)` and the target at `(4, 4)`.

Now, how do I find the path? Breadth-First Search (BFS) is perfect for this. It'll give me the shortest path because it explores systematically.  I'll use a queue and a visited set to keep track of where I've been. For each cell, I'll check its neighbors. I need to make sure I don't run into walls, and I haven't been there already.  I'll translate this into code.

Let's trace it manually, to be sure. I'm imagining starting at `O`, and then checking if a move is blocked by a wall.  I'll make moves step by step, keeping track of how the queue and visited set will evolve. It's a bit tedious, but it gives me confidence that I'm getting a correct and optimal path.

After tracing, it is clear that my algorithm will work. I'm confident about my neighbor checking and wall detection logic. It should be able to handle all possible paths and find the shortest one. The main function will parse the ASCII maze, setup the BFS algorithm, execute BFS algorithm, and finally return the path.

The simulation and plan seem solid. I will now prepare the code.
""",
        thought=True
      ),
      Part(
        text="""An elegant path from 'O' to 'T' can be found by navigating through the open passages of the maze. The path is determined by moving from one cell to an adjacent cell (up, down, left, or right) where no wall obstructs the way. The solution provided below represents the shortest possible path.

Here is the step-by-step path from the start point 'O' at (0, 0) to the target 'T' at (4, 4), represented as a list of (row, col) coordinates:

```json
[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

