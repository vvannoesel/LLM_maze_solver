# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_32.jpg` | **0.00%** | `input: 434 , ouput: 460` | `the, maze, can, be, represented, as, a, 3x3, grid., the, start, (circle), is, in, cell, (0, 0)., the, end, (star), is, in, cell, (2, 2)., let's, analyze, the, possible, moves, from, each, cell., from, (0, 0):, -, down:, possible, moves, to, (1, 0)., -, right:, blocked, by, a, wall., from, (1, 0):, -, up:, possible, moves, to, (0, 0)., -, down:, possible, moves, to, (2, 0)., -, right:, blocked, by, a, wall., from, (2, 0):, -, up:, possible, moves, to, (1, 0)., -, right:, possible, moves, to, (2, 1)., from, (2, 1):, -, left:, possible, moves, to, (2, 0)., -, down:, blocked, by, a, wall., -, right:, possible, moves, to, (2, 2)., from, (2, 2), (end)., now, let's, find, a, path, from, (0, 0), to, (2, 2)., one, possible, path, is:, (0, 0), ->, down, ->, (1, 0), (1, 0), ->, down, ->, (2, 0), (2, 0), ->, right, ->, (2, 1), (2, 1), ->, right, ->, (2, 2), this, translates, to, the, moves:, down, down, right, right., let's, confirm, there, are, no, other, obvious, paths, that, might, be, shorter, although, in, this, small, maze, this, path, appears, to, be, the, most, direct., from, (0, 0), the, only, way, to, move, is, down., from, (1, 0), we, can, go, down, or, back, up., to, reach, the, star, we, must, move, away, from, (0, 0), so, down., from, (2, 0), we, can, go, right, or, back, up., to, reach, the, star, we, must, go, right., from, (2, 1), we, can, go, right, or, back, left., to, reach, the, star, we, must, go, right., therefore, the, path, found, is, a, valid, and, direct, path., down, down, right, right` |
| `maze_line_3x3_32.json` | **50.00%** | `input: 657 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_adj_32.json` | **50.00%** | `input: 719 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_adj_32.txt` | **50.00%** | `input: 351 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_tokenized_32.txt` | **0.00%** | `input: 322 , ouput: 650` | `let's, analyze, the, maze, and, find, a, path., the, maze, is, a, 3x3, grid., the, cells, are, described, by, their, walls, and, whether, they, are, the, start, or, end., here's, a, breakdown, of, the, cells, and, their, connections:, *, **(0, 0), <|origin|>**:, walls:, up, right, left., this, means, the, only, possible, move, from, (0, 0), is, down, to, (1, 0)., *, **(0, 1)**:, walls:, up, down, left., this, cell, is, connected, to, (0, 0), (left, wall, is, missing, but, (0, 0), has, a, right, wall), and, (0, 2), (right, wall, is, missing)., *, **(0, 2)**:, walls:, up, right., this, cell, is, connected, to, (0, 1), (left, wall, is, missing)., *, **(1, 0)**:, walls:, right, left., this, cell, is, connected, to, (0, 0), (down, wall, is, missing, but, (0, 0), has, an, up, wall), and, (2, 0), (down, wall, is, missing)., *, **(1, 1)**:, walls:, up, left., this, cell, is, connected, to, (1, 0), (right, wall, is, missing, but, (1, 0), has, a, left, wall), (1, 2), (right, wall, is, missing), and, (2, 1), (down, wall, is, missing)., *, **(1, 2)**:, walls:, right., this, cell, is, connected, to, (1, 1), (left, wall, is, missing), and, (2, 2), (down, wall, is, missing)., *, **(2, 0)**:, walls:, down, left., this, cell, is, connected, to, (1, 0), (up, wall, is, missing)., *, **(2, 1)**:, walls:, down, right., this, cell, is, connected, to, (1, 1), (up, wall, is, missing), and, (2, 0), (left, wall, is, missing), and, (2, 2), (right, wall, is, missing)., *, **(2, 2), <|target|:**, walls:, down, right, left., this, cell, is, connected, to, (1, 2), (up, wall, is, missing), and, (2, 1), (right, wall, is, missing)., let's, trace, a, path:, 1., **start, at, (0, 0)**., the, only, exit, is, down, to, (1, 0)., **move:, down**, 2., **from, (1, 0)**., we, can, go, left, (blocked, by, maze, edge, also, (2, 0), has, a, left, wall), or, down, to, (2, 0)., **move:, down**, 3., **from, (2, 0)**., we, can, go, up, to, (1, 0), (already, visited), or, right, to, (2, 1)., **move:, right**, 4., **from, (2, 1)**., we, can, go, up, to, (1, 1), or, left, to, (2, 0), (already, visited), or, right, to, (2, 2)., **move:, right**, 5., **from, (` |
| `maze_occupancy_3x3_32.jpg` | **16.67%** | `input: 429 , ouput: 17` | `down, down, right, right, right, up, right, down, down` |
| `maze_occupancy_3x3_32.json` | **8.33%** | `input: 472 , ouput: 27` | `down, right, down, right, down, right, down, right, up, right, right, down, down, right` |
| `maze_occupancy_3x3_adj_32.json` | **25.00%** | `input: 1175 , ouput: 17` | `down, down, down, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_32.txt` | **0.00%** | `input: 463 , ouput: 19` | `right, down, down, down, right, right, up, right, down, down` |
| `maze_occupancy_3x3_ascii_32.txt` | **0.00%** | `input: 202 , ouput: 37` | `right, down, right, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right` |
| `maze_occupancy_3x3_tokenized_32.txt` | **0.00%** | `input: 750 , ouput: 49` | `right, down, right, down, right, down, right, down, left, down, left, down, left, right, right, right, up, right, up, right, up, up, up, up, up` |

