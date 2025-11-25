# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_2.jpg` | **0.00%** | `input: 436 , ouput: 113` | `right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, left, up, left, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right` |
| `maze_line_15x15_2.json` | **4.41%** | `input: 9807 , ouput: 53` | `down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_2.json` | **0.00%** | `input: 13485 , ouput: 99` | `right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_2.txt` | **0.00%** | `input: 3677 , ouput: 650` | `right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down` |
| `maze_line_15x15_tokenized_2.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_2.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right` |
| `maze_occupancy_15x15_2.json` | **0.00%** | `input: 4246 , ouput: 57` | `right, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_2.json` | **1.47%** | `input: 27627 , ouput: 650` | `down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_2.txt` | **nan%** | `input: 7725 , ouput: 0` | `` |
| `maze_occupancy_15x15_ascii_2.txt` | **0.00%** | `input: 540 , ouput: 650` | `right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left` |
| `maze_occupancy_15x15_tokenized_2.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, down, down, right, right, right, right, right, right, down, left, left, down, right, right, down, left, down, down, left, up, up, left, up, up, left, down, left, up, left, left, left, down, down, right, right, right, down, left, down, right, right, up, right, down, down, right, right, right, right, down, right, down, down, right, down, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, left, up, left, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,down,left,down,left,up,left,down,right,down,right,down,right,down,right,up,right,up,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6_wlacfdNZfYxs0P243yYA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=436,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=178
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=549
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=436 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=549 traffic_type=None
```

### `maze_line_15x15_2.json`

**Score:** 4.41%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, down, down, right, right, right, right, right, right, down, left, left, down, right, right, down, left, down, down, left, up, up, left, up, up, left, down, left, up, left, left, left, down, down, right, right, right, down, left, down, right, right, up, right, down, down, right, right, right, right, down, right, down, down, right, down, right, down, right, up, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7fwlabuRFeu_vdIP9tzPYA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=9860
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9860 traffic_type=None
```

### `maze_line_15x15_adj_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, down, down, right, right, right, right, right, right, down, left, left, down, right, right, down, left, down, down, left, up, up, left, up, up, left, down, left, up, left, left, left, down, down, right, right, right, down, left, down, right, right, up, right, down, down, right, right, right, right, down, right, down, down, right, down, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7vwlacqGNYPkxN8PieetaQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=99,
  prompt_token_count=13485,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13485
    ),
  ],
  total_token_count=13584
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=99 candidates_tokens_details=None prompt_token_count=13485 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13485
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13584 traffic_type=None
```

### `maze_line_15x15_adj_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, down, down, right, right, right, right, right, right, down, left, left, down, right, right, down, left, down, down, left, up, up, left, up, up, left, down, left, up, left, left, left, down, down, right, right, right, down, left, down, right, right, up, right, down, down, right, right, right, right, down, right, down, down, right, down, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8fwlaY_YFfq5vdIPxL60kAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3677,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3677
    ),
  ],
  total_token_count=4327
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3677 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3677
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4327 traffic_type=None
```

### `maze_line_15x15_tokenized_2.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, right, up, up, right, down, down, right, right, right, right, right, right, down, left, left, down, right, right, down, left, down, down, left, up, up, left, up, up, left, down, left, up, left, left, left, down, down, right, right, right, down, left, down, right, right, up, right, down, down, right, right, right, right, down, right, down, down, right, down, right, down, right, up, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9fwlaZGrJJ-AvdIP7L-c6Q4' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=3282,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3282
    ),
  ],
  total_token_count=3282
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=3282 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3282
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3282 traffic_type=None
```

### `maze_occupancy_15x15_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, left, left, up, up, up, up, left, left, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-fwlaYqeAdi7xN8PlP70yAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, left, left, up, up, up, up, left, left, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-vwlabLoA4W7xN8P8JTdiQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4303
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4303 traffic_type=None
```

### `maze_occupancy_15x15_adj_2.json`

**Score:** 1.47%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, left, left, up, up, up, up, left, left, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_PwlaZePNenbxs0PudTh-QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27627,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27627
    ),
  ],
  total_token_count=28277
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27627 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27627
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28277 traffic_type=None
```

### `maze_occupancy_15x15_adj_2.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, left, left, up, up, up, up, left, left, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='__wlaY-1OqH6xs0Pi9na8Q4' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=7725,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7725
    ),
  ],
  total_token_count=7725
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=7725 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7725
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7725 traffic_type=None
```

### `maze_occupancy_15x15_ascii_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, left, left, up, up, up, up, left, left, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Av0ladLgL_7XxN8PqJbHmAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=540,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=540
    ),
  ],
  total_token_count=1190
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=540 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=540
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1190 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, left, left, up, up, up, up, left, left, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Bf0ladudFNqzvdIP6ufKoQ4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=12134,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=12134
    ),
  ],
  total_token_count=12784
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=12134 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=12134
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=12784 traffic_type=None
```

