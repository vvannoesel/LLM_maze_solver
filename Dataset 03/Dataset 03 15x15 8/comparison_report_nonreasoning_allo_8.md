# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_8.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_8.json` | **nan%** | `input: 9807 , ouput: 0` | `` |
| `maze_line_15x15_adj_8.json` | **1.28%** | `input: 13485 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_8.txt` | **1.28%** | `input: 3677 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_8.txt` | **0.00%** | `input: 3282 , ouput: 650` | `down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right` |
| `maze_occupancy_15x15_8.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_8.json` | **0.64%** | `input: 4246 , ouput: 650` | `right, down, down, right, right, down, down, right, right, down, down, right, right, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right` |
| `maze_occupancy_15x15_adj_8.json` | **2.56%** | `input: 27639 , ouput: 650` | `right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right` |
| `maze_occupancy_15x15_adj_8.txt` | **nan%** | `input: 7734 , ouput: 0` | `` |
| `maze_occupancy_15x15_ascii_8.txt` | **1.92%** | `input: 548 , ouput: 650` | `right, right, down, right, right, down, down, right, right, right, right, right, right, down, right, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right` |
| `maze_occupancy_15x15_tokenized_8.txt` | **1.92%** | `input: 12134 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_8.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, left, down, down, right, up, right, down, down, right, down, down, left, down, right, down, right, up, up, right, down, right, up, right, right, down, down, down, right, down, left, down, down, down, down, right, up, right, up, left, up, right, up, right, right, down, right, up, up, left, up, left, left, up, right, up, up, right, right, right, down, left, down, down, right, down, down, down, down, left, left, left, down, right, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uf4lacW7OJHkkdUPk_Ko-QE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_8.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, left, down, down, right, up, right, down, down, right, down, down, left, down, right, down, right, up, up, right, down, right, up, right, right, down, down, down, right, down, left, down, down, down, down, right, up, right, up, left, up, right, up, right, right, down, right, up, up, left, up, left, left, up, right, up, up, right, right, right, down, left, down, down, right, down, down, down, down, left, left, left, down, right, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vf4labR-xpiR1Q_H1ejgDQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_8.json`

**Score:** 1.28%

**Ground Truth Solution:**
```
right, down, left, down, down, right, up, right, down, down, right, down, down, left, down, right, down, right, up, up, right, down, right, up, right, right, down, down, down, right, down, left, down, down, down, down, right, up, right, up, left, up, right, up, right, right, down, right, up, up, left, up, left, left, up, right, up, up, right, right, right, down, left, down, down, right, down, down, down, down, left, left, left, down, right, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vf4laaWrOMaYkdUPx9Xo4A0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_8.txt`

**Score:** 1.28%

**Ground Truth Solution:**
```
right, down, left, down, down, right, up, right, down, down, right, down, down, left, down, right, down, right, up, up, right, down, right, up, right, right, down, down, down, right, down, left, down, down, down, down, right, up, right, up, left, up, right, up, right, right, down, right, up, up, left, up, left, left, up, right, up, up, right, right, right, down, left, down, down, right, down, down, down, down, left, left, left, down, right, right, down, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wP4lafDKLa6mkdUPjtmneA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_8.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, down, right, up, right, down, down, right, down, down, left, down, right, down, right, up, up, right, down, right, up, right, right, down, down, down, right, down, left, down, down, down, down, right, up, right, up, left, up, right, up, right, right, down, right, up, up, left, up, left, left, up, right, up, up, right, right, right, down, left, down, down, right, down, down, down, down, left, left, left, down, right, right, down, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w_4laczoKv-qnsEPmN6KqA4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_8.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yf4laer2Ibe3nsEP8dSxUQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_8.json`

**Score:** 0.64%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, right, down, down, right, right, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,right,down,down,right,right,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zP4lafv8G66mkdUP-NineA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_8.json`

**Score:** 2.56%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='z_4ladONErKhkdUP9M3S2A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27639,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27639
    ),
  ],
  total_token_count=28289
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27639 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27639
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28289 traffic_type=None
```

### `maze_occupancy_15x15_adj_8.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0v4laajNN-D_nsEPmfWD4A0' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=7734,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7734
    ),
  ],
  total_token_count=7734
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=7734 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7734
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7734 traffic_type=None
```

### `maze_occupancy_15x15_ascii_8.txt`

**Score:** 1.92%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, down, down, right, right, right, right, right, right, down, right, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,down,right,right,right,right,right,right,down,right,down,right,right,right,right,right,right,right,down,down,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1f4laYyoKO2znsEP7-_u8A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=548,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=548
    ),
  ],
  total_token_count=1198
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=548 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=548
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1198 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_8.txt`

**Score:** 1.92%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, up, up, left, left, up, up, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, up, up, left, left, left, left, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1_4lac7UJc64nsEPvd3zWA' usage_metadata=GenerateContentResponseUsageMetadata(
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

