# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_45.jpg` | **0.00%** | `input: 436 , ouput: 650` | `down, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right` |
| `maze_line_15x15_45.json` | **1.00%** | `input: 9807 , ouput: 53` | `right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_45.json` | **nan%** | `input: 13487 , ouput: 0` | `` |
| `maze_line_15x15_adj_45.txt` | **1.00%** | `input: 3679 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_45.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_45.jpg` | **0.50%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right` |
| `maze_occupancy_15x15_45.json` | **2.00%** | `input: 4246 , ouput: 650` | `right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_45.json` | **1.50%** | `input: 27624 , ouput: 117` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_45.txt` | **0.00%** | `input: 7727 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_45.txt` | **2.50%** | `input: 552 , ouput: 650` | `right, right, down, down, right, down, right, right, down, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, right, right, right, down, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, down, down, right, down, right, down, down, down, right, right, down, right, right, down, down, right, right, right, right, down, down, right, right, right, down, right, down, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, down, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right` |
| `maze_occupancy_15x15_tokenized_45.txt` | **1.00%** | `input: 12134 , ouput: 650` | `right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_45.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, down, left, down, right, down, right, right, down, down, left, up, left, down, down, right, down, right, down, left, down, down, left, down, down, right, right, right, right, up, right, right, up, left, up, right, up, right, up, up, right, up, left, left, left, left, left, up, up, right, up, right, up, up, right, right, down, down, right, right, right, up, right, down, down, down, right, down, right, down, down, left, up, left, up, left, left, down, right, down, down, down, right, up, right, right, down, left, down, down, right, down
```

**Extracted Answer:**
```
down, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KKqUaYjJOb-xnsEPuMqioQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_45.json`

**Score:** 1.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, down, left, down, right, down, right, right, down, down, left, up, left, down, down, right, down, right, down, left, down, down, left, down, down, right, right, right, right, up, right, right, up, left, up, right, up, right, up, up, right, up, left, left, left, left, left, up, up, right, up, right, up, up, right, right, down, down, right, right, right, up, right, down, down, down, right, down, right, down, down, left, up, left, up, left, left, down, right, down, down, down, right, up, right, right, down, left, down, down, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KaqUadGoPNGqnsEPwL-awAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_45.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, down, left, down, right, down, right, right, down, down, left, up, left, down, down, right, down, right, down, left, down, down, left, down, down, right, right, right, right, up, right, right, up, left, up, right, up, right, up, up, right, up, left, left, left, left, left, up, up, right, up, right, up, up, right, right, down, down, right, right, right, up, right, down, down, down, right, down, right, down, down, left, up, left, up, left, left, down, right, down, down, down, right, up, right, right, down, left, down, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LaqUacqlCdyWkdUPpoLOyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=13487,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13487
    ),
  ],
  total_token_count=13487
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=13487 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13487
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13487 traffic_type=None
```

### `maze_line_15x15_adj_45.txt`

**Score:** 1.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, down, left, down, right, down, right, right, down, down, left, up, left, down, down, right, down, right, down, left, down, down, left, down, down, right, right, right, right, up, right, right, up, left, up, right, up, right, up, up, right, up, left, left, left, left, left, up, up, right, up, right, up, up, right, right, down, down, right, right, right, up, right, down, down, down, right, down, right, down, down, left, up, left, up, left, left, down, right, down, down, down, right, up, right, right, down, left, down, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='L6qUabbvH73ukdUPh-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_45.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, down, left, down, right, down, right, right, down, down, left, up, left, down, down, right, down, right, down, left, down, down, left, down, down, right, right, right, right, up, right, right, up, left, up, right, up, right, up, up, right, up, left, left, left, left, left, up, up, right, up, right, up, up, right, right, down, down, right, right, right, up, right, down, down, down, right, down, right, down, down, left, up, left, up, left, left, down, right, down, down, down, right, up, right, right, down, left, down, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MaqUadOeGpz07M8PqPy4oQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_45.jpg`

**Score:** 0.50%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, up, up, right, right, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, right, right, up, up, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NaqUacWnKoWjnsEPtLnfyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_45.json`

**Score:** 2.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, up, up, right, right, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, right, right, up, up, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZqqUaeDhFND-nsEPgIiFuAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_45.json`

**Score:** 1.50%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, up, up, right, right, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, right, right, up, up, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Z6qUaZWRM73knsEP-_zhiQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=117,
  prompt_token_count=27624,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27624
    ),
  ],
  total_token_count=27741
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=117 candidates_tokens_details=None prompt_token_count=27624 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27624
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27741 traffic_type=None
```

### `maze_occupancy_15x15_adj_45.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, up, up, right, right, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, right, right, up, up, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aqqUafmGELWVnsEPl_iniQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7727,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7727
    ),
  ],
  total_token_count=8377
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7727 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7727
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8377 traffic_type=None
```



### `maze_occupancy_15x15_ascii_45.txt`

**Score:** 2.50%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, up, up, right, right, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, right, right, up, up, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, right, right, down, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, right, down, right, right, down, right, down, right, down, right, right, down, right, right, right, down, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, down, down, right, down, right, down, down, down, right, right, down, right, right, down, down, right, right, right, right, down, down, right, right, right, down, right, down, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, down, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, right, right, down, down, down, right, right, right, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,right,right,down,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,right,down,right,right,down,right,down,right,down,right,right,down,right,right,right,down,down,down,right,right,down,down,right,down,right,right,down,down,right,right,right,right,down,down,right,right,right,right,right,down,down,right,down,right,down,down,down,right,right,down,right,right,down,down,right,right,right,right,down,down,right,right,right,down,right,down,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,down,right,right,right,down,right,right,down,right,down,down,right,right,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,right,right,down,down,down,right,right,right,right,down,right,right,down,right,down,down,right,right,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,right,right,down,down,down,right,right,right,right,down,right,right,down,right,down,down,right,right,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,right,right,down,down,down,right,right,right,right,down,right,right,down,right,down,down,right,right,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,right,right,down,down,down,right,right,right,right,down,right,right,down,right,down,down,right,right,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,right,right,down,down,down,right,right,right,right,down,right,right,down,right,down,down,right,right,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,right,right,down,down,down,right,right,right,right,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jaqUaYHxLemekdUPq_LrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=552,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=552
    ),
  ],
  total_token_count=1202
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=552 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=552
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1202 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_45.txt`

**Score:** 1.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, up, up, right, right, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, right, right, up, up, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j6qUaZvnO9D-nsEPgIiFuAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

