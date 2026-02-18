# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_39.jpg` | **0.00%** | `input: 434 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_39.json` | **0.00%** | `input: 657 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_39.json` | **100.00%** | `input: 719 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_adj_39.txt` | **100.00%** | `input: 351 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_tokenized_39.txt` | **0.00%** | `input: 322 , ouput: 650` | `the, maze, provided, is, a, bit, complex, to, interpret, directly, with, the, wall, notation, given., let's, break, down, the, maze, structure, assuming, the, notation, describes, the, walls, *surrounding*, each, cell., the, maze, is, 3x3., cells:, (0, 0), <|updownleft_wall|>, <|origin|>, -, this, cell, has, walls, to, the, up, down, and, left., this, means, it, can, only, connect, to, the, right., (0, 1), <|updown_wall|>, -, this, cell, has, walls, to, the, up, and, down., it, can, connect, to, the, left, and, right., (0, 2), <|upright_wall|>, -, this, cell, has, walls, to, the, up, and, right., it, can, connect, to, the, left, and, down., (1, 0), <|upleft_wall|>, -, this, cell, has, walls, to, the, up, and, left., it, can, connect, to, the, right, and, down., (1, 1), <|upright_wall|>, -, this, cell, has, walls, to, the, up, and, right., it, can, connect, to, the, left, and, down., (1, 2), <|rightleft_wall|>, -, this, cell, has, walls, to, the, right, and, left., it, can, connect, to, the, up, and, down., (2, 0), <|downrightleft_wall|>, -, this, cell, has, walls, to, the, down, right, and, left., it, can, connect, to, the, up., (2, 1), <|downleft_wall|>, -, this, cell, has, walls, to, the, down, and, left., it, can, connect, to, the, up, and, right., (2, 2), <|downright_wall|>, <|target|>, -, this, cell, has, walls, to, the, down, and, right., it, can, connect, to, the, up, and, left., let's, re-evaluate, the, connectivity, based, on, this, interpretation:, **origin, (0, 0):**, -, walls:, up, down, left., -, possible, move:, right, to, (0, 1)., **cell, (0, 1):**, -, walls:, up, down., -, possible, moves:, left, to, (0, 0), right, to, (0, 2)., **cell, (0, 2):**, -, walls:, up, right., -, possible, moves:, left, to, (0, 1), down, to, (1, 2)., **cell, (1, 0):**, -, walls:, up, left., -, possible, moves:, right, to, (1, 1), down, to, (2, 0)., **cell, (1, 1):**, -, walls:, up, right., -, possible, moves:, left, to, (1, 0), down, to, (2, 1)., **cell, (1, 2):**, -, walls:, right, left., -, possible, moves:, up, to, (0, 2), down, to, (2, 2)., **cell, (2, 0):**, -, walls:, down, right, left., -, possible, moves:, up, to, (1, 0)., **cell, (2, 1):**, -, walls:, down, left., -, possible, moves:, up, to, (1, 1), right, to, (2` |
| `maze_occupancy_3x3_39.jpg` | **12.50%** | `input: 429 , ouput: 31` | `right, down, down, right, right, down, down, left, down, left, up, left, down, right, right, down` |
| `maze_occupancy_3x3_39.json` | **87.50%** | `input: 472 , ouput: 23` | `right, right, right, right, down, down, down, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_39.json` | **110.00%** | `input: 1175 , ouput: 19` | `right, right, right, right, down, down, down, down, right, right` |
| `maze_occupancy_3x3_adj_39.txt` | **0.00%** | `input: 463 , ouput: 21` | `up, right, right, right, right, down, down, down, down, right, right` |
| `maze_occupancy_3x3_ascii_39.txt` | **0.00%** | `input: 200 , ouput: 23` | `down, down, right, right, right, right, up, up, right, down, down, down` |
| `maze_occupancy_3x3_tokenized_39.txt` | **110.00%** | `input: 750 , ouput: 21` | `right, right, right, right, down, down, down, down, down, right, right` |

---

## Full LLM Responses

