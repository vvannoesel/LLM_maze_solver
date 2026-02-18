# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_22.jpg` | **0.00%** | `input: 551 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_22.json` | **0.00%** | `input: 774 , ouput: 15` | `right, forward, right, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_22.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, forward, right, forward, left, forward` |
| `maze_line_3x3_adj_22.txt` | **0.00%** | `input: 468 , ouput: 21` | `right, forward, right, forward, right, forward, left, forward, left, forward, forward` |
| `maze_line_3x3_tokenized_22.txt` | **0.00%** | `input: 439 , ouput: 650` | `the, maze, is, represented, as, follows:, (0, 0):, origin, has, top, down, and, left, walls., (0, 1):, no, walls., (0, 2):, has, top, right, and, left, walls., (1, 0):, has, up, left, walls., (1, 1):, has, down, right, walls., (1, 2):, has, right, left, walls., (2, 0):, has, down, left, walls., (2, 1):, has, up, down, walls., (2, 2):, target, has, down, right, walls., the, agent, starts, at, (0, 0), facing, south., let's, trace, the, path:, *, **start, at, (0, 0), facing, south.**, *, to, move, out, of, (0, 0), we, need, to, move, down., *, `forward`, (agent, moves, to, (1, 0), still, facing, south), *, at, (1, 0), we, have, up, and, left, walls., we, need, to, move, right, to, reach, (1, 1)., *, `right`, (agent, turns, 90°, right, now, facing, west., then, moves, forward, to, (1, 1)., oh, wait, this, is, wrong., the, instruction, is, "left:, this, turns, the, agent, 90°, to, the, left, and, then, moves, the, agent, 1, step, in, the, new, direction, it, is, facing.", and, "right:, this, turns, the, agent, 90°, to, the, right, and, then, moves, the, agent, 1, step, in, the, new, direction, it, is, facing."., so, at, (1, 0), facing, south, to, go, right, to, (1, 1), we, need, to, turn, left, first.), *, `left`, (agent, turns, 90°, left, now, facing, east., moves, forward, to, (1, 1)), *, at, (1, 1), we, have, down, and, right, walls., we, need, to, go, to, (1, 2)., *, `forward`, (agent, moves, to, (1, 2), still, facing, east), *, at, (1, 2), we, have, right, and, left, walls., we, need, to, go, to, (2, 2)., *, `right`, (agent, turns, 90°, right, now, facing, south., moves, forward, to, (2, 2)), let's, retrace, carefully:, 1., **start, at, (0, 0), facing, south.**, *, cell, (0, 0), has, `<|updownleft_wall|>`., this, means, there, is, no, wall, on, the, right., *, to, move, from, (0, 0), to, (0, 1), we, need, to, move, east., since, the, agent, is, facing, south, we, need, to, turn, left, twice, (90°, +, 90°, =, 180°), to, face, north, then, turn, left, again, to, face, west, then, turn, left, again, to, face, east., this, is, too, many, turns., *, let's, consider, the, walls., *, (0, 0):, top, down, left, walls., (can't, go, up, down, left)., so, can, only` |
| `maze_occupancy_3x3_22.jpg` | **0.00%** | `input: 546 , ouput: 27` | `right, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_22.json` | **0.00%** | `input: 589 , ouput: 73` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_22.json` | **0.00%** | `input: 1292 , ouput: 85` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_22.txt` | **0.00%** | `input: 580 , ouput: 650` | `the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., here's, a, possible, path:, 1., the, agent, is, at, (1, 1), facing, south., it, needs, to, go, to, (1, 2), which, is, to, its, right., -, action:, right, -, now, at, (1, 1), facing, west., -, action:, forward, -, now, at, (1, 2), facing, west., 2., from, (1, 2), the, agent, needs, to, go, to, (1, 3), which, is, to, its, right., -, action:, right, -, now, at, (1, 2), facing, north., -, action:, forward, -, now, at, (1, 3), facing, north., 3., from, (1, 3), the, agent, needs, to, go, to, (2, 3), which, is, in, front., -, action:, forward, -, now, at, (2, 3), facing, north., 4., from, (2, 3), the, agent, needs, to, go, to, (3, 3), which, is, in, front., -, action:, forward, -, now, at, (3, 3), facing, north., 5., from, (3, 3), the, agent, needs, to, go, to, (3, 2), which, is, to, its, left., -, action:, left, -, now, at, (3, 3), facing, west., -, action:, forward, -, now, at, (3, 2), facing, west., 6., from, (3, 2), the, agent, needs, to, go, to, (3, 1), which, is, in, front., -, action:, forward, -, now, at, (3, 1), facing, west., 7., from, (3, 1), the, agent, needs, to, go, to, (4, 1), which, is, in, front., -, action:, forward, -, now, at, (4, 1), facing, west., 8., from, (4, 1), the, agent, needs, to, go, to, (5, 1), which, is, in, front., -, action:, forward, -, now, at, (5, 1), facing, west., 9., from, (5, 1), the, agent, needs, to, go, to, (5, 2), which, is, to, its, right., -, action:, right, -, now, at, (5, 1), facing, north., -, action:, forward, -, now, at, (5, 2), facing, north., 10., from, (5, 2), the, agent, needs, to, go, to, (5, 3), which, is, to, its, right., -, action:, right, -, now, at, (5, 2), facing, east., -, action:, forward, -, now, at, (5, 3), facing, east., 11., from, (5, 3), the, agent, needs, to, go, to, (5, 4), which, is, in, front., -, action:, forward, -, now, at, (5, 4), facing, east., 12., from, (5, 4), the, agent, needs, to, go, to, (5, 5), which, is, in, front., -, action` |
| `maze_occupancy_3x3_ascii_22.txt` | **0.00%** | `input: 317 , ouput: 35` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_tokenized_22.txt` | **0.00%** | `input: 867 , ouput: 650` | `forward, right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left` |

---

## Full LLM Responses

### `maze_line_3x3_22.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
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
        text='right,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='l5eVadnkMqSDkdUP5IaYkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
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
  total_token_count=564
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=564 traffic_type=None
```

### `maze_line_3x3_22.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mJeVaZWeF-TQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=789
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=789 traffic_type=None
```

### `maze_line_3x3_adj_22.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mZeVacVh4oCR1Q-IjYSZCw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=853
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=853 traffic_type=None
```

### `maze_line_3x3_adj_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Left, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mZeVacDoHYKN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=489
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=489 traffic_type=None
```

### `maze_line_3x3_tokenized_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows:, (0, 0):, origin, has, top, down, and, left, walls., (0, 1):, no, walls., (0, 2):, has, top, right, and, left, walls., (1, 0):, has, up, left, walls., (1, 1):, has, down, right, walls., (1, 2):, has, right, left, walls., (2, 0):, has, down, left, walls., (2, 1):, has, up, down, walls., (2, 2):, target, has, down, right, walls., the, agent, starts, at, (0, 0), facing, south., let's, trace, the, path:, *, **start, at, (0, 0), facing, south.**, *, to, move, out, of, (0, 0), we, need, to, move, down., *, `forward`, (agent, moves, to, (1, 0), still, facing, south), *, at, (1, 0), we, have, up, and, left, walls., we, need, to, move, right, to, reach, (1, 1)., *, `right`, (agent, turns, 90°, right, now, facing, west., then, moves, forward, to, (1, 1)., oh, wait, this, is, wrong., the, instruction, is, "left:, this, turns, the, agent, 90°, to, the, left, and, then, moves, the, agent, 1, step, in, the, new, direction, it, is, facing.", and, "right:, this, turns, the, agent, 90°, to, the, right, and, then, moves, the, agent, 1, step, in, the, new, direction, it, is, facing."., so, at, (1, 0), facing, south, to, go, right, to, (1, 1), we, need, to, turn, left, first.), *, `left`, (agent, turns, 90°, left, now, facing, east., moves, forward, to, (1, 1)), *, at, (1, 1), we, have, down, and, right, walls., we, need, to, go, to, (1, 2)., *, `forward`, (agent, moves, to, (1, 2), still, facing, east), *, at, (1, 2), we, have, right, and, left, walls., we, need, to, go, to, (2, 2)., *, `right`, (agent, turns, 90°, right, now, facing, south., moves, forward, to, (2, 2)), let's, retrace, carefully:, 1., **start, at, (0, 0), facing, south.**, *, cell, (0, 0), has, `<|updownleft_wall|>`., this, means, there, is, no, wall, on, the, right., *, to, move, from, (0, 0), to, (0, 1), we, need, to, move, east., since, the, agent, is, facing, south, we, need, to, turn, left, twice, (90°, +, 90°, =, 180°), to, face, north, then, turn, left, again, to, face, west, then, turn, left, again, to, face, east., this, is, too, many, turns., *, let's, consider, the, walls., *, (0, 0):, top, down, left, walls., (can't, go, up, down, left)., so, can, only
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

