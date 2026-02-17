# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_50.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, left, down, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right` |
| `maze_line_15x15_50.json` | **1.39%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_50.json` | **0.00%** | `input: 13487 , ouput: 55` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_50.txt` | **0.00%** | `input: 3679 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_50.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_50.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_50.json` | **0.00%** | `input: 4246 , ouput: 57` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_50.json` | **4.17%** | `input: 27629 , ouput: 650` | `down, down, right, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right` |
| `maze_occupancy_15x15_adj_50.txt` | **1.39%** | `input: 7731 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_50.txt` | **0.00%** | `input: 547 , ouput: 650` | `up, right, right, right, right, right, right, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_50.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_50.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, left, down, right, down, left, down, down, down, down, down, right, up, right, down, right, right, down, down, down, right, right, up, up, right, up, left, up, left, left, left, up, right, right, up, left, left, up, up, up, right, right, up, right, up, right, right, right, right, down, down, right, down, right, down, left, down, right, right, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, left, down, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,left,down,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uKuUaaDrEZeBkdUP9--_-AI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_50.json`

**Score:** 1.39%

**Ground Truth Solution:**
```
down, right, down, down, left, down, right, down, left, down, down, down, down, down, right, up, right, down, right, right, down, down, down, right, right, up, up, right, up, left, up, left, left, left, up, right, right, up, left, left, up, up, up, right, right, up, right, up, right, right, right, right, down, down, right, down, right, down, left, down, right, right, right, down, down, down, down, left, down, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uauUaYr4A_OekdUPoeqlcA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_50.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, left, down, right, down, left, down, down, down, down, down, right, up, right, down, right, right, down, down, down, right, right, up, up, right, up, left, up, left, left, left, up, right, right, up, left, left, up, up, up, right, right, up, right, up, right, right, right, right, down, down, right, down, right, down, left, down, right, right, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uauUaYucIaXu7M8P4P7CkQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=13487,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13487
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=13487 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13487
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13542 traffic_type=None
```

### `maze_line_15x15_adj_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, left, down, right, down, left, down, down, down, down, down, right, up, right, down, right, right, down, down, down, right, right, up, up, right, up, left, up, left, left, left, up, right, right, up, left, left, up, up, up, right, right, up, right, up, right, right, right, right, down, down, right, down, right, down, left, down, right, right, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='u6uUaZzhKdGxnsEPuvytyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, left, down, right, down, left, down, down, down, down, down, right, up, right, down, right, right, down, down, down, right, right, up, up, right, up, left, up, left, left, left, up, right, right, up, left, left, up, up, up, right, right, up, right, up, right, right, right, right, down, down, right, down, right, down, left, down, right, right, right, down, down, down, down, left, down, down, right, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vKuUadPnObOlnsEPjtai8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_50.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, left, left, up, up, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wKuUabrqBfCMkdUPpaWNwAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_50.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, left, left, up, up, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wKuUabDtN4vw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_50.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, left, left, up, up, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wquUaYSdHdGqnsEPwL-awAE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27629,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27629
    ),
  ],
  total_token_count=28279
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27629 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27629
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28279 traffic_type=None
```

### `maze_occupancy_15x15_adj_50.txt`

**Score:** 1.39%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, left, left, up, up, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w6uUaYH1FKiSkdUPmsP7uA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7731,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7731
    ),
  ],
  total_token_count=7844
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7731 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7731
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7844 traffic_type=None
```

### `maze_occupancy_15x15_ascii_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, left, left, up, up, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
up, right, right, right, right, right, right, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='up,right,right,right,right,right,right,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xauUaZqqEKXu7M8P4P7CkQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=547,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=547
    ),
  ],
  total_token_count=1197
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=547 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=547
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1197 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, up, up, left, left, up, up, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='x6uUada3FPaHnsEPm6HKoQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

