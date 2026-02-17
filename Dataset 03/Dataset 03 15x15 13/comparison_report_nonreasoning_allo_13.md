# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_13.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_13.json` | **0.78%** | `input: 9807 , ouput: 650` | `down, down, right, down, down, right, right, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down` |
| `maze_line_15x15_adj_13.json` | **0.78%** | `input: 13487 , ouput: 85` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_13.txt` | **0.78%** | `input: 3679 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_line_15x15_tokenized_13.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_13.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right` |
| `maze_occupancy_15x15_13.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_13.json` | **0.39%** | `input: 27635 , ouput: 650` | `down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down` |
| `maze_occupancy_15x15_adj_13.txt` | **0.78%** | `input: 7731 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_13.txt` | **nan%** | `input: 531 , ouput: 0` | `` |
| `maze_occupancy_15x15_tokenized_13.txt` | **0.00%** | `input: 12134 , ouput: 121` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_13.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, right, down, right, down, down, down, right, down, left, left, left, down, down, down, down, right, right, up, right, up, up, right, right, up, up, left, up, right, up, right, down, down, right, down, right, right, right, up, right, down, down, right, up, up, up, left, left, left, down, left, up, left, up, right, up, up, up, right, right, down, left, down, right, down, right, up, up, right, down, down, right, right, down, left, down, down, down, right, down, left, left, left, left, left, down, left, left, down, left, down, left, down, left, up, up, left, down, down, down, right, down, right, right, right, right, up, left, up, right, up, right, right, down, right, right, up, right, right, down, left, down, left, left, down, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Up-UaY_hBK3hnsEPxYDs0QE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_13.json`

**Score:** 0.78%

**Ground Truth Solution:**
```
down, right, down, right, down, down, down, right, down, left, left, left, down, down, down, down, right, right, up, right, up, up, right, right, up, up, left, up, right, up, right, down, down, right, down, right, right, right, up, right, down, down, right, up, up, up, left, left, left, down, left, up, left, up, right, up, up, up, right, right, down, left, down, right, down, right, up, up, right, down, down, right, right, down, left, down, down, down, right, down, left, left, left, left, left, down, left, left, down, left, down, left, down, left, up, up, left, down, down, down, right, down, right, right, right, right, up, left, up, right, up, right, right, down, right, right, up, right, right, down, left, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
down, down, right, down, down, right, right, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,down,down,right,right,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VJ-Uade3Edfu7M8Pk_6wkAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=10457
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=10457 traffic_type=None
```

### `maze_line_15x15_adj_13.json`

**Score:** 0.78%

**Ground Truth Solution:**
```
down, right, down, right, down, down, down, right, down, left, left, left, down, down, down, down, right, right, up, right, up, up, right, right, up, up, left, up, right, up, right, down, down, right, down, right, right, right, up, right, down, down, right, up, up, up, left, left, left, down, left, up, left, up, right, up, up, up, right, right, down, left, down, right, down, right, up, up, right, down, down, right, right, down, left, down, down, down, right, down, left, left, left, left, left, down, left, left, down, left, down, left, down, left, up, up, left, down, down, down, right, down, right, right, right, right, up, left, up, right, up, right, right, down, right, right, up, right, right, down, left, down, left, left, down, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VZ-Uaf2JEqqEkdUPzIWYoAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=13487,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13487
    ),
  ],
  total_token_count=13572
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=13487 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13487
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13572 traffic_type=None
```

### `maze_line_15x15_adj_13.txt`

**Score:** 0.78%

**Ground Truth Solution:**
```
down, right, down, right, down, down, down, right, down, left, left, left, down, down, down, down, right, right, up, right, up, up, right, right, up, up, left, up, right, up, right, down, down, right, down, right, right, right, up, right, down, down, right, up, up, up, left, left, left, down, left, up, left, up, right, up, up, up, right, right, down, left, down, right, down, right, up, up, right, down, down, right, right, down, left, down, down, down, right, down, left, left, left, left, left, down, left, left, down, left, down, left, down, left, up, up, left, down, down, down, right, down, right, right, right, right, up, left, up, right, up, right, right, down, right, right, up, right, right, down, left, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Vp-Uae-iJrOlnsEPjtai8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3679,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3679
    ),
  ],
  total_token_count=4329
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3679 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3679
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4329 traffic_type=None
```

### `maze_line_15x15_tokenized_13.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, right, down, down, down, right, down, left, left, left, down, down, down, down, right, right, up, right, up, up, right, right, up, up, left, up, right, up, right, down, down, right, down, right, right, right, up, right, down, down, right, up, up, up, left, left, left, down, left, up, left, up, right, up, up, up, right, right, down, left, down, right, down, right, up, up, right, down, down, right, right, down, left, down, down, down, right, down, left, left, left, left, left, down, left, left, down, left, down, left, down, left, up, up, left, down, down, down, right, down, right, right, right, right, up, left, up, right, up, right, right, down, right, right, up, right, right, down, left, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WJ-UafabJMSzkdUP4ZaoqQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3282,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3282
    ),
  ],
  total_token_count=3932
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3282 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3282
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3932 traffic_type=None
```

### `maze_occupancy_15x15_13.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, left, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,left,down,right,down,left,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Wp-UaZ_zI9yWkdUPpoLOyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_13.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XJ-Uaa6iKtjpnsEPmcvxyAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_13.json`

**Score:** 0.39%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='X5-UaeP7E8SzkdUP4ZaoqQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27635,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27635
    ),
  ],
  total_token_count=28285
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27635 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27635
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28285 traffic_type=None
```

### `maze_occupancy_15x15_adj_13.txt`

**Score:** 0.78%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YZ-UacqtH43znsEPmfLf8QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7731,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7731
    ),
  ],
  total_token_count=8381
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7731 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7731
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8381 traffic_type=None
```

### `maze_occupancy_15x15_ascii_13.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZJ-UafG7BceUnsEPgvzb-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=531,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=531
    ),
  ],
  total_token_count=531
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=531 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=531
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=531 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_13.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, up, up, left, left, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZZ-UaehswaSewQ_MptiYAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=121,
  prompt_token_count=12134,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=12134
    ),
  ],
  total_token_count=12255
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=121 candidates_tokens_details=None prompt_token_count=12134 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=12134
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=12255 traffic_type=None
```

