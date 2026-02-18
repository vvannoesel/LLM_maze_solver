# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_23.jpg` | **0.00%** | `input: 551 , ouput: 535` | `the, agent, starts, at, (0, 0), and, is, facing, south., the, star, is, at, (2, 2)., the, path, is:, the, agent, is, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0), still, facing, south), 2., right, (turns, to, face, west), 3., forward, (moves, to, (1, -1), but, this, is, outside, the, maze., let's, restart, and, re-evaluate.), let's, assume, the, agent, is, inside, the, cell, and, not, on, the, border., the, start, is, the, top-left, cell, (0, 0)., the, star, is, the, bottom-right, cell, (2, 2)., the, agent, starts, facing, south., 1., forward, (moves, to, (1, 0), facing, south), 2., right, (turns, to, face, west)., there, is, a, wall, to, the, west., this, path, is, blocked., let's, try, turning, right, first., the, agent, is, at, (0, 0), facing, south., 1., right, (turns, to, face, west)., wall., blocked., let's, try, turning, left, first., the, agent, is, at, (0, 0), facing, south., 1., left, (turns, to, face, east)., 2., forward, (moves, to, (0, 1), facing, east), 3., forward, (moves, to, (0, 2), facing, east), 4., right, (turns, to, face, south), 5., forward, (moves, to, (1, 2), facing, south), 6., forward, (moves, to, (2, 2), facing, south)., goal, reached., so, the, sequence, of, actions, is:, left, forward, forward, right, forward, forward., let's, trace, this, path, on, the, maze:, start, at, (0, 0), facing, south., 1., left:, turn, 90, degrees, left., now, facing, east., 2., forward:, move, one, step, in, the, current, direction, (east)., agent, is, now, at, (0, 1), facing, east., 3., forward:, move, one, step, in, the, current, direction, (east)., agent, is, now, at, (0, 2), facing, east., 4., right:, turn, 90, degrees, right., now, facing, south., 5., forward:, move, one, step, in, the, current, direction, (south)., agent, is, now, at, (1, 2), facing, south., 6., forward:, move, one, step, in, the, current, direction, (south)., agent, is, now, at, (2, 2), facing, south., the, star, is, at, (2, 2)., this, path, is, valid., left, forward, forward, right, forward, forward` |
| `maze_line_3x3_23.json` | **25.00%** | `input: 774 , ouput: 15` | `forward, right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_23.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, forward, left, forward, left, forward` |
| `maze_line_3x3_adj_23.txt` | **0.00%** | `input: 468 , ouput: 23` | `right, forward, right, forward, right, forward, left, forward, left, forward, left, forward` |
| `maze_line_3x3_tokenized_23.txt` | **0.00%** | `input: 439 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_23.jpg` | **0.00%** | `input: 546 , ouput: 52` | `right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward.` |
| `maze_occupancy_3x3_23.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right` |
| `maze_occupancy_3x3_adj_23.json` | **0.00%** | `input: 1292 , ouput: 41` | `right, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_adj_23.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_ascii_23.txt` | **0.00%** | `input: 315 , ouput: 41` | `right, forward, forward, right, forward, forward, backward, forward, left, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_tokenized_23.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward` |

---

## Full LLM Responses

