# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_11.jpg` | **7.14%** | `input: 434 , ouput: 23` | `right, down, right, down, right, down, left, down, right, right, down, right` |
| `maze_line_6x6_11.json` | **42.86%** | `input: 1809 , ouput: 23` | `right, right, right, right, down, down, down, right, down, down, right, right` |
| `maze_line_6x6_adj_11.json` | **42.86%** | `input: 2258 , ouput: 29` | `right, right, right, right, down, down, right, down, down, right, right, down, down, right, right` |
| `maze_line_6x6_adj_11.txt` | **42.86%** | `input: 729 , ouput: 25` | `right, right, right, right, down, down, right, down, down, right, right, down, right` |
| `maze_line_6x6_tokenized_11.txt` | **7.14%** | `input: 673 , ouput: 29` | `right, down, right, down, right, down, right, down, left, down, left, down, left, down, left` |
| `maze_occupancy_6x6_11.jpg` | **3.57%** | `input: 431 , ouput: 650` | `right, down, down, right, right, down, down, right, right, right, up, right, down, down, down, left, down, right, right, right, up, right, up, right, down, down, down, left, down, down, right, right, right, right, down, down, down, left, left, up, left, up, up, right, right, down, down, down, left, left, left, up, up, up, right, right, down, down, right, right, down, down, left, left, left, up, up, up, right, right, right, right, down, down, down, down, left, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, left, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up` |
| `maze_occupancy_6x6_11.json` | **28.57%** | `input: 988 , ouput: 125` | `right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_11.json` | **39.29%** | `input: 4346 , ouput: 59` | `right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_11.txt` | **0.00%** | `input: 1277 , ouput: 650` | `down, right, right, right, right, right, right, right, down, down, right, down, right, right, right, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right` |
| `maze_occupancy_6x6_ascii_11.txt` | **50.00%** | `input: 241 , ouput: 57` | `right, right, right, right, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_11.txt` | **28.57%** | `input: 2162 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_11.jpg`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, right, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, left, down, right, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Bn-VadKVMoqjkdUP-qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_11.json`

**Score:** 42.86%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, down, down, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B3-VabOfKIWF7M8PnoeMqQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_11.json`

**Score:** 42.86%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CH-VaaGuHK7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_11.txt`

**Score:** 42.86%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, down, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,down,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CX-VabbJDJC-nsEPxMmk4QY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_11.txt`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, right, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, left, down, left, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,left,down,left,down,left'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CX-VadH8KtihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=702
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=702 traffic_type=None
```

### `maze_occupancy_6x6_11.jpg`

**Score:** 3.57%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, right, right, up, right, down, down, down, left, down, right, right, right, up, right, up, right, down, down, down, left, down, down, right, right, right, right, down, down, down, left, left, up, left, up, up, right, right, down, down, down, left, left, left, up, up, up, right, right, down, down, right, right, down, down, left, left, left, up, up, up, right, right, right, right, down, down, down, down, left, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, left, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,right,right,up,right,down,down,down,left,down,right,right,right,up,right,up,right,down,down,down,left,down,down,right,right,right,right,down,down,down,left,left,up,left,up,up,right,right,down,down,down,left,left,left,up,up,up,right,right,down,down,right,right,down,down,left,left,left,up,up,up,right,right,right,right,down,down,down,down,left,left,left,up,up,up,up,right,right,right,right,down,down,down,down,down,left,left,left,up,up,up,up,right,right,right,right,down,down,down,down,down,down,left,left,left,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,up,up,up,up,up,up,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TX-VafP-Ho65kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_11.json`

**Score:** 28.57%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Tn-Vaa3sFffonsEPwaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=125,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1113
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=125 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1113 traffic_type=None
```

### `maze_occupancy_6x6_adj_11.json`

**Score:** 39.29%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T3-VaZO0Dcjl7M8P9OOViAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=4346,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4346
    ),
  ],
  total_token_count=4405
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=4346 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4346
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4405 traffic_type=None
```

### `maze_occupancy_6x6_adj_11.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, right, right, right, right, down, down, right, down, right, right, right, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, right, right, right, right, right, down, down, right, down, right, right, right, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UH-VacvPJpPe7M8PjqaxkQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_11.txt`

**Score:** 50.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,down,left,left,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UX-VafLPFoTw7M8P482J-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=241,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=241
    ),
  ],
  total_token_count=298
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=241 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=241
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=298 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_11.txt`

**Score:** 28.57%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Un-VabamMoOH7M8PxuqcmAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

