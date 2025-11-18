# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_9.jpg` | **0.00%** | `input: 427 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_9.json` | **33.33%** | `input: 650 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_9.json` | **33.33%** | `input: 712 , ouput: 5` | `down, right, down` |
| `maze_line_3x3_adj_9.txt` | **33.33%** | `input: 344 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_tokenized_9.txt` | **0.00%** | `input: 315 , ouput: 5` | `right, down, right` |
| `maze_occupancy_3x3_9.jpg` | **8.33%** | `input: 422 , ouput: 21` | `down, right, down, right, down, right, down, left, down, right, right` |
| `maze_occupancy_3x3_9.json` | **0.00%** | `input: 465 , ouput: 650` | `right, down, down, right, right, down, down, right, right, up, right, down, down, right, down, down, left, left, left, left, down, down, right, right, right, right, up, right, right, down, down, down, right, right, right, up, up, up, up, right, down, down, down, right, right, right, up, up, up, right, right, down, down, down, right, right, right, up, up, up, up, up, right, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down` |
| `maze_occupancy_3x3_adj_9.json` | **0.00%** | `input: 1174 , ouput: 650` | `the, provided, maze, data, is, an, adjacency, list, representation, of, the, maze., to, solve, the, maze, i, will, use, a, breadth-first, search, (bfs), algorithm., bfs, is, suitable, for, finding, the, shortest, path, in, an, unweighted, graph, which, is, what, this, maze, represents., here's, how, i'll, approach, it:, 1., **parse, the, maze:**, i'll, convert, the, adjacency, list, into, a, more, usable, dictionary, where, keys, are, node, coordinates, (tuples), and, values, are, lists, of, their, neighboring, coordinates., 2., **initialize, bfs:**, *, a, queue, will, store, paths, to, explore., each, element, in, the, queue, will, be, a, tuple:, `(current_node, path_taken_to_reach_it)`., *, a, set, will, keep, track, of, visited, nodes, to, avoid, cycles, and, redundant, exploration., 3., **start, bfs:**, *, add, the, start, node, `(1, 1)`, and, an, empty, path, `[]`, to, the, queue., *, add, the, start, node, `(1, 1)`, to, the, visited, set., 4., **explore:**, *, while, the, queue, is, not, empty:, *, dequeue, the, `(current_node, current_path)`., *, if, `current_node`, is, the, `end`, node, `(5, 5)`, i've, found, the, path., i, will, then, convert, the, `current_path`, (which, is, a, list, of, coordinate, changes), into, the, required, move, sequence, (up, down, left, right)., *, for, each, `neighbor`, of, `current_node`:, *, if, the, `neighbor`, has, not, been, visited:, *, mark, the, `neighbor`, as, visited., *, calculate, the, move, from, `current_node`, to, `neighbor`, (e.g., `(2, 1)`, from, `(1, 1)`, is, a, 'down', move)., *, enqueue, `(neighbor, current_path, +, [move])`., let's, trace, the, path., start:, `[1, 1]`, end:, `[5, 5]`, maze, graph, representation, (derived, from, json):, `{, (1, 1):, [(2, 1)], (1, 3):, [(1, 4), (2, 3)], (1, 4):, [(1, 5), (1, 3)], (1, 5):, [(1, 4), (2, 5)], (2, 1):, [(3, 1), (1, 1)], (2, 3):, [(3, 3), (1, 3)], (2, 5):, [(3, 5), (1, 5)], (3, 1):, [(3, 2), (2, 1)], (3, 2):, [(3, 3), (3, 1)], (3, 3):, [(3, 2)` |
| `maze_occupancy_3x3_adj_9.txt` | **0.00%** | `input: 456 , ouput: 650` | `i, need, to, find, a, path, from, (1, 1), to, (5, 5), in, the, given, 7x7, maze., the, adjacency, list, represents, the, connections, between, cells., i, can, visualize, this, as, a, grid, where, (row, col), represents, a, cell., let's, list, the, connections, and, identify, the, start, and, end, points:, start:, (1, 1), end:, (5, 5), connections:, (1, 1), <->, (2, 1), (1, 3), <->, (1, 4), (1, 3), <->, (2, 3), (1, 4), <->, (1, 5), (1, 5), <->, (2, 5), (2, 1), <->, (3, 1), (2, 3), <->, (3, 3), (2, 5), <->, (3, 5), (3, 1), <->, (3, 2), (3, 2), <->, (3, 3), (3, 5), <->, (4, 5), (4, 5), <->, (5, 5), (5, 1), <->, (5, 2), (5, 2), <->, (5, 3), (5, 3), <->, (5, 4), (5, 4), <->, (5, 5), let's, try, to, trace, a, path, from, (1, 1), to, (5, 5):, 1., start, at, (1, 1)., 2., from, (1, 1), the, only, connection, is, to, (2, 1)., move, down., current, path:, down., current, position:, (2, 1)., 3., from, (2, 1), the, only, connection, is, to, (3, 1)., move, down., current, path:, down, down., current, position:, (3, 1)., 4., from, (3, 1), we, can, go, to, (3, 2)., move, right., current, path:, down, down, right., current, position:, (3, 2)., 5., from, (3, 2), we, can, go, to, (3, 3)., move, right., current, path:, down, down, right, right., current, position:, (3, 3)., 6., from, (3, 3), we, can, go, to, (2, 3)., let's, check, if, this, leads, anywhere, useful., if, we, go, to, (2, 3), then, to, (1, 3), or, (2, 5)., this, seems, to, be, going, away, from, (5, 5)., let's, backtrack, and, explore, other, options, from, (3, 3)., from, (3, 3), we, can, also, go, to, (3, 2), (backtrack), or, (2, 3)., let's, reconsider., let's, retry, systematically, exploring, the, path, to, (5, 5)., start:, (1, 1), possible, moves, from, (1, 1):, (2, 1), path:, (1, 1), ->, (2, 1), move:, down, current, position:, (2` |
| `maze_occupancy_3x3_ascii_9.txt` | **33.33%** | `input: 193 , ouput: 21` | `down, down, right, right, right, up, right, down, down, right, right` |
| `maze_occupancy_3x3_tokenized_9.txt` | **0.00%** | `input: 743 , ouput: 650` | `right, down, down, down, right, right, down, right, right, right, up, up, up, up, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right` |

---

## Full LLM Responses

### `maze_line_3x3_9.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down
```

**Extracted Answer:**
```
right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='b4ocae7WJLSHkdUPzY3Q8QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=427,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=169
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=434
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=427 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=434 traffic_type=None
```

### `maze_line_3x3_9.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, right, up, right, down, down
```

**Extracted Answer:**
```
down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cIocac68FfPvnsEP6a-L8AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=650,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=650
    ),
  ],
  total_token_count=657
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=185 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=650 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=650
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=657 traffic_type=None
```

### `maze_line_3x3_adj_9.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, right, up, right, down, down
```

**Extracted Answer:**
```
down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cIocaYHnOLrk7M8P0bvv2QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=5,
  prompt_token_count=712,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=712
    ),
  ],
  total_token_count=717
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=5 candidates_tokens_details=None prompt_token_count=712 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=712
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=717 traffic_type=None
```

### `maze_line_3x3_adj_9.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, right, up, right, down, down
```

**Extracted Answer:**
```
down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cYocaZTSFfG4kdUPtcqRwAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=344,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=344
    ),
  ],
  total_token_count=351
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=344 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=344
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=351 traffic_type=None
```

### `maze_line_3x3_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down
```

**Extracted Answer:**
```
right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='coocaeTsBZzo7M8PmunkwAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=5,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=320
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=187 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=5 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=320 traffic_type=None
```

### `maze_occupancy_3x3_9.jpg`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='c4ocaZuGOPDjkdUP2eDb-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=422,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=164
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=443
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=422 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=422 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=164
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=443 traffic_type=None
```

