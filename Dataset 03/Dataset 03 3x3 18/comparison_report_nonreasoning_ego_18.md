# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_18.jpg` | **0.00%** | `input: 551 , ouput: 650` | `the, agent, starts, at, (0, 0), facing, south., the, goal, is, to, reach, the, star, at, (2, 2)., 1., the, agent, is, at, (0, 0), facing, south., to, move, towards, the, star, the, agent, needs, to, go, right, and, then, down., 2., turn, right, (now, facing, west)., 3., forward, (moves, to, (0, 1), facing, west)., 4., turn, right, (now, facing, north)., 5., forward, (moves, to, (0, 2), facing, north)., 6., turn, right, (now, facing, east)., 7., forward, (moves, to, (1, 2), facing, east)., 8., turn, right, (now, facing, south)., 9., forward, (moves, to, (2, 2), facing, south)., this, is, the, star., let's, re-evaluate, based, on, the, maze, structure., the, agent, starts, at, (0, 0), facing, south., 1., the, cell, (0, 0), is, the, top-left, cell., there, is, a, wall, to, the, east., 2., we, need, to, go, down., the, agent, is, facing, south., 3., forward, (moves, to, (1, 0), facing, south)., 4., the, cell, (1, 0), has, a, wall, to, the, east., 5., we, need, to, go, down, again., 6., forward, (moves, to, (2, 0), facing, south)., 7., now, we, are, at, the, bottom-left, cell., the, star, is, at, (2, 2)., we, need, to, move, east., 8., turn, right, (now, facing, west)., 9., turn, right, (now, facing, north)., 10., turn, right, (now, facing, east)., now, facing, east., 11., forward, (moves, to, (2, 1), facing, east)., 12., forward, (moves, to, (2, 2), facing, east)., this, is, the, star., let's, try, another, path., start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0), facing, south)., 2., turn, left, (now, facing, east)., 3., forward, (moves, to, (1, 1), facing, east)., 4., turn, left, (now, facing, north)., 5., forward, (moves, to, (0, 1), facing, north)., 6., turn, right, (now, facing, east)., 7., forward, (moves, to, (0, 2), facing, east)., 8., turn, right, (now, facing, south)., 9., forward, (moves, to, (1, 2), facing, south)., 10., turn, right, (now, facing, west)., 11., turn, right, (now, facing, north)., 12., turn, right, (now, facing, east)., now, facing, east., 13., forward, (moves, to, (2, 2), facing, east)., this, is, the, star., let's, try, the, most, direct, path., start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0), facing, south)., 2., turn, left, (now, facing, east)., 3., forward, (moves, to, (1, 1), facing, east)., 4., turn, right, (now, facing, south)., 5.` |
| `maze_line_3x3_18.json` | **0.00%** | `input: 774 , ouput: 17` | `right, forward, right, forward, left, forward, forward, right, forward` |
| `maze_line_3x3_adj_18.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_18.txt` | **0.00%** | `input: 468 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_tokenized_18.txt` | **0.00%** | `input: 439 , ouput: 650` | `right, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward` |
| `maze_occupancy_3x3_18.jpg` | **0.00%** | `input: 546 , ouput: 41` | `right, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_18.json` | **0.00%** | `input: 589 , ouput: 650` | `forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left` |
| `maze_occupancy_3x3_adj_18.json` | **0.00%** | `input: 1298 , ouput: 35` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_18.txt` | **0.00%** | `input: 580 , ouput: 39` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_18.txt` | **0.00%** | `input: 315 , ouput: 57` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, backward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_18.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_18.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), facing, south., the, goal, is, to, reach, the, star, at, (2, 2)., 1., the, agent, is, at, (0, 0), facing, south., to, move, towards, the, star, the, agent, needs, to, go, right, and, then, down., 2., turn, right, (now, facing, west)., 3., forward, (moves, to, (0, 1), facing, west)., 4., turn, right, (now, facing, north)., 5., forward, (moves, to, (0, 2), facing, north)., 6., turn, right, (now, facing, east)., 7., forward, (moves, to, (1, 2), facing, east)., 8., turn, right, (now, facing, south)., 9., forward, (moves, to, (2, 2), facing, south)., this, is, the, star., let's, re-evaluate, based, on, the, maze, structure., the, agent, starts, at, (0, 0), facing, south., 1., the, cell, (0, 0), is, the, top-left, cell., there, is, a, wall, to, the, east., 2., we, need, to, go, down., the, agent, is, facing, south., 3., forward, (moves, to, (1, 0), facing, south)., 4., the, cell, (1, 0), has, a, wall, to, the, east., 5., we, need, to, go, down, again., 6., forward, (moves, to, (2, 0), facing, south)., 7., now, we, are, at, the, bottom-left, cell., the, star, is, at, (2, 2)., we, need, to, move, east., 8., turn, right, (now, facing, west)., 9., turn, right, (now, facing, north)., 10., turn, right, (now, facing, east)., now, facing, east., 11., forward, (moves, to, (2, 1), facing, east)., 12., forward, (moves, to, (2, 2), facing, east)., this, is, the, star., let's, try, another, path., start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0), facing, south)., 2., turn, left, (now, facing, east)., 3., forward, (moves, to, (1, 1), facing, east)., 4., turn, left, (now, facing, north)., 5., forward, (moves, to, (0, 1), facing, north)., 6., turn, right, (now, facing, east)., 7., forward, (moves, to, (0, 2), facing, east)., 8., turn, right, (now, facing, south)., 9., forward, (moves, to, (1, 2), facing, south)., 10., turn, right, (now, facing, west)., 11., turn, right, (now, facing, north)., 12., turn, right, (now, facing, east)., now, facing, east., 13., forward, (moves, to, (2, 2), facing, east)., this, is, the, star., let's, try, the, most, direct, path., start, at, (0, 0), facing, south., 1., forward, (moves, to, (1, 0), facing, south)., 2., turn, left, (now, facing, east)., 3., forward, (moves, to, (1, 1), facing, east)., 4., turn, right, (now, facing, south)., 5.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (0,0) facing south. The goal is to reach the star at (2,2).

