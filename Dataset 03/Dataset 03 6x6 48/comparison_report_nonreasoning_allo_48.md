# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_48.jpg` | **0.00%** | `input: 434 , ouput: 19` | `right, down, right, down, right, down, down, right, down, right` |
| `maze_line_6x6_48.json` | **9.09%** | `input: 1809 , ouput: 23` | `down, down, down, right, right, down, right, right, down, down, right, right` |
| `maze_line_6x6_adj_48.json` | **9.09%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_48.txt` | **0.00%** | `input: 729 , ouput: 19` | `right, right, right, right, down, down, down, down, down, down` |
| `maze_line_6x6_tokenized_48.txt` | **0.00%** | `input: 673 , ouput: 650` | `right, down, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left` |
| `maze_occupancy_6x6_48.jpg` | **0.00%** | `input: 431 , ouput: 45` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right` |
| `maze_occupancy_6x6_48.json` | **0.00%** | `input: 988 , ouput: 71` | `right, down, down, right, right, right, right, right, right, down, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_48.json` | **9.09%** | `input: 4340 , ouput: 650` | `down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down` |
| `maze_occupancy_6x6_adj_48.txt` | **0.00%** | `input: 1277 , ouput: 51` | `right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_48.txt` | **9.09%** | `input: 245 , ouput: 297` | `down, down, down, down, down, right, right, right, down, down, right, right, right, right, up, up, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_48.txt` | **2.27%** | `input: 2162 , ouput: 650` | `down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down` |

---

## Full LLM Responses

### `maze_line_6x6_48.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, left, down, left, up, left, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VYWVaZenIoqjkdUPl43u2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_48.json`

**Score:** 9.09%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, left, down, left, up, left, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
down, down, down, right, right, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VoWVab6FCdqfnsEPvPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_48.json`

**Score:** 9.09%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, left, down, left, up, left, left, down, down, right, right, right, right, up, right, down
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
        text='down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VoWVaY2CMujpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, left, down, left, up, left, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, down, down, down, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V4WVacizEoqjkdUP8qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=748
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=748 traffic_type=None
```

### `maze_line_6x6_tokenized_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, left, down, left, up, left, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left, left, down, right, right, right, down, down, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,left,down,right,right,right,down,down,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WYWVaYGXGffo7M8PiZSSoQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_48.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WoWVabKzF7T7nsEPovPikQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
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
  total_token_count=476
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=476 traffic_type=None
```

### `maze_occupancy_6x6_48.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, right, right, down, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,right,right,down,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='W4WVabfMCK7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=71,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1059
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=71 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1059 traffic_type=None
```

### `maze_occupancy_6x6_adj_48.json`

**Score:** 9.09%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XYWVadfNCazd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4340,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4340
    ),
  ],
  total_token_count=4990
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4340 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4340
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4990 traffic_type=None
```

### `maze_occupancy_6x6_adj_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XYWVaaz8OK2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=1277,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1277
    ),
  ],
  total_token_count=1328
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=1277 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1277
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1328 traffic_type=None
```

### `maze_occupancy_6x6_ascii_48.txt`

**Score:** 9.09%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, down, down, right, right, right, right, up, up, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,down,down,right,right,right,right,up,up,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,right,right,up,up,up,up,up,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,left,left,left,left,left,left,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='X4WVadifGYyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=297,
  prompt_token_count=245,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=245
    ),
  ],
  total_token_count=542
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=297 candidates_tokens_details=None prompt_token_count=245 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=245
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=542 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_48.txt`

**Score:** 2.27%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YYWVacHPIO3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

