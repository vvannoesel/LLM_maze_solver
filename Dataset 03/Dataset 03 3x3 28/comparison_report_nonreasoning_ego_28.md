# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_28.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_28.json` | **0.00%** | `input: 774 , ouput: 15` | `right, forward, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_28.json` | **0.00%** | `input: 836 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_28.txt` | **0.00%** | `input: 468 , ouput: 21` | `right, forward, right, forward, forward, right, forward, left, forward, left, forward` |
| `maze_line_3x3_tokenized_28.txt` | **0.00%** | `input: 439 , ouput: 19` | `right, forward, right, forward, right, forward, left, forward, left, forward` |
| `maze_occupancy_3x3_28.jpg` | **0.00%** | `input: 546 , ouput: 37` | `right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_28.json` | **0.00%** | `input: 589 , ouput: 81` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_adj_28.json` | **0.00%** | `input: 1292 , ouput: 33` | `right, forward, right, forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward` |
| `maze_occupancy_3x3_adj_28.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_ascii_28.txt` | **0.00%** | `input: 320 , ouput: 51` | `right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_28.txt` | **0.00%** | `input: 867 , ouput: 381` | `the, maze, is, 7x7., the, origin, is, at, (1, 1)., the, agent, starts, facing, south., the, target, is, at, (5, 5)., let's, trace, a, path, from, (1, 1), to, (5, 5)., 1., start, at, (1, 1), facing, south., 2., move, forward, to, (2, 1)., (facing, south), 3., move, forward, to, (3, 1)., (facing, south), 4., move, forward, to, (4, 1)., (facing, south), 5., move, forward, to, (5, 1)., (facing, south), 6., turn, right., now, facing, west., 7., move, forward, to, (5, 2)., (facing, west), 8., move, forward, to, (5, 3)., (facing, west), 9., turn, right., now, facing, north., 10., turn, right., now, facing, east., 11., move, forward, to, (5, 4)., (facing, east), 12., move, forward, to, (5, 5)., (facing, east), -, target, reached., let's, confirm, this, path, with, the, maze, layout:, (1, 1), origin, facing, south, forward, ->, (2, 1), blank, forward, ->, (3, 1), blank, forward, ->, (4, 1), blank, forward, ->, (5, 1), blank, right, ->, facing, west, forward, ->, (5, 2), blank, forward, ->, (5, 3), blank, right, ->, facing, north, right, ->, facing, east, forward, ->, (5, 4), blank, forward, ->, (5, 5), target, the, instructions, are:, forward, forward, forward, forward, right, forward, forward, right, right, forward, forward., forward, forward, forward, forward, right, forward, forward, right, right, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_28.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='J5mVaa7_HqvgnsEP8Mu7uAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_28.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KJmVab-7BdHMkdUPyI67sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_28.json`

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
        text='Right, Forward, Right, Forward, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KJmVabbBJvT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Right, Forward, Left, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KZmVae6_D4qwnsEPl8W4mAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=489
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=489 traffic_type=None
```

### `maze_line_3x3_tokenized_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, left, forward, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Left, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KZmVaeXbLffonsEPuaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_28.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KpmVab7_Gazu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_28.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KpmVabbVO7zhnsEPwLCgiQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=81,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=670
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=81 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=670 traffic_type=None
```

### `maze_occupancy_3x3_adj_28.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K5mVafnKKtWbkdUPuuCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LZmVae4S9Pvszw-um-3oCA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LZmVafqUMaeN7M8P6NXVwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=320,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=320
    ),
  ],
  total_token_count=371
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=320 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=320
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=371 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
the, maze, is, 7x7., the, origin, is, at, (1, 1)., the, agent, starts, facing, south., the, target, is, at, (5, 5)., let's, trace, a, path, from, (1, 1), to, (5, 5)., 1., start, at, (1, 1), facing, south., 2., move, forward, to, (2, 1)., (facing, south), 3., move, forward, to, (3, 1)., (facing, south), 4., move, forward, to, (4, 1)., (facing, south), 5., move, forward, to, (5, 1)., (facing, south), 6., turn, right., now, facing, west., 7., move, forward, to, (5, 2)., (facing, west), 8., move, forward, to, (5, 3)., (facing, west), 9., turn, right., now, facing, north., 10., turn, right., now, facing, east., 11., move, forward, to, (5, 4)., (facing, east), 12., move, forward, to, (5, 5)., (facing, east), -, target, reached., let's, confirm, this, path, with, the, maze, layout:, (1, 1), origin, facing, south, forward, ->, (2, 1), blank, forward, ->, (3, 1), blank, forward, ->, (4, 1), blank, forward, ->, (5, 1), blank, right, ->, facing, west, forward, ->, (5, 2), blank, forward, ->, (5, 3), blank, right, ->, facing, north, right, ->, facing, east, forward, ->, (5, 4), blank, forward, ->, (5, 5), target, the, instructions, are:, forward, forward, forward, forward, right, forward, forward, right, right, forward, forward., forward, forward, forward, forward, right, forward, forward, right, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is 7x7.
The origin is at (1,1). The agent starts facing South.
The target is at (5,5).

Let's trace a path from (1,1) to (5,5).

1. Start at (1,1) facing South.
2. Move Forward to (2,1). (facing South)
3. Move Forward to (3,1). (facing South)
4. Move Forward to (4,1). (facing South)
5. Move Forward to (5,1). (facing South)
6. Turn Right. Now facing West.
7. Move Forward to (5,2). (facing West)
8. Move Forward to (5,3). (facing West)
9. Turn Right. Now facing North.
10. Turn Right. Now facing East.
11. Move Forward to (5,4). (facing East)
12. Move Forward to (5,5). (facing East) - Target reached.

Let's confirm this path with the maze layout:
(1,1) origin, facing South
Forward -> (2,1) blank
Forward -> (3,1) blank
Forward -> (4,1) blank
Forward -> (5,1) blank
Right -> Facing West
Forward -> (5,2) blank
Forward -> (5,3) blank
Right -> Facing North
Right -> Facing East
Forward -> (5,4) blank
Forward -> (5,5) target

The instructions are: forward, forward, forward, forward, right, forward, forward, right, right, forward, forward.

forward,forward,forward,forward,right,forward,forward,right,right,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='L5mVaYSVIryK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=381,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1248
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=381 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1248 traffic_type=None
```

