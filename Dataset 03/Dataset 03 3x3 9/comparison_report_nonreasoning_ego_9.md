# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_9.jpg` | **0.00%** | `input: 551 , ouput: 19` | `right, forward, right, forward, forward, left, forward, forward, right, forward` |
| `maze_line_3x3_9.json` | **0.00%** | `input: 774 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_adj_9.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_9.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_tokenized_9.txt` | **0.00%** | `input: 439 , ouput: 650` | `the, maze, is, a, 3x3, grid., the, origin, is, at, (0, 0)., the, target, is, at, (2, 2)., the, agent, starts, at, (0, 0), facing, south., let's, analyze, the, walls:, (0, 0):, walls:, up, right, left., this, means, only, down, is, open., (0, 1):, walls:, up, left., this, means, only, right, and, down, are, open., (0, 2):, walls:, up, right., this, means, only, left, and, down, are, open., (1, 0):, walls:, down, left., this, means, only, up, and, right, are, open., (1, 1):, walls:, down, right., this, means, only, up, and, left, are, open., (1, 2):, walls:, right, left., this, means, only, up, and, down, are, open., (2, 0):, walls:, up, down, left., this, means, only, right, is, open., (2, 1):, walls:, up, down., this, means, only, left, and, right, are, open., (2, 2):, walls:, down, right., this, means, only, up, and, left, are, open., start, at, (0, 0), facing, south., 1., from, (0, 0), facing, south, the, only, way, to, move, is, forward., -, action:, forward., agent, is, now, at, (1, 0), facing, south., 2., at, (1, 0), facing, south., walls, are, down, left., up, is, open, right, is, open., -, to, move, towards, the, target, (2, 2), we, need, to, go, east., from, south, turning, right, will, make, us, face, west., turning, left, will, make, us, face, east., -, action:, left., agent, is, now, at, (1, 0), facing, east., 3., at, (1, 0), facing, east., walls, are, down, left., up, is, open, right, is, open., -, move, forward, to, (1, 1)., -, action:, forward., agent, is, now, at, (1, 1), facing, east., 4., at, (1, 1), facing, east., walls, are, down, right., up, is, open, left, is, open., -, we, need, to, reach, (2, 2)., from, (1, 1), facing, east, we, can, go, to, (1, 2)., -, action:, forward., agent, is, now, at, (1, 2), facing, east., 5., at, (1, 2), facing, east., walls, are, right, left., up, is, open, down, is, open., -, from, (1, 2), facing, east, we, can't, move, forward., we, need, to, move, south., to, face, south, from, east, we, need, to, turn, right., -, action:, right., agent, is, now, at, (1, 2), facing, south., 6., at, (1, 2), facing, south., walls, are, right, left., up, is, open, down, is, open., -, move, forward, to, (2, 2)., -, action:, forward., agent, is, now, at, (2, 2), facing, south., this, is, the, target., the, sequence` |
| `maze_occupancy_3x3_9.jpg` | **0.00%** | `input: 546 , ouput: 35` | `right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_9.json` | **0.00%** | `input: 589 , ouput: 41` | `right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_9.json` | **8.33%** | `input: 1298 , ouput: 47` | `forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_9.txt` | **0.00%** | `input: 580 , ouput: 650` | `the, maze, is, a, 7x7, grid., the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., let's, represent, the, maze, as, a, graph., the, nodes, are, the, cells, (row, col), and, the, edges, represent, connections, between, adjacent, cells., nodes:, (1, 1), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 5), (3, 1), (3, 2), (3, 3), (3, 5), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), edges:, (1, 1), <->, (2, 1), (1, 3), <->, (1, 4), (1, 3), <->, (2, 3), (1, 4), <->, (1, 5), (1, 5), <->, (2, 5), (2, 1), <->, (3, 1), (2, 3), <->, (3, 3), (2, 5), <->, (3, 5), (3, 1), <->, (3, 2), (3, 2), <->, (3, 3), (3, 5), <->, (4, 5), (4, 5), <->, (5, 5), (5, 1), <->, (5, 2), (5, 2), <->, (5, 3), (5, 3), <->, (5, 4), (5, 4), <->, (5, 5), start:, (1, 1), facing, south, target:, (5, 5), we, can, use, breadth-first, search, (bfs), or, depth-first, search, (dfs), to, find, a, path., let's, trace, a, path, manually, keeping, track, of, the, agent's, current, position, and, direction., start, at, (1, 1), facing, south., 1., move, forward, to, (2, 1)., (facing, south), 2., move, forward, to, (3, 1)., (facing, south), 3., turn, right, (now, facing, west)., 4., move, forward, to, (3, 2)., (facing, west), 5., move, forward, to, (3, 3)., (facing, west), 6., turn, left, (now, facing, south)., 7., move, forward, to, (2, 3)., (facing, south), -, this, is, a, dead, end, for, now, as, we, want, to, go, towards, (5, 5), and, the, path, through, (2, 3), doesn't, seem, direct., let's, backtrack, to, (3, 3)., (backtrack, to, (3, 3), facing, south), 8., turn, right, (now, facing, east)., 9., move, forward, to, (3, 5)., (facing, east), 10., move, forward, to, (4, 5)., (facing, east), 11., move, forward, to, (5, 5)., (facing, east), -` |
| `maze_occupancy_3x3_ascii_9.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_9.txt` | **0.00%** | `input: 867 , ouput: 45` | `right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward` |

