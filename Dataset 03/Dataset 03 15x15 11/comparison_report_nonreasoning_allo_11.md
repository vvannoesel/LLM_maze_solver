# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_11.jpg` | **3.33%** | `input: 436 , ouput: 650` | `right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right` |
| `maze_line_15x15_11.json` | **3.33%** | `input: 9807 , ouput: 650` | `right, down, right, right, down, down, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down` |
| `maze_line_15x15_adj_11.json` | **nan%** | `input: 13487 , ouput: 0` | `` |
| `maze_line_15x15_adj_11.txt` | **nan%** | `input: 3679 , ouput: 0` | `` |
| `maze_line_15x15_tokenized_11.txt` | **2.22%** | `input: 3282 , ouput: 59` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_11.jpg` | **2.78%** | `input: 431 , ouput: 650` | `right, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, left, down, down, right, right, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left` |
| `maze_occupancy_15x15_11.json` | **nan%** | `input: 4246 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_11.json` | **3.33%** | `input: 27631 , ouput: 650` | `right, right, down, down, right, right, right, down, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_11.txt` | **0.00%** | `input: 7728 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_11.txt` | **0.00%** | `input: 552 , ouput: 650` | `down, down, right, right, right, right, down, right, down, down, down, down, down, right, right, right, right, right, right, down, right, down, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down` |
| `maze_occupancy_15x15_tokenized_11.txt` | **1.11%** | `input: 12134 , ouput: 650` | `right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_11.jpg`

**Score:** 3.33%

**Ground Truth Solution:**
```
right, down, right, up, right, right, down, right, up, right, down, down, left, down, down, down, down, right, up, right, right, down, down, left, down, left, left, up, left, up, left, up, up, right, up, up, left, left, left, down, left, down, down, down, down, down, down, right, down, down, right, up, right, down, down, left, left, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, down, right, right, up, up, up, right, down, down, right, up, right, up, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R5yUae2lM8eUnsEPgvzb-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_11.json`

**Score:** 3.33%

**Ground Truth Solution:**
```
right, down, right, up, right, right, down, right, up, right, down, down, left, down, down, down, down, right, up, right, right, down, down, left, down, left, left, up, left, up, left, up, up, right, up, up, left, left, left, down, left, down, down, down, down, down, down, right, down, down, right, up, right, down, down, left, left, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, down, right, right, up, up, up, right, down, down, right, up, right, up, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, right, down, down, right, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,down,right,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SZyUaZ_uE6zzkdUPnrP0qAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_11.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, up, right, right, down, right, up, right, down, down, left, down, down, down, down, right, up, right, right, down, down, left, down, left, left, up, left, up, left, up, up, right, up, up, left, left, left, down, left, down, down, down, down, down, down, right, down, down, right, up, right, down, down, left, left, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, down, right, right, up, up, up, right, down, down, right, up, right, up, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TJyUaZHuIdGqnsEPwL-awAE' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=13487,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13487
    ),
  ],
  total_token_count=13487
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=13487 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13487
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13487 traffic_type=None
```

### `maze_line_15x15_adj_11.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, up, right, right, down, right, up, right, down, down, left, down, down, down, down, right, up, right, right, down, down, left, down, left, left, up, left, up, left, up, up, right, up, up, left, left, left, down, left, down, down, down, down, down, down, right, down, down, right, up, right, down, down, left, left, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, down, right, right, up, up, up, right, down, down, right, up, right, up, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T5yUaf72CoqB7M8P4pHemAI' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=3679,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3679
    ),
  ],
  total_token_count=3679
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=3679 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3679
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3679 traffic_type=None
```

### `maze_line_15x15_tokenized_11.txt`

**Score:** 2.22%

**Ground Truth Solution:**
```
right, down, right, up, right, right, down, right, up, right, down, down, left, down, down, down, down, right, up, right, right, down, down, left, down, left, left, up, left, up, left, up, up, right, up, up, left, left, left, down, left, down, down, down, down, down, down, right, down, down, right, up, right, down, down, left, left, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, down, right, right, up, up, up, right, down, down, right, up, right, up, right, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T5yUaYCFNcGknsEPzKbYmAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=3282,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3282
    ),
  ],
  total_token_count=3341
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=3282 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3282
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3341 traffic_type=None
```

### `maze_occupancy_15x15_11.jpg`

**Score:** 2.78%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, left, left, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, left, down, down, right, right, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left, down, down, right, right, down, down, right, down, down, right, down, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,left,down,down,right,right,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,down,down,right,right,down,down,right,down,down,right,down,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UpyUaYreC43hnsEPj-nr0Q8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_11.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, left, left, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VZyUadXSJ5eBkdUP9--_-AI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_11.json`

**Score:** 3.33%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, left, left, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V5yUaYj6LtuXkdUPsdSSoAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27631,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27631
    ),
  ],
  total_token_count=28281
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27631 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27631
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28281 traffic_type=None
```

### `maze_occupancy_15x15_adj_11.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, left, left, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WJyUaZivM4b1kdUP6IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7728,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7728
    ),
  ],
  total_token_count=7841
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7728 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7728
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7841 traffic_type=None
```

### `maze_occupancy_15x15_ascii_11.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, left, left, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, down, right, down, down, down, down, down, right, right, right, right, right, right, down, right, down, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down, down, down, down, right, right, right, right, right, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,down,right,down,down,down,down,down,right,right,right,right,right,right,down,right,down,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,down,down,down,right,right,right,right,right,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WpyUaYfwLNjpnsEPp8vxyAE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=552,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=552
    ),
  ],
  total_token_count=1202
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=552 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=552
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1202 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_11.txt`

**Score:** 1.11%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, left, left, left, left, up, up, left, left, up, up, left, left, up, up, up, up, right, right, up, up, up, up, left, left, left, left, left, left, down, down, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XJyUaZz-Kdfu7M8Pk_6wkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

