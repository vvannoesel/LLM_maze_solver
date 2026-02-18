# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_33.jpg` | **0.00%** | `input: 551 , ouput: 19` | `forward, right, forward, right, forward, left, forward, forward, left, forward` |
| `maze_line_3x3_33.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_33.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_33.txt` | **0.00%** | `input: 468 , ouput: 15` | `right, forward, right, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_33.txt` | **0.00%** | `input: 439 , ouput: 23` | `right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_33.jpg` | **0.00%** | `input: 546 , ouput: 650` | `the, start, is, at, (1, 1), and, the, end, is, at, (5, 5)., the, agent, starts, facing, south., 1., **forward:**, the, agent, moves, to, (2, 1)., 2., **left:**, the, agent, turns, west, and, moves, to, (2, 0)., this, hits, a, wall, so, this, is, not, the, right, path., let's, backtrack., let's, re-examine, the, maze., start:, (1, 1), facing, south., end:, (5, 5), from, (1, 1), facing, south:, -, forward, moves, to, (2, 1)., -, from, (2, 1), facing, south, turning, left, is, east., -, from, (2, 1), facing, south, turning, right, is, west., let's, try, a, different, approach., we, need, to, reach, (5, 5)., start, at, (1, 1), facing, south., 1., **forward**:, move, to, (2, 1)., facing, south., 2., **right**:, turn, west., move, to, (2, 0)., wall., backtrack., let's, try, again:, start, at, (1, 1), facing, south., 1., **forward**:, move, to, (2, 1)., facing, south., 2., **left**:, turn, east., move, to, (2, 2)., facing, east., 3., **forward**:, move, to, (2, 3)., facing, east., 4., **forward**:, move, to, (2, 4)., facing, east., 5., **right**:, turn, south., move, to, (3, 4)., facing, south., 6., **forward**:, move, to, (4, 4)., facing, south., 7., **forward**:, move, to, (5, 4)., facing, south., 8., **right**:, turn, west., move, to, (5, 3)., facing, west., 9., **right**:, turn, north., move, to, (4, 3)., facing, north., 10., **right**:, turn, east., move, to, (4, 4)., facing, east., 11., **forward**:, move, to, (4, 5)., facing, east., 12., **forward**:, move, to, (5, 5)., facing, east., this, is, the, end., let's, retrace, and, confirm, the, path., start:, (1, 1), facing, south., 1., forward, ->, (2, 1), facing, south., 2., left, ->, turn, east, move, to, (2, 2), facing, east., 3., forward, ->, (2, 3), facing, east., 4., forward, ->, (2, 4), facing, east., 5., right, ->, turn, south, move, to, (3, 4), facing, south., 6., forward, ->, (4, 4), facing, south., 7., forward, ->, (5, 4), facing, south., 8., right, ->, turn, west, move, to, (5, 3), facing, west., (this, is, not, going, towards, the, star)., let's, rethink., start:, (1, 1), facing, south., path, to, (5, 5)., from, (1, 1), facing, south., 1., **forward**:, (` |
| `maze_occupancy_3x3_33.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right` |
| `maze_occupancy_3x3_adj_33.json` | **0.00%** | `input: 1292 , ouput: 71` | `right, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_adj_33.txt` | **0.00%** | `input: 580 , ouput: 29` | `right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_ascii_33.txt` | **0.00%** | `input: 317 , ouput: 41` | `right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_33.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward` |

---

## Full LLM Responses

