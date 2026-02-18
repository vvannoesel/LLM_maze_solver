# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_37.jpg` | **21.43%** | `input: 434 , ouput: 27` | `down, right, down, right, down, right, up, right, down, down, left, down, right, right` |
| `maze_line_6x6_37.json` | **7.14%** | `input: 1809 , ouput: 29` | `down, down, right, right, down, down, right, right, up, right, down, down, right, down, down` |
| `maze_line_6x6_adj_37.json` | **7.14%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_37.txt` | **0.00%** | `input: 729 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_tokenized_37.txt` | **0.00%** | `input: 673 , ouput: 650` | `right, down, right, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, left, down, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up` |
| `maze_occupancy_6x6_37.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, down, right, up, right, down, right, down, down, left, down, left, down, right, right, up, right, down, right, down, down, right, up, right, up, right, down, down, right, down, left, down, left, down, right, right, right, up, right, down, right, up, right, up, right, down, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right` |
| `maze_occupancy_6x6_37.json` | **25.00%** | `input: 988 , ouput: 650` | `down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down` |
| `maze_occupancy_6x6_adj_37.json` | **7.14%** | `input: 4342 , ouput: 41` | `down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_37.txt` | **0.00%** | `input: 1278 , ouput: 263` | `right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_37.txt` | **0.00%** | `input: 254 , ouput: 650` | `right, right, down, down, right, right, right, down, down, left, left, down, down, right, right, right, right, right, up, up, left, left, down, down, right, right, right, right, right, up, up, up, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_37.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right` |

---

## Full LLM Responses

### `maze_line_6x6_37.jpg`

**Score:** 21.43%

**Ground Truth Solution:**
```
down, right, down, down, right, right, down, left, down, right, right, up, right, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, up, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right, down, right, up, right, down, down, left, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='coSVaZWbBYOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_37.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
down, right, down, down, right, right, down, left, down, right, right, up, right, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, up, right, down, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, down, right, right, up, right, down, down, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='c4SVadjOAq2WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1838
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1838 traffic_type=None
```

### `maze_line_6x6_adj_37.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
down, right, down, down, right, right, down, left, down, right, right, up, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='c4SVaYXXKf7MkdUP7NXHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, right, right, down, left, down, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dISVaZKtFLW5kdUP1c_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=748
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=748 traffic_type=None
```

### `maze_line_6x6_tokenized_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, right, right, down, left, down, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, left, down, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up, left, left, down, right, right, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,down,left,down,right,right,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,left,down,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,left,left,down,right,right,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='doSVaZu5INnn7M8P8fieuAs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_37.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, up, right, down, right, down, down, left, down, left, down, right, right, up, right, down, right, down, down, right, up, right, up, right, down, down, right, down, left, down, left, down, right, right, right, up, right, down, right, up, right, up, right, down, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right, down, right, up, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,up,right,down,right,down,down,left,down,left,down,right,right,up,right,down,right,down,down,right,up,right,up,right,down,down,right,down,left,down,left,down,right,right,right,up,right,down,right,up,right,up,right,down,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,down,right,up,right,up,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eISVaZTGF9HMkdUPyI67sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_37.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,down,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eYSVaYPwM_367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_37.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eoSVaezWF6zu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=4342,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4342
    ),
  ],
  total_token_count=4383
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=4342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4383 traffic_type=None
```

### `maze_occupancy_6x6_adj_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e4SVaaLpM_7MkdUPkdfHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=263,
  prompt_token_count=1278,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1278
    ),
  ],
  total_token_count=1541
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=263 candidates_tokens_details=None prompt_token_count=1278 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1278
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1541 traffic_type=None
```

### `maze_occupancy_6x6_ascii_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, left, left, down, down, right, right, right, right, right, up, up, left, left, down, down, right, right, right, right, right, up, up, up, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,left,left,down,down,right,right,right,right,right,up,up,left,left,down,down,right,right,right,right,right,up,up,up,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,up,left,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,up,left,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,right,up,up,up,up,up,left,left,left,left,left,down,down,right,right,right,right,right,down,down,left,left,left,left,down,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='foSVaY7yDuyOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=254,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=254
    ),
  ],
  total_token_count=904
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=254 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=254
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=904 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gISVaa3QEYKG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

