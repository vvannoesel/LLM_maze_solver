# LLM Maze Solving Comparison Report

 NEW ASCII

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_4.jpg` | **100.00%** | `input: 427 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_4.json` | **0.00%** | `input: 650 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_4.json` | **100.00%** | `input: 712 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_adj_4.txt` | **100.00%** | `input: 344 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_4.txt` | **25.00%** | `input: 315 , ouput: 7` | `right, right, down, down` |
| `maze_occupancy_3x3_4.jpg` | **0.00%** | `input: 422 , ouput: 49` | `the, start, is, at, (0, 0), and, the, end, is, at, (5, 6)., here's, a, possible, path:, down, down, right, right, down, down, right, right, down, right, right` |
| `maze_occupancy_3x3_4.json` | **0.00%** | `input: 465 , ouput: 21` | `down, right, right, down, down, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_4.json` | **110.00%** | `input: 1174 , ouput: 19` | `right, right, down, down, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_4.txt` | **37.50%** | `input: 456 , ouput: 15` | `right, right, down, right, down, right, down, right` |
| `maze_occupancy_3x3_ascii_4.txt` | **0.00%** | `input: 193 , ouput: 23` | `down, right, right, down, right, down, down, left, down, right, right, right` |
| `maze_occupancy_3x3_tokenized_4.txt` | **50.00%** | `input: 744 , ouput: 650` | `right, right, down, down, down, down, right, right, right, up, up, right, down, down, down, down, down, right, right, up, up, up, up, right, right, right, down, down, right, right, right, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right` |

---

## Full LLM Responses

### `maze_line_3x3_4.jpg`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DDMbaZ_iB6DinsEP8LuCuQs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_4.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DDMbafLNIaDinsEP8LuCuQs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_4.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DTMbaYGpE86VkdUP7KTRiA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_4.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DjMbabmmAtalkdUPpciFuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_4.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DjMbaY6tG6WG7M8PiI2-2Q8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_4.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
the, start, is, at, (0, 0), and, the, end, is, at, (5, 6)., here's, a, possible, path:, down, down, right, right, down, down, right, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The start is at (0,0) and the end is at (5,6).

Here's a possible path:
down, down, right, right, down, down, right, right, down, right, right"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EDMbae30BLnqkdUPzvrjgAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
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
  total_token_count=471
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=422 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=164
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=471 traffic_type=None
```

### `maze_occupancy_3x3_4.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EDMbaf20MNGsnsEPu8DVuQs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_4.json`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ETMbaf6OEfDjkdUPq-nViQs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_4.txt`

**Score:** 37.50%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ETMbadOyKrn4nsEPzLSLkA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, down, right, down, down, left, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,right,down,down,left,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EjMbaZDgGNrikdUPiciowQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=193,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=193
    ),
  ],
  total_token_count=216
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=193 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=193
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=216 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_4.txt`

**Score:** 50.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, right, right, right, up, up, right, down, down, down, down, down, right, right, up, up, up, up, right, right, right, down, down, right, right, right, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right, right, up, up, up, up, up, up, right, right, right, down, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,right,right,right,up,up,right,down,down,down,down,down,right,right,up,up,up,up,right,right,right,down,down,right,right,right,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,right,up,up,up,up,up,up,right,right,right,down,down,down,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FDMbafm9NsWEkdUP5M7mwQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=744,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=744
    ),
  ],
  total_token_count=1394
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=744 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=744
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1394 traffic_type=None
```

