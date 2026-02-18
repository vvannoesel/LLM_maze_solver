# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_38.jpg` | **7.14%** | `input: 434 , ouput: 17` | `right, down, right, down, down, right, right, down, right` |
| `maze_line_6x6_38.json` | **7.14%** | `input: 1809 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_adj_38.json` | **28.57%** | `input: 2258 , ouput: 29` | `right, right, down, down, right, right, down, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_38.txt` | **28.57%** | `input: 729 , ouput: 21` | `right, right, down, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_tokenized_38.txt` | **7.14%** | `input: 673 , ouput: 27` | `right, down, right, right, right, down, down, left, down, right, right, down, down, right` |
| `maze_occupancy_6x6_38.jpg` | **3.57%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left` |
| `maze_occupancy_6x6_38.json` | **14.29%** | `input: 988 , ouput: 650` | `right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right` |
| `maze_occupancy_6x6_adj_38.json` | **nan%** | `input: 4340 , ouput: 0` | `` |
| `maze_occupancy_6x6_adj_38.txt` | **25.00%** | `input: 1277 , ouput: 650` | `right, right, right, right, down, down, down, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_38.txt` | **21.43%** | `input: 248 , ouput: 81` | `right, right, right, right, down, down, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_tokenized_38.txt` | **14.29%** | `input: 2162 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_38.jpg`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, down, down, left, down, down, right, right, right, up, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, down, right, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='joSVacfOOtuxnsEPg_7zyAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_38.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, down, down, left, down, down, right, right, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j4SVaYznOI65kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_38.json`

**Score:** 28.57%

**Ground Truth Solution:**
```
right, right, down, down, left, down, down, right, right, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kISVaarBLOjpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_38.txt`

**Score:** 28.57%

**Ground Truth Solution:**
```
right, right, down, down, left, down, down, right, right, right, up, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kYSVafWXHdWbkdUPueCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=750
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=750 traffic_type=None
```

### `maze_line_6x6_tokenized_38.txt`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, down, down, left, down, down, right, right, right, up, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, right, down, down, left, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,down,down,left,down,right,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='koSVae-dENqfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=700
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=700 traffic_type=None
```

### `maze_occupancy_6x6_38.jpg`

**Score:** 3.57%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lISVaaSlKoqjkdUPl43u2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_38.json`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='loSVaby2LLyK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_38.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mYSVaZ31M7yK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_38.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, down, down, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m4SVaZaoOeO9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_38.txt`

**Score:** 21.43%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nISVabXDMuO9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=81,
  prompt_token_count=248,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=248
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=81 candidates_tokens_details=None prompt_token_count=248 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=248
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=329 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_38.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='noSVadWKH4yD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

