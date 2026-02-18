# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_15.jpg` | **10.00%** | `input: 434 , ouput: 17` | `right, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_15.json` | **6.67%** | `input: 1809 , ouput: 23` | `right, down, down, right, right, down, down, right, right, down, down, right` |
| `maze_line_6x6_adj_15.json` | **3.33%** | `input: 2258 , ouput: 29` | `right, right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_15.txt` | **3.33%** | `input: 729 , ouput: 27` | `right, right, down, right, right, down, down, right, right, down, down, right, down, right` |
| `maze_line_6x6_tokenized_15.txt` | **10.00%** | `input: 673 , ouput: 650` | `right, down, right, down, right, down, left, down, right, right, up, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, up, right, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left` |
| `maze_occupancy_6x6_15.jpg` | **1.67%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_15.json` | **6.67%** | `input: 988 , ouput: 650` | `right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_15.json` | **5.00%** | `input: 4345 , ouput: 43` | `right, right, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_15.txt` | **0.00%** | `input: 1276 , ouput: 45` | `down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_ascii_15.txt` | **5.00%** | `input: 246 , ouput: 650` | `right, right, down, right, down, down, right, right, right, down, right, right, right, right, right, right, down, down, down, left, down, left, left, left, left, up, left, left, down, down, down, down, right, right, right, up, right, up, right, up, up, left, left, left, left, down, down, right, right, right, right, right, right, down, right, down, down, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_tokenized_15.txt` | **6.67%** | `input: 2162 , ouput: 650` | `right, right, down, down, left, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up` |

---

## Full LLM Responses

### `maze_line_6x6_15.jpg`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, down, right, up, right, right, right, down, left, left, down, right, down, left, left, up, left, left, down, right, down, left, down, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yoGVab_dGseC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
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
  total_token_count=451
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=451 traffic_type=None
```

### `maze_line_6x6_15.json`

**Score:** 6.67%

**Ground Truth Solution:**
```
right, down, right, up, right, right, right, down, left, left, down, right, down, left, left, up, left, left, down, right, down, left, down, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, right, down, down, right, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='y4GVaZm8A_jHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1832
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1832 traffic_type=None
```

### `maze_line_6x6_adj_15.json`

**Score:** 3.33%

**Ground Truth Solution:**
```
right, down, right, up, right, right, right, down, left, left, down, right, down, left, left, up, left, left, down, right, down, left, down, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='y4GVaZ_YK465kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2287
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2287 traffic_type=None
```

### `maze_line_6x6_adj_15.txt`

**Score:** 3.33%

**Ground Truth Solution:**
```
right, down, right, up, right, right, right, down, left, left, down, right, down, left, left, up, left, left, down, right, down, left, down, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
right, right, down, right, right, down, down, right, right, down, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, right, right, down, down, right, right, down, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zIGVaauJGbyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=756
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=756 traffic_type=None
```

### `maze_line_6x6_tokenized_15.txt`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, down, right, up, right, right, right, down, left, left, down, right, down, left, left, up, left, left, down, right, down, left, down, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, up, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, up, right, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left, up, up, up, right, down, down, left, left, up, right, right, down, down, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,up,right,down,down,left,left,up,up,right,right,down,down,left,left,up,up,up,right,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,up,up,up,right,down,down,left,left,up,right,right,down,down,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zYGVab_QO6nw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=1323
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1323 traffic_type=None
```

### `maze_occupancy_6x6_15.jpg`

**Score:** 1.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1779,
        license='',
        start_index=135,
        uri='https://americanarchive.org/catalog/cpb-aacip-b6e75cd0ce5'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0IGVacH4HoDHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=431,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=173
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=1081
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=431 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1081 traffic_type=None
```

### `maze_occupancy_6x6_15.json`

**Score:** 6.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down, right, right, right, right, up, right, right, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,right,right,right,right,up,right,right,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0oGVaeidAvfnnsEPornoiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1638
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=174 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1638 traffic_type=None
```

### `maze_occupancy_6x6_adj_15.json`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0oGVaczfM9qgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=4345,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4345
    ),
  ],
  total_token_count=4388
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=4345 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4345
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4388 traffic_type=None
```

### `maze_occupancy_6x6_adj_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='04GVafy8KKOF7M8P9PzH6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=1276,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1276
    ),
  ],
  total_token_count=1321
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=198 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=1276 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1276
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1321 traffic_type=None
```

### `maze_occupancy_6x6_ascii_15.txt`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, down, down, right, right, right, down, right, right, right, right, right, right, down, down, down, left, down, left, left, left, left, up, left, left, down, down, down, down, right, right, right, up, right, up, right, up, up, left, left, left, left, down, down, right, right, right, right, right, right, down, right, down, down, left, left, left, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,right,right,right,down,right,right,right,right,right,right,down,down,down,left,down,left,left,left,left,up,left,left,down,down,down,down,right,right,right,up,right,up,right,up,up,left,left,left,left,down,down,right,right,right,right,right,right,down,right,down,down,left,left,left,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1YGVaaejB4KN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=246
    ),
  ],
  total_token_count=896
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=173 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=896 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_15.txt`

**Score:** 6.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, left, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,left,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1oGVae36N8Pe7M8PidibyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2812
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=197 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2812 traffic_type=None
```

