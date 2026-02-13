# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-pro`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_26.jpg` | **0.00%** | `input: 551 , ouput: 1686` | `forward, left, right, forward, right, left, forward, left, forward, forward` |
| `maze_line_6x6_26.json` | **100.00%** | `input: 1926 , ouput: 6715` | `left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right` |

---

## Full LLM Responses

### `maze_line_6x6_26.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Full User-Facing Response (Final Answer):**
```
forward,left,right,forward,right,left,forward,left,forward,forward
```

**Internal Thoughts:**
```
**Maze Navigation Strategy**

Okay, so I've got a 6x6 maze problem to tackle. My primary goal is to determine the action sequence for an agent to move from a specific start point (0, 1) to a target end point (5, 4) in the grid, abiding by its available actions: `Forward`, `Left`, `Right`, and `Backward`, with no movement through walls. The agent starts facing South.

My initial approach will be to visually trace a path through the maze. I will start by identifying the obvious moves at each step, taking note of the agent's current position and orientation. I see the path immediately leads South.  I will then systematically trace the most direct route, coordinating the actions required with the turning and movement capabilities of the agent.

I'll start with a methodical traversal. At (0, 1), facing South, the first step is `Forward` to (1, 1). Next, the path heads East, thus a `Left` turn, then `Forward` to (1, 2). Continue the path:  South to (2, 2) which requires `Right` and `Forward`. South to (3, 2), then a `Forward` move. West to (3, 1), requires a `Right`, then `Forward`. South to (4, 1), needing a `Left`, then `Forward`. South to (5, 1) and another `Forward`. East to (5, 2) which requires a `Left`, then `Forward`, East to (5, 3) which is `Forward`. Finally, East to the destination (5, 4) with `Forward`.

Now, I'll translate the traced path into a sequence of agent instructions, carefully tracking the agent's position and direction at each move. I'll translate these moves into a comma-separated action string.

I need to confirm all the actions and verify the output. I'll double-check to ensure the sequence of actions I created effectively moves the agent through the maze in the correct direction.

So, the definitive instructions are: `forward,left,right,forward,right,left,forward,left,forward,forward`.

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Navigation Strategy**

Okay, so I've got a 6x6 maze problem to tackle. My primary goal is to determine the action sequence for an agent to move from a specific start point (0, 1) to a target end point (5, 4) in the grid, abiding by its available actions: `Forward`, `Left`, `Right`, and `Backward`, with no movement through walls. The agent starts facing South.

My initial approach will be to visually trace a path through the maze. I will start by identifying the obvious moves at each step, taking note of the agent's current position and orientation. I see the path immediately leads South.  I will then systematically trace the most direct route, coordinating the actions required with the turning and movement capabilities of the agent.

I'll start with a methodical traversal. At (0, 1), facing South, the first step is `Forward` to (1, 1). Next, the path heads East, thus a `Left` turn, then `Forward` to (1, 2). Continue the path:  South to (2, 2) which requires `Right` and `Forward`. South to (3, 2), then a `Forward` move. West to (3, 1), requires a `Right`, then `Forward`. South to (4, 1), needing a `Left`, then `Forward`. South to (5, 1) and another `Forward`. East to (5, 2) which requires a `Left`, then `Forward`, East to (5, 3) which is `Forward`. Finally, East to the destination (5, 4) with `Forward`.

Now, I'll translate the traced path into a sequence of agent instructions, carefully tracking the agent's position and direction at each move. I'll translate these moves into a comma-separated action string.

I need to confirm all the actions and verify the output. I'll double-check to ensure the sequence of actions I created effectively moves the agent through the maze in the correct direction.

So, the definitive instructions are: `forward,left,right,forward,right,left,forward,left,forward,forward`.
""",
        thought=True
      ),
      Part(
        text='forward,left,right,forward,right,left,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='SACPaaxJ0qKewQ_72JroCw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=551,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=293
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  thoughts_token_count=1667,
  total_token_count=2237
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=551 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=1667 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2237 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Navigation Strategy**

Okay, so I've got a 6x6 maze problem to tackle. My primary goal is to determine the action sequence for an agent to move from a specific start point (0, 1) to a target end point (5, 4) in the grid, abiding by its available actions: `Forward`, `Left`, `Right`, and `Backward`, with no movement through walls. The agent starts facing South.

My initial approach will be to visually trace a path through the maze. I will start by identifying the obvious moves at each step, taking note of the agent's current position and orientation. I see the path immediately leads South.  I will then systematically trace the most direct route, coordinating the actions required with the turning and movement capabilities of the agent.

I'll start with a methodical traversal. At (0, 1), facing South, the first step is `Forward` to (1, 1). Next, the path heads East, thus a `Left` turn, then `Forward` to (1, 2). Continue the path:  South to (2, 2) which requires `Right` and `Forward`. South to (3, 2), then a `Forward` move. West to (3, 1), requires a `Right`, then `Forward`. South to (4, 1), needing a `Left`, then `Forward`. South to (5, 1) and another `Forward`. East to (5, 2) which requires a `Left`, then `Forward`, East to (5, 3) which is `Forward`. Finally, East to the destination (5, 4) with `Forward`.

Now, I'll translate the traced path into a sequence of agent instructions, carefully tracking the agent's position and direction at each move. I'll translate these moves into a comma-separated action string.

I need to confirm all the actions and verify the output. I'll double-check to ensure the sequence of actions I created effectively moves the agent through the maze in the correct direction.

So, the definitive instructions are: `forward,left,right,forward,right,left,forward,left,forward,forward`.
""",
        thought=True
      ),
      Part(
        text='forward,left,right,forward,right,left,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

### `maze_line_6x6_26.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Full User-Facing Response (Final Answer):**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Internal Thoughts:**
```
**Maze Solving Algorithm and Action Sequence**

Okay, I've got this. The user wants me to solve a 6x6 maze. The goal is to navigate from the start [0, 0] to the end [5, 5], given a 2D grid of cells each with wall information and actions for the agent to take. The agent starts facing South. The actions are Forward, Left, Right and Backward.

First, I need to understand how each action impacts the agent's position and orientation. Forward moves one step in the current facing direction. Left is a 90° left turn, then one step. Right is 90° right turn, then one step, and Backward is a 180° turn, then one step.

Let's begin. I will need to trace a path through the maze. I start at (0, 0) facing South. The initial wall checks show that South is closed, so I cannot take the Forward direction. Turning West is not an option either, because the walls indicate it's blocked. So, Left gives me the only possible first move and takes me to (0, 1) facing East.

I'll proceed to examine each possible move at (0, 1), and at each next location. I've to check the surrounding walls and then decide the next action based on the agent's current facing direction. I'm going to follow the logic until I get to the destination. Since there are several possibilities and paths, I need to choose the ones that are most efficient and make sure the wall constraints are met. I start at the beginning.

Based on the wall information, I can see that going South would mean going to a dead-end at the beginning. Hence, I'm going to take the correct path from (0, 0).
The path is:
(0,0) E-> (0,1)
(0,1) S-> (1,1)
(1,1) W-> (1,0)
(1,0) S-> (2,0)
(2,0) E-> (2,1)
(2,1) S-> (3,1)
(3,1) W-> (3,0)
(3,0) S-> (4,0)
(4,0) S-> (5,0)
(5,0) E-> (5,1)
(5,1) E-> (5,2)
(5,2) N-> (4,2)
(4,2) E-> (4,3) -> (4,4) -> (4,5) -> (5,5)

Once I have traced the path, I need to translate it into a sequence of the agent's actions. I'll need to keep track of the current direction at each position. The agent starts facing South, so the first step needs to turn to the East. I calculate the turns and then write them as an action sequence. I double-check each step. Finally, I will output the comma separated sequence of instructions:

`Left, Right, Right, Left, Left, Right, Right, Left, Forward, Left, Forward, Left, Right, Forward, Forward, Right`

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Solving Algorithm and Action Sequence**

Okay, I've got this. The user wants me to solve a 6x6 maze. The goal is to navigate from the start [0, 0] to the end [5, 5], given a 2D grid of cells each with wall information and actions for the agent to take. The agent starts facing South. The actions are Forward, Left, Right and Backward.

First, I need to understand how each action impacts the agent's position and orientation. Forward moves one step in the current facing direction. Left is a 90° left turn, then one step. Right is 90° right turn, then one step, and Backward is a 180° turn, then one step.

Let's begin. I will need to trace a path through the maze. I start at (0, 0) facing South. The initial wall checks show that South is closed, so I cannot take the Forward direction. Turning West is not an option either, because the walls indicate it's blocked. So, Left gives me the only possible first move and takes me to (0, 1) facing East.

I'll proceed to examine each possible move at (0, 1), and at each next location. I've to check the surrounding walls and then decide the next action based on the agent's current facing direction. I'm going to follow the logic until I get to the destination. Since there are several possibilities and paths, I need to choose the ones that are most efficient and make sure the wall constraints are met. I start at the beginning.

Based on the wall information, I can see that going South would mean going to a dead-end at the beginning. Hence, I'm going to take the correct path from (0, 0).
The path is:
(0,0) E-> (0,1)
(0,1) S-> (1,1)
(1,1) W-> (1,0)
(1,0) S-> (2,0)
(2,0) E-> (2,1)
(2,1) S-> (3,1)
(3,1) W-> (3,0)
(3,0) S-> (4,0)
(4,0) S-> (5,0)
(5,0) E-> (5,1)
(5,1) E-> (5,2)
(5,2) N-> (4,2)
(4,2) E-> (4,3) -> (4,4) -> (4,5) -> (5,5)

Once I have traced the path, I need to translate it into a sequence of the agent's actions. I'll need to keep track of the current direction at each position. The agent starts facing South, so the first step needs to turn to the East. I calculate the turns and then write them as an action sequence. I double-check each step. Finally, I will output the comma separated sequence of instructions:

`Left, Right, Right, Left, Left, Right, Right, Left, Forward, Left, Forward, Left, Right, Forward, Forward, Right`
""",
        thought=True
      ),
      Part(
        text='left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='fwCPaffFFYb1kdUP6uq64Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=1926,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1926
    ),
  ],
  thoughts_token_count=6684,
  total_token_count=8641
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=309 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=1926 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1926
)] thoughts_token_count=6684 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8641 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Maze Solving Algorithm and Action Sequence**

Okay, I've got this. The user wants me to solve a 6x6 maze. The goal is to navigate from the start [0, 0] to the end [5, 5], given a 2D grid of cells each with wall information and actions for the agent to take. The agent starts facing South. The actions are Forward, Left, Right and Backward.

First, I need to understand how each action impacts the agent's position and orientation. Forward moves one step in the current facing direction. Left is a 90° left turn, then one step. Right is 90° right turn, then one step, and Backward is a 180° turn, then one step.

Let's begin. I will need to trace a path through the maze. I start at (0, 0) facing South. The initial wall checks show that South is closed, so I cannot take the Forward direction. Turning West is not an option either, because the walls indicate it's blocked. So, Left gives me the only possible first move and takes me to (0, 1) facing East.

I'll proceed to examine each possible move at (0, 1), and at each next location. I've to check the surrounding walls and then decide the next action based on the agent's current facing direction. I'm going to follow the logic until I get to the destination. Since there are several possibilities and paths, I need to choose the ones that are most efficient and make sure the wall constraints are met. I start at the beginning.

Based on the wall information, I can see that going South would mean going to a dead-end at the beginning. Hence, I'm going to take the correct path from (0, 0).
The path is:
(0,0) E-> (0,1)
(0,1) S-> (1,1)
(1,1) W-> (1,0)
(1,0) S-> (2,0)
(2,0) E-> (2,1)
(2,1) S-> (3,1)
(3,1) W-> (3,0)
(3,0) S-> (4,0)
(4,0) S-> (5,0)
(5,0) E-> (5,1)
(5,1) E-> (5,2)
(5,2) N-> (4,2)
(4,2) E-> (4,3) -> (4,4) -> (4,5) -> (5,5)

Once I have traced the path, I need to translate it into a sequence of the agent's actions. I'll need to keep track of the current direction at each position. The agent starts facing South, so the first step needs to turn to the East. I calculate the turns and then write them as an action sequence. I double-check each step. Finally, I will output the comma separated sequence of instructions:

`Left, Right, Right, Left, Left, Right, Right, Left, Forward, Left, Forward, Left, Right, Forward, Forward, Right`
""",
        thought=True
      ),
      Part(
        text='left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

