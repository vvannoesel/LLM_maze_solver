# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_25.jpg` | **25.00%** | `input: 434 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_25.json` | **100.00%** | `input: 657 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_adj_25.json` | **100.00%** | `input: 719 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_adj_25.txt` | **0.00%** | `input: 351 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_25.txt` | **0.00%** | `input: 322 , ouput: 649` | `the, provided, maze, description, is, a, bit, confusing, and, seems, to, have, some, inconsistencies., the, standard, way, to, represent, a, 3x3, maze, grid, with, walls, and, start/end, points, would, be, to, list, each, cell, and, its, walls., let's, try, to, interpret, the, provided, input, as, clearly, as, possible, to, solve, the, maze:, *, **<|0-0|>, <|uprightleft_wall|>, <|origin|>**:, this, is, cell, (0, 0)., it's, the, origin, (start)., it, has, walls, on, the, up, right, and, left., this, implies, it, only, has, a, path, downwards., *, **<|0-1|>, <|upleft_wall|>**:, this, is, cell, (0, 1)., it, has, a, wall, on, the, up, and, left., this, implies, it, has, paths, down, and, right., *, **<|0-2|>, <|upright_wall|>**:, this, is, cell, (0, 2)., it, has, a, wall, on, the, up, and, right., this, implies, it, has, paths, down, and, left., *, **<|1-0|>, <|rightleft_wall|>**:, this, is, cell, (1, 0)., it, has, walls, on, the, right, and, left., this, implies, it, has, paths, up, and, down., *, **<|1-1|>, <|downrightleft_wall|>**:, this, is, cell, (1, 1)., it, has, walls, on, the, down, right, and, left., this, implies, it, only, has, a, path, upwards., *, **<|1-2|>, <|rightleft_wall|>**:, this, is, cell, (1, 2)., it, has, walls, on, the, right, and, left., this, implies, it, has, paths, up, and, down., *, **<|2-0|>, <|downleft_wall|>**:, this, is, cell, (2, 0)., it, has, walls, on, the, down, and, left., this, implies, it, has, paths, up, and, right., *, **<|2-1|>, <|updown_wall|>**:, this, is, cell, (2, 1)., it, has, walls, on, the, up, and, down., this, implies, it, has, paths, left, and, right., *, **<|2-2|>, <|downright_wall|>, <|target|>**:, this, is, cell, (2, 2)., it's, the, target, (end)., it, has, walls, on, the, down, and, right., this, implies, it, has, paths, up, and, left., let's, map, out, the, traversable, paths, based, on, this, interpretation:, *, **(0, 0)**:, can, only, go, **down**, to, (1, 0)., *, **(1, 0)**:, can, go, **up**, to, (0, 0), or, **down**, to, (2, 0)., *, **(2, 0)**:, can, go, **up**, to, (1, 0), or, **right**, to, (2, 1)., *, **(2, 1)**:, can, go, **left**, to, (2, 0), or, **right**, to, (2, 2)., *, **(2, 2)**:, can, go, **up**, to, (1, 2), or, **left**, to, (2, 1).` |
| `maze_occupancy_3x3_25.jpg` | **12.50%** | `input: 429 , ouput: 27` | `down, right, down, down, right, right, up, right, down, down, left, down, right, right` |
| `maze_occupancy_3x3_25.json` | **12.50%** | `input: 472 , ouput: 21` | `down, right, down, down, down, right, right, right, down, down, right` |
| `maze_occupancy_3x3_adj_25.json` | **110.00%** | `input: 1175 , ouput: 23` | `down, down, down, down, right, right, right, right, up, up, up, up` |
| `maze_occupancy_3x3_adj_25.txt` | **100.00%** | `input: 463 , ouput: 15` | `down, down, down, down, right, right, right, right` |
| `maze_occupancy_3x3_ascii_25.txt` | **37.50%** | `input: 201 , ouput: 35` | `down, down, down, right, right, right, down, down, left, left, left, up, up, up, right, right, down, down` |
| `maze_occupancy_3x3_tokenized_25.txt` | **12.50%** | `input: 750 , ouput: 650` | `down, right, right, right, right, down, down, down, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up` |

---

## Full LLM Responses

### `maze_line_3x3_25.jpg`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8pGVacmUO62xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
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
  total_token_count=441
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=441 traffic_type=None
```

### `maze_line_3x3_25.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='85GVaafoJP367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_25.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9JGVacbyFIOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right
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
        text='right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9JGVaf_rNOTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right
