# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_32.jpg` | **3.12%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, down, right, down, right, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right` |
| `maze_line_15x15_32.json` | **nan%** | `input: 9807 , ouput: 0` | `` |
| `maze_line_15x15_adj_32.json` | **1.56%** | `input: 13489 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_32.txt` | **0.00%** | `input: 3681 , ouput: 650` | `down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down` |
| `maze_line_15x15_tokenized_32.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_32.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_32.json` | **1.56%** | `input: 4246 , ouput: 650` | `right, right, right, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_32.json` | **3.12%** | `input: 27622 , ouput: 115` | `right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_32.txt` | **0.00%** | `input: 7726 , ouput: 650` | `down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down` |
| `maze_occupancy_15x15_ascii_32.txt` | **2.34%** | `input: 517 , ouput: 650` | `right, right, down, right, down, down, right, right, down, right, right, right, down, right, right, right, down, right, right, down, right, right, right, down, right, right, down, right, right, right, down, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right` |
| `maze_occupancy_15x15_tokenized_32.txt` | **3.12%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_32.jpg`

**Score:** 3.12%

**Ground Truth Solution:**
```
right, down, left, down, right, right, right, down, left, left, left, down, down, down, down, down, right, up, right, up, left, up, up, right, right, right, down, left, down, down, down, down, left, down, down, left, down, left, down, down, right, right, right, up, left, up, right, right, right, down, down, right, right, up, right, up, right, down, right, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, down, right, down, right, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,down,right,down,right,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KaiUaan9Harw7M8Pw5-qsA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_32.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, left, down, right, right, right, down, left, left, left, down, down, down, down, down, right, up, right, up, left, up, up, right, right, right, down, left, down, down, down, down, left, down, down, left, down, left, down, down, right, right, right, up, left, up, right, right, right, down, down, right, right, up, right, up, right, down, right, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LKiUacC7Etfu7M8Pk_6wkAU' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=9807
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9807 traffic_type=None
```

### `maze_line_15x15_adj_32.json`

**Score:** 1.56%

**Ground Truth Solution:**
```
right, down, left, down, right, right, right, down, left, left, left, down, down, down, down, down, right, up, right, up, left, up, up, right, right, right, down, left, down, down, down, down, left, down, down, left, down, left, down, down, right, right, right, up, left, up, right, right, right, down, down, right, right, up, right, up, right, down, right, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LaiUaYbpC73ukdUP_eOHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=13489,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13489
    ),
  ],
  total_token_count=13546
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=13489 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13489
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13546 traffic_type=None
```

### `maze_line_15x15_adj_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, right, right, right, down, left, left, left, down, down, down, down, down, right, up, right, up, left, up, up, right, right, right, down, left, down, down, down, down, left, down, down, left, down, left, down, down, right, right, right, up, left, up, right, right, right, down, down, right, right, up, right, up, right, down, right, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LqiUabWUGfWinsEPtZuzkQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3681,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3681
    ),
  ],
  total_token_count=4331
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3681 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3681
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4331 traffic_type=None
```

### `maze_line_15x15_tokenized_32.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, left, down, right, right, right, down, left, left, left, down, down, down, down, down, right, up, right, up, left, up, up, right, right, right, down, left, down, down, down, down, left, down, down, left, down, left, down, down, right, right, right, up, left, up, right, right, right, down, down, right, right, up, right, up, right, down, right, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MKiUafyIPNrOnsEPw-rG0AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_32.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NKiUaeW8BIb1kdUP6IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_32.json`

**Score:** 1.56%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,right,right,right,right,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NqiUaYC8Cb-NkdUPkILV0AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_32.json`

**Score:** 3.12%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='N6iUaenfK8DzkdUPloGV4Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=115,
  prompt_token_count=27622,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27622
    ),
  ],
  total_token_count=27737
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=115 candidates_tokens_details=None prompt_token_count=27622 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27622
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27737 traffic_type=None
```

### `maze_occupancy_15x15_adj_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OaiUac7BLsDzkdUPloGV4Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7726,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7726
    ),
  ],
  total_token_count=8376
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7726 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7726
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8376 traffic_type=None
```

### `maze_occupancy_15x15_ascii_32.txt`

**Score:** 2.34%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, right, down, down, right, right, down, right, right, right, down, right, right, right, down, right, right, down, right, right, right, down, right, right, down, right, right, right, down, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right, right, down, right, right, right, down, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,right,right,down,right,right,right,down,right,right,right,down,right,right,down,right,right,right,down,right,right,down,right,right,right,down,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,right,down,right,right,right,down,right,right,right,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OqiUaffnN-mekdUPn_LrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=517,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=517
    ),
  ],
  total_token_count=1167
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=517 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=517
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1167 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_32.txt`

**Score:** 3.12%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, left, left, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='PKiUafbRMKfi7M8Pw_bz4AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

