# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_47.jpg` | **0.00%** | `input: 551 , ouput: 19` | `right, forward, right, forward, forward, left, forward, forward, right, forward` |
| `maze_line_3x3_47.json` | **0.00%** | `input: 774 , ouput: 17` | `right, forward, right, forward, forward, left, forward, right, forward` |
| `maze_line_3x3_adj_47.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, forward, left, forward, left, forward` |
| `maze_line_3x3_adj_47.txt` | **0.00%** | `input: 468 , ouput: 15` | `right, forward, right, forward, right, forward, left, forward` |
| `maze_line_3x3_tokenized_47.txt` | **0.00%** | `input: 439 , ouput: 25` | `right, forward, right, forward, down, forward, left, forward, down, right, forward, right, forward` |
| `maze_occupancy_3x3_47.jpg` | **0.00%** | `input: 546 , ouput: 31` | `right, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward` |
| `maze_occupancy_3x3_47.json` | **0.00%** | `input: 589 , ouput: 103` | `right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_47.json` | **0.00%** | `input: 1292 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_47.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward` |
| `maze_occupancy_3x3_ascii_47.txt` | **25.00%** | `input: 318 , ouput: 650` | `forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_47.txt` | **25.00%** | `input: 867 , ouput: 47` | `forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_47.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6JuVae3rE6zd7M8PqdSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=551,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=293
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=570
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=551 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=570 traffic_type=None
```

### `maze_line_3x3_47.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Left, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6JuVadyUOZC-nsEPxMmk4QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=791
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=309 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=791 traffic_type=None
```

### `maze_line_3x3_adj_47.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6ZuVaaT8FNqfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=853
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=280 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=853 traffic_type=None
```

### `maze_line_3x3_adj_47.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, right, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6puVabelBpjknsEPxt7C0AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=483
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=313 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=483 traffic_type=None
```

### `maze_line_3x3_tokenized_47.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, down, forward, left, forward, down, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Down, Forward, Left, Forward, Down, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6puVaf_2L6eN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=464
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=311 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=464 traffic_type=None
```

### `maze_occupancy_3x3_47.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='65uVabrZG8PPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=546,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=288
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=577
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=546 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=577 traffic_type=None
```

### `maze_occupancy_3x3_47.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, Right, forward, Right, forward, forward, forward, forward, Right, forward, forward, forward, forward, Left, forward, forward, Left, forward, forward, forward, forward, Right, forward, Right, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7JuVacXdBf7MkdUPkdfHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=103,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=692
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=289 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=103 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=692 traffic_type=None
```

### `maze_occupancy_3x3_adj_47.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7ZuVaajSPPnOnsEPkprNkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1942
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=280 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1942 traffic_type=None
```

### `maze_occupancy_3x3_adj_47.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='75uVab2dPNqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=1230
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=313 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1230 traffic_type=None
```

### `maze_occupancy_3x3_ascii_47.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8puVaazkEZHw7M8Pi4iBgAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=318,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=318
    ),
  ],
  total_token_count=968
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=288 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=318 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=318
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=968 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_47.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='85uVacqDBLyK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=914
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=312 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=914 traffic_type=None
```

