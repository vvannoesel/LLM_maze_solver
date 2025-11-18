# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_6.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_6.json` | **0.00%** | `input: 774 , ouput: 21` | `right, forward, right, forward, forward, left, forward, left, forward, left, forward` |
| `maze_line_3x3_adj_6.json` | **0.00%** | `input: 836 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_6.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_6.txt` | **0.00%** | `input: 439 , ouput: 517` | `the, maze, is, represented, as, follows:, (0, 0):, top-left, origin, walls:, up, right, left, (0, 1):, top, walls:, up, down, left, (0, 2):, top-right, walls:, up, right, (1, 0):, middle-left, walls:, down, left, (1, 1):, center, walls:, up, right, (1, 2):, middle-right, walls:, right, left, (2, 0):, bottom-left, walls:, up, down, left, (2, 1):, bottom, walls:, down, (2, 2):, bottom-right, target, walls:, down, right, the, agent, starts, at, (0, 0), facing, south., let's, trace, a, path:, 1., **start:**, (0, 0), facing, south., 2., **forward:**, moves, to, (1, 0)., now, at, (1, 0), facing, south., (cell, (0, 0), has, an, 'uprightleft_wall', so, cannot, go, up, right, or, left, from, origin., can, only, go, down.), 3., **right:**, turns, 90°, right, now, facing, west., at, (1, 0)., 4., **backward:**, turns, 180°, now, facing, east., moves, to, (1, 1)., now, at, (1, 1), facing, east., (cell, (1, 0), has, 'downleft_wall', so, cannot, go, down, or, left., can, go, up, to, (0, 0), but, that, is, origin, and, we, want, to, explore., can, go, right, to, (1, 1).), 5., **forward:**, moves, to, (1, 2)., now, at, (1, 2), facing, east., (cell, (1, 1), has, 'upright_wall', so, cannot, go, up, or, right., can, go, down, to, (2, 1), or, forward, to, (1, 2), if, facing, east/west.), 6., **forward:**, moves, to, (2, 2)., now, at, (2, 2), facing, east., (cell, (1, 2), has, 'rightleft_wall', so, cannot, go, right, or, left., can, go, up, to, (0, 2), or, down, to, (2, 2).), 7., **forward:**, reaches, target, at, (2, 2)., the, sequence, of, moves, is:, forward, right, backward, forward, forward., forward, right, backward, forward, forward` |
| `maze_occupancy_3x3_6.jpg` | **0.00%** | `input: 546 , ouput: 650` | `the, starting, position, is, (1, 1), and, the, agent, is, facing, south., the, goal, is, to, reach, the, star, at, (5, 5)., here's, the, path:, 1., the, agent, is, at, (1, 1), facing, south., move, forward, to, (2, 1)., 2., turn, left, now, facing, east., move, forward, to, (2, 2)., 3., turn, right, now, facing, south., move, forward, to, (3, 2)., 4., turn, right, now, facing, west., move, forward, to, (3, 1)., 5., turn, right, now, facing, north., move, forward, to, (2, 1)., 6., turn, right, now, facing, east., move, forward, to, (2, 2)., 7., turn, right, now, facing, south., move, forward, to, (3, 2)., 8., turn, left, now, facing, east., move, forward, to, (3, 3)., 9., turn, left, now, facing, north., move, forward, to, (2, 3)., 10., turn, left, now, facing, west., move, forward, to, (2, 2)., 11., turn, right, now, facing, south., move, forward, to, (3, 2)., 12., turn, right, now, facing, west., move, forward, to, (3, 1)., 13., turn, right, now, facing, north., move, forward, to, (2, 1)., 14., turn, right, now, facing, east., move, forward, to, (2, 2)., 15., turn, right, now, facing, south., move, forward, to, (3, 2)., 16., turn, right, now, facing, west., move, forward, to, (3, 1)., 17., turn, right, now, facing, north., move, forward, to, (2, 1)., 18., turn, right, now, facing, east., move, forward, to, (2, 2)., 19., turn, right, now, facing, south., move, forward, to, (3, 2)., 20., turn, left, now, facing, east., move, forward, to, (3, 3)., 21., turn, right, now, facing, south., move, forward, to, (4, 3)., 22., turn, left, now, facing, east., move, forward, to, (4, 4)., 23., turn, left, now, facing, north., move, forward, to, (3, 4)., 24., turn, right, now, facing, east., move, forward, to, (3, 5)., 25., turn, left, now, facing, north., move, forward, to, (2, 5)., 26., turn, left, now, facing, west., move, forward, to, (2, 4)., 27., turn, right, now, facing, north., move, forward, to, (1, 4)., 28., turn, right, now, facing, east., move, forward, to, (1, 5)., 29., turn, right, now, facing, south., move, forward, to, (2, 5)., 30., turn, right, now, facing, west., move, forward, to, (2, 4)., 31., turn, right, now, facing, north., move, forward, to, (1, 4)., 32., turn, right, now, facing, east., move, forward, to, (1, 5)., 33., turn, right, now` |
| `maze_occupancy_3x3_6.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_adj_6.json` | **0.00%** | `input: 1298 , ouput: 35` | `right, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_adj_6.txt` | **0.00%** | `input: 580 , ouput: 436` | `the, maze, is, 7x7., the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., here's, the, path, from, (1, 1), to, (5, 5):, 1., **(1, 1), facing, south:**, the, agent, needs, to, move, away, from, (1, 1)., the, only, available, move, from, (1, 1), is, to, (2, 1)., *, `forward`, (moves, to, (2, 1)), 2., **(2, 1), facing, south:**, from, (2, 1), the, agent, can, move, to, (3, 1)., *, `forward`, (moves, to, (3, 1)), 3., **(3, 1), facing, south:**, from, (3, 1), the, agent, can, move, to, (3, 2)., *, `right`, (turns, to, face, west, then, moves, to, (3, 2)), 4., **(3, 2), facing, west:**, from, (3, 2), the, agent, can, move, to, (3, 3)., *, `forward`, (moves, to, (3, 3)), 5., **(3, 3), facing, west:**, from, (3, 3), the, agent, can, move, to, (4, 3)., *, `forward`, (moves, to, (4, 3)), 6., **(4, 3), facing, west:**, from, (4, 3), the, agent, can, move, to, (5, 3)., *, `forward`, (moves, to, (5, 3)), 7., **(5, 3), facing, west:**, from, (5, 3), the, agent, can, move, to, (5, 4)., *, `forward`, (moves, to, (5, 4)), 8., **(5, 4), facing, west:**, from, (5, 4), the, agent, can, move, to, (5, 5)., *, `forward`, (moves, to, (5, 5)), the, final, sequence, of, instructions, is:, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_6.txt` | **0.00%** | `input: 317 , ouput: 51` | `right, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_tokenized_6.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward` |

