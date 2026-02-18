# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_46.jpg` | **3.85%** | `input: 434 , ouput: 21` | `down, down, right, down, right, right, up, right, down, down, right` |
| `maze_line_6x6_46.json` | **3.85%** | `input: 1809 , ouput: 19` | `down, down, right, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_46.json` | **3.85%** | `input: 2258 , ouput: 23` | `down, down, right, right, down, down, right, right, down, down, right, right` |
| `maze_line_6x6_adj_46.txt` | **0.00%** | `input: 729 , ouput: 23` | `right, right, right, down, right, down, right, down, down, right, right, right` |
| `maze_line_6x6_tokenized_46.txt` | **0.00%** | `input: 673 , ouput: 650` | `the, maze, is, 6x6., the, origin, is, at, (0, 0), and, the, target, is, at, (5, 5)., let's, represent, the, maze, as, a, grid, and, mark, the, walls., (0, 0), is, origin, has, up, right, left, walls., this, means, we, can, only, go, down, from, (0, 0)., (0, 1), has, up, down, left, walls., from, (0, 0), down, to, (1, 0)., then, from, (1, 0), we, can, go, right, to, (1, 1)., (1, 0), has, down, left, walls., from, (0, 0), down, to, (1, 0)., (1, 1), has, up, right, walls., from, (1, 0), right, to, (1, 1)., (1, 2), has, up, left, walls., from, (1, 1), right, to, (1, 2)., (1, 3), has, down, right, walls., from, (1, 2), right, to, (1, 3)., (1, 4), has, up, left, walls., from, (1, 3), right, to, (1, 4)., (1, 5), has, down, right, walls., from, (1, 4), right, to, (1, 5)., (2, 0), has, up, left, walls., from, (1, 0), down, to, (2, 0)., (2, 1), has, down, right, walls., from, (2, 0), right, to, (2, 1)., (2, 2), has, right, left, walls., from, (2, 1), right, to, (2, 2)., (2, 3), has, up, right, left, walls., from, (2, 2), right, to, (2, 3)., (2, 4), has, down, left, walls., from, (2, 3), right, to, (2, 4)., (2, 5), has, up, right, walls., from, (2, 4), right, to, (2, 5)., (3, 0), has, right, left, walls., from, (2, 0), down, to, (3, 0)., (3, 1), has, up, down, left, walls., from, (3, 0), right, to, (3, 1)., (3, 2), has, right, wall., from, (3, 1), right, to, (3, 2)., (3, 3), has, left, wall., from, (3, 2), right, to, (3, 3)., (3, 4), has, up, down, right, walls., from, (3, 3), right, to, (3, 4)., (3, 5), has, right, left, walls., from, (3, 4), right, to, (3, 5)., (4, 0), has, down, left, walls., from, (3, 0), down, to, (4, 0)., (4, 1), has, up, down, walls., from, (4, 0), right, to, (4, 1)., (4, 2), has, down, right, walls., from, (4, 1), right, to, (4, 2)., (4, 3), has` |
| `maze_occupancy_6x6_46.jpg` | **0.00%** | `input: 431 , ouput: 25` | `right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_46.json` | **0.00%** | `input: 988 , ouput: 650` | `right, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_46.json` | **3.85%** | `input: 4335 , ouput: 63` | `down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_46.txt` | **11.54%** | `input: 1273 , ouput: 650` | `down, down, right, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down` |
| `maze_occupancy_6x6_ascii_46.txt` | **0.00%** | `input: 244 , ouput: 141` | `right, right, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_46.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_46.jpg`

**Score:** 3.85%

**Ground Truth Solution:**
```
down, right, down, left, down, down, right, right, up, up, up, right, up, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, down, right, down, right, right, up, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, right, up, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OoWVaeGUMoOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
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
  total_token_count=455
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=455 traffic_type=None
```

### `maze_line_6x6_46.json`

**Score:** 3.85%

**Ground Truth Solution:**
```
down, right, down, left, down, down, right, right, up, up, up, right, up, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='O4WVac25Jv7MkdUP7NXHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1828
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1828 traffic_type=None
```

### `maze_line_6x6_adj_46.json`

**Score:** 3.85%

**Ground Truth Solution:**
```
down, right, down, left, down, down, right, right, up, up, up, right, up, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, down, right, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='PIWVaevfDoKN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2281
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2281 traffic_type=None
```