---

## Full LLM Responses

### `maze_line_3x3_32.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, right, down
```

**Extracted Answer:**
```
the, maze, can, be, represented, as, a, 3x3, grid., the, start, (circle), is, in, cell, (0, 0)., the, end, (star), is, in, cell, (2, 2)., let's, analyze, the, possible, moves, from, each, cell., from, (0, 0):, -, down:, possible, moves, to, (1, 0)., -, right:, blocked, by, a, wall., from, (1, 0):, -, up:, possible, moves, to, (0, 0)., -, down:, possible, moves, to, (2, 0)., -, right:, blocked, by, a, wall., from, (2, 0):, -, up:, possible, moves, to, (1, 0)., -, right:, possible, moves, to, (2, 1)., from, (2, 1):, -, left:, possible, moves, to, (2, 0)., -, down:, blocked, by, a, wall., -, right:, possible, moves, to, (2, 2)., from, (2, 2), (end)., now, let's, find, a, path, from, (0, 0), to, (2, 2)., one, possible, path, is:, (0, 0), ->, down, ->, (1, 0), (1, 0), ->, down, ->, (2, 0), (2, 0), ->, right, ->, (2, 1), (2, 1), ->, right, ->, (2, 2), this, translates, to, the, moves:, down, down, right, right., let's, confirm, there, are, no, other, obvious, paths, that, might, be, shorter, although, in, this, small, maze, this, path, appears, to, be, the, most, direct., from, (0, 0), the, only, way, to, move, is, down., from, (1, 0), we, can, go, down, or, back, up., to, reach, the, star, we, must, move, away, from, (0, 0), so, down., from, (2, 0), we, can, go, right, or, back, up., to, reach, the, star, we, must, go, right., from, (2, 1), we, can, go, right, or, back, left., to, reach, the, star, we, must, go, right., therefore, the, path, found, is, a, valid, and, direct, path., down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze can be represented as a 3x3 grid.
The start (circle) is in cell (0,0).
The end (star) is in cell (2,2).

Let's analyze the possible moves from each cell.

From (0,0):
- Down: Possible, moves to (1,0).
- Right: Blocked by a wall.

From (1,0):
- Up: Possible, moves to (0,0).
- Down: Possible, moves to (2,0).
- Right: Blocked by a wall.

From (2,0):
- Up: Possible, moves to (1,0).
- Right: Possible, moves to (2,1).

