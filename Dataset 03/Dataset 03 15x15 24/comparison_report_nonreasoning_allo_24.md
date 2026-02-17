# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_24.jpg` | **0.00%** | `input: 436 , ouput: 103` | `right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, left, down, right, down, right, up, right, up, right, up, left, up, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down` |
| `maze_line_15x15_24.json` | **1.67%** | `input: 9807 , ouput: 85` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_24.json` | **1.67%** | `input: 13485 , ouput: 85` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_24.txt` | **1.67%** | `input: 3677 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left` |
| `maze_line_15x15_tokenized_24.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_24.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, down, left, down, right, right, up, right, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right` |
| `maze_occupancy_15x15_24.json` | **1.67%** | `input: 4246 , ouput: 173` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_15x15_adj_24.json` | **0.00%** | `input: 27634 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_24.txt` | **1.67%** | `input: 7730 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_24.txt` | **0.42%** | `input: 549 , ouput: 650` | `down, right, right, right, right, right, down, right, right, right, right, down, down, down, right, right, right, down, right, right, right, right, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_24.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_24.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, down, left, down, right, right, up, up, right, right, down, right, right, up, up, left, up, right, right, right, right, down, left, left, down, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, left, up, up, left, down, down, left, left, left, down, left, down, right, down, left, left, down, right, right, down, right, right, up, up, up, left, up, right, right, down, right, up, right, down, right, up, right, right, up, left, up, up, up, up, up, right, up, left, up, left, down, left, up, up, right, right, right, right, down, down, down, down, left, down, right, down, left, down, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, left, down, right, down, right, up, right, up, right, up, left, up, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, left, down, right, down, right, up, right, up, right, up, left, up, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='u6aUaer2H6OrnsEP8_bgmQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=103,
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
  total_token_count=539
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=103 candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=539 traffic_type=None
```

### `maze_line_15x15_24.json`

**Score:** 1.67%

**Ground Truth Solution:**
```
down, down, right, down, left, down, right, right, up, up, right, right, down, right, right, up, up, left, up, right, right, right, right, down, left, left, down, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, left, up, up, left, down, down, left, left, left, down, left, down, right, down, left, left, down, right, right, down, right, right, up, up, up, left, up, right, right, down, right, up, right, down, right, up, right, right, up, left, up, up, up, up, up, right, up, left, up, left, down, left, up, up, right, right, right, right, down, down, down, down, left, down, right, down, left, down, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vKaUaY3kEuiXkdUPtIrQkAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=9892
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9892 traffic_type=None
```

### `maze_line_15x15_adj_24.json`

**Score:** 1.67%

**Ground Truth Solution:**
```
down, down, right, down, left, down, right, right, up, up, right, right, down, right, right, up, up, left, up, right, right, right, right, down, left, left, down, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, left, up, up, left, down, down, left, left, left, down, left, down, right, down, left, left, down, right, right, down, right, right, up, up, up, left, up, right, right, down, right, up, right, down, right, up, right, right, up, left, up, up, up, up, up, right, up, left, up, left, down, left, up, up, right, right, right, right, down, down, down, down, left, down, right, down, left, down, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vaaUaeeiDKGF7M8PzMbuaA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=13485,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13485
    ),
  ],
  total_token_count=13570
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=13485 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13485
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13570 traffic_type=None
```

### `maze_line_15x15_adj_24.txt`

**Score:** 1.67%

**Ground Truth Solution:**
```
down, down, right, down, left, down, right, right, up, up, right, right, down, right, right, up, up, left, up, right, right, right, right, down, left, left, down, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, left, up, up, left, down, down, left, left, left, down, left, down, right, down, left, left, down, right, right, down, right, right, up, up, up, left, up, right, right, down, right, up, right, down, right, up, right, right, up, left, up, up, up, up, up, right, up, left, up, left, down, left, up, up, right, right, right, right, down, down, down, down, left, down, right, down, left, down, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v6aUafi5DNfu7M8Pk_6wkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_24.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, down, left, down, right, right, up, up, right, right, down, right, right, up, up, left, up, right, right, right, right, down, left, left, down, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, left, up, up, left, down, down, left, left, left, down, left, down, right, down, left, left, down, right, right, down, right, right, up, up, up, left, up, right, right, down, right, up, right, down, right, up, right, right, up, left, up, up, up, up, up, right, up, left, up, left, down, left, up, up, right, right, right, right, down, down, down, down, left, down, right, down, left, down, right, down, down, down, down, left, down, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wqaUafH-D4b1kdUP6IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_24.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, down, left, down, right, right, up, right, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right, down, left, down, right, right, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,down,left,down,right,right,up,right,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,down,left,down,right,right,down,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xKaUaYmDBuOXkdUPwKDLyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_24.json`

**Score:** 1.67%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xaaUacPjCfaHnsEPm6HKoQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=173,
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4419
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=173 candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4419 traffic_type=None
```

### `maze_occupancy_15x15_adj_24.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='x6aUafXZFp6jnsEP0cGigAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27634,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27634
    ),
  ],
  total_token_count=28284
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27634 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27634
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28284 traffic_type=None
```

### `maze_occupancy_15x15_adj_24.txt`

**Score:** 1.67%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='x6aUaaC9NqzzkdUPnrP0qAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7730
    ),
  ],
  total_token_count=7843
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7843 traffic_type=None
```

### `maze_occupancy_15x15_ascii_24.txt`

**Score:** 0.42%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, right, right, right, down, right, right, right, right, down, down, down, right, right, right, down, right, right, right, right, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,right,down,right,right,right,right,down,down,down,right,right,right,down,right,right,right,right,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yaaUabuDFpT8nsEP5Y-B0A8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=549,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=549
    ),
  ],
  total_token_count=1199
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=549 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=549
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1199 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='y6aUacyBFvCMkdUPn6WNwAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

