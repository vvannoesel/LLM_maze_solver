# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_31.jpg` | **0.00%** | `input: 551 , ouput: 21` | `right, forward, forward, right, forward, forward, left, forward, left, forward, forward` |
| `maze_line_3x3_31.json` | **12.50%** | `input: 774 , ouput: 17` | `forward, right, forward, right, forward, left, forward, left, forward` |
| `maze_line_3x3_adj_31.json` | **0.00%** | `input: 836 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_31.txt` | **0.00%** | `input: 468 , ouput: 25` | `right, forward, right, forward, right, forward, left, forward, forward, left, forward, left, forward` |
| `maze_line_3x3_tokenized_31.txt` | **0.00%** | `input: 439 , ouput: 19` | `right, forward, right, forward, forward, left, forward, forward, left, forward` |
| `maze_occupancy_3x3_31.jpg` | **0.00%** | `input: 546 , ouput: 39` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_31.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_adj_31.json` | **0.00%** | `input: 1292 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_31.txt` | **0.00%** | `input: 580 , ouput: 35` | `right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward` |
| `maze_occupancy_3x3_ascii_31.txt` | **0.00%** | `input: 320 , ouput: 47` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_31.txt` | **0.00%** | `input: 867 , ouput: 650` | `the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., here's, the, path:, 1., the, agent, is, at, (1, 1), facing, south., the, cell, below, is, (2, 1), which, is, blank., move, forward., (now, at, (2, 1), facing, south)., 2., the, agent, is, at, (2, 1), facing, south., the, cell, below, is, (3, 1), which, is, blank., move, forward., (now, at, (3, 1), facing, south)., 3., the, agent, is, at, (3, 1), facing, south., the, cell, below, is, (4, 1), which, is, blank., move, forward., (now, at, (4, 1), facing, south)., 4., the, agent, is, at, (4, 1), facing, south., the, cell, below, is, (5, 1), which, is, blank., move, forward., (now, at, (5, 1), facing, south)., 5., the, agent, is, at, (5, 1), facing, south., the, cell, to, the, right, is, (5, 2), which, is, blank., turn, right., (now, at, (5, 1), facing, west)., 6., the, agent, is, at, (5, 1), facing, west., the, cell, to, the, right, is, (5, 2), which, is, blank., move, forward., (now, at, (5, 2), facing, west)., 7., the, agent, is, at, (5, 2), facing, west., the, cell, to, the, right, is, (5, 3), which, is, blank., move, forward., (now, at, (5, 3), facing, west)., 8., the, agent, is, at, (5, 3), facing, west., the, cell, to, the, right, is, (5, 4), which, is, occupied., turn, right., (now, at, (5, 3), facing, north)., 9., the, agent, is, at, (5, 3), facing, north., the, cell, to, the, right, is, (5, 4), which, is, occupied., the, cell, ahead, is, (4, 3), which, is, blank., move, forward., (now, at, (4, 3), facing, north)., 10., the, agent, is, at, (4, 3), facing, north., the, cell, to, the, right, is, (4, 4), which, is, occupied., the, cell, ahead, is, (3, 3), which, is, blank., move, forward., (now, at, (3, 3), facing, north)., 11., the, agent, is, at, (3, 3), facing, north., the, cell, to, the, right, is, (3, 4), which, is, occupied., the, cell, ahead, is, (2, 3), which, is, blank., move, forward., (now, at, (2, 3), facing, north)., 12., the, agent, is, at, (2, 3), facing, north., the, cell, to, the, right, is, (2, 4), which, is, occupied., the, cell, ahead, is, (1, 3), which, is, blank., move, forward., (now, at, (1, 3), facing, north)., 13., the, agent, is, at, (1, 3), facing, north., the, cell, to, the, right, is, (1, 4), which, is, blank., turn, right., (now, at` |

---

## Full LLM Responses

