# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_24.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_24.json` | **0.00%** | `input: 774 , ouput: 17` | `right, forward, right, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_24.json` | **0.00%** | `input: 836 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_24.txt` | **0.00%** | `input: 468 , ouput: 27` | `right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward` |
| `maze_line_3x3_tokenized_24.txt` | **0.00%** | `input: 439 , ouput: 650` | `the, maze, is, as, follows:, (0, 0), origin, walls:, up, right, left, (0, 1), walls:, up, left, (0, 2), walls:, up, right, (1, 0), walls:, right, left, (1, 1), walls:, right, left, (1, 2), walls:, right, left, (2, 0), walls:, down, left, (2, 1), walls:, down, right, (2, 2), target, walls:, down, right, left, let's, trace, the, path., the, agent, starts, at, (0, 0), facing, south., 1., the, agent, is, at, (0, 0), facing, south., it, cannot, move, forward, due, to, walls., it, needs, to, move, to, (1, 0)., to, do, this, it, must, turn, right, twice, to, face, east, then, move, forward., then, turn, right, to, face, south., -, turn, right, (facing, east), -, forward, (at, (0, 1)), -, turn, right, (facing, south), -, forward, (at, (1, 1)), -, turn, right, (facing, west), -, forward, (at, (1, 0)), 2., the, agent, is, at, (1, 0), facing, west., it, needs, to, reach, (2, 2), (target)., -, from, (1, 0), facing, west, it, cannot, move, forward., it, needs, to, go, down., -, turn, right, (facing, north), -, turn, right, (facing, east), -, forward, (at, (1, 1)), -, turn, right, (facing, south), -, forward, (at, (2, 1)), -, turn, right, (facing, west), -, forward, (at, (2, 0)), 3., this, path, seems, wrong., let's, restart, with, a, clearer, strategy., the, agent, is, at, (0, 0), facing, south., *, **current, position:**, (0, 0), **facing:**, south, *, from, (0, 0), there, are, walls, to, the, right, and, left., the, only, way, to, move, is, down., *, **action:**, `forward`, (moves, to, (1, 0)), *, **current, position:**, (1, 0), **facing:**, south, *, at, (1, 0), there, are, walls, to, the, right, and, left., the, only, way, to, move, is, down., *, **action:**, `forward`, (moves, to, (2, 0)), *, **current, position:**, (2, 0), **facing:**, south, *, at, (2, 0), there, are, walls, to, the, down, and, left., the, only, way, to, move, is, right., to, face, right, the, agent, needs, to, turn, left, twice., *, **action:**, `left`, (facing, east), *, **action:**, `left`, (facing, north), *, **action:**, `forward`, (moves, to, (1, 0))., this, is, not, progress., let's, rethink., the, agent, starts, at, (0, 0), facing, south., 1., **at, (0, 0), facing, south` |
| `maze_occupancy_3x3_24.jpg` | **0.00%** | `input: 546 , ouput: 31` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_24.json` | **0.00%** | `input: 589 , ouput: 121` | `right, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_24.json` | **0.00%** | `input: 1292 , ouput: 650` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left` |
| `maze_occupancy_3x3_adj_24.txt` | **0.00%** | `input: 580 , ouput: 650` | `the, agent, starts, at, (1, 1), and, is, facing, south., the, target, is, at, (5, 5)., here's, a, step-by-step, breakdown, to, reach, the, target:, 1., **start, at, (1, 1), facing, south.**, 2., move, forward, to, (2, 1)., 3., move, forward, to, (3, 1)., 4., move, forward, to, (4, 1)., 5., move, forward, to, (5, 1)., 6., turn, right, to, face, west., 7., move, forward, to, (5, 2)., 8., move, forward, to, (5, 3)., 9., turn, right, to, face, north., 10., move, forward, to, (4, 3)., 11., turn, left, to, face, west., 12., move, forward, to, (4, 1)., (this, is, a, backtrack, but, necessary, to, get, to, the, correct, path), 13., turn, right, to, face, north., 14., move, forward, to, (3, 1)., 15., turn, right, to, face, east., 16., move, forward, to, (3, 3)., 17., turn, right, to, face, south., 18., move, forward, to, (4, 3)., 19., turn, right, to, face, west., 20., move, forward, to, (4, 1)., (another, backtrack), 21., turn, right, to, face, north., 22., move, forward, to, (3, 1)., 23., turn, right, to, face, east., 24., move, forward, to, (3, 3)., 25., turn, right, to, face, south., 26., move, forward, to, (4, 3)., 27., turn, right, to, face, west., 28., move, forward, to, (4, 1)., (this, seems, to, be, a, cycle, let's, re-evaluate, the, path.), let's, try, a, different, approach, focusing, on, the, structure, of, the, maze., **revised, plan:**, start, at, (1, 1), facing, south., 1., **forward**, (to, 2, 1), 2., **forward**, (to, 3, 1), 3., **forward**, (to, 4, 1), 4., **forward**, (to, 5, 1), 5., **right**, (now, facing, west), 6., **forward**, (to, 5, 2), 7., **forward**, (to, 5, 3), 8., **left**, (now, facing, south), -, this, is, a, mistake, agent, is, at, (5, 3), facing, south., 9., let's, restart, from, (5, 3), facing, south., the, connections, are:, (5, 1), <->, (5, 2), <->, (5, 3), and, (4, 3), <->, (5, 3)., the, target, is, (5, 5)., from, (5, 3), facing, south:, *, move, forward, to, (5, 3), is, not, possible., let's, try, again, from, the, beginning, with, a` |
| `maze_occupancy_3x3_ascii_24.txt` | **0.00%** | `input: 320 , ouput: 47` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_24.txt` | **0.00%** | `input: 867 , ouput: 221` | `the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., here's, a, possible, path:, 1., **forward**:, move, to, (2, 1), 2., **right**:, turn, to, face, west., 3., **forward**:, move, to, (2, 2), 4., **left**:, turn, to, face, south., 5., **forward**:, move, to, (3, 2), 6., **forward**:, move, to, (4, 2), 7., **forward**:, move, to, (5, 2), 8., **right**:, turn, to, face, west., 9., **forward**:, move, to, (5, 3), 10., **right**:, turn, to, face, north., 11., **left**:, turn, to, face, west., 12., **forward**:, move, to, (5, 4), 13., **forward**:, move, to, (5, 5), (target), forward, right, forward, left, forward, forward, forward, right, forward, right, left, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_24.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vpeVaZ6pBMPe7M8PidibyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
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
  total_token_count=566
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=566 traffic_type=None
```

### `maze_line_3x3_24.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vpeVaZTEIqzu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_24.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v5eVabmxCv7MkdUPkdfHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=849
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=849 traffic_type=None
```

### `maze_line_3x3_adj_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v5eVae-EKOeGkdUPsqK74AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=495
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=495 traffic_type=None
```

### `maze_line_3x3_tokenized_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
the, maze, is, as, follows:, (0, 0), origin, walls:, up, right, left, (0, 1), walls:, up, left, (0, 2), walls:, up, right, (1, 0), walls:, right, left, (1, 1), walls:, right, left, (1, 2), walls:, right, left, (2, 0), walls:, down, left, (2, 1), walls:, down, right, (2, 2), target, walls:, down, right, left, let's, trace, the, path., the, agent, starts, at, (0, 0), facing, south., 1., the, agent, is, at, (0, 0), facing, south., it, cannot, move, forward, due, to, walls., it, needs, to, move, to, (1, 0)., to, do, this, it, must, turn, right, twice, to, face, east, then, move, forward., then, turn, right, to, face, south., -, turn, right, (facing, east), -, forward, (at, (0, 1)), -, turn, right, (facing, south), -, forward, (at, (1, 1)), -, turn, right, (facing, west), -, forward, (at, (1, 0)), 2., the, agent, is, at, (1, 0), facing, west., it, needs, to, reach, (2, 2), (target)., -, from, (1, 0), facing, west, it, cannot, move, forward., it, needs, to, go, down., -, turn, right, (facing, north), -, turn, right, (facing, east), -, forward, (at, (1, 1)), -, turn, right, (facing, south), -, forward, (at, (2, 1)), -, turn, right, (facing, west), -, forward, (at, (2, 0)), 3., this, path, seems, wrong., let's, restart, with, a, clearer, strategy., the, agent, is, at, (0, 0), facing, south., *, **current, position:**, (0, 0), **facing:**, south, *, from, (0, 0), there, are, walls, to, the, right, and, left., the, only, way, to, move, is, down., *, **action:**, `forward`, (moves, to, (1, 0)), *, **current, position:**, (1, 0), **facing:**, south, *, at, (1, 0), there, are, walls, to, the, right, and, left., the, only, way, to, move, is, down., *, **action:**, `forward`, (moves, to, (2, 0)), *, **current, position:**, (2, 0), **facing:**, south, *, at, (2, 0), there, are, walls, to, the, down, and, left., the, only, way, to, move, is, right., to, face, right, the, agent, needs, to, turn, left, twice., *, **action:**, `left`, (facing, east), *, **action:**, `left`, (facing, north), *, **action:**, `forward`, (moves, to, (1, 0))., this, is, not, progress., let's, rethink., the, agent, starts, at, (0, 0), facing, south., 1., **at, (0, 0), facing, south
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is as follows:

