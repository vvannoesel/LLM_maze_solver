# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_39.jpg` | **4.55%** | `input: 434 , ouput: 17` | `right, right, down, down, right, down, down, right, right` |
| `maze_line_6x6_39.json` | **0.00%** | `input: 1809 , ouput: 57` | `down, down, down, down, right, right, right, right, right, up, up, up, up, down, right, right, down, down, down, right, right, right, up, up, up, up, up, right, right` |
| `maze_line_6x6_adj_39.json` | **13.64%** | `input: 2258 , ouput: 21` | `right, down, right, down, down, right, down, right, down, right, down` |
| `maze_line_6x6_adj_39.txt` | **4.55%** | `input: 729 , ouput: 25` | `right, right, right, right, down, down, right, down, down, right, right, down, down` |
| `maze_line_6x6_tokenized_39.txt` | **13.64%** | `input: 673 , ouput: 650` | `right, down, right, down, right, down, left, down, right, right, up, right, down, left, down, right, right, up, right, up, left, down, right, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right` |
| `maze_occupancy_6x6_39.jpg` | **2.27%** | `input: 431 , ouput: 69` | `right, down, right, down, right, down, down, right, down, right, up, right, down, right, down, left, down, right, right, down, right, up, right, down, left, down, right, right, up, right, down, left, down, right, right` |
| `maze_occupancy_6x6_39.json` | **11.36%** | `input: 988 , ouput: 650` | `right, right, down, down, right, down, down, right, right, down, down, down, right, right, right, down, right, down, down, down, right, right, right, right, down, down, right, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right` |
| `maze_occupancy_6x6_adj_39.json` | **6.82%** | `input: 4342 , ouput: 41` | `right, right, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_39.txt` | **4.55%** | `input: 1278 , ouput: 650` | `right, right, right, down, down, right, right, right, right, right, right, down, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down` |
| `maze_occupancy_6x6_ascii_39.txt` | **6.82%** | `input: 252 , ouput: 650` | `right, right, down, right, right, right, down, right, right, down, right, down, down, left, down, right, right, right, right, up, right, down, down, left, left, down, right, right, right, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right` |
| `maze_occupancy_6x6_tokenized_39.txt` | **0.00%** | `input: 2162 , ouput: 650` | `down, right, right, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_39.jpg`

**Score:** 4.55%

**Ground Truth Solution:**
```
right, down, right, right, down, left, down, left, up, left, down, down, down, right, up, right, down, right, right, up, right, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n4SVacLzGYOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_39.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, right, down, left, down, left, up, left, down, down, down, right, up, right, down, right, right, up, right, down
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right, right, up, up, up, up, down, right, right, down, down, down, right, right, right, up, up, up, up, up, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,right,right,right,right,right,up,up,up,up,down,right,right,down,down,down,right,right,right,up,up,up,up,up,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oISVaabyBvT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1866
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1866 traffic_type=None
```

### `maze_line_6x6_adj_39.json`

**Score:** 13.64%

**Ground Truth Solution:**
```
right, down, right, right, down, left, down, left, up, left, down, down, down, right, up, right, down, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oISVacmbLJnqkdUP57jkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2279
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2279 traffic_type=None
```

### `maze_line_6x6_adj_39.txt`

**Score:** 4.55%

**Ground Truth Solution:**
```
right, down, right, right, down, left, down, left, up, left, down, down, down, right, up, right, down, right, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, down, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,down,down,right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oYSVaZHMGMyynsEPyd_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_39.txt`

**Score:** 13.64%

**Ground Truth Solution:**
```
right, down, right, right, down, left, down, left, up, left, down, down, down, right, up, right, down, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, up, right, down, left, down, right, right, up, right, up, left, down, right, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right, right, up, right, up, left, down, right, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,up,right,down,left,down,right,right,up,right,up,left,down,right,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,right,up,right,up,left,down,right,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o4SVaezdIa2WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_39.jpg`

**Score:** 2.27%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, down, right, down, right, up, right, down, right, down, left, down, right, right, down, right, up, right, down, left, down, right, right, up, right, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,down,right,down,right,up,right,down,right,down,left,down,right,right,down,right,up,right,down,left,down,right,right,up,right,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pISVaeXRK8PPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=69,
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
  total_token_count=500
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=69 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=500 traffic_type=None
```

### `maze_occupancy_6x6_39.json`

**Score:** 11.36%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, down, right, right, down, down, down, right, right, right, down, right, down, down, down, right, right, right, right, down, down, right, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,down,right,right,down,down,down,right,right,right,down,right,down,down,down,right,right,right,right,down,down,right,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='poSVaYzmEtHMkdUPjY-7sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_39.json`

**Score:** 6.82%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='poSVaYKfO9WbkdUPuuCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=4342,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4342
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=4342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4383 traffic_type=None
```

### `maze_occupancy_6x6_adj_39.txt`

**Score:** 4.55%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, right, right, right, right, down, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, down, down, right, right, right, right, right, right, down, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qYSVacePBvKcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_39.txt`

**Score:** 6.82%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, right, down, right, right, down, right, down, down, left, down, right, right, right, right, up, right, down, down, left, left, down, right, right, right, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right, right, up, up, right, right, down, down, left, left, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,down,right,right,down,right,down,down,left,down,right,right,right,right,up,right,down,down,left,left,down,right,right,right,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,right,up,up,right,right,down,down,left,left,left,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='q4SVabuiH-yOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=252,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=252
    ),
  ],
  total_token_count=902
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=252 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=252
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=902 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rYSVacfbI9qfnsEPzfyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

