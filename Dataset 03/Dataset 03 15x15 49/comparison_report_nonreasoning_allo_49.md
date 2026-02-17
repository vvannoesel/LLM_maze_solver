# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_49.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_49.json` | **2.70%** | `input: 9807 , ouput: 650` | `right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, down, right, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right` |
| `maze_line_15x15_adj_49.json` | **1.35%** | `input: 13486 , ouput: 55` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_49.txt` | **1.35%** | `input: 3678 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_49.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_49.jpg` | **3.38%** | `input: 431 , ouput: 650` | `right, right, down, down, right, down, right, down, down, down, right, right, down, right, down, down, down, right, down, right, down, right, right, down, down, down, right, down, right, down, down, down, right, down, right, down, down, down, right, right, down, right, down, right, right, down, down, right, down, right, right, down, down, down, right, down, right, down, right, right, down, down, down, right, down, right, down, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down` |
| `maze_occupancy_15x15_49.json` | **1.35%** | `input: 4246 , ouput: 650` | `right, right, right, down, down, right, down, down, right, right, down, down, down, right, right, right, down, down, down, down, right, right, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down` |
| `maze_occupancy_15x15_adj_49.json` | **2.03%** | `input: 27633 , ouput: 650` | `right, right, down, right, right, down, right, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, down, right, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, right, down, right, right, down, right, right, right, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down` |
| `maze_occupancy_15x15_adj_49.txt` | **nan%** | `input: 7734 , ouput: 0` | `` |
| `maze_occupancy_15x15_ascii_49.txt` | **nan%** | `input: 539 , ouput: 0` | `` |
| `maze_occupancy_15x15_tokenized_49.txt` | **2.03%** | `input: 12134 , ouput: 650` | `right, right, down, right, right, down, down, right, right, right, right, down, down, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_49.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, down, right, right, up, right, right, right, right, down, left, left, down, left, down, down, left, down, right, right, up, up, right, right, up, right, up, up, right, down, right, down, down, down, left, left, down, left, left, down, left, down, left, down, right, down, right, right, up, up, up, right, down, right, up, up, right, down, down, down, down, down, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mauUaea-OtjpnsEPmcvxyAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_49.json`

**Score:** 2.70%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, down, right, right, up, right, right, right, right, down, left, left, down, left, down, down, left, down, right, right, up, up, right, right, up, right, up, up, right, down, right, down, down, down, left, left, down, left, left, down, left, down, left, down, right, down, right, right, up, up, up, right, down, right, up, up, right, down, down, down, down, down, down, left, down, right
```

**Extracted Answer:**
```
right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, down, right, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,right,down,down,right,right,right,down,down,down,right,right,down,right,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m6uUaeD-O_aHnsEPm6HKoQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_49.json`

**Score:** 1.35%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, down, right, right, up, right, right, right, right, down, left, left, down, left, down, down, left, down, right, right, up, up, right, right, up, right, up, up, right, down, right, down, down, down, left, left, down, left, left, down, left, down, left, down, right, down, right, right, up, up, up, right, down, right, up, up, right, down, down, down, down, down, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nKuUaZzALb3ukdUPl-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_49.txt`

**Score:** 1.35%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, down, right, right, up, right, right, right, right, down, left, left, down, left, down, down, left, down, right, right, up, up, right, right, up, right, up, up, right, down, right, down, down, down, left, left, down, left, left, down, left, down, left, down, right, down, right, right, up, up, up, right, down, right, up, up, right, down, down, down, down, down, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nquUab7uGObgnsEP3-2VSQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_49.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, up, right, down, right, right, down, down, right, right, up, right, right, right, right, down, left, left, down, left, down, down, left, down, right, right, up, up, right, right, up, right, up, up, right, down, right, down, down, down, left, left, down, left, left, down, left, down, left, down, right, down, right, right, up, up, up, right, down, right, up, up, right, down, down, down, down, down, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oKuUafryOtGxnsEPuvytyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_49.jpg`

**Score:** 3.38%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, down, right, down, down, down, right, right, down, right, down, down, down, right, down, right, down, right, right, down, down, down, right, down, right, down, down, down, right, down, right, down, down, down, right, right, down, right, down, right, right, down, down, right, down, right, right, down, down, down, right, down, right, down, right, right, down, down, down, right, down, right, down, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,right,down,down,down,right,right,down,right,down,down,down,right,down,right,down,right,right,down,down,down,right,down,right,down,down,down,right,down,right,down,down,down,right,right,down,right,down,right,right,down,down,right,down,right,right,down,down,down,right,down,right,down,right,right,down,down,down,right,down,right,down,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o6uUaeaTGdqE7M8Pyb-HyQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_49.json`

**Score:** 1.35%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, down, down, right, down, down, right, right, down, down, down, right, right, right, down, down, down, down, right, right, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,down,down,right,right,down,down,down,right,right,right,down,down,down,down,right,right,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pKuUadm0KL3ukdUPjeSHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_49.json`

**Score:** 2.03%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, down, right, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, down, right, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, right, down, right, right, down, right, right, right, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, right, right, right, down, right, right, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,right,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,down,right,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,right,down,right,right,down,right,right,right,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,right,right,right,down,right,right,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pquUacbADcGknsEPzKbYmAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_49.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qKuUaaLMOKzzkdUPnrP0qAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_ascii_49.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='q6uUaaHDHfaHnsEPm6HKoQE' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=539,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=539
    ),
  ],
  total_token_count=539
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=539 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=539
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=539 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_49.txt`

**Score:** 2.03%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, down, down, right, right, right, right, down, down, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,down,right,right,right,right,down,down,right,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rquUaYKlDIb1kdUP6IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