(0,0) Origin, walls: up, right, left
(0,1) Walls: up, left
(0,2) Walls: up, right

(1,0) Walls: right, left
(1,1) Walls: right, left
(1,2) Walls: right, left

(2,0) Walls: down, left
(2,1) Walls: down, right
(2,2) Target, walls: down, right, left

Let's trace the path. The agent starts at (0,0) facing South.

1. The agent is at (0,0) facing South. It cannot move forward due to walls. It needs to move to (1,0). To do this, it must turn right twice to face East, then move forward. Then turn right to face South.
   - Turn Right (facing East)
   - Forward (at (0,1))
   - Turn Right (facing South)
   - Forward (at (1,1))
   - Turn Right (facing West)
   - Forward (at (1,0))

2. The agent is at (1,0) facing West. It needs to reach (2,2) (Target).
   - From (1,0) facing West, it cannot move forward. It needs to go down.
   - Turn Right (facing North)
   - Turn Right (facing East)
   - Forward (at (1,1))
   - Turn Right (facing South)
   - Forward (at (2,1))
   - Turn Right (facing West)
   - Forward (at (2,0))

3. This path seems wrong. Let's restart with a clearer strategy.

The agent is at (0,0) facing South.

*   **Current position:** (0,0), **Facing:** South
*   From (0,0), there are walls to the right and left. The only way to move is down.
*   **Action:** `forward` (moves to (1,0))
*   **Current position:** (1,0), **Facing:** South

