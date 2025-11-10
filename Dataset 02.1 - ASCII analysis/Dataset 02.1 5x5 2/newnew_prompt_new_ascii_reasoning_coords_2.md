# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `The following is an ASCII representation of a maze:  - '|' represents a vertical wall, '-' represents a horizontal wall, that both can not be passed through.  - ' ' (space) represents an open path that can be passed through.  - '+' represents a corner of the cells of the maze.  - 'O' is the starting point.  - 'T' is the end point (target). Please solve the maze by providing a path from the starting point to the end point. The path should be provided as a list of coordinates of each step, where the coordinate is a (row, col) tuple, and row, col are zero-based indices. Consider the origin (0, 0) to be the top-left corner. Overall, the path should be provided in the format of [(row1, col1), (row2, col2), ...]. A valid path must: - Start at starting point 'O'.  - End at end point 'T'.  - Avoid the walls '|' and '-'.  - Pass only through empty space ' '.  - Move one square at a time.  - Only move up, down, left, and right, not diagonally. Correct your answer if you spot any errors. Here is the maze in ASCII format: `

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_2.txt` | **0.00%** | `input: 343 , ouput: 12775` | `[(1, 1), (9, 9), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
Here is the step-by-step solution to the maze:

The path is a list of coordinates (row, col) moving from the starting point 'O' at (1, 1) to the target 'T' at (9, 9). The path only moves through open spaces, one step at a time, avoiding all walls ('|', '-', '+').

The correct path is as follows:
```
[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9)]
```
```

**Internal Thoughts:**
```
**My approach to solving this maze started with understanding its representation:** I carefully analyzed the ASCII characters, identifying walls, paths, start, and target, and how they relate to a grid. The key was recognizing the need to translate the irregular ASCII grid into a more usable coordinate system. I figured out the cell structure and how to map cell coordinates to ASCII coordinates.

**Next, I parsed the maze and built a representation for pathfinding:** I determined that a 5x5 cell grid made the most sense, and found the ASCII coordinates of the start ('O') and the target ('T'). I used this information to set up the grid system to work with.

**I then represented the maze as a graph:** I considered graph and 2D grid representations and chose a 2D grid representation which can be worked with. This also meant translating the information about the walls into the grid to define what paths are possible. I thought Breadth-First Search (BFS) was a suitable algorithm for finding the shortest path and started thinking through the steps of BFS. The process involved identifying valid moves, boundary checks, and using BFS which is the best option for the shortest path.

**To solve the maze, I considered a visual path-tracing (both high-level, and at the coordinate level), and considered a DFS for a single path:** To find the path, I tried visual path tracing and DFS to manually solve. I quickly realized this method was prone to errors, and that BFS provided a better way to systematically explore all possibilities and find the shortest path.

**Finally, I coded BFS using a Python-like pseudocode:** After initial error, I used this to carefully implement the Breadth-First Search, simulating a queue and visited set. I performed a meticulous visual trace of the BFS algorithm, layer by layer, meticulously tracking the coordinates and validating each move against the maze rules. Then, I manually traced the search on the grid.

**After several iterations of verification, tracing, and correction I was able to find a correct shortest path:** I carefully analyzed the neighbors of each cell and double-checked the steps to ensure a correct and the shortest possible solution. I then constructed the final path, converting it into a list of (row, col) coordinates as requested. After, I did a full, final validation, step-by-step. The final path, and its format, was verified and reviewed in detail multiple times.

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**My approach to solving this maze started with understanding its representation:** I carefully analyzed the ASCII characters, identifying walls, paths, start, and target, and how they relate to a grid. The key was recognizing the need to translate the irregular ASCII grid into a more usable coordinate system. I figured out the cell structure and how to map cell coordinates to ASCII coordinates.

**Next, I parsed the maze and built a representation for pathfinding:** I determined that a 5x5 cell grid made the most sense, and found the ASCII coordinates of the start ('O') and the target ('T'). I used this information to set up the grid system to work with.

**I then represented the maze as a graph:** I considered graph and 2D grid representations and chose a 2D grid representation which can be worked with. This also meant translating the information about the walls into the grid to define what paths are possible. I thought Breadth-First Search (BFS) was a suitable algorithm for finding the shortest path and started thinking through the steps of BFS. The process involved identifying valid moves, boundary checks, and using BFS which is the best option for the shortest path.

**To solve the maze, I considered a visual path-tracing (both high-level, and at the coordinate level), and considered a DFS for a single path:** To find the path, I tried visual path tracing and DFS to manually solve. I quickly realized this method was prone to errors, and that BFS provided a better way to systematically explore all possibilities and find the shortest path.

**Finally, I coded BFS using a Python-like pseudocode:** After initial error, I used this to carefully implement the Breadth-First Search, simulating a queue and visited set. I performed a meticulous visual trace of the BFS algorithm, layer by layer, meticulously tracking the coordinates and validating each move against the maze rules. Then, I manually traced the search on the grid.

**After several iterations of verification, tracing, and correction I was able to find a correct shortest path:** I carefully analyzed the neighbors of each cell and double-checked the steps to ensure a correct and the shortest possible solution. I then constructed the final path, converting it into a list of (row, col) coordinates as requested. After, I did a full, final validation, step-by-step. The final path, and its format, was verified and reviewed in detail multiple times.
""",
        thought=True
      ),
      Part(
        text="""Here is the step-by-step solution to the maze:

The path is a list of coordinates (row, col) moving from the starting point 'O' at (1, 1) to the target 'T' at (9, 9). The path only moves through open spaces, one step at a time, avoiding all walls ('|', '-', '+').

The correct path is as follows:
```
[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='Hn0IabuODYjOxN8Ph962yAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=192,
  prompt_token_count=343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=343
    ),
  ],
  thoughts_token_count=12583,
  total_token_count=13118
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=192 candidates_tokens_details=None prompt_token_count=343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=343
)] thoughts_token_count=12583 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13118 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**My approach to solving this maze started with understanding its representation:** I carefully analyzed the ASCII characters, identifying walls, paths, start, and target, and how they relate to a grid. The key was recognizing the need to translate the irregular ASCII grid into a more usable coordinate system. I figured out the cell structure and how to map cell coordinates to ASCII coordinates.

**Next, I parsed the maze and built a representation for pathfinding:** I determined that a 5x5 cell grid made the most sense, and found the ASCII coordinates of the start ('O') and the target ('T'). I used this information to set up the grid system to work with.

**I then represented the maze as a graph:** I considered graph and 2D grid representations and chose a 2D grid representation which can be worked with. This also meant translating the information about the walls into the grid to define what paths are possible. I thought Breadth-First Search (BFS) was a suitable algorithm for finding the shortest path and started thinking through the steps of BFS. The process involved identifying valid moves, boundary checks, and using BFS which is the best option for the shortest path.

**To solve the maze, I considered a visual path-tracing (both high-level, and at the coordinate level), and considered a DFS for a single path:** To find the path, I tried visual path tracing and DFS to manually solve. I quickly realized this method was prone to errors, and that BFS provided a better way to systematically explore all possibilities and find the shortest path.

**Finally, I coded BFS using a Python-like pseudocode:** After initial error, I used this to carefully implement the Breadth-First Search, simulating a queue and visited set. I performed a meticulous visual trace of the BFS algorithm, layer by layer, meticulously tracking the coordinates and validating each move against the maze rules. Then, I manually traced the search on the grid.

**After several iterations of verification, tracing, and correction I was able to find a correct shortest path:** I carefully analyzed the neighbors of each cell and double-checked the steps to ensure a correct and the shortest possible solution. I then constructed the final path, converting it into a list of (row, col) coordinates as requested. After, I did a full, final validation, step-by-step. The final path, and its format, was verified and reviewed in detail multiple times.
""",
        thought=True
      ),
      Part(
        text="""Here is the step-by-step solution to the maze:

The path is a list of coordinates (row, col) moving from the starting point 'O' at (1, 1) to the target 'T' at (9, 9). The path only moves through open spaces, one step at a time, avoiding all walls ('|', '-', '+').

The correct path is as follows:
```
[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

