# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_5.jpg` | **33.33%** | `input: 427 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_5.json` | **33.33%** | `input: 650 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_5.json` | **33.33%** | `input: 712 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_adj_5.txt` | **0.00%** | `input: 344 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_5.txt` | **0.00%** | `input: 315 , ouput: 7` | `right, down, right, down` |
| `maze_occupancy_3x3_5.jpg` | **8.33%** | `input: 422 , ouput: 21` | `down, right, down, right, down, right, down, right, up, right, down` |
| `maze_occupancy_3x3_5.json` | **0.00%** | `input: 465 , ouput: 29` | `right, down, down, right, right, down, down, right, right, up, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_5.json` | **0.00%** | `input: 1174 , ouput: 21` | `right, right, right, down, down, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_5.txt` | **33.33%** | `input: 456 , ouput: 13` | `down, down, right, right, right, down, down` |
| `maze_occupancy_3x3_ascii_5.txt` | **0.00%** | `input: 193 , ouput: 39` | `right, right, down, right, down, down, left, left, down, right, right, right, up, up, left, left, down, right, right, right` |
| `maze_occupancy_3x3_tokenized_5.txt` | **8.33%** | `input: 744 , ouput: 31` | `down, right, down, down, right, down, right, right, up, right, down, down, right, right, right, down` |

---

## Full LLM Responses

### `maze_line_3x3_5.jpg`

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
        text='down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='joMcaZiWHsu2xN8Pj9DiyAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_5.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j4Mcac3ZDueP28oP2dzIyAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_5.json`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j4McafLqL-eP28oP2dzIyAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_5.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kIMcaZrZH7jUvdIPjbOpuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_5.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kYMcaZ6fENX8vdIPueXoyAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_5.jpg`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,up,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zYMcabH7L9H3xN8P5NmBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
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
  total_token_count=443
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=422 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=164
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=443 traffic_type=None
```

### `maze_occupancy_3x3_5.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, right, up, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,right,up,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zoMcaezgLa2XvdIPtvWGyQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=465,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=465
    ),
  ],
  total_token_count=494
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=465 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=465
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=494 traffic_type=None
```

### `maze_occupancy_3x3_adj_5.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='z4McadfvGZfOvdIPsNOE0Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1174,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1174
    ),
  ],
  total_token_count=1195
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1174 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1174
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1195 traffic_type=None
```

### `maze_occupancy_3x3_adj_5.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0IMcaYHOBIrkvdIPipOBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=456,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=456
    ),
  ],
  total_token_count=469
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=456 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=456
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=469 traffic_type=None
```

### `maze_occupancy_3x3_ascii_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, down, left, left, down, right, right, right, up, up, left, left, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,left,left,down,right,right,right,up,up,left,left,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0YMcacR57YK90g_t6IGQCQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=193,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=193
    ),
  ],
  total_token_count=232
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=193 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=193
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=232 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_5.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, down, right, down, right, right, up, right, down, down, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, down, right, down, right, right, up, right, down, down, right, right, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0YMcabevN5fOvdIPsNOE0Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=744,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=744
    ),
  ],
  total_token_count=775
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=744 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=744
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=775 traffic_type=None
```

