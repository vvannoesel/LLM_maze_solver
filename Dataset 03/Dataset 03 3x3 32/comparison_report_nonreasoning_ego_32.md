# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_32.jpg` | **0.00%** | `input: 551 , ouput: 23` | `right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_line_3x3_32.json` | **0.00%** | `input: 774 , ouput: 15` | `right, forward, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_32.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_32.txt` | **0.00%** | `input: 468 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_32.txt` | **0.00%** | `input: 439 , ouput: 9` | `right, forward, right, forward, forward` |
| `maze_occupancy_3x3_32.jpg` | **0.00%** | `input: 546 , ouput: 34` | `right, forward, forward, right, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward.` |
| `maze_occupancy_3x3_32.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_adj_32.json` | **0.00%** | `input: 1292 , ouput: 35` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_32.txt` | **0.00%** | `input: 580 , ouput: 71` | `right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, left, forward, forward, right, forward, right, forward, right, forward, forward, left, forward, left, forward, left, forward, forward, right, forward, right, forward, right, forward, forward` |
| `maze_occupancy_3x3_ascii_32.txt` | **0.00%** | `input: 319 , ouput: 49` | `right, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_32.txt` | **0.00%** | `input: 867 , ouput: 370` | `the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., 1., **move, south**:, the, agent, is, at, (1, 1), facing, south., it, needs, to, move, to, (2, 1)., action:, `forward`, 2., **move, south**:, the, agent, is, at, (2, 1), facing, south., it, needs, to, move, to, (3, 1)., action:, `forward`, 3., **move, south**:, the, agent, is, at, (3, 1), facing, south., it, needs, to, move, to, (4, 1)., action:, `forward`, 4., **move, south**:, the, agent, is, at, (4, 1), facing, south., it, needs, to, move, to, (5, 1)., action:, `forward`, 5., **turn, right**:, the, agent, is, at, (5, 1), facing, south., it, needs, to, face, east, to, move, towards, (5, 2)., action:, `right`, 6., **move, east**:, the, agent, is, at, (5, 1), facing, east., it, needs, to, move, to, (5, 2)., action:, `forward`, 7., **move, east**:, the, agent, is, at, (5, 2), facing, east., it, needs, to, move, to, (5, 3)., action:, `forward`, 8., **move, east**:, the, agent, is, at, (5, 3), facing, east., it, needs, to, move, to, (5, 4)., action:, `forward`, 9., **move, east**:, the, agent, is, at, (5, 4), facing, east., it, needs, to, move, to, (5, 5), the, target., action:, `forward`, therefore, the, sequence, of, actions, is:, forward, forward, forward, forward, right, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_32.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lpmVafnYBIKG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=574
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=574 traffic_type=None
```

### `maze_line_3x3_32.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
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
        text='Right,forward,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lpmVaZSaKryK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_32.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='l5mVac3JDqOF7M8P9PzH6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
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
        text='right, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='l5mVad2AN9HMkdUPjY-7sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mJmVaYXuFtWbkdUPuuCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=9,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=448
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=9 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=448 traffic_type=None
```

### `maze_occupancy_3x3_32.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, right, forward, forward, left, forward, forward, left, forward, forward, Right, forward, forward.'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mZmVaZXOA465kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=34,
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
  total_token_count=580
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=34 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=580 traffic_type=None
```

### `maze_occupancy_3x3_32.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mpmVacTcN_367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_32.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m5mVab3cGPDm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1327
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1327 traffic_type=None
```

### `maze_occupancy_3x3_adj_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward, forward, left, forward, left, forward, left, forward, forward, right, forward, right, forward, right, forward, forward, left, forward, left, forward, left, forward, forward, right, forward, right, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Left, Forward, Forward, Right, Forward, Right, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nJmVabD3FffnnsEPornoiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=71,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=651
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=71 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=651 traffic_type=None
```

### `maze_occupancy_3x3_ascii_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nJmVaeywNvDm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=319,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=319
    ),
  ],
  total_token_count=368
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=319 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=319
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=368 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
the, origin, is, at, (1, 1), and, the, target, is, at, (5, 5)., the, agent, starts, at, (1, 1), facing, south., 1., **move, south**:, the, agent, is, at, (1, 1), facing, south., it, needs, to, move, to, (2, 1)., action:, `forward`, 2., **move, south**:, the, agent, is, at, (2, 1), facing, south., it, needs, to, move, to, (3, 1)., action:, `forward`, 3., **move, south**:, the, agent, is, at, (3, 1), facing, south., it, needs, to, move, to, (4, 1)., action:, `forward`, 4., **move, south**:, the, agent, is, at, (4, 1), facing, south., it, needs, to, move, to, (5, 1)., action:, `forward`, 5., **turn, right**:, the, agent, is, at, (5, 1), facing, south., it, needs, to, face, east, to, move, towards, (5, 2)., action:, `right`, 6., **move, east**:, the, agent, is, at, (5, 1), facing, east., it, needs, to, move, to, (5, 2)., action:, `forward`, 7., **move, east**:, the, agent, is, at, (5, 2), facing, east., it, needs, to, move, to, (5, 3)., action:, `forward`, 8., **move, east**:, the, agent, is, at, (5, 3), facing, east., it, needs, to, move, to, (5, 4)., action:, `forward`, 9., **move, east**:, the, agent, is, at, (5, 4), facing, east., it, needs, to, move, to, (5, 5), the, target., action:, `forward`, therefore, the, sequence, of, actions, is:, forward, forward, forward, forward, right, forward, forward, forward, forward
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

1. **Move South**: The agent is at (1,1) facing South. It needs to move to (2,1). Action: `forward`
2. **Move South**: The agent is at (2,1) facing South. It needs to move to (3,1). Action: `forward`
3. **Move South**: The agent is at (3,1) facing South. It needs to move to (4,1). Action: `forward`
4. **Move South**: The agent is at (4,1) facing South. It needs to move to (5,1). Action: `forward`
5. **Turn Right**: The agent is at (5,1) facing South. It needs to face East to move towards (5,2). Action: `right`
6. **Move East**: The agent is at (5,1) facing East. It needs to move to (5,2). Action: `forward`
7. **Move East**: The agent is at (5,2) facing East. It needs to move to (5,3). Action: `forward`
8. **Move East**: The agent is at (5,3) facing East. It needs to move to (5,4). Action: `forward`
9. **Move East**: The agent is at (5,4) facing East. It needs to move to (5,5), the target. Action: `forward`

Therefore, the sequence of actions is:
forward, forward, forward, forward, right, forward, forward, forward, forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nZmVaY2JM465kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=370,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1237
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=370 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1237 traffic_type=None
```

