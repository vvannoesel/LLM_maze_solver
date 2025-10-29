# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools. The maze is represented as a 5x5 grid. The top-left corner is (0,0). Instructions: 1. You cannot move diagonally or through walls ('-' and '|'), only from one cell to an adjacent cell. 2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1). 3. Provide only the final list of coordinates from start to end in your response.`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_1.txt` | **18.18%** | `input: 217 , ouput: 25886` | `[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (4, 3), (3, 3), (3, 4), (4, 4), (2, 2), (3, 2), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (3, 3), (3, 4), (4, 4), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (3, 3), (3, 4), (2, 4), (1, 4), (2, 4), (3, 4), (4, 4), (3, 4), (2, 4), (1, 4), (4, 4), (3, 4), (3, 3), (4, 3), (4, 2), (3, 2), (3, 1), (3, 2), (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (3, 3), (3, 4), (4, 4)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_1.txt`

**Score:** 18.18%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,1),(1,1),(1,2),(1,3),(2,3),(2,2),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,3),(4,3),(3,3),(3,4),(4,4)
I am sorry, the maze provided seems to be unsolvable as there is no path from the section containing the start 'O' to the section containing the end 'T'. After a thorough analysis, all paths from the start lead to dead ends.

However, if we assume a single wall is missing, a solution can be found. Assuming the wall between (2,2) and (3,2) is passable, the path would be:
(0,0),(1,0),(2,0),(2,1),(2,2),(3,2),(4,2),(4,3),(3,3),(3,4),(4,4)

Let's re-examine the maze, as a solution should exist.

I have made a critical error in my previous analyses. The connection between rows is key.