---

## Full LLM Responses

### `maze_line_3x3_6.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ypMcaYCpMdj9xN8PsaeMoAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_6.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,left,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='y5McabjJJPK3xN8PoLSU2Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=795
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=795 traffic_type=None
```

### `maze_line_3x3_adj_6.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
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
        text='right, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zJMcad_HDPuDvdIPn_iEyAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_6.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
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
        text='right,forward,forward,right,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zJMcacanMKq-vdIPlaK54Ak' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_6.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows:, (0, 0):, top-left, origin, walls:, up, right, left, (0, 1):, top, walls:, up, down, left, (0, 2):, top-right, walls:, up, right, (1, 0):, middle-left, walls:, down, left, (1, 1):, center, walls:, up, right, (1, 2):, middle-right, walls:, right, left, (2, 0):, bottom-left, walls:, up, down, left, (2, 1):, bottom, walls:, down, (2, 2):, bottom-right, target, walls:, down, right, the, agent, starts, at, (0, 0), facing, south., let's, trace, a, path:, 1., **start:**, (0, 0), facing, south., 2., **forward:**, moves, to, (1, 0)., now, at, (1, 0), facing, south., (cell, (0, 0), has, an, 'uprightleft_wall', so, cannot, go, up, right, or, left, from, origin., can, only, go, down.), 3., **right:**, turns, 90°, right, now, facing, west., at, (1, 0)., 4., **backward:**, turns, 180°, now, facing, east., moves, to, (1, 1)., now, at, (1, 1), facing, east., (cell, (1, 0), has, 'downleft_wall', so, cannot, go, down, or, left., can, go, up, to, (0, 0), but, that, is, origin, and, we, want, to, explore., can, go, right, to, (1, 1).), 5., **forward:**, moves, to, (1, 2)., now, at, (1, 2), facing, east., (cell, (1, 1), has, 'upright_wall', so, cannot, go, up, or, right., can, go, down, to, (2, 1), or, forward, to, (1, 2), if, facing, east/west.), 6., **forward:**, moves, to, (2, 2)., now, at, (2, 2), facing, east., (cell, (1, 2), has, 'rightleft_wall', so, cannot, go, right, or, left., can, go, up, to, (0, 2), or, down, to, (2, 2).), 7., **forward:**, reaches, target, at, (2, 2)., the, sequence, of, moves, is:, forward, right, backward, forward, forward., forward, right, backward, forward, forward
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

(0,0): Top-left, origin, walls: up, right, left
(0,1): Top, walls: up, down, left
(0,2): Top-right, walls: up, right