### `maze_line_3x3_31.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i5mVab6kLtHMkdUPyI67sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_31.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
forward, right, forward, right, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,right,forward,left,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jJmVac6sDaeN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_31.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jJmVac7NKffonsEPwaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_31.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, right, forward, left, forward, forward, left, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jZmVae62Ea7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=493
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=493 traffic_type=None
```

### `maze_line_3x3_tokenized_31.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jZmVaZTXNqPwnsEPgLOouAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=458
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=458 traffic_type=None
```

### `maze_occupancy_3x3_31.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jpmVaa3uJtiCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
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
  total_token_count=585
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=585 traffic_type=None
```

### `maze_occupancy_3x3_31.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kJmVacL3HLW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_31.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kpmVaaieKNqgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_31.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k5mVafGJEceC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=615
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=615 traffic_type=None
```

### `maze_occupancy_3x3_ascii_31.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Right,Forward,Forward,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k5mVaeTtLuKAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=320,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=320
    ),
  ],
  total_token_count=367
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=320 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=320
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=367 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_31.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., here's, the, path:, 1., the, agent, is, at, (1, 1), facing, south., the, cell, below, is, (2, 1), which, is, blank., move, forward., (now, at, (2, 1), facing, south)., 2., the, agent, is, at, (2, 1), facing, south., the, cell, below, is, (3, 1), which, is, blank., move, forward., (now, at, (3, 1), facing, south)., 3., the, agent, is, at, (3, 1), facing, south., the, cell, below, is, (4, 1), which, is, blank., move, forward., (now, at, (4, 1), facing, south)., 4., the, agent, is, at, (4, 1), facing, south., the, cell, below, is, (5, 1), which, is, blank., move, forward., (now, at, (5, 1), facing, south)., 5., the, agent, is, at, (5, 1), facing, south., the, cell, to, the, right, is, (5, 2), which, is, blank., turn, right., (now, at, (5, 1), facing, west)., 6., the, agent, is, at, (5, 1), facing, west., the, cell, to, the, right, is, (5, 2), which, is, blank., move, forward., (now, at, (5, 2), facing, west)., 7., the, agent, is, at, (5, 2), facing, west., the, cell, to, the, right, is, (5, 3), which, is, blank., move, forward., (now, at, (5, 3), facing, west)., 8., the, agent, is, at, (5, 3), facing, west., the, cell, to, the, right, is, (5, 4), which, is, occupied., turn, right., (now, at, (5, 3), facing, north)., 9., the, agent, is, at, (5, 3), facing, north., the, cell, to, the, right, is, (5, 4), which, is, occupied., the, cell, ahead, is, (4, 3), which, is, blank., move, forward., (now, at, (4, 3), facing, north)., 10., the, agent, is, at, (4, 3), facing, north., the, cell, to, the, right, is, (4, 4), which, is, occupied., the, cell, ahead, is, (3, 3), which, is, blank., move, forward., (now, at, (3, 3), facing, north)., 11., the, agent, is, at, (3, 3), facing, north., the, cell, to, the, right, is, (3, 4), which, is, occupied., the, cell, ahead, is, (2, 3), which, is, blank., move, forward., (now, at, (2, 3), facing, north)., 12., the, agent, is, at, (2, 3), facing, north., the, cell, to, the, right, is, (2, 4), which, is, occupied., the, cell, ahead, is, (1, 3), which, is, blank., move, forward., (now, at, (1, 3), facing, north)., 13., the, agent, is, at, (1, 3), facing, north., the, cell, to, the, right, is, (1, 4), which, is, blank., turn, right., (now, at
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The origin is at (1,1) and the target is at (5,5). The agent starts at (1,1) facing South.

Here's the path:

1. The agent is at (1,1) facing South. The cell below is (2,1) which is blank. Move forward. (Now at (2,1) facing South).
2. The agent is at (2,1) facing South. The cell below is (3,1) which is blank. Move forward. (Now at (3,1) facing South).
3. The agent is at (3,1) facing South. The cell below is (4,1) which is blank. Move forward. (Now at (4,1) facing South).
4. The agent is at (4,1) facing South. The cell below is (5,1) which is blank. Move forward. (Now at (5,1) facing South).
5. The agent is at (5,1) facing South. The cell to the right is (5,2) which is blank. Turn Right. (Now at (5,1) facing West).
6. The agent is at (5,1) facing West. The cell to the right is (5,2) which is blank. Move forward. (Now at (5,2) facing West).
7. The agent is at (5,2) facing West. The cell to the right is (5,3) which is blank. Move forward. (Now at (5,3) facing West).
8. The agent is at (5,3) facing West. The cell to the right is (5,4) which is occupied. Turn Right. (Now at (5,3) facing North).
9. The agent is at (5,3) facing North. The cell to the right is (5,4) which is occupied. The cell ahead is (4,3) which is blank. Move forward. (Now at (4,3) facing North).
10. The agent is at (4,3) facing North. The cell to the right is (4,4) which is occupied. The cell ahead is (3,3) which is blank. Move forward. (Now at (3,3) facing North).
11. The agent is at (3,3) facing North. The cell to the right is (3,4) which is occupied. The cell ahead is (2,3) which is blank. Move forward. (Now at (2,3) facing North).
12. The agent is at (2,3) facing North. The cell to the right is (2,4) which is occupied. The cell ahead is (1,3) which is blank. Move forward. (Now at (1,3) facing North).
13. The agent is at (1,3) facing North. The cell to the right is (1,4) which is blank. Turn Right. (Now at"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lZmVab_1GsPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
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

