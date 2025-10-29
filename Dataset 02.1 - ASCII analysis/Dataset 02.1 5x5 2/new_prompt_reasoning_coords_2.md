# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools. The maze is represented as a 5x5 grid. The top-left corner is (0,0). Instructions: 1. You cannot move diagonally or through walls ('-' and '|'), only from one cell to an adjacent cell. 2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1). 3. Provide only the final list of coordinates from start to end in your response.`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_2.txt` | **18.18%** | `input: 220 , ouput: 8583` | `[(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_2.txt`

**Score:** 18.18%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
(0,0),(1,0),(1,1),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4),(3,4),(4,4)
```

**Internal Thoughts:**
```
**Alright, here's the breakdown of my thought process for solving this maze.**

First, I identified the key elements: the 5x5 grid representation, the start ('O'), the target ('T'), walls ('-', '|', '+'), and open paths (' '). I'm going to start with a standard DFS or BFS. I'll need to use a graph search approach.

Then, I carefully examined the grid's structure to create a mental model of the maze's connectivity. I'll trace paths and keep track of visited nodes to avoid getting stuck in loops.

I did a first quick trace. I manually stepped through the maze, but got a bit lost and decided it wasn't scalable or the best route to find the *shortest* path.

So, I decided to analyze the maze systematically, listing all valid moves from each cell, using it to create a connectivity graph. I realized the importance of accurate connections!

I started a breadth-first search (BFS) implementation in my head, since that is usually most efficient. I carefully used a queue and a visited set and a "parent map" to reconstruct the shortest path. I implemented this step by step. I made sure to meticulously update the data structures.

Finally, after backtracking, I found a path, then checked the path on the maze representation. The first path I found wasn't the most efficient, I found a quicker, shorter path from a DFS trace. So, I checked the path again. It matched all the constraints!

I confirmed that my final path was the shortest path that correctly navigated the maze from the starting point to the target point, avoiding all walls. I ensured the output format was correct. That's a wrap!

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Alright, here's the breakdown of my thought process for solving this maze.**

First, I identified the key elements: the 5x5 grid representation, the start ('O'), the target ('T'), walls ('-', '|', '+'), and open paths (' '). I'm going to start with a standard DFS or BFS. I'll need to use a graph search approach.

Then, I carefully examined the grid's structure to create a mental model of the maze's connectivity. I'll trace paths and keep track of visited nodes to avoid getting stuck in loops.

I did a first quick trace. I manually stepped through the maze, but got a bit lost and decided it wasn't scalable or the best route to find the *shortest* path.

So, I decided to analyze the maze systematically, listing all valid moves from each cell, using it to create a connectivity graph. I realized the importance of accurate connections!

I started a breadth-first search (BFS) implementation in my head, since that is usually most efficient. I carefully used a queue and a visited set and a "parent map" to reconstruct the shortest path. I implemented this step by step. I made sure to meticulously update the data structures.

Finally, after backtracking, I found a path, then checked the path on the maze representation. The first path I found wasn't the most efficient, I found a quicker, shorter path from a DFS trace. So, I checked the path again. It matched all the constraints!

I confirmed that my final path was the shortest path that correctly navigated the maze from the starting point to the target point, avoiding all walls. I ensured the output format was correct. That's a wrap!
""",
        thought=True
      ),
      Part(
        text='(0,0),(1,0),(1,1),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4),(3,4),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='BwQCaZ-JDvHhnsEPp_CPwAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=220,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=220
    ),
  ],
  thoughts_token_count=8538,
  total_token_count=8803
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=220 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=220
)] thoughts_token_count=8538 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8803 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Alright, here's the breakdown of my thought process for solving this maze.**

First, I identified the key elements: the 5x5 grid representation, the start ('O'), the target ('T'), walls ('-', '|', '+'), and open paths (' '). I'm going to start with a standard DFS or BFS. I'll need to use a graph search approach.

Then, I carefully examined the grid's structure to create a mental model of the maze's connectivity. I'll trace paths and keep track of visited nodes to avoid getting stuck in loops.

I did a first quick trace. I manually stepped through the maze, but got a bit lost and decided it wasn't scalable or the best route to find the *shortest* path.

So, I decided to analyze the maze systematically, listing all valid moves from each cell, using it to create a connectivity graph. I realized the importance of accurate connections!

I started a breadth-first search (BFS) implementation in my head, since that is usually most efficient. I carefully used a queue and a visited set and a "parent map" to reconstruct the shortest path. I implemented this step by step. I made sure to meticulously update the data structures.

Finally, after backtracking, I found a path, then checked the path on the maze representation. The first path I found wasn't the most efficient, I found a quicker, shorter path from a DFS trace. So, I checked the path again. It matched all the constraints!

I confirmed that my final path was the shortest path that correctly navigated the maze from the starting point to the target point, avoiding all walls. I ensured the output format was correct. That's a wrap!
""",
        thought=True
      ),
      Part(
        text='(0,0),(1,0),(1,1),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4),(3,4),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

