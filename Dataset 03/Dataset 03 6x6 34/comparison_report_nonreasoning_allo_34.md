# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_34.jpg` | **6.25%** | `input: 434 , ouput: 21` | `down, right, down, right, down, right, down, right, up, right, down` |
| `maze_line_6x6_34.json` | **18.75%** | `input: 1809 , ouput: 41` | `down, down, right, right, down, down, right, right, right, down, down, right, down, right, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_34.json` | **18.75%** | `input: 2258 , ouput: 19` | `down, down, right, right, down, down, right, right, down, down` |
| `maze_line_6x6_adj_34.txt` | **18.75%** | `input: 729 , ouput: 25` | `down, down, right, down, right, down, right, right, down, right, down, down, right` |
| `maze_line_6x6_tokenized_34.txt` | **0.00%** | `input: 673 , ouput: 51` | `right, down, right, down, right, down, left, down, right, right, up, right, down, left, down, right, right, up, right, up, right, down, left, down, right, right` |
| `maze_occupancy_6x6_34.jpg` | **3.12%** | `input: 431 , ouput: 129` | `down, right, right, down, down, right, right, right, down, down, left, down, right, right, up, right, down, down, right, right, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right, up, right, down, down, right, right, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right` |
| `maze_occupancy_6x6_34.json` | **3.12%** | `input: 988 , ouput: 650` | `down, right, down, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, down, down, right, right, down, down, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right` |
| `maze_occupancy_6x6_adj_34.json` | **12.50%** | `input: 4346 , ouput: 650` | `down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left` |
| `maze_occupancy_6x6_adj_34.txt` | **12.50%** | `input: 1281 , ouput: 650` | `down, down, down, down, down, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_34.txt` | **0.00%** | `input: 254 , ouput: 650` | `right, down, right, right, right, down, left, down, right, right, right, down, left, down, left, down, right, right, down, right, right, right, up, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, left, down, left, down, right, right, right, up, up, right, right, right, up, up, up, up, up, up, up, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right` |
| `maze_occupancy_6x6_tokenized_34.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, right, down, down, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_34.jpg`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, right, down, right, down, left, down, down, right
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right, down, right, down, right, up, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M4SVaeWBCvKcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
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
  total_token_count=455
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=455 traffic_type=None
```

### `maze_line_6x6_34.json`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, right, down, right, down, left, down, down, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, right, down, down, right, down, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,right,down,down,right,down,right,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M4SVadXUNfjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1850
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1850 traffic_type=None
```

### `maze_line_6x6_adj_34.json`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, right, down, right, down, left, down, down, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NISVaci-Gazu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_34.txt`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, right, down, right, down, left, down, down, right
```

**Extracted Answer:**
```
down, down, right, down, right, down, right, right, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, down, right, right, down, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NYSVaaqZBPDm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_34.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, right, down, right, down, left, down, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, up, right, down, left, down, right, right, up, right, up, right, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,up,right,down,left,down,right,right,up,right,up,right,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NoSVaYuLEoqjkdUP8qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=724
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=724 traffic_type=None
```

### `maze_occupancy_6x6_34.jpg`

**Score:** 3.12%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, right, down, down, left, down, right, right, up, right, down, down, right, right, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right, up, right, down, down, right, right, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, down, down, right, right, right, down, down, left, down, right, right, up, right, down, down, right, right, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right, up, right, down, down, right, right, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right, up, right, down, down, left, down, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='N4SVaYTeILyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=129,
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
  total_token_count=560
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=129 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=560 traffic_type=None
```

### `maze_occupancy_6x6_34.json`

**Score:** 3.12%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, right, down, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, down, down, right, right, down, down, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,down,down,right,right,down,down,right,right,down,down,right,right,right,down,down,down,right,right,right,down,down,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OYSVafmXBIWF7M8PnoeMqQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_34.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left, left, left, left, left, left, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='O4SVaefTDtqgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4346,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4346
    ),
  ],
  total_token_count=4996
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4346 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4346
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4996 traffic_type=None
```

### `maze_occupancy_6x6_adj_34.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='PISVadD7LoOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1281,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1281
    ),
  ],
  total_token_count=1931
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1281 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1281
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1931 traffic_type=None
```

### `maze_occupancy_6x6_ascii_34.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, down, left, down, right, right, right, down, left, down, left, down, right, right, down, right, right, right, up, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, left, down, left, down, right, right, right, up, up, right, right, right, up, up, up, up, up, up, up, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right, right, right, down, left, down, left, down, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,down,left,down,right,right,right,down,left,down,left,down,right,right,down,right,right,right,up,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,left,down,left,down,right,right,right,up,up,right,right,right,up,up,up,up,up,up,up,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,right,right,down,left,down,left,down,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='P4SVab2WCduxnsEPg_7zyAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=254,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=254
    ),
  ],
  total_token_count=904
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=254 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=254
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=904 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_34.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QYSVadbTHqPwnsEPgLOouAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

