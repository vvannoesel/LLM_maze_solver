# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_12.jpg` | **0.00%** | `input: 434 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_12.json` | **25.00%** | `input: 657 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_adj_12.json` | **100.00%** | `input: 719 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_adj_12.txt` | **100.00%** | `input: 351 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_tokenized_12.txt` | **0.00%** | `input: 322 , ouput: 394` | `the, maze, representation, appears, to, be, incomplete, or, malformed., it's, difficult, to, construct, a, valid, path, without, a, clear, definition, of, walls, for, each, cell, and, especially, without, knowing, the, connectivity, between, adjacent, cells., however, if, we, interpret, the, provided, information, as, follows, assuming, missing, walls, imply, open, passages:, -, **(0, 0), <|updownleft_wall|>, <|origin|>**, :, this, cell, has, walls, up, down, and, left., to, move, we, can, only, go, right., -, **(0, 1), <|updown_wall|>**, :, this, cell, has, walls, up, and, down., to, move, we, can, only, go, left, or, right., -, **(0, 2), <|upright_wall|>, <|target|>**, :, this, cell, has, walls, up, and, right., to, move, we, can, only, go, left., let's, try, to, trace, a, path, based, on, this, limited, interpretation, assuming, the, maze, is, implicitly, connected, where, not, explicitly, blocked:, 1., **start, at, (0, 0)**., the, only, possible, move, is, right., 2., **move, to, (0, 1)**., from, (0, 1), we, can, move, left, or, right., since, the, target, is, to, the, right, of, (0, 1), and, we, can't, go, back, to, (0, 0), without, hitting, a, wall, we, must, go, right., 3., **move, to, (0, 2)**., this, is, the, target., based, on, this, very, limited, interpretation, the, path, would, be:, right, right, however, if, the, intention, was, to, provide, a, fully, specified, 3x3, maze, the, current, input, is, insufficient, to, guarantee, a, correct, solution., i, would, need, a, clear, description, of, walls, for, every, cell, and, how, they, connect, to, their, neighbors., please, provide, a, complete, and, unambiguous, maze, representation., if, i, must, provide, an, answer, based, on, the, above, interpretation, it, is:, right, right` |
| `maze_occupancy_3x3_12.jpg` | **25.00%** | `input: 429 , ouput: 23` | `right, right, down, down, right, right, down, down, left, down, right, right` |
| `maze_occupancy_3x3_12.json` | **75.00%** | `input: 472 , ouput: 23` | `right, right, right, right, down, down, right, down, down, down, right, right` |
| `maze_occupancy_3x3_adj_12.json` | **87.50%** | `input: 1175 , ouput: 17` | `right, right, right, right, down, down, down, right, down` |
| `maze_occupancy_3x3_adj_12.txt` | **87.50%** | `input: 463 , ouput: 17` | `right, right, right, right, down, down, down, right, right` |
| `maze_occupancy_3x3_ascii_12.txt` | **75.00%** | `input: 200 , ouput: 21` | `right, right, right, right, down, down, left, left, down, right, right` |
| `maze_occupancy_3x3_tokenized_12.txt` | **110.00%** | `input: 750 , ouput: 650` | `right, right, right, right, down, down, down, down, left, left, down, right, right, right, down, down, left, left, left, left, up, up, up, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down` |

---

## Full LLM Responses