---

## Full LLM Responses

### `maze_line_3x3_9.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DJQcafjdFOaavdIPio31oQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DZQcaaeLBuv_vdIP4IWYuAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=785
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=785 traffic_type=None
```

### `maze_line_3x3_adj_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
        text='Right,forward,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DZQcaevmKeLTvdIPoYrOqAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
        text='Right, Forward, Right, Forward, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DpQcafayHM3VvdIP5qGjwQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
the, maze, is, a, 3x3, grid., the, origin, is, at, (0, 0)., the, target, is, at, (2, 2)., the, agent, starts, at, (0, 0), facing, south., let's, analyze, the, walls:, (0, 0):, walls:, up, right, left., this, means, only, down, is, open., (0, 1):, walls:, up, left., this, means, only, right, and, down, are, open., (0, 2):, walls:, up, right., this, means, only, left, and, down, are, open., (1, 0):, walls:, down, left., this, means, only, up, and, right, are, open., (1, 1):, walls:, down, right., this, means, only, up, and, left, are, open., (1, 2):, walls:, right, left., this, means, only, up, and, down, are, open., (2, 0):, walls:, up, down, left., this, means, only, right, is, open., (2, 1):, walls:, up, down., this, means, only, left, and, right, are, open., (2, 2):, walls:, down, right., this, means, only, up, and, left, are, open., start, at, (0, 0), facing, south., 1., from, (0, 0), facing, south, the, only, way, to, move, is, forward., -, action:, forward., agent, is, now, at, (1, 0), facing, south., 2., at, (1, 0), facing, south., walls, are, down, left., up, is, open, right, is, open., -, to, move, towards, the, target, (2, 2), we, need, to, go, east., from, south, turning, right, will, make, us, face, west., turning, left, will, make, us, face, east., -, action:, left., agent, is, now, at, (1, 0), facing, east., 3., at, (1, 0), facing, east., walls, are, down, left., up, is, open, right, is, open., -, move, forward, to, (1, 1)., -, action:, forward., agent, is, now, at, (1, 1), facing, east., 4., at, (1, 1), facing, east., walls, are, down, right., up, is, open, left, is, open., -, we, need, to, reach, (2, 2)., from, (1, 1), facing, east, we, can, go, to, (1, 2)., -, action:, forward., agent, is, now, at, (1, 2), facing, east., 5., at, (1, 2), facing, east., walls, are, right, left., up, is, open, down, is, open., -, from, (1, 2), facing, east, we, can't, move, forward., we, need, to, move, south., to, face, south, from, east, we, need, to, turn, right., -, action:, right., agent, is, now, at, (1, 2), facing, south., 6., at, (1, 2), facing, south., walls, are, right, left., up, is, open, down, is, open., -, move, forward, to, (2, 2)., -, action:, forward., agent, is, now, at, (2, 2), facing, south., this, is, the, target., the, sequence
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is a 3x3 grid.
The origin is at (0,0).
The target is at (2,2).
The agent starts at (0,0) facing South.

Let's analyze the walls:

(0,0): Walls: up, right, left. This means only down is open.
(0,1): Walls: up, left. This means only right and down are open.
(0,2): Walls: up, right. This means only left and down are open.

(1,0): Walls: down, left. This means only up and right are open.
(1,1): Walls: down, right. This means only up and left are open.
(1,2): Walls: right, left. This means only up and down are open.

(2,0): Walls: up, down, left. This means only right is open.
(2,1): Walls: up, down. This means only left and right are open.
(2,2): Walls: down, right. This means only up and left are open.

Start at (0,0) facing South.

1. From (0,0) facing South, the only way to move is Forward.
   - Action: Forward. Agent is now at (1,0) facing South.

2. At (1,0) facing South. Walls are down, left. Up is open, Right is open.
   - To move towards the target (2,2), we need to go East. From South, turning Right will make us face West. Turning Left will make us face East.
   - Action: Left. Agent is now at (1,0) facing East.

3. At (1,0) facing East. Walls are down, left. Up is open, Right is open.
   - Move forward to (1,1).
   - Action: Forward. Agent is now at (1,1) facing East.

4. At (1,1) facing East. Walls are down, right. Up is open, Left is open.
   - We need to reach (2,2). From (1,1) facing East, we can go to (1,2).
   - Action: Forward. Agent is now at (1,2) facing East.

5. At (1,2) facing East. Walls are right, left. Up is open, Down is open.
   - From (1,2) facing East, we can't move forward. We need to move South. To face South from East, we need to turn Right.
   - Action: Right. Agent is now at (1,2) facing South.

