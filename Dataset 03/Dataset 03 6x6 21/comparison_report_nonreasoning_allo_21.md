# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_21.jpg` | **0.00%** | `input: 434 , ouput: 27` | `right, down, right, down, right, down, right, down, left, down, right, right, down, right` |
| `maze_line_6x6_21.json` | **8.33%** | `input: 1809 , ouput: 21` | `down, right, down, right, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_21.json` | **4.17%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_21.txt` | **0.00%** | `input: 729 , ouput: 29` | `right, right, right, down, right, down, down, right, down, down, right, right, right, down, right` |
| `maze_line_6x6_tokenized_21.txt` | **0.00%** | `input: 673 , ouput: 51` | `right, down, down, right, right, up, right, down, down, left, down, right, right, up, up, right, down, down, down, right, right, up, up, up, left, down` |
| `maze_occupancy_6x6_21.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, down, right, down, right, down, right, up, right, down, down, right, down, left, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right` |
| `maze_occupancy_6x6_21.json` | **0.00%** | `input: 988 , ouput: 650` | `right, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down` |
| `maze_occupancy_6x6_adj_21.json` | **4.17%** | `input: 4345 , ouput: 61` | `down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_21.txt` | **4.17%** | `input: 1276 , ouput: 65` | `down, down, down, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_6x6_ascii_21.txt` | **0.00%** | `input: 240 , ouput: 650` | `right, right, down, down, right, right, right, down, down, right, right, right, right, right, down, down, left, left, left, left, down, right, right, right, down, right, right, right, down, left, left, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down` |
| `maze_occupancy_6x6_tokenized_21.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, down, right, right, down, right, right, right, down, right, down, right, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right` |

---

## Full LLM Responses

### `maze_line_6x6_21.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, right, down, down, left, left, down, left, left, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QIKVaZupBu21xN8P7oq10Qw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
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
  total_token_count=461
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=461 traffic_type=None
```

### `maze_line_6x6_21.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, right, down, down, left, left, down, left, left, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
down, right, down, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right, right, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QIKVabW1PN7mxs0P4czy8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1830
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1830 traffic_type=None
```

### `maze_line_6x6_adj_21.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, right, down, down, left, left, down, left, left, left, down, right, right, right, right, up, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QYKVabCNIYa8xN8Puu-IoAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2277
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2277 traffic_type=None
```

### `maze_line_6x6_adj_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, right, down, down, left, left, down, left, left, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, down, right, down, down, right, down, down, right, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, down, right, down, down, right, down, down, right, right, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QoKVab6XFrvzxs0Ps7mRkAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, right, down, down, left, left, down, left, left, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, down, right, right, up, right, down, down, left, down, right, right, up, up, right, down, down, down, right, right, up, up, up, left, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, right, up, right, down, down, left, down, right, right, up, up, right, down, down, down, right, right, up, up, up, left, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Q4KVadrSDfWNxs0PtLSW2QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=724
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=724 traffic_type=None
```

### `maze_occupancy_6x6_21.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, down, right, down, right, up, right, down, down, right, down, left, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, down, right, down, right, up, right, down, down, right, down, left, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RYKVaYbvMZme28oPkrijmAw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_21.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R4KVaf2WKP6o28oP8YeKkQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_21.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SIKVaeuLGpXIvdIP-oyG2AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=4345,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4345
    ),
  ],
  total_token_count=4406
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=4345 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4345
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4406 traffic_type=None
```

### `maze_occupancy_6x6_adj_21.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SYKVaYOsFrnwxN8P8smN8QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=65,
  prompt_token_count=1276,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1276
    ),
  ],
  total_token_count=1341
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=65 candidates_tokens_details=None prompt_token_count=1276 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1276
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1341 traffic_type=None
```

### `maze_occupancy_6x6_ascii_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, right, right, right, right, right, down, down, left, left, left, left, down, right, right, right, down, right, right, right, down, left, left, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down, left, left, left, left, down, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,right,right,right,right,right,down,down,left,left,left,left,down,right,right,right,down,right,right,right,down,left,left,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,left,left,left,left,down,right,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='S4KVaZKTA6S9xN8PvoPm4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
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
) total_tokens=173 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=240 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=240
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=890 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, down, right, right, right, down, right, down, right, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, right, down, right, right, right, down, right, down, right, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TIKVaZzpIsPgvdIP96mU8Qw' usage_metadata=GenerateContentResponseUsageMetadata(
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

