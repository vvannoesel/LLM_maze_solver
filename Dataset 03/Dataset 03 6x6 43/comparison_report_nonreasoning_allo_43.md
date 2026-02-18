# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_43.jpg` | **0.00%** | `input: 434 , ouput: 23` | `right, down, right, down, right, down, right, down, left, down, right, right` |
| `maze_line_6x6_43.json` | **4.55%** | `input: 1809 , ouput: 39` | `down, down, down, down, right, right, right, right, right, down, down, right, right, up, right, down, down, down, right, right` |
| `maze_line_6x6_adj_43.json` | **4.55%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_43.txt` | **13.64%** | `input: 729 , ouput: 27` | `down, right, right, right, down, down, right, down, right, right, down, down, right, right` |
| `maze_line_6x6_tokenized_43.txt` | **0.00%** | `input: 673 , ouput: 17` | `right, down, right, down, down, right, down, right, right` |
| `maze_occupancy_6x6_43.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, left, down, right, down, right, up, right, down, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, up, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down` |
| `maze_occupancy_6x6_43.json` | **0.00%** | `input: 988 , ouput: 650` | `right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down` |
| `maze_occupancy_6x6_adj_43.json` | **13.64%** | `input: 4343 , ouput: 49` | `down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_43.txt` | **0.00%** | `input: 1279 , ouput: 650` | `right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_6x6_ascii_43.txt` | **0.00%** | `input: 249 , ouput: 650` | `right, right, right, right, right, down, down, left, down, down, right, right, right, right, right, up, right, down, down, down, left, left, left, left, left, down, down, right, right, right, right, right, right, right, up, right, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left` |
| `maze_occupancy_6x6_tokenized_43.txt` | **nan%** | `input: 2162 , ouput: 0` | `` |

---

## Full LLM Responses

### `maze_line_6x6_43.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, down, left, up, left, down, left, down, down, right, right, up, right, right, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_4SVafa4AeeGkdUPsqK74AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_43.json`

**Score:** 4.55%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, down, left, up, left, down, left, down, down, right, right, up, right, right, right, down
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right, right, down, down, right, right, up, right, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, right, right, right, right, right, down, down, right, right, up, right, down, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_4SVaZTGM8yynsEP0d_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1848
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1848 traffic_type=None
```

### `maze_line_6x6_adj_43.json`

**Score:** 4.55%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, down, left, up, left, down, left, down, down, right, right, up, right, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AIWVad_rIqzu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_43.txt`

**Score:** 13.64%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, down, left, up, left, down, left, down, down, right, right, up, right, right, right, down
```

**Extracted Answer:**
```
down, right, right, right, down, down, right, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, right, down, down, right, down, right, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AYWVaaaxCZmG7M8PkeL4mAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=756
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=756 traffic_type=None
```

### `maze_line_6x6_tokenized_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, down, left, up, left, down, left, down, down, right, right, up, right, right, right, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AoWVaYFukL6ewQ_EyaThBg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_43.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, down, right, up, right, down, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, up, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,down,right,up,right,down,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,up,right,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BIWVad6YCcjl7M8P9OOViAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_43.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BoWVabf4Earw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_43.json`

**Score:** 13.64%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B4WVac_rD9qgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=4343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4343
    ),
  ],
  total_token_count=4392
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=4343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4343
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4392 traffic_type=None
```

### `maze_occupancy_6x6_adj_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CYWVaYbSIejpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1279,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1279
    ),
  ],
  total_token_count=1929
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1279 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1279
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1929 traffic_type=None
```

### `maze_occupancy_6x6_ascii_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, left, down, down, right, right, right, right, right, up, right, down, down, down, left, left, left, left, left, down, down, right, right, right, right, right, right, right, up, right, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, right, right, up, right, up, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,left,down,down,right,right,right,right,right,up,right,down,down,down,left,left,left,left,left,down,down,right,right,right,right,right,right,right,up,right,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,right,right,up,right,up,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='C4WVadDzB6zd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=249,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=249
    ),
  ],
  total_token_count=899
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=249 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=249
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=899 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_43.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DYWVaZ2zPKOF7M8P9PzH6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2162
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2162 traffic_type=None
```