6. At (1,2) facing South. Walls are right, left. Up is open, Down is open.
   - Move forward to (2,2).
   - Action: Forward. Agent is now at (2,2) facing South. This is the target.

The sequence"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EZQcaYX2Au2jxN8PmJGE0Ak' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_9.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EpQcad-IB__axs0P3PW82Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
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
  total_token_count=581
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=581 traffic_type=None
```

### `maze_occupancy_3x3_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='E5QcabWoBKuP28oPu5_O2Q4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=630
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=630 traffic_type=None
```

### `maze_occupancy_3x3_adj_9.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FJQcaauxAeXZxs0P5LjvsAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1345
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1345 traffic_type=None
```

### `maze_occupancy_3x3_adj_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
the, maze, is, a, 7x7, grid., the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., let's, represent, the, maze, as, a, graph., the, nodes, are, the, cells, (row, col), and, the, edges, represent, connections, between, adjacent, cells., nodes:, (1, 1), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 5), (3, 1), (3, 2), (3, 3), (3, 5), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), edges:, (1, 1), <->, (2, 1), (1, 3), <->, (1, 4), (1, 3), <->, (2, 3), (1, 4), <->, (1, 5), (1, 5), <->, (2, 5), (2, 1), <->, (3, 1), (2, 3), <->, (3, 3), (2, 5), <->, (3, 5), (3, 1), <->, (3, 2), (3, 2), <->, (3, 3), (3, 5), <->, (4, 5), (4, 5), <->, (5, 5), (5, 1), <->, (5, 2), (5, 2), <->, (5, 3), (5, 3), <->, (5, 4), (5, 4), <->, (5, 5), start:, (1, 1), facing, south, target:, (5, 5), we, can, use, breadth-first, search, (bfs), or, depth-first, search, (dfs), to, find, a, path., let's, trace, a, path, manually, keeping, track, of, the, agent's, current, position, and, direction., start, at, (1, 1), facing, south., 1., move, forward, to, (2, 1)., (facing, south), 2., move, forward, to, (3, 1)., (facing, south), 3., turn, right, (now, facing, west)., 4., move, forward, to, (3, 2)., (facing, west), 5., move, forward, to, (3, 3)., (facing, west), 6., turn, left, (now, facing, south)., 7., move, forward, to, (2, 3)., (facing, south), -, this, is, a, dead, end, for, now, as, we, want, to, go, towards, (5, 5), and, the, path, through, (2, 3), doesn't, seem, direct., let's, backtrack, to, (3, 3)., (backtrack, to, (3, 3), facing, south), 8., turn, right, (now, facing, east)., 9., move, forward, to, (3, 5)., (facing, east), 10., move, forward, to, (4, 5)., (facing, east), 11., move, forward, to, (5, 5)., (facing, east), -
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is a 7x7 grid. The agent starts at (1,1) facing south. The target is at (5,5).

Let's represent the maze as a graph. The nodes are the cells (row, col), and the edges represent connections between adjacent cells.

Nodes:
(1,1), (1,3), (1,4), (1,5)
(2,1), (2,3), (2,5)
(3,1), (3,2), (3,3), (3,5)
(4,5)
(5,1), (5,2), (5,3), (5,4), (5,5)

Edges:
(1,1) <-> (2,1)
(1,3) <-> (1,4)
(1,3) <-> (2,3)
(1,4) <-> (1,5)
(1,5) <-> (2,5)
(2,1) <-> (3,1)
(2,3) <-> (3,3)
(2,5) <-> (3,5)
(3,1) <-> (3,2)
(3,2) <-> (3,3)
(3,5) <-> (4,5)
(4,5) <-> (5,5)
(5,1) <-> (5,2)
(5,2) <-> (5,3)
(5,3) <-> (5,4)
(5,4) <-> (5,5)

Start: (1,1) facing South
Target: (5,5)

We can use Breadth-First Search (BFS) or Depth-First Search (DFS) to find a path. Let's trace a path manually, keeping track of the agent's current position and direction.

Start at (1,1) facing South.

1. Move Forward to (2,1). (Facing South)
2. Move Forward to (3,1). (Facing South)
3. Turn Right (now facing West).
4. Move Forward to (3,2). (Facing West)
5. Move Forward to (3,3). (Facing West)
6. Turn Left (now facing South).
7. Move Forward to (2,3). (Facing South) - This is a dead end for now as we want to go towards (5,5) and the path through (2,3) doesn't seem direct. Let's backtrack to (3,3).
   (Backtrack to (3,3) facing South)
8. Turn Right (now facing East).
9. Move Forward to (3,5). (Facing East)
10. Move Forward to (4,5). (Facing East)
11. Move Forward to (5,5). (Facing East) -"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F5QcaZrwA5_VvdIPmYCYwQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GZQcafm2HZ7sxs0P6peA-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=967
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=967 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GpQcaaiNB__WvdIPm53psAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=912
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=912 traffic_type=None
```

