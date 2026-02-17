# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_23.jpg` | **5.77%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right` |
| `maze_line_15x15_23.json` | **3.85%** | `input: 9807 , ouput: 650` | `right, down, down, down, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_23.json` | **nan%** | `input: 13488 , ouput: 0` | `` |
| `maze_line_15x15_adj_23.txt` | **1.92%** | `input: 3680 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_23.txt` | **nan%** | `input: 3283 , ouput: 0` | `` |
| `maze_occupancy_15x15_23.jpg` | **0.96%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right` |
| `maze_occupancy_15x15_23.json` | **nan%** | `input: 4246 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_23.json` | **nan%** | `input: 27630 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_23.txt` | **0.00%** | `input: 7727 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_23.txt` | **2.88%** | `input: 574 , ouput: 650` | `right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right` |
| `maze_occupancy_15x15_tokenized_23.txt` | **3.85%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_15x15_23.jpg`

**Score:** 5.77%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, right, right, down, right, up, right, down, right, up, right, right, down, down, left, left, left, left, down, down, down, down, down, right, down, down, down, down, right, up, up, right, right, down, down, left, down, down, down, right, up, up, right, down, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n6aUaZ6rAeOXkdUPwKDLyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_23.json`

**Score:** 3.85%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, right, right, down, right, up, right, down, right, up, right, right, down, down, left, left, left, left, down, down, down, down, down, right, down, down, down, down, right, up, up, right, right, down, down, left, down, down, down, right, up, up, right, down, right, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oKaUaYTZGZn7nsEP24btcA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_23.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, right, right, down, right, up, right, down, right, up, right, right, down, down, left, left, left, left, down, down, down, down, down, right, down, down, down, down, right, up, up, right, right, down, down, left, down, down, down, right, up, up, right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o6aUaYShHK3hnsEP0oDs0QE' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=13488,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13488
    ),
  ],
  total_token_count=13488
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=13488 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13488
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13488 traffic_type=None
```

### `maze_line_15x15_adj_23.txt`

**Score:** 1.92%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, right, right, down, right, up, right, down, right, up, right, right, down, down, left, left, left, left, down, down, down, down, down, right, down, down, down, down, right, up, up, right, right, down, down, left, down, down, down, right, up, up, right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='paaUac6NEarw7M8Pw5-qsA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_23.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, right, right, down, right, up, right, down, right, up, right, right, down, down, left, left, left, left, down, down, down, down, down, right, down, down, down, down, right, up, up, right, right, down, down, left, down, down, down, right, up, up, right, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='p6aUadiANumekdUPuPLrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=3283,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3283
    ),
  ],
  total_token_count=3283
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=3283 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3283
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3283 traffic_type=None
```

### `maze_occupancy_15x15_23.jpg`

**Score:** 0.96%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qqaUadznDJqAkdUP4OXyyQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_23.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rKaUaZvUMLWVnsEPl_iniQI' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4246
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4246 traffic_type=None
```

### `maze_occupancy_15x15_adj_23.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='r6aUacmwFqeN7M8Pq5OaoQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=27630,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27630
    ),
  ],
  total_token_count=27630
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=27630 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27630
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27630 traffic_type=None
```

### `maze_occupancy_15x15_adj_23.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='saaUafuqC8eUnsEPgvzb-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_ascii_23.txt`

**Score:** 2.88%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right, right, right, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,right,right,down,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sqaUaYDMHND-nsEPgIiFuAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=574,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=574
    ),
  ],
  total_token_count=1224
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=574 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=574
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1224 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_23.txt`

**Score:** 3.85%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='s6aUacWJL6DxnsEP86zG2AI' usage_metadata=GenerateContentResponseUsageMetadata(
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

