# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_21.jpg` | **0.00%** | `input: 434 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_21.json` | **33.33%** | `input: 657 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_21.json` | **33.33%** | `input: 719 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_21.txt` | **0.00%** | `input: 351 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_21.txt` | **0.00%** | `input: 322 , ouput: 7` | `right, down, down, right` |
| `maze_occupancy_3x3_21.jpg` | **8.33%** | `input: 429 , ouput: 19` | `down, right, down, right, down, down, right, up, right, down` |
| `maze_occupancy_3x3_21.json` | **8.33%** | `input: 472 , ouput: 37` | `down, right, right, down, down, right, right, right, down, down, left, down, right, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_21.json` | **33.33%** | `input: 1175 , ouput: 21` | `down, down, right, right, right, up, right, down, down, right, down` |
| `maze_occupancy_3x3_adj_21.txt` | **16.67%** | `input: 463 , ouput: 15` | `down, down, down, right, right, right, down, down` |
| `maze_occupancy_3x3_ascii_21.txt` | **33.33%** | `input: 200 , ouput: 17` | `down, down, right, right, right, down, down, right, right` |
| `maze_occupancy_3x3_tokenized_21.txt` | **0.00%** | `input: 750 , ouput: 650` | `right, down, right, right, down, left, down, right, right, right, down, down, left, left, up, up, right, right, down, down, left, left, left, down, right, right, right, right, down, left, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right` |

---

## Full LLM Responses

### `maze_line_3x3_21.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vZGVaZ-8B6eN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_21.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vZGVaYaKKqG-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_21.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vpGVabXYE67pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v5GVadvqAvfnnsEPornoiAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down
```

**Extracted Answer:**
```
right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v5GVacqDLIqjkdUP-qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_21.jpg`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, down, right, up, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,down,right,up,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wJGVabXRPPujkdUP0fjD0QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_21.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, right, down, down, left, down, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,right,down,down,left,down,right,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wpGVadH_Cpzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=472,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=472
    ),
  ],
  total_token_count=509
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=472 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=472
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=509 traffic_type=None
```

### `maze_occupancy_3x3_adj_21.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, up, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, right, up, right, down, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wpGVad-oKtHMkdUPy8C6kAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1175,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1175
    ),
  ],
  total_token_count=1196
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1175 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1175
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1196 traffic_type=None
```

### `maze_occupancy_3x3_adj_21.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w5GVaYTVHtqfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_21.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xJGVaaC3A6zd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=200,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=200
    ),
  ],
  total_token_count=217
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=200 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=200
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=217 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, right, down, left, down, right, right, right, down, down, left, left, up, up, right, right, down, down, left, left, left, down, right, right, right, right, down, left, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right, right, right, up, up, up, left, left, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,left,down,right,right,right,down,down,left,left,up,up,right,right,down,down,left,left,left,down,right,right,right,right,down,left,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,right,right,up,up,up,left,left,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xpGVaefdF5mG7M8PkeL4mAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