### `maze_line_3x3_33.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, right, forward, left, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,right,forward,left,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='npmVadO2J4qjkdUPl43u2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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
  total_token_count=570
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
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=570 traffic_type=None
```

### `maze_line_3x3_33.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n5mVadG3COTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=787
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=787 traffic_type=None
```

### `maze_line_3x3_adj_33.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n5mVacSwIrnjnsEPxoKX6AU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
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
        text='Right, forward, right, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oJmVaeu-Bqzd7M8PqdSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=483
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=483 traffic_type=None
```

### `maze_line_3x3_tokenized_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oJmVaa33JNqgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=462
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=462 traffic_type=None
```

### `maze_occupancy_3x3_33.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
the, start, is, at, (1, 1), and, the, end, is, at, (5, 5)., the, agent, starts, facing, south., 1., **forward:**, the, agent, moves, to, (2, 1)., 2., **left:**, the, agent, turns, west, and, moves, to, (2, 0)., this, hits, a, wall, so, this, is, not, the, right, path., let's, backtrack., let's, re-examine, the, maze., start:, (1, 1), facing, south., end:, (5, 5), from, (1, 1), facing, south:, -, forward, moves, to, (2, 1)., -, from, (2, 1), facing, south, turning, left, is, east., -, from, (2, 1), facing, south, turning, right, is, west., let's, try, a, different, approach., we, need, to, reach, (5, 5)., start, at, (1, 1), facing, south., 1., **forward**:, move, to, (2, 1)., facing, south., 2., **right**:, turn, west., move, to, (2, 0)., wall., backtrack., let's, try, again:, start, at, (1, 1), facing, south., 1., **forward**:, move, to, (2, 1)., facing, south., 2., **left**:, turn, east., move, to, (2, 2)., facing, east., 3., **forward**:, move, to, (2, 3)., facing, east., 4., **forward**:, move, to, (2, 4)., facing, east., 5., **right**:, turn, south., move, to, (3, 4)., facing, south., 6., **forward**:, move, to, (4, 4)., facing, south., 7., **forward**:, move, to, (5, 4)., facing, south., 8., **right**:, turn, west., move, to, (5, 3)., facing, west., 9., **right**:, turn, north., move, to, (4, 3)., facing, north., 10., **right**:, turn, east., move, to, (4, 4)., facing, east., 11., **forward**:, move, to, (4, 5)., facing, east., 12., **forward**:, move, to, (5, 5)., facing, east., this, is, the, end., let's, retrace, and, confirm, the, path., start:, (1, 1), facing, south., 1., forward, ->, (2, 1), facing, south., 2., left, ->, turn, east, move, to, (2, 2), facing, east., 3., forward, ->, (2, 3), facing, east., 4., forward, ->, (2, 4), facing, east., 5., right, ->, turn, south, move, to, (3, 4), facing, south., 6., forward, ->, (4, 4), facing, south., 7., forward, ->, (5, 4), facing, south., 8., right, ->, turn, west, move, to, (5, 3), facing, west., (this, is, not, going, towards, the, star)., let's, rethink., start:, (1, 1), facing, south., path, to, (5, 5)., from, (1, 1), facing, south., 1., **forward**:, (
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The start is at (1,1) and the end is at (5,5). The agent starts facing South.

1.  **Forward:** The agent moves to (2,1).
2.  **Left:** The agent turns West and moves to (2,0). This hits a wall, so this is not the right path. Let's backtrack.

Let's re-examine the maze.
Start: (1,1), facing South.
End: (5,5)

From (1,1) facing South:
- Forward moves to (2,1).
- From (2,1), facing South, turning Left is East.
- From (2,1) facing South, turning Right is West.

Let's try a different approach. We need to reach (5,5).

Start at (1,1) facing South.
1. **Forward**: Move to (2,1). Facing South.
2. **Right**: Turn West. Move to (2,0). Wall. Backtrack.

Let's try again:
Start at (1,1) facing South.
1. **Forward**: Move to (2,1). Facing South.
2. **Left**: Turn East. Move to (2,2). Facing East.
3. **Forward**: Move to (2,3). Facing East.
4. **Forward**: Move to (2,4). Facing East.
5. **Right**: Turn South. Move to (3,4). Facing South.
6. **Forward**: Move to (4,4). Facing South.
7. **Forward**: Move to (5,4). Facing South.
8. **Right**: Turn West. Move to (5,3). Facing West.
9. **Right**: Turn North. Move to (4,3). Facing North.
10. **Right**: Turn East. Move to (4,4). Facing East.
11. **Forward**: Move to (4,5). Facing East.
12. **Forward**: Move to (5,5). Facing East. This is the end.

Let's retrace and confirm the path.
Start: (1,1) facing South.
1. Forward -> (2,1) facing South.
2. Left -> turn East, move to (2,2) facing East.
3. Forward -> (2,3) facing East.
4. Forward -> (2,4) facing East.
5. Right -> turn South, move to (3,4) facing South.
6. Forward -> (4,4) facing South.
7. Forward -> (5,4) facing South.
8. Right -> turn West, move to (5,3) facing West. (This is not going towards the star).

Let's rethink.
Start: (1,1) facing South.
Path to (5,5).

From (1,1) facing South.
1. **Forward**: ("""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='opmVafOgJYqjkdUP8qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1196
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1196 traffic_type=None
```

### `maze_occupancy_3x3_33.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pJmVadiQCK2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_33.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, Right, forward, forward, Right, forward, forward, forward, Right, forward, forward, Right, forward, forward, forward, Right, forward, forward, forward, Right, forward, forward, forward, Right, forward, forward, forward, Right, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pJmVabS5LOjpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=71,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1363
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=71 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1363 traffic_type=None
```

### `maze_occupancy_3x3_adj_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pZmVaf_tF9WbkdUPuuCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=609
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=609 traffic_type=None
```

### `maze_occupancy_3x3_ascii_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ppmVaZJFw8-ewQ-l-prIBw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=358
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=358 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='p5mVafX-KryK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

