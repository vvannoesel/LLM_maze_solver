# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_19.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, up, left, up, right, down, right, down, right, down, left, down, right, up, right, up, right, down, right, down, right, up, left, up, left, up, right, up, right, down, right, up, left, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right` |
| `maze_line_15x15_19.json` | **8.33%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_19.json` | **8.33%** | `input: 13487 , ouput: 85` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_19.txt` | **0.00%** | `input: 3679 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down` |
| `maze_line_15x15_tokenized_19.txt` | **4.17%** | `input: 3282 , ouput: 650` | `down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_19.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, right, down, right, down, right, down, left, down, right, down, right, down, left, down, left, up, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up` |
| `maze_occupancy_15x15_19.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_19.json` | **2.08%** | `input: 27632 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_19.txt` | **8.33%** | `input: 7729 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left` |
| `maze_occupancy_15x15_ascii_19.txt` | **0.00%** | `input: 535 , ouput: 650` | `this, is, a, challenging, maze!, i, will, now, trace, the, path, from, 's', to, 'e'., (0, 0), s, (1, 0), down, (2, 0), down, (3, 0), down, (4, 0), down, (5, 0), down, (6, 0), down, (7, 0), down, (8, 0), down, (9, 0), down, (10, 0), down, (11, 0), down, (12, 0), down, (13, 0), down, (14, 0), down, (15, 0), down, (16, 0), down, (17, 0), down, (18, 0), down, (19, 0), down, (20, 0), down, (21, 0), down, (22, 0), down, (23, 0), down, (24, 0), down, (25, 0), down, (26, 0), down, (27, 0), down, (28, 0), down, (29, 0), down, (29, 1), right, (29, 2), right, (29, 3), right, (28, 3), up, (27, 3), up, (26, 3), up, (25, 3), up, (24, 3), up, (23, 3), up, (22, 3), up, (21, 3), up, (20, 3), up, (19, 3), up, (18, 3), up, (17, 3), up, (16, 3), up, (15, 3), up, (14, 3), up, (13, 3), up, (12, 3), up, (11, 3), up, (10, 3), up, (9, 3), up, (8, 3), up, (7, 3), up, (6, 3), up, (5, 3), up, (4, 3), up, (3, 3), up, (2, 3), up, (1, 3), up, (1, 4), right, (1, 5), right, (1, 6), right, (1, 7), right, (1, 8), right, (1, 9), right, (1, 10), right, (1, 11), right, (1, 12), right, (1, 13), right, (1, 14), right, (1, 15), right, (1, 16), right, (1, 17), right, (1, 18), right, (1, 19), right, (1, 20), right, (1, 21), right, (1, 22), right, (1, 23), right, (1, 24)` |
| `maze_occupancy_15x15_tokenized_19.txt` | **0.00%** | `input: 12134 , ouput: 119` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_19.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, up, up, up, right, up, right, down, down, right, up, right, right, up, right, right, down, right, right, right, right, down, down, down, left, down, right, down, down, left, left, down, down, right, right, down, left, down, down, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, up, left, up, right, down, right, down, right, down, left, down, right, up, right, up, right, down, right, down, right, up, left, up, left, up, right, up, right, down, right, up, left, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, left, down, left, down, right, down, left, down, right, up, right, down, right, up, left, up, left, up, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,up,right,up,left,up,right,down,right,down,right,down,left,down,right,up,right,up,right,down,right,down,right,up,left,up,left,up,right,up,right,down,right,up,left,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,left,down,left,down,right,down,left,down,right,up,right,down,right,up,left,up,left,up,right,up,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KKaUafXyGo3hnsEPj-nr0Q8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_19.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, up, up, up, right, up, right, down, down, right, up, right, right, up, right, right, down, right, right, right, right, down, down, down, left, down, right, down, down, left, left, down, down, right, right, down, left, down, down, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KKaUacu2NominsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_19.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, up, up, up, right, up, right, down, down, right, up, right, right, up, right, right, down, right, right, right, right, down, down, down, left, down, right, down, down, left, left, down, down, right, right, down, left, down, down, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KaaUafmvJMSzkdUP4ZaoqQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=85,
  prompt_token_count=13487,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13487
    ),
  ],
  total_token_count=13572
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=85 candidates_tokens_details=None prompt_token_count=13487 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13487
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13572 traffic_type=None
```

### `maze_line_15x15_adj_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, up, up, up, right, up, right, down, down, right, up, right, right, up, right, right, down, right, right, right, right, down, down, down, left, down, right, down, down, left, left, down, down, right, right, down, left, down, down, right, down, down
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
        text='right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K6aUabiTIbWVnsEPl_iniQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3679,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3679
    ),
  ],
  total_token_count=4329
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3679 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3679
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4329 traffic_type=None
```

### `maze_line_15x15_tokenized_19.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, up, up, up, right, up, right, down, down, right, up, right, right, up, right, right, down, right, right, right, right, down, down, down, left, down, right, down, down, left, left, down, down, right, right, down, left, down, down, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LaaUacL9Ir3ukdUPh-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_19.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, right, down, left, down, right, down, right, down, left, down, left, up, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up, right, up, right, up, left, up, right, down, right, down, left, down, left, down, right, down, right, down, right, down, left, down, left, up, left, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,right,down,left,down,right,down,right,down,left,down,left,up,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,right,up,right,up,left,up,right,down,right,down,left,down,left,down,right,down,right,down,right,down,left,down,left,up,left,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MKaUaeCoDuOXkdUPwKDLyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_19.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MaaUaeP6H8_HnsEPxMXdkAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_19.json`

**Score:** 2.08%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M6aUaaaBEc37nsEP0869mQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27632,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27632
    ),
  ],
  total_token_count=28282
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27632 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27632
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28282 traffic_type=None
```

