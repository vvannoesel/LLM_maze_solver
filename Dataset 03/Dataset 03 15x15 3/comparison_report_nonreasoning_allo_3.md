# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_3.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, right, down, left, down, right, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down` |
| `maze_line_15x15_3.json` | **0.72%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_3.json` | **0.00%** | `input: 13484 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_3.txt` | **0.00%** | `input: 3676 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down` |
| `maze_line_15x15_tokenized_3.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_15x15_3.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, right, down, right, down, down, left, down, right, right, down, right, up, right, down, down, right, down, left, down, left, down, left, up, left, up, right, up, right, up, left, up, left, down, left, up, right, up, right, down, right, up, right, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left` |
| `maze_occupancy_15x15_3.json` | **nan%** | `input: 4246 , ouput: 0` | `` |
| `maze_occupancy_15x15_3.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_3.json` | **2.17%** | `input: 27635 , ouput: 650` | `down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_3.txt` | **0.72%** | `input: 7731 , ouput: 115` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_3.txt` | **0.72%** | `input: 546 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_3.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_3.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, right, down, down, right, down, down, down, left, left, up, right, up, left, up, left, down, left, up, left, down, down, right, right, down, down, left, left, down, down, down, right, right, right, down, down, down, left, up, left, up, left, down, down, right, down, down, right, right, right, right, up, up, right, right, right, down, left, down, right, right, up, right, up, up, right, right, up, up, up, up, up, left, left, down, down, right, down, left, left, up, up, up, up, right, up, left, left, left, down, left, up, up, right, up, left, up, up, right, right, right, down, right, down, right, up, up, right, down, right, right, down, down, left, left, left, down, right, down, right, down, right, down, left, down, down, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,right,up,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CP0laZ3WI6H6xs0Pi9na8Q4' usage_metadata=GenerateContentResponseUsageMetadata(
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


### `maze_line_15x15_3.json`

**Score:** 0.72%

**Ground Truth Solution:**
```
down, right, right, up, right, right, down, down, right, down, down, down, left, left, up, right, up, left, up, left, down, left, up, left, down, down, right, right, down, down, left, left, down, down, down, right, right, right, down, down, down, left, up, left, up, left, down, down, right, down, down, right, right, right, right, up, up, right, right, right, down, left, down, right, right, up, right, up, up, right, right, up, up, up, up, up, left, left, down, down, right, down, left, left, up, up, up, up, right, up, left, left, left, down, left, up, up, right, up, left, up, up, right, right, right, down, right, down, right, up, up, right, down, right, right, down, down, left, left, left, down, right, down, right, down, right, down, left, down, down, right, down, left, down, down, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Cf0laYDIHs6BvdIPhvWKwAc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_3.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, right, down, down, right, down, down, down, left, left, up, right, up, left, up, left, down, left, up, left, down, down, right, right, down, down, left, left, down, down, down, right, right, right, down, down, down, left, up, left, up, left, down, down, right, down, down, right, right, right, right, up, up, right, right, right, down, left, down, right, right, up, right, up, up, right, right, up, up, up, up, up, left, left, down, down, right, down, left, left, up, up, up, up, right, up, left, left, left, down, left, up, up, right, up, left, up, up, right, right, right, down, right, down, right, up, up, right, down, right, right, down, down, left, left, left, down, right, down, right, down, right, down, left, down, down, right, down, left, down, down, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Cv0ladHrLJfYxs0P243yYA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=13484,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13484
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=13484 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13484
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13541 traffic_type=None
```

### `maze_line_15x15_adj_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, right, down, down, right, down, down, down, left, left, up, right, up, left, up, left, down, left, up, left, down, down, right, right, down, down, left, left, down, down, down, right, right, right, down, down, down, left, up, left, up, left, down, down, right, down, down, right, right, right, right, up, up, right, right, right, down, left, down, right, right, up, right, up, up, right, right, up, up, up, up, up, left, left, down, down, right, down, left, left, up, up, up, up, right, up, left, left, left, down, left, up, up, right, up, left, up, up, right, right, right, down, right, down, right, up, up, right, down, right, right, down, down, left, left, left, down, right, down, right, down, right, down, left, down, down, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Df0lacP3L6u7xN8PgfWXyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, right, down, down, right, down, down, down, left, left, up, right, up, left, up, left, down, left, up, left, down, down, right, right, down, down, left, left, down, down, down, right, right, right, down, down, down, left, up, left, up, left, down, down, right, down, down, right, right, right, right, up, up, right, right, right, down, left, down, right, right, up, right, up, up, right, right, up, up, up, up, up, left, left, down, down, right, down, left, left, up, up, up, up, right, up, left, left, left, down, left, up, up, right, up, left, up, up, right, right, right, down, right, down, right, up, up, right, down, right, right, down, down, left, left, left, down, right, down, right, down, right, down, left, down, down, right, down, left, down, down, down, right, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ef0laYuzFv69vdIPmfTLoQ4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_3.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, left, left, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, down, left, down, right, right, down, right, up, right, down, down, right, down, left, down, left, down, left, up, left, up, right, up, right, up, left, up, left, down, left, up, right, up, right, down, right, up, right, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, left, down, left, down, right, down, right, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,left,down,right,right,down,right,up,right,down,down,right,down,left,down,left,down,left,up,left,up,right,up,right,up,left,up,left,down,left,up,right,up,right,down,right,up,right,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,left,down,left,down,right,down,right,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FP0labOADKfaxs0PzejI8QI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_3.json`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, left, left, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F_0laZnMCc6BvdIPhvWKwAc' usage_metadata=GenerateContentResponseUsageMetadata(
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
### `maze_occupancy_15x15_3.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, left, left, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ycsmaamGGOC3xN8P-s3c8Qs' usage_metadata=GenerateContentResponseUsageMetadata(
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


### `maze_occupancy_15x15_adj_3.json`

**Score:** 2.17%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, left, left, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Gv0labObF9COvdIPkJWQ6AM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_3.txt`

**Score:** 0.72%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, left, left, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G_0lae_aFqTCvdIPwej94A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=115,
  prompt_token_count=7731,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7731
    ),
  ],
  total_token_count=7846
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=115 candidates_tokens_details=None prompt_token_count=7731 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7731
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7846 traffic_type=None
```

### `maze_occupancy_15x15_ascii_3.txt`

**Score:** 0.72%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, left, left, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Hf0lafblNLnaxs0P9PfZiA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=546,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=546
    ),
  ],
  total_token_count=1196
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=546
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1196 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down, left, left, left, left, up, up, right, right, up, up, left, left, up, up, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, up, up, right, right, up, up, up, up, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IP0labeYNaH6xs0Pi9na8Q4' usage_metadata=GenerateContentResponseUsageMetadata(
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

