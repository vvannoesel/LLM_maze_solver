# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_47.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right` |
| `maze_line_15x15_47.json` | **0.70%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_47.json` | **0.00%** | `input: 13488 , ouput: 85` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_47.txt` | **0.70%** | `input: 3680 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_47.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, down, right, right, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right` |
| `maze_occupancy_15x15_47.jpg` | **1.41%** | `input: 431 , ouput: 650` | `down, down, right, right, down, right, down, down, right, right, down, right, right, down, left, down, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right` |
| `maze_occupancy_15x15_47.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down` |
| `maze_occupancy_15x15_adj_47.json` | **1.41%** | `input: 27620 , ouput: 57` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_47.txt` | **0.70%** | `input: 7724 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_47.txt` | **0.70%** | `input: 547 , ouput: 650` | `down, down, down, right, right, right, down, down, right, right, down, down, down, right, down, down, down, right, right, right, down, down, down, right, right, down, down, right, down, right, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, right, right, right, down, down, down, right, right, right, down, right, down, down, right, down, down, right, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, right, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, right, down, right, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, right, down, right, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right` |
| `maze_occupancy_15x15_tokenized_47.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_47.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, down, left, down, left, up, left, down, down, right, right, down, right, up, up, right, up, right, right, right, up, left, up, right, up, up, left, left, left, up, right, right, right, right, right, right, right, down, down, down, right, right, up, right, down, down, left, left, down, down, down, right, up, right, down, down, left, down, left, up, left, up, left, up, left, up, right, up, left, up, right, up, up, left, left, down, down, down, down, down, left, left, down, down, left, left, down, down, left, up, left, left, left, down, down, right, down, left, down, down, right, up, right, down, right, right, up, left, up, left, up, right, right, down, right, down, right, right, up, up, right, right, down, down, left, down, right, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, left, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RquUabGvMvminsEP9fLK0AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_47.json`

**Score:** 0.70%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, down, left, down, left, up, left, down, down, right, right, down, right, up, up, right, up, right, right, right, up, left, up, right, up, up, left, left, left, up, right, right, right, right, right, right, right, down, down, down, right, right, up, right, down, down, left, left, down, down, down, right, up, right, down, down, left, down, left, up, left, up, left, up, left, up, right, up, left, up, right, up, up, left, left, down, down, down, down, down, left, left, down, down, left, left, down, down, left, up, left, left, left, down, down, right, down, left, down, down, right, up, right, down, right, right, up, left, up, left, up, right, right, down, right, down, right, right, up, up, right, right, down, down, left, down, right, right, right, right, up, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R6uUac67H-iXkdUPtIrQkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_47.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, down, left, down, left, up, left, down, down, right, right, down, right, up, up, right, up, right, right, right, up, left, up, right, up, up, left, left, left, up, right, right, right, right, right, right, right, down, down, down, right, right, up, right, down, down, left, left, down, down, down, right, up, right, down, down, left, down, left, up, left, up, left, up, left, up, right, up, left, up, right, up, up, left, left, down, down, down, down, down, left, left, down, down, left, left, down, down, left, up, left, left, left, down, down, right, down, left, down, down, right, up, right, down, right, right, up, left, up, left, up, right, right, down, right, down, right, right, up, up, right, right, down, down, left, down, right, right, right, right, up, right, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SKuUaaGKEL3knsEP-_zhiQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=13488,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13488
    ),
  ],
  total_token_count=13573
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=13488 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13488
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13573 traffic_type=None
```

### `maze_line_15x15_adj_47.txt`

