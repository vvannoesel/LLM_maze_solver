# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_21.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_21.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_21.json` | **0.00%** | `input: 836 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_21.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_21.txt` | **0.00%** | `input: 439 , ouput: 17` | `right, forward, right, forward, left, forward, forward, right, forward` |
| `maze_occupancy_3x3_21.jpg` | **8.33%** | `input: 546 , ouput: 29` | `forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_21.json` | **0.00%** | `input: 589 , ouput: 125` | `right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_21.json` | **8.33%** | `input: 1292 , ouput: 650` | `forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right` |
| `maze_occupancy_3x3_adj_21.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, right, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, left, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_ascii_21.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, right, forward, forward, forward, backward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_21.txt` | **8.33%** | `input: 867 , ouput: 650` | `forward, right, forward, right, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward` |

---

## Full LLM Responses

### `maze_line_3x3_21.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i5eVabyYEdihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_21.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
        text='right,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i5eVaf7cK4KN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_21.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
        text='Right, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jJeVaemWHYKN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
        text='Right, Forward, Right, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jZeVadPECZPe7M8PjqaxkQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, left, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jZeVafb-L9qfnsEPxvyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=456
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=456 traffic_type=None
```

### `maze_occupancy_3x3_21.jpg`

**Score:** 8.33%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jpeVafWgIoKN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
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
  total_token_count=575
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=575 traffic_type=None
```

### `maze_occupancy_3x3_21.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j5eVafXSF5Pe7M8PjqaxkQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=125,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=714
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=125 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=714 traffic_type=None
```

### `maze_occupancy_3x3_adj_21.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kZeVaeXhKNqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, right, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, left, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Right, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Left, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k5eVaZKhJanw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, backward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Forward,Backward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lZeVac3oB7njnsEPxoKX6AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=967
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=967 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_21.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, right, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Forward,Right,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='l5eVaZ_8CbyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1517
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1517 traffic_type=None
```

