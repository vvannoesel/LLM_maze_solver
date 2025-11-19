# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_10.jpg` | **10.00%** | `input: 427 , ouput: 51` | `right, down, right, down, right, down, right, up, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right, down, right` |
| `maze_line_6x6_10.json` | **0.00%** | `input: 1802 , ouput: 21` | `down, down, right, right, down, down, right, right, down, right, right` |
| `maze_line_6x6_adj_10.json` | **15.00%** | `input: 2251 , ouput: 19` | `right, down, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_10.txt` | **5.00%** | `input: 722 , ouput: 23` | `right, right, right, down, right, down, down, right, down, right, down, right` |
| `maze_line_6x6_tokenized_10.txt` | **10.00%** | `input: 666 , ouput: 57` | `right, down, right, down, right, down, left, down, right, right, up, right, down, down, right, down, left, left, down, right, right, up, right, up, right, down, down, right, down` |
| `maze_occupancy_6x6_10.jpg` | **0.00%** | `input: 424 , ouput: 37` | `down, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_10.json` | **10.00%** | `input: 981 , ouput: 650` | `right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down` |
| `maze_occupancy_6x6_adj_10.json` | **5.00%** | `input: 4335 , ouput: 650` | `right, right, right, down, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_10.txt` | **0.00%** | `input: 1267 , ouput: 43` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_10.txt` | **7.50%** | `input: 239 , ouput: 650` | `right, right, down, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_tokenized_10.txt` | **2.50%** | `input: 2155 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down` |

---

## Full LLM Responses

### `maze_line_6x6_10.jpg`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, down, down, left, down, down, right, right, up, up, right, right, down, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,up,right,down,down,left,down,right,right,up,right,down,down,left,left,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7N8daY6ZDcOvxN8P2_qB8Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
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
  total_token_count=478
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=478 traffic_type=None
```

### `maze_line_6x6_10.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, left, down, down, right, right, up, up, right, right, down, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7d8daZPJDZXVxs0P7sqPqQ4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1823
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1823 traffic_type=None
```

### `maze_line_6x6_adj_10.json`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, down, down, left, down, down, right, right, up, up, right, right, down, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7t8daZTKDoDXvdIPwbrDyAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_10.txt`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, down, down, left, down, down, right, right, up, up, right, right, down, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, right, right, down, right, down, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, down, right, down, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='798dafTVD6H6xs0P87WrgAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=745
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=745 traffic_type=None
```

### `maze_line_6x6_tokenized_10.txt`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, down, down, left, down, down, right, right, up, up, right, right, down, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, up, right, down, down, right, down, left, left, down, right, right, up, right, up, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,up,right,down,down,right,down,left,left,down,right,right,up,right,up,right,down,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8N8dabW7Bu64vdIP3oP06Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=723
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=723 traffic_type=None
```

### `maze_occupancy_6x6_10.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8N8dafr8OpfOvdIPsNOE0Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
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
  total_token_count=461
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=461 traffic_type=None
```

### `maze_occupancy_6x6_10.json`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9N8dafKeD_Xzxs0Pn66hoAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_10.json`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, down, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-N8dabH6KOLTvdIPoYrOqAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4335,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4335
    ),
  ],
  total_token_count=4985
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4335 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4335
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4985 traffic_type=None
```

### `maze_occupancy_6x6_adj_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-d8dab6oFerVvdIP957EwAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=1267,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1267
    ),
  ],
  total_token_count=1310
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=1267 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1267
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1310 traffic_type=None
```

### `maze_occupancy_6x6_ascii_10.txt`

**Score:** 7.50%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_N8dacnMKqTyxs0PnYinqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=239,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=239
    ),
  ],
  total_token_count=889
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=239 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=239
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=889 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_10.txt`

**Score:** 2.50%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_98daZ-sMOXZxs0P5LjvsAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

