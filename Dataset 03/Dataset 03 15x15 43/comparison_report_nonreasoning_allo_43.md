# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_43.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_43.json` | **2.86%** | `input: 9807 , ouput: 57` | `right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_line_15x15_adj_43.json` | **1.43%** | `input: 13485 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_43.txt` | **1.43%** | `input: 3677 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_43.txt` | **1.43%** | `input: 3282 , ouput: 650` | `right, right, right, down, right, down, right, down, down, right, down, down, right, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, down, right, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left` |
| `maze_occupancy_15x15_43.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_43.json` | **5.71%** | `input: 4246 , ouput: 650` | `right, right, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_43.json` | **2.14%** | `input: 27633 , ouput: 650` | `right, right, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right` |
| `maze_occupancy_15x15_adj_43.txt` | **0.00%** | `input: 7734 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_43.txt` | **0.00%** | `input: 546 , ouput: 650` | `down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_43.txt` | **4.29%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_43.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, down, right, right, up, up, right, down, right, up, right, down, right, down, left, left, left, down, down, down, right, right, up, up, right, right, down, right, up, right, up, up, left, up, right, right, right, right, right, down, down, left, up, left, left, down, right, down, down, right, down, down, down, down, down, left, up, left, down, left, down, right, right, right, down, down, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZqmUabSEPMeqnsEPypadgQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_43.json`

**Score:** 2.86%

**Ground Truth Solution:**
```
right, down, down, right, right, up, up, right, down, right, up, right, down, right, down, left, left, left, down, down, down, right, right, up, up, right, right, down, right, up, right, up, up, left, up, right, right, right, right, right, down, down, left, up, left, left, down, right, down, down, right, down, down, down, down, down, left, up, left, down, left, down, right, right, right, down, down, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,right,right,down,right,right,down,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Z6mUac2PLJTlnsEP9NTwiQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_43.json`

**Score:** 1.43%

**Ground Truth Solution:**
```
right, down, down, right, right, up, up, right, down, right, up, right, down, right, down, left, left, left, down, down, down, right, right, up, up, right, right, down, right, up, right, up, up, left, up, right, right, right, right, right, down, down, left, up, left, left, down, right, down, down, right, down, down, down, down, down, left, up, left, down, left, down, right, right, right, down, down, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aKmUafCGHYvw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_43.txt`

**Score:** 1.43%

**Ground Truth Solution:**
```
right, down, down, right, right, up, up, right, down, right, up, right, down, right, down, left, left, left, down, down, down, right, right, up, up, right, right, down, right, up, right, up, up, left, up, right, right, right, right, right, down, down, left, up, left, left, down, right, down, down, right, down, down, down, down, down, left, up, left, down, left, down, right, right, right, down, down, right, down, down
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
        text='right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aqmUaZazG73ukdUPl-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_43.txt`

**Score:** 1.43%

**Ground Truth Solution:**
```
right, down, down, right, right, up, up, right, down, right, up, right, down, right, down, left, left, left, down, down, down, right, right, up, up, right, right, down, right, up, right, up, up, left, up, right, right, right, right, right, down, down, left, up, left, left, down, right, down, down, right, down, down, down, down, down, left, up, left, down, left, down, right, right, right, down, down, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, right, down, right, down, down, right, down, down, right, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, down, right, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left, down, left, down, down, down, right, down, right, up, right, up, up, left, up, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,down,right,down,down,right,down,down,right,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,down,right,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,down,left,down,down,down,right,down,right,up,right,up,up,left,up,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bKmUaaPWHfCMkdUPn6WNwAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_43.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, up, up, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, right, right, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='b6mUadGfNMDw7M8P6KGOoQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_43.json`

**Score:** 5.71%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, up, up, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,right,right,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='camUae_CKpS8nsEPnPGoiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_43.json`

**Score:** 2.14%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, up, up, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dKmUaaS2A-LW7M8PiN7ImA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27633,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27633
    ),
  ],
  total_token_count=28283
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27633 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27633
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28283 traffic_type=None
```

### `maze_occupancy_15x15_adj_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, up, up, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, right, right, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dKmUaYydI_CMkdUPn6WNwAE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7734,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7734
    ),
  ],
  total_token_count=7847
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7734 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7734
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7847 traffic_type=None
```

### `maze_occupancy_15x15_ascii_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, up, up, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, down, down, down, down, down, down, down, right, right, down, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,right,down,down,down,down,down,down,down,down,right,right,down,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='damUaf2UM8D97M8P2J3Q4Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=546,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=546
    ),
  ],
  total_token_count=1196
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=546
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1196 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_43.txt`

**Score:** 4.29%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, right, right, up, up, right, right, up, up, up, up, left, left, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, left, left, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, up, up, left, left, down, down, left, left, down, down, right, right, right, right, right, right, down, down, down, down, right, right, down, down, down, down
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
        text='right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d6mUafW8JNfu7M8Pk_6wkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

