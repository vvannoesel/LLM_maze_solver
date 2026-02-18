# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_14.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_14.json` | **0.00%** | `input: 774 , ouput: 17` | `right, forward, right, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_14.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, backward, forward, forward, left, forward` |
| `maze_line_3x3_adj_14.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_14.txt` | **0.00%** | `input: 439 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_14.jpg` | **0.00%** | `input: 546 , ouput: 33` | `right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_14.json` | **16.67%** | `input: 589 , ouput: 75` | `forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_adj_14.json` | **8.33%** | `input: 1298 , ouput: 650` | `forward, right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_14.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_14.txt` | **0.00%** | `input: 319 , ouput: 650` | `right, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_tokenized_14.txt` | **0.00%** | `input: 867 , ouput: 119` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_14.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FZeVabm9O-KAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
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
  total_token_count=566
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=566 traffic_type=None
```

### `maze_line_3x3_14.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FpeVaa-wF465kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_14.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, backward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,backward,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F5eVaeoj2efszw_x-J64Cw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_14.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
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
        text='right, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F5eVabHSH9iCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=481
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=481 traffic_type=None
```

### `maze_line_3x3_tokenized_14.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GJeVad_MEqvgnsEP8Mu7uAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=450
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=450 traffic_type=None
```

### `maze_occupancy_3x3_14.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GZeVabvNAqjlnsEP1bugwAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
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
  total_token_count=579
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=579 traffic_type=None
```

### `maze_occupancy_3x3_14.json`

**Score:** 16.67%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,left,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,forward,right,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GZeVad2aKZnqkdUP57jkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=75,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=664
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=75 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=664 traffic_type=None
```

### `maze_occupancy_3x3_adj_14.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G5eVaZfGLqjlnsEP1bugwAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1948
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1948 traffic_type=None
```

### `maze_occupancy_3x3_adj_14.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2801,
        license='',
        start_index=25,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HpeVacjzAqOF7M8P9PzH6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_14.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='H5eVafrHM-jpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=319,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=319
    ),
  ],
  total_token_count=969
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=319 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=319
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=969 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_14.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IJeVadLxLtiCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=119,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=986
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=119 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=986 traffic_type=None
```

