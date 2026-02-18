# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_19.jpg` | **0.00%** | `input: 551 , ouput: 9` | `right, forward, forward, right, forward` |
| `maze_line_3x3_19.json` | **0.00%** | `input: 774 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_adj_19.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, right, forward, left, forward` |
| `maze_line_3x3_adj_19.txt` | **0.00%** | `input: 468 , ouput: 27` | `right, forward, right, forward, forward, right, forward, left, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_19.txt` | **0.00%** | `input: 439 , ouput: 25` | `right, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward` |
| `maze_occupancy_3x3_19.jpg` | **12.50%** | `input: 546 , ouput: 27` | `forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_19.json` | **0.00%** | `input: 589 , ouput: 91` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_adj_19.json` | **0.00%** | `input: 1292 , ouput: 33` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_adj_19.txt` | **0.00%** | `input: 580 , ouput: 69` | `right, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_19.txt` | **0.00%** | `input: 317 , ouput: 85` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_tokenized_19.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_19.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZpeVada1A4yD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=9,
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
  total_token_count=560
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=9 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=560 traffic_type=None
```

### `maze_line_3x3_19.json`

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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZpeVaYnZGuO9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_19.json`

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
        text='Right, forward, right, forward, right, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Z5eVaZj6ArW5kdUP1c_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, left, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Right, Forward, Left, Forward, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Z5eVabmMH9qfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=495
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=495 traffic_type=None
```

### `maze_line_3x3_tokenized_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aJeVaaKLBq7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_19.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aJeVaautNtqgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_19.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aZeVacCcHbnjnsEPxoKX6AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=91,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=680
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=91 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=680 traffic_type=None
```

### `maze_occupancy_3x3_adj_19.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aZeVabnoN4DHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='apeVadLbLbyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=69,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=649
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=69 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=649 traffic_type=None
```

### `maze_occupancy_3x3_ascii_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='a5eVaeCdINihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=402
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=402 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bZeVabDsFJPe7M8PjqaxkQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