### `maze_occupancy_15x15_adj_19.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NKaUaY6ULP27nsEPhr2MyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7729
    ),
  ],
  total_token_count=8379
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8379 traffic_type=None
```

### `maze_occupancy_15x15_ascii_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
this, is, a, challenging, maze!, i, will, now, trace, the, path, from, 's', to, 'e'., (0, 0), s, (1, 0), down, (2, 0), down, (3, 0), down, (4, 0), down, (5, 0), down, (6, 0), down, (7, 0), down, (8, 0), down, (9, 0), down, (10, 0), down, (11, 0), down, (12, 0), down, (13, 0), down, (14, 0), down, (15, 0), down, (16, 0), down, (17, 0), down, (18, 0), down, (19, 0), down, (20, 0), down, (21, 0), down, (22, 0), down, (23, 0), down, (24, 0), down, (25, 0), down, (26, 0), down, (27, 0), down, (28, 0), down, (29, 0), down, (29, 1), right, (29, 2), right, (29, 3), right, (28, 3), up, (27, 3), up, (26, 3), up, (25, 3), up, (24, 3), up, (23, 3), up, (22, 3), up, (21, 3), up, (20, 3), up, (19, 3), up, (18, 3), up, (17, 3), up, (16, 3), up, (15, 3), up, (14, 3), up, (13, 3), up, (12, 3), up, (11, 3), up, (10, 3), up, (9, 3), up, (8, 3), up, (7, 3), up, (6, 3), up, (5, 3), up, (4, 3), up, (3, 3), up, (2, 3), up, (1, 3), up, (1, 4), right, (1, 5), right, (1, 6), right, (1, 7), right, (1, 8), right, (1, 9), right, (1, 10), right, (1, 11), right, (1, 12), right, (1, 13), right, (1, 14), right, (1, 15), right, (1, 16), right, (1, 17), right, (1, 18), right, (1, 19), right, (1, 20), right, (1, 21), right, (1, 22), right, (1, 23), right, (1, 24)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""This is a challenging maze! I will now trace the path from 'S' to 'E'.

(0,0) S
(1,0) Down
(2,0) Down
(3,0) Down
(4,0) Down
(5,0) Down
(6,0) Down
(7,0) Down
(8,0) Down
(9,0) Down
(10,0) Down
(11,0) Down
(12,0) Down
(13,0) Down
(14,0) Down
(15,0) Down
(16,0) Down
(17,0) Down
(18,0) Down
(19,0) Down
(20,0) Down
(21,0) Down
(22,0) Down
(23,0) Down
(24,0) Down
(25,0) Down
(26,0) Down
(27,0) Down
(28,0) Down
(29,0) Down
(29,1) Right
(29,2) Right
(29,3) Right
(28,3) Up
(27,3) Up
(26,3) Up
(25,3) Up
(24,3) Up
(23,3) Up
(22,3) Up
(21,3) Up
(20,3) Up
(19,3) Up
(18,3) Up
(17,3) Up
(16,3) Up
(15,3) Up
(14,3) Up
(13,3) Up
(12,3) Up
(11,3) Up
(10,3) Up
(9,3) Up
(8,3) Up
(7,3) Up
(6,3) Up
(5,3) Up
(4,3) Up
(3,3) Up
(2,3) Up
(1,3) Up
(1,4) Right
(1,5) Right
(1,6) Right
(1,7) Right
(1,8) Right
(1,9) Right
(1,10) Right
(1,11) Right
(1,12) Right
(1,13) Right
(1,14) Right
(1,15) Right
(1,16) Right
(1,17) Right
(1,18) Right
(1,19) Right
(1,20) Right
(1,21) Right
(1,22) Right
(1,23) Right
(1,24)"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NqaUaY2uIarw7M8Pw5-qsA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=535,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=535
    ),
  ],
  total_token_count=1185
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=535 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=535
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1185 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_19.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='N6aUae68FObgnsEP6p2VqQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=119,
  prompt_token_count=12134,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=12134
    ),
  ],
  total_token_count=12253
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=119 candidates_tokens_details=None prompt_token_count=12134 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=12134
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=12253 traffic_type=None
```

