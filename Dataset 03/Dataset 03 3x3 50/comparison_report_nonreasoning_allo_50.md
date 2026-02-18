# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_50.jpg` | **50.00%** | `input: 434 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_50.json` | **100.00%** | `input: 657 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_50.json` | **100.00%** | `input: 719 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_50.txt` | **0.00%** | `input: 351 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_50.txt` | **0.00%** | `input: 322 , ouput: 650` | `the, maze, description, provided, is, a, bit, unusual, with, `<|updownleft_wall|>`, etc., i, will, interpret, these, as, walls, in, a, standard, grid., let's, visualize, the, 3x3, maze., cells, are, described, by, their, walls., (0, 0):, `<|origin|>`, -, this, cell, has, walls, that, are, not, explicitly, listed, but, it's, the, origin., let's, assume, it, has, walls, described, by, the, surrounding, cells., (0, 1):, `<|uprightleft_wall|>`, -, this, cell, has, a, wall, to, its, right, and, left, and, potentially, up., since, it's, in, the, top, row, 'up', is, an, edge., (0, 2):, `<|upright_wall|>`, -, this, cell, has, a, wall, to, its, right, and, potentially, up., since, it's, in, the, top, row, 'up', is, an, edge., (1, 0):, `<|downleft_wall|>`, -, this, cell, has, a, wall, to, its, left, and, down., (1, 1):, `<|upright_wall|>`, -, this, cell, has, a, wall, to, its, right, and, up., (1, 2):, `<|rightleft_wall|>`, -, this, cell, has, walls, to, its, right, and, left., (2, 0):, `<|updownleft_wall|>`, -, this, cell, has, a, wall, to, its, left, and, down, and, potentially, up., since, it's, in, the, bottom, row, 'down', is, an, edge., (2, 1):, `<|down_wall|>`, -, this, cell, has, a, wall, down., (2, 2):, `<|downright_wall|>`, -, this, cell, has, walls, down, and, to, its, right., this, is, also, the, `<|target|>`., let's, reconstruct, the, walls, between, cells:, (0, 0), origin, (0, 1), has, wall, left, (to, 0, 0), and, right, (to, 0, 2)., (0, 2), has, wall, left, (to, 0, 1), and, right, (edge)., (1, 0), has, wall, left, (edge), and, down, (to, 2, 0)., (1, 1), has, wall, up, (to, 0, 1), and, right, (to, 1, 2)., (1, 2), has, wall, left, (to, 1, 1), and, right, (edge)., (2, 0), has, wall, left, (edge), and, down, (edge)., (2, 1), has, wall, down, (edge)., (2, 2), target, has, wall, down, (edge), and, right, (edge)., let's, refine, the, wall, interpretation, based, on, the, descriptions:, *, **<|0-0|>, <|uprightleft_wall|>, <|origin|>**, *, this, is, (0, 0)., the, description, `<|uprightleft_wall|>`, is, confusing, here, as, it's, the, origin., let's, assume, the, surrounding, cells', descriptions, define, its, walls., *, **<|0-1|>, <|updownleft_wall|>**, *, this, is, (0, 1` |
| `maze_occupancy_3x3_50.jpg` | **12.50%** | `input: 429 , ouput: 19` | `down, right, down, down, right, right, up, right, down, down` |
| `maze_occupancy_3x3_50.json` | **12.50%** | `input: 472 , ouput: 27` | `down, right, down, down, right, right, up, right, down, down, right, right, down, right` |
| `maze_occupancy_3x3_adj_50.json` | **62.50%** | `input: 1175 , ouput: 19` | `down, down, right, right, down, right, down, right, down, right` |
| `maze_occupancy_3x3_adj_50.txt` | **25.00%** | `input: 463 , ouput: 15` | `down, down, down, right, right, down, right, right` |
| `maze_occupancy_3x3_ascii_50.txt` | **0.00%** | `input: 200 , ouput: 27` | `right, right, down, left, left, down, right, right, right, down, left, down, right, right` |
| `maze_occupancy_3x3_tokenized_50.txt` | **0.00%** | `input: 750 , ouput: 169` | `right, down, down, right, down, down, right, right, down, right, up, right, up, up, up, up, right, right, right, down, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up` |

---

## Full LLM Responses

### `maze_line_3x3_50.jpg`

**Score:** 50.00%

**Ground Truth Solution:**
```
down, right, down, right
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
        text='down, right, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-JSVacrhHazd7M8PqdSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_50.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
down, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-ZSVaeetEY-VkdUPpZbhqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_50.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
down, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-pSVaaGlDbW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-pSVaZjmNL-fkdUPtcm3yAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, right
```

