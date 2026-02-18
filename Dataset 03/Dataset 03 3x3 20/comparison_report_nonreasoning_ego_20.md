# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_20.jpg` | **0.00%** | `input: 551 , ouput: 21` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward` |
| `maze_line_3x3_20.json` | **0.00%** | `input: 774 , ouput: 15` | `right, forward, forward, right, forward, left, forward, forward` |
| `maze_line_3x3_adj_20.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, right, forward, left, forward, forward` |
| `maze_line_3x3_adj_20.txt` | **0.00%** | `input: 468 , ouput: 15` | `right, forward, forward, right, forward, left, forward, forward` |
| `maze_line_3x3_tokenized_20.txt` | **0.00%** | `input: 439 , ouput: 17` | `right, forward, right, forward, backward, forward, left, forward, forward` |
| `maze_occupancy_3x3_20.jpg` | **12.50%** | `input: 546 , ouput: 29` | `forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_20.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left` |
| `maze_occupancy_3x3_adj_20.json` | **0.00%** | `input: 1292 , ouput: 29` | `right, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_20.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward` |
| `maze_occupancy_3x3_ascii_20.txt` | **0.00%** | `input: 315 , ouput: 59` | `right, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_20.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_20.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gZeVab_0FcPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_20.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,right,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gpeVaeCNApnqkdUP3rjkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_20.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
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
        text='right,forward,right,forward,right,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gpeVafGrJ7W5kdUP1c_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_20.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='g5eVadzrFIqjkdUP8qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=483
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=483 traffic_type=None
```

### `maze_line_3x3_tokenized_20.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, backward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Backward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hJeVaa64BIqjkdUP-qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=456
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=456 traffic_type=None
```

### `maze_occupancy_3x3_20.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hJeVacCCMI65kdUPzNPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_20.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hpeVacLQEdqfnsEPvPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_20.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hpeVaZu2PNqfnsEPzfyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1321
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1321 traffic_type=None
```

### `maze_occupancy_3x3_adj_20.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Right,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Left,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iJeVae3bG6zd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_20.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iZeVaZ576OmewQ_XvduJCA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=374
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=374 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_20.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=543,
        license='',
        start_index=155,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=2833,
        license='',
        start_index=483,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ipeVafLqG9qfnsEPxvyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

