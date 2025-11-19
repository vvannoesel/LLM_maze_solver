# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_8.jpg` | **0.00%** | `input: 427 , ouput: 15` | `down, right, down, right, down, right, down, right` |
| `maze_line_6x6_8.json` | **0.00%** | `input: 1802 , ouput: 21` | `down, down, right, down, right, right, down, right, down, right, right` |
| `maze_line_6x6_adj_8.json` | **110.00%** | `input: 2251 , ouput: 27` | `right, right, right, right, down, down, down, down, down, right, right, right, right, down` |
| `maze_line_6x6_adj_8.txt` | **60.00%** | `input: 722 , ouput: 27` | `right, right, right, right, down, down, right, down, down, down, right, right, down, right` |
| `maze_line_6x6_tokenized_8.txt` | **10.00%** | `input: 666 , ouput: 33` | `right, down, right, right, down, right, down, left, down, right, right, up, right, down, down, right, down` |
| `maze_occupancy_6x6_8.jpg` | **5.00%** | `input: 424 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right` |
| `maze_occupancy_6x6_8.json` | **80.00%** | `input: 981 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down` |
| `maze_occupancy_6x6_adj_8.json` | **50.00%** | `input: 4335 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down` |
| `maze_occupancy_6x6_adj_8.txt` | **90.00%** | `input: 1267 , ouput: 47` | `right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right` |
| `maze_occupancy_6x6_ascii_8.txt` | **55.00%** | `input: 246 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, down, right, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_8.txt` | **40.00%** | `input: 2155 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_6x6_8.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, down, right
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w98daZe-B8eSxN8P7IGBoAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
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
  total_token_count=442
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=442 traffic_type=None
```

### `maze_line_6x6_8.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, down, right
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
        text='down,down,right,down,right,right,down,right,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w98daZSINP_WvdIPm53psAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_8.json`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,right,right,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xd8daceCBealvdIPmN-H4QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2278
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2278 traffic_type=None
```

### `maze_line_6x6_adj_8.txt`

**Score:** 60.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, down, down, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,down,down,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xd8daZ2eLd_UvdIPtoDHyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=749
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=749 traffic_type=None
```

### `maze_line_6x6_tokenized_8.txt`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down, down, right
```

**Extracted Answer:**
```
right, down, right, right, down, right, down, left, down, right, right, up, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,right,down,left,down,right,right,up,right,down,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xt8dacP-F_SOvdIP7bjwwQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=699
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=699 traffic_type=None
```

### `maze_occupancy_6x6_8.jpg`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yN8dafK0LofYxs0PzZjGyQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1074
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1074 traffic_type=None
```

### `maze_occupancy_6x6_8.json`

**Score:** 80.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='y98daZ2sCd_UvdIPtoDHyAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_8.json`

**Score:** 50.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zt8dad-wIaePvdIPj5TpsQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4335,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4335
    ),
  ],
  total_token_count=4985
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4335 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4335
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4985 traffic_type=None
```

### `maze_occupancy_6x6_adj_8.txt`

**Score:** 90.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='z98daYr5Dv7hxN8PyeLZ6Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=1267,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1267
    ),
  ],
  total_token_count=1314
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=1267 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1267
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1314 traffic_type=None
```

### `maze_occupancy_6x6_ascii_8.txt`

**Score:** 55.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, right, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,right,down,down,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0d8dadHxIN-kvdIPgMvu8AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=246
    ),
  ],
  total_token_count=896
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=896 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_8.txt`

**Score:** 40.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1N8dafuyMqTyxs0PnYinqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