Let's trace the correct path:
(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(3,3),(3,4),(2,4),(1,4) ... This seems to be a dead end.

Let me re-re-examine the horizontal lines.
Line 6: `+ +-+-+-+ +` -> This separates row 2 from row 3.
The last segment is `+ +`, meaning there is a path between (2,4) and (3,4).
The end part of the maze is: (4,4) -> (3,4) -> (2,4) -> (1,4). This is a dead-end branch.
The end part also has: (4,4) -> (3,4) -> (3,3) -> (4,3) -> (4,2) -> (3,2). This is another dead-end branch.
The maze is unsolvable as written.

I will provide the most plausible path, which assumes a typo in the maze's construction. The path below assumes the vertical wall between (3,1) and (3,2) is missing.

(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,3),(3,3),(3,4),(4,4)
```

**Internal Thoughts:**
```
**Initial Thoughts & Maze Analysis**

Okay, here we go. The user wants me to navigate a maze represented as a 5x5 grid, find a path from 'O' to 'T', and provide the coordinate list. Let's dig in. I'm going to visually trace the maze and map out all the possible moves from each cell, considering walls. I need to get this right - no dead ends! I know to use the spaces as walkable areas and the `|` and `-` as walls. I'll make a grid, starting with 'O' at (0,0) and 'T' at (4,4), and trace the path logically. This ASCII art maze has a simple structure, I just need to be careful and systematic.

**Mapping Connections & Wall Analysis**

Right, let's look for valid moves. First pass seems to indicate a simple initial move, either downwards (from the `O`) or right. Now I'll need to double check any move which seems to leave one direction (left or up) inaccessible. I’m thinking forward planning is key here. I will look at each cell's connections, documenting them carefully. I'll track where each move can go, carefully noting the positions of the walls. It is a bit tedious but crucial. The walls create a pattern and I'll need to figure that out.

**Path Tracing and Iteration**

Okay, the path seems obvious at first, but this is clearly a tricky maze. I've attempted a path, and I've hit a dead end, indicating a trap. I have to re-evaluate where I've gone wrong. I'm going to need to backtrack and explore other paths. I'm getting back to the basics and going step by step. I am looking for a direct path. Now I am going to re-check all my previous analysis and attempt to rule out any possibilities that contain loops. I’ll keep a systematic path-tracing and exploration.

**Loop Detection & Path Refinement**

Here we go again. This is more complex than it seemed. It looks like I am forming a loop and cannot get out. This is a common pattern in mazes. Time to explore all the directions from this current cell. I'm re-analyzing the maze structure, and it seems there's a pattern, some sort of a trap, and a set of dead-ends. I am carefully documenting each branch. I'm going to need to approach it from a different angle, like a graph with nodes and paths.

**Reframing the Problem & Identifying Components**

This is getting complex, I need to take a wider view. Let's see if I can identify disconnected components - parts of the maze that are isolated from each other. I am going to see if any nodes can be identified as entry/exit points to distinct sections of the maze. There must be one single path from O to T. Ah - I just found my error - I completely missed a link. It turns out that I've been over-analyzing a pattern and that simple path I first suspected would never work. I've reanalyzed the wall constraints. I'll need to re-trace the entire path.

**Graph Rebuilding and Maze Redefinition**

Okay, the analysis is now much cleaner - all horizontal walls, vertical walls. This will make it far easier to construct the graph. Okay, I rebuilt the maze into a clear path with nodes, and I have found two separate parts. This seems to be the crucial piece of information. There are two disconnected components, one with the starting point, and one with the end point. There must be a typo, or I'm missing something important.

**Re-Examination and Typo Assumption**

Hold on. I'm now realizing that this cannot be solvable with the provided rules. The left path is disconnected from the right path. This is a contradiction. The prompt implies there is a path. Hmm. I can only assume there's a single typo. Let's see what looks most likely... a horizontal wall that isn't really there?

**Hypothetical Fix and Path Construction**

I am going to assume a wall is missing and construct a path. I will provide the path that would work *if* there were a small typo at that cell. This is the best I can do. I found a plausible typo. If that wall isn't there, there's a path. This feels like the right answer given that I'm supposed to find a path, and I've found an unsolvable maze.

**Final Path and Considerations**

I have a valid path, after assuming the typo. The problem with these computer simulations is that, with an error in the construction, the answer is hard to find! This problem is now clear, so I'll generate the final list of coordinates
```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Initial Thoughts & Maze Analysis**

Okay, here we go. The user wants me to navigate a maze represented as a 5x5 grid, find a path from 'O' to 'T', and provide the coordinate list. Let's dig in. I'm going to visually trace the maze and map out all the possible moves from each cell, considering walls. I need to get this right - no dead ends! I know to use the spaces as walkable areas and the `|` and `-` as walls. I'll make a grid, starting with 'O' at (0,0) and 'T' at (4,4), and trace the path logically. This ASCII art maze has a simple structure, I just need to be careful and systematic.

**Mapping Connections & Wall Analysis**

Right, let's look for valid moves. First pass seems to indicate a simple initial move, either downwards (from the `O`) or right. Now I'll need to double check any move which seems to leave one direction (left or up) inaccessible. I’m thinking forward planning is key here. I will look at each cell's connections, documenting them carefully. I'll track where each move can go, carefully noting the positions of the walls. It is a bit tedious but crucial. The walls create a pattern and I'll need to figure that out.

**Path Tracing and Iteration**

Okay, the path seems obvious at first, but this is clearly a tricky maze. I've attempted a path, and I've hit a dead end, indicating a trap. I have to re-evaluate where I've gone wrong. I'm going to need to backtrack and explore other paths. I'm getting back to the basics and going step by step. I am looking for a direct path. Now I am going to re-check all my previous analysis and attempt to rule out any possibilities that contain loops. I’ll keep a systematic path-tracing and exploration.

**Loop Detection & Path Refinement**

Here we go again. This is more complex than it seemed. It looks like I am forming a loop and cannot get out. This is a common pattern in mazes. Time to explore all the directions from this current cell. I'm re-analyzing the maze structure, and it seems there's a pattern, some sort of a trap, and a set of dead-ends. I am carefully documenting each branch. I'm going to need to approach it from a different angle, like a graph with nodes and paths.

**Reframing the Problem & Identifying Components**

This is getting complex, I need to take a wider view. Let's see if I can identify disconnected components - parts of the maze that are isolated from each other. I am going to see if any nodes can be identified as entry/exit points to distinct sections of the maze. There must be one single path from O to T. Ah - I just found my error - I completely missed a link. It turns out that I've been over-analyzing a pattern and that simple path I first suspected would never work. I've reanalyzed the wall constraints. I'll need to re-trace the entire path.

**Graph Rebuilding and Maze Redefinition**

Okay, the analysis is now much cleaner - all horizontal walls, vertical walls. This will make it far easier to construct the graph. Okay, I rebuilt the maze into a clear path with nodes, and I have found two separate parts. This seems to be the crucial piece of information. There are two disconnected components, one with the starting point, and one with the end point. There must be a typo, or I'm missing something important.

**Re-Examination and Typo Assumption**

Hold on. I'm now realizing that this cannot be solvable with the provided rules. The left path is disconnected from the right path. This is a contradiction. The prompt implies there is a path. Hmm. I can only assume there's a single typo. Let's see what looks most likely... a horizontal wall that isn't really there?

**Hypothetical Fix and Path Construction**

I am going to assume a wall is missing and construct a path. I will provide the path that would work *if* there were a small typo at that cell. This is the best I can do. I found a plausible typo. If that wall isn't there, there's a path. This feels like the right answer given that I'm supposed to find a path, and I've found an unsolvable maze.

**Final Path and Considerations**

I have a valid path, after assuming the typo. The problem with these computer simulations is that, with an error in the construction, the answer is hard to find! This problem is now clear, so I'll generate the final list of coordinates""",
        thought=True
      ),
      Part(
        text="""(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,1),(1,1),(1,2),(1,3),(2,3),(2,2),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,3),(4,3),(3,3),(3,4),(4,4)
I am sorry, the maze provided seems to be unsolvable as there is no path from the section containing the start 'O' to the section containing the end 'T'. After a thorough analysis, all paths from the start lead to dead ends.

However, if we assume a single wall is missing, a solution can be found. Assuming the wall between (2,2) and (3,2) is passable, the path would be:
(0,0),(1,0),(2,0),(2,1),(2,2),(3,2),(4,2),(4,3),(3,3),(3,4),(4,4)

Let's re-examine the maze, as a solution should exist.

I have made a critical error in my previous analyses. The connection between rows is key.

Let's trace the correct path:
(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(3,3),(3,4),(2,4),(1,4) ... This seems to be a dead end.

Let me re-re-examine the horizontal lines.
Line 6: `+ +-+-+-+ +` -> This separates row 2 from row 3.
The last segment is `+ +`, meaning there is a path between (2,4) and (3,4).
The end part of the maze is: (4,4) -> (3,4) -> (2,4) -> (1,4). This is a dead-end branch.
The end part also has: (4,4) -> (3,4) -> (3,3) -> (4,3) -> (4,2) -> (3,2). This is another dead-end branch.
The maze is unsolvable as written.

I will provide the most plausible path, which assumes a typo in the maze's construction. The path below assumes the vertical wall between (3,1) and (3,2) is missing.

(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,3),(3,3),(3,4),(4,4)"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='xwMCaYDXD_TY7M8P5p3qgQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=591,
  prompt_token_count=217,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=217
    ),
  ],
  thoughts_token_count=25295,
  total_token_count=26103
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=591 candidates_tokens_details=None prompt_token_count=217 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=217
)] thoughts_token_count=25295 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=26103 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Initial Thoughts & Maze Analysis**

Okay, here we go. The user wants me to navigate a maze represented as a 5x5 grid, find a path from 'O' to 'T', and provide the coordinate list. Let's dig in. I'm going to visually trace the maze and map out all the possible moves from each cell, considering walls. I need to get this right - no dead ends! I know to use the spaces as walkable areas and the `|` and `-` as walls. I'll make a grid, starting with 'O' at (0,0) and 'T' at (4,4), and trace the path logically. This ASCII art maze has a simple structure, I just need to be careful and systematic.

**Mapping Connections & Wall Analysis**

Right, let's look for valid moves. First pass seems to indicate a simple initial move, either downwards (from the `O`) or right. Now I'll need to double check any move which seems to leave one direction (left or up) inaccessible. I’m thinking forward planning is key here. I will look at each cell's connections, documenting them carefully. I'll track where each move can go, carefully noting the positions of the walls. It is a bit tedious but crucial. The walls create a pattern and I'll need to figure that out.

**Path Tracing and Iteration**

Okay, the path seems obvious at first, but this is clearly a tricky maze. I've attempted a path, and I've hit a dead end, indicating a trap. I have to re-evaluate where I've gone wrong. I'm going to need to backtrack and explore other paths. I'm getting back to the basics and going step by step. I am looking for a direct path. Now I am going to re-check all my previous analysis and attempt to rule out any possibilities that contain loops. I’ll keep a systematic path-tracing and exploration.

**Loop Detection & Path Refinement**

Here we go again. This is more complex than it seemed. It looks like I am forming a loop and cannot get out. This is a common pattern in mazes. Time to explore all the directions from this current cell. I'm re-analyzing the maze structure, and it seems there's a pattern, some sort of a trap, and a set of dead-ends. I am carefully documenting each branch. I'm going to need to approach it from a different angle, like a graph with nodes and paths.

**Reframing the Problem & Identifying Components**

This is getting complex, I need to take a wider view. Let's see if I can identify disconnected components - parts of the maze that are isolated from each other. I am going to see if any nodes can be identified as entry/exit points to distinct sections of the maze. There must be one single path from O to T. Ah - I just found my error - I completely missed a link. It turns out that I've been over-analyzing a pattern and that simple path I first suspected would never work. I've reanalyzed the wall constraints. I'll need to re-trace the entire path.

**Graph Rebuilding and Maze Redefinition**

Okay, the analysis is now much cleaner - all horizontal walls, vertical walls. This will make it far easier to construct the graph. Okay, I rebuilt the maze into a clear path with nodes, and I have found two separate parts. This seems to be the crucial piece of information. There are two disconnected components, one with the starting point, and one with the end point. There must be a typo, or I'm missing something important.

**Re-Examination and Typo Assumption**

Hold on. I'm now realizing that this cannot be solvable with the provided rules. The left path is disconnected from the right path. This is a contradiction. The prompt implies there is a path. Hmm. I can only assume there's a single typo. Let's see what looks most likely... a horizontal wall that isn't really there?

**Hypothetical Fix and Path Construction**

I am going to assume a wall is missing and construct a path. I will provide the path that would work *if* there were a small typo at that cell. This is the best I can do. I found a plausible typo. If that wall isn't there, there's a path. This feels like the right answer given that I'm supposed to find a path, and I've found an unsolvable maze.

**Final Path and Considerations**

I have a valid path, after assuming the typo. The problem with these computer simulations is that, with an error in the construction, the answer is hard to find! This problem is now clear, so I'll generate the final list of coordinates""",
        thought=True
      ),
      Part(
        text="""(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,1),(1,1),(1,2),(1,3),(2,3),(2,2),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,3),(4,3),(3,3),(3,4),(4,4)
I am sorry, the maze provided seems to be unsolvable as there is no path from the section containing the start 'O' to the section containing the end 'T'. After a thorough analysis, all paths from the start lead to dead ends.

However, if we assume a single wall is missing, a solution can be found. Assuming the wall between (2,2) and (3,2) is passable, the path would be:
(0,0),(1,0),(2,0),(2,1),(2,2),(3,2),(4,2),(4,3),(3,3),(3,4),(4,4)

Let's re-examine the maze, as a solution should exist.

I have made a critical error in my previous analyses. The connection between rows is key.

Let's trace the correct path:
(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(3,3),(3,4),(2,4),(1,4) ... This seems to be a dead end.

Let me re-re-examine the horizontal lines.
Line 6: `+ +-+-+-+ +` -> This separates row 2 from row 3.
The last segment is `+ +`, meaning there is a path between (2,4) and (3,4).
The end part of the maze is: (4,4) -> (3,4) -> (2,4) -> (1,4). This is a dead-end branch.
The end part also has: (4,4) -> (3,4) -> (3,3) -> (4,3) -> (4,2) -> (3,2). This is another dead-end branch.
The maze is unsolvable as written.

I will provide the most plausible path, which assumes a typo in the maze's construction. The path below assumes the vertical wall between (3,1) and (3,2) is missing.

(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,3),(3,3),(3,4),(4,4)"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

