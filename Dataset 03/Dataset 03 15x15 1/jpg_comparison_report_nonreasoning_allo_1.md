# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_1.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_occupancy_15x15_1.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, down, down, right, down, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, right, down, right, right, down, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down` |

---

## Full LLM Responses

### `maze_line_15x15_1.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, down, right, right, up, left, up, right, up, right, down, down, right, up, up, right, down, right, down, down, down, right, up, up, right, right, down, left, down, down, down, down, down, left, down, left, up, left, down, down, left, left, down, left, up, left, up, up, up, left, up, right, right, down, down, right, right, up, left, up, right, right, up, up, up, left, down, left, left, down, left, left, up, left, left, down, down, right, down, down, down, down, down, left, down, right, down, right, down, right, up, up, right, right, right, down, left, down, right, right, up, up, up, right, right, right, up, up, right, up, up, right, right, down, left, down, right, down, right, down, down, down, left, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BM4maYuNCYXlxN8P2afLYA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_1.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, right, right, up, up, up, up, up, up, left, left, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, up, up, up, up, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, down, right, right, down, right, down, down, right, right, down, down, right, down, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, right, down, right, down, right, right, down, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,down,right,right,down,right,down,down,right,right,down,down,right,down,right,down,down,right,down,down,right,right,down,down,right,right,down,down,right,right,down,right,down,right,right,down,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B84maaPrH4CDvdIP_s7auQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

