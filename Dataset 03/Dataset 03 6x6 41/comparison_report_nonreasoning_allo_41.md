# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_41.jpg` | **3.57%** | `input: 434 , ouput: 35` | `right, down, right, down, down, right, up, right, down, down, left, down, right, right, up, right, down, down` |
| `maze_line_6x6_41.json` | **0.00%** | `input: 1809 , ouput: 23` | `down, down, right, right, down, down, right, right, down, down, right, right` |
| `maze_line_6x6_adj_41.json` | **14.29%** | `input: 2258 , ouput: 35` | `right, right, down, down, down, down, right, right, right, down, down, down, right, right, down, down, right, right` |
| `maze_line_6x6_adj_41.txt` | **10.71%** | `input: 729 , ouput: 21` | `right, right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_tokenized_41.txt` | **3.57%** | `input: 673 , ouput: 650` | `right, down, right, right, down, right, down, down, left, down, left, left, up, left, up, up, right, up, right, down, right, down, down, left, left, up, left, up, up, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up` |
| `maze_occupancy_6x6_41.jpg` | **1.79%** | `input: 431 , ouput: 650` | `right, down, right, down, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down, right, right, up, left, up, right, up, right, up, right, up, left, up, left, up, right, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, left, up, left, up, right, up, right, right, down, down, left, down, left, down, left, down, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right` |
| `maze_occupancy_6x6_41.json` | **7.14%** | `input: 988 , ouput: 650` | `right, right, right, right, right, down, down, right, down, down, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right` |
| `maze_occupancy_6x6_adj_41.json` | **8.93%** | `input: 4344 , ouput: 650` | `right, right, right, right, down, right, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right` |
| `maze_occupancy_6x6_adj_41.txt` | **14.29%** | `input: 1280 , ouput: 650` | `right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down` |
| `maze_occupancy_6x6_ascii_41.txt` | **10.71%** | `input: 250 , ouput: 155` | `right, right, right, right, down, down, left, down, down, right, right, down, right, right, right, right, right, right, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_41.txt` | **7.14%** | `input: 2162 , ouput: 650` | `right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_6x6_41.jpg`

**Score:** 3.57%

**Ground Truth Solution:**
```
right, right, down, down, left, up, left, down, down, right, down, down, right, right, right, up, left, left, up, right, up, up, right, down, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, up, right, down, down, left, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,up,right,down,down,left,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0oSVaeqdDcPwnsEPpffzuQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
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
  total_token_count=469
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=469 traffic_type=None
```

### `maze_line_6x6_41.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, left, up, left, down, down, right, down, down, right, right, right, up, left, left, up, right, up, up, right, down, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='04SVaeaDDNHMkdUPjY-7sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_41.json`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, right, down, down, left, up, left, down, down, right, down, down, right, right, right, up, left, left, up, right, up, up, right, down, right, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, right, right, right, down, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,right,right,right,down,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='04SVadevN62WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2293
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2293 traffic_type=None
```

### `maze_line_6x6_adj_41.txt`

**Score:** 10.71%

**Ground Truth Solution:**
```
right, right, down, down, left, up, left, down, down, right, down, down, right, right, right, up, left, left, up, right, up, up, right, down, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1ISVaYqwKIKN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=750
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=750 traffic_type=None
```

### `maze_line_6x6_tokenized_41.txt`

**Score:** 3.57%

**Ground Truth Solution:**
```
right, right, down, down, left, up, left, down, down, right, down, down, right, right, right, up, left, left, up, right, up, up, right, down, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, right, down, right, down, down, left, down, left, left, up, left, up, up, right, up, right, down, right, down, down, left, left, up, left, up, up, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up, up, right, right, right, right, down, down, right, down, down, left, left, up, left, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,right,down,down,left,down,left,left,up,left,up,up,right,up,right,down,right,down,down,left,left,up,left,up,up,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,up,right,right,right,right,down,down,right,down,down,left,left,up,left,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1oSVaaP1EMeC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_41.jpg`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down, right, right, up, left, up, right, up, right, up, right, up, left, up, left, up, right, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, left, up, left, up, right, up, right, right, down, down, left, down, left, down, left, down, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down, right, right, up, left, up, right, up, right, up, right, up, left, up, left, up, right, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, left, up, left, up, right, up, right, right, down, down, left, down, left, down, left, down, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right, right, down, right, up, right, up, right, up, left, up, right, right, down, right, down, left, down, left, down, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2ISVacG8L6vgnsEP8Mu7uAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_41.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, right, down, down, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,right,down,down,left,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2oSVafLlFueGkdUPsqK74AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_41.json`

**Score:** 8.93%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, right, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,right,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3ISVacjiJI65kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4344,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4344
    ),
  ],
  total_token_count=4994
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4344 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4344
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4994 traffic_type=None
```

### `maze_occupancy_6x6_adj_41.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3oSVaauKJPfonsEPuaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1280,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1280
    ),
  ],
  total_token_count=1930
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1280 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1280
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1930 traffic_type=None
```

### `maze_occupancy_6x6_ascii_41.txt`

**Score:** 10.71%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, left, down, down, right, right, down, right, right, right, right, right, right, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,left,down,down,right,right,down,right,right,right,right,right,right,up,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='34SVaZKdJdHMkdUPy8C6kAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=155,
  prompt_token_count=250,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=250
    ),
  ],
  total_token_count=405
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=155 candidates_tokens_details=None prompt_token_count=250 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=250
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=405 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_41.txt`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4YSVaYTNCKzd7M8PqdSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