(1,0): Middle-left, walls: down, left
(1,1): Center, walls: up, right
(1,2): Middle-right, walls: right, left

(2,0): Bottom-left, walls: up, down, left
(2,1): Bottom, walls: down
(2,2): Bottom-right, target, walls: down, right

The agent starts at (0,0) facing South.

Let's trace a path:

1.  **Start:** (0,0), facing South.
2.  **Forward:** Moves to (1,0). Now at (1,0), facing South. (Cell (0,0) has an 'uprightleft_wall', so cannot go up, right, or left from origin. Can only go down.)
3.  **Right:** Turns 90° right, now facing West. At (1,0).
4.  **Backward:** Turns 180°, now facing East. Moves to (1,1). Now at (1,1), facing East. (Cell (1,0) has 'downleft_wall', so cannot go down or left. Can go up to (0,0) but that is origin and we want to explore. Can go right to (1,1).)
5.  **Forward:** Moves to (1,2). Now at (1,2), facing East. (Cell (1,1) has 'upright_wall', so cannot go up or right. Can go down to (2,1) or forward to (1,2) if facing east/west.)
6.  **Forward:** Moves to (2,2). Now at (2,2), facing East. (Cell (1,2) has 'rightleft_wall', so cannot go right or left. Can go up to (0,2) or down to (2,2).)
7.  **Forward:** Reaches target at (2,2).

The sequence of moves is: forward, right, backward, forward, forward.

forward,right,backward,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='z5McabetE-eP28oP2dzIyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=517,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=956
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=517 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=956 traffic_type=None
```

### `maze_occupancy_3x3_6.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
the, starting, position, is, (1, 1), and, the, agent, is, facing, south., the, goal, is, to, reach, the, star, at, (5, 5)., here's, the, path:, 1., the, agent, is, at, (1, 1), facing, south., move, forward, to, (2, 1)., 2., turn, left, now, facing, east., move, forward, to, (2, 2)., 3., turn, right, now, facing, south., move, forward, to, (3, 2)., 4., turn, right, now, facing, west., move, forward, to, (3, 1)., 5., turn, right, now, facing, north., move, forward, to, (2, 1)., 6., turn, right, now, facing, east., move, forward, to, (2, 2)., 7., turn, right, now, facing, south., move, forward, to, (3, 2)., 8., turn, left, now, facing, east., move, forward, to, (3, 3)., 9., turn, left, now, facing, north., move, forward, to, (2, 3)., 10., turn, left, now, facing, west., move, forward, to, (2, 2)., 11., turn, right, now, facing, south., move, forward, to, (3, 2)., 12., turn, right, now, facing, west., move, forward, to, (3, 1)., 13., turn, right, now, facing, north., move, forward, to, (2, 1)., 14., turn, right, now, facing, east., move, forward, to, (2, 2)., 15., turn, right, now, facing, south., move, forward, to, (3, 2)., 16., turn, right, now, facing, west., move, forward, to, (3, 1)., 17., turn, right, now, facing, north., move, forward, to, (2, 1)., 18., turn, right, now, facing, east., move, forward, to, (2, 2)., 19., turn, right, now, facing, south., move, forward, to, (3, 2)., 20., turn, left, now, facing, east., move, forward, to, (3, 3)., 21., turn, right, now, facing, south., move, forward, to, (4, 3)., 22., turn, left, now, facing, east., move, forward, to, (4, 4)., 23., turn, left, now, facing, north., move, forward, to, (3, 4)., 24., turn, right, now, facing, east., move, forward, to, (3, 5)., 25., turn, left, now, facing, north., move, forward, to, (2, 5)., 26., turn, left, now, facing, west., move, forward, to, (2, 4)., 27., turn, right, now, facing, north., move, forward, to, (1, 4)., 28., turn, right, now, facing, east., move, forward, to, (1, 5)., 29., turn, right, now, facing, south., move, forward, to, (2, 5)., 30., turn, right, now, facing, west., move, forward, to, (2, 4)., 31., turn, right, now, facing, north., move, forward, to, (1, 4)., 32., turn, right, now, facing, east., move, forward, to, (1, 5)., 33., turn, right, now
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The starting position is (1, 1) and the agent is facing South. The goal is to reach the star at (5, 5).

