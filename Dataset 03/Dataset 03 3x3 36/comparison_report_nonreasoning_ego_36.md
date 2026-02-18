# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_36.jpg` | **0.00%** | `input: 551 , ouput: 13` | `right, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_36.json` | **0.00%** | `input: 774 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_36.json` | **0.00%** | `input: 836 , ouput: 13` | `right, right, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_36.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_36.txt` | **0.00%** | `input: 439 , ouput: 15` | `right, forward, forward, right, forward, forward, right, forward` |
| `maze_occupancy_3x3_36.jpg` | **0.00%** | `input: 546 , ouput: 23` | `forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_36.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_36.json` | **0.00%** | `input: 1292 , ouput: 33` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_36.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_36.txt` | **0.00%** | `input: 315 , ouput: 41` | `right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_36.txt` | **0.00%** | `input: 867 , ouput: 650` | `forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_36.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='epqVabX1Fo65kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
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
  total_token_count=564
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=564 traffic_type=None
```

### `maze_line_3x3_36.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
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
        text='right,forward,right,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e5qVaZyYG_KcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=785
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=785 traffic_type=None
```

### `maze_line_3x3_adj_36.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
```

**Extracted Answer:**
```
right, right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,forward,right,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e5qVaebAO6eN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_36.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fJqVaZDCMdHMkdUPyI67sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_36.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, left, left
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fZqVad3IGrzhnsEPwLCgiQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=454
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=454 traffic_type=None
```

### `maze_occupancy_3x3_36.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fpqVadbsDJC-nsEPxMmk4QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=569
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=569 traffic_type=None
```

### `maze_occupancy_3x3_36.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gJqVaaDACsPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_36.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gJqVaZOLMsPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1325
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1325 traffic_type=None
```

### `maze_occupancy_3x3_adj_36.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gpqVadeOL5nqkdUP57jkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_36.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='g5qVaeioFKL17M8Pt6zc8AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=356
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=356 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_36.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Forward,forward,right,forward,forward,forward,right,forward,forward,left,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hZqVadyYJMPe7M8PidibyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

