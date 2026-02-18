# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_49.jpg` | **5.56%** | `input: 434 , ouput: 23` | `down, right, down, right, down, right, down, right, up, right, down, down` |
| `maze_line_6x6_49.json` | **11.11%** | `input: 1809 , ouput: 29` | `down, down, right, right, down, down, right, right, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_49.json` | **16.67%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_49.txt` | **16.67%** | `input: 729 , ouput: 29` | `down, down, down, down, right, right, right, right, down, right, down, right, right, down, right` |
| `maze_line_6x6_tokenized_49.txt` | **0.00%** | `input: 673 , ouput: 17` | `right, down, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_49.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right` |
| `maze_occupancy_6x6_49.json` | **0.00%** | `input: 988 , ouput: 650` | `right, down, down, right, right, right, right, right, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right` |
| `maze_occupancy_6x6_adj_49.json` | **16.67%** | `input: 4342 , ouput: 65` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_49.txt` | **16.67%** | `input: 1278 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_ascii_49.txt` | **0.00%** | `input: 254 , ouput: 57` | `right, right, right, right, right, right, right, right, down, down, right, down, down, left, down, left, down, left, left, left, left, down, down, down, down, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_49.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down` |

---

## Full LLM Responses

### `maze_line_6x6_49.jpg`

**Score:** 5.56%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, right, up, right, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='boWVaYLpIvfo7M8PiZSSoQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=457
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=457 traffic_type=None
```

### `maze_line_6x6_49.json`

**Score:** 11.11%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, right, up, right, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='b4WVacOMFo65kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1838
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1838 traffic_type=None
```

### `maze_line_6x6_adj_49.json`

**Score:** 16.67%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, right, up, right, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='b4WVaYf-N8PPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_49.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, right, up, right, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right, down, right, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, right, right, right, right, down, right, down, right, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cIWVadeqJcyynsEP0d_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=758
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=758 traffic_type=None
```

### `maze_line_6x6_tokenized_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, right, up, right, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cYWVabKmFYWF7M8PnoeMqQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=690
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=690 traffic_type=None
```

### `maze_occupancy_6x6_49.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='c4WVafCzKNqgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1081
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1081 traffic_type=None
```

### `maze_occupancy_6x6_49.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, right, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,right,down,down,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dYWVadntJq2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_49.json`

**Score:** 16.67%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='doWVabHvHafx7M8PiZPD-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=65,
  prompt_token_count=4342,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4342
    ),
  ],
  total_token_count=4407
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=65 candidates_tokens_details=None prompt_token_count=4342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4407 traffic_type=None
```


### `maze_occupancy_6x6_adj_49.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1oWVaab8FMeC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1278,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1278
    ),
  ],
  total_token_count=1928
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1278 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1278
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1928 traffic_type=None
```

### `maze_occupancy_6x6_ascii_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, right, down, down, left, down, left, down, left, left, left, left, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,right,down,down,left,down,left,down,left,left,left,left,down,down,down,down,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='14WVafmLB7W5kdUP1c_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=254,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=254
    ),
  ],
  total_token_count=311
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=254 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=254
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=311 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2IWVafXiIajlnsEP1bugwAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

