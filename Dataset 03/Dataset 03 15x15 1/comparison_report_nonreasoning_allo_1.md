# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_1.jpg` | **nan%** | `input: 429 , ouput: 0` | `` |
| `maze_line_15x15_1.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_1.json` | **1.54%** | `input: 9800 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_1.json` | **0.00%** | `input: 13483 , ouput: 650` | `right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right` |
| `maze_line_15x15_adj_1.txt` | **0.00%** | `input: 3675 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_1.txt` | **0.00%** | `input: 3275 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up` |
| `maze_occupancy_15x15_1.jpg` | **nan%** | `input: 424 , ouput: 0` | `` |
| `maze_occupancy_15x15_1.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, down, down, right, down, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, right, down, right, right, down, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down` |
| `maze_occupancy_15x15_1.json` | **0.00%** | `input: 4239 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, down, right, right, down, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, down, right, right, down, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down` |
| `maze_occupancy_15x15_adj_1.json` | **0.77%** | `input: 27628 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_1.txt` | **0.00%** | `input: 7724 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_1.txt` | **0.00%** | `input: 541 , ouput: 650` | `right, right, right, right, right, right, right, right, down, right, down, down, down, left, down, down, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_1.txt` | **0.00%** | `input: 12128 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_15x15_1.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, down, right, right, up, left, up, right, up, right, down, down, right, up, up, right, down, right, down, down, down, right, up, up, right, right, down, left, down, down, down, down, down, left, down, left, up, left, down, down, left, left, down, left, up, left, up, up, up, left, up, right, right, down, down, right, right, up, left, up, right, right, up, up, up, left, down, left, left, down, left, left, up, left, left, down, down, right, down, down, down, down, down, left, down, right, down, right, down, right, up, up, right, right, right, down, left, down, right, right, up, up, up, right, right, right, up, up, right, up, up, right, right, down, left, down, right, down, right, down, down, down, left, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BfAVad3cC6PXvdIPireC4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=429,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=171
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=429
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=429 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=429 traffic_type=None
```
### `maze_line_15x15_1.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, down, right, right, up, left, up, right, up, right, down, down, right, up, up, right, down, right, down, down, down, right, up, up, right, right, down, left, down, down, down, down, down, left, down, left, up, left, down, down, left, left, down, left, up, left, up, up, up, left, up, right, right, down, down, right, right, up, left, up, right, right, up, up, up, left, down, left, left, down, left, left, up, left, left, down, down, right, down, down, down, down, down, left, down, right, down, right, down, right, up, up, right, right, right, down, left, down, right, right, up, up, up, right, right, right, up, up, right, up, up, right, right, down, left, down, right, down, right, down, down, down, left, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BM4maYuNCYXlxN8P2afLYA' usage_metadata=GenerateContentResponseUsageMetadata(
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
  total_token_count=436
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=436 traffic_type=None
```

### `maze_line_15x15_1.json`

**Score:** 1.54%

**Ground Truth Solution:**
```
down, down, right, right, down, right, right, up, left, up, right, up, right, down, down, right, up, up, right, down, right, down, down, down, right, up, up, right, right, down, left, down, down, down, down, down, left, down, left, up, left, down, down, left, left, down, left, up, left, up, up, up, left, up, right, right, down, down, right, right, up, left, up, right, right, up, up, up, left, down, left, left, down, left, left, up, left, left, down, down, right, down, down, down, down, down, left, down, right, down, right, down, right, up, up, right, right, right, down, left, down, right, right, up, up, up, right, right, right, up, up, right, up, up, right, right, down, left, down, right, down, right, down, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BvAVaYKeFNvTxN8P5fytuQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=9800,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9800
    ),
  ],
  total_token_count=9855
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=9800 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9800
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9855 traffic_type=None
```

### `maze_line_15x15_adj_1.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, right, right, up, left, up, right, up, right, down, down, right, up, up, right, down, right, down, down, down, right, up, up, right, right, down, left, down, down, down, down, down, left, down, left, up, left, down, down, left, left, down, left, up, left, up, up, up, left, up, right, right, down, down, right, right, up, left, up, right, right, up, up, up, left, down, left, left, down, left, left, up, left, left, down, down, right, down, down, down, down, down, left, down, right, down, right, down, right, up, up, right, right, right, down, left, down, right, right, up, up, up, right, right, right, up, up, right, up, up, right, right, down, left, down, right, down, right, down, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CPAVaanEN77YvdIPitG6yQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=13483,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13483
    ),
  ],
  total_token_count=14133
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13483 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13483
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14133 traffic_type=None
```

### `maze_line_15x15_adj_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, right, right, up, left, up, right, up, right, down, down, right, up, up, right, down, right, down, down, down, right, up, up, right, right, down, left, down, down, down, down, down, left, down, left, up, left, down, down, left, left, down, left, up, left, up, up, up, left, up, right, right, down, down, right, right, up, left, up, right, right, up, up, up, left, down, left, left, down, left, left, up, left, left, down, down, right, down, down, down, down, down, left, down, right, down, right, down, right, up, up, right, right, right, down, left, down, right, right, up, up, up, right, right, right, up, up, right, up, up, right, right, down, left, down, right, down, right, down, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CfAVaf6-Mp3TvdIPktuioAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=3675,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3675
    ),
  ],
  total_token_count=3732
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=3675 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3675
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3732 traffic_type=None
```

### `maze_line_15x15_tokenized_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, right, right, up, left, up, right, up, right, down, down, right, up, up, right, down, right, down, down, down, right, up, up, right, right, down, left, down, down, down, down, down, left, down, left, up, left, down, down, left, left, down, left, up, left, up, up, up, left, up, right, right, down, down, right, right, up, left, up, right, right, up, up, up, left, down, left, left, down, left, left, up, left, left, down, down, right, down, down, down, down, down, left, down, right, down, right, down, right, up, up, right, right, right, down, left, down, right, right, up, up, up, right, right, right, up, up, right, up, up, right, right, down, left, down, right, down, right, down, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DPAVac-SBLeDxs0PydaXsA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3275,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3275
    ),
  ],
  total_token_count=3925
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3275 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3275
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3925 traffic_type=None
```

### `maze_occupancy_15x15_1.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EPAVafzlFaDZxN8PgOuXsA4' usage_metadata=GenerateContentResponseUsageMetadata(
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
  total_token_count=424
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=424 traffic_type=None
```
### `maze_occupancy_15x15_1.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, down, down, right, down, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, right, down, right, right, down, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,down,down,right,down,right,down,down,right,down,down,right,right,down,down,right,right,down,down,right,right,down,right,down,right,right,down,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B84maaPrH4CDvdIP_s7auQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_1.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, down, right, right, down, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, down, right, right, down, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,right,right,right,down,right,right,down,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,down,right,right,down,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EvAVaanrN__axs0P8-qZwA4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4239,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4239
    ),
  ],
  total_token_count=4889
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4239 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4239
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4889 traffic_type=None
```

### `maze_occupancy_15x15_adj_1.json`

**Score:** 0.77%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FfAVaYzmLuvzvdIPkYfx6Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27628,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27628
    ),
  ],
  total_token_count=28278
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27628 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27628
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28278 traffic_type=None
```

### `maze_occupancy_15x15_adj_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GPAVaey0Cv36vdIPxKqI2A4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7724,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7724
    ),
  ],
  total_token_count=8374
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7724 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7724
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8374 traffic_type=None
```

### `maze_occupancy_15x15_ascii_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, right, down, down, down, left, down, down, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,right,down,down,down,left,down,down,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GvAVaYHOO7GkvdIP-aDM8Qs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=541,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=541
    ),
  ],
  total_token_count=1191
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=541 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=541
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1191 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HvAVaY2-Ba7CvdIPwbH4oAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=12128,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=12128
    ),
  ],
  total_token_count=12778
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=12128 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=12128
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=12778 traffic_type=None
```

