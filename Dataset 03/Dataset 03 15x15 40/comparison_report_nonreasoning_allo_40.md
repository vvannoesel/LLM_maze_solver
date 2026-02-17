# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_40.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, up, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right` |
| `maze_line_15x15_40.json` | **0.85%** | `input: 9807 , ouput: 85` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_40.json` | **0.85%** | `input: 13485 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right` |
| `maze_line_15x15_adj_40.txt` | **0.85%** | `input: 3677 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_40.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_40.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right` |
| `maze_occupancy_15x15_40.json` | **0.00%** | `input: 4246 , ouput: 59` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right` |
| `maze_occupancy_15x15_adj_40.json` | **2.54%** | `input: 27641 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_40.txt` | **2.54%** | `input: 7740 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_ascii_40.txt` | **2.54%** | `input: 525 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_40.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_15x15_40.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, down, right, up, right, right, down, down, left, left, down, down, down, right, right, down, left, left, left, left, up, right, up, up, up, left, down, left, down, down, down, down, down, right, up, right, down, down, left, left, down, down, down, right, right, up, right, up, right, up, right, right, right, right, right, up, left, left, left, left, up, right, up, up, right, down, down, right, up, right, right, down, down, down, down, left, left, left, down, down, left, down, right, right, right, up, left, up, right, right, right, right, up, left, up, up, up, right, up, left, up, right, right, right, down, down, left, down, left, down, right, down, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, up, right, down, left, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,up,right,down,left,down,right,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FqmUafzUEND-nsEPgIiFuAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_40.json`

**Score:** 0.85%

**Ground Truth Solution:**
```
down, right, right, down, right, up, right, right, down, down, left, left, down, down, down, right, right, down, left, left, left, left, up, right, up, up, up, left, down, left, down, down, down, down, down, right, up, right, down, down, left, left, down, down, down, right, right, up, right, up, right, up, right, right, right, right, right, up, left, left, left, left, up, right, up, up, right, down, down, right, up, right, right, down, down, down, down, left, left, left, down, down, left, down, right, right, right, up, left, up, right, right, right, right, up, left, up, up, up, right, up, left, up, right, right, right, down, down, left, down, left, down, right, down, right, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FqmUafCkL5z07M8PqPy4oQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=9892
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9892 traffic_type=None
```

### `maze_line_15x15_adj_40.json`

**Score:** 0.85%

**Ground Truth Solution:**
```
down, right, right, down, right, up, right, right, down, down, left, left, down, down, down, right, right, down, left, left, left, left, up, right, up, up, up, left, down, left, down, down, down, down, down, right, up, right, down, down, left, left, down, down, down, right, right, up, right, up, right, up, right, right, right, right, right, up, left, left, left, left, up, right, up, up, right, down, down, right, up, right, right, down, down, down, down, left, left, left, down, down, left, down, right, right, right, up, left, up, right, right, right, right, up, left, up, up, up, right, up, left, up, right, right, right, down, down, left, down, left, down, right, down, right, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GKmUadioB9jpnsEPmcvxyAE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=13485,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13485
    ),
  ],
  total_token_count=14135
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13485 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13485
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14135 traffic_type=None
```

### `maze_line_15x15_adj_40.txt`

**Score:** 0.85%

**Ground Truth Solution:**
```
down, right, right, down, right, up, right, right, down, down, left, left, down, down, down, right, right, down, left, left, left, left, up, right, up, up, up, left, down, left, down, down, down, down, down, right, up, right, down, down, left, left, down, down, down, right, right, up, right, up, right, up, right, right, right, right, right, up, left, left, left, left, up, right, up, up, right, down, down, right, up, right, right, down, down, down, down, left, left, left, down, down, left, down, right, right, right, up, left, up, right, right, right, right, up, left, up, up, up, right, up, left, up, right, right, right, down, down, left, down, left, down, right, down, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GKmUaY-PM_minsEP9fLK0AM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=3677,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3677
    ),
  ],
  total_token_count=3732
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=3677 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3677
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3732 traffic_type=None
```

### `maze_line_15x15_tokenized_40.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, down, right, up, right, right, down, down, left, left, down, down, down, right, right, down, left, left, left, left, up, right, up, up, up, left, down, left, down, down, down, down, down, right, up, right, down, down, left, left, down, down, down, right, right, up, right, up, right, up, right, right, right, right, right, up, left, left, left, left, up, right, up, up, right, down, down, right, up, right, right, down, down, down, down, left, left, left, down, down, left, down, right, right, right, up, left, up, right, right, right, right, up, left, up, up, up, right, up, left, up, right, right, right, down, down, left, down, left, down, right, down, right, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G6mUaZC8Af27nsEPhr2MyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_40.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HamUabXmKaX07M8P2KK7sA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_40.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='H6mUacLMAob1kdUP6IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4305
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4305 traffic_type=None
```

### `maze_occupancy_15x15_adj_40.json`

**Score:** 2.54%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IamUaf3nEIb1kdUP6IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27641,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27641
    ),
  ],
  total_token_count=28291
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27641 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27641
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28291 traffic_type=None
```

### `maze_occupancy_15x15_adj_40.txt`

**Score:** 2.54%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I6mUadOKAa3hnsEPxYDs0QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7740,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7740
    ),
  ],
  total_token_count=8390
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7740 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7740
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8390 traffic_type=None
```

### `maze_occupancy_15x15_ascii_40.txt`

**Score:** 2.54%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JKmUaYnoMMeUnsEPgvzb-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=525,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=525
    ),
  ],
  total_token_count=1175
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=525 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=525
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1175 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_40.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, up, up, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, down, down, right, right, right, right, up, up, right, right, up, up, right, right, up, up, right, right, right, right, right, right, right, right, right, right, up, up, left, left, left, left, left, left, left, left, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='J6mUabOlBM37nsEP0869mQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

