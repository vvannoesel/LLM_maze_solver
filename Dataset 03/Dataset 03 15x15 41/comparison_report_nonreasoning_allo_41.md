# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_41.jpg` | **1.41%** | `input: 436 , ouput: 650` | `right, down, down, right, down, right, right, down, right, down, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right` |
| `maze_line_15x15_41.json` | **0.70%** | `input: 9807 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_41.json` | **0.70%** | `input: 13485 , ouput: 57` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_41.txt` | **0.70%** | `input: 3677 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_41.txt` | **0.70%** | `input: 3282 , ouput: 117` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_15x15_41.jpg` | **0.35%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right` |
| `maze_occupancy_15x15_41.json` | **1.06%** | `input: 4246 , ouput: 650` | `right, right, down, right, right, down, down, right, down, down, down, right, down, down, right, down, down, down, down, right, right, right, down, down, down, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_41.json` | **nan%** | `input: 27623 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_41.txt` | **1.06%** | `input: 7727 , ouput: 113` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_ascii_41.txt` | **0.00%** | `input: 518 , ouput: 650` | `down, down, down, right, right, down, down, right, right, down, down, down, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_41.txt` | **1.41%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_41.jpg`

**Score:** 1.41%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, left, down, down, down, down, left, up, left, down, down, left, down, left, down, right, right, right, down, left, left, down, right, right, down, right, down, down, right, right, right, up, up, right, up, right, right, right, right, right, up, left, left, up, left, left, up, up, right, down, right, up, up, left, left, left, down, left, down, down, down, left, down, left, up, left, up, up, left, up, right, right, right, up, left, up, right, up, up, up, up, right, up, right, down, down, down, left, down, right, down, right, right, up, left, up, right, right, right, right, right, down, left, left, left, down, right, right, down, left, down, down, right, right, down, down, down, down, down, left, up, left, left, down, left, up, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, down, right, right, down, right, down, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, down, right, right, down, right, down, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, down, right, down, right, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MamUaYPfNv3onsEP3cCnyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1086
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1086 traffic_type=None
```

### `maze_line_15x15_41.json`

**Score:** 0.70%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, left, down, down, down, down, left, up, left, down, down, left, down, left, down, right, right, right, down, left, left, down, right, right, down, right, down, down, right, right, right, up, up, right, up, right, right, right, right, right, up, left, left, up, left, left, up, up, right, down, right, up, up, left, left, left, down, left, down, down, down, left, down, left, up, left, up, up, left, up, right, right, right, up, left, up, right, up, up, up, up, right, up, right, down, down, down, left, down, right, down, right, right, up, left, up, right, right, right, right, right, down, left, left, left, down, right, right, down, left, down, down, right, right, down, down, down, down, down, left, up, left, left, down, left, up, left, down, down, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MqmUafOVFvWinsEPtZuzkQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=9864
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9864 traffic_type=None
```

### `maze_line_15x15_adj_41.json`

**Score:** 0.70%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, left, down, down, down, down, left, up, left, down, down, left, down, left, down, right, right, right, down, left, left, down, right, right, down, right, down, down, right, right, right, up, up, right, up, right, right, right, right, right, up, left, left, up, left, left, up, up, right, down, right, up, up, left, left, left, down, left, down, down, down, left, down, left, up, left, up, up, left, up, right, right, right, up, left, up, right, up, up, up, up, right, up, right, down, down, down, left, down, right, down, right, right, up, left, up, right, right, right, right, right, down, left, left, left, down, right, right, down, left, down, down, right, right, down, down, down, down, down, left, up, left, left, down, left, up, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M6mUabiSDaOrnsEP8_bgmQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=13485,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13485
    ),
  ],
  total_token_count=13542
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=13485 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13485
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13542 traffic_type=None
```

### `maze_line_15x15_adj_41.txt`

**Score:** 0.70%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, left, down, down, down, down, left, up, left, down, down, left, down, left, down, right, right, right, down, left, left, down, right, right, down, right, down, down, right, right, right, up, up, right, up, right, right, right, right, right, up, left, left, up, left, left, up, up, right, down, right, up, up, left, left, left, down, left, down, down, down, left, down, left, up, left, up, up, left, up, right, right, right, up, left, up, right, up, up, up, up, right, up, right, down, down, down, left, down, right, down, right, right, up, left, up, right, right, right, right, right, down, left, left, left, down, right, right, down, left, down, down, right, right, down, down, down, down, down, left, up, left, left, down, left, up, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NamUabGCC9GqnsEPwL-awAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_41.txt`

**Score:** 0.70%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, left, down, down, down, down, left, up, left, down, down, left, down, left, down, right, right, right, down, left, left, down, right, right, down, right, down, down, right, right, right, up, up, right, up, right, right, right, right, right, up, left, left, up, left, left, up, up, right, down, right, up, up, left, left, left, down, left, down, down, down, left, down, left, up, left, up, up, left, up, right, right, right, up, left, up, right, up, up, up, up, right, up, right, down, down, down, left, down, right, down, right, right, up, left, up, right, right, right, right, right, down, left, left, left, down, right, right, down, left, down, down, right, right, down, down, down, down, down, left, up, left, left, down, left, up, left, down, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NqmUac_OCubgnsEP6p2VqQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=117,
  prompt_token_count=3282,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3282
    ),
  ],
  total_token_count=3399
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=117 candidates_tokens_details=None prompt_token_count=3282 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3282
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3399 traffic_type=None
```

### `maze_occupancy_15x15_41.jpg`

**Score:** 0.35%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, down, down, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, up, up, left, left, left, left, up, up, up, up, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OamUacKKFsTV7M8PzpbtcQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_41.json`

**Score:** 1.06%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, down, down, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, up, up, left, left, left, left, up, up, up, up, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, down, down, right, down, down, down, right, down, down, right, down, down, down, down, right, right, right, down, down, down, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,down,right,down,down,down,right,down,down,right,down,down,down,down,right,right,right,down,down,down,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OqmUacDgJsf5nsEPi7DUqAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_41.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, down, down, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, up, up, left, left, left, left, up, up, up, up, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='PamUaeL2A73ukdUPl-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=27623,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27623
    ),
  ],
  total_token_count=27623
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=27623 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27623
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27623 traffic_type=None
```

### `maze_occupancy_15x15_adj_41.txt`

**Score:** 1.06%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, down, down, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, up, up, left, left, left, left, up, up, up, up, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='PamUabfjN-bgnsEP3-2VSQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7727,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7727
    ),
  ],
  total_token_count=7840
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7727 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7727
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7840 traffic_type=None
```

### `maze_occupancy_15x15_ascii_41.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, down, down, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, up, up, left, left, left, left, up, up, up, up, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, right, right, down, down, right, right, down, down, down, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,down,down,right,right,down,down,down,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='P6mUaf3tNL3ukdUPl-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=518,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=518
    ),
  ],
  total_token_count=1168
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=518 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=518
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1168 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_41.txt`

**Score:** 1.41%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, down, down, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, up, up, left, left, left, left, up, up, up, up, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QqmUadXkBITv7M8P2pmO8AE' usage_metadata=GenerateContentResponseUsageMetadata(
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