1. The agent is at (0,0) facing South. To move towards the star, the agent needs to go right and then down.
2. Turn right (now facing West).
3. Forward (moves to (0,1), facing West).
4. Turn right (now facing North).
5. Forward (moves to (0,2), facing North).
6. Turn right (now facing East).
7. Forward (moves to (1,2), facing East).
8. Turn right (now facing South).
9. Forward (moves to (2,2), facing South). This is the star.

Let's re-evaluate based on the maze structure.

The agent starts at (0,0) facing South.

1. The cell (0,0) is the top-left cell. There is a wall to the east.
2. We need to go down. The agent is facing South.
3. Forward (moves to (1,0), facing South).
4. The cell (1,0) has a wall to the east.
5. We need to go down again.
6. Forward (moves to (2,0), facing South).
7. Now we are at the bottom-left cell. The star is at (2,2). We need to move East.
8. Turn right (now facing West).
9. Turn right (now facing North).
10. Turn right (now facing East). Now facing East.
11. Forward (moves to (2,1), facing East).
12. Forward (moves to (2,2), facing East). This is the star.

Let's try another path.
Start at (0,0) facing South.

1. Forward (moves to (1,0), facing South).
2. Turn left (now facing East).
3. Forward (moves to (1,1), facing East).
4. Turn left (now facing North).
5. Forward (moves to (0,1), facing North).
6. Turn right (now facing East).
7. Forward (moves to (0,2), facing East).
8. Turn right (now facing South).
9. Forward (moves to (1,2), facing South).
10. Turn right (now facing West).
11. Turn right (now facing North).
12. Turn right (now facing East). Now facing East.
13. Forward (moves to (2,2), facing East). This is the star.

Let's try the most direct path.
Start at (0,0) facing South.

1. Forward (moves to (1,0), facing South).
2. Turn left (now facing East).
3. Forward (moves to (1,1), facing East).
4. Turn right (now facing South).
5."""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='W5eVaeKND-3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1201
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1201 traffic_type=None
```

### `maze_line_3x3_18.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
```

**Extracted Answer:**
```
right, forward, right, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Left, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='W5eVafCeOdqfnsEPzfyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_18.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XJeVaYveG5C-nsEPxMmk4QY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_18.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XZeVaYn-AoqjkdUPl43u2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=479
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=479 traffic_type=None
```

### `maze_line_3x3_tokenized_18.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='X5eVaYyjD-O9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_18.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='X5eVafCJPMPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
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
  total_token_count=587
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=587 traffic_type=None
```

### `maze_occupancy_3x3_18.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YZeVae-tHIWF7M8PnoeMqQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_18.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YpeVad3fEq2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_18.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YpeVaZfaM7yK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=619
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=619 traffic_type=None
```

### `maze_occupancy_3x3_ascii_18.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, backward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,right,forward,forward,forward,backward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Y5eVafDvGt_x7M8P1Ouu-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=372
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=372 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_18.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZZeVadzbEeO9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