(0,0): Origin, has top, down, and left walls.
(0,1): No walls.
(0,2): Has top, right, and left walls.
(1,0): Has up, left walls.
(1,1): Has down, right walls.
(1,2): Has right, left walls.
(2,0): Has down, left walls.
(2,1): Has up, down walls.
(2,2): Target, has down, right walls.

The agent starts at (0,0) facing South.

Let's trace the path:

*   **Start at (0,0), facing South.**
*   To move out of (0,0), we need to move Down.
    *   `forward` (Agent moves to (1,0), still facing South)
*   At (1,0), we have up and left walls. We need to move Right to reach (1,1).
    *   `right` (Agent turns 90° right, now facing West. Then moves Forward to (1,1). Oh wait, this is wrong. The instruction is "Left: this turns the agent 90° to the left and then moves the agent 1 step in the new direction it is facing." and "Right: this turns the agent 90° to the right and then moves the agent 1 step in the new direction it is facing.". So, at (1,0) facing South, to go Right to (1,1), we need to turn Left first.)
    *   `left` (Agent turns 90° left, now facing East. Moves Forward to (1,1))
*   At (1,1), we have down and right walls. We need to go to (1,2).
    *   `forward` (Agent moves to (1,2), still facing East)
*   At (1,2), we have right and left walls. We need to go to (2,2).
    *   `right` (Agent turns 90° right, now facing South. Moves Forward to (2,2))

