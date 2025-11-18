# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_8.jpg` | **0.00%** | `input: 551 , ouput: 650` | `the, agent, starts, at, (0, 0), facing, south., the, maze, is, 3x3., the, start, is, the, circle, at, (0, 0)., the, end, is, the, star, at, (2, 2)., 1., the, agent, is, at, (0, 0), facing, south., the, wall, is, to, the, left, and, in, front., the, only, way, to, move, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (0, 1), facing, east), 2., the, agent, is, at, (0, 1), facing, east., the, wall, is, in, front., the, only, way, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (1, 1), facing, south), 3., the, agent, is, at, (1, 1), facing, south., there, is, a, wall, to, the, left, and, in, front., the, only, way, to, move, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (1, 0), facing, west), 4., the, agent, is, at, (1, 0), facing, west., the, wall, is, in, front., the, only, way, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (2, 0), facing, north), 5., the, agent, is, at, (2, 0), facing, north., there, is, a, wall, to, the, left., the, path, is, forward, and, then, right., forward., (agent, is, now, at, (1, 0), facing, north), turn, right., forward., (agent, is, now, at, (1, 1), facing, east), 6., the, agent, is, at, (1, 1), facing, east., the, path, is, forward., forward., (agent, is, now, at, (1, 2), facing, east), 7., the, agent, is, at, (1, 2), facing, east., the, path, is, forward., forward., (agent, is, now, at, (2, 2), facing, east), let's, restart, with, a, simpler, path., start, at, (0, 0), facing, south., the, goal, is, (2, 2)., 1., move, right, (turn, right, move, forward)., agent, is, at, (0, 1), facing, east., 2., turn, right., agent, is, at, (0, 1), facing, south., 3., move, forward., agent, is, at, (1, 1), facing, south., 4., turn, right., agent, is, at, (1, 1), facing, west., 5., move, forward., agent, is, at, (1, 0), facing, west., 6., turn, right., agent, is, at, (1, 0), facing, north., 7., move, forward., agent, is, at, (0, 0), facing, north., this, is, not, working., let's, analyze, the, maze, again., start, at, (0, 0), facing, south., walls:, (0, 0), south, wall., (0, 1), east, wall., (1, 1), north, and, east, wall., (1, 0), south, wall., (2, 0), west, wall., (2, 1), west, wall., the, path, must, go, around` |
| `maze_line_3x3_8.json` | **0.00%** | `input: 774 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_adj_8.json` | **0.00%** | `input: 836 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_8.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_8.txt` | **0.00%** | `input: 439 , ouput: 47` | `right, forward, right, forward, left, forward, forward, right, forward, left, left, forward, forward, right, forward, right, forward, left, forward, left, left, forward, right, forward` |
| `maze_occupancy_3x3_8.jpg` | **0.00%** | `input: 546 , ouput: 27` | `right, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward` |
| `maze_occupancy_3x3_8.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_8.json` | **0.00%** | `input: 1298 , ouput: 39` | `forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_8.txt` | **0.00%** | `input: 580 , ouput: 45` | `right, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_ascii_8.txt` | **0.00%** | `input: 317 , ouput: 51` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_tokenized_8.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_8.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), facing, south., the, maze, is, 3x3., the, start, is, the, circle, at, (0, 0)., the, end, is, the, star, at, (2, 2)., 1., the, agent, is, at, (0, 0), facing, south., the, wall, is, to, the, left, and, in, front., the, only, way, to, move, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (0, 1), facing, east), 2., the, agent, is, at, (0, 1), facing, east., the, wall, is, in, front., the, only, way, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (1, 1), facing, south), 3., the, agent, is, at, (1, 1), facing, south., there, is, a, wall, to, the, left, and, in, front., the, only, way, to, move, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (1, 0), facing, west), 4., the, agent, is, at, (1, 0), facing, west., the, wall, is, in, front., the, only, way, is, to, turn, right, and, move, forward., turn, right., forward., (agent, is, now, at, (2, 0), facing, north), 5., the, agent, is, at, (2, 0), facing, north., there, is, a, wall, to, the, left., the, path, is, forward, and, then, right., forward., (agent, is, now, at, (1, 0), facing, north), turn, right., forward., (agent, is, now, at, (1, 1), facing, east), 6., the, agent, is, at, (1, 1), facing, east., the, path, is, forward., forward., (agent, is, now, at, (1, 2), facing, east), 7., the, agent, is, at, (1, 2), facing, east., the, path, is, forward., forward., (agent, is, now, at, (2, 2), facing, east), let's, restart, with, a, simpler, path., start, at, (0, 0), facing, south., the, goal, is, (2, 2)., 1., move, right, (turn, right, move, forward)., agent, is, at, (0, 1), facing, east., 2., turn, right., agent, is, at, (0, 1), facing, south., 3., move, forward., agent, is, at, (1, 1), facing, south., 4., turn, right., agent, is, at, (1, 1), facing, west., 5., move, forward., agent, is, at, (1, 0), facing, west., 6., turn, right., agent, is, at, (1, 0), facing, north., 7., move, forward., agent, is, at, (0, 0), facing, north., this, is, not, working., let's, analyze, the, maze, again., start, at, (0, 0), facing, south., walls:, (0, 0), south, wall., (0, 1), east, wall., (1, 1), north, and, east, wall., (1, 0), south, wall., (2, 0), west, wall., (2, 1), west, wall., the, path, must, go, around
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (0,0) facing south.
The maze is 3x3.
The start is the circle at (0,0).
The end is the star at (2,2).

