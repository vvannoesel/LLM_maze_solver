# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_2.jpg` | **0.00%** | `input: 427 , ouput: 23` | `right, down, right, down, down, right, down, right, up, right, down, down` |
| `maze_line_6x6_2.json` | **5.56%** | `input: 1802 , ouput: 49` | `down, down, down, right, right, down, down, right, right, right, up, right, down, down, right, down, right, right, up, right, down, down, right, right, down` |
| `maze_line_6x6_adj_2.json` | **5.56%** | `input: 2251 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_2.txt` | **0.00%** | `input: 722 , ouput: 19` | `right, right, right, right, right, down, down, down, down, down` |
| `maze_line_6x6_tokenized_2.txt` | **0.00%** | `input: 666 , ouput: 29` | `right, down, down, down, down, down, right, right, right, right, up, up, up, up, right` |
| `maze_occupancy_6x6_2.jpg` | **0.00%** | `input: 424 , ouput: 41` | `right, down, right, down, right, down, left, down, right, right, down, right, down, left, down, left, down, right, right, down, right` |
| `maze_occupancy_6x6_2.json` | **0.00%** | `input: 981 , ouput: 650` | `right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_2.json` | **5.56%** | `input: 4343 , ouput: 53` | `down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_2.txt` | **5.56%** | `input: 1273 , ouput: 650` | `down, down, down, down, right, right, down, down, right, right, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down` |
| `maze_occupancy_6x6_ascii_2.txt` | **11.11%** | `input: 240 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_2.txt` | **0.00%** | `input: 2155 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, right, right, down, down, left, up, left, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, down, right, down, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,down,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='L98dadnWMq2XvdIPtvWGyQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=450
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=450 traffic_type=None
```

### `maze_line_6x6_2.json`

**Score:** 5.56%

**Ground Truth Solution:**
```
down, right, down, right, right, down, down, left, up, left, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, right, right, down, down, right, right, right, up, right, down, down, right, down, right, right, up, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, right, right, down, down, right, right, right, up, right, down, down, right, down, right, right, up, right, down, down, right, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Md8daZbUC6_9xN8Pgt6ymQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1851
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1851 traffic_type=None
```

### `maze_line_6x6_adj_2.json`

**Score:** 5.56%

**Ground Truth Solution:**
```
down, right, down, right, right, down, down, left, up, left, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Md8dadSbO9WNvdIPo9-nuA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2270
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2270 traffic_type=None
```

### `maze_line_6x6_adj_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, right, right, down, down, left, up, left, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M98daajNAcrVvdIPuoSCuAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=741
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=741 traffic_type=None
```

### `maze_line_6x6_tokenized_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, right, right, down, down, left, up, left, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, right, right, right, right, up, up, up, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,right,right,right,right,up,up,up,up,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M98daeOJMpDyxs0PvfG_iQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=695
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=695 traffic_type=None
```

### `maze_occupancy_6x6_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, down, right, down, left, down, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,down,right,down,left,down,left,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Nt8daduOA6uP28oPu5_O2Q4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
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
  total_token_count=465
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=465 traffic_type=None
```

### `maze_occupancy_6x6_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Od8daYb1C_SOvdIP7bjwwQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_2.json`

**Score:** 5.56%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ot8dad6oHuy2vdIP_Yq5mQ4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=4343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4343
    ),
  ],
  total_token_count=4396
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=4343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4343
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4396 traffic_type=None
```

### `maze_occupancy_6x6_adj_2.txt`

**Score:** 5.56%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, right, right, down, down, right, right, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, right, right, down, down, right, right, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Pt8daYmaDu3Zxs0PsZuluAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1273,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1273
    ),
  ],
  total_token_count=1923
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1273 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1273
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1923 traffic_type=None
```

### `maze_occupancy_6x6_ascii_2.txt`

**Score:** 11.11%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Qt8dae2fB-DTvdIPsdP1mAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=240,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=240
    ),
  ],
  total_token_count=890
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=240 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=240
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=890 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Rd8daarmLODTvdIPsdP1mAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2155,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2155
    ),
  ],
  total_token_count=2805
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2155 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2155
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2805 traffic_type=None
```