**Score:** 0.70%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, down, left, down, left, up, left, down, down, right, right, down, right, up, up, right, up, right, right, right, up, left, up, right, up, up, left, left, left, up, right, right, right, right, right, right, right, down, down, down, right, right, up, right, down, down, left, left, down, down, down, right, up, right, down, down, left, down, left, up, left, up, left, up, left, up, right, up, left, up, right, up, up, left, left, down, down, down, down, down, left, left, down, down, left, left, down, down, left, up, left, left, left, down, down, right, down, left, down, down, right, up, right, down, right, right, up, left, up, left, up, right, right, down, right, down, right, right, up, up, right, right, down, down, left, down, right, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SquUaYX2ELK7nsEPp-bmmQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3680,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3680
    ),
  ],
  total_token_count=4330
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3680 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3680
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4330 traffic_type=None
```

### `maze_line_15x15_tokenized_47.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, down, left, down, left, up, left, down, down, right, right, down, right, up, up, right, up, right, right, right, up, left, up, right, up, up, left, left, left, up, right, right, right, right, right, right, right, down, down, down, right, right, up, right, down, down, left, left, down, down, down, right, up, right, down, down, left, down, left, up, left, up, left, up, left, up, right, up, left, up, right, up, up, left, left, down, down, down, down, down, left, left, down, down, left, left, down, down, left, up, left, left, left, down, down, right, down, left, down, down, right, up, right, down, right, right, up, left, up, left, up, right, right, down, right, down, right, right, up, up, right, right, down, down, left, down, right, right, right, right, up, right, down, right
```

**Extracted Answer:**
```
right, down, right, right, down, right, right, down, right, right, down, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,right,right,down,right,right,down,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TKuUaaueFdGxnsEPuvytyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_47.jpg`

**Score:** 1.41%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, down, down, down, down, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, down, right, right, down, right, right, down, left, down, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right, right, down, left, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,right,down,down,right,right,down,right,right,down,left,down,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,right,down,left,down,right,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TquUaZLLMr-xnsEPuMqioQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_47.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, down, down, down, down, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UKuUaebgNcTV7M8PzpbtcQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_47.json`

**Score:** 1.41%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, down, down, down, down, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UquUaZcitZWewQ-X-KeJAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=27620,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27620
    ),
  ],
  total_token_count=27677
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=27620 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27620
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27677 traffic_type=None
```

### `maze_occupancy_15x15_adj_47.txt`

**Score:** 0.70%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, down, down, down, down, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UquUaej4IaeN7M8P04OMiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7724,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7724
    ),
  ],
  total_token_count=7837
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7724 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7724
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7837 traffic_type=None
```

### `maze_occupancy_15x15_ascii_47.txt`

**Score:** 0.70%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, down, down, down, down, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, down, right, right, down, down, down, right, down, down, down, right, right, right, down, down, down, right, right, down, down, right, down, right, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, right, right, right, right, right, down, down, down, right, right, right, down, right, down, down, right, down, down, right, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, right, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, right, down, right, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, right, down, right, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right, right, right, down, down, down, right, right, right, down, down, down, right, right, down, right, down, right, right, right, down, down, down, right, right, down, right, down, down, right, down, down, right, down, down, down, right, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,right,down,down,right,right,down,down,down,right,down,down,down,right,right,right,down,down,down,right,right,down,down,right,down,right,right,right,right,down,down,down,right,right,right,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,right,right,right,right,right,down,down,down,right,right,right,down,right,down,down,right,down,down,right,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,down,right,down,right,right,right,right,down,down,down,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,right,right,down,down,down,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,right,right,down,down,right,down,right,right,right,right,down,down,down,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,down,right,down,right,right,right,down,down,down,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,right,right,down,down,right,down,right,right,right,right,down,down,down,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,right,right,down,down,down,right,right,right,down,down,down,right,right,down,right,down,right,right,right,down,down,down,right,right,down,right,down,down,right,down,down,right,down,down,down,right,right,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U6uUacbNOebgnsEP3-2VSQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=547,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=547
    ),
  ],
  total_token_count=1197
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=547 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=547
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1197 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_47.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, up, up, up, up, right, right, up, up, right, right, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, left, left, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, up, up, left, left, up, up, right, right, up, up, left, left, up, up, right, right, up, up, up, up, left, left, left, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, down, down, down, down, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VauUaeX9PJ6jnsEP0cGigAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