*   At (1,0), there are walls to the right and left. The only way to move is down.
*   **Action:** `forward` (moves to (2,0))
*   **Current position:** (2,0), **Facing:** South

*   At (2,0), there are walls to the down and left. The only way to move is right. To face right, the agent needs to turn left twice.
*   **Action:** `left` (facing East)
*   **Action:** `left` (facing North)
*   **Action:** `forward` (moves to (1,0)). This is not progress.

Let's rethink. The agent starts at (0,0) facing South.

1.  **At (0,0), facing South"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wZeVaY7nGLW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_24.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w5eVabnsEYTensEP6bbt4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
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
  total_token_count=577
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=577 traffic_type=None
```

### `maze_occupancy_3x3_24.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xJeVaYi1EtqfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=121,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=710
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=121 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=710 traffic_type=None
```

### `maze_occupancy_3x3_adj_24.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xpeVac-7G5Pe7M8PjqaxkQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1942
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1942 traffic_type=None
```

### `maze_occupancy_3x3_adj_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (1, 1), and, is, facing, south., the, target, is, at, (5, 5)., here's, a, step-by-step, breakdown, to, reach, the, target:, 1., **start, at, (1, 1), facing, south.**, 2., move, forward, to, (2, 1)., 3., move, forward, to, (3, 1)., 4., move, forward, to, (4, 1)., 5., move, forward, to, (5, 1)., 6., turn, right, to, face, west., 7., move, forward, to, (5, 2)., 8., move, forward, to, (5, 3)., 9., turn, right, to, face, north., 10., move, forward, to, (4, 3)., 11., turn, left, to, face, west., 12., move, forward, to, (4, 1)., (this, is, a, backtrack, but, necessary, to, get, to, the, correct, path), 13., turn, right, to, face, north., 14., move, forward, to, (3, 1)., 15., turn, right, to, face, east., 16., move, forward, to, (3, 3)., 17., turn, right, to, face, south., 18., move, forward, to, (4, 3)., 19., turn, right, to, face, west., 20., move, forward, to, (4, 1)., (another, backtrack), 21., turn, right, to, face, north., 22., move, forward, to, (3, 1)., 23., turn, right, to, face, east., 24., move, forward, to, (3, 3)., 25., turn, right, to, face, south., 26., move, forward, to, (4, 3)., 27., turn, right, to, face, west., 28., move, forward, to, (4, 1)., (this, seems, to, be, a, cycle, let's, re-evaluate, the, path.), let's, try, a, different, approach, focusing, on, the, structure, of, the, maze., **revised, plan:**, start, at, (1, 1), facing, south., 1., **forward**, (to, 2, 1), 2., **forward**, (to, 3, 1), 3., **forward**, (to, 4, 1), 4., **forward**, (to, 5, 1), 5., **right**, (now, facing, west), 6., **forward**, (to, 5, 2), 7., **forward**, (to, 5, 3), 8., **left**, (now, facing, south), -, this, is, a, mistake, agent, is, at, (5, 3), facing, south., 9., let's, restart, from, (5, 3), facing, south., the, connections, are:, (5, 1), <->, (5, 2), <->, (5, 3), and, (4, 3), <->, (5, 3)., the, target, is, (5, 5)., from, (5, 3), facing, south:, *, move, forward, to, (5, 3), is, not, possible., let's, try, again, from, the, beginning, with, a
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (1,1) and is facing South. The target is at (5,5).

