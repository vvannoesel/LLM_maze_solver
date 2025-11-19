# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_3.jpg` | **2.94%** | `input: 427 , ouput: 21` | `right, down, right, down, down, right, right, down, right, down, right` |
| `maze_line_6x6_3.json` | **0.00%** | `input: 1802 , ouput: 19` | `down, right, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_3.json` | **8.82%** | `input: 2251 , ouput: 23` | `right, right, down, down, right, right, down, down, right, down, down, right` |
| `maze_line_6x6_adj_3.txt` | **11.76%** | `input: 722 , ouput: 21` | `right, right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_tokenized_3.txt` | **0.00%** | `input: 666 , ouput: 117` | `down, right, right, down, right, down, down, left, down, right, right, right, up, right, down, down, left, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, right, right, up, up, right, down, down, left, left, up, right, right` |
| `maze_occupancy_6x6_3.jpg` | **1.47%** | `input: 424 , ouput: 65` | `right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, left, down, left, down, right, down, right, down, right` |
| `maze_occupancy_6x6_3.json` | **5.88%** | `input: 981 , ouput: 650` | `right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left` |
| `maze_occupancy_6x6_adj_3.json` | **7.35%** | `input: 4341 , ouput: 51` | `right, right, right, right, down, right, up, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_3.txt` | **8.82%** | `input: 1271 , ouput: 189` | `right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_3.txt` | **0.00%** | `input: 243 , ouput: 650` | `down, down, right, right, right, right, down, down, right, right, right, right, up, up, right, down, down, down, down, left, left, left, down, down, down, down, down, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_tokenized_3.txt` | **0.00%** | `input: 2155 , ouput: 85` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up` |

---

## Full LLM Responses

### `maze_line_6x6_3.jpg`

**Score:** 2.94%

**Ground Truth Solution:**
```
right, right, down, right, up, right, right, down, left, down, right, down, left, left, up, left, down, down, left, up, up, up, left, down, down, down, down, right, right, right, up, right, right, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Rt8dadC4M6_9xN8Pgt6ymQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
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
  total_token_count=448
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=448 traffic_type=None
```

### `maze_line_6x6_3.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, right, up, right, right, down, left, down, right, down, left, left, up, left, down, down, left, up, up, up, left, down, down, down, down, right, right, right, up, right, right, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R98daeL4Ne64vdIP3oP06Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1821
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1821 traffic_type=None
```

### `maze_line_6x6_adj_3.json`

**Score:** 8.82%

**Ground Truth Solution:**
```
right, right, down, right, up, right, right, down, left, down, right, down, left, left, up, left, down, down, left, up, up, up, left, down, down, down, down, right, right, right, up, right, right, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SN8dab2ZLI7WvdIP2uCBoAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2274
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2274 traffic_type=None
```

### `maze_line_6x6_adj_3.txt`

**Score:** 11.76%

**Ground Truth Solution:**
```
right, right, down, right, up, right, right, down, left, down, right, down, left, left, up, left, down, down, left, up, up, up, left, down, down, down, down, right, right, right, up, right, right, down
```

**Extracted Answer:**
```
right, right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Sd8daar9FOeP28oP2dzIyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=743
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=743 traffic_type=None
```

### `maze_line_6x6_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, right, up, right, right, down, left, down, right, down, left, left, up, left, down, down, left, up, up, up, left, down, down, down, down, right, right, right, up, right, right, down
```

**Extracted Answer:**
```
down, right, right, down, right, down, down, left, down, right, right, right, up, right, down, down, left, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, right, right, up, up, right, down, down, left, left, up, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,right,down,down,left,down,right,right,right,up,right,down,down,left,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,right,right,up,up,right,down,down,left,left,up,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='St8daZXFNqnUvdIPh8yB8As' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=117,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=783
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=117 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=783 traffic_type=None
```

### `maze_occupancy_6x6_3.jpg`

**Score:** 1.47%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, up, up, up, up, up, up, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, left, down, left, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,up,right,up,right,down,right,down,left,down,left,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TN8daZ6BB4fYvdIPoMnJwQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=65,
  prompt_token_count=424,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=166
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=489
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=424 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=65 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=489 traffic_type=None
```

### `maze_occupancy_6x6_3.json`

**Score:** 5.88%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, up, up, up, up, up, up, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T98daYaNF5fOvdIPsNOE0Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=981,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=981
    ),
  ],
  total_token_count=1631
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=167 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=981 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=981
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1631 traffic_type=None
```

### `maze_occupancy_6x6_adj_3.json`

**Score:** 7.35%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, up, up, up, up, up, up, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, right, up, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,right,up,right,right,right,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UN8dadipEtj9xN8PsaeMoAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=4341,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4341
    ),
  ],
  total_token_count=4392
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=158 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=4341 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4341
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4392 traffic_type=None
```

### `maze_occupancy_6x6_adj_3.txt`

**Score:** 8.82%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, up, up, up, up, up, up, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ud8dacX9MePUxs0Pk8v7uA0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=189,
  prompt_token_count=1271,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1271
    ),
  ],
  total_token_count=1460
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=191 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=189 candidates_tokens_details=None prompt_token_count=1271 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1271
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1460 traffic_type=None
```

### `maze_occupancy_6x6_ascii_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, up, up, up, up, up, up, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, down, down, right, right, right, right, up, up, right, down, down, down, down, left, left, left, down, down, down, down, down, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,down,down,right,right,right,right,up,up,right,down,down,down,down,left,left,left,down,down,down,down,down,right,right,right,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,down,down,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Vd8daazHF6-8xN8Plpr0oAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=243,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=243
    ),
  ],
  total_token_count=893
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=166 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=243 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=243
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=893 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, up, up, up, up, up, up, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Vt8daY2OGP-ivdIPxr60wAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=2155,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2155
    ),
  ],
  total_token_count=2240
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=190 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=2155 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2155
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2240 traffic_type=None
```

