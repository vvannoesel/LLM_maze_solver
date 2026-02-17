# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_30.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, left, down, right, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, right, up, right, down, right, down, left, down, right, right, down, left, down, right, right, down, right, down, left, down, right, right, up, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left` |
| `maze_line_15x15_30.json` | **2.05%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_30.json` | **2.05%** | `input: 13486 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_30.txt` | **0.00%** | `input: 3678 , ouput: 650` | `right, right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_30.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_30.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_30.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, down, right, right, right, down, right, down, down, down, down, right, down, down, right, right, down, down, down, down, right, right, right, down, right, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down` |
| `maze_occupancy_15x15_adj_30.json` | **0.68%** | `input: 27636 , ouput: 57` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_30.txt` | **2.05%** | `input: 7736 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_30.txt` | **0.68%** | `input: 545 , ouput: 650` | `down, down, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right` |
| `maze_occupancy_15x15_tokenized_30.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_30.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, right, right, right, down, right, up, up, up, left, up, right, right, down, right, down, right, up, right, up, right, down, down, down, left, down, down, right, down, left, left, up, left, down, down, left, left, left, up, right, up, left, left, up, left, down, down, right, down, down, down, down, left, up, up, left, down, down, left, down, right, right, right, right, up, up, right, down, down, down, down, left, down, right, right, up, right, right, down, right, up, up, left, up, left, up, left, up, up, right, down, right, up, right, up, right, right, up, up, up, right, up, left, up, up, up, right, right, right, down, down, down, left, down, down, right, down, left, left, down, right, down, left, down, right, right, down, down, left, left, left, left, down, right, down, down, right, up, up, right, down, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, right, up, right, down, right, down, left, down, right, right, down, left, down, right, right, down, right, down, left, down, right, right, up, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left, down, right, right, down, right, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,right,up,right,down,right,down,left,down,right,right,down,left,down,right,right,down,right,down,left,down,right,right,up,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,down,right,right,down,right,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8KeUae_2E6OrnsEP8_bgmQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_30.json`

**Score:** 2.05%

**Ground Truth Solution:**
```
down, down, down, right, right, right, right, down, right, up, up, up, left, up, right, right, down, right, down, right, up, right, up, right, down, down, down, left, down, down, right, down, left, left, up, left, down, down, left, left, left, up, right, up, left, left, up, left, down, down, right, down, down, down, down, left, up, up, left, down, down, left, down, right, right, right, right, up, up, right, down, down, down, down, left, down, right, right, up, right, right, down, right, up, up, left, up, left, up, left, up, up, right, down, right, up, right, up, right, right, up, up, up, right, up, left, up, up, up, right, right, right, down, down, down, left, down, down, right, down, left, left, down, right, down, left, down, right, right, down, down, left, left, left, left, down, right, down, down, right, up, up, right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8aeUaZPBAv27nsEPhr2MyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_30.json`

**Score:** 2.05%

**Ground Truth Solution:**
```
down, down, down, right, right, right, right, down, right, up, up, up, left, up, right, right, down, right, down, right, up, right, up, right, down, down, down, left, down, down, right, down, left, left, up, left, down, down, left, left, left, up, right, up, left, left, up, left, down, down, right, down, down, down, down, left, up, up, left, down, down, left, down, right, right, right, right, up, up, right, down, down, down, down, left, down, right, right, up, right, right, down, right, up, up, left, up, left, up, left, up, up, right, down, right, up, right, up, right, right, up, up, up, right, up, left, up, up, up, right, right, right, down, down, down, left, down, down, right, down, left, left, down, right, down, left, down, right, right, down, down, left, left, left, left, down, right, down, down, right, up, up, right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8qeUaauMA6fi7M8Pw_bz4AM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=13486,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13486
    ),
  ],
  total_token_count=13541
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=13486 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13486
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13541 traffic_type=None
```

### `maze_line_15x15_adj_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, right, right, right, down, right, up, up, up, left, up, right, right, down, right, down, right, up, right, up, right, down, down, down, left, down, down, right, down, left, left, up, left, down, down, left, left, left, up, right, up, left, left, up, left, down, down, right, down, down, down, down, left, up, up, left, down, down, left, down, right, right, right, right, up, up, right, down, down, down, down, left, down, right, right, up, right, right, down, right, up, up, left, up, left, up, left, up, up, right, down, right, up, right, up, right, right, up, up, up, right, up, left, up, up, up, right, right, right, down, down, down, left, down, down, right, down, left, left, down, right, down, left, down, right, right, down, down, left, left, left, left, down, right, down, down, right, up, up, right, down, down, right
```

**Extracted Answer:**
```
right, right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='86eUaba1M6iSkdUPmsP7uA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3678,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3678
    ),
  ],
  total_token_count=4328
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3678 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3678
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4328 traffic_type=None
```

### `maze_line_15x15_tokenized_30.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, right, right, right, right, down, right, up, up, up, left, up, right, right, down, right, down, right, up, right, up, right, down, down, down, left, down, down, right, down, left, left, up, left, down, down, left, left, left, up, right, up, left, left, up, left, down, down, right, down, down, down, down, left, up, up, left, down, down, left, down, right, right, right, right, up, up, right, down, down, down, down, left, down, right, right, up, right, right, down, right, up, up, left, up, left, up, left, up, up, right, down, right, up, right, up, right, right, up, up, up, right, up, left, up, up, up, right, right, right, down, down, down, left, down, down, right, down, left, left, down, right, down, left, down, right, right, down, down, left, left, left, left, down, right, down, down, right, up, up, right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9qeUaeHbE-bgnsEP6p2VqQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_30.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, left, left, left, left, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-aeUaercL5T8nsEP5Y-B0A8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_30.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, left, left, left, left, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, right, down, right, down, down, down, down, right, down, down, right, right, down, down, down, down, right, right, right, down, right, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down, down, down, down, right, right, right, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,down,right,down,down,down,down,right,down,down,right,right,down,down,down,down,right,right,right,down,right,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,down,down,down,right,right,right,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-6eUacDmLaeN7M8Pq5OaoQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_30.json`

**Score:** 0.68%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, left, left, left, left, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_KeUaY_EIZn7nsEP24btcA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=27636,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27636
    ),
  ],
  total_token_count=27693
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=27636 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27636
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27693 traffic_type=None
```

### `maze_occupancy_15x15_adj_30.txt`

**Score:** 2.05%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, left, left, left, left, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_aeUaZ7AEs_HnsEPxMXdkAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7736,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7736
    ),
  ],
  total_token_count=7849
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7736 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7736
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7849 traffic_type=None
```

### `maze_occupancy_15x15_ascii_30.txt`

**Score:** 0.68%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, left, left, left, left, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_6eUacmeB8Dw7M8P6KGOoQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=545,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=545
    ),
  ],
  total_token_count=1195
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=545 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=545
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1195 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_30.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, right, right, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, left, left, down, down, down, down, left, left, left, left, left, left, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, up, up, right, right, up, up, right, right, right, right, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AaiUaZL2EKX07M8P2KK7sA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

