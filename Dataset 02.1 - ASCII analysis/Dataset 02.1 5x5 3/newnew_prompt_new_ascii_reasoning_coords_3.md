# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `The following is an ASCII representation of a maze:  - '|' represents a vertical wall, '-' represents a horizontal wall, that both can not be passed through.  - ' ' (space) represents an open path that can be passed through.  - '+' represents a corner of the cells of the maze.  - 'O' is the starting point.  - 'T' is the end point (target). Please solve the maze by providing a path from the starting point to the end point. The path should be provided as a list of coordinates of each step, where the coordinate is a (row, col) tuple, and row, col are zero-based indices. Consider the origin (0, 0) to be the top-left corner. Overall, the path should be provided in the format of [(row1, col1), (row2, col2), ...]. A valid path must: - Start at starting point 'O'.  - End at end point 'T'.  - Avoid the walls '|' and '-'.  - Pass only through empty space ' '.  - Move one square at a time.  - Only move up, down, left, and right, not diagonally. Correct your answer if you spot any errors. Here is the maze in ASCII format: `

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_3.txt` | **7.69%** | `input: 341 , ouput: 12932` | `[(0, 0), (4, 4), (0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_3.txt`

**Score:** 7.69%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
An analysis of the maze reveals a 5x5 grid of cells. The starting point 'O' is at cell coordinate (0, 0), and the target 'T' is at (4, 4). By using a pathfinding algorithm like Breadth-First Search (BFS), we can find a shortest path from the start to the target.

The path involves navigating down the left side of the maze, and then moving across the bottom row to reach the target.

Here is a valid path from 'O' to 'T' as a list of (row, col) coordinates:
```
[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]
```
```

**Internal Thoughts:**
```
**My Solution for the ASCII Maze**

Alright, let's break this down systematically. My objective is to find a path from 'O' to 'T' in this ASCII maze.

1.  **Maze Interpretation:**  This is a grid, and the pluses, minuses, and bars are walls. Spaces are walkable paths. I've got to figure out where 'O' and 'T' are, but first, I need to translate these ASCII characters to a coordinate system that makes sense for my algorithm. I'm going to set up a mapping from the character grid coordinates to maze cell coordinates. I figured out that a cell at `(row, col)` in my coordinate system corresponds to the character at `(2*row + 1, 2*col + 1)` in the ASCII grid.

2.  **Locating Start and Target:** Using that conversion, I located 'O' (start) at cell (0, 0) and 'T' (target) at cell (4, 4). The maze is 5x5 cells.

3.  **Wall Analysis:** I now know how to tell if there's a wall. To get from a cell `(r, c)` to its neighbor, the ASCII character between them has to be a space. So to go right from `(r, c)`, the character at `(2*r + 1, 2*c + 2)` must be a space. Left is `(2*r + 1, 2*c)`, down is `(2*r + 2, 2*c + 1)`, and up is `(2*r, 2*c + 1)`.

4.  **Choosing a Search Strategy:**  I'll use Breadth-First Search (BFS) for this. BFS guarantees I'll find the shortest path, which is important. I'll represent the maze as a grid and check for walls as I explore.

5.  **Manual Tracing:** I began with a manual trace to verify my understanding and start getting a feel for the maze structure. I started from 'O' at (0,0) and carefully followed possible paths, checking for walls at each step.  I got a bit tangled up in the walls at first! I was able to identify some dead ends, which is normal for this kind of problem.

6.  **BFS Implementation:**
    I'll implement BFS to search the maze, storing paths in a queue and tracking visited cells. Here's my plan:
    *   **Parsing:** Find dimensions (5x5), start, and target and store ASCII.
    *   **Initialize:** Queue starts with `[(0, 0)]` and visited set with `{(0, 0)}`.
    *   **Loop:**
        *   Dequeue a path.
        *   If the last cell is the target, I'm done.
        *   Explore each neighbor: make sure it's in bounds, not visited, and there's no wall.
        *   Add valid neighbor to visited, add new path to queue.

7.  **Mental BFS Execution:**
    I mentally ran through the BFS algorithm step by step. I traced the queue, the visited set, and considered all neighbor wall checks carefully. I was sure to track potential errors and backtrack when required. I mentally performed wall checks on each potential cell I visited. This process was rigorous to ensure all details were handled. After mentally running BFS, I ended up with a valid path. I re-checked my wall interpretations carefully to make sure there are no errors in my plan.

8.  **Building the Path:** After all this, I assembled the final path from the BFS result:
    `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]`

9.  **Verification:** I traced this final path, step-by-step, checking each move against the ASCII maze to make sure it was valid.

10. **Final Answer:** The final path is a list of cell coordinates. The number of coordinates is 11, the number of steps is 10. The path is:
    `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]`

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**My Solution for the ASCII Maze**

Alright, let's break this down systematically. My objective is to find a path from 'O' to 'T' in this ASCII maze.

1.  **Maze Interpretation:**  This is a grid, and the pluses, minuses, and bars are walls. Spaces are walkable paths. I've got to figure out where 'O' and 'T' are, but first, I need to translate these ASCII characters to a coordinate system that makes sense for my algorithm. I'm going to set up a mapping from the character grid coordinates to maze cell coordinates. I figured out that a cell at `(row, col)` in my coordinate system corresponds to the character at `(2*row + 1, 2*col + 1)` in the ASCII grid.

2.  **Locating Start and Target:** Using that conversion, I located 'O' (start) at cell (0, 0) and 'T' (target) at cell (4, 4). The maze is 5x5 cells.

3.  **Wall Analysis:** I now know how to tell if there's a wall. To get from a cell `(r, c)` to its neighbor, the ASCII character between them has to be a space. So to go right from `(r, c)`, the character at `(2*r + 1, 2*c + 2)` must be a space. Left is `(2*r + 1, 2*c)`, down is `(2*r + 2, 2*c + 1)`, and up is `(2*r, 2*c + 1)`.

4.  **Choosing a Search Strategy:**  I'll use Breadth-First Search (BFS) for this. BFS guarantees I'll find the shortest path, which is important. I'll represent the maze as a grid and check for walls as I explore.

5.  **Manual Tracing:** I began with a manual trace to verify my understanding and start getting a feel for the maze structure. I started from 'O' at (0,0) and carefully followed possible paths, checking for walls at each step.  I got a bit tangled up in the walls at first! I was able to identify some dead ends, which is normal for this kind of problem.

6.  **BFS Implementation:**
    I'll implement BFS to search the maze, storing paths in a queue and tracking visited cells. Here's my plan:
    *   **Parsing:** Find dimensions (5x5), start, and target and store ASCII.
    *   **Initialize:** Queue starts with `[(0, 0)]` and visited set with `{(0, 0)}`.
    *   **Loop:**
        *   Dequeue a path.
        *   If the last cell is the target, I'm done.
        *   Explore each neighbor: make sure it's in bounds, not visited, and there's no wall.
        *   Add valid neighbor to visited, add new path to queue.

7.  **Mental BFS Execution:**
    I mentally ran through the BFS algorithm step by step. I traced the queue, the visited set, and considered all neighbor wall checks carefully. I was sure to track potential errors and backtrack when required. I mentally performed wall checks on each potential cell I visited. This process was rigorous to ensure all details were handled. After mentally running BFS, I ended up with a valid path. I re-checked my wall interpretations carefully to make sure there are no errors in my plan.

8.  **Building the Path:** After all this, I assembled the final path from the BFS result:
    `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]`

9.  **Verification:** I traced this final path, step-by-step, checking each move against the ASCII maze to make sure it was valid.

10. **Final Answer:** The final path is a list of cell coordinates. The number of coordinates is 11, the number of steps is 10. The path is:
    `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]`
""",
        thought=True
      ),
      Part(
        text="""An analysis of the maze reveals a 5x5 grid of cells. The starting point 'O' is at cell coordinate (0, 0), and the target 'T' is at (4, 4). By using a pathfinding algorithm like Breadth-First Search (BFS), we can find a shortest path from the start to the target.

The path involves navigating down the left side of the maze, and then moving across the bottom row to reach the target.

Here is a valid path from 'O' to 'T' as a list of (row, col) coordinates:
```
[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='gn0IaciYKciWvdIP-5yO4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=194,
  prompt_token_count=341,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=341
    ),
  ],
  thoughts_token_count=12738,
  total_token_count=13273
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=194 candidates_tokens_details=None prompt_token_count=341 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=341
)] thoughts_token_count=12738 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13273 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**My Solution for the ASCII Maze**

