# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_44.jpg` | **0.00%** | `input: 434 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_44.json` | **0.00%** | `input: 657 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_44.json` | **50.00%** | `input: 719 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_adj_44.txt` | **50.00%** | `input: 351 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_44.txt` | **0.00%** | `input: 322 , ouput: 133` | `this, maze, is, too, small, to, represent, properly., the, description, provided, suggests, a, 3x3, grid, but, the, wall, descriptions, within, the, given, tokens, do, not, create, a, solvable, 3x3, maze, with, a, clear, path, from, origin, to, target., specifically, the, origin, at, (0, 0), has, walls, "<|updownleft_wall|>", meaning, it, has, walls, on, the, top, down, and, left., this, isolates, the, origin, cell, entirely., similarly, the, target, at, (2, 2), has, "<|downright_wall|>", indicating, walls, on, the, bottom, and, right., without, a, valid, maze, structure, where, movement, is, possible, i, cannot, provide, a, solution.` |
| `maze_occupancy_3x3_44.jpg` | **12.50%** | `input: 429 , ouput: 13` | `right, down, down, right, right, down, right` |
| `maze_occupancy_3x3_44.json` | **50.00%** | `input: 472 , ouput: 29` | `right, right, down, down, right, right, down, down, right, down, left, left, down, right, right` |
| `maze_occupancy_3x3_adj_44.json` | **50.00%** | `input: 1175 , ouput: 17` | `right, right, down, down, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_44.txt` | **0.00%** | `input: 463 , ouput: 15` | `down, down, right, right, down, right, down, right` |
| `maze_occupancy_3x3_ascii_44.txt` | **110.00%** | `input: 201 , ouput: 29` | `right, right, down, down, down, down, right, right, up, up, left, left, down, down, right` |
| `maze_occupancy_3x3_tokenized_44.txt` | **12.50%** | `input: 750 , ouput: 31` | `right, down, down, right, down, down, right, right, right, right, up, up, up, right, up, up` |

---

## Full LLM Responses

### `maze_line_3x3_44.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='15OVaYODO4zYxs0P5_PJ2Qo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_44.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2ZOVaZxm9-nE3w_So7jJDA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_44.json`

**Score:** 50.00%

**Ground Truth Solution:**
```
right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2ZOVaarALp_ZxN8PqqCEiAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_44.txt`

**Score:** 50.00%

**Ground Truth Solution:**
```
right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2pOVaZX5Gtqb28oPgemZoQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_44.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, right
```

**Extracted Answer:**
```
this, maze, is, too, small, to, represent, properly., the, description, provided, suggests, a, 3x3, grid, but, the, wall, descriptions, within, the, given, tokens, do, not, create, a, solvable, 3x3, maze, with, a, clear, path, from, origin, to, target., specifically, the, origin, at, (0, 0), has, walls, "<|updownleft_wall|>", meaning, it, has, walls, on, the, top, down, and, left., this, isolates, the, origin, cell, entirely., similarly, the, target, at, (2, 2), has, "<|downright_wall|>", indicating, walls, on, the, bottom, and, right., without, a, valid, maze, structure, where, movement, is, possible, i, cannot, provide, a, solution.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""This maze is too small to represent properly. The description provided suggests a 3x3 grid, but the wall descriptions within the given tokens do not create a solvable 3x3 maze with a clear path from origin to target.

Specifically, the origin at (0,0) has walls "<|updownleft_wall|>", meaning it has walls on the top, down, and left. This isolates the origin cell entirely. Similarly, the target at (2,2) has "<|downright_wall|>", indicating walls on the bottom and right.

Without a valid maze structure where movement is possible, I cannot provide a solution."""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='25OVadPuLaS9xN8PvoPm4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=133,
  prompt_token_count=322,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=322
    ),
  ],
  total_token_count=455
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=133 candidates_tokens_details=None prompt_token_count=322 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=322
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=455 traffic_type=None
```

### `maze_occupancy_3x3_44.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3JOVaceQL-K9xN8P27PqsQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
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
  total_token_count=442
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=442 traffic_type=None
```

### `maze_occupancy_3x3_44.json`

**Score:** 50.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, right, down, left, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,right,down,left,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3ZOVaYrfLIjyxs0PwJ_VyQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=472,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=472
    ),
  ],
  total_token_count=501
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=472 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=472
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=501 traffic_type=None
```

### `maze_occupancy_3x3_adj_44.json`

**Score:** 50.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3pOVadvqHP6jvdIPjJjJuQQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_44.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='35OVafWgAd--xN8Puvy7kAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_44.txt`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, down, down, right, right, up, up, left, left, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,right,right,up,up,left,left,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='35OVaYrbK5y8xN8Pl5eC0Aw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=201,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=201
    ),
  ],
  total_token_count=230
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=201 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=201
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=230 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_44.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, down, down, right, right, right, right, up, up, up, right, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, down, down, right, right, right, right, up, up, up, right, up, up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4JOVaY_UFdPevdIP3abOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