### `maze_occupancy_3x3_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, right, up, right, down, down, right, down, down, left, left, left, left, down, down, right, right, right, right, up, right, right, down, down, down, right, right, right, up, up, up, up, right, down, down, down, right, right, right, up, up, up, right, right, down, down, down, right, right, right, up, up, up, up, up, right, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down, down, down, right, right, right, up, up, up, up, up, up, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,right,up,right,down,down,right,down,down,left,left,left,left,down,down,right,right,right,right,up,right,right,down,down,down,right,right,right,up,up,up,up,right,down,down,down,right,right,right,up,up,up,right,right,down,down,down,right,right,right,up,up,up,up,up,right,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,down,down,right,right,right,up,up,up,up,up,up,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='doocaaC_KLrrkdUP_f6z-QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=465,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=465
    ),
  ],
  total_token_count=1115
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=165 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=465 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=465
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1115 traffic_type=None
```

### `maze_occupancy_3x3_adj_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
the, provided, maze, data, is, an, adjacency, list, representation, of, the, maze., to, solve, the, maze, i, will, use, a, breadth-first, search, (bfs), algorithm., bfs, is, suitable, for, finding, the, shortest, path, in, an, unweighted, graph, which, is, what, this, maze, represents., here's, how, i'll, approach, it:, 1., **parse, the, maze:**, i'll, convert, the, adjacency, list, into, a, more, usable, dictionary, where, keys, are, node, coordinates, (tuples), and, values, are, lists, of, their, neighboring, coordinates., 2., **initialize, bfs:**, *, a, queue, will, store, paths, to, explore., each, element, in, the, queue, will, be, a, tuple:, `(current_node, path_taken_to_reach_it)`., *, a, set, will, keep, track, of, visited, nodes, to, avoid, cycles, and, redundant, exploration., 3., **start, bfs:**, *, add, the, start, node, `(1, 1)`, and, an, empty, path, `[]`, to, the, queue., *, add, the, start, node, `(1, 1)`, to, the, visited, set., 4., **explore:**, *, while, the, queue, is, not, empty:, *, dequeue, the, `(current_node, current_path)`., *, if, `current_node`, is, the, `end`, node, `(5, 5)`, i've, found, the, path., i, will, then, convert, the, `current_path`, (which, is, a, list, of, coordinate, changes), into, the, required, move, sequence, (up, down, left, right)., *, for, each, `neighbor`, of, `current_node`:, *, if, the, `neighbor`, has, not, been, visited:, *, mark, the, `neighbor`, as, visited., *, calculate, the, move, from, `current_node`, to, `neighbor`, (e.g., `(2, 1)`, from, `(1, 1)`, is, a, 'down', move)., *, enqueue, `(neighbor, current_path, +, [move])`., let's, trace, the, path., start:, `[1, 1]`, end:, `[5, 5]`, maze, graph, representation, (derived, from, json):, `{, (1, 1):, [(2, 1)], (1, 3):, [(1, 4), (2, 3)], (1, 4):, [(1, 5), (1, 3)], (1, 5):, [(1, 4), (2, 5)], (2, 1):, [(3, 1), (1, 1)], (2, 3):, [(3, 3), (1, 3)], (2, 5):, [(3, 5), (1, 5)], (3, 1):, [(3, 2), (2, 1)], (3, 2):, [(3, 3), (3, 1)], (3, 3):, [(3, 2)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The provided maze data is an adjacency list representation of the maze. To solve the maze, I will use a Breadth-First Search (BFS) algorithm. BFS is suitable for finding the shortest path in an unweighted graph, which is what this maze represents.