### `maze_line_3x3_39.jpg`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iZOVaY_OJeW1vdIPpY7RsQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_39.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ipOVaZz9G8n7vdIP_oGtyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_39.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ipOVadj3O8zXvdIPq7fiiAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_39.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i5OVadD6Jvbzxs0P0ID50Aw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
```

**Extracted Answer:**
```
the, maze, provided, is, a, bit, complex, to, interpret, directly, with, the, wall, notation, given., let's, break, down, the, maze, structure, assuming, the, notation, describes, the, walls, *surrounding*, each, cell., the, maze, is, 3x3., cells:, (0, 0), <|updownleft_wall|>, <|origin|>, -, this, cell, has, walls, to, the, up, down, and, left., this, means, it, can, only, connect, to, the, right., (0, 1), <|updown_wall|>, -, this, cell, has, walls, to, the, up, and, down., it, can, connect, to, the, left, and, right., (0, 2), <|upright_wall|>, -, this, cell, has, walls, to, the, up, and, right., it, can, connect, to, the, left, and, down., (1, 0), <|upleft_wall|>, -, this, cell, has, walls, to, the, up, and, left., it, can, connect, to, the, right, and, down., (1, 1), <|upright_wall|>, -, this, cell, has, walls, to, the, up, and, right., it, can, connect, to, the, left, and, down., (1, 2), <|rightleft_wall|>, -, this, cell, has, walls, to, the, right, and, left., it, can, connect, to, the, up, and, down., (2, 0), <|downrightleft_wall|>, -, this, cell, has, walls, to, the, down, right, and, left., it, can, connect, to, the, up., (2, 1), <|downleft_wall|>, -, this, cell, has, walls, to, the, down, and, left., it, can, connect, to, the, up, and, right., (2, 2), <|downright_wall|>, <|target|>, -, this, cell, has, walls, to, the, down, and, right., it, can, connect, to, the, up, and, left., let's, re-evaluate, the, connectivity, based, on, this, interpretation:, **origin, (0, 0):**, -, walls:, up, down, left., -, possible, move:, right, to, (0, 1)., **cell, (0, 1):**, -, walls:, up, down., -, possible, moves:, left, to, (0, 0), right, to, (0, 2)., **cell, (0, 2):**, -, walls:, up, right., -, possible, moves:, left, to, (0, 1), down, to, (1, 2)., **cell, (1, 0):**, -, walls:, up, left., -, possible, moves:, right, to, (1, 1), down, to, (2, 0)., **cell, (1, 1):**, -, walls:, up, right., -, possible, moves:, left, to, (1, 0), down, to, (2, 1)., **cell, (1, 2):**, -, walls:, right, left., -, possible, moves:, up, to, (0, 2), down, to, (2, 2)., **cell, (2, 0):**, -, walls:, down, right, left., -, possible, moves:, up, to, (1, 0)., **cell, (2, 1):**, -, walls:, down, left., -, possible, moves:, up, to, (1, 1), right, to, (2
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze provided is a bit complex to interpret directly with the wall notation given. Let's break down the maze structure assuming the notation describes the walls *surrounding* each cell.

The maze is 3x3.
Cells:
(0,0) <|updownleft_wall|> <|origin|> - This cell has walls to the up, down, and left. This means it can only connect to the right.
(0,1) <|updown_wall|> - This cell has walls to the up and down. It can connect to the left and right.
(0,2) <|upright_wall|> - This cell has walls to the up and right. It can connect to the left and down.

(1,0) <|upleft_wall|> - This cell has walls to the up and left. It can connect to the right and down.
(1,1) <|upright_wall|> - This cell has walls to the up and right. It can connect to the left and down.
(1,2) <|rightleft_wall|> - This cell has walls to the right and left. It can connect to the up and down.

(2,0) <|downrightleft_wall|> - This cell has walls to the down, right, and left. It can connect to the up.
(2,1) <|downleft_wall|> - This cell has walls to the down and left. It can connect to the up and right.
(2,2) <|downright_wall|> <|target|> - This cell has walls to the down and right. It can connect to the up and left.

Let's re-evaluate the connectivity based on this interpretation:

**Origin (0,0):**
- Walls: Up, Down, Left.
- Possible move: Right to (0,1).

**Cell (0,1):**
- Walls: Up, Down.
- Possible moves: Left to (0,0), Right to (0,2).

**Cell (0,2):**
- Walls: Up, Right.
- Possible moves: Left to (0,1), Down to (1,2).

**Cell (1,0):**
- Walls: Up, Left.
- Possible moves: Right to (1,1), Down to (2,0).

**Cell (1,1):**
- Walls: Up, Right.
- Possible moves: Left to (1,0), Down to (2,1).

**Cell (1,2):**
- Walls: Right, Left.
- Possible moves: Up to (0,2), Down to (2,2).

**Cell (2,0):**
- Walls: Down, Right, Left.
- Possible moves: Up to (1,0).

**Cell (2,1):**
- Walls: Down, Left.
- Possible moves: Up to (1,1), Right to (2"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jpOVac7wB7PUvdIPi6LC6QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_39.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, left, down, left, up, left, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, right, down, down, left, down, left, up, left, down, right, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j5OVacflF8_c28oPsY6G4AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
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
  total_token_count=460
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=460 traffic_type=None
```

### `maze_occupancy_3x3_39.json`

**Score:** 87.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j5OVaeaPO8HWxs0PwvX2iQ4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_39.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kZOVadvgC7nwxN8P8smN8QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
up, right, right, right, right, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='up,right,right,right,right,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kZOVafaUOYbIvdIPqfe6oAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=463,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=463
    ),
  ],
  total_token_count=484
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=463 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=463
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=484 traffic_type=None
```

### `maze_occupancy_3x3_ascii_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, up, up, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,up,up,right,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kpOVaf-BLsTdvdIPxenY-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=200,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=200
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=200 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=200
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=223 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_39.txt`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k5OVadHrM6nFvdIP2N2Q8Qc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=750,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=750
    ),
  ],
  total_token_count=771
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=750 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=750
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=771 traffic_type=None
```

