# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_42.jpg` | **12.50%** | `input: 434 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_42.json` | **37.50%** | `input: 657 , ouput: 7` | `down, down, right, right` |
| `maze_line_3x3_adj_42.json` | **12.50%** | `input: 719 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_42.txt` | **12.50%** | `input: 351 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_tokenized_42.txt` | **0.00%** | `input: 322 , ouput: 7` | `right, down, right, down` |
| `maze_occupancy_3x3_42.jpg` | **12.50%** | `input: 429 , ouput: 21` | `down, down, right, down, down, right, right, up, right, down, down` |
| `maze_occupancy_3x3_42.json` | **6.25%** | `input: 472 , ouput: 21` | `down, right, right, down, down, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_42.json` | **37.50%** | `input: 1175 , ouput: 17` | `down, down, down, down, right, right, right, down, down` |
| `maze_occupancy_3x3_adj_42.txt` | **37.50%** | `input: 463 , ouput: 21` | `down, down, down, down, right, right, right, up, up, up, up` |
| `maze_occupancy_3x3_ascii_42.txt` | **12.50%** | `input: 203 , ouput: 29` | `down, down, right, right, right, down, down, left, left, up, up, right, right, down, down` |
| `maze_occupancy_3x3_tokenized_42.txt` | **0.00%** | `input: 750 , ouput: 650` | `right, down, down, down, down, right, right, right, right, down, left, left, down, right, right, right, down, left, left, left, left, up, up, up, up, up, up, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left` |

---

## Full LLM Responses

### `maze_line_3x3_42.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='t5OVaf2kBd--xN8Puvy7kAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_42.json`

**Score:** 37.50%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='t5OVaY64L9KwxN8PyNH2gQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_42.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uJOVaeGJI7vzxs0P38eemAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_42.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uZOVacW-M76CvdIPqpzqmAg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_42.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='upOVaZr_G9qb28oPgemZoQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_42.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, down, right, right, up, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='u5OVae-bH8HWxs0PwvX2iQ4' usage_metadata=GenerateContentResponseUsageMetadata(
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=450 traffic_type=None
```

### `maze_occupancy_3x3_42.json`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vJOVabbqDp_UxN8P5b7YuQc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_42.json`

**Score:** 37.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, right, right, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vJOVafDsMJuZ28oPi9qtsAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_42.txt`

**Score:** 37.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,right,right,right,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vZOVaZXTGfWNxs0PtLSW2QE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_42.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, down, down, left, left, up, up, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,down,left,left,up,up,right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vpOVacuIBPfpxN8P0qO4yQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=203,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=203
    ),
  ],
  total_token_count=232
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=203 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=203
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=232 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_42.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, right, right, right, right, down, left, left, down, right, right, right, down, left, left, left, left, up, up, up, up, up, up, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,right,right,right,right,down,left,left,down,right,right,right,down,left,left,left,left,up,up,up,up,up,up,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wJOVabyCBOLSvdIP0O3TwQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

