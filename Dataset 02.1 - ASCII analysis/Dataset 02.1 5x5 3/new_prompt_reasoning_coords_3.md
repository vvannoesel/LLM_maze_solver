# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools. The maze is represented as a 5x5 grid. The top-left corner is (0,0). Instructions: 1. You cannot move diagonally or through walls ('-' and '|'), only from one cell to an adjacent cell. 2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1). 3. Provide only the final list of coordinates from start to end in your response.`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_3.txt` | **23.08%** | `input: 218 , ouput: 16369` | `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_3.txt`

**Score:** 23.08%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(4,4)
```

**Internal Thoughts:**
```
**Initial Setup and Understanding**

I'm tasked with solving a maze presented as ASCII art and providing the path as a coordinate sequence. I first need to decipher the maze's structure. It's a 5x5 grid with characters representing corners, walls, open paths, start (O), and end (T) points. I map the maze's visual representation to a coordinate system where each cell has a specific position (row, column). I identify (0,0) as the start and (4,4) as the target.

**Initial Maze Analysis and Interpretation Struggles**

I begin by examining the maze's walls, tracing a path from the start point.  I realize the maze representation is more complex than initially thought.  I struggle with how the spaces and characters within the ASCII art represent the maze's cells and walls, leading to several incorrect interpretations of the grid and open paths. I analyze horizontal and vertical movement, initially misinterpreting walls and openings.

**Corrected Maze Graph and Pathfinding**

After several missteps, I realize that the `+` characters are just vertices, while the `-` and `|` characters form the walls. Open spaces indicate open paths between cells. Each cell has four potential walls based on its position within the ASCII representation. After numerous visual inspections, I map the correct cell neighbors and openings.

**Pathfinding and Solution**

Using this corrected graph, I attempt a visual trace, following the path from the start to the target. I determine the shortest path using a Breadth-First Search (BFS) technique. After tracing and backtracking to find the optimal route, I determine the complete coordinate sequence (0,0), (0,1), (1,1), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4), verifying all the steps are open and correct. I'm now certain this is the correct solution.

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Initial Setup and Understanding**

I'm tasked with solving a maze presented as ASCII art and providing the path as a coordinate sequence. I first need to decipher the maze's structure. It's a 5x5 grid with characters representing corners, walls, open paths, start (O), and end (T) points. I map the maze's visual representation to a coordinate system where each cell has a specific position (row, column). I identify (0,0) as the start and (4,4) as the target.

**Initial Maze Analysis and Interpretation Struggles**

I begin by examining the maze's walls, tracing a path from the start point.  I realize the maze representation is more complex than initially thought.  I struggle with how the spaces and characters within the ASCII art represent the maze's cells and walls, leading to several incorrect interpretations of the grid and open paths. I analyze horizontal and vertical movement, initially misinterpreting walls and openings.

**Corrected Maze Graph and Pathfinding**

After several missteps, I realize that the `+` characters are just vertices, while the `-` and `|` characters form the walls. Open spaces indicate open paths between cells. Each cell has four potential walls based on its position within the ASCII representation. After numerous visual inspections, I map the correct cell neighbors and openings.

**Pathfinding and Solution**

Using this corrected graph, I attempt a visual trace, following the path from the start to the target. I determine the shortest path using a Breadth-First Search (BFS) technique. After tracing and backtracking to find the optimal route, I determine the complete coordinate sequence (0,0), (0,1), (1,1), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4), verifying all the steps are open and correct. I'm now certain this is the correct solution.
""",
        thought=True
      ),
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='iAQCad6eI_TY7M8P5p3qgQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=218,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=218
    ),
  ],
  thoughts_token_count=16324,
  total_token_count=16587
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=144 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=218 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=218
)] thoughts_token_count=16324 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=16587 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Initial Setup and Understanding**

I'm tasked with solving a maze presented as ASCII art and providing the path as a coordinate sequence. I first need to decipher the maze's structure. It's a 5x5 grid with characters representing corners, walls, open paths, start (O), and end (T) points. I map the maze's visual representation to a coordinate system where each cell has a specific position (row, column). I identify (0,0) as the start and (4,4) as the target.

**Initial Maze Analysis and Interpretation Struggles**

I begin by examining the maze's walls, tracing a path from the start point.  I realize the maze representation is more complex than initially thought.  I struggle with how the spaces and characters within the ASCII art represent the maze's cells and walls, leading to several incorrect interpretations of the grid and open paths. I analyze horizontal and vertical movement, initially misinterpreting walls and openings.

**Corrected Maze Graph and Pathfinding**

After several missteps, I realize that the `+` characters are just vertices, while the `-` and `|` characters form the walls. Open spaces indicate open paths between cells. Each cell has four potential walls based on its position within the ASCII representation. After numerous visual inspections, I map the correct cell neighbors and openings.

**Pathfinding and Solution**

Using this corrected graph, I attempt a visual trace, following the path from the start to the target. I determine the shortest path using a Breadth-First Search (BFS) technique. After tracing and backtracking to find the optimal route, I determine the complete coordinate sequence (0,0), (0,1), (1,1), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4), verifying all the steps are open and correct. I'm now certain this is the correct solution.
""",
        thought=True
      ),
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

