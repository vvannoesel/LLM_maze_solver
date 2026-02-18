# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_40.jpg` | **0.00%** | `input: 551 , ouput: 17` | `right, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_40.json` | **0.00%** | `input: 774 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_40.json` | **0.00%** | `input: 836 , ouput: 17` | `backward, right, forward, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_40.txt` | **0.00%** | `input: 468 , ouput: 15` | `right, forward, forward, right, forward, left, forward, forward` |
| `maze_line_3x3_tokenized_40.txt` | **0.00%** | `input: 439 , ouput: 650` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left` |
| `maze_occupancy_3x3_40.jpg` | **0.00%** | `input: 546 , ouput: 47` | `right, forward, right, forward, forward, left, forward, forward, right, forward, forward, backward, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_40.json` | **0.00%** | `input: 589 , ouput: 49` | `right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_adj_40.json` | **0.00%** | `input: 1292 , ouput: 33` | `right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_40.txt` | **0.00%** | `input: 580 , ouput: 47` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_ascii_40.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_tokenized_40.txt` | **0.00%** | `input: 867 , ouput: 75` | `right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_40.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uJqVaYDYAs_c28oPsY6G4AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
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
  total_token_count=568
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=568 traffic_type=None
```

### `maze_line_3x3_40.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
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
        text='Right,Forward,Right,Forward,Right,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uJqVac2zJd--xN8Puvy7kAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_40.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
backward, right, forward, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Backward,right,forward,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uZqVaZHGD82Lxs0PxI-H-Qs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_40.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
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
        text='Right, Forward, Forward, Right, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uZqVafCmKczXvdIPq7fiiAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_40.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='u5qVacufMPfpxN8P0qO4yQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_40.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward, forward, backward, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward,right,forward,forward,backward,forward,forward,left,forward,forward,right,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vZqVaYfEErPTvdIPh7q28Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
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
  total_token_count=593
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=593 traffic_type=None
```

### `maze_occupancy_3x3_40.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vZqVaayvM8zXvdIPtLfiiAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_40.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vpqVaYWGF6bTvdIP79ai6Ao' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_40.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vpqVabuMOrvzxs0Ps7mRkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=627
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=627 traffic_type=None
```

### `maze_occupancy_3x3_ascii_40.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wZqVaY-eA4a8xN8Puu-IoAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_40.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wZqVaci-K43ZvdIPlZKdgQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

