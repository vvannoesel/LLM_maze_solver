# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_17.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_17.json` | **2.22%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_17.json` | **3.33%** | `input: 13483 , ouput: 650` | `down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down` |
| `maze_line_15x15_adj_17.txt` | **0.00%** | `input: 3675 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_17.txt` | **0.00%** | `input: 3283 , ouput: 650` | `right, right, down, down, right, down, right, right, down, down, right, down, right, right, right, down, right, down, down, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right` |
| `maze_occupancy_15x15_17.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down` |
| `maze_occupancy_15x15_17.json` | **2.22%** | `input: 4246 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_17.json` | **1.11%** | `input: 27626 , ouput: 650` | `down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_17.txt` | **2.22%** | `input: 7724 , ouput: 121` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_17.txt` | **0.00%** | `input: 556 , ouput: 650` | `right, down, down, right, right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_17.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_17.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, right, down, left, down, down, down, right, down, left, down, right, down, down, right, right, up, left, up, right, up, up, left, up, left, up, right, up, right, right, down, left, down, right, down, down, down, down, right, up, right, up, up, up, up, up, up, left, up, right, right, up, right, right, down, down, left, left, down, down, right, down, right, down, left, left, down, down, right, up, right, down, right, up, right, up, right, right, right, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NKSUad-rKqXu7M8P4P7CkQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_17.json`

**Score:** 2.22%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, right, down, left, down, down, down, right, down, left, down, right, down, down, right, right, up, left, up, right, up, up, left, up, left, up, right, up, right, right, down, left, down, right, down, down, down, down, right, up, right, up, up, up, up, up, up, left, up, right, right, up, right, right, down, down, left, left, down, down, right, down, right, down, left, left, down, down, right, up, right, down, right, up, right, up, right, right, right, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NaSUaYGEGdy8nsEPjZySgAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=9862
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9862 traffic_type=None
```

### `maze_line_15x15_adj_17.json`

**Score:** 3.33%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, right, down, left, down, down, down, right, down, left, down, right, down, down, right, right, up, left, up, right, up, up, left, up, left, up, right, up, right, right, down, left, down, right, down, down, down, down, right, up, right, up, up, up, up, up, up, left, up, right, right, up, right, right, down, down, left, left, down, down, right, down, right, down, left, left, down, down, right, up, right, down, right, up, right, up, right, right, right, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='N6SUae2VLbGqnsEPso7fsQU' usage_metadata=GenerateContentResponseUsageMetadata(
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
) total_tokens=165 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13483 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13483
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14133 traffic_type=None
```

### `maze_line_15x15_adj_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, right, down, left, down, down, down, right, down, left, down, right, down, down, right, right, up, left, up, right, up, up, left, up, left, up, right, up, right, right, down, left, down, right, down, down, down, down, right, up, right, up, up, up, up, up, up, left, up, right, right, up, right, right, down, down, left, left, down, down, right, down, right, down, left, left, down, down, right, up, right, down, right, up, right, up, right, right, right, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OKSUaZmLG9rOnsEPw-rG0AM' usage_metadata=GenerateContentResponseUsageMetadata(
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
) total_tokens=198 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=3675 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3675
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3732 traffic_type=None
```

### `maze_line_15x15_tokenized_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, right, down, left, down, down, down, right, down, left, down, right, down, down, right, right, up, left, up, right, up, up, left, up, left, up, right, up, right, right, down, left, down, right, down, down, down, down, right, up, right, up, up, up, up, up, up, left, up, right, right, up, right, right, down, down, left, left, down, down, right, down, right, down, left, left, down, down, right, up, right, down, right, up, right, up, right, right, right, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, right, right, down, down, right, down, right, right, right, down, right, down, down, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,right,right,down,down,right,down,right,right,right,down,right,down,down,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OqSUadDfK-LW7M8PiN7ImA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3283,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3283
    ),
  ],
  total_token_count=3933
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3283 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3283
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3933 traffic_type=None
```


### `maze_occupancy_15x15_17.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eqWUabPfD-bgnsEP6p2VqQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_17.json`

**Score:** 2.22%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fKWUabWPEO6hnsEPsYODsAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4896
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4896 traffic_type=None
```

### `maze_occupancy_15x15_adj_17.json`

**Score:** 1.11%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='faWUaZSNM6iSkdUPusP7uA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27626,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27626
    ),
  ],
  total_token_count=28276
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27626 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27626
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28276 traffic_type=None
```

### `maze_occupancy_15x15_adj_17.txt`

**Score:** 2.22%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fqWUaaGXMtuXkdUPsdSSoAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=121,
  prompt_token_count=7724,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7724
    ),
  ],
  total_token_count=7845
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=121 candidates_tokens_details=None prompt_token_count=7724 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7724
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7845 traffic_type=None
```

### `maze_occupancy_15x15_ascii_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gKWUacnoNLK7nsEPp-bmmQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=556,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=556
    ),
  ],
  total_token_count=1206
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=556 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=556
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1206 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_17.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down
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
        text='right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='g6WUaZZXv7GewQ-4yqKhAg' usage_metadata=GenerateContentResponseUsageMetadata(
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

