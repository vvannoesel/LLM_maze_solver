# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_15.jpg` | **0.00%** | `input: 551 , ouput: 19` | `right, forward, right, forward, forward, left, forward, forward, right, forward` |
| `maze_line_3x3_15.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_15.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_15.txt` | **0.00%** | `input: 468 , ouput: 23` | `right, forward, right, forward, right, forward, left, forward, left, forward, left, forward` |
| `maze_line_3x3_tokenized_15.txt` | **0.00%** | `input: 439 , ouput: 650` | `right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left` |
| `maze_occupancy_3x3_15.jpg` | **0.00%** | `input: 546 , ouput: 37` | `forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_15.json` | **0.00%** | `input: 589 , ouput: 103` | `right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_15.json` | **0.00%** | `input: 1298 , ouput: 33` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_15.txt` | **0.00%** | `input: 580 , ouput: 39` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_15.txt` | **0.00%** | `input: 313 , ouput: 650` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_tokenized_15.txt` | **0.00%** | `input: 867 , ouput: 155` | `the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., from, (1, 1), facing, south:, 1., forward, (moves, to, 2, 1), 2., forward, (moves, to, 3, 1), 3., forward, (moves, to, 4, 1), 4., forward, (moves, to, 5, 1), 5., right, (turns, to, face, west), 6., forward, (moves, to, 5, 2), 7., forward, (moves, to, 5, 3), 8., forward, (moves, to, 5, 4), 9., forward, (moves, to, 5, 5), forward, forward, forward, forward, right, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_15.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,right,forward,forward,left,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KZeVabOTLITw7M8P482J-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
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
  total_token_count=570
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=570 traffic_type=None
```

### `maze_line_3x3_15.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KpeVaa3QMoTensEP6bbt4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_15.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K5eVaZ3YFNWbkdUPuuCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Left, Forward, Left, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K5eVacLTM-yOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=491
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=491 traffic_type=None
```

### `maze_line_3x3_tokenized_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left, Forward, Left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LZeVadXPGffonsEPuaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_15.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LpeVaernFd_x7M8P1Ouu-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
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
  total_token_count=583
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=583 traffic_type=None
```

### `maze_occupancy_3x3_15.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='L5eVaciyGdiCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=103,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=692
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=103 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=692 traffic_type=None
```

### `maze_occupancy_3x3_adj_15.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MJeVacCQBv7MkdUP7NXHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1331
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1331 traffic_type=None
```

### `maze_occupancy_3x3_adj_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MJeVacrHI_KcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=619
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=619 traffic_type=None
```

### `maze_occupancy_3x3_ascii_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MpeVaafpPJnqkdUP3rjkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=313,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=313
    ),
  ],
  total_token_count=963
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=313 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=313
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=963 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (5, 5)., from, (1, 1), facing, south:, 1., forward, (moves, to, 2, 1), 2., forward, (moves, to, 3, 1), 3., forward, (moves, to, 4, 1), 4., forward, (moves, to, 5, 1), 5., right, (turns, to, face, west), 6., forward, (moves, to, 5, 2), 7., forward, (moves, to, 5, 3), 8., forward, (moves, to, 5, 4), 9., forward, (moves, to, 5, 5), forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (1,1) facing south. The target is at (5,5).

From (1,1) facing South:
1. forward (moves to 2,1)
2. forward (moves to 3,1)
3. forward (moves to 4,1)
4. forward (moves to 5,1)
5. right (turns to face West)
6. forward (moves to 5,2)
7. forward (moves to 5,3)
8. forward (moves to 5,4)
9. forward (moves to 5,5)

forward,forward,forward,forward,right,forward,forward,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M5eVaZWRJpzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=155,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1022
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=155 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1022 traffic_type=None
```

