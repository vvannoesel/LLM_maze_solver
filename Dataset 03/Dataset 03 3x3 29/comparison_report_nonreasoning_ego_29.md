# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_29.jpg` | **0.00%** | `input: 551 , ouput: 17` | `right, forward, right, forward, forward, right, forward, left, forward` |
| `maze_line_3x3_29.json` | **0.00%** | `input: 774 , ouput: 17` | `right, forward, forward, right, forward, right, forward, left, forward` |
| `maze_line_3x3_adj_29.json` | **0.00%** | `input: 836 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_29.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_29.txt` | **0.00%** | `input: 439 , ouput: 643` | `the, maze, is, represented, as, follows:, (0, 0):, <|uprightleft_wall|>, <|origin|>, (0, 1):, <|updownleft_wall|>, (0, 2):, <|upright_wall|>, (1, 0):, <|downleft_wall|>, (1, 1):, <|updown_wall|>, (1, 2):, <|right_wall|>, (2, 0):, <|updownleft_wall|>, (2, 1):, <|updown_wall|>, (2, 2):, <|downright_wall|>, <|target|>, let's, break, down, the, maze, and, find, the, path., **maze, analysis:**, *, **start, (0, 0):**, has, walls, to, the, up, right, and, left., this, means, the, only, possible, move, from, (0, 0), is, down., *, **(0, 1):**, has, walls, to, the, up, down, and, left., this, means, the, only, possible, move, from, (0, 1), is, right., *, **(0, 2):**, has, walls, to, the, up, and, right., *, **(1, 0):**, has, walls, to, the, down, left., *, **(1, 1):**, has, walls, to, the, up, and, down., *, **(1, 2):**, has, a, wall, to, the, right., *, **(2, 0):**, has, walls, to, the, up, down, and, left., *, **(2, 1):**, has, walls, to, the, up, and, down., *, **end, (2, 2):**, has, walls, to, the, down, and, right., **pathfinding:**, the, agent, starts, at, (0, 0), facing, south., 1., from, (0, 0), the, only, available, move, is, **forward**., this, takes, the, agent, to, (1, 0)., the, agent, is, now, facing, south., 2., at, (1, 0), the, agent, has, walls, to, the, down, and, left., to, move, right, to, (1, 1), the, agent, needs, to, turn, left., so, the, instruction, is, **left**., the, agent, is, now, facing, east., 3., from, (1, 0), facing, east, move, **forward**., this, takes, the, agent, to, (1, 1)., the, agent, is, now, facing, east., 4., at, (1, 1), the, agent, has, walls, to, the, up, and, down., to, move, to, (1, 2), the, agent, needs, to, continue, facing, east., so, move, **forward**., this, takes, the, agent, to, (1, 2)., the, agent, is, now, facing, east., 5., at, (1, 2), the, agent, has, a, wall, to, the, right., to, move, to, (2, 2), the, agent, needs, to, turn, right., so, the, instruction, is, **right**., the, agent, is, now, facing, south., 6., from, (1, 2), facing, south, move, **forward**., this, takes, the, agent, to, (2, 2), the, target., therefore, the, sequence, of, instructions, is:, forward, left, forward, forward, right, forward` |
| `maze_occupancy_3x3_29.jpg` | **0.00%** | `input: 546 , ouput: 73` | `right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_29.json` | **0.00%** | `input: 589 , ouput: 79` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_29.json` | **0.00%** | `input: 1292 , ouput: 25` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_29.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, forward, forward, forward, right, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right` |
| `maze_occupancy_3x3_ascii_29.txt` | **0.00%** | `input: 315 , ouput: 650` | `right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward` |
| `maze_occupancy_3x3_tokenized_29.txt` | **12.50%** | `input: 867 , ouput: 650` | `forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_29.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,right,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aZmVadTjCIyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
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
  total_token_count=568
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=568 traffic_type=None
```

