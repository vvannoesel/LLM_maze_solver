# LLM Maze Solving Comparison Report

 NEW ASCII

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_3.jpg` | **50.00%** | `input: 421 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_3.json` | **100.00%** | `input: 644 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_adj_3.json` | **100.00%** | `input: 706 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_adj_3.txt` | **0.00%** | `input: 338 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_tokenized_3.txt` | **0.00%** | `input: 309 , ouput: 5` | `right, down, right` |
| `maze_occupancy_3x3_3.jpg` | **12.50%** | `input: 416 , ouput: 15` | `down, right, down, right, down, right, down, right` |
| `maze_occupancy_3x3_3.json` | **0.00%** | `input: 459 , ouput: 45` | `right, down, down, right, right, right, down, down, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right` |
| `maze_occupancy_3x3_adj_3.json` | **75.00%** | `input: 1168 , ouput: 21` | `down, down, right, right, right, right, right, down, down, down, down` |
| `maze_occupancy_3x3_adj_3.txt` | **0.00%** | `input: 450 , ouput: 1734` | `the, provided, adjacency, list, represents, a, 7x7, maze., let's, convert, it, into, a, more, usable, format, marking, the, start, and, end, points., the, grid, coordinates, are, (row, column), starting, from, (0, 0), at, the, top-left., **maze, representation:**, *, **start:**, (1, 1), *, **end:**, (5, 5), **adjacency, list, breakdown:**, *, (1, 1), is, connected, to, (2, 1), *, (1, 3), is, connected, to, (1, 4), *, (1, 4), is, connected, to, (1, 3), and, (1, 5), *, (1, 5), is, connected, to, (1, 4), and, (2, 5), *, (2, 1), is, connected, to, (1, 1), and, (3, 1), *, (2, 5), is, connected, to, (1, 5), and, (3, 5), *, (3, 1), is, connected, to, (2, 1), and, (3, 2), *, (3, 2), is, connected, to, (3, 1), and, (3, 3), *, (3, 3), is, connected, to, (3, 2), and, (3, 4), *, (3, 4), is, connected, to, (3, 3), and, (3, 5), *, (3, 5), is, connected, to, (3, 4), and, (2, 5), and, (4, 5), *, (4, 5), is, connected, to, (3, 5), and, (5, 5), *, (5, 1), is, connected, to, (5, 2), *, (5, 2), is, connected, to, (5, 1), and, (5, 3), *, (5, 3), is, connected, to, (5, 2), and, (5, 4), *, (5, 4), is, connected, to, (5, 3), and, (5, 5), *, (5, 5), is, connected, to, (4, 5), and, (5, 4), **pathfinding, (breadth-first, search, -, bfs):**, we, will, use, bfs, to, find, the, shortest, path., 1., **start, at, (1, 1).**, 2., possible, moves, from, (1, 1):, (2, 1), *, path:, (1, 1), ->, (2, 1), 3., from, (2, 1), possible, moves:, (1, 1), (already, visited), (3, 1), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), 4., from, (3, 1), possible, moves:, (2, 1), (visited), (3, 2), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), 5., from, (3, 2), possible, moves:, (3, 1), (visited), (3, 3), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), 6., from, (3, 3), possible, moves:, (3, 2), (visited), (3, 4), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), 7., from, (3, 4), possible, moves:, (3, 3), (visited), (3, 5), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), 8., from, (3, 5), possible, moves:, (3, 4), (visited), (2, 5), (4, 5), *, let's, explore, (2, 5), first., *, path, to, (2, 5):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), *, from, (2, 5), possible, moves:, (3, 5), (visited), (1, 5), *, path, to, (1, 5):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), ->, (1, 5), *, from, (1, 5), possible, moves:, (2, 5), (visited), (1, 4), *, path, to, (1, 4):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), ->, (1, 5), ->, (1, 4), *, from, (1, 4), possible, moves:, (1, 5), (visited), (1, 3), *, path, to, (1, 3):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), ->, (1, 5), ->, (1, 4), ->, (1, 3), *, this, path, is, getting, long, and, doesn't, seem, to, lead, to, (5, 5), easily., let's, backtrack, to, step, 7, and, explore, (4, 5), from, (3, 5)., *, **back, to, step, 7:**, from, (3, 5), possible, moves:, (3, 4), (visited), (2, 5), (4, 5)., we, chose, (2, 5), last, time., let's, choose, (4, 5)., *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), 9., from, (4, 5), possible, moves:, (3, 5), (visited), (5, 5), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), ->, (5, 5), we, have, reached, the, target, (5, 5)., now, let's, convert, this, path, to, moves., we, need, to, map, coordinate, changes, to, directions., remember, that, row, increases, downwards, and, column, increases, to, the, right., *, (1, 1), to, (2, 1):, down, (row, increases, by, 1, column, stays, the, same), *, (2, 1), to, (3, 1):, down, (row, increases, by, 1, column, stays, the, same), *, (3, 1), to, (3, 2):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 2), to, (3, 3):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 3), to, (3, 4):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 4), to, (3, 5):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 5), to, (4, 5):, down, (row, increases, by, 1, column, stays, the, same), *, (4, 5), to, (5, 5):, down, (row, increases, by, 1, column, stays, the, same), down, down, right, right, right, right, down, down` |
| `maze_occupancy_3x3_ascii_3.txt` | **0.00%** | `input: 185 , ouput: 43` | `right, right, down, down, right, down, down, left, left, down, right, right, right, up, up, right, up, up, up, left, left, left` |
| `maze_occupancy_3x3_tokenized_3.txt` | **0.00%** | `input: 738 , ouput: 4000` | `right, down, right, down, right, right, right, down, down, left, down, right, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right` |

---

## Full LLM Responses

### `maze_line_3x3_3.jpg`

**Score:** 50.00%

**Ground Truth Solution:**
```
down, right, right, down
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
        text='down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i7kVaaSkKK7CvdIP1pDPQA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=421,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=163
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=428
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=421 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=421 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=163
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=428 traffic_type=None
```

### `maze_line_3x3_3.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jLkVafXtDL3WvdIP05-s2AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=644,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=644
    ),
  ],
  total_token_count=651
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=179 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=644 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=644
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=651 traffic_type=None
```

### `maze_line_3x3_adj_3.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jLkVaf3TKamuxN8PmKHSYQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=706,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=706
    ),
  ],
  total_token_count=713
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=150 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=706 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=706
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=713 traffic_type=None
```

### `maze_line_3x3_adj_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, down
```

**Extracted Answer:**
```
right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jbkVacaiCPKUvdIPs5-MoAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=338,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=338
    ),
  ],
  total_token_count=345
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=183 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=338 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=338
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=345 traffic_type=None
```

### `maze_line_3x3_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jbkVacOALbrbvdIP4O7N2QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=5,
  prompt_token_count=309,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=309
    ),
  ],
  total_token_count=314
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=181 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=5 candidates_tokens_details=None prompt_token_count=309 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=309
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=314 traffic_type=None
```

### `maze_occupancy_3x3_3.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j7kVabaeGc-XvdIPiY6XgAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=416,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=158
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=431
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=416 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=416 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=158
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=431 traffic_type=None
```

### `maze_occupancy_3x3_3.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, down, down, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,down,down,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kLkVaY-hB52_vdIP-9fMgQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=459,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=459
    ),
  ],
  total_token_count=504
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=159 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=459 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=459
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=504 traffic_type=None
```

### `maze_occupancy_3x3_adj_3.json`

**Score:** 75.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, right, right, right, down, down, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kLkVaeyGJ8Lbxs0Psc7RUQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1168,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1168
    ),
  ],
  total_token_count=1189
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=150 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1168 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1168
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1189 traffic_type=None
```

