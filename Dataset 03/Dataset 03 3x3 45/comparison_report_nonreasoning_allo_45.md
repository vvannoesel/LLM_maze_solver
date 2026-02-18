# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_45.jpg` | **0.00%** | `input: 434 , ouput: 9` | `down, right, right, down, right` |
| `maze_line_3x3_45.json` | **0.00%** | `input: 657 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_45.json` | **100.00%** | `input: 719 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_adj_45.txt` | **100.00%** | `input: 351 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_tokenized_45.txt` | **0.00%** | `input: 322 , ouput: 366` | `here's, how, to, interpret, the, maze, and, find, the, path:, *, **maze, grid:**, *, (0, 0):, start, only, has, a, wall, on, the, left., this, means, we, can, move, right, or, down., *, (0, 1):, has, walls, up, and, down., we, can, only, move, left, or, right., *, (0, 2):, has, walls, up, and, right., we, can, move, left, or, down., *, (1, 0):, has, walls, up, and, left., we, can, move, right, or, down., *, (1, 1):, has, walls, up, down, and, right., we, can, only, move, left., *, (1, 2):, has, walls, right, and, left., we, can, only, move, up, or, down., *, (2, 0):, has, walls, down, and, left., we, can, move, up, or, right., *, (2, 1):, has, walls, up, and, down., we, can, only, move, left, or, right., *, (2, 2):, end, has, walls, down, and, right., we, can, move, up, or, left., *, **pathfinding:**, 1., from, (0, 0), we, must, move, right, to, (0, 1), as, there's, no, wall, to, the, right., 2., from, (0, 1), we, must, move, right, to, (0, 2), as, there's, no, wall, to, the, right., 3., from, (0, 2), we, can, move, down, to, (1, 2), as, there's, no, wall, down., 4., from, (1, 2), we, can, move, down, to, (2, 2), as, there's, no, wall, down., right, right, down, down` |
| `maze_occupancy_3x3_45.jpg` | **25.00%** | `input: 429 , ouput: 43` | `right, right, down, right, down, down, left, down, right, right, up, right, down, down, left, left, left, up, up, right, right, down` |
| `maze_occupancy_3x3_45.json` | **75.00%** | `input: 472 , ouput: 23` | `right, right, right, right, down, down, right, down, down, down, right, right` |
| `maze_occupancy_3x3_adj_45.json` | **110.00%** | `input: 1175 , ouput: 19` | `right, right, right, right, down, down, down, down, right, right` |
| `maze_occupancy_3x3_adj_45.txt` | **75.00%** | `input: 463 , ouput: 23` | `right, right, right, right, down, down, right, down, down, right, right, right` |
| `maze_occupancy_3x3_ascii_45.txt` | **87.50%** | `input: 198 , ouput: 25` | `right, right, right, right, down, down, down, left, left, down, right, right, right` |
| `maze_occupancy_3x3_tokenized_45.txt` | **110.00%** | `input: 750 , ouput: 31` | `right, right, right, right, down, down, down, down, left, left, left, down, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_3x3_45.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
```

**Extracted Answer:**
```
down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4ZOVacWIOqS1xN8P7ILa-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=9,
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
  total_token_count=443
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=9 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=443 traffic_type=None
```

### `maze_line_3x3_45.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4pOVabeZKpuZ28oPi9qtsAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_45.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='45OVaeisHpuZ28oPjdqtsAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_45.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, right, down, down
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
        text='right, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5JOVaej_Eeb1xN8PzZ3x8QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_45.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
```

**Extracted Answer:**
```
here's, how, to, interpret, the, maze, and, find, the, path:, *, **maze, grid:**, *, (0, 0):, start, only, has, a, wall, on, the, left., this, means, we, can, move, right, or, down., *, (0, 1):, has, walls, up, and, down., we, can, only, move, left, or, right., *, (0, 2):, has, walls, up, and, right., we, can, move, left, or, down., *, (1, 0):, has, walls, up, and, left., we, can, move, right, or, down., *, (1, 1):, has, walls, up, down, and, right., we, can, only, move, left., *, (1, 2):, has, walls, right, and, left., we, can, only, move, up, or, down., *, (2, 0):, has, walls, down, and, left., we, can, move, up, or, right., *, (2, 1):, has, walls, up, and, down., we, can, only, move, left, or, right., *, (2, 2):, end, has, walls, down, and, right., we, can, move, up, or, left., *, **pathfinding:**, 1., from, (0, 0), we, must, move, right, to, (0, 1), as, there's, no, wall, to, the, right., 2., from, (0, 1), we, must, move, right, to, (0, 2), as, there's, no, wall, to, the, right., 3., from, (0, 2), we, can, move, down, to, (1, 2), as, there's, no, wall, down., 4., from, (1, 2), we, can, move, down, to, (2, 2), as, there's, no, wall, down., right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""Here's how to interpret the maze and find the path:

*   **Maze Grid:**
    *   (0,0): Start, only has a wall on the left. This means we can move right or down.
    *   (0,1): Has walls up and down. We can only move left or right.
    *   (0,2): Has walls up and right. We can move left or down.
    *   (1,0): Has walls up and left. We can move right or down.
    *   (1,1): Has walls up, down, and right. We can only move left.
    *   (1,2): Has walls right and left. We can only move up or down.
    *   (2,0): Has walls down and left. We can move up or right.
    *   (2,1): Has walls up and down. We can only move left or right.
    *   (2,2): End, has walls down and right. We can move up or left.

*   **Pathfinding:**
    1.  From (0,0), we must move right to (0,1) as there's no wall to the right.
    2.  From (0,1), we must move right to (0,2) as there's no wall to the right.
    3.  From (0,2), we can move down to (1,2) as there's no wall down.
    4.  From (1,2), we can move down to (2,2) as there's no wall down.

right, right, down, down"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5pOVaYr_Ipy8xN8Pl5eC0Aw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=366,
  prompt_token_count=322,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=322
    ),
  ],
  total_token_count=688
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=366 candidates_tokens_details=None prompt_token_count=322 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=322
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=688 traffic_type=None
```

### `maze_occupancy_3x3_45.jpg`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, down, left, down, right, right, up, right, down, down, left, left, left, up, up, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,left,down,right,right,up,right,down,down,left,left,left,up,up,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6JOVacT8Ddrbxs0P1qTOyAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
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
  total_token_count=472
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=472 traffic_type=None
```

### `maze_occupancy_3x3_45.json`

**Score:** 75.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6ZOVaYDWDLPUvdIPgaLC6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=472,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=472
    ),
  ],
  total_token_count=495
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=472 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=472
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=495 traffic_type=None
```

### `maze_occupancy_3x3_adj_45.json`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6pOVabGdHIjyxs0PwJ_VyQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1175,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1175
    ),
  ],
  total_token_count=1194
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1175 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1175
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1194 traffic_type=None
```

### `maze_occupancy_3x3_adj_45.txt`

**Score:** 75.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,down,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='65OVadqMCIjyxs0PwJ_VyQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=463,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=463
    ),
  ],
  total_token_count=486
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=463 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=463
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=486 traffic_type=None
```

### `maze_occupancy_3x3_ascii_45.txt`

**Score:** 87.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, left, left, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,left,left,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='65OVad7xLbT4xs0P_M6xgA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=198,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=198
    ),
  ],
  total_token_count=223
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=198 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=198
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=223 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_45.txt`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, left, left, left, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,left,left,left,down,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7JOVabvuIIjyxs0PwJ_VyQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=750,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=750
    ),
  ],
  total_token_count=781
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=750 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=750
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=781 traffic_type=None
```

