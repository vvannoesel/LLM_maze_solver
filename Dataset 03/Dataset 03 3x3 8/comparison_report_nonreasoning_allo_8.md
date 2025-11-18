# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_8.jpg` | **0.00%** | `input: 427 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_8.json` | **0.00%** | `input: 650 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_8.json` | **33.33%** | `input: 712 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_adj_8.txt` | **33.33%** | `input: 344 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_8.txt` | **33.33%** | `input: 315 , ouput: 7` | `right, down, right, down` |
| `maze_occupancy_3x3_8.jpg` | **8.33%** | `input: 422 , ouput: 17` | `right, down, down, right, down, right, right, down, right` |
| `maze_occupancy_3x3_8.json` | **33.33%** | `input: 465 , ouput: 21` | `right, right, down, down, right, down, down, right, right, right, down` |
| `maze_occupancy_3x3_adj_8.json` | **33.33%** | `input: 1174 , ouput: 19` | `right, right, down, down, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_8.txt` | **33.33%** | `input: 456 , ouput: 15` | `right, right, down, down, right, down, right, right` |
| `maze_occupancy_3x3_ascii_8.txt` | **33.33%** | `input: 193 , ouput: 31` | `right, right, down, down, right, right, right, down, down, left, left, left, down, down, right, right` |
| `maze_occupancy_3x3_tokenized_8.txt` | **8.33%** | `input: 744 , ouput: 25` | `right, down, down, right, right, down, down, down, down, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_3x3_8.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='D4UcaZSZMuDTvdIPsdP1mAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=427,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=169
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=434
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=427 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=434 traffic_type=None
```

### `maze_line_3x3_8.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EIUcaY-7NdH3xN8P5NmBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=650,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=650
    ),
  ],
  total_token_count=657
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=185 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=650 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=650
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=657 traffic_type=None
```

### `maze_line_3x3_adj_8.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, down, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EYUcadzXKPClvdIPvJaP0Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=712,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=712
    ),
  ],
  total_token_count=719
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=712 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=712
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=719 traffic_type=None
```

### `maze_line_3x3_adj_8.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, down, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EoUcafq5F9rzxs0Pi5nMiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=344,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=344
    ),
  ],
  total_token_count=351
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=344 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=344
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=351 traffic_type=None
```

### `maze_line_3x3_tokenized_8.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, down, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EoUcabKHO8LBvdIPla2QkAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=322
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=187 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=322 traffic_type=None
```

### `maze_occupancy_3x3_8.jpg`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T4UcafLhFtrzxs0Pi5nMiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=422,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=164
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=439
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=422 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=422 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=164
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=439 traffic_type=None
```

### `maze_occupancy_3x3_8.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, down, down, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,down,right,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UIUcaduwDImHxN8PivzW-Q8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=465,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=465
    ),
  ],
  total_token_count=486
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=165 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=465 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=465
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=486 traffic_type=None
```

### `maze_occupancy_3x3_adj_8.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UIUcab-VMIGOvdIP28nzuQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1174,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1174
    ),
  ],
  total_token_count=1193
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1174 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1174
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1193 traffic_type=None
```

### `maze_occupancy_3x3_adj_8.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UYUcafX7FYrkvdIPipOBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=456,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=456
    ),
  ],
  total_token_count=471
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=456 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=456
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=471 traffic_type=None
```

### `maze_occupancy_3x3_ascii_8.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, left, left, left, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,left,left,left,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UoUcaYuVBuaavdIPio31oQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=193,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=193
    ),
  ],
  total_token_count=224
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=164 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=193 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=193
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=224 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_8.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,down,down,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4UcaeCsBffPvdIPp-ycyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=744,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=744
    ),
  ],
  total_token_count=769
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=744 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=744
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=769 traffic_type=None
```

