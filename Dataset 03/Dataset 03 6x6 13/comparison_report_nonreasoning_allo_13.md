# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_13.jpg` | **0.00%** | `input: 434 , ouput: 23` | `down, right, right, down, right, down, right, down, left, down, right, right` |
| `maze_line_6x6_13.json` | **0.00%** | `input: 1809 , ouput: 19` | `down, right, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_13.json` | **8.33%** | `input: 2258 , ouput: 23` | `right, right, right, right, right, down, down, down, down, down, right, right` |
| `maze_line_6x6_adj_13.txt` | **8.33%** | `input: 729 , ouput: 25` | `right, right, right, right, down, down, down, down, down, down, right, right, right` |
| `maze_line_6x6_tokenized_13.txt` | **16.67%** | `input: 673 , ouput: 23` | `right, down, right, down, right, right, down, down, left, down, right, right` |
| `maze_occupancy_6x6_13.jpg` | **4.17%** | `input: 431 , ouput: 650` | `right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left` |
| `maze_occupancy_6x6_13.json` | **20.83%** | `input: 988 , ouput: 650` | `right, right, down, down, down, right, down, down, down, down, down, down, left, down, left, left, left, up, left, up, up, up, up, right, right, right, down, right, right, right, down, left, down, down, down, right, right, right, down, down, down, right, right, right, down, right, down, left, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_13.json` | **16.67%** | `input: 4349 , ouput: 650` | `right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right` |
| `maze_occupancy_6x6_adj_13.txt` | **8.33%** | `input: 1279 , ouput: 650` | `right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right` |
| `maze_occupancy_6x6_ascii_13.txt` | **16.67%** | `input: 254 , ouput: 650` | `right, right, down, down, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, up, right, up, up, right, right, right, down, down, down, down, down, left, left, left, left, left, down, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_6x6_tokenized_13.txt` | **25.00%** | `input: 2162 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_13.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, right, up, right, down, down, right, down, right, down
```

**Extracted Answer:**
```
down, right, right, down, right, down, right, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,right,down,right,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ooGVac2AG4-VkdUPpZbhqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_13.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, right, up, right, down, down, right, down, right, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o4GVaZf9A4DHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_13.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, down, right, up, right, down, down, right, down, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o4GVaeSHJ9qI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2281
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2281 traffic_type=None
```

### `maze_line_6x6_adj_13.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, down, right, up, right, down, down, right, down, right, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, down, down, down, down, down, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pIGVaYueEoyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_13.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, down, down, right, up, right, down, down, right, down, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,right,down,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pIGVaeXfOOjpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=696
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=696 traffic_type=None
```

### `maze_occupancy_6x6_13.jpg`

**Score:** 4.17%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='p4GVaYHECtqgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_13.json`

**Score:** 20.83%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, right, down, down, down, down, down, down, left, down, left, left, left, up, left, up, up, up, up, right, right, right, down, right, right, right, down, left, down, down, down, right, right, right, down, down, down, right, right, right, down, right, down, left, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,right,down,down,down,down,down,down,left,down,left,left,left,up,left,up,up,up,up,right,right,right,down,right,right,right,down,left,down,down,down,right,right,right,down,down,down,right,right,right,down,right,down,left,down,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qYGVacvSBeTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_13.json`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='q4GVaYKqDqzd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4349,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4349
    ),
  ],
  total_token_count=4999
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4349 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4349
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4999 traffic_type=None
```

### `maze_occupancy_6x6_adj_13.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rYGVaZqyILyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_13.txt`

**Score:** 16.67%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, up, right, up, up, right, right, right, down, down, down, down, down, left, left, left, left, left, down, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,right,right,down,down,down,down,right,right,right,right,up,right,up,up,right,right,right,down,down,down,down,down,left,left,left,left,left,down,right,right,right,right,right,right,right,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='r4GVadzMNsPwnsEPpffzuQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_tokenized_13.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='soGVaffBCqnw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

