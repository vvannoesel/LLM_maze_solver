# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_1.jpg` | **6.25%** | `input: 427 , ouput: 31` | `down, right, down, right, down, right, down, right, up, right, down, down, right, up, right, down` |
| `maze_line_6x6_1.json` | **12.50%** | `input: 1802 , ouput: 21` | `down, down, right, right, down, right, down, right, right, down, right` |
| `maze_line_6x6_adj_1.json` | **18.75%** | `input: 2251 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_1.txt` | **25.00%** | `input: 722 , ouput: 25` | `down, down, down, right, right, down, down, right, right, right, down, right, right` |
| `maze_line_6x6_tokenized_1.txt` | **0.00%** | `input: 666 , ouput: 43` | `right, down, right, down, right, down, right, down, left, down, left, left, up, left, up, up, right, up, right, right, down, right` |
| `maze_occupancy_6x6_1.jpg` | **0.00%** | `input: 424 , ouput: 61` | `right, down, down, down, right, right, down, down, right, right, right, up, right, down, down, down, down, left, down, down, right, right, right, right, up, up, right, right, down, down, down` |
| `maze_occupancy_6x6_1.json` | **0.00%** | `input: 981 , ouput: 650` | `right, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_1.json` | **18.75%** | `input: 4342 , ouput: 65` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_1.txt` | **18.75%** | `input: 1272 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_ascii_1.txt` | **6.25%** | `input: 245 , ouput: 650` | `down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right` |
| `maze_occupancy_6x6_tokenized_1.txt` | **0.00%** | `input: 2155 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_6x6_1.jpg`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, down, right, down, down, right, right, up, right, up, up, right, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, down, down, right, up, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,up,right,down,down,right,up,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Gd8dab_lCrDTxN8Pj8DlmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=427,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=169
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=458
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=427 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=458 traffic_type=None
```

### `maze_line_6x6_1.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, down, right, down, down, right, right, up, right, up, up, right, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,right,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Gd8dab_kPIHhvdIPo9CWoAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1823
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=185 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1823 traffic_type=None
```

### `maze_line_6x6_adj_1.json`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, down, down, right, down, down, right, right, up, right, up, up, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G98dadGJAZfOvdIPsNOE0Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2270
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2270 traffic_type=None
```

### `maze_line_6x6_adj_1.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
down, down, down, right, down, down, right, right, up, right, up, up, right, down, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, down, down, right, right, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,down,down,right,right,right,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HN8dae6gD4zKvdIP5Nu3oAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=747
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=747 traffic_type=None
```

### `maze_line_6x6_tokenized_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, down, down, right, right, up, right, up, up, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, left, left, up, left, up, up, right, up, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,left,left,up,left,up,up,right,up,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Hd8daa22Ds3VvdIP5qGjwQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=709
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=187 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=709 traffic_type=None
```

### `maze_occupancy_6x6_1.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, down, right, right, right, up, right, down, down, down, down, left, down, down, right, right, right, right, up, up, right, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,down,down,right,right,right,up,right,down,down,down,down,left,down,down,right,right,right,right,up,up,right,right,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ht8dadvLO9_UvdIPtoDHyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=424,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=166
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=485
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=424 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=485 traffic_type=None
```

### `maze_occupancy_6x6_1.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='It8dabjLGfuDvdIPn_iEyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=981,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=981
    ),
  ],
  total_token_count=1631
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=167 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=981 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=981
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1631 traffic_type=None
```

### `maze_occupancy_6x6_adj_1.json`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I98dafSrCfXzxs0Pn66hoAk' usage_metadata=GenerateContentResponseUsageMetadata(
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
) total_tokens=158 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=65 candidates_tokens_details=None prompt_token_count=4342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4407 traffic_type=None
```

### `maze_occupancy_6x6_adj_1.txt`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Jt8daevtBJfOvdIPsNOE0Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1272,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1272
    ),
  ],
  total_token_count=1922
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=191 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1272 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1272
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1922 traffic_type=None
```

### `maze_occupancy_6x6_ascii_1.txt`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Kd8daZrpJ4mHxN8PivzW-Q8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=245,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=245
    ),
  ],
  total_token_count=895
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=166 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=245 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=245
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=895 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ld8daeKfBeaavdIPio31oQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2155,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2155
    ),
  ],
  total_token_count=2805
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=190 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2155 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2155
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2805 traffic_type=None
```