Here's the path:
1. The agent is at (1,1) facing South. Move forward to (2,1).
2. Turn left, now facing East. Move forward to (2,2).
3. Turn right, now facing South. Move forward to (3,2).
4. Turn right, now facing West. Move forward to (3,1).
5. Turn right, now facing North. Move forward to (2,1).
6. Turn right, now facing East. Move forward to (2,2).
7. Turn right, now facing South. Move forward to (3,2).
8. Turn left, now facing East. Move forward to (3,3).
9. Turn left, now facing North. Move forward to (2,3).
10. Turn left, now facing West. Move forward to (2,2).
11. Turn right, now facing South. Move forward to (3,2).
12. Turn right, now facing West. Move forward to (3,1).
13. Turn right, now facing North. Move forward to (2,1).
14. Turn right, now facing East. Move forward to (2,2).
15. Turn right, now facing South. Move forward to (3,2).
16. Turn right, now facing West. Move forward to (3,1).
17. Turn right, now facing North. Move forward to (2,1).
18. Turn right, now facing East. Move forward to (2,2).
19. Turn right, now facing South. Move forward to (3,2).
20. Turn left, now facing East. Move forward to (3,3).
21. Turn right, now facing South. Move forward to (4,3).
22. Turn left, now facing East. Move forward to (4,4).
23. Turn left, now facing North. Move forward to (3,4).
24. Turn right, now facing East. Move forward to (3,5).
25. Turn left, now facing North. Move forward to (2,5).
26. Turn left, now facing West. Move forward to (2,4).
27. Turn right, now facing North. Move forward to (1,4).
28. Turn right, now facing East. Move forward to (1,5).
29. Turn right, now facing South. Move forward to (2,5).
30. Turn right, now facing West. Move forward to (2,4).
31. Turn right, now facing North. Move forward to (1,4).
32. Turn right, now facing East. Move forward to (1,5).
33. Turn right, now"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1JMcacUEofrGzQ_ztauACQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_6.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1pMcabm6BKWd28oP46bOiAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_6.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,right,forward,forward,right,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='15McabvTCvjXxs0P146HoQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1333 traffic_type=None
```

### `maze_occupancy_3x3_adj_6.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
the, maze, is, 7x7., the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., here's, the, path, from, (1, 1), to, (5, 5):, 1., **(1, 1), facing, south:**, the, agent, needs, to, move, away, from, (1, 1)., the, only, available, move, from, (1, 1), is, to, (2, 1)., *, `forward`, (moves, to, (2, 1)), 2., **(2, 1), facing, south:**, from, (2, 1), the, agent, can, move, to, (3, 1)., *, `forward`, (moves, to, (3, 1)), 3., **(3, 1), facing, south:**, from, (3, 1), the, agent, can, move, to, (3, 2)., *, `right`, (turns, to, face, west, then, moves, to, (3, 2)), 4., **(3, 2), facing, west:**, from, (3, 2), the, agent, can, move, to, (3, 3)., *, `forward`, (moves, to, (3, 3)), 5., **(3, 3), facing, west:**, from, (3, 3), the, agent, can, move, to, (4, 3)., *, `forward`, (moves, to, (4, 3)), 6., **(4, 3), facing, west:**, from, (4, 3), the, agent, can, move, to, (5, 3)., *, `forward`, (moves, to, (5, 3)), 7., **(5, 3), facing, west:**, from, (5, 3), the, agent, can, move, to, (5, 4)., *, `forward`, (moves, to, (5, 4)), 8., **(5, 4), facing, west:**, from, (5, 4), the, agent, can, move, to, (5, 5)., *, `forward`, (moves, to, (5, 5)), the, final, sequence, of, instructions, is:, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is 7x7. The origin is at (1,1) and the target is at (5,5). The agent starts at (1,1) facing south.

Here's the path from (1,1) to (5,5):

1. **(1,1) facing South:** The agent needs to move away from (1,1). The only available move from (1,1) is to (2,1).
    * `forward` (moves to (2,1))
2. **(2,1) facing South:** From (2,1), the agent can move to (3,1).
    * `forward` (moves to (3,1))
3. **(3,1) facing South:** From (3,1), the agent can move to (3,2).
    * `right` (turns to face West, then moves to (3,2))
4. **(3,2) facing West:** From (3,2), the agent can move to (3,3).
    * `forward` (moves to (3,3))
5. **(3,3) facing West:** From (3,3), the agent can move to (4,3).
    * `forward` (moves to (4,3))
6. **(4,3) facing West:** From (4,3), the agent can move to (5,3).
    * `forward` (moves to (5,3))
7. **(5,3) facing West:** From (5,3), the agent can move to (5,4).
    * `forward` (moves to (5,4))
8. **(5,4) facing West:** From (5,4), the agent can move to (5,5).
    * `forward` (moves to (5,5))

The final sequence of instructions is:
forward,forward,right,forward,forward,forward,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2ZMcaeTWCoGavdIPjcmJsAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=436,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=1016
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=436 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1016 traffic_type=None
```

### `maze_occupancy_3x3_ascii_6.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2ZMcaZLNM-3Zxs0PsZuluAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=368
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=368 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_6.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3JMcabarNaePvdIPnZTpsQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

