# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_30.jpg` | **100.00%** | `input: 434 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_30.json` | **50.00%** | `input: 657 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_30.json` | **0.00%** | `input: 719 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_adj_30.txt` | **100.00%** | `input: 351 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_tokenized_30.txt` | **0.00%** | `input: 322 , ouput: 7` | `right, down, right, down` |
| `maze_occupancy_3x3_30.jpg` | **0.00%** | `input: 429 , ouput: 21` | `right, down, right, down, down, right, right, up, right, down, down` |
| `maze_occupancy_3x3_30.json` | **12.50%** | `input: 472 , ouput: 23` | `down, right, down, right, right, right, down, down, right, right, down, right` |
| `maze_occupancy_3x3_adj_30.json` | **110.00%** | `input: 1175 , ouput: 19` | `down, down, right, right, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_30.txt` | **25.00%** | `input: 463 , ouput: 19` | `down, down, down, right, right, right, up, up, up, up` |
| `maze_occupancy_3x3_ascii_30.txt` | **0.00%** | `input: 198 , ouput: 35` | `right, down, right, right, right, down, left, down, right, right, down, left, left, left, down, right, right, right` |
| `maze_occupancy_3x3_tokenized_30.txt` | **12.50%** | `input: 750 , ouput: 650` | `down, right, down, right, down, right, down, right, up, right, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right` |

---

## Full LLM Responses

### `maze_line_3x3_30.jpg`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dZKVaZ7sF9ihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_30.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dpKVaeaWBY-VkdUPpZbhqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_30.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dpKVadjKKpzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_30.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d5KVaZHXDoyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d5KVaZm3Nqfx7M8PiZPD-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_30.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eJKVaevZNKG-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
  cache_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=117
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=176
    ),
  ],
  cached_content_token_count=293,
  candidates_token_count=21,
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
  total_token_count=450
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
cache_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=117
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=176
)] cached_content_token_count=293 candidates_token_count=21 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=450 traffic_type=None
```

### `maze_occupancy_3x3_30.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, right, down, right, right, right, down, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,right,right,down,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eZKVaaPnH4DHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_30.json`

**Score:** 110.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, right, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='epKVaaDlCJjknsEPxt7C0AU' usage_metadata=GenerateContentResponseUsageMetadata(
  cache_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1017
    ),
  ],
  cached_content_token_count=1017,
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
cache_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1017
)] cached_content_token_count=1017 candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1175 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1175
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1194 traffic_type=None
```

### `maze_occupancy_3x3_adj_30.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,right,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='epKVafvINP_DnsEPhPSp6QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=463,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=463
    ),
  ],
  total_token_count=482
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=463 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=463
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=482 traffic_type=None
```

### `maze_occupancy_3x3_ascii_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, right, down, left, down, right, right, down, left, left, left, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,down,left,down,right,right,down,left,left,left,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e5KVaeGvK9z07M8PwPSugQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=198,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=198
    ),
  ],
  total_token_count=233
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=198 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=198
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=233 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_30.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right, down, right, down, right, up, right, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right, up, up, up, right, down, down, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fZKVaZ7qNffonsEPwaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

