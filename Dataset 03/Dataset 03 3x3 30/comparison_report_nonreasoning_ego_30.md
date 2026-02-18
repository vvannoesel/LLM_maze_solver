# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_30.jpg` | **0.00%** | `input: 551 , ouput: 530` | `the, agent, starts, at, (0, 0), facing, south., the, star, is, at, (2, 2)., from, (0, 0), facing, south, the, agent, needs, to, move, to, (1, 0)., then, turn, right, to, face, west, and, move, to, (1, 1)., then, turn, right, to, face, north, and, move, to, (0, 1)., then, turn, right, to, face, east, and, move, to, (0, 2)., then, turn, right, to, face, south, and, move, to, (1, 2)., then, turn, right, to, face, west, and, move, to, (2, 2)., let's, refine, this., start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0)), 2., right, (turns, to, face, west), 3., forward, (moves, to, (1, 1)), 4., right, (turns, to, face, north), 5., forward, (moves, to, (0, 1)), 6., right, (turns, to, face, east), 7., forward, (moves, to, (0, 2)), 8., right, (turns, to, face, south), 9., forward, (moves, to, (1, 2)), 10., right, (turns, to, face, west), 11., forward, (moves, to, (2, 2)), let's, check, the, wall., there, is, a, wall, between, (0, 0), and, (0, 1)., revised, plan:, start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0)), 2., right, (turns, to, face, west), 3., forward, (moves, to, (1, 1)), 4., right, (turns, to, face, north), 5., right, (turns, to, face, east), 6., forward, (moves, to, (1, 2)), 7., right, (turns, to, face, south), 8., forward, (moves, to, (2, 2)), let's, trace, this., start, (0, 0), facing, south., 1., forward, ->, (1, 0), facing, south., 2., right, ->, (1, 0), facing, west., 3., forward, ->, (1, 1), facing, west., 4., right, ->, (1, 1), facing, north., 5., right, ->, (1, 1), facing, east., 6., forward, ->, (1, 2), facing, east., 7., right, ->, (1, 2), facing, south., 8., forward, ->, (2, 2), facing, south., this, path, is, valid., forward, right, forward, right, right, forward, right, forward` |
| `maze_line_3x3_30.json` | **0.00%** | `input: 774 , ouput: 15` | `right, forward, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_30.json` | **0.00%** | `input: 836 , ouput: 23` | `right, forward, right, forward, right, forward, left, forward, left, forward, left, forward` |
| `maze_line_3x3_adj_30.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_30.txt` | **0.00%** | `input: 439 , ouput: 473` | `the, maze, is, as, follows:, (0, 0):, origin, walls:, up, right, left, (0, 1):, walls:, up, down, left, (0, 2):, walls:, up, right, (1, 0):, walls:, down, left, (1, 1):, walls:, up, down, (1, 2):, walls:, right, (2, 0):, walls:, up, down, left, (2, 1):, walls:, up, down, (2, 2):, target, walls:, down, right, let's, trace, the, path:, *, **start:**, (0, 0), facing, south., *, the, agent, is, at, (0, 0), and, facing, south., *, there, is, no, wall, to, the, south, from, (0, 0)., *, **action:**, forward., agent, moves, to, (1, 0)., facing, south., *, the, agent, is, at, (1, 0), and, facing, south., *, there, is, a, wall, to, the, south, at, (1, 0)., *, the, agent, needs, to, go, to, (1, 1)., from, (1, 0), facing, south, turning, left, will, face, east., *, **action:**, left., agent, turns, east., *, **action:**, forward., agent, moves, to, (1, 1)., facing, east., *, the, agent, is, at, (1, 1), and, facing, east., *, there, is, no, wall, to, the, east, from, (1, 1)., *, **action:**, forward., agent, moves, to, (1, 2)., facing, east., *, the, agent, is, at, (1, 2), and, facing, east., *, there, is, a, wall, to, the, east, at, (1, 2)., *, the, agent, needs, to, go, to, (2, 2)., from, (1, 2), facing, east, turning, left, will, face, north, turning, right, will, face, south., *, **action:**, right., agent, turns, south., *, **action:**, forward., agent, moves, to, (2, 2)., facing, south., *, the, agent, is, at, (2, 2), which, is, the, target., therefore, the, sequence, of, moves, is:, forward, left, forward, right, forward., forward, left, forward, right, forward` |
| `maze_occupancy_3x3_30.jpg` | **0.00%** | `input: 546 , ouput: 29` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_30.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_30.json` | **0.00%** | `input: 1292 , ouput: 29` | `right, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_30.txt` | **0.00%** | `input: 580 , ouput: 41` | `right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward` |
| `maze_occupancy_3x3_ascii_30.txt` | **0.00%** | `input: 315 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left` |
| `maze_occupancy_3x3_tokenized_30.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward` |

---

## Full LLM Responses

### `maze_line_3x3_30.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), facing, south., the, star, is, at, (2, 2)., from, (0, 0), facing, south, the, agent, needs, to, move, to, (1, 0)., then, turn, right, to, face, west, and, move, to, (1, 1)., then, turn, right, to, face, north, and, move, to, (0, 1)., then, turn, right, to, face, east, and, move, to, (0, 2)., then, turn, right, to, face, south, and, move, to, (1, 2)., then, turn, right, to, face, west, and, move, to, (2, 2)., let's, refine, this., start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0)), 2., right, (turns, to, face, west), 3., forward, (moves, to, (1, 1)), 4., right, (turns, to, face, north), 5., forward, (moves, to, (0, 1)), 6., right, (turns, to, face, east), 7., forward, (moves, to, (0, 2)), 8., right, (turns, to, face, south), 9., forward, (moves, to, (1, 2)), 10., right, (turns, to, face, west), 11., forward, (moves, to, (2, 2)), let's, check, the, wall., there, is, a, wall, between, (0, 0), and, (0, 1)., revised, plan:, start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0)), 2., right, (turns, to, face, west), 3., forward, (moves, to, (1, 1)), 4., right, (turns, to, face, north), 5., right, (turns, to, face, east), 6., forward, (moves, to, (1, 2)), 7., right, (turns, to, face, south), 8., forward, (moves, to, (2, 2)), let's, trace, this., start, (0, 0), facing, south., 1., forward, ->, (1, 0), facing, south., 2., right, ->, (1, 0), facing, west., 3., forward, ->, (1, 1), facing, west., 4., right, ->, (1, 1), facing, north., 5., right, ->, (1, 1), facing, east., 6., forward, ->, (1, 2), facing, east., 7., right, ->, (1, 2), facing, south., 8., forward, ->, (2, 2), facing, south., this, path, is, valid., forward, right, forward, right, right, forward, right, forward
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
The star is at (2,2).

