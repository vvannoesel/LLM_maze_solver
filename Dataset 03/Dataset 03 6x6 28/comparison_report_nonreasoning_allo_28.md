# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_28.jpg` | **25.00%** | `input: 434 , ouput: 37` | `right, down, right, down, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down` |
| `maze_line_6x6_28.json` | **0.00%** | `input: 1809 , ouput: 23` | `down, down, right, down, right, right, up, right, down, down, right, right` |
| `maze_line_6x6_adj_28.json` | **16.67%** | `input: 2258 , ouput: 29` | `right, down, down, down, right, right, down, right, down, down, right, down, right, down, right` |
| `maze_line_6x6_adj_28.txt` | **8.33%** | `input: 729 , ouput: 23` | `right, right, right, down, right, down, down, right, down, down, right, right` |
| `maze_line_6x6_tokenized_28.txt` | **0.00%** | `input: 673 , ouput: 650` | `down, right, right, down, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up` |
| `maze_occupancy_6x6_28.jpg` | **0.00%** | `input: 431 , ouput: 83` | `down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, left, up, left, up, right, up, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, right, down, right` |
| `maze_occupancy_6x6_28.json` | **nan%** | `input: 988 , ouput: 0` | `` |
| `maze_occupancy_6x6_adj_28.json` | **nan%** | `input: 4340 , ouput: 0` | `` |
| `maze_occupancy_6x6_adj_28.txt` | **33.33%** | `input: 1277 , ouput: 650` | `right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right` |
| `maze_occupancy_6x6_ascii_28.txt` | **16.67%** | `input: 249 , ouput: 419` | `right, right, down, down, down, right, right, right, right, right, down, down, down, left, left, down, right, right, right, right, down, right, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, left, down, right, right, right, right, right, down, left, left, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, right, down, left, left, left, left, left, down, right, right, right, right, down, left, left, left, left, left, left, down, right, right, right, right, right, down, left, left, left, left, left, down, right, right, right, right, right, right, down, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_28.txt` | **16.67%** | `input: 2162 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right` |

---

## Full LLM Responses

### `maze_line_6x6_28.jpg`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2oKVade5BfjwxN8Px9POiQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
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
  total_token_count=471
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=471 traffic_type=None
```

### `maze_line_6x6_28.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, down, right, right, up, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, right, up, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2oKVaevoJrPTvdIPh7q28Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1832
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1832 traffic_type=None
```

### `maze_line_6x6_adj_28.json`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, right, down, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, down, right, right, down, right, down, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='24KVaeX2FdPevdIP3abOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_28.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, down, right, down, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,down,down,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='24KVaY6MOqS9xN8PvoPm4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, down, down, down, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, up, right, down, down, left, down, right, right, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, down, right, right, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,up,right,down,down,left,down,right,right,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,down,right,right,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3YKVaebgJI3ZvdIPlZKdgQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=1323
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1323 traffic_type=None
```

### `maze_occupancy_6x6_28.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, left, up, left, up, right, up, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,left,up,left,up,right,up,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3oKVacejH_6o28oP8YeKkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=83,
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
  total_token_count=514
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=83 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=514 traffic_type=None
```

### `maze_occupancy_6x6_28.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```

```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  finish_reason=<FinishReason.RECITATION: 'RECITATION'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4YKVaZufGozYxs0P5_PJ2Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=988
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=988 traffic_type=None
```

### `maze_occupancy_6x6_adj_28.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```

```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  finish_reason=<FinishReason.RECITATION: 'RECITATION'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5IKVadvuCML1xs0Pl-qmkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=4340,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4340
    ),
  ],
  total_token_count=4340
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=4340 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4340
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4340 traffic_type=None
```

### `maze_occupancy_6x6_adj_28.txt`

**Score:** 33.33%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5YKVaePKKYaSxN8P5cLTkAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_28.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, right, right, right, right, right, down, down, down, left, left, down, right, right, right, right, down, right, right, right, right, right, down, left, left, left, left, down, right, right, right, right, down, left, left, left, left, left, down, right, right, right, right, right, down, left, left, left, left, left, left, down, right, right, right, right, down, left, left, left, left, down, right, right, right, right, right, down, left, left, left, left, left, down, right, right, right, right, down, left, left, left, left, left, left, down, right, right, right, right, right, down, left, left, left, left, left, down, right, right, right, right, right, right, down, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, down, left, left, left, left, left, left, left, left, left, left, left, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,right,right,right,right,right,down,down,down,left,left,down,right,right,right,right,down,right,right,right,right,right,down,left,left,left,left,down,right,right,right,right,down,left,left,left,left,left,down,right,right,right,right,right,down,left,left,left,left,left,left,down,right,right,right,right,down,left,left,left,left,down,right,right,right,right,right,down,left,left,left,left,left,down,right,right,right,right,down,left,left,left,left,left,left,down,right,right,right,right,right,down,left,left,left,left,left,down,right,right,right,right,right,right,down,left,left,left,left,left,left,left,down,right,right,right,right,right,right,right,down,left,left,left,left,left,left,left,left,down,right,right,right,right,right,right,right,right,down,left,left,left,left,left,left,left,left,left,down,right,right,right,right,right,right,right,right,right,down,left,left,left,left,left,left,left,left,left,left,down,right,right,right,right,right,right,right,right,right,right,right,down,left,left,left,left,left,left,left,left,left,left,left,down,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='54KVadiNEuW1vdIPpY7RsQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=419,
  prompt_token_count=249,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=249
    ),
  ],
  total_token_count=668
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=419 candidates_tokens_details=None prompt_token_count=249 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=249
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=668 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_28.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6YKVaZHtIvyc28oP7rOrsAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

