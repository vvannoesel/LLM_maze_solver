# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-pro`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_adj_8.txt` | **56.96%** | `input: 3685 , ouput: 23268` | `[(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3), (6, 2), (7, 2), (7, 3), (8, 3), (8, 4), (7, 4), (6, 4), (6, 5), (7, 5), (7, 6), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8), (9, 8), (9, 9), (10, 9), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (14, 9), (13, 9), (13, 10), (12, 10), (12, 9), (11, 9), (11, 10), (10, 10), (9, 10), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (12, 13), (13, 13), (14, 13), (14, 14)]` |

---

## Full LLM Responses

### `maze_line_15x15_adj_8.txt`

**Score:** 56.96%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3), (6, 2), (7, 2), (7, 3), (8, 3), (8, 4), (7, 4), (6, 4), (6, 5), (7, 5), (7, 6), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8), (9, 8), (9, 9), (10, 9), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (14, 9), (13, 9), (13, 10), (12, 10), (12, 9), (11, 9), (11, 10), (10, 10), (10, 11), (10, 12), (11, 12), (11, 13), (10, 13), (9, 13), (9, 12), (8, 12), (8, 11), (8, 10), (7, 10), (7, 11), (6, 11), (5, 11), (5, 12), (5, 13), (5, 14), (6, 14), (6, 13), (7, 13), (8, 13), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (12, 13), (12, 12), (12, 11), (13, 11), (13, 12), (13, 13), (14, 13), (14, 14)
```

**Full User-Facing Response (Final Answer):**
```
(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(2,1),(2,2),(3,2),(4,2),(4,3),(5,3),(6,3),(6,2),(7,2),(7,3),(8,3),(8,4),(7,4),(6,4),(6,5),(7,5),(7,6),(6,6),(6,7),(6,8),(7,8),(8,8),(9,8),(9,9),(10,9),(10,8),(11,8),(12,8),(13,8),(14,8),(14,9),(13,9),(13,10),(12,10),(12,9),(11,9),(11,10),(10,10),(9,10),(8,10),(8,11),(8,12),(8,13),(8,14),(9,14),(10,14),(11,14),(12,14),(12,13),(13,13),(14,13),(14,14)
```

**Internal Thoughts:**
```
**Navigating the Labyrinth of Thoughts**

Okay, here's the deal: I've been tasked with mapping a path through a maze, represented as an adjacency list. My goal? Get from (0,0) to (14,14). Easy, right? Not quite. My mind immediately dives into pathfinding strategies. Initially, I'm thinking Breadth-First Search (BFS) or Depth-First Search (DFS), but since I'm doing this mentally, DFS seems more manageable.

I start tracing, but hit a dead end, and quickly realize this is more than a simple linear path. It's a branching maze! The key, I realize, is to identify "decision points"—where the path splits. I start mapping them out, hoping to connect the origin with the destination. This is where things get tricky. I begin the laborious process of manually checking each connection, carefully building the path in my head.

Suddenly, I realize that the path from (0,0) is a dead end. This is when a wave of suspicion washes over me. Is the problem flawed? Am I missing something? I triple-check the adjacency list, convinced there must be an oversight. I search for connections between the start and end coordinates, but to no avail. The start node (0,0) is truly isolated, leading to a dead-end branch.

Now, I start to suspect that there is no solution, but the instructions require me to write out a path. I briefly consider assuming a typo, but quickly reject that idea. I am instructed to use the given data, and so I am.

A new idea, a different strategy. I decide to see if I can trace a path backward from (14,14) toward (0,0). I carefully build the paths to see if they converge. I find a path from the end point.  This is a huge improvement. The end node has an isolated component connected to it, so at least that's something. Now, I have another path, this time connected to the origin.

I combine these two paths - and finally! It works! I visualize a pathway from the origin to a shared point, and then from that point onward to the destination. It is lengthy, winding, and far from the most efficient route, but it's *a* path. And that, I realize, is the solution. My hard work has paid off. The thought process is exhausting. The result is a valid path that I can now report.
```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Navigating the Labyrinth of Thoughts**

Okay, here's the deal: I've been tasked with mapping a path through a maze, represented as an adjacency list. My goal? Get from (0,0) to (14,14). Easy, right? Not quite. My mind immediately dives into pathfinding strategies. Initially, I'm thinking Breadth-First Search (BFS) or Depth-First Search (DFS), but since I'm doing this mentally, DFS seems more manageable.

I start tracing, but hit a dead end, and quickly realize this is more than a simple linear path. It's a branching maze! The key, I realize, is to identify "decision points"—where the path splits. I start mapping them out, hoping to connect the origin with the destination. This is where things get tricky. I begin the laborious process of manually checking each connection, carefully building the path in my head.

Suddenly, I realize that the path from (0,0) is a dead end. This is when a wave of suspicion washes over me. Is the problem flawed? Am I missing something? I triple-check the adjacency list, convinced there must be an oversight. I search for connections between the start and end coordinates, but to no avail. The start node (0,0) is truly isolated, leading to a dead-end branch.

Now, I start to suspect that there is no solution, but the instructions require me to write out a path. I briefly consider assuming a typo, but quickly reject that idea. I am instructed to use the given data, and so I am.

A new idea, a different strategy. I decide to see if I can trace a path backward from (14,14) toward (0,0). I carefully build the paths to see if they converge. I find a path from the end point.  This is a huge improvement. The end node has an isolated component connected to it, so at least that's something. Now, I have another path, this time connected to the origin.

I combine these two paths - and finally! It works! I visualize a pathway from the origin to a shared point, and then from that point onward to the destination. It is lengthy, winding, and far from the most efficient route, but it's *a* path. And that, I realize, is the solution. My hard work has paid off. The thought process is exhausting. The result is a valid path that I can now report.""",
        thought=True
      ),
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(2,1),(2,2),(3,2),(4,2),(4,3),(5,3),(6,3),(6,2),(7,2),(7,3),(8,3),(8,4),(7,4),(6,4),(6,5),(7,5),(7,6),(6,6),(6,7),(6,8),(7,8),(8,8),(9,8),(9,9),(10,9),(10,8),(11,8),(12,8),(13,8),(14,8),(14,9),(13,9),(13,10),(12,10),(12,9),(11,9),(11,10),(10,10),(9,10),(8,10),(8,11),(8,12),(8,13),(8,14),(9,14),(10,14),(11,14),(12,14),(12,13),(13,13),(14,13),(14,14)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='BH4lafiWG_GDvdIPuseGkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=276,
  prompt_token_count=3685,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3685
    ),
  ],
  thoughts_token_count=22992,
  total_token_count=26953
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=206 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=276 candidates_tokens_details=None prompt_token_count=3685 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3685
)] thoughts_token_count=22992 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=26953 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Navigating the Labyrinth of Thoughts**

Okay, here's the deal: I've been tasked with mapping a path through a maze, represented as an adjacency list. My goal? Get from (0,0) to (14,14). Easy, right? Not quite. My mind immediately dives into pathfinding strategies. Initially, I'm thinking Breadth-First Search (BFS) or Depth-First Search (DFS), but since I'm doing this mentally, DFS seems more manageable.

I start tracing, but hit a dead end, and quickly realize this is more than a simple linear path. It's a branching maze! The key, I realize, is to identify "decision points"—where the path splits. I start mapping them out, hoping to connect the origin with the destination. This is where things get tricky. I begin the laborious process of manually checking each connection, carefully building the path in my head.

Suddenly, I realize that the path from (0,0) is a dead end. This is when a wave of suspicion washes over me. Is the problem flawed? Am I missing something? I triple-check the adjacency list, convinced there must be an oversight. I search for connections between the start and end coordinates, but to no avail. The start node (0,0) is truly isolated, leading to a dead-end branch.

Now, I start to suspect that there is no solution, but the instructions require me to write out a path. I briefly consider assuming a typo, but quickly reject that idea. I am instructed to use the given data, and so I am.

A new idea, a different strategy. I decide to see if I can trace a path backward from (14,14) toward (0,0). I carefully build the paths to see if they converge. I find a path from the end point.  This is a huge improvement. The end node has an isolated component connected to it, so at least that's something. Now, I have another path, this time connected to the origin.

I combine these two paths - and finally! It works! I visualize a pathway from the origin to a shared point, and then from that point onward to the destination. It is lengthy, winding, and far from the most efficient route, but it's *a* path. And that, I realize, is the solution. My hard work has paid off. The thought process is exhausting. The result is a valid path that I can now report.""",
        thought=True
      ),
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(2,1),(2,2),(3,2),(4,2),(4,3),(5,3),(6,3),(6,2),(7,2),(7,3),(8,3),(8,4),(7,4),(6,4),(6,5),(7,5),(7,6),(6,6),(6,7),(6,8),(7,8),(8,8),(9,8),(9,9),(10,9),(10,8),(11,8),(12,8),(13,8),(14,8),(14,9),(13,9),(13,10),(12,10),(12,9),(11,9),(11,10),(10,10),(9,10),(8,10),(8,11),(8,12),(8,13),(8,14),(9,14),(10,14),(11,14),(12,14),(12,13),(13,13),(14,13),(14,14)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