From (2,1):
- Left: Possible, moves to (2,0).
- Down: Blocked by a wall.
- Right: Possible, moves to (2,2).

From (2,2) (End).

Now, let's find a path from (0,0) to (2,2).

One possible path is:
(0,0) -> Down -> (1,0)
(1,0) -> Down -> (2,0)
(2,0) -> Right -> (2,1)
(2,1) -> Right -> (2,2)

This translates to the moves: down, down, right, right.

Let's confirm there are no other obvious paths that might be shorter, although in this small maze, this path appears to be the most direct.

From (0,0), the only way to move is down.
From (1,0), we can go down or back up. To reach the star, we must move away from (0,0), so down.
From (2,0), we can go right or back up. To reach the star, we must go right.
From (2,1), we can go right or back left. To reach the star, we must go right.

Therefore, the path found is a valid and direct path.

down,down,right,right"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hZKVaa3rFZnqkdUP3rjkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=460,
  prompt_token_count=434,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=176
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=894
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=434 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=460 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=894 traffic_type=None
```

### `maze_line_3x3_32.json`

**Score:** 50.00%

**Ground Truth Solution:**
```
down, down, right, up, right, down
```

**Extracted Answer:**
```
down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hpKVadz1A5nqkdUP3rjkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=657,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=657
    ),
  ],
  total_token_count=664
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=192 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=657 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=657
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=664 traffic_type=None
```

### `maze_line_3x3_adj_32.json`

**Score:** 50.00%

**Ground Truth Solution:**
```
down, down, right, up, right, down
```

**Extracted Answer:**
```
down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hpKVaY-oKvDm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=719,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=719
    ),
  ],
  total_token_count=726
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=163 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=719 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=719
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=726 traffic_type=None
```

### `maze_line_3x3_adj_32.txt`

**Score:** 50.00%

**Ground Truth Solution:**
```
down, down, right, up, right, down
```

**Extracted Answer:**
```
down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='h5KVacaoFuKAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=351,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=351
    ),
  ],
  total_token_count=358
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=196 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=351 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=351
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=358 traffic_type=None
```

### `maze_line_3x3_tokenized_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, right, down
```

**Extracted Answer:**
```
let's, analyze, the, maze, and, find, a, path., the, maze, is, a, 3x3, grid., the, cells, are, described, by, their, walls, and, whether, they, are, the, start, or, end., here's, a, breakdown, of, the, cells, and, their, connections:, *, **(0, 0), <|origin|>**:, walls:, up, right, left., this, means, the, only, possible, move, from, (0, 0), is, down, to, (1, 0)., *, **(0, 1)**:, walls:, up, down, left., this, cell, is, connected, to, (0, 0), (left, wall, is, missing, but, (0, 0), has, a, right, wall), and, (0, 2), (right, wall, is, missing)., *, **(0, 2)**:, walls:, up, right., this, cell, is, connected, to, (0, 1), (left, wall, is, missing)., *, **(1, 0)**:, walls:, right, left., this, cell, is, connected, to, (0, 0), (down, wall, is, missing, but, (0, 0), has, an, up, wall), and, (2, 0), (down, wall, is, missing)., *, **(1, 1)**:, walls:, up, left., this, cell, is, connected, to, (1, 0), (right, wall, is, missing, but, (1, 0), has, a, left, wall), (1, 2), (right, wall, is, missing), and, (2, 1), (down, wall, is, missing)., *, **(1, 2)**:, walls:, right., this, cell, is, connected, to, (1, 1), (left, wall, is, missing), and, (2, 2), (down, wall, is, missing)., *, **(2, 0)**:, walls:, down, left., this, cell, is, connected, to, (1, 0), (up, wall, is, missing)., *, **(2, 1)**:, walls:, down, right., this, cell, is, connected, to, (1, 1), (up, wall, is, missing), and, (2, 0), (left, wall, is, missing), and, (2, 2), (right, wall, is, missing)., *, **(2, 2), <|target|:**, walls:, down, right, left., this, cell, is, connected, to, (1, 2), (up, wall, is, missing), and, (2, 1), (right, wall, is, missing)., let's, trace, a, path:, 1., **start, at, (0, 0)**., the, only, exit, is, down, to, (1, 0)., **move:, down**, 2., **from, (1, 0)**., we, can, go, left, (blocked, by, maze, edge, also, (2, 0), has, a, left, wall), or, down, to, (2, 0)., **move:, down**, 3., **from, (2, 0)**., we, can, go, up, to, (1, 0), (already, visited), or, right, to, (2, 1)., **move:, right**, 4., **from, (2, 1)**., we, can, go, up, to, (1, 1), or, left, to, (2, 0), (already, visited), or, right, to, (2, 2)., **move:, right**, 5., **from, (
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""Let's analyze the maze and find a path.