1. The agent is at (0,0) facing South. The wall is to the left and in front. The only way to move is to turn right and move forward.
Turn Right.
Forward. (Agent is now at (0,1) facing East)
2. The agent is at (0,1) facing East. The wall is in front. The only way is to turn right and move forward.
Turn Right.
Forward. (Agent is now at (1,1) facing South)
3. The agent is at (1,1) facing South. There is a wall to the left and in front. The only way to move is to turn right and move forward.
Turn Right.
Forward. (Agent is now at (1,0) facing West)
4. The agent is at (1,0) facing West. The wall is in front. The only way is to turn right and move forward.
Turn Right.
Forward. (Agent is now at (2,0) facing North)
5. The agent is at (2,0) facing North. There is a wall to the left. The path is forward and then right.
Forward. (Agent is now at (1,0) facing North)
Turn Right.
Forward. (Agent is now at (1,1) facing East)
6. The agent is at (1,1) facing East. The path is forward.
Forward. (Agent is now at (1,2) facing East)
7. The agent is at (1,2) facing East. The path is forward.
Forward. (Agent is now at (2,2) facing East)

Let's restart with a simpler path.

Start at (0,0) facing South.
The goal is (2,2).

1. Move Right (turn right, move forward). Agent is at (0,1) facing East.
2. Turn Right. Agent is at (0,1) facing South.
3. Move Forward. Agent is at (1,1) facing South.
4. Turn Right. Agent is at (1,1) facing West.
5. Move Forward. Agent is at (1,0) facing West.
6. Turn Right. Agent is at (1,0) facing North.
7. Move Forward. Agent is at (0,0) facing North.

This is not working. Let's analyze the maze again.

Start at (0,0) facing South.
Walls:
(0,0) South wall.
(0,1) East wall.
(1,1) North and East wall.
(1,0) South wall.
(2,0) West wall.
(2,1) West wall.

The path must go around"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_5Mcaf7JL4f0xs0Pvuq1kAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_8.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
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
        text='Right,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AJQcae7DJLLUvdIP9tDr8As' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_8.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AZQcaYOmDpzYxN8PqcOgsQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_8.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AZQcaeTgLvfPvdIPp-ycyAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_8.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, left, forward, forward, right, forward, left, left, forward, forward, right, forward, right, forward, left, forward, left, left, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Left, Forward, Forward, Right, Forward, Left, Left, Forward, Forward, Right, Forward, Right, Forward, Left, Forward, Left, Left, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ApQcacmBIof0xs0Pvuq1kAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=486
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=486 traffic_type=None
```

### `maze_occupancy_3x3_8.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BJQcad6HDoDXvdIP097RmAg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_8.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BpQcadP-D4Laxs0PwvHjwQ4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_8.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BpQcae6oOvuDvdIPn_iEyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1337
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1337 traffic_type=None
```

### `maze_occupancy_3x3_adj_8.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Right,Forward,Left,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B5Qcae2wMLLUvdIP9tDr8As' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=625
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=625 traffic_type=None
```

### `maze_occupancy_3x3_ascii_8.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CJQcaZ7kJYrkvdIPipOBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_8.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='C5QcabegC6uP28oPu5_O2Q4' usage_metadata=GenerateContentResponseUsageMetadata(
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

