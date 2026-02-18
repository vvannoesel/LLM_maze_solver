# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_13.jpg` | **0.00%** | `input: 551 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_13.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_13.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_13.txt` | **0.00%** | `input: 468 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_tokenized_13.txt` | **0.00%** | `input: 439 , ouput: 27` | `right, forward, forward, right, forward, left, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_13.jpg` | **0.00%** | `input: 546 , ouput: 35` | `forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_13.json` | **0.00%** | `input: 589 , ouput: 83` | `right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_13.json` | **0.00%** | `input: 1292 , ouput: 33` | `right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_13.txt` | **0.00%** | `input: 580 , ouput: 650` | `the, maze, is, a, 7x7, grid, but, the, provided, adjacency, list, only, defines, connections, for, a, subset, of, the, cells., based, on, the, adjacency, list, the, passable, cells, appear, to, form, a, structure., the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., here's, a, path, from, (1, 1), to, (5, 5):, 1., from, (1, 1), facing, south:, the, agent, needs, to, move, towards, the, areas, where, the, target, is., looking, at, the, connections, it, seems, the, agent, needs, to, move, generally, down, and, then, right., there, are, no, direct, south, connections, from, (1, 1)., the, adjacency, list, implies, that, (1, 1), is, connected, to, (1, 2), but, no, other, cell., since, the, agent, is, facing, south, and, there's, no, south, connection, it, must, turn., however, given, the, adjacency, list, (1, 1), only, connects, to, (1, 2)., this, implies, the, agent, must, turn, east, to, move, to, (1, 2)., *, turn, right, (now, facing, east), *, forward, (moves, to, (1, 2)), 2., from, (1, 2), facing, east:, the, agent, can, move, east, to, (1, 3)., *, forward, (moves, to, (1, 3)), 3., from, (1, 3), facing, east:, the, agent, can, move, east, to, (1, 4), is, not, listed., it, can, move, south, to, (2, 3)., *, turn, left, (now, facing, south), *, forward, (moves, to, (2, 3)), 4., from, (2, 3), facing, south:, the, agent, can, move, south, to, (3, 3)., *, forward, (moves, to, (3, 3)), 5., from, (3, 3), facing, south:, the, agent, needs, to, get, towards, (5, 5)., from, (3, 3), it, can, go, to, (4, 3)., *, forward, (moves, to, (4, 3)), 6., from, (4, 3), facing, south:, the, agent, can, move, south, to, (5, 3)., *, forward, (moves, to, (5, 3)), 7., from, (5, 3), facing, south:, the, agent, can, move, east, to, (5, 4)., *, turn, right, (now, facing, west), *, turn, right, (now, facing, north), *, turn, right, (now, facing, east), *, forward, (moves, to, (5, 4)), 8., from, (5, 4), facing, east:, the, agent, can, move, east, to, (5, 5)., *, forward, (moves, to, (5, 5)), let's, re-evaluate, from, (1, 1), facing, south., the, adjacency, list:, (1, 1), <->, (1, 2)., so, the, only, way, from, (1, 1), is, to, (1, 2)., start, (1, 1), facing, south., to, move, to, (1, 2), the, agent, must, face, east` |
| `maze_occupancy_3x3_ascii_13.txt` | **0.00%** | `input: 318 , ouput: 37` | `right, forward, forward, right, forward, forward, backward, forward, left, forward, left, forward, forward, forward, right, forward, forward, right, forward` |
| `maze_occupancy_3x3_tokenized_13.txt` | **0.00%** | `input: 867 , ouput: 47` | `right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_13.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, forward, left
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DZeVabvQMqOF7M8P9PzH6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_13.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, forward, left
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
        text='Right,Forward,Right,Forward,Forward,Right,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DpeVaaXfDvjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_13.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, forward, left
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
        text='Right, forward, right, forward, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DpeVaYuZOYTw7M8P482J-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_13.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, forward, left
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
        text='Right, Forward, Right, Forward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='D5eVaYrhIN_x7M8P1Ouu-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_13.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, forward, left
```

**Extracted Answer:**
```
right, forward, forward, right, forward, left, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='D5eVaYmsO9qfnsEPxvyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=466
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=466 traffic_type=None
```

