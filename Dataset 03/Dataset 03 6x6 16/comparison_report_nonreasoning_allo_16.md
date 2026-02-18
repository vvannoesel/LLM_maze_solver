# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_16.jpg` | **0.00%** | `input: 434 , ouput: 23` | `right, down, right, down, right, down, right, down, left, down, right, right` |
| `maze_line_6x6_16.json` | **4.17%** | `input: 1809 , ouput: 23` | `down, down, right, down, right, right, up, right, down, down, right, down` |
| `maze_line_6x6_adj_16.json` | **4.17%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_16.txt` | **4.17%** | `input: 729 , ouput: 23` | `down, down, right, right, down, down, right, right, down, down, right, right` |
| `maze_line_6x6_tokenized_16.txt` | **0.00%** | `input: 673 , ouput: 31` | `right, down, down, down, down, down, right, right, right, right, up, right, up, up, up, up` |
| `maze_occupancy_6x6_16.jpg` | **2.08%** | `input: 431 , ouput: 650` | `down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down` |
| `maze_occupancy_6x6_16.json` | **0.00%** | `input: 988 , ouput: 650` | `right, down, right, right, down, down, down, right, down, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_16.json` | **4.17%** | `input: 4345 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_16.txt` | **0.00%** | `input: 1276 , ouput: 45` | `right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_16.txt` | **0.00%** | `input: 253 , ouput: 650` | `right, right, down, down, right, right, down, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, up, right, right, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down` |
| `maze_occupancy_6x6_tokenized_16.txt` | **2.08%** | `input: 2162 , ouput: 650` | `down, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_16.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, down, right, up, up, right, up, right, down, down, left, down, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2IGVaaiAKa7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=457
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=457 traffic_type=None
```

### `maze_line_6x6_16.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, up, right, down, down, down, right, up, up, right, up, right, down, down, left, down, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
down, down, right, down, right, right, up, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, right, up, right, down, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2YGVae_KD-jpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_16.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, up, right, down, down, down, right, up, up, right, up, right, down, down, left, down, down, left, left, down, right, right, right
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
        text='down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2YGVadLuN4WF7M8PnoeMqQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_16.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, up, right, down, down, down, right, up, up, right, up, right, down, down, left, down, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, down, right, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2oGVabOYLIyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=752
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=752 traffic_type=None
```

### `maze_line_6x6_tokenized_16.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, down, right, up, up, right, up, right, down, down, left, down, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, right, right, right, right, up, right, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,right,right,right,right,up,right,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='24GVaeTdEcjl7M8P9OOViAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=704
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=704 traffic_type=None
```

### `maze_occupancy_6x6_16.jpg`

**Score:** 2.08%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3YGVadC2B_jHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_16.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, down, down, down, right, down, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,down,down,right,down,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='34GVacewFr-fkdUPtcm3yAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_16.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4YGVaYC8H_fnnsEPornoiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4345,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4345
    ),
  ],
  total_token_count=4995
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4345 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4345
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4995 traffic_type=None
```

### `maze_occupancy_6x6_adj_16.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4oGVaYzcE9z07M8PwPSugQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_16.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, up, right, right, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down, left, down, right, right, down, down, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,up,right,right,down,down,down,right,right,up,up,right,right,down,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,left,down,right,right,down,down,right,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5IGVaY6GKY65kdUPzNPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=253,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=253
    ),
  ],
  total_token_count=903
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=253 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=253
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=903 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_16.txt`

**Score:** 2.08%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='54GVacD9AY65kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