Alright, let's break this down systematically. My objective is to find a path from 'O' to 'T' in this ASCII maze.

1.  **Maze Interpretation:**  This is a grid, and the pluses, minuses, and bars are walls. Spaces are walkable paths. I've got to figure out where 'O' and 'T' are, but first, I need to translate these ASCII characters to a coordinate system that makes sense for my algorithm. I'm going to set up a mapping from the character grid coordinates to maze cell coordinates. I figured out that a cell at `(row, col)` in my coordinate system corresponds to the character at `(2*row + 1, 2*col + 1)` in the ASCII grid.

2.  **Locating Start and Target:** Using that conversion, I located 'O' (start) at cell (0, 0) and 'T' (target) at cell (4, 4). The maze is 5x5 cells.

3.  **Wall Analysis:** I now know how to tell if there's a wall. To get from a cell `(r, c)` to its neighbor, the ASCII character between them has to be a space. So to go right from `(r, c)`, the character at `(2*r + 1, 2*c + 2)` must be a space. Left is `(2*r + 1, 2*c)`, down is `(2*r + 2, 2*c + 1)`, and up is `(2*r, 2*c + 1)`.

4.  **Choosing a Search Strategy:**  I'll use Breadth-First Search (BFS) for this. BFS guarantees I'll find the shortest path, which is important. I'll represent the maze as a grid and check for walls as I explore.

