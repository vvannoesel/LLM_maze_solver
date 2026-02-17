# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_15.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right` |
| `maze_line_15x15_15.json` | **6.25%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_15.json` | **6.25%** | `input: 13484 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_15.txt` | **6.25%** | `input: 3676 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right` |
| `maze_line_15x15_tokenized_15.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right` |
| `maze_occupancy_15x15_15.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left` |
| `maze_occupancy_15x15_15.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, right, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down` |
| `maze_occupancy_15x15_adj_15.json` | **1.25%** | `input: 27635 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_15.txt` | **6.25%** | `input: 7731 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left` |
| `maze_occupancy_15x15_ascii_15.txt` | **0.00%** | `input: 533 , ouput: 650` | `right, right, right, right, right, right, right, right, down, right, down, down, down, down, down, right, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_15.txt` | **0.00%** | `input: 12134 , ouput: 179` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_15x15_15.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, right, right, right, up, left, up, left, up, up, right, down, right, right, up, right, right, up, right, down, right, up, right, right, down, right, right, down, right, down, down, down, right, down, down, down, left, up, up, left, left, down, down, left, up, left, left, left, down, right, right, down, left, down, right, down, right, up, up, right, down, right, up, right, down, right, down, down, left, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,left,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B6SUadHYOKOrnsEP8_bgmQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_15.json`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, down, down, down, right, right, right, up, left, up, left, up, up, right, down, right, right, up, right, right, up, right, down, right, up, right, right, down, right, right, down, right, down, down, down, right, down, down, down, left, up, up, left, left, down, down, left, up, left, left, left, down, right, right, down, left, down, right, down, right, up, up, right, down, right, up, right, down, right, down, down, left, left, down, down, right, up, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CKSUacSNLJTlnsEP9NTwiQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_15.json`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, down, down, down, right, right, right, up, left, up, left, up, up, right, down, right, right, up, right, right, up, right, down, right, up, right, right, down, right, right, down, right, down, down, down, right, down, down, down, left, up, up, left, left, down, down, left, up, left, left, left, down, right, right, down, left, down, right, down, right, up, up, right, down, right, up, right, down, right, down, down, left, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CaSUaZ63Jr-NkdUPkILV0AM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=13484,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13484
    ),
  ],
  total_token_count=13597
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=13484 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13484
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13597 traffic_type=None
```

### `maze_line_15x15_adj_15.txt`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, down, down, down, right, right, right, up, left, up, left, up, up, right, down, right, right, up, right, right, up, right, down, right, up, right, right, down, right, right, down, right, down, down, down, right, down, down, down, left, up, up, left, left, down, down, left, up, left, left, left, down, right, right, down, left, down, right, down, right, up, up, right, down, right, up, right, down, right, down, down, left, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CqSUaeDJNKOrnsEP8_bgmQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3676,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3676
    ),
  ],
  total_token_count=4326
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3676 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3676
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4326 traffic_type=None
```

### `maze_line_15x15_tokenized_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, right, right, right, up, left, up, left, up, up, right, down, right, right, up, right, right, up, right, down, right, up, right, right, down, right, right, down, right, down, down, down, right, down, down, down, left, up, up, left, left, down, down, left, up, left, left, left, down, right, right, down, left, down, right, down, right, up, up, right, down, right, up, right, down, right, down, down, left, left, down, down, right, up, right, down
```

**Extracted Answer:**
```
right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DKSUadS9I4minsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_15.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='D6SUabrYNLGqnsEPso7fsQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_15.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EaSUafDnBoWjnsEPtLnfyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_15.json`

**Score:** 1.25%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='E6SUaYKtEo3hnsEPj-nr0Q8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27635,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27635
    ),
  ],
  total_token_count=28285
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27635 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27635
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28285 traffic_type=None
```

### `maze_occupancy_15x15_adj_15.txt`

**Score:** 6.25%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FaSUadjvCYbe7M8P85iEkAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7731,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7731
    ),
  ],
  total_token_count=8381
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7731 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7731
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8381 traffic_type=None
```

### `maze_occupancy_15x15_ascii_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, right, down, down, down, down, down, right, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,right,down,down,down,down,down,right,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F6SUaYvnAemekdUPq_LrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=533,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=533
    ),
  ],
  total_token_count=1183
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=533 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=533
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1183 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, left, left, up, up, left, left, left, left, left, left, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F6SUaYHmPI3hnsEPj-nr0Q8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=179,
  prompt_token_count=12134,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=12134
    ),
  ],
  total_token_count=12313
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=179 candidates_tokens_details=None prompt_token_count=12134 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=12134
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=12313 traffic_type=None
```

