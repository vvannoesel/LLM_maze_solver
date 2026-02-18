# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_25.jpg` | **4.17%** | `input: 434 , ouput: 19` | `right, down, right, down, left, down, right, right, down, right` |
| `maze_line_6x6_25.json` | **0.00%** | `input: 1809 , ouput: 23` | `down, down, right, down, right, down, right, right, down, right, down, right` |
| `maze_line_6x6_adj_25.json` | **20.83%** | `input: 2258 , ouput: 27` | `right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_25.txt` | **20.83%** | `input: 729 , ouput: 29` | `right, right, right, right, down, down, down, right, down, right, right, down, down, right, right` |
| `maze_line_6x6_tokenized_25.txt` | **4.17%** | `input: 673 , ouput: 650` | `right, down, right, down, right, down, right, down, left, down, left, up, left, down, right, right, up, right, up, up, left, up, left, down, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up` |
| `maze_occupancy_6x6_25.jpg` | **2.08%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right` |
| `maze_occupancy_6x6_25.json` | **16.67%** | `input: 988 , ouput: 47` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right` |
| `maze_occupancy_6x6_adj_25.json` | **20.83%** | `input: 4339 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_25.txt` | **20.83%** | `input: 1276 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_25.txt` | **14.58%** | `input: 248 , ouput: 37` | `right, right, right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, right, right` |
| `maze_occupancy_6x6_tokenized_25.txt` | **16.67%** | `input: 2162 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_25.jpg`

**Score:** 4.17%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, left, down, down, down, right, right, up, up, right, up, right, down, down, left, down, right
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nIKVadvrH-GlxN8Ppv3riAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
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
  total_token_count=453
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=453 traffic_type=None
```

### `maze_line_6x6_25.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, left, down, down, down, right, right, up, up, right, up, right, down, down, left, down, right
```

**Extracted Answer:**
```
down, down, right, down, right, down, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, down, right, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nYKVaafwFpy8xN8Pl5eC0Aw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_25.json`

**Score:** 20.83%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, left, down, down, down, right, right, up, up, right, up, right, down, down, left, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='noKVaeuLBLyLxs0Pjd6hiAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2285
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2285 traffic_type=None
```

### `maze_line_6x6_adj_25.txt`

**Score:** 20.83%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, left, down, down, down, right, right, up, up, right, up, right, down, down, left, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, right, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,right,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='noKVaYuCM7T4xs0P_M6xgA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=758
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=758 traffic_type=None
```

### `maze_line_6x6_tokenized_25.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
right, right, right, right, down, left, down, left, left, down, down, down, right, right, up, up, right, up, right, down, down, left, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, left, up, left, down, right, right, up, right, up, up, left, up, left, down, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, left, down, left, up, left, down, right, right, up, right, up, up, left, up, left, down, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up, left, up, left, down, right, right, up, up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oYKVaafOEZm0vdIPm7_0-Qo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_25.jpg`

**Score:** 2.08%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pIKVaZq0IOLSvdIP0O3TwQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_25.json`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pYKVaf2jD-K9xN8P27PqsQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1035
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1035 traffic_type=None
```

### `maze_occupancy_6x6_adj_25.json`

**Score:** 20.83%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='p4KVaa3CJqbZvdIPiYDjiQw' usage_metadata=GenerateContentResponseUsageMetadata(
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
) total_tokens=165 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4339 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4339
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4989 traffic_type=None
```

### `maze_occupancy_6x6_adj_25.txt`

**Score:** 20.83%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qYKVab_JBrvzxs0Ps7mRkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1276,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1276
    ),
  ],
  total_token_count=1926
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1276 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1276
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1926 traffic_type=None
```

### `maze_occupancy_6x6_ascii_25.txt`

**Score:** 14.58%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,down,down,right,down,down,down,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qYKVaaSKKpm0vdIPm7_0-Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=248,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=248
    ),
  ],
  total_token_count=285
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=248 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=248
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=285 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_25.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rIKVafL0C8HwvdIPhbD0iAw' usage_metadata=GenerateContentResponseUsageMetadata(
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