### `maze_line_3x3_23.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), and, is, facing, south., the, star, is, at, (2, 2)., the, path, is:, the, agent, is, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0), still, facing, south), 2., right, (turns, to, face, west), 3., forward, (moves, to, (1, -1), but, this, is, outside, the, maze., let's, restart, and, re-evaluate.), let's, assume, the, agent, is, inside, the, cell, and, not, on, the, border., the, start, is, the, top-left, cell, (0, 0)., the, star, is, the, bottom-right, cell, (2, 2)., the, agent, starts, facing, south., 1., forward, (moves, to, (1, 0), facing, south), 2., right, (turns, to, face, west)., there, is, a, wall, to, the, west., this, path, is, blocked., let's, try, turning, right, first., the, agent, is, at, (0, 0), facing, south., 1., right, (turns, to, face, west)., wall., blocked., let's, try, turning, left, first., the, agent, is, at, (0, 0), facing, south., 1., left, (turns, to, face, east)., 2., forward, (moves, to, (0, 1), facing, east), 3., forward, (moves, to, (0, 2), facing, east), 4., right, (turns, to, face, south), 5., forward, (moves, to, (1, 2), facing, south), 6., forward, (moves, to, (2, 2), facing, south)., goal, reached., so, the, sequence, of, actions, is:, left, forward, forward, right, forward, forward., let's, trace, this, path, on, the, maze:, start, at, (0, 0), facing, south., 1., left:, turn, 90, degrees, left., now, facing, east., 2., forward:, move, one, step, in, the, current, direction, (east)., agent, is, now, at, (0, 1), facing, east., 3., forward:, move, one, step, in, the, current, direction, (east)., agent, is, now, at, (0, 2), facing, east., 4., right:, turn, 90, degrees, right., now, facing, south., 5., forward:, move, one, step, in, the, current, direction, (south)., agent, is, now, at, (1, 2), facing, south., 6., forward:, move, one, step, in, the, current, direction, (south)., agent, is, now, at, (2, 2), facing, south., the, star, is, at, (2, 2)., this, path, is, valid., left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (0,0) and is facing south. The star is at (2,2).
The path is:
The agent is at (0,0) facing South.
1. Forward (moves to (1,0), still facing South)
2. Right (turns to face West)
3. Forward (moves to (1, -1), but this is outside the maze. Let's restart and re-evaluate.)

Let's assume the agent is inside the cell and not on the border.
The start is the top-left cell (0,0). The star is the bottom-right cell (2,2).
The agent starts facing South.

1. Forward (moves to (1,0), facing South)
2. Right (turns to face West). There is a wall to the West. This path is blocked.

Let's try turning right first.
The agent is at (0,0) facing South.
1. Right (turns to face West). Wall. Blocked.

Let's try turning left first.
The agent is at (0,0) facing South.
1. Left (turns to face East).
2. Forward (moves to (0,1), facing East)
3. Forward (moves to (0,2), facing East)
4. Right (turns to face South)
5. Forward (moves to (1,2), facing South)
6. Forward (moves to (2,2), facing South). Goal reached.

So the sequence of actions is: left, forward, forward, right, forward, forward.

Let's trace this path on the maze:
Start at (0,0) facing South.
1. Left: Turn 90 degrees left. Now facing East.
2. Forward: Move one step in the current direction (East). Agent is now at (0,1), facing East.
3. Forward: Move one step in the current direction (East). Agent is now at (0,2), facing East.
4. Right: Turn 90 degrees right. Now facing South.
5. Forward: Move one step in the current direction (South). Agent is now at (1,2), facing South.
6. Forward: Move one step in the current direction (South). Agent is now at (2,2), facing South. The star is at (2,2). This path is valid.

left,forward,forward,right,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='s5eVafwqzLKewQ_R3-6IBA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=535,
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
  total_token_count=1086
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=535 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1086 traffic_type=None
```

### `maze_line_3x3_23.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
forward, right, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='s5eVabbiJeTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_23.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tJeVacqwDOTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_23.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Left, Forward, Left, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tZeVaeuHAv_DnsEPhPSp6QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=491
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=491 traffic_type=None
```

### `maze_line_3x3_tokenized_23.txt`

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
        text='Right, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tZeVaf6jIvDm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=450
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=450 traffic_type=None
```

### `maze_occupancy_3x3_23.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward.'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tpeVad_zFNqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=52,
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
  total_token_count=598
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=52 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=598 traffic_type=None
```

### `maze_occupancy_3x3_23.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uJeVaZH_D5nqkdUP57jkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=1239
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1239 traffic_type=None
```

### `maze_occupancy_3x3_adj_23.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,right,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uJeVabG9LdqfnsEPxvyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1333
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1333 traffic_type=None
```

### `maze_occupancy_3x3_adj_23.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='upeVaZG4J5nqkdUP57jkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_23.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, backward, forward, left, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Backward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='u5eVacq5Dazu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=356
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=356 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_23.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vZeVabXwGvKcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