From (0,0) facing South, the agent needs to move to (1,0).
Then turn right to face West and move to (1,1).
Then turn right to face North and move to (0,1).
Then turn right to face East and move to (0,2).
Then turn right to face South and move to (1,2).
Then turn right to face West and move to (2,2).

Let's refine this.

Start at (0,0) facing South.
1. Forward (moves to (1,0))
2. Right (turns to face West)
3. Forward (moves to (1,1))
4. Right (turns to face North)
5. Forward (moves to (0,1))
6. Right (turns to face East)
7. Forward (moves to (0,2))
8. Right (turns to face South)
9. Forward (moves to (1,2))
10. Right (turns to face West)
11. Forward (moves to (2,2))

Let's check the wall. There is a wall between (0,0) and (0,1).

Revised plan:
Start at (0,0) facing South.
1. Forward (moves to (1,0))
2. Right (turns to face West)
3. Forward (moves to (1,1))
4. Right (turns to face North)
5. Right (turns to face East)
6. Forward (moves to (1,2))
7. Right (turns to face South)
8. Forward (moves to (2,2))

Let's trace this.
Start (0,0) facing South.
1. Forward -> (1,0), facing South.
2. Right -> (1,0), facing West.
3. Forward -> (1,1), facing West.
4. Right -> (1,1), facing North.
5. Right -> (1,1), facing East.
6. Forward -> (1,2), facing East.
7. Right -> (1,2), facing South.
8. Forward -> (2,2), facing South.

This path is valid.

forward,right,forward,right,right,forward,right,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dpmVac_gDOO9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=530,
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
  total_token_count=1081
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=530 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1081 traffic_type=None
```

### `maze_line_3x3_30.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d5mVacC_BKzd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_30.json`

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
        text='Right, forward, right, forward, right, forward, left, forward, left, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d5mVafXtIMjl7M8P9OOViAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=859
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=859 traffic_type=None
```