### `maze_occupancy_3x3_adj_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
the, provided, adjacency, list, represents, a, 7x7, maze., let's, convert, it, into, a, more, usable, format, marking, the, start, and, end, points., the, grid, coordinates, are, (row, column), starting, from, (0, 0), at, the, top-left., **maze, representation:**, *, **start:**, (1, 1), *, **end:**, (5, 5), **adjacency, list, breakdown:**, *, (1, 1), is, connected, to, (2, 1), *, (1, 3), is, connected, to, (1, 4), *, (1, 4), is, connected, to, (1, 3), and, (1, 5), *, (1, 5), is, connected, to, (1, 4), and, (2, 5), *, (2, 1), is, connected, to, (1, 1), and, (3, 1), *, (2, 5), is, connected, to, (1, 5), and, (3, 5), *, (3, 1), is, connected, to, (2, 1), and, (3, 2), *, (3, 2), is, connected, to, (3, 1), and, (3, 3), *, (3, 3), is, connected, to, (3, 2), and, (3, 4), *, (3, 4), is, connected, to, (3, 3), and, (3, 5), *, (3, 5), is, connected, to, (3, 4), and, (2, 5), and, (4, 5), *, (4, 5), is, connected, to, (3, 5), and, (5, 5), *, (5, 1), is, connected, to, (5, 2), *, (5, 2), is, connected, to, (5, 1), and, (5, 3), *, (5, 3), is, connected, to, (5, 2), and, (5, 4), *, (5, 4), is, connected, to, (5, 3), and, (5, 5), *, (5, 5), is, connected, to, (4, 5), and, (5, 4), **pathfinding, (breadth-first, search, -, bfs):**, we, will, use, bfs, to, find, the, shortest, path., 1., **start, at, (1, 1).**, 2., possible, moves, from, (1, 1):, (2, 1), *, path:, (1, 1), ->, (2, 1), 3., from, (2, 1), possible, moves:, (1, 1), (already, visited), (3, 1), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), 4., from, (3, 1), possible, moves:, (2, 1), (visited), (3, 2), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), 5., from, (3, 2), possible, moves:, (3, 1), (visited), (3, 3), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), 6., from, (3, 3), possible, moves:, (3, 2), (visited), (3, 4), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), 7., from, (3, 4), possible, moves:, (3, 3), (visited), (3, 5), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), 8., from, (3, 5), possible, moves:, (3, 4), (visited), (2, 5), (4, 5), *, let's, explore, (2, 5), first., *, path, to, (2, 5):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), *, from, (2, 5), possible, moves:, (3, 5), (visited), (1, 5), *, path, to, (1, 5):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), ->, (1, 5), *, from, (1, 5), possible, moves:, (2, 5), (visited), (1, 4), *, path, to, (1, 4):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), ->, (1, 5), ->, (1, 4), *, from, (1, 4), possible, moves:, (1, 5), (visited), (1, 3), *, path, to, (1, 3):, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (2, 5), ->, (1, 5), ->, (1, 4), ->, (1, 3), *, this, path, is, getting, long, and, doesn't, seem, to, lead, to, (5, 5), easily., let's, backtrack, to, step, 7, and, explore, (4, 5), from, (3, 5)., *, **back, to, step, 7:**, from, (3, 5), possible, moves:, (3, 4), (visited), (2, 5), (4, 5)., we, chose, (2, 5), last, time., let's, choose, (4, 5)., *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), 9., from, (4, 5), possible, moves:, (3, 5), (visited), (5, 5), *, path:, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), ->, (5, 5), we, have, reached, the, target, (5, 5)., now, let's, convert, this, path, to, moves., we, need, to, map, coordinate, changes, to, directions., remember, that, row, increases, downwards, and, column, increases, to, the, right., *, (1, 1), to, (2, 1):, down, (row, increases, by, 1, column, stays, the, same), *, (2, 1), to, (3, 1):, down, (row, increases, by, 1, column, stays, the, same), *, (3, 1), to, (3, 2):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 2), to, (3, 3):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 3), to, (3, 4):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 4), to, (3, 5):, right, (row, stays, the, same, column, increases, by, 1), *, (3, 5), to, (4, 5):, down, (row, increases, by, 1, column, stays, the, same), *, (4, 5), to, (5, 5):, down, (row, increases, by, 1, column, stays, the, same), down, down, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The provided adjacency list represents a 7x7 maze. Let's convert it into a more usable format, marking the start and end points. The grid coordinates are (row, column) starting from (0,0) at the top-left.