### `maze_occupancy_3x3_13.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, forward, forward, left, forward
```

**Extracted Answer:**
```
forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EJeVaavDK465kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_13.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EZeVab6JE4OH7M8PxuqcmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=83,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=672
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=83 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=672 traffic_type=None
```

### `maze_occupancy_3x3_adj_13.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EZeVaYS2LfjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1325
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1325 traffic_type=None
```

### `maze_occupancy_3x3_adj_13.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, forward, forward, left, forward
```

**Extracted Answer:**
```
the, maze, is, a, 7x7, grid, but, the, provided, adjacency, list, only, defines, connections, for, a, subset, of, the, cells., based, on, the, adjacency, list, the, passable, cells, appear, to, form, a, structure., the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., here's, a, path, from, (1, 1), to, (5, 5):, 1., from, (1, 1), facing, south:, the, agent, needs, to, move, towards, the, areas, where, the, target, is., looking, at, the, connections, it, seems, the, agent, needs, to, move, generally, down, and, then, right., there, are, no, direct, south, connections, from, (1, 1)., the, adjacency, list, implies, that, (1, 1), is, connected, to, (1, 2), but, no, other, cell., since, the, agent, is, facing, south, and, there's, no, south, connection, it, must, turn., however, given, the, adjacency, list, (1, 1), only, connects, to, (1, 2)., this, implies, the, agent, must, turn, east, to, move, to, (1, 2)., *, turn, right, (now, facing, east), *, forward, (moves, to, (1, 2)), 2., from, (1, 2), facing, east:, the, agent, can, move, east, to, (1, 3)., *, forward, (moves, to, (1, 3)), 3., from, (1, 3), facing, east:, the, agent, can, move, east, to, (1, 4), is, not, listed., it, can, move, south, to, (2, 3)., *, turn, left, (now, facing, south), *, forward, (moves, to, (2, 3)), 4., from, (2, 3), facing, south:, the, agent, can, move, south, to, (3, 3)., *, forward, (moves, to, (3, 3)), 5., from, (3, 3), facing, south:, the, agent, needs, to, get, towards, (5, 5)., from, (3, 3), it, can, go, to, (4, 3)., *, forward, (moves, to, (4, 3)), 6., from, (4, 3), facing, south:, the, agent, can, move, south, to, (5, 3)., *, forward, (moves, to, (5, 3)), 7., from, (5, 3), facing, south:, the, agent, can, move, east, to, (5, 4)., *, turn, right, (now, facing, west), *, turn, right, (now, facing, north), *, turn, right, (now, facing, east), *, forward, (moves, to, (5, 4)), 8., from, (5, 4), facing, east:, the, agent, can, move, east, to, (5, 5)., *, forward, (moves, to, (5, 5)), let's, re-evaluate, from, (1, 1), facing, south., the, adjacency, list:, (1, 1), <->, (1, 2)., so, the, only, way, from, (1, 1), is, to, (1, 2)., start, (1, 1), facing, south., to, move, to, (1, 2), the, agent, must, face, east
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is a 7x7 grid, but the provided adjacency list only defines connections for a subset of the cells. Based on the adjacency list, the passable cells appear to form a structure. The origin is at (1,1) and the target is at (5,5). The agent starts at (1,1) facing South.

Here's a path from (1,1) to (5,5):

1.  From (1,1) facing South: The agent needs to move towards the areas where the target is. Looking at the connections, it seems the agent needs to move generally down and then right. There are no direct South connections from (1,1). The adjacency list implies that (1,1) is connected to (1,2), but no other cell. Since the agent is facing South and there's no South connection, it must turn. However, given the adjacency list, (1,1) only connects to (1,2). This implies the agent must turn East to move to (1,2).
    *   Turn Right (now facing East)
    *   Forward (moves to (1,2))
2.  From (1,2) facing East: The agent can move East to (1,3).
    *   Forward (moves to (1,3))
3.  From (1,3) facing East: The agent can move East to (1,4) is not listed. It can move South to (2,3).
    *   Turn Left (now facing South)
    *   Forward (moves to (2,3))
4.  From (2,3) facing South: The agent can move South to (3,3).
    *   Forward (moves to (3,3))
5.  From (3,3) facing South: The agent needs to get towards (5,5). From (3,3), it can go to (4,3).
    *   Forward (moves to (4,3))
6.  From (4,3) facing South: The agent can move South to (5,3).
    *   Forward (moves to (5,3))
7.  From (5,3) facing South: The agent can move East to (5,4).
    *   Turn Right (now facing West)
    *   Turn Right (now facing North)
    *   Turn Right (now facing East)
    *   Forward (moves to (5,4))
8.  From (5,4) facing East: The agent can move East to (5,5).
    *   Forward (moves to (5,5))

Let's re-evaluate from (1,1) facing South. The adjacency list: (1,1) <-> (1,2). So the only way from (1,1) is to (1,2).
Start (1,1) facing South.
To move to (1,2), the agent must face East"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FJeVabPcCaeN7M8P6NXVwQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_13.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, backward, forward, left, forward, left, forward, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Backward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FJeVaZzoNNHMkdUPyI67sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=318,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=318
    ),
  ],
  total_token_count=355
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=318 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=318
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=355 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_13.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FZeVaZnOFO3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=914
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=914 traffic_type=None
```

