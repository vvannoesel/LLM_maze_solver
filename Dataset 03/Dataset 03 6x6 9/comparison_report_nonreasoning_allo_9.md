# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_9.jpg` | **0.00%** | `input: 427 , ouput: 27` | `right, down, right, down, right, down, right, down, left, down, right, right, down, right` |
| `maze_line_6x6_9.json` | **18.75%** | `input: 1802 , ouput: 21` | `down, right, down, right, down, right, down, right, right, down, right` |
| `maze_line_6x6_adj_9.json` | **12.50%** | `input: 2251 , ouput: 31` | `down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down` |
| `maze_line_6x6_adj_9.txt` | **0.00%** | `input: 722 , ouput: 29` | `right, right, right, down, down, right, right, down, down, right, down, down, down, right, right` |
| `maze_line_6x6_tokenized_9.txt` | **0.00%** | `input: 666 , ouput: 650` | `right, down, right, down, right, down, left, down, right, right, down, left, left, down, right, right, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left` |
| `maze_occupancy_6x6_9.jpg` | **3.12%** | `input: 424 , ouput: 41` | `down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down` |
| `maze_occupancy_6x6_9.json` | **0.00%** | `input: 981 , ouput: 650` | `right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, right, right, down, down, right, right, down, right, right, down, down, down, right, right, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right` |
| `maze_occupancy_6x6_adj_9.json` | **6.25%** | `input: 4338 , ouput: 650` | `down, down, down, right, right, down, down, right, right, right, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_9.txt` | **18.75%** | `input: 1269 , ouput: 650` | `down, down, right, right, down, down, right, right, right, down, down, down, right, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right` |
| `maze_occupancy_6x6_ascii_9.txt` | **0.00%** | `input: 245 , ouput: 650` | `right, right, down, down, right, right, right, down, down, right, down, right, right, down, down, right, right, down, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right` |
| `maze_occupancy_6x6_tokenized_9.txt` | **0.00%** | `input: 2155 , ouput: 650` | `right, down, down, right, right, down, right, right, down, right, right, right, down, right, right, right, down, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_9.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, right, up, right, right, down, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1t8dacyqBPClvdIPvJaP0Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
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
  total_token_count=454
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=454 traffic_type=None
```

### `maze_line_6x6_9.json`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, right, down, down, right, up, right, right, down, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1t8dafH3NP_axs0P3PW82Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_9.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, right, down, down, right, up, right, right, down, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2N8dacVH9ta90g-11quhCQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2282
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2282 traffic_type=None
```

### `maze_line_6x6_adj_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, right, up, right, right, down, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, down, down, right, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,right,down,down,right,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2d8dafqvA-DTvdIPsdP1mAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=751
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=751 traffic_type=None
```

### `maze_line_6x6_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, right, up, right, right, down, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, down, left, left, down, right, right, up, right, down, down, left, left, down, right, right, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left, left, up, up, right, down, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,down,left,left,down,right,right,up,right,down,down,left,left,down,right,right,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,left,up,up,right,down,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='298dacyCIorkvdIPipOBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_9.jpg`

**Score:** 3.12%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3N8daamBGpXVxs0P7sqPqQ4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
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
  total_token_count=465
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=465 traffic_type=None
```

### `maze_occupancy_6x6_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, right, right, down, down, right, right, down, right, right, down, down, down, right, right, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,right,right,down,down,right,right,down,right,right,down,down,down,right,right,right,right,right,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3t8daaj0M4fYvdIPoMnJwQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_9.json`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, down, down, right, right, right, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,down,down,right,right,right,down,down,down,down,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4d8dadWhOYGOvdIP28nzuQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4338,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4338
    ),
  ],
  total_token_count=4988
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4338 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4338
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4988 traffic_type=None
```

### `maze_occupancy_6x6_adj_9.txt`

**Score:** 18.75%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, right, down, down, down, right, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,right,down,down,down,right,down,down,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5d8daa2-FJ_VvdIPmYCYwQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1269,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1269
    ),
  ],
  total_token_count=1919
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1269 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1269
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1919 traffic_type=None
```

### `maze_occupancy_6x6_ascii_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, right, down, right, right, down, down, right, right, down, right, right, right, right, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,right,down,right,right,down,down,right,right,down,right,right,right,right,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='598dadKgIuPUxs0Pk8v7uA0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, down, right, right, down, right, right, right, down, right, right, right, down, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, right, down, right, right, down, right, right, right, down, right, right, right, down, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6t8dacKPL9WNvdIPo9-nuA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