Here's a step-by-step breakdown to reach the target:

1.  **Start at (1,1) facing South.**
2.  Move Forward to (2,1).
3.  Move Forward to (3,1).
4.  Move Forward to (4,1).
5.  Move Forward to (5,1).
6.  Turn Right to face West.
7.  Move Forward to (5,2).
8.  Move Forward to (5,3).
9.  Turn Right to face North.
10. Move Forward to (4,3).
11. Turn Left to face West.
12. Move Forward to (4,1). (This is a backtrack, but necessary to get to the correct path)
13. Turn Right to face North.
14. Move Forward to (3,1).
15. Turn Right to face East.
16. Move Forward to (3,3).
17. Turn Right to face South.
18. Move Forward to (4,3).
19. Turn Right to face West.
20. Move Forward to (4,1). (Another backtrack)
21. Turn Right to face North.
22. Move Forward to (3,1).
23. Turn Right to face East.
24. Move Forward to (3,3).
25. Turn Right to face South.
26. Move Forward to (4,3).
27. Turn Right to face West.
28. Move Forward to (4,1). (This seems to be a cycle, let's re-evaluate the path.)

Let's try a different approach focusing on the structure of the maze.

**Revised Plan:**

Start at (1,1) facing South.

1.  **forward** (to 2,1)
2.  **forward** (to 3,1)
3.  **forward** (to 4,1)
4.  **forward** (to 5,1)
5.  **right** (now facing West)
6.  **forward** (to 5,2)
7.  **forward** (to 5,3)
8.  **left** (now facing South) - This is a mistake, agent is at (5,3) facing South.
9.  Let's restart from (5,3) facing South.
    The connections are: (5,1) <-> (5,2) <-> (5,3) and (4,3) <-> (5,3). The target is (5,5).

    From (5,3) facing South:
    *   Move Forward to (5,3) is not possible.

Let's try again from the beginning with a"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yJeVacLcFNqfnsEPzfyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yJeVafD7OqeN7M8P6NXVwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=320,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=320
    ),
  ],
  total_token_count=367
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=320 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=320
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=367 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., here's, a, possible, path:, 1., **forward**:, move, to, (2, 1), 2., **right**:, turn, to, face, west., 3., **forward**:, move, to, (2, 2), 4., **left**:, turn, to, face, south., 5., **forward**:, move, to, (3, 2), 6., **forward**:, move, to, (4, 2), 7., **forward**:, move, to, (5, 2), 8., **right**:, turn, to, face, west., 9., **forward**:, move, to, (5, 3), 10., **right**:, turn, to, face, north., 11., **left**:, turn, to, face, west., 12., **forward**:, move, to, (5, 4), 13., **forward**:, move, to, (5, 5), (target), forward, right, forward, left, forward, forward, forward, right, forward, right, left, forward, forward
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

1. **Forward**: Move to (2,1)
2. **Right**: Turn to face West.
3. **Forward**: Move to (2,2)
4. **Left**: Turn to face South.
5. **Forward**: Move to (3,2)
6. **Forward**: Move to (4,2)
7. **Forward**: Move to (5,2)
8. **Right**: Turn to face West.
9. **Forward**: Move to (5,3)
10. **Right**: Turn to face North.
11. **Left**: Turn to face West.
12. **Forward**: Move to (5,4)
13. **Forward**: Move to (5,5) (Target)

forward,right,forward,left,forward,forward,forward,right,forward,right,left,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ypeVadHUAYyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=221,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1088
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=221 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1088 traffic_type=None
```