```

**Extracted Answer:**
```
the, provided, maze, description, is, a, bit, confusing, and, seems, to, have, some, inconsistencies., the, standard, way, to, represent, a, 3x3, maze, grid, with, walls, and, start/end, points, would, be, to, list, each, cell, and, its, walls., let's, try, to, interpret, the, provided, input, as, clearly, as, possible, to, solve, the, maze:, *, **<|0-0|>, <|uprightleft_wall|>, <|origin|>**:, this, is, cell, (0, 0)., it's, the, origin, (start)., it, has, walls, on, the, up, right, and, left., this, implies, it, only, has, a, path, downwards., *, **<|0-1|>, <|upleft_wall|>**:, this, is, cell, (0, 1)., it, has, a, wall, on, the, up, and, left., this, implies, it, has, paths, down, and, right., *, **<|0-2|>, <|upright_wall|>**:, this, is, cell, (0, 2)., it, has, a, wall, on, the, up, and, right., this, implies, it, has, paths, down, and, left., *, **<|1-0|>, <|rightleft_wall|>**:, this, is, cell, (1, 0)., it, has, walls, on, the, right, and, left., this, implies, it, has, paths, up, and, down., *, **<|1-1|>, <|downrightleft_wall|>**:, this, is, cell, (1, 1)., it, has, walls, on, the, down, right, and, left., this, implies, it, only, has, a, path, upwards., *, **<|1-2|>, <|rightleft_wall|>**:, this, is, cell, (1, 2)., it, has, walls, on, the, right, and, left., this, implies, it, has, paths, up, and, down., *, **<|2-0|>, <|downleft_wall|>**:, this, is, cell, (2, 0)., it, has, walls, on, the, down, and, left., this, implies, it, has, paths, up, and, right., *, **<|2-1|>, <|updown_wall|>**:, this, is, cell, (2, 1)., it, has, walls, on, the, up, and, down., this, implies, it, has, paths, left, and, right., *, **<|2-2|>, <|downright_wall|>, <|target|>**:, this, is, cell, (2, 2)., it's, the, target, (end)., it, has, walls, on, the, down, and, right., this, implies, it, has, paths, up, and, left., let's, map, out, the, traversable, paths, based, on, this, interpretation:, *, **(0, 0)**:, can, only, go, **down**, to, (1, 0)., *, **(1, 0)**:, can, go, **up**, to, (0, 0), or, **down**, to, (2, 0)., *, **(2, 0)**:, can, go, **up**, to, (1, 0), or, **right**, to, (2, 1)., *, **(2, 1)**:, can, go, **left**, to, (2, 0), or, **right**, to, (2, 2)., *, **(2, 2)**:, can, go, **up**, to, (1, 2), or, **left**, to, (2, 1).
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The provided maze description is a bit confusing and seems to have some inconsistencies. The standard way to represent a 3x3 maze grid with walls and start/end points would be to list each cell and its walls.

Let's try to interpret the provided input as clearly as possible to solve the maze:

*   **<|0-0|> <|uprightleft_wall|> <|origin|>**: This is cell (0,0). It's the origin (start). It has walls on the up, right, and left. This implies it only has a path downwards.
*   **<|0-1|> <|upleft_wall|>**: This is cell (0,1). It has a wall on the up and left. This implies it has paths down and right.
*   **<|0-2|> <|upright_wall|>**: This is cell (0,2). It has a wall on the up and right. This implies it has paths down and left.
*   **<|1-0|> <|rightleft_wall|>**: This is cell (1,0). It has walls on the right and left. This implies it has paths up and down.
*   **<|1-1|> <|downrightleft_wall|>**: This is cell (1,1). It has walls on the down, right, and left. This implies it only has a path upwards.
*   **<|1-2|> <|rightleft_wall|>**: This is cell (1,2). It has walls on the right and left. This implies it has paths up and down.
*   **<|2-0|> <|downleft_wall|>**: This is cell (2,0). It has walls on the down and left. This implies it has paths up and right.
*   **<|2-1|> <|updown_wall|>**: This is cell (2,1). It has walls on the up and down. This implies it has paths left and right.
*   **<|2-2|> <|downright_wall|> <|target|>**: This is cell (2,2). It's the target (end). It has walls on the down and right. This implies it has paths up and left.

Let's map out the traversable paths based on this interpretation:

*   **(0,0)**: Can only go **down** to (1,0).
*   **(1,0)**: Can go **up** to (0,0) or **down** to (2,0).
*   **(2,0)**: Can go **up** to (1,0) or **right** to (2,1).
*   **(2,1)**: Can go **left** to (2,0) or **right** to (2,2).
*   **(2,2)**: Can go **up** to (1,2) or **left** to (2,1).

"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='95GVafaKDtihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=649,
  prompt_token_count=322,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=322
    ),
  ],
  total_token_count=971
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=649 candidates_tokens_details=None prompt_token_count=322 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=322
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=971 traffic_type=None
```

### `maze_occupancy_3x3_25.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, right, down, down, right, right, up, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,down,right,right,up,right,down,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-JGVacLjA5jknsEPxt7C0AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
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
  total_token_count=456
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=456 traffic_type=None
```

### `maze_occupancy_3x3_25.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, right, down, down, down, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,down,down,right,right,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-JGVabu-MfKcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=472,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=472
    ),
  ],
  total_token_count=493
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=472 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=472
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=493 traffic_type=None
```

### `maze_occupancy_3x3_adj_25.json`

**Score:** 110.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, right, right, right, right, up, up, up, up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-ZGVaYm6I9qgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=1175,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1175
    ),
  ],
  total_token_count=1198
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=1175 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1175
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1198 traffic_type=None
```

### `maze_occupancy_3x3_adj_25.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-pGVadzVBOyOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=463,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=463
    ),
  ],
  total_token_count=478
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=463 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=463
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=478 traffic_type=None
```

### `maze_occupancy_3x3_ascii_25.txt`

**Score:** 37.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, down, left, left, left, up, up, up, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,right,down,down,left,left,left,up,up,up,right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-5GVacu1A6vgnsEP8Mu7uAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=201,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=201
    ),
  ],
  total_token_count=236
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=201 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=201
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=236 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_25.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, right, down, down, down, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,down,down,down,down,right,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,up,up,up,right,right,down,down,down,down,right,right,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_JGVaeLcItWbkdUPueCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=750,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=750
    ),
  ],
  total_token_count=1400
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=750 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=750
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1400 traffic_type=None
```