5.  **Manual Tracing:** I began with a manual trace to verify my understanding and start getting a feel for the maze structure. I started from 'O' at (0,0) and carefully followed possible paths, checking for walls at each step.  I got a bit tangled up in the walls at first! I was able to identify some dead ends, which is normal for this kind of problem.

6.  **BFS Implementation:**
    I'll implement BFS to search the maze, storing paths in a queue and tracking visited cells. Here's my plan:
    *   **Parsing:** Find dimensions (5x5), start, and target and store ASCII.
    *   **Initialize:** Queue starts with `[(0, 0)]` and visited set with `{(0, 0)}`.
    *   **Loop:**
        *   Dequeue a path.
        *   If the last cell is the target, I'm done.
        *   Explore each neighbor: make sure it's in bounds, not visited, and there's no wall.
        *   Add valid neighbor to visited, add new path to queue.

7.  **Mental BFS Execution:**
    I mentally ran through the BFS algorithm step by step. I traced the queue, the visited set, and considered all neighbor wall checks carefully. I was sure to track potential errors and backtrack when required. I mentally performed wall checks on each potential cell I visited. This process was rigorous to ensure all details were handled. After mentally running BFS, I ended up with a valid path. I re-checked my wall interpretations carefully to make sure there are no errors in my plan.

8.  **Building the Path:** After all this, I assembled the final path from the BFS result:
    `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]`

9.  **Verification:** I traced this final path, step-by-step, checking each move against the ASCII maze to make sure it was valid.

10. **Final Answer:** The final path is a list of cell coordinates. The number of coordinates is 11, the number of steps is 10. The path is:
    `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]`
""",
        thought=True
      ),
      Part(
        text="""An analysis of the maze reveals a 5x5 grid of cells. The starting point 'O' is at cell coordinate (0, 0), and the target 'T' is at (4, 4). By using a pathfinding algorithm like Breadth-First Search (BFS), we can find a shortest path from the start to the target.

The path involves navigating down the left side of the maze, and then moving across the bottom row to reach the target.

Here is a valid path from 'O' to 'T' as a list of (row, col) coordinates:
```
[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]
```"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

