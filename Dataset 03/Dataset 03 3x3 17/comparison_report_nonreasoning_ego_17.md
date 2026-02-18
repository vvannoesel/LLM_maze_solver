# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_17.jpg` | **0.00%** | `input: 551 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_17.json` | **0.00%** | `input: 774 , ouput: 650` | `the, agent, starts, at, (0, 0), facing, south., the, maze, is:, (0, 0), -, north:, wall, east:, wall, south:, pass, west:, wall, (0, 1), -, north:, wall, east:, pass, south:, pass, west:, wall, (0, 2), -, north:, wall, east:, wall, south:, pass, west:, pass, (1, 0), -, north:, pass, east:, wall, south:, pass, west:, wall, (1, 1), -, north:, pass, east:, wall, south:, pass, west:, wall, (1, 2), -, north:, pass, east:, wall, south:, pass, west:, wall, (2, 0), -, north:, pass, east:, pass, south:, wall, west:, wall, (2, 1), -, north:, pass, east:, wall, south:, wall, west:, pass, (2, 2), -, north:, pass, east:, wall, south:, wall, west:, wall, the, target, is, (2, 2)., let's, trace, the, path:, start, at, (0, 0), facing, south., 1., **forward**:, agent, moves, to, (1, 0)., facing, south., 2., **forward**:, agent, moves, to, (2, 0)., facing, south., 3., **right**:, agent, turns, west, then, moves, to, (2, 1)., facing, west., 4., **forward**:, agent, moves, to, (2, 0), which, is, incorrect., let's, rethink, the, approach., start, at, (0, 0), facing, south., 1., **forward**:, agent, moves, to, (1, 0)., facing, south., 2., **forward**:, agent, moves, to, (2, 0)., facing, south., 3., **right**:, agent, turns, west., the, agent, cannot, move, west, from, (2, 0), as, there, is, a, wall., this, indicates, a, mistake, in, my, manual, trace, or, understanding, of, the, problem., let's, re-examine, the, maze, and, movement, from, (2, 0):, from, (2, 0):, walls:, n:, false, e:, false, s:, true, w:, true., if, facing, south, attempting, to, move, forward, hits, s:, true, wall., if, facing, west, attempting, to, move, forward, hits, w:, true, wall., if, facing, east, attempting, to, move, forward, hits, e:, false., let's, restart, the, trace, from, (0, 0), facing, south., 1., **forward**:, moves, to, (1, 0)., facing, south., *, (0, 0), n:t, e:t, s:f, w:t, *, (1, 0), n:f, e:t, s:f, w:t, *, agent, is, at, (1, 0), facing, south., 2., **forward**:, moves, to, (2, 0)., facing, south., *, (2, 0), n:f, e:f, s:t, w:t, *, agent, is, at, (2` |
| `maze_line_3x3_adj_17.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_17.txt` | **0.00%** | `input: 468 , ouput: 23` | `right, forward, right, forward, right, forward, left, forward, left, forward, left, forward` |
| `maze_line_3x3_tokenized_17.txt` | **0.00%** | `input: 439 , ouput: 21` | `right, forward, right, forward, backward, left, forward, left, forward, right, forward` |
| `maze_occupancy_3x3_17.jpg` | **12.50%** | `input: 546 , ouput: 31` | `forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_17.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, forward, backward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right` |
| `maze_occupancy_3x3_adj_17.json` | **0.00%** | `input: 1292 , ouput: 650` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_adj_17.txt` | **0.00%** | `input: 580 , ouput: 49` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_17.txt` | **0.00%** | `input: 320 , ouput: 650` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left` |
| `maze_occupancy_3x3_tokenized_17.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward` |

---

## Full LLM Responses

### `maze_line_3x3_17.jpg`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='S5eVaYuWC5nqkdUP3rjkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_17.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), facing, south., the, maze, is:, (0, 0), -, north:, wall, east:, wall, south:, pass, west:, wall, (0, 1), -, north:, wall, east:, pass, south:, pass, west:, wall, (0, 2), -, north:, wall, east:, wall, south:, pass, west:, pass, (1, 0), -, north:, pass, east:, wall, south:, pass, west:, wall, (1, 1), -, north:, pass, east:, wall, south:, pass, west:, wall, (1, 2), -, north:, pass, east:, wall, south:, pass, west:, wall, (2, 0), -, north:, pass, east:, pass, south:, wall, west:, wall, (2, 1), -, north:, pass, east:, wall, south:, wall, west:, pass, (2, 2), -, north:, pass, east:, wall, south:, wall, west:, wall, the, target, is, (2, 2)., let's, trace, the, path:, start, at, (0, 0), facing, south., 1., **forward**:, agent, moves, to, (1, 0)., facing, south., 2., **forward**:, agent, moves, to, (2, 0)., facing, south., 3., **right**:, agent, turns, west, then, moves, to, (2, 1)., facing, west., 4., **forward**:, agent, moves, to, (2, 0), which, is, incorrect., let's, rethink, the, approach., start, at, (0, 0), facing, south., 1., **forward**:, agent, moves, to, (1, 0)., facing, south., 2., **forward**:, agent, moves, to, (2, 0)., facing, south., 3., **right**:, agent, turns, west., the, agent, cannot, move, west, from, (2, 0), as, there, is, a, wall., this, indicates, a, mistake, in, my, manual, trace, or, understanding, of, the, problem., let's, re-examine, the, maze, and, movement, from, (2, 0):, from, (2, 0):, walls:, n:, false, e:, false, s:, true, w:, true., if, facing, south, attempting, to, move, forward, hits, s:, true, wall., if, facing, west, attempting, to, move, forward, hits, w:, true, wall., if, facing, east, attempting, to, move, forward, hits, e:, false., let's, restart, the, trace, from, (0, 0), facing, south., 1., **forward**:, moves, to, (1, 0)., facing, south., *, (0, 0), n:t, e:t, s:f, w:t, *, (1, 0), n:f, e:t, s:f, w:t, *, agent, is, at, (1, 0), facing, south., 2., **forward**:, moves, to, (2, 0)., facing, south., *, (2, 0), n:f, e:f, s:t, w:t, *, agent, is, at, (2
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (0,0) facing South.

The maze is:
(0,0) - North: Wall, East: Wall, South: Pass, West: Wall
(0,1) - North: Wall, East: Pass, South: Pass, West: Wall
(0,2) - North: Wall, East: Wall, South: Pass, West: Pass

(1,0) - North: Pass, East: Wall, South: Pass, West: Wall
(1,1) - North: Pass, East: Wall, South: Pass, West: Wall
(1,2) - North: Pass, East: Wall, South: Pass, West: Wall

(2,0) - North: Pass, East: Pass, South: Wall, West: Wall
(2,1) - North: Pass, East: Wall, South: Wall, West: Pass
(2,2) - North: Pass, East: Wall, South: Wall, West: Wall

The target is (2,2).

Let's trace the path:
Start at (0,0) facing South.

1.  **Forward**: Agent moves to (1,0). Facing South.
2.  **Forward**: Agent moves to (2,0). Facing South.
3.  **Right**: Agent turns West, then moves to (2,1). Facing West.
4.  **Forward**: Agent moves to (2,0) which is incorrect.

Let's rethink the approach.

Start at (0,0) facing South.

1.  **Forward**: Agent moves to (1,0). Facing South.
2.  **Forward**: Agent moves to (2,0). Facing South.
3.  **Right**: Agent turns West. The agent cannot move West from (2,0) as there is a wall. This indicates a mistake in my manual trace or understanding of the problem.

Let's re-examine the maze and movement from (2,0):
From (2,0):
Walls: N: False, E: False, S: True, W: True.
If facing South, attempting to move Forward hits S: True wall.
If facing West, attempting to move Forward hits W: True wall.
If facing East, attempting to move Forward hits E: False.

Let's restart the trace from (0,0) facing South.

1.  **Forward**: Moves to (1,0). Facing South.
    *   (0,0) N:T, E:T, S:F, W:T
    *   (1,0) N:F, E:T, S:F, W:T
    *   Agent is at (1,0) facing South.

2.  **Forward**: Moves to (2,0). Facing South.
    *   (2,0) N:F, E:F, S:T, W:T
    *   Agent is at (2"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TZeVaYSzIO3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=1424
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1424 traffic_type=None
```

### `maze_line_3x3_adj_17.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TpeVaYftFKrw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=851
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=851 traffic_type=None
```

### `maze_line_3x3_adj_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
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
        text='right, forward, right, forward, right, forward, left, forward, left, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TpeVaZjkOI-VkdUPpZbhqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, backward, left, forward, left, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Backward, Left, Forward, Left, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T5eVacPHG-KAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=460
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=460 traffic_type=None
```

### `maze_occupancy_3x3_17.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UJeVabewHqL17M8Pt6zc8AU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_17.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, backward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,forward,backward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UpeVaf2LG4KG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_17.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,left,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VJeVaczcCtqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VJeVaaWgNKG-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=629
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=629 traffic_type=None
```

### `maze_occupancy_3x3_ascii_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VpeVadn9OeKAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=320,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=320
    ),
  ],
  total_token_count=970
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=320 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=320
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=970 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WZeVadWTApzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

