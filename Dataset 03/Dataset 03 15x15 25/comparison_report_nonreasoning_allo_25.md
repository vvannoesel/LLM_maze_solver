# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_25.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right` |
| `maze_line_15x15_25.json` | **5.26%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_25.json` | **0.00%** | `input: 13488 , ouput: 55` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_25.txt` | **5.26%** | `input: 3680 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left` |
| `maze_line_15x15_tokenized_25.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_25.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left` |
| `maze_occupancy_15x15_25.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down` |
| `maze_occupancy_15x15_adj_25.json` | **2.63%** | `input: 27628 , ouput: 650` | `down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down` |
| `maze_occupancy_15x15_adj_25.txt` | **5.26%** | `input: 7730 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_25.txt` | **nan%** | `input: 552 , ouput: 0` | `` |
| `maze_occupancy_15x15_tokenized_25.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_25.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, right, right, right, right, right, right, down, right, up, right, right, up, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='16aUabrwEMTV7M8PzpbtcQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_25.json`

**Score:** 5.26%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, right, right, right, right, right, right, down, right, up, right, right, up, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2KaUafrDCp6jnsEP0cGigAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_25.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, right, right, right, right, right, right, down, right, up, right, right, up, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2KaUabGJNKXu7M8P4P7CkQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=13488,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13488
    ),
  ],
  total_token_count=13543
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=13488 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13488
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13543 traffic_type=None
```

### `maze_line_15x15_adj_25.txt`

**Score:** 5.26%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, right, right, right, right, right, right, down, right, up, right, right, up, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='26aUadwrqoSR1Q_MhZigAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3680,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3680
    ),
  ],
  total_token_count=4330
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3680 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3680
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4330 traffic_type=None
```

### `maze_line_15x15_tokenized_25.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, down, left, down, down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, right, right, right, right, right, right, down, right, up, right, right, up, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3aaUafS0LI3hnsEPj-nr0Q8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_25.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4KaUacjWAdX1kdUPq5K00AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_25.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,right,down,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4aaUafiXOtuXkdUPsdSSoAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_25.json`

**Score:** 2.63%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5KaUaZvZHpqAkdUP4OXyyQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_25.txt`

**Score:** 5.26%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5qaUaYjrF8_HnsEPxMXdkAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7730
    ),
  ],
  total_token_count=8380
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8380 traffic_type=None
```

### `maze_occupancy_15x15_ascii_25.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, right, right, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6aaUadqYCqiSkdUPusP7uA8' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=552,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=552
    ),
  ],
  total_token_count=552
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=552 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=552
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=552 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_25.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='66aUaaysC4Tv7M8P2pmO8AE' usage_metadata=GenerateContentResponseUsageMetadata(
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

