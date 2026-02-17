# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_27.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right` |
| `maze_line_15x15_27.json` | **0.96%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_27.json` | **0.00%** | `input: 13486 , ouput: 650` | `right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down` |
| `maze_line_15x15_adj_27.txt` | **1.92%** | `input: 3678 , ouput: 650` | `down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_27.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_27.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, left, down, left, down, left, up, left, up, right, up, left, up, left, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, left, down, left, up, left, up, right, up, left, up, left, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right` |
| `maze_occupancy_15x15_27.json` | **nan%** | `input: 4246 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_27.json` | **0.00%** | `input: 27628 , ouput: 650` | `right, right, right, right, right, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right` |
| `maze_occupancy_15x15_adj_27.txt` | **0.00%** | `input: 7730 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_ascii_27.txt` | **1.92%** | `input: 555 , ouput: 650` | `down, down, right, right, right, right, right, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_27.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_15x15_27.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, left, down, down, down, down, right, right, up, up, up, up, up, right, down, down, right, up, right, right, right, right, up, left, up, right, right, down, down, down, left, left, left, down, left, left, down, left, down, down, down, down, down, down, right, down, left, down, down, right, up, right, down, right, up, up, left, up, up, left, up, up, up, right, down, right, down, right, right, up, right, right, down, down, left, down, down, down, left, up, up, up, left, left, down, right, down, down, down, right, right, right, up, right, up, up, right, down, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,up,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jqeUaaPnNYqB7M8P4pHemAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_27.json`

**Score:** 0.96%

**Ground Truth Solution:**
```
down, right, down, left, down, down, down, down, right, right, up, up, up, up, up, right, down, down, right, up, right, right, right, right, up, left, up, right, right, down, down, down, left, left, left, down, left, left, down, left, down, down, down, down, down, down, right, down, left, down, down, right, up, right, down, right, up, up, left, up, up, left, up, up, up, right, down, right, down, right, right, up, right, right, down, down, left, down, down, down, left, up, up, up, left, left, down, right, down, down, down, right, right, right, up, right, up, up, right, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j6eUaYTUKL3ukdUPh-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_27.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, left, down, down, down, down, right, right, up, up, up, up, up, right, down, down, right, up, right, right, right, right, up, left, up, right, right, down, down, down, left, left, left, down, left, left, down, left, down, down, down, down, down, down, right, down, left, down, down, right, up, right, down, right, up, up, left, up, up, left, up, up, up, right, down, right, down, right, right, up, right, right, down, down, left, down, down, down, left, up, up, up, left, left, down, right, down, down, down, right, right, right, up, right, up, up, right, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kaeUaZ-SKYvw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=13486,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13486
    ),
  ],
  total_token_count=14136
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13486 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13486
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14136 traffic_type=None
```

### `maze_line_15x15_adj_27.txt`

**Score:** 1.92%

**Ground Truth Solution:**
```
down, right, down, left, down, down, down, down, right, right, up, up, up, up, up, right, down, down, right, up, right, right, right, right, up, left, up, right, right, down, down, down, left, left, left, down, left, left, down, left, down, down, down, down, down, down, right, down, left, down, down, right, up, right, down, right, up, up, left, up, up, left, up, up, up, right, down, right, down, right, right, up, right, right, down, down, left, down, down, down, left, up, up, up, left, left, down, right, down, down, down, right, right, right, up, right, up, up, right, down, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k6eUaZDjN4be7M8P85iEkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_27.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, right, down, left, down, down, down, down, right, right, up, up, up, up, up, right, down, down, right, up, right, right, right, right, up, left, up, right, right, down, down, down, left, left, left, down, left, left, down, left, down, down, down, down, down, down, right, down, left, down, down, right, up, right, down, right, up, up, left, up, up, left, up, up, up, right, down, right, down, right, right, up, right, right, down, down, left, down, down, down, left, up, up, up, left, left, down, right, down, down, down, right, right, right, up, right, up, up, right, down, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lqeUaYjfMYqB7M8P4pHemAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_27.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, up, up, left, left, up, up, up, up, left, left, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, left, down, left, down, left, up, left, up, right, up, left, up, left, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, left, down, left, up, left, up, right, up, left, up, left, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,left,down,left,down,left,up,left,up,right,up,left,up,left,up,right,up,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,left,down,left,up,left,up,right,up,left,up,left,up,right,up,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mKeUaZ3zJty8nsEPjZySgAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_27.json`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, up, up, left, left, up, up, up, up, left, left, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m6eUaZu4H4be7M8P85iEkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_27.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, up, up, left, left, up, up, up, up, left, left, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, down, down, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,down,down,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='naeUaaePBM_HnsEPxMXdkAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27628,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27628
    ),
  ],
  total_token_count=28278
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27628 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27628
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28278 traffic_type=None
```

### `maze_occupancy_15x15_adj_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, up, up, left, left, up, up, up, up, left, left, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down
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
        text='right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nqeUadzKNYvw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_ascii_27.txt`

**Score:** 1.92%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, up, up, left, left, up, up, up, up, left, left, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oKeUaYaEK73ukdUP_eOHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=555,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=555
    ),
  ],
  total_token_count=1205
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=555 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=555
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1205 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_27.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, up, up, left, left, up, up, up, up, left, left, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oqeUaeyiL-mekdUPoPLrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

