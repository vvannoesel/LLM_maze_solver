# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_32.jpg` | **0.00%** | `input: 434 , ouput: 23` | `down, right, down, right, right, down, left, down, right, right, down, right` |
| `maze_line_6x6_32.json` | **6.67%** | `input: 1809 , ouput: 23` | `right, down, down, right, down, right, right, down, right, down, down, right` |
| `maze_line_6x6_adj_32.json` | **3.33%** | `input: 2258 , ouput: 29` | `right, right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_32.txt` | **0.00%** | `input: 729 , ouput: 25` | `down, right, right, down, down, right, down, right, right, down, right, down, right` |
| `maze_line_6x6_tokenized_32.txt` | **6.67%** | `input: 673 , ouput: 21` | `right, down, down, right, right, down, down, left, down, right, right` |
| `maze_occupancy_6x6_32.jpg` | **1.67%** | `input: 431 , ouput: 650` | `right, down, right, down, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down` |
| `maze_occupancy_6x6_32.json` | **1.67%** | `input: 988 , ouput: 650` | `right, down, down, right, right, down, down, right, right, right, down, down, right, right, right, down, down, left, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down` |
| `maze_occupancy_6x6_adj_32.json` | **13.33%** | `input: 4342 , ouput: 650` | `right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down` |
| `maze_occupancy_6x6_adj_32.txt` | **0.00%** | `input: 1278 , ouput: 650` | `down, down, right, right, right, down, down, right, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right` |
| `maze_occupancy_6x6_ascii_32.txt` | **6.67%** | `input: 247 , ouput: 650` | `right, right, down, down, left, down, right, right, right, right, down, right, down, left, left, down, right, right, right, right, right, up, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_6x6_tokenized_32.txt` | **0.00%** | `input: 2162 , ouput: 650` | `down, right, right, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down` |

---

## Full LLM Responses

### `maze_line_6x6_32.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, right, down, down, left, up, left, left, up, left, left, down, down, down, right, up, right, down, right, right, right
```

**Extracted Answer:**
```
down, right, down, right, right, down, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,right,down,left,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HIOVadr0I_rhnsEP9oTP2Qk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_32.json`

**Score:** 6.67%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, right, down, down, left, up, left, left, up, left, left, down, down, down, right, up, right, down, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, down, right, right, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, down, right, right, down, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HYOVaanXB9qfnsEPvPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_32.json`

**Score:** 3.33%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, right, down, down, left, up, left, left, up, left, left, down, down, down, right, up, right, down, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, right, down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HYOVafj5O6rw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, right, down, down, left, up, left, left, up, left, left, down, down, down, right, up, right, down, right, right, right
```

**Extracted Answer:**
```
down, right, right, down, down, right, down, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,down,right,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HoOVaZ2lIqzd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_32.txt`

**Score:** 6.67%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, right, down, down, left, up, left, left, up, left, left, down, down, down, right, up, right, down, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='H4OVaZq8DO3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=694
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=694 traffic_type=None
```

### `maze_occupancy_6x6_32.jpg`

**Score:** 1.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, up, up, left, left, left, left, up, up, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IoOVafCsGqjlnsEP1bugwAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_32.json`

**Score:** 1.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, up, up, left, left, left, left, up, up, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, right, right, down, down, right, right, right, down, down, left, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,right,right,down,down,right,right,right,down,down,left,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JIOVabSsAYKG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_32.json`

**Score:** 13.33%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, up, up, left, left, left, left, up, up, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JoOVadu-B465kdUPy9PImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4342,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4342
    ),
  ],
  total_token_count=4992
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4992 traffic_type=None
```

### `maze_occupancy_6x6_adj_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, up, up, left, left, left, left, up, up, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, down, down, right, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,down,right,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KIOVabyUFuyOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_32.txt`

**Score:** 6.67%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, up, up, left, left, left, left, up, up, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, left, down, right, right, right, right, down, right, down, left, left, down, right, right, right, right, right, up, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=336,
        license='',
        start_index=136,
        uri='https://github.com/Amable-Valdes/Prolog-Mazes'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,left,down,right,right,right,right,down,right,down,left,left,down,right,right,right,right,right,up,right,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KoOVafyTMaeN7M8P6NXVwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=247,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=247
    ),
  ],
  total_token_count=897
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=247 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=247
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=897 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, up, up, left, left, left, left, up, up, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LIOVad3TB6OF7M8P9PzH6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

