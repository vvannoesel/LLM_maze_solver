# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_46.jpg` | **3.23%** | `input: 436 , ouput: 650` | `right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right` |
| `maze_line_15x15_46.json` | **0.00%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_46.json` | **0.81%** | `input: 13489 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_46.txt` | **0.81%** | `input: 3681 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_46.txt` | **2.42%** | `input: 3283 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_46.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_46.json` | **0.40%** | `input: 4246 , ouput: 650` | `right, down, down, right, down, down, down, down, right, down, right, down, down, right, down, down, down, right, down, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down` |
| `maze_occupancy_15x15_adj_46.json` | **nan%** | `input: 27624 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_46.txt` | **0.00%** | `input: 7728 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_46.txt` | **nan%** | `input: 550 , ouput: 0` | `` |
| `maze_occupancy_15x15_tokenized_46.txt` | **0.81%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_15x15_46.jpg`

**Score:** 3.23%

**Ground Truth Solution:**
```
right, down, right, down, down, left, down, right, down, right, down, down, right, up, up, up, up, up, up, up, right, right, down, down, down, right, down, left, left, down, right, down, left, down, down, left, left, down, right, right, right, down, down, left, up, left, down, left, up, left, up, left, up, right, up, up, left, down, left, down, down, down, right, down, down, right, down, left, down, right, right, right, right, up, up, right, down, down, right, right, up, left, up, up, up, up, right, up, left, left, up, right, up, right, down, right, down, down, right, up, right, up, right, right, up, right, down, down, left, down, left, down, down, right, right, down, left, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KquUaaSBH9fu7M8Pk_6wkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_46.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, down, down, left, down, right, down, right, down, down, right, up, up, up, up, up, up, up, right, right, down, down, down, right, down, left, left, down, right, down, left, down, down, left, left, down, right, right, right, down, down, left, up, left, down, left, up, left, up, left, up, right, up, up, left, down, left, down, down, down, right, down, down, right, down, left, down, right, right, right, right, up, up, right, down, down, right, right, up, left, up, up, up, up, right, up, left, left, up, right, up, right, down, right, down, down, right, up, right, up, right, right, up, right, down, down, left, down, left, down, down, right, right, down, left, down, left, left, down, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K6uUacWAEIbe7M8P85iEkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_46.json`

**Score:** 0.81%

**Ground Truth Solution:**
```
right, down, right, down, down, left, down, right, down, right, down, down, right, up, up, up, up, up, up, up, right, right, down, down, down, right, down, left, left, down, right, down, left, down, down, left, left, down, right, right, right, down, down, left, up, left, down, left, up, left, up, left, up, right, up, up, left, down, left, down, down, down, right, down, down, right, down, left, down, right, right, right, right, up, up, right, down, down, right, right, up, left, up, up, up, up, right, up, left, left, up, right, up, right, down, right, down, down, right, up, right, up, right, right, up, right, down, down, left, down, left, down, down, right, right, down, left, down, left, left, down, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K6uUaYTfMafi7M8Pw_bz4AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_46.txt`

**Score:** 0.81%

**Ground Truth Solution:**
```
right, down, right, down, down, left, down, right, down, right, down, down, right, up, up, up, up, up, up, up, right, right, down, down, down, right, down, left, left, down, right, down, left, down, down, left, left, down, right, right, right, down, down, left, up, left, down, left, up, left, up, left, up, right, up, up, left, down, left, down, down, down, right, down, down, right, down, left, down, right, right, right, right, up, up, right, down, down, right, right, up, left, up, up, up, up, right, up, left, left, up, right, up, right, down, right, down, down, right, up, right, up, right, right, up, right, down, down, left, down, left, down, down, right, right, down, left, down, left, left, down, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LauUacGtLOmekdUPq_LrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_46.txt`

**Score:** 2.42%

**Ground Truth Solution:**
```
right, down, right, down, down, left, down, right, down, right, down, down, right, up, up, up, up, up, up, up, right, right, down, down, down, right, down, left, left, down, right, down, left, down, down, left, left, down, right, right, right, down, down, left, up, left, down, left, up, left, up, left, up, right, up, up, left, down, left, down, down, down, right, down, down, right, down, left, down, right, right, right, right, up, up, right, down, down, right, right, up, left, up, up, up, up, right, up, left, left, up, right, up, right, down, right, down, down, right, up, right, up, right, right, up, right, down, down, left, down, left, down, down, right, right, down, left, down, left, left, down, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,right,right,right,right,right,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='L6uUadn2MKfi7M8Pw_bz4AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_46.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M6uUaaXlJcewnsEPm4ag0QM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_46.json`

**Score:** 0.40%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, down, down, down, down, right, down, right, down, down, right, down, down, down, right, down, down, down, right, down, down, right, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,down,down,down,down,right,down,right,down,down,right,down,down,down,right,down,down,down,right,down,down,right,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NKuUafKsMsf5nsEPi7DUqAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_46.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='N6uUaa_FM63hnsEP0oDs0QE' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=27624,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27624
    ),
  ],
  total_token_count=27624
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=27624 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27624
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27624 traffic_type=None
```

### `maze_occupancy_15x15_adj_46.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='OKuUaeGyJZz07M8PqPy4oQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7728,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7728
    ),
  ],
  total_token_count=7841
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7728 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7728
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7841 traffic_type=None
```

### `maze_occupancy_15x15_ascii_46.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='O6uUabnNCrWVnsEPl_iniQI' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=550,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=550
    ),
  ],
  total_token_count=550
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=550 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=550
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=550 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_46.txt`

**Score:** 0.81%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, down, down, down, down, left, left, up, up, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, left, left, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='PKuUabmyIaeN7M8Pq5OaoQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

