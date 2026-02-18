# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_37.jpg` | **25.00%** | `input: 434 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_37.json` | **100.00%** | `input: 657 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_adj_37.json` | **100.00%** | `input: 719 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_adj_37.txt` | **100.00%** | `input: 351 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_tokenized_37.txt` | **0.00%** | `input: 322 , ouput: 7` | `right, down, right, down` |
| `maze_occupancy_3x3_37.jpg` | **25.00%** | `input: 429 , ouput: 23` | `down, down, right, right, down, down, right, right, up, right, down, down` |
| `maze_occupancy_3x3_37.json` | **25.00%** | `input: 472 , ouput: 19` | `down, down, right, down, right, right, right, down, down, right` |
| `maze_occupancy_3x3_adj_37.json` | **110.00%** | `input: 1175 , ouput: 19` | `down, down, down, down, right, right, right, right, down, down` |
| `maze_occupancy_3x3_adj_37.txt` | **100.00%** | `input: 463 , ouput: 15` | `down, down, down, down, right, right, right, right` |
| `maze_occupancy_3x3_ascii_37.txt` | **0.00%** | `input: 201 , ouput: 37` | `right, down, right, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right` |
| `maze_occupancy_3x3_tokenized_37.txt` | **0.00%** | `input: 750 , ouput: 650` | `right, down, down, down, down, right, right, up, right, up, up, right, right, right, down, down, down, down, left, left, left, down, left, left, left, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_3x3_37.jpg`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bJOVafikDf6o28oPm8yLkQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_37.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bZOVadrCBqS9xN8PvoPm4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_37.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bZOVaYHBO43ZvdIPlZKdgQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_37.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bpOVaevNO_6jvdIPjJjJuQQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_37.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cJOVaaj-FJ-NvdIPi-LSsQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=322,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=322
    ),
  ],
  total_token_count=329
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=322 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=322
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=329 traffic_type=None
```

### `maze_occupancy_3x3_37.jpg`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cZOVaenHKNPevdIP3abOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_37.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, down, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,down,right,right,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cpOVafeHDsn7vdIP_oGtyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=472,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=472
    ),
  ],
  total_token_count=491
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=472 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=472
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=491 traffic_type=None
```

### `maze_occupancy_3x3_adj_37.json`

**Score:** 110.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, right, right, right, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cpOVaciTML7zxs0PkPG1-Qs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_37.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='c5OVacTsG_nTxN8Pjof32Qc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dJOVaeaxJa_5vdIP_s_aiAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=201,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=201
    ),
  ],
  total_token_count=238
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=201 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=201
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=238 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, right, right, up, right, up, up, right, right, right, down, down, down, down, left, left, left, down, left, left, left, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,right,right,up,right,up,up,right,right,right,down,down,down,down,left,left,left,down,left,left,left,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dpOVaZnoOrPTvdIPh7q28Qo' usage_metadata=GenerateContentResponseUsageMetadata(
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