### `maze_line_3x3_12.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QJGVabjpGPfo7M8PipSSoQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_12.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QZGVabKCA9HMkdUPy8C6kAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_12.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QZGVaduyNLnjnsEPxoKX6AU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_12.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QpGVadrEJvT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
```

**Extracted Answer:**
```
the, maze, representation, appears, to, be, incomplete, or, malformed., it's, difficult, to, construct, a, valid, path, without, a, clear, definition, of, walls, for, each, cell, and, especially, without, knowing, the, connectivity, between, adjacent, cells., however, if, we, interpret, the, provided, information, as, follows, assuming, missing, walls, imply, open, passages:, -, **(0, 0), <|updownleft_wall|>, <|origin|>**, :, this, cell, has, walls, up, down, and, left., to, move, we, can, only, go, right., -, **(0, 1), <|updown_wall|>**, :, this, cell, has, walls, up, and, down., to, move, we, can, only, go, left, or, right., -, **(0, 2), <|upright_wall|>, <|target|>**, :, this, cell, has, walls, up, and, right., to, move, we, can, only, go, left., let's, try, to, trace, a, path, based, on, this, limited, interpretation, assuming, the, maze, is, implicitly, connected, where, not, explicitly, blocked:, 1., **start, at, (0, 0)**., the, only, possible, move, is, right., 2., **move, to, (0, 1)**., from, (0, 1), we, can, move, left, or, right., since, the, target, is, to, the, right, of, (0, 1), and, we, can't, go, back, to, (0, 0), without, hitting, a, wall, we, must, go, right., 3., **move, to, (0, 2)**., this, is, the, target., based, on, this, very, limited, interpretation, the, path, would, be:, right, right, however, if, the, intention, was, to, provide, a, fully, specified, 3x3, maze, the, current, input, is, insufficient, to, guarantee, a, correct, solution., i, would, need, a, clear, description, of, walls, for, every, cell, and, how, they, connect, to, their, neighbors., please, provide, a, complete, and, unambiguous, maze, representation., if, i, must, provide, an, answer, based, on, the, above, interpretation, it, is:, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze representation appears to be incomplete or malformed. It's difficult to construct a valid path without a clear definition of walls for each cell, and especially without knowing the connectivity between adjacent cells.

However, if we interpret the provided information as follows, assuming missing walls imply open passages:

- **(0,0) <|updownleft_wall|> <|origin|>** : This cell has walls up, down, and left. To move, we can only go right.
- **(0,1) <|updown_wall|>** : This cell has walls up and down. To move, we can only go left or right.
- **(0,2) <|upright_wall|> <|target|>** : This cell has walls up and right. To move, we can only go left.

Let's try to trace a path based on this limited interpretation, assuming the maze is implicitly connected where not explicitly blocked:

1. **Start at (0,0)**. The only possible move is right.
2. **Move to (0,1)**. From (0,1), we can move left or right. Since the target is to the right of (0,1), and we can't go back to (0,0) without hitting a wall, we must go right.
3. **Move to (0,2)**. This is the target.

Based on this very limited interpretation, the path would be:

right, right

However, if the intention was to provide a fully specified 3x3 maze, the current input is insufficient to guarantee a correct solution. I would need a clear description of walls for every cell, and how they connect to their neighbors.

Please provide a complete and unambiguous maze representation.

If I must provide an answer based on the above interpretation, it is:

right, right"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RJGVabf1OavgnsEP8Mu7uAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=394,
  prompt_token_count=322,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=322
    ),
  ],
  total_token_count=716
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=394 candidates_tokens_details=None prompt_token_count=322 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=322
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=716 traffic_type=None
```

### `maze_occupancy_3x3_12.jpg`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RpGVaYEB9-jszw-JlJKhCQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=452
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=452 traffic_type=None
```

### `maze_occupancy_3x3_12.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RpGVaf2gNLyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_12.json`

**Score:** 87.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R5GVabL8GsPe7M8PidibyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_12.txt`

**Score:** 87.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SJGVadGXBJnqkdUP57jkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=463,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=463
    ),
  ],
  total_token_count=480
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=463 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=463
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=480 traffic_type=None
```

### `maze_occupancy_3x3_ascii_12.txt`

**Score:** 75.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, left, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, down, left, left, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SZGVaceZFdWbkdUPueCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=200,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=200
    ),
  ],
  total_token_count=221
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=200 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=200
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=221 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_12.txt`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, left, left, down, right, right, right, down, down, left, left, left, left, up, up, up, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down, down, down, left, left, left, left, up, up, up, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,left,left,down,right,right,right,down,down,left,left,left,left,up,up,up,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,down,down,left,left,left,left,up,up,up,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='S5GVaefyIv7MkdUPkdfHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