**Extracted Answer:**
```
the, maze, description, provided, is, a, bit, unusual, with, `<|updownleft_wall|>`, etc., i, will, interpret, these, as, walls, in, a, standard, grid., let's, visualize, the, 3x3, maze., cells, are, described, by, their, walls., (0, 0):, `<|origin|>`, -, this, cell, has, walls, that, are, not, explicitly, listed, but, it's, the, origin., let's, assume, it, has, walls, described, by, the, surrounding, cells., (0, 1):, `<|uprightleft_wall|>`, -, this, cell, has, a, wall, to, its, right, and, left, and, potentially, up., since, it's, in, the, top, row, 'up', is, an, edge., (0, 2):, `<|upright_wall|>`, -, this, cell, has, a, wall, to, its, right, and, potentially, up., since, it's, in, the, top, row, 'up', is, an, edge., (1, 0):, `<|downleft_wall|>`, -, this, cell, has, a, wall, to, its, left, and, down., (1, 1):, `<|upright_wall|>`, -, this, cell, has, a, wall, to, its, right, and, up., (1, 2):, `<|rightleft_wall|>`, -, this, cell, has, walls, to, its, right, and, left., (2, 0):, `<|updownleft_wall|>`, -, this, cell, has, a, wall, to, its, left, and, down, and, potentially, up., since, it's, in, the, bottom, row, 'down', is, an, edge., (2, 1):, `<|down_wall|>`, -, this, cell, has, a, wall, down., (2, 2):, `<|downright_wall|>`, -, this, cell, has, walls, down, and, to, its, right., this, is, also, the, `<|target|>`., let's, reconstruct, the, walls, between, cells:, (0, 0), origin, (0, 1), has, wall, left, (to, 0, 0), and, right, (to, 0, 2)., (0, 2), has, wall, left, (to, 0, 1), and, right, (edge)., (1, 0), has, wall, left, (edge), and, down, (to, 2, 0)., (1, 1), has, wall, up, (to, 0, 1), and, right, (to, 1, 2)., (1, 2), has, wall, left, (to, 1, 1), and, right, (edge)., (2, 0), has, wall, left, (edge), and, down, (edge)., (2, 1), has, wall, down, (edge)., (2, 2), target, has, wall, down, (edge), and, right, (edge)., let's, refine, the, wall, interpretation, based, on, the, descriptions:, *, **<|0-0|>, <|uprightleft_wall|>, <|origin|>**, *, this, is, (0, 0)., the, description, `<|uprightleft_wall|>`, is, confusing, here, as, it's, the, origin., let's, assume, the, surrounding, cells', descriptions, define, its, walls., *, **<|0-1|>, <|updownleft_wall|>**, *, this, is, (0, 1
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze description provided is a bit unusual with `<|updownleft_wall|>` etc. I will interpret these as walls in a standard grid.
Let's visualize the 3x3 maze.

Cells are described by their walls.
(0,0): `<|origin|>` - This cell has walls that are not explicitly listed, but it's the origin. Let's assume it has walls described by the surrounding cells.
(0,1): `<|uprightleft_wall|>` - This cell has a wall to its right and left, and potentially up. Since it's in the top row, 'up' is an edge.
(0,2): `<|upright_wall|>` - This cell has a wall to its right and potentially up. Since it's in the top row, 'up' is an edge.
(1,0): `<|downleft_wall|>` - This cell has a wall to its left and down.
(1,1): `<|upright_wall|>` - This cell has a wall to its right and up.
(1,2): `<|rightleft_wall|>` - This cell has walls to its right and left.
(2,0): `<|updownleft_wall|>` - This cell has a wall to its left and down, and potentially up. Since it's in the bottom row, 'down' is an edge.
(2,1): `<|down_wall|>` - This cell has a wall down.
(2,2): `<|downright_wall|>` - This cell has walls down and to its right. This is also the `<|target|>`.

Let's reconstruct the walls between cells:

(0,0) Origin
(0,1) Has wall left (to 0,0) and right (to 0,2).
(0,2) Has wall left (to 0,1) and right (edge).
(1,0) Has wall left (edge) and down (to 2,0).
(1,1) Has wall up (to 0,1) and right (to 1,2).
(1,2) Has wall left (to 1,1) and right (edge).
(2,0) Has wall left (edge) and down (edge).
(2,1) Has wall down (edge).
(2,2) Target has wall down (edge) and right (edge).

Let's refine the wall interpretation based on the descriptions:

*   **<|0-0|> <|uprightleft_wall|> <|origin|>**
    *   This is (0,0). The description `<|uprightleft_wall|>` is confusing here, as it's the origin. Let's assume the surrounding cells' descriptions define its walls.

*   **<|0-1|> <|updownleft_wall|>**
    *   This is (0,1"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_ZSVaZ_kN465kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_50.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_5SVaeU_8Obszw-ju87pBQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
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
  total_token_count=448
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=448 traffic_type=None
```

### `maze_occupancy_3x3_50.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, right, down, down, right, right, up, right, down, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,down,right,right,up,right,down,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AJWVaejHLKzd7M8PqdSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_50.json`

**Score:** 62.50%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AZWVaZjPF5Hw7M8Pi4iBgAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_50.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, right, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ApWVaYjOB4-VkdUPpZbhqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, left, left, down, right, right, right, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,left,left,down,right,right,right,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ApWVafrnNNqfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=200,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=200
    ),
  ],
  total_token_count=227
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=200 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=200
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=227 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, down, down, right, right, down, right, up, right, up, up, up, up, right, right, right, down, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, down, down, right, right, down, right, up, right, up, up, up, up, right, right, right, down, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up, right, down, down, down, right, right, right, up, right, up, up, up, up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='A5WVaY7yLvDm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=169,
  prompt_token_count=750,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=750
    ),
  ],
  total_token_count=919
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=169 candidates_tokens_details=None prompt_token_count=750 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=750
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=919 traffic_type=None
```