Let's retrace carefully:

1.  **Start at (0,0), facing South.**
    *   Cell (0,0) has `<|updownleft_wall|>`. This means there is no wall on the right.
    *   To move from (0,0) to (0,1), we need to move East. Since the agent is facing South, we need to turn left twice (90° + 90° = 180°) to face North, then turn left again to face West, then turn left again to face East. This is too many turns.
    *   Let's consider the walls.
        *   (0,0): top, down, left walls. (Can't go up, down, left). So can only"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nJeVaam3CbT7nsEPovPikQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=1089
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1089 traffic_type=None
```

### `maze_occupancy_3x3_22.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nJeVadK-KryK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
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
  total_token_count=573
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=573 traffic_type=None
```

### `maze_occupancy_3x3_22.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,left,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nZeVabW5IoTensEP6bbt4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=73,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=662
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=73 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=662 traffic_type=None
```

### `maze_occupancy_3x3_adj_22.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='npeVacTZE9qfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1377
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1377 traffic_type=None
```

### `maze_occupancy_3x3_adj_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., here's, a, possible, path:, 1., the, agent, is, at, (1, 1), facing, south., it, needs, to, go, to, (1, 2), which, is, to, its, right., -, action:, right, -, now, at, (1, 1), facing, west., -, action:, forward, -, now, at, (1, 2), facing, west., 2., from, (1, 2), the, agent, needs, to, go, to, (1, 3), which, is, to, its, right., -, action:, right, -, now, at, (1, 2), facing, north., -, action:, forward, -, now, at, (1, 3), facing, north., 3., from, (1, 3), the, agent, needs, to, go, to, (2, 3), which, is, in, front., -, action:, forward, -, now, at, (2, 3), facing, north., 4., from, (2, 3), the, agent, needs, to, go, to, (3, 3), which, is, in, front., -, action:, forward, -, now, at, (3, 3), facing, north., 5., from, (3, 3), the, agent, needs, to, go, to, (3, 2), which, is, to, its, left., -, action:, left, -, now, at, (3, 3), facing, west., -, action:, forward, -, now, at, (3, 2), facing, west., 6., from, (3, 2), the, agent, needs, to, go, to, (3, 1), which, is, in, front., -, action:, forward, -, now, at, (3, 1), facing, west., 7., from, (3, 1), the, agent, needs, to, go, to, (4, 1), which, is, in, front., -, action:, forward, -, now, at, (4, 1), facing, west., 8., from, (4, 1), the, agent, needs, to, go, to, (5, 1), which, is, in, front., -, action:, forward, -, now, at, (5, 1), facing, west., 9., from, (5, 1), the, agent, needs, to, go, to, (5, 2), which, is, to, its, right., -, action:, right, -, now, at, (5, 1), facing, north., -, action:, forward, -, now, at, (5, 2), facing, north., 10., from, (5, 2), the, agent, needs, to, go, to, (5, 3), which, is, to, its, right., -, action:, right, -, now, at, (5, 2), facing, east., -, action:, forward, -, now, at, (5, 3), facing, east., 11., from, (5, 3), the, agent, needs, to, go, to, (5, 4), which, is, in, front., -, action:, forward, -, now, at, (5, 4), facing, east., 12., from, (5, 4), the, agent, needs, to, go, to, (5, 5), which, is, in, front., -, action
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (1,1) facing South. The target is at (5,5).

Here's a possible path:

1. The agent is at (1,1) facing South. It needs to go to (1,2) which is to its right.
   - Action: right
   - Now at (1,1) facing West.
   - Action: forward
   - Now at (1,2) facing West.
2. From (1,2), the agent needs to go to (1,3) which is to its right.
   - Action: right
   - Now at (1,2) facing North.
   - Action: forward
   - Now at (1,3) facing North.
3. From (1,3), the agent needs to go to (2,3) which is in front.
   - Action: forward
   - Now at (2,3) facing North.
4. From (2,3), the agent needs to go to (3,3) which is in front.
   - Action: forward
   - Now at (3,3) facing North.
5. From (3,3), the agent needs to go to (3,2) which is to its left.
   - Action: left
   - Now at (3,3) facing West.
   - Action: forward
   - Now at (3,2) facing West.
6. From (3,2), the agent needs to go to (3,1) which is in front.
   - Action: forward
   - Now at (3,1) facing West.
7. From (3,1), the agent needs to go to (4,1) which is in front.
   - Action: forward
   - Now at (4,1) facing West.
8. From (4,1), the agent needs to go to (5,1) which is in front.
   - Action: forward
   - Now at (5,1) facing West.
9. From (5,1), the agent needs to go to (5,2) which is to its right.
   - Action: right
   - Now at (5,1) facing North.
   - Action: forward
   - Now at (5,2) facing North.
10. From (5,2), the agent needs to go to (5,3) which is to its right.
   - Action: right
   - Now at (5,2) facing East.
   - Action: forward
   - Now at (5,3) facing East.
11. From (5,3), the agent needs to go to (5,4) which is in front.
   - Action: forward
   - Now at (5,4) facing East.
12. From (5,4), the agent needs to go to (5,5) which is in front.
   - Action"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n5eVaa_EMv7MkdUP7NXHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oJeVaZP-Hq7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=352
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=352 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='opeVafSEH6zd7M8PqdSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

