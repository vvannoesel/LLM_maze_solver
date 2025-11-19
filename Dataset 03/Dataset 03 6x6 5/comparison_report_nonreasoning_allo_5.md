# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_5.jpg` | **0.00%** | `input: 427 , ouput: 31` | `right, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right` |
| `maze_line_6x6_5.json` | **21.43%** | `input: 1802 , ouput: 23` | `down, down, right, right, down, right, down, right, right, down, down, right` |
| `maze_line_6x6_adj_5.json` | **0.00%** | `input: 2251 , ouput: 29` | `right, right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_5.txt` | **21.43%** | `input: 722 , ouput: 23` | `down, down, right, right, down, down, right, right, down, right, down, right` |
| `maze_line_6x6_tokenized_5.txt` | **21.43%** | `input: 666 , ouput: 650` | `down, down, right, right, right, down, down, left, left, down, right, right, right, up, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right` |
| `maze_occupancy_6x6_5.jpg` | **3.57%** | `input: 424 , ouput: 650` | `down, right, right, down, right, down, left, down, right, down, right, right, down, left, left, down, right, right, right, up, right, down, down, left, down, left, left, down, right, down, down, right, right, right, up, right, up, right, down, down, left, left, down, down, right, right, right, up, right, up, left, down, down, right, down, right, up, right, down, right, up, up, left, down, right, up, left, down, right, up, up, left, left, down, right, down, right, up, up, left, left, down, right, down, right, up, left, up, left, down, right, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right` |
| `maze_occupancy_6x6_5.json` | **0.00%** | `input: 981 , ouput: 650` | `right, down, down, down, right, right, right, down, down, right, down, down, right, right, right, right, down, down, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right` |
| `maze_occupancy_6x6_adj_5.json` | **14.29%** | `input: 4342 , ouput: 650` | `down, down, down, down, down, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right` |
| `maze_occupancy_6x6_adj_5.txt` | **14.29%** | `input: 1272 , ouput: 53` | `down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_5.txt` | **0.00%** | `input: 245 , ouput: 650` | `right, right, down, down, right, right, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, down, down, right, right, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down` |
| `maze_occupancy_6x6_tokenized_5.txt` | **nan%** | `input: 2155 , ouput: 0` | `` |

---

## Full LLM Responses

### `maze_line_6x6_5.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, right, down, down, right, down, down, right
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,right,up,right,down,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='a98daanuIfjXxs0P146HoQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_5.json`

**Score:** 21.43%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, right, down, down, right, down, down, right
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, right, down, right, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bN8daeXiL_SOvdIP7bjwwQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1825
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1825 traffic_type=None
```

### `maze_line_6x6_adj_5.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, right, down, down, right, down, down, right
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
        text='right,right,right,right,right,down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bd8daeyAIev-xN8P1_-n0A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2280
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2280 traffic_type=None
```

### `maze_line_6x6_adj_5.txt`

**Score:** 21.43%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, right, down, down, right, down, down, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bt8dadGtIq_9xN8Pgt6ymQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=745
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=745 traffic_type=None
```

### `maze_line_6x6_tokenized_5.txt`

**Score:** 21.43%

**Ground Truth Solution:**
```
down, down, right, up, up, right, down, right, down, down, right, down, down, right
```

**Extracted Answer:**
```
down, down, right, right, right, down, down, left, left, down, right, right, right, up, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,down,left,left,down,right,right,right,up,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cd8daZulC9WNvdIPo9-nuA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=1316
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1316 traffic_type=None
```

### `maze_occupancy_6x6_5.jpg`

**Score:** 3.57%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, right, right, down, right, down, left, down, right, down, right, right, down, left, left, down, right, right, right, up, right, down, down, left, down, left, left, down, right, down, down, right, right, right, up, right, up, right, down, down, left, left, down, down, right, right, right, up, right, up, left, down, down, right, down, right, up, right, down, right, up, up, left, down, right, up, left, down, right, up, up, left, left, down, right, down, right, up, up, left, left, down, right, down, right, up, left, up, left, down, right, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right, up, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1564,
        license='',
        start_index=456,
        uri='https://github.com/CerditoAgridulce/Fibbonaci-s-spiral'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,right,down,left,down,right,down,right,right,down,left,left,down,right,right,right,up,right,down,down,left,down,left,left,down,right,down,down,right,right,right,up,right,up,right,down,down,left,left,down,down,right,right,right,up,right,up,left,down,down,right,down,right,up,right,down,right,up,up,left,down,right,up,left,down,right,up,up,left,left,down,right,down,right,up,up,left,left,down,right,down,right,up,left,up,left,down,right,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,up,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dd8daZPlG5O_vdIPuo6_-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_5.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, down, right, right, right, down, down, right, down, down, right, right, right, right, down, down, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,right,down,down,right,down,down,right,right,right,right,down,down,left,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eN8dadvRDIfYxs0PzZjGyQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_5.json`

**Score:** 14.29%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='et8dadrwMKq-vdIPlaK54Ak' usage_metadata=GenerateContentResponseUsageMetadata(
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
) total_tokens=158 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4992 traffic_type=None
```

### `maze_occupancy_6x6_adj_5.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e98daeb4JbjZvdIP6qu5mQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=1272,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1272
    ),
  ],
  total_token_count=1325
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=1272 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1272
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1325 traffic_type=None
```

### `maze_occupancy_6x6_ascii_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, down, down, right, right, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, left, left, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,left,left,left,left,down,down,right,right,down,down,right,right,right,right,down,down,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,down,right,right,down,down,right,right,right,right,down,down,left,left,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ft8dabO0A-rVvdIP957EwAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_tokenized_5.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gd8dad7TLKHXxN8Ph5ic0Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=2155,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2155
    ),
  ],
  total_token_count=2155
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=2155 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2155
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2155 traffic_type=None
```