### `maze_line_6x6_adj_46.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, left, down, down, right, right, up, up, up, right, up, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, right, right, down, right, down, right, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,down,right,down,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='PYWVafQ62p-ewQ-8_I3IAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=752
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=752 traffic_type=None
```

### `maze_line_6x6_tokenized_46.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, left, down, down, right, right, up, up, up, right, up, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
the, maze, is, 6x6., the, origin, is, at, (0, 0), and, the, target, is, at, (5, 5)., let's, represent, the, maze, as, a, grid, and, mark, the, walls., (0, 0), is, origin, has, up, right, left, walls., this, means, we, can, only, go, down, from, (0, 0)., (0, 1), has, up, down, left, walls., from, (0, 0), down, to, (1, 0)., then, from, (1, 0), we, can, go, right, to, (1, 1)., (1, 0), has, down, left, walls., from, (0, 0), down, to, (1, 0)., (1, 1), has, up, right, walls., from, (1, 0), right, to, (1, 1)., (1, 2), has, up, left, walls., from, (1, 1), right, to, (1, 2)., (1, 3), has, down, right, walls., from, (1, 2), right, to, (1, 3)., (1, 4), has, up, left, walls., from, (1, 3), right, to, (1, 4)., (1, 5), has, down, right, walls., from, (1, 4), right, to, (1, 5)., (2, 0), has, up, left, walls., from, (1, 0), down, to, (2, 0)., (2, 1), has, down, right, walls., from, (2, 0), right, to, (2, 1)., (2, 2), has, right, left, walls., from, (2, 1), right, to, (2, 2)., (2, 3), has, up, right, left, walls., from, (2, 2), right, to, (2, 3)., (2, 4), has, down, left, walls., from, (2, 3), right, to, (2, 4)., (2, 5), has, up, right, walls., from, (2, 4), right, to, (2, 5)., (3, 0), has, right, left, walls., from, (2, 0), down, to, (3, 0)., (3, 1), has, up, down, left, walls., from, (3, 0), right, to, (3, 1)., (3, 2), has, right, wall., from, (3, 1), right, to, (3, 2)., (3, 3), has, left, wall., from, (3, 2), right, to, (3, 3)., (3, 4), has, up, down, right, walls., from, (3, 3), right, to, (3, 4)., (3, 5), has, right, left, walls., from, (3, 4), right, to, (3, 5)., (4, 0), has, down, left, walls., from, (3, 0), down, to, (4, 0)., (4, 1), has, up, down, walls., from, (4, 0), right, to, (4, 1)., (4, 2), has, down, right, walls., from, (4, 1), right, to, (4, 2)., (4, 3), has
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is 6x6. The origin is at (0,0) and the target is at (5,5).

Let's represent the maze as a grid and mark the walls.

(0,0) is origin, has up, right, left walls. This means we can only go down from (0,0).
(0,1) has up, down, left walls. From (0,0) down to (1,0). Then from (1,0) we can go right to (1,1).
(1,0) has down, left walls. From (0,0) down to (1,0).
(1,1) has up, right walls. From (1,0) right to (1,1).
(1,2) has up, left walls. From (1,1) right to (1,2).
(1,3) has down, right walls. From (1,2) right to (1,3).
(1,4) has up, left walls. From (1,3) right to (1,4).
(1,5) has down, right walls. From (1,4) right to (1,5).
(2,0) has up, left walls. From (1,0) down to (2,0).
(2,1) has down, right walls. From (2,0) right to (2,1).
(2,2) has right, left walls. From (2,1) right to (2,2).
(2,3) has up, right, left walls. From (2,2) right to (2,3).
(2,4) has down, left walls. From (2,3) right to (2,4).
(2,5) has up, right walls. From (2,4) right to (2,5).
(3,0) has right, left walls. From (2,0) down to (3,0).
(3,1) has up, down, left walls. From (3,0) right to (3,1).
(3,2) has right wall. From (3,1) right to (3,2).
(3,3) has left wall. From (3,2) right to (3,3).
(3,4) has up, down, right walls. From (3,3) right to (3,4).
(3,5) has right, left walls. From (3,4) right to (3,5).
(4,0) has down, left walls. From (3,0) down to (4,0).
(4,1) has up, down walls. From (4,0) right to (4,1).
(4,2) has down, right walls. From (4,1) right to (4,2).
(4,3) has"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='P4WVaY7BBuyOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=1323
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1323 traffic_type=None
```

### `maze_occupancy_6x6_46.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QIWVaemNBY65kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=431,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=173
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=456
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=431 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=456 traffic_type=None
```

### `maze_occupancy_6x6_46.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QYWVaf7_HrnjnsEPxoKX6AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1638
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=174 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1638 traffic_type=None
```

### `maze_occupancy_6x6_adj_46.json`

**Score:** 3.85%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QoWVafTNFvfo7M8PiZSSoQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=63,
  prompt_token_count=4335,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4335
    ),
  ],
  total_token_count=4398
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=63 candidates_tokens_details=None prompt_token_count=4335 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4335
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4398 traffic_type=None
```

### `maze_occupancy_6x6_adj_46.txt`

**Score:** 11.54%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RIWVaYXUJtHMkdUPjY-7sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1273,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1273
    ),
  ],
  total_token_count=1923
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=198 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1273 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1273
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1923 traffic_type=None
```

### `maze_occupancy_6x6_ascii_46.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RYWVabr1KMjl7M8P9OOViAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=141,
  prompt_token_count=244,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=244
    ),
  ],
  total_token_count=385
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=173 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=141 candidates_tokens_details=None prompt_token_count=244 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=244
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=385 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_46.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R4WVadebE4DHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2812
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=197 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2812 traffic_type=None
```

