# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-pro`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_46.jpg` | **0.81%** | `input: 553 , ouput: 9137` | `left, forward, right, left, right, left, right, left, left, forward, right, forward, forward, right, left, right, left, forward, right, left, right, left, right, forward, forward, forward, forward, forward, forward, forward, forward, right` |
| `maze_line_15x15_46.json` | **2.42%** | `input: 9924 , ouput: 18313` | `left, right, left, forward, forward, forward, right, left, left, forward, right, forward, forward, forward, forward, forward, forward, right, forward, right, left, forward, forward, left, right, forward, left, right, right, left, right, left, left, right, left, right, forward, forward` |

---

## Full LLM Responses

### `maze_line_15x15_46.jpg`

**Score:** 0.81%

**Ground Truth Solution:**
```
left, right, left, right, forward, right, left, left, right, left, right, forward, left, left, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, left, right, right, forward, left, left, right, right, left, forward, right, forward, left, left, forward, forward, right, forward, right, right, left, left, right, right, left, right, left, right, right, left, forward, left, left, right, left, forward, forward, left, right, forward, left, right, right, left, left, forward, forward, forward, left, forward, right, right, forward, left, forward, left, left, right, forward, forward, forward, right, left, left, forward, right, right, left, right, right, left, right, forward, left, left, right, left, right, forward, left, right, right, forward, right, left, right, left, forward, left, forward, right, right, left, right, forward, left, left, forward, forward
```

**Full User-Facing Response (Final Answer):**
```
left, forward, right, left, right, left, right, left, left, forward, right, forward, forward, right, left, right, left, forward, right, left, right, left, right, forward, forward, forward, forward, forward, forward, forward, forward, right
```

