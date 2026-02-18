# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_50.jpg` | **0.00%** | `input: 551 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_50.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_50.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, right, forward, left, forward` |
| `maze_line_3x3_adj_50.txt` | **0.00%** | `input: 468 , ouput: 19` | `right, forward, right, forward, forward, left, forward, left, forward, forward` |
| `maze_line_3x3_tokenized_50.txt` | **0.00%** | `input: 439 , ouput: 23` | `right, forward, right, forward, backward, left, forward, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_50.jpg` | **12.50%** | `input: 546 , ouput: 27` | `forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_50.json` | **0.00%** | `input: 589 , ouput: 51` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_50.json` | **0.00%** | `input: 1292 , ouput: 41` | `right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_50.txt` | **0.00%** | `input: 580 , ouput: 41` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, left, forward, forward, left, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_50.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_tokenized_50.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left` |

---

## Full LLM Responses

### `maze_line_3x3_50.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FZyVacaPFujpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_50.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FZyVaYzILvKcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_50.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
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
        text='right,forward,right,forward,right,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FpyVaaOHENuxnsEPg_7zyAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, left, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FpyVaauMMbnjnsEPxoKX6AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=487
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=487 traffic_type=None
```

### `maze_line_3x3_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
right, forward, right, forward, backward, left, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Backward, Left, Forward, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F5yVaYWkDI65kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=462
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=462 traffic_type=None
```

### `maze_occupancy_3x3_50.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F5yVaZ7cK9WbkdUPueCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
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
  total_token_count=573
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=573 traffic_type=None
```

### `maze_occupancy_3x3_50.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GJyVadPFDvT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=640
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=640 traffic_type=None
```

### `maze_occupancy_3x3_adj_50.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GJyVab7jNqnw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1333
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1333 traffic_type=None
```

### `maze_occupancy_3x3_adj_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, left, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GZyVaZeJF5zw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=621
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=621 traffic_type=None
```

### `maze_occupancy_3x3_ascii_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G5yVaZPkG9qgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HZyVaeTEIarw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