The maze is a 3x3 grid. The cells are described by their walls and whether they are the start or end.

Here's a breakdown of the cells and their connections:

*   **(0,0) <|origin|>**: Walls: up, right, left. This means the only possible move from (0,0) is down to (1,0).
*   **(0,1)**: Walls: up, down, left. This cell is connected to (0,0) (left wall is missing, but (0,0) has a right wall) and (0,2) (right wall is missing).
*   **(0,2)**: Walls: up, right. This cell is connected to (0,1) (left wall is missing).
*   **(1,0)**: Walls: right, left. This cell is connected to (0,0) (down wall is missing, but (0,0) has an up wall) and (2,0) (down wall is missing).
*   **(1,1)**: Walls: up, left. This cell is connected to (1,0) (right wall is missing, but (1,0) has a left wall), (1,2) (right wall is missing), and (2,1) (down wall is missing).
*   **(1,2)**: Walls: right. This cell is connected to (1,1) (left wall is missing) and (2,2) (down wall is missing).
*   **(2,0)**: Walls: down, left. This cell is connected to (1,0) (up wall is missing).
*   **(2,1)**: Walls: down, right. This cell is connected to (1,1) (up wall is missing) and (2,0) (left wall is missing) and (2,2) (right wall is missing).
*   **(2,2) <|target|:** Walls: down, right, left. This cell is connected to (1,2) (up wall is missing) and (2,1) (right wall is missing).

Let's trace a path:

1.  **Start at (0,0)**. The only exit is down to (1,0). **Move: down**
2.  **From (1,0)**. We can go left (blocked by maze edge, also (2,0) has a left wall), or down to (2,0). **Move: down**
3.  **From (2,0)**. We can go up to (1,0) (already visited), or right to (2,1). **Move: right**
4.  **From (2,1)**. We can go up to (1,1), or left to (2,0) (already visited), or right to (2,2). **Move: right**
5.  **From ("""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iZKVaaj2E62WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=322,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=322
    ),
  ],
  total_token_count=972
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=194 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=322 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=322
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=972 traffic_type=None
```

### `maze_occupancy_3x3_32.jpg`

**Score:** 16.67%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ipKVaZGwEqzu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=429,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=171
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=446
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=429 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=446 traffic_type=None
```

### `maze_occupancy_3x3_32.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,up,right,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ipKVad6AN4KN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=472,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=472
    ),
  ],
  total_token_count=499
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=172 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=472 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=472
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=499 traffic_type=None
```

### `maze_occupancy_3x3_adj_32.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i5KVaf-sIaOF7M8P9PzH6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=1175,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1175
    ),
  ],
  total_token_count=1192
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=163 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=1175 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1175
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1192 traffic_type=None
```

### `maze_occupancy_3x3_adj_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jJKVaa-dFIOH7M8PxuqcmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=463,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=463
    ),
  ],
  total_token_count=482
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=196 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=463 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=463
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=482 traffic_type=None
```

### `maze_occupancy_3x3_ascii_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,down,left,down,right,right,up,right,down,down,left,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jZKVacbjBavgnsEP8Mu7uAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=202,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=202
    ),
  ],
  total_token_count=239
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=171 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=202 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=202
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=239 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, left, down, left, right, right, right, up, right, up, right, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,left,down,left,right,right,right,up,right,up,right,up,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jZKVadudKaeN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=750,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=750
    ),
  ],
  total_token_count=799
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=195 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=750 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=750
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=799 traffic_type=None
```

