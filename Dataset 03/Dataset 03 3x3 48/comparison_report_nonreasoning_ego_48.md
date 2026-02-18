# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_48.jpg` | **0.00%** | `input: 551 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_48.json` | **0.00%** | `input: 774 , ouput: 15` | `right, forward, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_48.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_48.txt` | **0.00%** | `input: 468 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_48.txt` | **0.00%** | `input: 439 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_48.jpg` | **0.00%** | `input: 546 , ouput: 32` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, backward, right, forward, forward.` |
| `maze_occupancy_3x3_48.json` | **8.33%** | `input: 589 , ouput: 650` | `forward, right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_48.json` | **0.00%** | `input: 1292 , ouput: 650` | `right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left` |
| `maze_occupancy_3x3_adj_48.txt` | **0.00%** | `input: 580 , ouput: 49` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_ascii_48.txt` | **0.00%** | `input: 317 , ouput: 53` | `right, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_48.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_48.jpg`

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
        text='right,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AJyVabCuG6G-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_48.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
        text='Right, forward, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AZyVaYqNBY65kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=789
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=789 traffic_type=None
```

### `maze_line_3x3_adj_48.json`

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
        text='Right, forward, right, forward, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AZyVabmKKryK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=851
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=851 traffic_type=None
```

### `maze_line_3x3_adj_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ApyVac_5D6eN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='A5yVaZqVAtihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_48.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, backward, right, forward, forward.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, backward, right, forward, forward.'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='A5yVabOVM7-fkdUPtcm3yAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=32,
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
  total_token_count=578
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=32 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=578 traffic_type=None
```

### `maze_occupancy_3x3_48.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BZyVadnXLsyynsEP0d_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_48.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B5yVaY6uLtHMkdUPjY-7sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CJyVadmJHaSDkdUP5IaYkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=629
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=629 traffic_type=None
```

### `maze_occupancy_3x3_ascii_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CZyVaY7cCo65kdUPzNPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=370
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=370 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2837,
        license='',
        start_index=67,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='C5yVaffoA465kdUPzNPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

