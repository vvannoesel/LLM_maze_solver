# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_18.jpg` | **8.33%** | `input: 434 , ouput: 21` | `right, down, right, down, down, right, up, right, down, down, right` |
| `maze_line_6x6_18.json` | **0.00%** | `input: 1809 , ouput: 21` | `down, down, right, down, right, right, down, right, down, right, right` |
| `maze_line_6x6_adj_18.json` | **8.33%** | `input: 2258 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_adj_18.txt` | **8.33%** | `input: 729 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_tokenized_18.txt` | **12.50%** | `input: 673 , ouput: 31` | `right, down, down, down, right, right, down, right, up, right, down, down, left, down, right, right` |
| `maze_occupancy_6x6_18.jpg` | **2.08%** | `input: 431 , ouput: 51` | `right, down, right, down, right, down, right, down, left, down, left, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down` |
| `maze_occupancy_6x6_18.json` | **2.08%** | `input: 988 , ouput: 650` | `right, down, down, down, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right` |
| `maze_occupancy_6x6_adj_18.json` | **4.17%** | `input: 4345 , ouput: 650` | `right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_18.txt` | **4.17%** | `input: 1276 , ouput: 249` | `right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right` |
| `maze_occupancy_6x6_ascii_18.txt` | **10.42%** | `input: 256 , ouput: 73` | `right, right, down, down, down, right, down, down, down, right, right, right, down, down, down, right, right, right, right, right, right, up, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_18.txt` | **8.33%** | `input: 2162 , ouput: 650` | `right, right, down, down, right, down, right, down, down, right, down, right, down, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down` |

---

## Full LLM Responses

### `maze_line_6x6_18.jpg`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, down, left, down, down, down, right, up, right, up, right, up, up, up, right, down, down, right, down, down, left, down, right
```

**Extracted Answer:**
```
right, down, right, down, down, right, up, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,up,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AYKVaaHMFPyc28oP77OrsAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_18.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, left, down, down, down, right, up, right, up, right, up, up, up, right, down, down, right, down, down, left, down, right
```

**Extracted Answer:**
```
down, down, right, down, right, right, down, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, right, down, right, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AYKVabCvPN7mxs0P4czy8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1830
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1830 traffic_type=None
```

### `maze_line_6x6_adj_18.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, down, left, down, down, down, right, up, right, up, right, up, up, up, right, down, down, right, down, down, left, down, right
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
        text='right,down,right,down,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AoKVabapOI3ZvdIPlZKdgQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_18.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, down, left, down, down, down, right, up, right, up, right, up, up, up, right, down, down, right, down, down, left, down, right
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
        text='right,down,right,down,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='A4KVaYuXJ8HWxs0PwvX2iQ4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_18.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, down, down, left, down, down, down, right, up, right, up, right, up, up, up, right, down, down, right, down, down, left, down, right
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, right, up, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, down, right, right, down, right, up, right, down, down, left, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BIKVaZTzEOGlxN8Pl_3riAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=704
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=704 traffic_type=None
```

### `maze_occupancy_6x6_18.jpg`

**Score:** 2.08%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, left, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, left, down, left, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BYKVaaClGdfIvdIPlo3gqAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_18.json`

**Score:** 2.08%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,down,down,right,right,right,down,down,down,right,right,right,down,down,right,right,right,down,down,down,right,right,right,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B4KVabfuKYrbxN8P14bjqQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_18.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CYKVaYOSEIKVxN8Pts2XoAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4345,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4345
    ),
  ],
  total_token_count=4995
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4345 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4345
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4995 traffic_type=None
```

### `maze_occupancy_6x6_adj_18.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CoKVaYzVIpuZ28oPjdqtsAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=249,
  prompt_token_count=1276,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1276
    ),
  ],
  total_token_count=1525
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=249 candidates_tokens_details=None prompt_token_count=1276 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1276
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1525 traffic_type=None
```

### `maze_occupancy_6x6_ascii_18.txt`

**Score:** 10.42%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, down, right, down, down, down, right, right, right, down, down, down, right, right, right, right, right, right, up, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,right,down,down,down,right,right,right,down,down,down,right,right,right,right,right,right,up,up,right,right,right,down,down,down,down,down,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='C4KVacizFLvzxs0Ps7mRkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=73,
  prompt_token_count=256,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=256
    ),
  ],
  total_token_count=329
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=73 candidates_tokens_details=None prompt_token_count=256 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=256
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=329 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_18.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, down, right, down, down, right, down, right, down, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, down, right, down, right, down, down, right, down, right, down, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DYKVabvbLouX28oP-LHd-QI' usage_metadata=GenerateContentResponseUsageMetadata(
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