**Maze Representation:**

*   **Start:** (1,1)
*   **End:** (5,5)

**Adjacency List Breakdown:**

*   (1,1) is connected to (2,1)
*   (1,3) is connected to (1,4)
*   (1,4) is connected to (1,3) and (1,5)
*   (1,5) is connected to (1,4) and (2,5)
*   (2,1) is connected to (1,1) and (3,1)
*   (2,5) is connected to (1,5) and (3,5)
*   (3,1) is connected to (2,1) and (3,2)
*   (3,2) is connected to (3,1) and (3,3)
*   (3,3) is connected to (3,2) and (3,4)
*   (3,4) is connected to (3,3) and (3,5)
*   (3,5) is connected to (3,4) and (2,5) and (4,5)
*   (4,5) is connected to (3,5) and (5,5)
*   (5,1) is connected to (5,2)
*   (5,2) is connected to (5,1) and (5,3)
*   (5,3) is connected to (5,2) and (5,4)
*   (5,4) is connected to (5,3) and (5,5)
*   (5,5) is connected to (4,5) and (5,4)

**Pathfinding (Breadth-First Search - BFS):**

We will use BFS to find the shortest path.

1.  **Start at (1,1).**
2.  Possible moves from (1,1): (2,1)
    *   Path: (1,1) -> (2,1)