Here's how I'll approach it:

1.  **Parse the Maze:** I'll convert the adjacency list into a more usable dictionary where keys are node coordinates (tuples) and values are lists of their neighboring coordinates.
2.  **Initialize BFS:**
    *   A queue will store paths to explore. Each element in the queue will be a tuple: `(current_node, path_taken_to_reach_it)`.
    *   A set will keep track of visited nodes to avoid cycles and redundant exploration.
3.  **Start BFS:**
    *   Add the start node `(1, 1)` and an empty path `[]` to the queue.
    *   Add the start node `(1, 1)` to the visited set.
4.  **Explore:**
    *   While the queue is not empty:
        *   Dequeue the `(current_node, current_path)`.
        *   If `current_node` is the `end` node `(5, 5)`, I've found the path. I will then convert the `current_path` (which is a list of coordinate changes) into the required move sequence (up, down, left, right).
        *   For each `neighbor` of `current_node`:
            *   If the `neighbor` has not been visited:
                *   Mark the `neighbor` as visited.
                *   Calculate the move from `current_node` to `neighbor` (e.g., `(2, 1)` from `(1, 1)` is a 'down' move).
                *   Enqueue `(neighbor, current_path + [move])`.

Let's trace the path.

Start: `[1, 1]`
End: `[5, 5]`

Maze Graph Representation (derived from JSON):
`{
  (1, 1): [(2, 1)],
  (1, 3): [(1, 4), (2, 3)],
  (1, 4): [(1, 5), (1, 3)],
  (1, 5): [(1, 4), (2, 5)],
  (2, 1): [(3, 1), (1, 1)],
  (2, 3): [(3, 3), (1, 3)],
  (2, 5): [(3, 5), (1, 5)],
  (3, 1): [(3, 2), (2, 1)],
  (3, 2): [(3, 3), (3, 1)],
  (3, 3): [(3, 2),"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eoocabObF7rrkdUP_f6z-QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1174,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1174
    ),
  ],
  total_token_count=1824
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1174 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1174
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1824 traffic_type=None
```

