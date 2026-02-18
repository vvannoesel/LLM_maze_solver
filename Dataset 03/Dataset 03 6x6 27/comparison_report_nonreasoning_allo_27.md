# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_27.jpg` | **4.55%** | `input: 434 , ouput: 19` | `right, down, right, down, down, right, right, down, right, down` |
| `maze_line_6x6_27.json` | **0.00%** | `input: 1809 , ouput: 19` | `down, right, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_27.json` | **13.64%** | `input: 2258 , ouput: 29` | `right, right, down, down, right, right, down, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_27.txt` | **22.73%** | `input: 729 , ouput: 23` | `right, right, down, right, down, down, right, right, down, down, right, down` |
| `maze_line_6x6_tokenized_27.txt` | **4.55%** | `input: 673 , ouput: 37` | `right, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, down, right` |
| `maze_occupancy_6x6_27.jpg` | **2.27%** | `input: 431 , ouput: 71` | `right, down, right, down, right, down, left, down, right, right, down, right, up, right, down, right, down, left, down, right, right, up, right, down, down, right, down, right, down, right, up, right, down, right, down, right` |
| `maze_occupancy_6x6_27.json` | **9.09%** | `input: 988 , ouput: 650` | `right, right, right, right, right, down, down, right, right, down, down, down, down, down, right, right, right, right, right, down, down, left, down, down, right, right, right, right, right, right, down, down, down, left, left, left, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_27.json` | **11.36%** | `input: 4340 , ouput: 43` | `right, right, right, right, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_27.txt` | **0.00%** | `input: 1277 , ouput: 650` | `down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right` |
| `maze_occupancy_6x6_ascii_27.txt` | **9.09%** | `input: 246 , ouput: 53` | `right, right, right, right, right, down, down, right, down, down, down, down, right, right, right, down, right, down, down, down, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_27.txt` | **9.09%** | `input: 2162 , ouput: 650` | `right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_6x6_27.jpg`

**Score:** 4.55%

**Ground Truth Solution:**
```
right, right, down, right, down, left, left, left, down, right, right, down, right, right, up, up, up, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, down, right, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zoKVabjiEIzYxs0P5_PJ2Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=434,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=176
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=453
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=434 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=453 traffic_type=None
```

### `maze_line_6x6_27.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, right, down, left, left, left, down, right, right, down, right, right, up, up, up, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='z4KVad7KAdrzxs0PvK7U4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1828
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=192 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1828 traffic_type=None
```

### `maze_line_6x6_adj_27.json`

**Score:** 13.64%

**Ground Truth Solution:**
```
right, right, down, right, down, left, left, left, down, right, right, down, right, right, up, up, up, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='z4KVaYntMeGlxN8Ppv3riAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2287
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=163 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2287 traffic_type=None
```

### `maze_line_6x6_adj_27.txt`

**Score:** 22.73%

**Ground Truth Solution:**
```
right, right, down, right, down, left, left, left, down, right, right, down, right, right, up, up, up, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, down, right, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, right, down, down, right, right, down, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0IKVaem4GozYxs0P5_PJ2Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=752
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=196 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=752 traffic_type=None
```

### `maze_line_6x6_tokenized_27.txt`

**Score:** 4.55%

**Ground Truth Solution:**
```
right, right, down, right, down, left, left, left, down, right, right, down, right, right, up, up, up, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0YKVabiCDMn7vdIP_oGtyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=710
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=194 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=710 traffic_type=None
```

### `maze_occupancy_6x6_27.jpg`

**Score:** 2.27%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, down, right, up, right, down, right, down, left, down, right, right, up, right, down, down, right, down, right, down, right, up, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,down,right,up,right,down,right,down,left,down,right,right,up,right,down,down,right,down,right,down,right,up,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0oKVaayEBZme28oPkrijmAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=71,
  prompt_token_count=431,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=173
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=502
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=431 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=71 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=502 traffic_type=None
```

### `maze_occupancy_6x6_27.json`

**Score:** 9.09%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, right, right, down, down, down, down, down, right, right, right, right, right, down, down, left, down, down, right, right, right, right, right, right, down, down, down, left, left, left, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,right,right,down,down,down,down,down,right,right,right,right,right,down,down,left,down,down,right,right,right,right,right,right,down,down,down,left,left,left,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1IKVaaLvHIuX28oPlq_ciQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1638
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=174 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1638 traffic_type=None
```

### `maze_occupancy_6x6_adj_27.json`

**Score:** 11.36%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1YKVaYCTFdrbxs0P1qTOyAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=4340,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4340
    ),
  ],
  total_token_count=4383
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=165 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=4340 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4340
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4383 traffic_type=None
```

### `maze_occupancy_6x6_adj_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='14KVaeuABN--xN8Puvy7kAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1277,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1277
    ),
  ],
  total_token_count=1927
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=198 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1277 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1277
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1927 traffic_type=None
```

### `maze_occupancy_6x6_ascii_27.txt`

**Score:** 9.09%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, right, down, down, down, down, right, right, right, down, right, down, down, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,right,down,down,down,down,right,right,right,down,right,down,down,down,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='14KVafrpMszXvdIPtLfiiAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=246
    ),
  ],
  total_token_count=299
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=173 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=299 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_27.txt`

**Score:** 9.09%

**Ground Truth Solution:**
```
right, right, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2YKVaeC6F6S9xN8PvoPm4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2812
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=197 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2812 traffic_type=None
```

