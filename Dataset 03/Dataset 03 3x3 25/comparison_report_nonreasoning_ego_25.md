# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_25.jpg` | **0.00%** | `input: 551 , ouput: 21` | `right, forward, right, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_line_3x3_25.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_25.json` | **0.00%** | `input: 836 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_25.txt` | **0.00%** | `input: 468 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_tokenized_25.txt` | **0.00%** | `input: 439 , ouput: 71` | `right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, right, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, left, forward, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_25.jpg` | **0.00%** | `input: 546 , ouput: 47` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_25.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_25.json` | **0.00%** | `input: 1292 , ouput: 650` | `right, forward, right, forward, right, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_adj_25.txt` | **0.00%** | `input: 580 , ouput: 51` | `right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_25.txt` | **0.00%** | `input: 318 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_25.txt` | **0.00%** | `input: 867 , ouput: 55` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_25.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, left, forward, forward, right, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ypeVaYfQJazu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
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
  total_token_count=572
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=572 traffic_type=None
```

### `maze_line_3x3_25.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='y5eVaaa6HvDm7M8Po7vO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=787
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=787 traffic_type=None
```

### `maze_line_3x3_adj_25.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='y5eVacODOY65kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=849
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=849 traffic_type=None
```

### `maze_line_3x3_adj_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zJeVaYyUHZHw7M8Pi4iBgAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=479
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=479 traffic_type=None
```

### `maze_line_3x3_tokenized_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, right, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, left, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward, right, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, left, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zZeVaciDB_fo7M8PipSSoQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=71,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=510
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=71 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=510 traffic_type=None
```

### `maze_occupancy_3x3_25.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zZeVafy-OtiCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
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
  total_token_count=593
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=593 traffic_type=None
```

### `maze_occupancy_3x3_25.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='z5eVaeG9H4yD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=1239
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1239 traffic_type=None
```

### `maze_occupancy_3x3_adj_25.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0ZeVacz-Je3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0peVaYv5ErzhnsEPwLCgiQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=631
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=631 traffic_type=None
```

### `maze_occupancy_3x3_ascii_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='05eVaam-MKPwnsEPgLOouAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1JeVafrREqSDkdUP5IaYkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=922
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=922 traffic_type=None
```

