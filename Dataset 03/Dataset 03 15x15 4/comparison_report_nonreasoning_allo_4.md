# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_4.jpg` | **3.57%** | `input: 436 , ouput: 81` | `right, down, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down` |
| `maze_line_15x15_4.json` | **1.79%** | `input: 9807 , ouput: 650` | `right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right` |
| `maze_line_15x15_adj_4.json` | **1.79%** | `input: 13489 , ouput: 55` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_4.txt` | **1.79%** | `input: 3681 , ouput: 533` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_4.txt` | **0.00%** | `input: 3282 , ouput: 650` | `down, down, down, right, right, right, down, right, right, down, right, down, down, right, down, right, right, up, right, right, down, right, right, down, right, down, right, right, up, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right` |
| `maze_occupancy_15x15_4.jpg` | **0.89%** | `input: 431 , ouput: 650` | `right, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, left, down, right, down, right, down, left, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right` |
| `maze_occupancy_15x15_4.json` | **0.89%** | `input: 4246 , ouput: 650` | `right, down, down, down, down, down, right, right, right, down, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_4.json` | **nan%** | `input: 27632 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_4.txt` | **0.00%** | `input: 7729 , ouput: 117` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_4.txt` | **2.68%** | `input: 533 , ouput: 650` | `right, right, down, right, down, right, down, down, right, down, right, right, down, right, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down` |
| `maze_occupancy_15x15_tokenized_4.txt` | **1.79%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_15x15_4.jpg`

**Score:** 3.57%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, down, left, left, down, right, down, down, right, right, right, down, right, down, right, down, down, right, down, right, up, right, up, left, left, up, up, left, up, right, right, right, down, down, right, up, right, down, down, down, right, right, down, left, down, right, down, left, down, right
```

**Extracted Answer:**
```
right, down, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Iv0lafuxLfPnvdIPrO_VYQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=81,
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
  total_token_count=517
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=81 candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=517 traffic_type=None
```

### `maze_line_15x15_4.json`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, down, left, left, down, right, down, down, right, right, right, down, right, down, right, down, down, right, down, right, up, right, up, left, left, up, up, left, up, right, right, right, down, down, right, up, right, down, down, down, right, right, down, left, down, right, down, left, down, right
```

**Extracted Answer:**
```
right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Jf0ladz5IPCMvdIP2Ke6mQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_4.json`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, down, left, left, down, right, down, down, right, right, right, down, right, down, right, down, down, right, down, right, up, right, up, left, left, up, up, left, up, right, right, right, down, down, right, up, right, down, down, down, right, right, down, left, down, right, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Jv0labfRIrX3vdIP7KqaqAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=13489,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13489
    ),
  ],
  total_token_count=13544
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=13489 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13489
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13544 traffic_type=None
```

### `maze_line_15x15_adj_4.txt`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, down, left, left, down, right, down, down, right, right, right, down, right, down, right, down, down, right, down, right, up, right, up, left, left, up, up, left, up, right, right, right, down, down, right, up, right, down, down, down, right, right, down, left, down, right, down, left, down, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KP0lae2LNae3xN8P9_60mAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=533,
  prompt_token_count=3681,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3681
    ),
  ],
  total_token_count=4214
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=533 candidates_tokens_details=None prompt_token_count=3681 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3681
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4214 traffic_type=None
```

### `maze_line_15x15_tokenized_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, down, left, left, down, right, down, down, right, right, right, down, right, down, right, down, down, right, down, right, up, right, up, left, left, up, up, left, up, right, right, right, down, down, right, up, right, down, down, down, right, right, down, left, down, right, down, left, down, right
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, right, right, down, right, down, down, right, down, right, right, up, right, right, down, right, right, down, right, down, right, right, up, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, right, right, right, down, right, right, down, right, down, down, right, down, right, right, up, right, right, down, right, right, down, right, down, right, right, up, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right, right, up, right, down, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K_0laZCyGP-zvdIP2uy0AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_4.jpg`

**Score:** 0.89%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, left, down, right, down, right, down, left, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,left,down,right,down,right,down,left,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Lv0lac_oENe7vdIPp92m4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_4.json`

**Score:** 0.89%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, right, right, right, down, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,right,right,right,down,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Mf0laZKbIdSlvdIP8tGGgQ4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_4.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Nv0laaeMGfq5vdIPxL60kAc' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=27632,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27632
    ),
  ],
  total_token_count=27632
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=27632 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27632
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27632 traffic_type=None
```

### `maze_occupancy_15x15_adj_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='N_0lad3tHoXkxN8P3PS3yAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=117,
  prompt_token_count=7729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7729
    ),
  ],
  total_token_count=7846
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=117 candidates_tokens_details=None prompt_token_count=7729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7846 traffic_type=None
```

### `maze_occupancy_15x15_ascii_4.txt`

**Score:** 2.68%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, down, right, down, down, right, down, right, right, down, right, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,right,down,down,right,down,right,right,down,right,right,right,down,right,down,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ov0laZjQAYi-vdIP1YXPiAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=533,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=533
    ),
  ],
  total_token_count=1183
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=533 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=533
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1183 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_4.txt`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Pf0lac3rAYW0vdIPnOTA0AE' usage_metadata=GenerateContentResponseUsageMetadata(
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