3.  From (2,1), possible moves: (1,1) (already visited), (3,1)
    *   Path: (1,1) -> (2,1) -> (3,1)
4.  From (3,1), possible moves: (2,1) (visited), (3,2)
    *   Path: (1,1) -> (2,1) -> (3,1) -> (3,2)
5.  From (3,2), possible moves: (3,1) (visited), (3,3)
    *   Path: (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3)
6.  From (3,3), possible moves: (3,2) (visited), (3,4)
    *   Path: (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4)
7.  From (3,4), possible moves: (3,3) (visited), (3,5)
    *   Path: (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5)
8.  From (3,5), possible moves: (3,4) (visited), (2,5), (4,5)
    *   Let's explore (2,5) first.
    *   Path to (2,5): (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (2,5)
    *   From (2,5), possible moves: (3,5) (visited), (1,5)
    *   Path to (1,5): (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (2,5) -> (1,5)
    *   From (1,5), possible moves: (2,5) (visited), (1,4)
    *   Path to (1,4): (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (2,5) -> (1,5) -> (1,4)
    *   From (1,4), possible moves: (1,5) (visited), (1,3)
    *   Path to (1,3): (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (2,5) -> (1,5) -> (1,4) -> (1,3)
    *   This path is getting long and doesn't seem to lead to (5,5) easily. Let's backtrack to step 7 and explore (4,5) from (3,5).

    *   **Back to step 7:** From (3,5), possible moves: (3,4) (visited), (2,5), (4,5). We chose (2,5) last time. Let's choose (4,5).
    *   Path: (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (4,5)
9.  From (4,5), possible moves: (3,5) (visited), (5,5)
    *   Path: (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (4,5) -> (5,5)

We have reached the target (5,5). Now let's convert this path to moves. We need to map coordinate changes to directions. Remember that row increases downwards, and column increases to the right.

*   (1,1) to (2,1): Down (Row increases by 1, Column stays the same)
*   (2,1) to (3,1): Down (Row increases by 1, Column stays the same)
*   (3,1) to (3,2): Right (Row stays the same, Column increases by 1)
*   (3,2) to (3,3): Right (Row stays the same, Column increases by 1)
*   (3,3) to (3,4): Right (Row stays the same, Column increases by 1)
*   (3,4) to (3,5): Right (Row stays the same, Column increases by 1)
*   (3,5) to (4,5): Down (Row increases by 1, Column stays the same)
*   (4,5) to (5,5): Down (Row increases by 1, Column stays the same)

down,down,right,right,right,right,down,down"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lLkVaZr7HYf0xs0P8ZPLEQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=1734,
  prompt_token_count=450,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=450
    ),
  ],
  total_token_count=2184
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=183 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=1734 candidates_tokens_details=None prompt_token_count=450 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=450
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2184 traffic_type=None
```

### `maze_occupancy_3x3_ascii_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, down, left, left, down, right, right, right, up, up, right, up, up, up, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,down,left,left,down,right,right,right,up,up,right,up,up,up,left,left,left'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lbkVafu6B9y_vdIPyqna8Qw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=185,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=185
    ),
  ],
  total_token_count=228
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=158 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=185 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=185
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=228 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, right, right, down, down, left, down, right, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, right, right, down, down, left, down, right, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right, right, down, down, left, left, left, down, right, right, down, down, left, left, left, up, up, up, up, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nrkVaYHeHce_vdIPl9bb-Aw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=4000,
  prompt_token_count=738,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=738
    ),
  ],
  total_token_count=4738
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=183 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=4000 candidates_tokens_details=None prompt_token_count=738 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=738
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4738 traffic_type=None
```