**Internal Thoughts:**
```
**My Thought Process:**

Okay, the user wants me to solve a 15x15 maze visually, without any code or external tools. Fine, I can handle this. The challenge is to find the right sequence of movements (Forward, Left, Right, Backward) to get from a start (0, 1) to an end (14, 13) on a 15x15 grid, starting South.

First, I need to understand the goal: find the path from the start to the end. The constraints: no code, visual tracing, output a comma-separated instruction sequence, and the given starting position and orientation.

I'll start by systematically tracing a path from the start to the end, keeping track of my current location as I go. Since I'm starting at (0, 1) facing South, my first move is *Forward*. I'll continue tracing, step-by-step, determining the needed Left and Right turns as I encounter obstacles. I'll represent the path visually in my mind, noting the coordinate changes with each step and my orientation. It is important to remember that 'left' means I turn 90 degrees left and move one step; and 'right' means I turn 90 degrees right and move one step.

After the initial path tracing, I noticed that I was heading south and encountered a dead end, so I went through several turns and came to a much more difficult path. This is inefficient, and I should seek a simpler path. So I backtracked and explored the maze from the starting location again, and then tried out an alternate path. I can clearly see a much shorter and easier path than the initial one. I will trace this path and generate the commands.

I'll then convert my mental path into a sequence of instructions. At each step, I will calculate my direction and decide what movement is required to reach the next position. I'll need to remember the initial starting orientation as well. I'll double-check this instruction set by re-tracing with the generated commands to ensure it matches the traced path.

After generating the instruction set, and re-checking for efficiency. I need to make sure the sequence is correct.

Having verified the instructions and the path, the last step is to output the final sequence as a single comma-separated string, as the prompt specifies.

Here is the final set of instructions:

`left, forward, right, left, right, left, right, left, left, forward, right, forward, forward, right, left, right, left, forward, right, left, right, left, right, forward, forward, forward, forward, forward, forward, forward, forward, right`

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**My Thought Process:**

Okay, the user wants me to solve a 15x15 maze visually, without any code or external tools. Fine, I can handle this. The challenge is to find the right sequence of movements (Forward, Left, Right, Backward) to get from a start (0, 1) to an end (14, 13) on a 15x15 grid, starting South.

First, I need to understand the goal: find the path from the start to the end. The constraints: no code, visual tracing, output a comma-separated instruction sequence, and the given starting position and orientation.

I'll start by systematically tracing a path from the start to the end, keeping track of my current location as I go. Since I'm starting at (0, 1) facing South, my first move is *Forward*. I'll continue tracing, step-by-step, determining the needed Left and Right turns as I encounter obstacles. I'll represent the path visually in my mind, noting the coordinate changes with each step and my orientation. It is important to remember that 'left' means I turn 90 degrees left and move one step; and 'right' means I turn 90 degrees right and move one step.

After the initial path tracing, I noticed that I was heading south and encountered a dead end, so I went through several turns and came to a much more difficult path. This is inefficient, and I should seek a simpler path. So I backtracked and explored the maze from the starting location again, and then tried out an alternate path. I can clearly see a much shorter and easier path than the initial one. I will trace this path and generate the commands.

I'll then convert my mental path into a sequence of instructions. At each step, I will calculate my direction and decide what movement is required to reach the next position. I'll need to remember the initial starting orientation as well. I'll double-check this instruction set by re-tracing with the generated commands to ensure it matches the traced path.

After generating the instruction set, and re-checking for efficiency. I need to make sure the sequence is correct.

Having verified the instructions and the path, the last step is to output the final sequence as a single comma-separated string, as the prompt specifies.

Here is the final set of instructions:

`left, forward, right, left, right, left, right, left, left, forward, right, forward, forward, right, left, right, left, forward, right, left, right, left, right, forward, forward, forward, forward, forward, forward, forward, forward, right`
""",
        thought=True
      ),
      Part(
        text='left, forward, right, left, right, left, right, left, left, forward, right, forward, forward, right, left, right, left, forward, right, left, right, left, right, forward, forward, forward, forward, forward, forward, forward, forward, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='JOmSaeewGKbTvdIPuJ6ayQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=63,
  prompt_token_count=553,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=295
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  thoughts_token_count=9074,
  total_token_count=9690
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=553 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=63 candidates_tokens_details=None prompt_token_count=553 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=295
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=9074 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9690 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**My Thought Process:**

Okay, the user wants me to solve a 15x15 maze visually, without any code or external tools. Fine, I can handle this. The challenge is to find the right sequence of movements (Forward, Left, Right, Backward) to get from a start (0, 1) to an end (14, 13) on a 15x15 grid, starting South.

First, I need to understand the goal: find the path from the start to the end. The constraints: no code, visual tracing, output a comma-separated instruction sequence, and the given starting position and orientation.

I'll start by systematically tracing a path from the start to the end, keeping track of my current location as I go. Since I'm starting at (0, 1) facing South, my first move is *Forward*. I'll continue tracing, step-by-step, determining the needed Left and Right turns as I encounter obstacles. I'll represent the path visually in my mind, noting the coordinate changes with each step and my orientation. It is important to remember that 'left' means I turn 90 degrees left and move one step; and 'right' means I turn 90 degrees right and move one step.

After the initial path tracing, I noticed that I was heading south and encountered a dead end, so I went through several turns and came to a much more difficult path. This is inefficient, and I should seek a simpler path. So I backtracked and explored the maze from the starting location again, and then tried out an alternate path. I can clearly see a much shorter and easier path than the initial one. I will trace this path and generate the commands.

I'll then convert my mental path into a sequence of instructions. At each step, I will calculate my direction and decide what movement is required to reach the next position. I'll need to remember the initial starting orientation as well. I'll double-check this instruction set by re-tracing with the generated commands to ensure it matches the traced path.

After generating the instruction set, and re-checking for efficiency. I need to make sure the sequence is correct.

Having verified the instructions and the path, the last step is to output the final sequence as a single comma-separated string, as the prompt specifies.

Here is the final set of instructions:

`left, forward, right, left, right, left, right, left, left, forward, right, forward, forward, right, left, right, left, forward, right, left, right, left, right, forward, forward, forward, forward, forward, forward, forward, forward, right`
""",
        thought=True
      ),
      Part(
        text='left, forward, right, left, right, left, right, left, left, forward, right, forward, forward, right, left, right, left, forward, right, left, right, left, right, forward, forward, forward, forward, forward, forward, forward, forward, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

### `maze_line_15x15_46.json`

**Score:** 2.42%

**Ground Truth Solution:**
```
left, right, left, right, forward, right, left, left, right, left, right, forward, left, left, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, left, right, right, forward, left, left, right, right, left, forward, right, forward, left, left, forward, forward, right, forward, right, right, left, left, right, right, left, right, left, right, right, left, forward, left, left, right, left, forward, forward, left, right, forward, left, right, right, left, left, forward, forward, forward, left, forward, right, right, forward, left, forward, left, left, right, forward, forward, forward, right, left, left, forward, right, right, left, right, right, left, right, forward, left, left, right, left, right, forward, left, right, right, forward, right, left, right, left, forward, left, forward, right, right, left, right, forward, left, left, forward, forward
```

**Full User-Facing Response (Final Answer):**
```
Left, Right, Left, Forward, Forward, Forward, Right, Left, Left, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Right, Left, Forward, Forward, Left, Right, Forward, Left, Right, Right, Left, Right, Left, Left, Right, Left, Right, Forward, Forward
```

**Internal Thoughts:**
```
**Maze Solving Thought Process**