### `maze_occupancy_3x3_adj_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
i, need, to, find, a, path, from, (1, 1), to, (5, 5), in, the, given, 7x7, maze., the, adjacency, list, represents, the, connections, between, cells., i, can, visualize, this, as, a, grid, where, (row, col), represents, a, cell., let's, list, the, connections, and, identify, the, start, and, end, points:, start:, (1, 1), end:, (5, 5), connections:, (1, 1), <->, (2, 1), (1, 3), <->, (1, 4), (1, 3), <->, (2, 3), (1, 4), <->, (1, 5), (1, 5), <->, (2, 5), (2, 1), <->, (3, 1), (2, 3), <->, (3, 3), (2, 5), <->, (3, 5), (3, 1), <->, (3, 2), (3, 2), <->, (3, 3), (3, 5), <->, (4, 5), (4, 5), <->, (5, 5), (5, 1), <->, (5, 2), (5, 2), <->, (5, 3), (5, 3), <->, (5, 4), (5, 4), <->, (5, 5), let's, try, to, trace, a, path, from, (1, 1), to, (5, 5):, 1., start, at, (1, 1)., 2., from, (1, 1), the, only, connection, is, to, (2, 1)., move, down., current, path:, down., current, position:, (2, 1)., 3., from, (2, 1), the, only, connection, is, to, (3, 1)., move, down., current, path:, down, down., current, position:, (3, 1)., 4., from, (3, 1), we, can, go, to, (3, 2)., move, right., current, path:, down, down, right., current, position:, (3, 2)., 5., from, (3, 2), we, can, go, to, (3, 3)., move, right., current, path:, down, down, right, right., current, position:, (3, 3)., 6., from, (3, 3), we, can, go, to, (2, 3)., let's, check, if, this, leads, anywhere, useful., if, we, go, to, (2, 3), then, to, (1, 3), or, (2, 5)., this, seems, to, be, going, away, from, (5, 5)., let's, backtrack, and, explore, other, options, from, (3, 3)., from, (3, 3), we, can, also, go, to, (3, 2), (backtrack), or, (2, 3)., let's, reconsider., let's, retry, systematically, exploring, the, path, to, (5, 5)., start:, (1, 1), possible, moves, from, (1, 1):, (2, 1), path:, (1, 1), ->, (2, 1), move:, down, current, position:, (2
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""I need to find a path from (1,1) to (5,5) in the given 7x7 maze.
The adjacency list represents the connections between cells. I can visualize this as a grid, where (row, col) represents a cell.

Let's list the connections and identify the start and end points:

Start: (1,1)
End: (5,5)

Connections:
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

Let's try to trace a path from (1,1) to (5,5):

1. Start at (1,1).
2. From (1,1), the only connection is to (2,1). Move down. Current path: down. Current position: (2,1).
3. From (2,1), the only connection is to (3,1). Move down. Current path: down, down. Current position: (3,1).
4. From (3,1), we can go to (3,2). Move right. Current path: down, down, right. Current position: (3,2).
5. From (3,2), we can go to (3,3). Move right. Current path: down, down, right, right. Current position: (3,3).
6. From (3,3), we can go to (2,3). Let's check if this leads anywhere useful. If we go to (2,3), then to (1,3) or (2,5). This seems to be going away from (5,5). Let's backtrack and explore other options from (3,3).
    From (3,3), we can also go to (3,2) (backtrack) or (2,3). Let's reconsider.

Let's retry systematically, exploring the path to (5,5).

Start: (1,1)
Possible moves from (1,1): (2,1)
Path: (1,1) -> (2,1)
Move: down

Current position: (2,"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fYocacKvKbfz7M8Pn_rtkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=456,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=456
    ),
  ],
  total_token_count=1106
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=456 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=456
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1106 traffic_type=None
```

### `maze_occupancy_3x3_ascii_9.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, up, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,up,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='foocaaSBJOnd7M8PlPjCwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=193,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=193
    ),
  ],
  total_token_count=214
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=164 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=193 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=193
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=214 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, right, right, right, up, up, up, up, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,down,right,right,right,up,up,up,up,right,right,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gIocaf78L9b6kdUPie_GmQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=743,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=743
    ),
  ],
  total_token_count=1393
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=188 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=743 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=743
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1393 traffic_type=None
```

