# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_4.jpg` | **0.00%** | `input: 427 , ouput: 23` | `down, right, down, right, down, right, down, right, up, right, down, down` |
| `maze_line_6x6_4.json` | **17.86%** | `input: 1802 , ouput: 29` | `right, right, right, right, down, down, down, down, down, right, right, right, down, down, right` |
| `maze_line_6x6_adj_4.json` | **17.86%** | `input: 2251 , ouput: 29` | `right, right, right, right, down, down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_4.txt` | **17.86%** | `input: 722 , ouput: 29` | `right, right, right, right, down, right, down, right, down, down, right, down, right, down, right` |
| `maze_line_6x6_tokenized_4.txt` | **3.57%** | `input: 666 , ouput: 21` | `right, down, down, right, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_4.jpg` | **10.71%** | `input: 424 , ouput: 650` | `right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down` |
| `maze_occupancy_6x6_4.json` | **14.29%** | `input: 981 , ouput: 51` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, down, right, right, right` |
| `maze_occupancy_6x6_adj_4.json` | **17.86%** | `input: 4339 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_4.txt` | **17.86%** | `input: 1270 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down` |
| `maze_occupancy_6x6_ascii_4.txt` | **21.43%** | `input: 242 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |
| `maze_occupancy_6x6_tokenized_4.txt` | **14.29%** | `input: 2155 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_6x6_4.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, up, left, left, down, right, down, right, down, left, left, down, right, right, right, up, up, right, down, down, right
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V98dacWMC97YvdIPxbGQwAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_4.json`

**Score:** 17.86%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, up, left, left, down, right, down, right, down, left, left, down, right, right, right, up, up, right, down, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,right,right,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V98dafrhL9_UvdIPtoDHyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1831
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1831 traffic_type=None
```

### `maze_line_6x6_adj_4.json`

**Score:** 17.86%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, up, left, left, down, right, down, right, down, left, left, down, right, right, right, up, up, right, down, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WN8daZKIGorkvdIPipOBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2280
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2280 traffic_type=None
```

### `maze_line_6x6_adj_4.txt`

**Score:** 17.86%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, up, left, left, down, right, down, right, down, left, left, down, right, right, right, up, up, right, down, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, right, down, right, down, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, right, down, right, down, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Wd8daY-JA97YvdIPxbGQwAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=751
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=751 traffic_type=None
```

### `maze_line_6x6_tokenized_4.txt`

**Score:** 3.57%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, up, left, left, down, right, down, right, down, left, left, down, right, right, right, up, up, right, down, down, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Wd8daYDfLtWNvdIPo9-nuA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=687
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=687 traffic_type=None
```

### `maze_occupancy_6x6_4.jpg`

**Score:** 10.71%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,down,down,down,down,down,down,down,down,left,left,left,left,down,down,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XN8dabvVN5S3vdIPuPm34Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1074
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1074 traffic_type=None
```

### `maze_occupancy_6x6_4.json`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Xd8dabmZM-2CvdIP7eiBkAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=981,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=981
    ),
  ],
  total_token_count=1032
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=981 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=981
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1032 traffic_type=None
```

### `maze_occupancy_6x6_adj_4.json`

**Score:** 17.86%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YN8dadSlEe3Zxs0PsZuluAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4339,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4339
    ),
  ],
  total_token_count=4989
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4339 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4339
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4989 traffic_type=None
```

### `maze_occupancy_6x6_adj_4.txt`

**Score:** 17.86%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Y98daY-4LqHXxN8Ph5ic0Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1270,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1270
    ),
  ],
  total_token_count=1920
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1270 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1270
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1920 traffic_type=None
```

### `maze_occupancy_6x6_ascii_4.txt`

**Score:** 21.43%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Zt8daamVN6nUvdIPh8yB8As' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=242,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=242
    ),
  ],
  total_token_count=892
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=242 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=242
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=892 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_4.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='at8daeSlKITVxs0P2sbnuAg' usage_metadata=GenerateContentResponseUsageMetadata(
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

