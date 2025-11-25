# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_10.jpg` | **10.87%** | `input: 436 , ouput: 650` | `right, down, right, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, up, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down` |
| `maze_line_15x15_10.json` | **nan%** | `input: 9807 , ouput: 0` | `` |
| `maze_line_15x15_adj_10.json` | **2.17%** | `input: 13490 , ouput: 85` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_10.txt` | **2.17%** | `input: 3682 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_10.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_10.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_10.json` | **1.09%** | `input: 4246 , ouput: 650` | `right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right` |
| `maze_occupancy_15x15_adj_10.json` | **8.70%** | `input: 27630 , ouput: 650` | `right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_10.txt` | **0.00%** | `input: 7727 , ouput: 650` | `down, down, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_ascii_10.txt` | **3.26%** | `input: 539 , ouput: 650` | `right, right, down, right, right, down, right, right, right, right, right, down, down, right, right, down, down, right, right, right, right, right, right, down, down, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, down, down, right, down, right, down, right, right, right, down, down, down, down, right, right, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down` |
| `maze_occupancy_15x15_tokenized_10.txt` | **4.35%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_10.jpg`

**Score:** 10.87%

**Ground Truth Solution:**
```
right, down, right, right, down, down, down, left, left, down, left, down, right, down, right, up, right, down, right, right, right, right, up, right, right, down, right, down, down, down, left, left, down, down, right, down, right, down, right, up, up, right, down, right, right, down
```

**Extracted Answer:**
```
right, down, right, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, up, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, right, down, right, down, down, right, down, right, down, right, down, down, right, down, right, up, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down, right, down, down, right, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8_4laf-0GuinkdUPma66wA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_10.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, right, down, down, down, left, left, down, left, down, right, down, right, up, right, down, right, right, right, right, up, right, right, down, right, down, down, down, left, left, down, down, right, down, right, down, right, up, up, right, down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9_4laeiEGt36nsEPgoPD8A0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_10.json`

**Score:** 2.17%

**Ground Truth Solution:**
```
right, down, right, right, down, down, down, left, left, down, left, down, right, down, right, up, right, down, right, right, right, right, up, right, right, down, right, down, down, down, left, left, down, down, right, down, right, down, right, up, up, right, down, right, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-P4laeqYK4-qnsEPpOvUgA4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=13490,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13490
    ),
  ],
  total_token_count=13575
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=13490 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13490
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13575 traffic_type=None
```

### `maze_line_15x15_adj_10.txt`

**Score:** 2.17%

**Ground Truth Solution:**
```
right, down, right, right, down, down, down, left, left, down, left, down, right, down, right, up, right, down, right, right, right, right, up, right, right, down, right, down, down, down, left, left, down, down, right, down, right, down, right, up, up, right, down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-_4lad7aGezgkdUP4vSTWA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3682,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3682
    ),
  ],
  total_token_count=4332
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3682 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3682
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4332 traffic_type=None
```

### `maze_line_15x15_tokenized_10.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, right, down, down, down, left, left, down, left, down, right, down, right, up, right, down, right, right, right, right, up, right, right, down, right, down, down, down, left, left, down, down, right, down, right, down, right, up, up, right, down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_v4laaD6HryGkdUPssCgQQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_10.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='A_8laZfDGvjMkdUPy-PZSQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_10.json`

**Score:** 1.09%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Bf8laZOYLryFkdUP_qS9QA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_10.json`

**Score:** 8.70%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CP8lafqYIs64nsEPvd3zWA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27630,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27630
    ),
  ],
  total_token_count=28280
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27630 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27630
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28280 traffic_type=None
```

### `maze_occupancy_15x15_adj_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='C_8labTPGJXensEP7oWu-A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7727,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7727
    ),
  ],
  total_token_count=8377
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7727 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7727
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8377 traffic_type=None
```

### `maze_occupancy_15x15_ascii_10.txt`

**Score:** 3.26%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, down, right, right, right, right, right, down, down, right, right, down, down, right, right, right, right, right, right, down, down, down, right, right, right, down, right, down, right, down, right, down, right, right, right, down, down, down, right, down, right, down, right, right, right, down, down, down, down, right, right, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down, right, right, down, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,right,right,right,right,right,down,down,right,right,down,down,right,right,right,right,right,right,down,down,down,right,right,right,down,right,down,right,down,right,down,right,right,right,down,down,down,right,down,right,down,right,right,right,down,down,down,down,right,right,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,right,down,down,right,right,down,right,right,down,right,right,down,right,right,down,right,down,down,down,right,right,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,down,down,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,down,down,right,right,down,right,right,down,right,right,down,right,right,down,right,right,down,right,down,down,down,right,right,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,down,down,right,right,down,right,right,down,right,right,down,right,right,down,right,right,down,right,down,down,down,right,right,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,down,down,right,right,down,right,right,down,right,right,down,right,right,down,right,right,down,right,down,down,down,right,right,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='D_8labOcApXensEP7oWu-A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=539,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=539
    ),
  ],
  total_token_count=1189
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=539 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=539
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1189 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_10.txt`

**Score:** 4.35%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, down, down, down, down, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ef8labCfEvXPnsEPh-7RQQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

