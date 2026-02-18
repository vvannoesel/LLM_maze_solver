# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_27.jpg` | **0.00%** | `input: 551 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_27.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, right, forward, right` |
| `maze_line_3x3_adj_27.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_27.txt` | **0.00%** | `input: 468 , ouput: 17` | `right, forward, forward, right, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_27.txt` | **0.00%** | `input: 439 , ouput: 34` | `right, forward, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward.` |
| `maze_occupancy_3x3_27.jpg` | **0.00%** | `input: 546 , ouput: 29` | `right, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_27.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward` |
| `maze_occupancy_3x3_adj_27.json` | **0.00%** | `input: 1292 , ouput: 131` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_27.txt` | **0.00%** | `input: 580 , ouput: 31` | `forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_27.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward` |
| `maze_occupancy_3x3_tokenized_27.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left` |

---

## Full LLM Responses

### `maze_line_3x3_27.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='L5iVaZmWBoKG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_27.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='L5iVab_SIb-fkdUPtcm3yAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_27.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MJiVaYL9CP367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MJiVaYq1IrW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, Right, forward, Right, forward, Right, forward, Left, forward, Left, forward, Left, forward, Left, forward.'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MZiVadT3D62WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=34,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=473
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=34 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=473 traffic_type=None
```

### `maze_occupancy_3x3_27.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MpiVaYDIAtqfnsEPxvyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_27.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M5iVaYGFOoyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_27.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NZiVaaaSCZzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=131,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1423
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=131 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1423 traffic_type=None
```

### `maze_occupancy_3x3_adj_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NZiVaee0IseC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=611
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=611 traffic_type=None
```

### `maze_occupancy_3x3_ascii_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='N5iVaZHAMPjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OZiVacWACpjknsEPxt7C0AU' usage_metadata=GenerateContentResponseUsageMetadata(
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