### `maze_line_3x3_adj_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d5mVaYXHO6zd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
the, maze, is, as, follows:, (0, 0):, origin, walls:, up, right, left, (0, 1):, walls:, up, down, left, (0, 2):, walls:, up, right, (1, 0):, walls:, down, left, (1, 1):, walls:, up, down, (1, 2):, walls:, right, (2, 0):, walls:, up, down, left, (2, 1):, walls:, up, down, (2, 2):, target, walls:, down, right, let's, trace, the, path:, *, **start:**, (0, 0), facing, south., *, the, agent, is, at, (0, 0), and, facing, south., *, there, is, no, wall, to, the, south, from, (0, 0)., *, **action:**, forward., agent, moves, to, (1, 0)., facing, south., *, the, agent, is, at, (1, 0), and, facing, south., *, there, is, a, wall, to, the, south, at, (1, 0)., *, the, agent, needs, to, go, to, (1, 1)., from, (1, 0), facing, south, turning, left, will, face, east., *, **action:**, left., agent, turns, east., *, **action:**, forward., agent, moves, to, (1, 1)., facing, east., *, the, agent, is, at, (1, 1), and, facing, east., *, there, is, no, wall, to, the, east, from, (1, 1)., *, **action:**, forward., agent, moves, to, (1, 2)., facing, east., *, the, agent, is, at, (1, 2), and, facing, east., *, there, is, a, wall, to, the, east, at, (1, 2)., *, the, agent, needs, to, go, to, (2, 2)., from, (1, 2), facing, east, turning, left, will, face, north, turning, right, will, face, south., *, **action:**, right., agent, turns, south., *, **action:**, forward., agent, moves, to, (2, 2)., facing, south., *, the, agent, is, at, (2, 2), which, is, the, target., therefore, the, sequence, of, moves, is:, forward, left, forward, right, forward., forward, left, forward, right, forward
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

(0,0): Origin, walls: up, right, left
(0,1): Walls: up, down, left
(0,2): Walls: up, right

(1,0): Walls: down, left
(1,1): Walls: up, down
(1,2): Walls: right

(2,0): Walls: up, down, left
(2,1): Walls: up, down
(2,2): Target, walls: down, right

Let's trace the path:

*   **Start:** (0,0), facing South.
*   The agent is at (0,0) and facing South.
*   There is no wall to the South from (0,0).
*   **Action:** Forward. Agent moves to (1,0). Facing South.
*   The agent is at (1,0) and facing South.
*   There is a wall to the South at (1,0).
*   The agent needs to go to (1,1). From (1,0), facing South, turning left will face East.
*   **Action:** Left. Agent turns East.
*   **Action:** Forward. Agent moves to (1,1). Facing East.
*   The agent is at (1,1) and facing East.
*   There is no wall to the East from (1,1).
*   **Action:** Forward. Agent moves to (1,2). Facing East.
*   The agent is at (1,2) and facing East.
*   There is a wall to the East at (1,2).
*   The agent needs to go to (2,2). From (1,2), facing East, turning left will face North, turning right will face South.
*   **Action:** Right. Agent turns South.
*   **Action:** Forward. Agent moves to (2,2). Facing South.
*   The agent is at (2,2), which is the target.

Therefore, the sequence of moves is: forward, left, forward, right, forward.

forward,left,forward,right,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eZmVaYKKJJPe7M8PjqaxkQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=473,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=912
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=473 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=912 traffic_type=None
```

### `maze_occupancy_3x3_30.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='epmVaYT7CuO9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
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
  total_token_count=575
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=575 traffic_type=None
```

### `maze_occupancy_3x3_30.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e5mVaa7cIazd7M8PqdSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_30.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fJmVaZbjFKrw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1321
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1321 traffic_type=None
```

### `maze_occupancy_3x3_adj_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fJmVaebNNNWbkdUPueCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=621
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=621 traffic_type=None
```

### `maze_occupancy_3x3_ascii_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fpmVaYOtJNqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gJmVacbcKdnn7M8P8fieuAs' usage_metadata=GenerateContentResponseUsageMetadata(
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