### `maze_line_3x3_29.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Right,Forward,Right,Forward,Left,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aZmVaeTrIYOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=791
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=791 traffic_type=None
```

### `maze_line_3x3_adj_29.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='apmVac-FBPnOnsEPkprNkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=847
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=280 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=847 traffic_type=None
```

### `maze_line_3x3_adj_29.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='apmVaeq7KffnnsEPornoiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=481
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=313 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=481 traffic_type=None
```

### `maze_line_3x3_tokenized_29.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows:, (0, 0):, <|uprightleft_wall|>, <|origin|>, (0, 1):, <|updownleft_wall|>, (0, 2):, <|upright_wall|>, (1, 0):, <|downleft_wall|>, (1, 1):, <|updown_wall|>, (1, 2):, <|right_wall|>, (2, 0):, <|updownleft_wall|>, (2, 1):, <|updown_wall|>, (2, 2):, <|downright_wall|>, <|target|>, let's, break, down, the, maze, and, find, the, path., **maze, analysis:**, *, **start, (0, 0):**, has, walls, to, the, up, right, and, left., this, means, the, only, possible, move, from, (0, 0), is, down., *, **(0, 1):**, has, walls, to, the, up, down, and, left., this, means, the, only, possible, move, from, (0, 1), is, right., *, **(0, 2):**, has, walls, to, the, up, and, right., *, **(1, 0):**, has, walls, to, the, down, left., *, **(1, 1):**, has, walls, to, the, up, and, down., *, **(1, 2):**, has, a, wall, to, the, right., *, **(2, 0):**, has, walls, to, the, up, down, and, left., *, **(2, 1):**, has, walls, to, the, up, and, down., *, **end, (2, 2):**, has, walls, to, the, down, and, right., **pathfinding:**, the, agent, starts, at, (0, 0), facing, south., 1., from, (0, 0), the, only, available, move, is, **forward**., this, takes, the, agent, to, (1, 0)., the, agent, is, now, facing, south., 2., at, (1, 0), the, agent, has, walls, to, the, down, and, left., to, move, right, to, (1, 1), the, agent, needs, to, turn, left., so, the, instruction, is, **left**., the, agent, is, now, facing, east., 3., from, (1, 0), facing, east, move, **forward**., this, takes, the, agent, to, (1, 1)., the, agent, is, now, facing, east., 4., at, (1, 1), the, agent, has, walls, to, the, up, and, down., to, move, to, (1, 2), the, agent, needs, to, continue, facing, east., so, move, **forward**., this, takes, the, agent, to, (1, 2)., the, agent, is, now, facing, east., 5., at, (1, 2), the, agent, has, a, wall, to, the, right., to, move, to, (2, 2), the, agent, needs, to, turn, right., so, the, instruction, is, **right**., the, agent, is, now, facing, south., 6., from, (1, 2), facing, south, move, **forward**., this, takes, the, agent, to, (2, 2), the, target., therefore, the, sequence, of, instructions, is:, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is represented as follows:

(0,0): <|uprightleft_wall|> <|origin|>
(0,1): <|updownleft_wall|>
(0,2): <|upright_wall|>
(1,0): <|downleft_wall|>
(1,1): <|updown_wall|>
(1,2): <|right_wall|>
(2,0): <|updownleft_wall|>
(2,1): <|updown_wall|>
(2,2): <|downright_wall|> <|target|>

Let's break down the maze and find the path.

**Maze Analysis:**

*   **Start (0,0):** Has walls to the up, right, and left. This means the only possible move from (0,0) is down.
*   **(0,1):** Has walls to the up, down, and left. This means the only possible move from (0,1) is right.
*   **(0,2):** Has walls to the up and right.
*   **(1,0):** Has walls to the down, left.
*   **(1,1):** Has walls to the up and down.
*   **(1,2):** Has a wall to the right.
*   **(2,0):** Has walls to the up, down, and left.
*   **(2,1):** Has walls to the up and down.
*   **End (2,2):** Has walls to the down and right.

**Pathfinding:**

The agent starts at (0,0) facing South.

1.  From (0,0), the only available move is **forward**. This takes the agent to (1,0). The agent is now facing South.
2.  At (1,0), the agent has walls to the down and left. To move right to (1,1), the agent needs to turn Left. So, the instruction is **left**. The agent is now facing East.
3.  From (1,0) facing East, move **forward**. This takes the agent to (1,1). The agent is now facing East.
4.  At (1,1), the agent has walls to the up and down. To move to (1,2), the agent needs to continue facing East. So, move **forward**. This takes the agent to (1,2). The agent is now facing East.
5.  At (1,2), the agent has a wall to the right. To move to (2,2), the agent needs to turn Right. So, the instruction is **right**. The agent is now facing South.
6.  From (1,2) facing South, move **forward**. This takes the agent to (2,2), the target.

Therefore, the sequence of instructions is: forward, left, forward, forward, right, forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bZmVaeCQAtqfnsEPvPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=643,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=1082
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=643 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1082 traffic_type=None
```

### `maze_occupancy_3x3_29.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bZmVadzjNJzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  cache_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=163
    ),
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=182
    ),
  ],
  cached_content_token_count=345,
  candidates_token_count=73,
  prompt_token_count=546,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=288
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=619
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=546 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=163
), ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=182
)] cached_content_token_count=345 candidates_token_count=73 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=619 traffic_type=None
```

### `maze_occupancy_3x3_29.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bpmVabmbJIqjkdUPl43u2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=79,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=668
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=289 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=79 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=668 traffic_type=None
```

### `maze_occupancy_3x3_adj_29.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='b5mVaYeeEcjl7M8P9OOViAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1317
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=280 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1317 traffic_type=None
```

### `maze_occupancy_3x3_adj_29.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cZmVafyhA_7MkdUPkdfHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=1230
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=313 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1230 traffic_type=None
```

### `maze_occupancy_3x3_ascii_29.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cpmVaaXpN-O9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=965
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=288 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=965 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_29.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=256,
        license='',
        start_index=16,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=415,
        license='',
        start_index=163,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dJmVadaMHseC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1517
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=312 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1517 traffic_type=None
```

