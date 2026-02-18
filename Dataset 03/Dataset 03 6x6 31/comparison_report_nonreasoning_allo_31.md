# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_31.jpg` | **12.50%** | `input: 434 , ouput: 17` | `right, down, right, down, right, down, down, right, right` |
| `maze_line_6x6_31.json` | **12.50%** | `input: 1809 , ouput: 23` | `right, down, right, down, down, right, right, down, right, down, right, down` |
| `maze_line_6x6_adj_31.json` | **12.50%** | `input: 2258 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_adj_31.txt` | **16.67%** | `input: 729 , ouput: 25` | `right, down, right, right, down, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_tokenized_31.txt` | **8.33%** | `input: 673 , ouput: 650` | `right, down, down, right, down, right, down, left, down, right, right, up, right, down, down, left, left, up, left, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, up, left, left, down, down, right, right, up, up, left, left, up, right, right, down, down, left, left, up, up, right, right, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up` |
| `maze_occupancy_6x6_31.jpg` | **0.00%** | `input: 431 , ouput: 51` | `down, right, down, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down` |
| `maze_occupancy_6x6_31.json` | **6.25%** | `input: 988 , ouput: 650` | `right, right, down, right, down, down, down, down, right, down, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_31.json` | **6.25%** | `input: 4340 , ouput: 71` | `right, right, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_31.txt` | **0.00%** | `input: 1277 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_ascii_31.txt` | **6.25%** | `input: 251 , ouput: 113` | `right, right, down, right, right, right, right, right, down, down, down, left, left, left, down, right, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_31.txt` | **2.08%** | `input: 2162 , ouput: 650` | `right, down, down, right, right, right, down, right, down, right, right, right, right, down, down, down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down` |

---

## Full LLM Responses

### `maze_line_6x6_31.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, down, right, right, up, right, down, down, down, left, up, left, left, left, down, right, down, down, right, up, right, right, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DoOVadX_BdfIvdIPlo3gqAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
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
  total_token_count=451
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=451 traffic_type=None
```

### `maze_line_6x6_31.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, down, right, right, up, right, down, down, down, left, up, left, left, left, down, right, down, down, right, up, right, right, down, right
```

**Extracted Answer:**
```
right, down, right, down, down, right, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DoOVaZv0Mpy8xN8Pl5eC0Aw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_31.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, down, right, right, up, right, down, down, down, left, up, left, left, left, down, right, down, down, right, up, right, right, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='D4OVaZOBJIbIvdIPqfe6oAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2277
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2277 traffic_type=None
```

### `maze_line_6x6_adj_31.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, down, right, right, up, right, down, down, down, left, up, left, left, left, down, right, down, down, right, up, right, right, down, right
```

**Extracted Answer:**
```
right, down, right, right, down, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EIOVaYjmA_6jvdIPjJjJuQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=754
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=754 traffic_type=None
```

### `maze_line_6x6_tokenized_31.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, right, right, up, right, down, down, down, left, up, left, left, left, down, right, down, down, right, up, right, right, down, right
```

**Extracted Answer:**
```
right, down, down, right, down, right, down, left, down, right, right, up, right, down, down, left, left, up, left, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, up, left, left, down, down, right, right, up, up, left, left, up, right, right, down, down, left, left, up, up, right, right, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up, left, left, down, down, right, right, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,down,right,down,left,down,right,right,up,right,down,down,left,left,up,left,up,right,right,down,down,left,left,up,up,right,right,down,down,left,left,up,up,right,right,up,left,left,down,down,right,right,up,up,left,left,up,right,right,down,down,left,left,up,up,right,right,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,left,left,down,down,right,right,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EYOVacWVKd--xN8Puvy7kAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_31.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, right, down, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EoOVaYSBPYjyxs0PwJ_VyQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
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
  total_token_count=482
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=482 traffic_type=None
```

### `maze_occupancy_6x6_31.json`

**Score:** 6.25%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, down, down, down, down, right, down, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,down,down,right,down,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FYOVadDqFtPevdIP3abOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_31.json`

**Score:** 6.25%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FoOVaduEEOGlxN8Ppv3riAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=71,
  prompt_token_count=4340,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4340
    ),
  ],
  total_token_count=4411
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=71 candidates_tokens_details=None prompt_token_count=4340 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4340
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4411 traffic_type=None
```

### `maze_occupancy_6x6_adj_31.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GIOVaZyhI5-NvdIPi-LSsQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_31.txt`

**Score:** 6.25%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, down, down, down, left, left, left, down, right, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,down,down,down,left,left,left,down,right,right,right,right,right,down,down,down,down,left,left,left,left,left,left,left,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GYOVafC3FqbZvdIPiYDjiQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=251
    ),
  ],
  total_token_count=364
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=364 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_31.txt`

**Score:** 2.08%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, right, down, right, down, right, right, right, right, down, down, down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, right, right, down, right, down, right, right, right, right, down, down, down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G4OVaafPKeKO28oPte7eiAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

