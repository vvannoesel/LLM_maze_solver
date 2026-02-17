# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_35.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, left, down, right, down, right, down, left, down, right, right, down, right, up, right, up, left, down, right, down, right, down, right, up, right, up, right, up, left, up, right, down, right, down, right, down, right, down, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up` |
| `maze_line_15x15_35.json` | **3.66%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_35.json` | **3.66%** | `input: 13484 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_35.txt` | **3.66%** | `input: 3676 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_35.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_35.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_35.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, down, down, right, down, down, down, right, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, right, down, down, down, right, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_35.json` | **0.61%** | `input: 27628 , ouput: 650` | `down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right` |
| `maze_occupancy_15x15_adj_35.txt` | **3.66%** | `input: 7730 , ouput: 115` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_35.txt` | **nan%** | `input: 534 , ouput: 0` | `` |
| `maze_occupancy_15x15_tokenized_35.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_35.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, right, down, right, up, right, up, left, left, up, left, up, right, right, right, right, right, right, down, down, down, right, right, up, left, up, right, up, right, right, down, down, right, up, right, down, right, down, left, left, left, down, down, down, left, up, up, left, down, down, down, right, right, right, up, up, right, down, down, down, right, down, down, left, left, up, left, down, down, left, down, right, down, down, right, up, right, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, left, down, right, down, right, down, left, down, right, right, down, right, up, right, up, left, down, right, down, right, down, right, up, right, up, right, up, left, up, right, down, right, down, right, down, right, down, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,left,down,right,down,right,down,left,down,right,right,down,right,up,right,up,left,down,right,down,right,down,right,up,right,up,right,up,left,up,right,down,right,down,right,down,right,down,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gqiUabjsKqGF7M8PzMbuaA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_35.json`

**Score:** 3.66%

**Ground Truth Solution:**
```
down, down, down, right, right, down, right, up, right, up, left, left, up, left, up, right, right, right, right, right, right, down, down, down, right, right, up, left, up, right, up, right, right, down, down, right, up, right, down, right, down, left, left, left, down, down, down, left, up, up, left, down, down, down, right, right, right, up, up, right, down, down, down, right, down, down, left, left, up, left, down, down, left, down, right, down, down, right, up, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='g6iUabWCGb3knsEP-_zhiQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_35.json`

**Score:** 3.66%

**Ground Truth Solution:**
```
down, down, down, right, right, down, right, up, right, up, left, left, up, left, up, right, right, right, right, right, right, down, down, down, right, right, up, left, up, right, up, right, right, down, down, right, up, right, down, right, down, left, left, left, down, down, down, left, up, up, left, down, down, down, right, right, right, up, up, right, down, down, down, right, down, down, left, left, up, left, down, down, left, down, right, down, down, right, up, right, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='haiUabXYGPWinsEPtZuzkQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=13484,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13484
    ),
  ],
  total_token_count=14134
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13484 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13484
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14134 traffic_type=None
```

### `maze_line_15x15_adj_35.txt`

**Score:** 3.66%

**Ground Truth Solution:**
```
down, down, down, right, right, down, right, up, right, up, left, left, up, left, up, right, right, right, right, right, right, down, down, down, right, right, up, left, up, right, up, right, right, down, down, right, up, right, down, right, down, left, left, left, down, down, down, left, up, up, left, down, down, down, right, right, right, up, up, right, down, down, down, right, down, down, left, left, up, left, down, down, left, down, right, down, down, right, up, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='haiUafHaMqeN7M8P04OMiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=3676,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3676
    ),
  ],
  total_token_count=3731
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=3676 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3676
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3731 traffic_type=None
```

### `maze_line_15x15_tokenized_35.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, right, right, down, right, up, right, up, left, left, up, left, up, right, right, right, right, right, right, down, down, down, right, right, up, left, up, right, up, right, right, down, down, right, up, right, down, right, down, left, left, left, down, down, down, left, up, up, left, down, down, down, right, right, right, up, up, right, down, down, down, right, down, down, left, left, up, left, down, down, left, down, right, down, down, right, up, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iKiUabTqCqXu7M8P4P7CkQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_35.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i6iUacnCEtqE7M8Pyb-HyQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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
  total_token_count=431
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=431 traffic_type=None
```

### `maze_occupancy_15x15_35.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, down, down, down, right, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, right, down, down, down, right, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,down,down,down,right,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,right,down,down,down,right,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jaiUabGFBu6hnsEPsYODsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_35.json`

**Score:** 0.61%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j6iUaeW3E_3onsEP3cCnyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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
) total_tokens=165 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27628 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27628
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28278 traffic_type=None
```

### `maze_occupancy_15x15_adj_35.txt`

**Score:** 3.66%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j6iUadz5NKiSkdUPmsP7uA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=115,
  prompt_token_count=7730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7730
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=115 candidates_tokens_details=None prompt_token_count=7730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7845 traffic_type=None
```

### `maze_occupancy_15x15_ascii_35.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kqiUaYPXI9uXkdUPsdSSoAI' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=534,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=534
    ),
  ],
  total_token_count=534
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=534 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=534
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=534 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lKiUabGPHqXu7M8P4P7CkQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

