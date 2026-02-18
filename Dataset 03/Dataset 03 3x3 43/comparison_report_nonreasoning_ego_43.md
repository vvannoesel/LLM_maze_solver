# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_43.jpg` | **25.00%** | `input: 551 , ouput: 15` | `forward, right, forward, forward, right, forward, left, forward` |
| `maze_line_3x3_43.json` | **25.00%** | `input: 774 , ouput: 15` | `forward, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_43.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, right, forward, left, forward, forward` |
| `maze_line_3x3_adj_43.txt` | **0.00%** | `input: 468 , ouput: 17` | `right, forward, right, forward, forward, right, forward, left, forward` |
| `maze_line_3x3_tokenized_43.txt` | **0.00%** | `input: 439 , ouput: 650` | `right, forward, right, forward, down, forward, down, left, forward, up, forward, right, forward, right, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward` |
| `maze_occupancy_3x3_43.jpg` | **12.50%** | `input: 546 , ouput: 25` | `forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_43.json` | **0.00%** | `input: 589 , ouput: 49` | `right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_43.json` | **0.00%** | `input: 1292 , ouput: 49` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_43.txt` | **0.00%** | `input: 580 , ouput: 45` | `right, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_43.txt` | **0.00%** | `input: 317 , ouput: 63` | `right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_tokenized_43.txt` | **0.00%** | `input: 867 , ouput: 75` | `right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_43.jpg`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k5uVafm9OP6o28oPm8yLkQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_43.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lJuVafrGGKS1xN8P7ILa-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_43.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, right, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lJuVaYv0Otqb28oPgemZoQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, right, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lZuVacelFvHzxs0P47mHuA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=485
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=485 traffic_type=None
```

### `maze_line_3x3_tokenized_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, left
```

**Extracted Answer:**
```
right, forward, right, forward, down, forward, down, left, forward, up, forward, right, forward, right, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, down, forward, down, left, forward, up, forward, right, forward, right, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward, left, forward, up, forward, up, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='l5uVaa24G_HXvdIPssLX-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=1089
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1089 traffic_type=None
```

### `maze_occupancy_3x3_43.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mJuVaZ-UFfnTxN8Pjof32Qc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
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
  total_token_count=571
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=571 traffic_type=None
```

### `maze_occupancy_3x3_43.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mZuVaakRu_PGzQ_fx56YCg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=638
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=638 traffic_type=None
```

### `maze_occupancy_3x3_adj_43.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mZuVadmlL_yc28oP7rOrsAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1341
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1341 traffic_type=None
```

### `maze_occupancy_3x3_adj_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mpuVaeC3EMTdvdIPxenY-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=625
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=625 traffic_type=None
```

### `maze_occupancy_3x3_ascii_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,left,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mpuVafOlMeK9xN8P27PqsQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=63,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=380
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=63 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=380 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m5uVaeidFfHXvdIPssLX-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=75,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=942
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=75 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=942 traffic_type=None
```