Alright, let's break this down. I need to guide an agent through a 15x15 maze from (0,0) to (14,14). The agent starts facing South. The actions are Forward, Left, Right, Backward. I have a grid with each cell having wall information (N, E, S, W). I'll start by defining the agent's state: position (row, col) and direction (N, E, S, W).

I need to come up with a strategy to navigate. Mentally, I'll use a pathfinding algorithm to find a valid cell sequence first. I'm thinking something like Breadth-First Search (BFS) or Depth-First Search (DFS) would be a good starting point. I'll translate that cell sequence into the agent's actions later.

I'll execute this manually, carefully tracing a cell-by-cell path, while tracking the agent's position and direction. It's easy to make a small error, which has significant consequences. I need to be exact. This requires meticulous attention to the cell's wall information and the agent's orientation. I'll be sure to go backwards, to make sure I am on the correct path.

(0,0) has no S wall. Therefore, I must turn Left, going East.

Here's the planned path, and commands:

*   (0,0): **Left** (E)
*   (0,1): **Right** (S)
*   (1,1): **Left** (E)
*   (1,2): **Forward**
*   (1,3): **Forward**
*   (1,4): **Forward**
*   (1,5): **Right** (S)
*   (2,5): **Left** (E)
*   (2,6): **Left** (N)
*   (1,6): **Forward**
*   (0,6): **Right** (E)
*   (0,7): **Forward**
*   (0,8): **Forward**
*   (0,9): **Forward**
*   (0,10): **Forward**
*   (0,11): **Forward**
*   (0,12): **Forward**
*   (0,13): **Right** (S)
*   (1,13): **Forward**
*   (2,13): **Right** (W)
*   (2,12): **Left** (S)
*   (3,12): **Forward**
*   (4,12): **Forward**
*   (5,12): **Left** (E)
*   (5,13): **Right** (S)
*   (6,13): **Forward**
*   (7,13): **Left** (E)
*   (7,14): **Right** (S)
*   (8,14): **Right** (W)
*   (8,13): **Left** (S)
*   (9,13): **Right** (W)
*   (9,12): **Left** (S)
*   (10,12): **Left** (E)
*   (10,13): **Right** (S)
*   (11,13): **Left** (E)
*   (11,14): **Right** (S)
*   (12,14): **Forward**
*   (13,14): **Forward**

This set of action commands should successfully navigate the maze.

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Solving Thought Process**

Alright, let's break this down. I need to guide an agent through a 15x15 maze from (0,0) to (14,14). The agent starts facing South. The actions are Forward, Left, Right, Backward. I have a grid with each cell having wall information (N, E, S, W). I'll start by defining the agent's state: position (row, col) and direction (N, E, S, W).

I need to come up with a strategy to navigate. Mentally, I'll use a pathfinding algorithm to find a valid cell sequence first. I'm thinking something like Breadth-First Search (BFS) or Depth-First Search (DFS) would be a good starting point. I'll translate that cell sequence into the agent's actions later.

I'll execute this manually, carefully tracing a cell-by-cell path, while tracking the agent's position and direction. It's easy to make a small error, which has significant consequences. I need to be exact. This requires meticulous attention to the cell's wall information and the agent's orientation. I'll be sure to go backwards, to make sure I am on the correct path.

(0,0) has no S wall. Therefore, I must turn Left, going East.

Here's the planned path, and commands:

*   (0,0): **Left** (E)
*   (0,1): **Right** (S)
*   (1,1): **Left** (E)
*   (1,2): **Forward**
*   (1,3): **Forward**
*   (1,4): **Forward**
*   (1,5): **Right** (S)
*   (2,5): **Left** (E)
*   (2,6): **Left** (N)
*   (1,6): **Forward**
*   (0,6): **Right** (E)
*   (0,7): **Forward**
*   (0,8): **Forward**
*   (0,9): **Forward**
*   (0,10): **Forward**
*   (0,11): **Forward**
*   (0,12): **Forward**
*   (0,13): **Right** (S)
*   (1,13): **Forward**
*   (2,13): **Right** (W)
*   (2,12): **Left** (S)
*   (3,12): **Forward**
*   (4,12): **Forward**
*   (5,12): **Left** (E)
*   (5,13): **Right** (S)
*   (6,13): **Forward**
*   (7,13): **Left** (E)
*   (7,14): **Right** (S)
*   (8,14): **Right** (W)
*   (8,13): **Left** (S)
*   (9,13): **Right** (W)
*   (9,12): **Left** (S)
*   (10,12): **Left** (E)
*   (10,13): **Right** (S)
*   (11,13): **Left** (E)
*   (11,14): **Right** (S)
*   (12,14): **Forward**
*   (13,14): **Forward**

This set of action commands should successfully navigate the maze.
""",
        thought=True
      ),
      Part(
        text='Left, Right, Left, Forward, Forward, Forward, Right, Left, Left, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Right, Left, Forward, Forward, Left, Right, Forward, Left, Right, Right, Left, Right, Left, Left, Right, Left, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='pumSaZq8AuTA28oP_tSTgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=75,
  prompt_token_count=9924,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9924
    ),
  ],
  thoughts_token_count=18238,
  total_token_count=28237
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=311 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=75 candidates_tokens_details=None prompt_token_count=9924 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9924
)] thoughts_token_count=18238 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28237 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Solving Thought Process**

Alright, let's break this down. I need to guide an agent through a 15x15 maze from (0,0) to (14,14). The agent starts facing South. The actions are Forward, Left, Right, Backward. I have a grid with each cell having wall information (N, E, S, W). I'll start by defining the agent's state: position (row, col) and direction (N, E, S, W).

I need to come up with a strategy to navigate. Mentally, I'll use a pathfinding algorithm to find a valid cell sequence first. I'm thinking something like Breadth-First Search (BFS) or Depth-First Search (DFS) would be a good starting point. I'll translate that cell sequence into the agent's actions later.

I'll execute this manually, carefully tracing a cell-by-cell path, while tracking the agent's position and direction. It's easy to make a small error, which has significant consequences. I need to be exact. This requires meticulous attention to the cell's wall information and the agent's orientation. I'll be sure to go backwards, to make sure I am on the correct path.

(0,0) has no S wall. Therefore, I must turn Left, going East.

Here's the planned path, and commands:

*   (0,0): **Left** (E)
*   (0,1): **Right** (S)
*   (1,1): **Left** (E)
*   (1,2): **Forward**
*   (1,3): **Forward**
*   (1,4): **Forward**
*   (1,5): **Right** (S)
*   (2,5): **Left** (E)
*   (2,6): **Left** (N)
*   (1,6): **Forward**
*   (0,6): **Right** (E)
*   (0,7): **Forward**
*   (0,8): **Forward**
*   (0,9): **Forward**
*   (0,10): **Forward**
*   (0,11): **Forward**
*   (0,12): **Forward**
*   (0,13): **Right** (S)
*   (1,13): **Forward**
*   (2,13): **Right** (W)
*   (2,12): **Left** (S)
*   (3,12): **Forward**
*   (4,12): **Forward**
*   (5,12): **Left** (E)
*   (5,13): **Right** (S)
*   (6,13): **Forward**
*   (7,13): **Left** (E)
*   (7,14): **Right** (S)
*   (8,14): **Right** (W)
*   (8,13): **Left** (S)
*   (9,13): **Right** (W)
*   (9,12): **Left** (S)
*   (10,12): **Left** (E)
*   (10,13): **Right** (S)
*   (11,13): **Left** (E)
*   (11,14): **Right** (S)
*   (12,14): **Forward**
*   (13,14): **Forward**

This set of action commands should successfully navigate the maze.
""",
        thought=True
      ),
      Part(
        text='Left, Right, Left, Forward, Forward, Forward, Right, Left, Left, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Right, Left, Forward, Forward, Left, Right, Forward, Left, Right, Right, Left, Right, Left, Left, Right, Left, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

