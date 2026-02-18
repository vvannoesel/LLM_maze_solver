# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_11.jpg` | **0.00%** | `input: 551 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_11.json` | **0.00%** | `input: 774 , ouput: 19` | `right, forward, right, forward, forward, right, forward, left, forward, forward` |
| `maze_line_3x3_adj_11.json` | **0.00%** | `input: 836 , ouput: 19` | `right, forward, forward, right, forward, left, forward, forward, left, forward` |
| `maze_line_3x3_adj_11.txt` | **0.00%** | `input: 468 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_tokenized_11.txt` | **0.00%** | `input: 439 , ouput: 35` | `right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_11.jpg` | **0.00%** | `input: 546 , ouput: 40` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward.` |
| `maze_occupancy_3x3_11.json` | **0.00%** | `input: 589 , ouput: 75` | `right, forward, right, forward, forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_11.json` | **0.00%** | `input: 1292 , ouput: 650` | `right, forward, right, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_11.txt` | **0.00%** | `input: 580 , ouput: 73` | `right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_11.txt` | **25.00%** | `input: 318 , ouput: 650` | `forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_tokenized_11.txt` | **0.00%** | `input: 867 , ouput: 107` | `right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_11.jpg`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VJaVaeukN_Dm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
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
  total_token_count=562
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=562 traffic_type=None
```

### `maze_line_3x3_11.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, right, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VZaVady8Iafx7M8PiZPD-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=793
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=793 traffic_type=None
```

### `maze_line_3x3_adj_11.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, left, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,left,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VpaVadekAbW5kdUP1c_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=855
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=855 traffic_type=None
```

### `maze_line_3x3_adj_11.txt`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VpaVaYy_J-KAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_11.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V5aVaYnsELW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=474
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=474 traffic_type=None
```

### `maze_occupancy_3x3_11.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward.'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WJaVaYyHB4qjkdUPl43u2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=40,
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
  total_token_count=586
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=40 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=586 traffic_type=None
```

### `maze_occupancy_3x3_11.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,forward,left,forward,left,forward,forward,forward,right,forward,right,forward,forward,forward,right,forward,forward,left,forward,left,forward,forward,forward,right,forward,right,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WJaVaZrCM8yynsEP0d_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_11.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WpaVaajGMPfonsEPwaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_11.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='W5aVadqFMvjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=73,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=653
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=73 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=653 traffic_type=None
```


### `maze_occupancy_3x3_ascii_11.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lZaVadSHPNHMkdUPjY-7sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_11.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lpaVacGPPNWbkdUPueCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=107,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=974
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=107 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=974 traffic_type=None
```

