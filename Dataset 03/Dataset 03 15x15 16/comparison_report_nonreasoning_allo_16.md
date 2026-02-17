# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_16.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right` |
| `maze_line_15x15_16.json` | **3.28%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_16.json` | **0.00%** | `input: 13492 , ouput: 650` | `right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down` |
| `maze_line_15x15_adj_16.txt` | **3.28%** | `input: 3684 , ouput: 57` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_16.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, right, right, down, down, down, right, down, right, right, right, down, right, down, down, right, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down` |
| `maze_occupancy_15x15_16.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_16.json` | **0.00%** | `input: 4246 , ouput: 57` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_16.json` | **0.82%** | `input: 27634 , ouput: 650` | `down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right` |
| `maze_occupancy_15x15_adj_16.txt` | **3.28%** | `input: 7730 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_16.txt` | **3.28%** | `input: 557 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_16.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_15x15_16.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, up, right, down, down, down, left, left, left, down, right, right, down, left, left, down, right, right, right, up, right, up, right, up, left, up, up, up, up, right, right, up, right, up, up, up, up, up, up, right, down, right, right, up, right, down, right, down, down, right, down, down, down, right, down, down, left, down, left, up, left, down, left, up, up, right, up, up, left, down, left, up, up, left, down, down, down, right, down, left, down, left, up, left, down, down, down, down, right, down, left, down, right, right, up, right, right, up, up, right, up, right, down, right, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I6SUaZOMDPaHnsEPm6HKoQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_16.json`

**Score:** 3.28%

**Ground Truth Solution:**
```
down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, up, right, down, down, down, left, left, left, down, right, right, down, left, left, down, right, right, right, up, right, up, right, up, left, up, up, up, up, right, right, up, right, up, up, up, up, up, up, right, down, right, right, up, right, down, right, down, down, right, down, down, down, right, down, down, left, down, left, up, left, down, left, up, up, right, up, up, left, down, left, up, up, left, down, down, down, right, down, left, down, left, up, left, down, down, down, down, right, down, left, down, right, right, up, right, right, up, up, right, up, right, down, right, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JKSUac2HAv27nsEPhr2MyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_16.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, up, right, down, down, down, left, left, left, down, right, right, down, left, left, down, right, right, right, up, right, up, right, up, left, up, up, up, up, right, right, up, right, up, up, up, up, up, up, right, down, right, right, up, right, down, right, down, down, right, down, down, down, right, down, down, left, down, left, up, left, down, left, up, up, right, up, up, left, down, left, up, up, left, down, down, down, right, down, left, down, left, up, left, down, down, down, down, right, down, left, down, right, right, up, right, right, up, up, right, up, right, down, right, right, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down, right, right, right, down, down, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,right,right,right,down,down,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JqSUacnLIbWVnsEPl_iniQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=13492,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13492
    ),
  ],
  total_token_count=14142
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13492 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13492
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14142 traffic_type=None
```

### `maze_line_15x15_adj_16.txt`

**Score:** 3.28%

**Ground Truth Solution:**
```
down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, up, right, down, down, down, left, left, left, down, right, right, down, left, left, down, right, right, right, up, right, up, right, up, left, up, up, up, up, right, right, up, right, up, up, up, up, up, up, right, down, right, right, up, right, down, right, down, down, right, down, down, down, right, down, down, left, down, left, up, left, down, left, up, up, right, up, up, left, down, left, up, up, left, down, down, down, right, down, left, down, left, up, left, down, down, down, down, right, down, left, down, right, right, up, right, right, up, up, right, up, right, down, right, right, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='J6SUaYfiBITv7M8P2pmO8AE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=3684,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3684
    ),
  ],
  total_token_count=3741
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=3684 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3684
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3741 traffic_type=None
```

### `maze_line_15x15_tokenized_16.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, down, down, down, left, down, right, down, down, right, up, up, right, down, down, down, left, left, left, down, right, right, down, left, left, down, right, right, right, up, right, up, right, up, left, up, up, up, up, right, right, up, right, up, up, up, up, up, up, right, down, right, right, up, right, down, right, down, down, right, down, down, down, right, down, down, left, down, left, up, left, down, left, up, up, right, up, up, left, down, left, up, up, left, down, down, down, right, down, left, down, left, up, left, down, down, down, down, right, down, left, down, right, right, up, right, right, up, up, right, up, right, down, right, right, down, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, right, down, right, right, right, down, right, down, down, right, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,right,down,right,right,right,down,right,down,down,right,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KKSUaZT3FYvw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_16.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KqSUaaelOubgnsEP6p2VqQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_16.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K6SUafa0JL-xnsEPuMqioQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4303
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4303 traffic_type=None
```

### `maze_occupancy_15x15_adj_16.json`

**Score:** 0.82%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LqSUaeWRFKqEkdUPzIWYoAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27634,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27634
    ),
  ],
  total_token_count=28284
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27634 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27634
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28284 traffic_type=None
```

### `maze_occupancy_15x15_adj_16.txt`

**Score:** 3.28%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MKSUacrgE7DHnsEPzv7l8QE' usage_metadata=GenerateContentResponseUsageMetadata(
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


### `maze_occupancy_15x15_ascii_16.txt`

**Score:** 3.28%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zqSUaeGBAbnu7M8P587SoAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=557,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=557
    ),
  ],
  total_token_count=1207
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=557 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=557
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1207 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_16.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, up, up, left, left, up, up, up, up, up, up, up, up, right, right, right, right, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, up, up, left, left, down, down, down, down, down, down, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, right, right, up, up, up, up, right, right, up, up, right, right, down, down, right, right, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0KSUaeq_A5TlnsEP9NTwiQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

