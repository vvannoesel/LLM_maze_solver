# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_33.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_line_15x15_33.json` | **1.06%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_33.json` | **1.06%** | `input: 13488 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_33.txt` | **0.00%** | `input: 3680 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_33.txt` | **0.00%** | `input: 3283 , ouput: 650` | `right, right, down, right, down, right, down, right, right, down, left, down, right, down, right, down, right, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down` |
| `maze_occupancy_15x15_33.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right` |
| `maze_occupancy_15x15_33.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_33.json` | **3.19%** | `input: 27636 , ouput: 117` | `down, down, right, right, right, right, right, down, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_33.txt` | **0.00%** | `input: 7736 , ouput: 650` | `right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right` |
| `maze_occupancy_15x15_ascii_33.txt` | **1.06%** | `input: 525 , ouput: 650` | `down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_33.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_33.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, right, right, down, left, down, down, right, up, right, up, up, right, down, right, right, up, right, down, right, right, down, left, left, left, down, left, down, left, up, left, down, down, right, down, left, left, left, left, up, right, right, up, left, left, up, left, up, left, down, left, down, down, right, down, left, down, down, down, down, right, down, right, up, up, up, up, right, down, right, down, right, right, right, right, right, right, down, left, down, right, right, down, down, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1767,
        license='',
        start_index=222,
        uri='https://americanarchive.org/catalog/cpb-aacip-b6e75cd0ce5'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,up,right,up,right,up,right,up,right,up,right,up,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R6iUacCZDZ6jnsEP0cGigAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_33.json`

**Score:** 1.06%

**Ground Truth Solution:**
```
down, right, right, up, right, right, right, down, left, down, down, right, up, right, up, up, right, down, right, right, up, right, down, right, right, down, left, left, left, down, left, down, left, up, left, down, down, right, down, left, left, left, left, up, right, right, up, left, left, up, left, up, left, down, left, down, down, right, down, left, down, down, down, down, right, down, right, up, up, up, up, right, down, right, down, right, right, right, right, right, right, down, left, down, right, right, down, down, right, down, right, up, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R6iUabKzOrnu7M8P587SoAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_33.json`

**Score:** 1.06%

**Ground Truth Solution:**
```
down, right, right, up, right, right, right, down, left, down, down, right, up, right, up, up, right, down, right, right, up, right, down, right, right, down, left, left, left, down, left, down, left, up, left, down, down, right, down, left, left, left, left, up, right, right, up, left, left, up, left, up, left, down, left, down, down, right, down, left, down, down, down, down, right, down, right, up, up, up, up, right, down, right, down, right, right, right, right, right, right, down, left, down, right, right, down, down, right, down, right, up, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SKiUaeK7HemekdUPuPLrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=13488,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13488
    ),
  ],
  total_token_count=13543
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=13488 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13488
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13543 traffic_type=None
```

### `maze_line_15x15_adj_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, right, right, down, left, down, down, right, up, right, up, up, right, down, right, right, up, right, down, right, right, down, left, left, left, down, left, down, left, up, left, down, down, right, down, left, left, left, left, up, right, right, up, left, left, up, left, up, left, down, left, down, down, right, down, left, down, down, down, down, right, down, right, up, up, up, up, right, down, right, down, right, right, right, right, right, right, down, left, down, right, right, down, down, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SqiUab-cFLOlnsEPjtai8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, right, right, down, left, down, down, right, up, right, up, up, right, down, right, right, up, right, down, right, right, down, left, left, left, down, left, down, left, up, left, down, down, right, down, left, left, left, left, up, right, right, up, left, left, up, left, up, left, down, left, down, down, right, down, left, down, down, down, down, right, down, right, up, up, up, up, right, down, right, down, right, right, right, right, right, right, down, left, down, right, right, down, down, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, right, down, right, down, right, down, right, right, down, left, down, right, down, right, down, right, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,right,down,right,right,down,left,down,right,down,right,down,right,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TKiUaZGoDty8nsEPjZySgAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3283,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3283
    ),
  ],
  total_token_count=3933
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3283 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3283
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3933 traffic_type=None
```

### `maze_occupancy_15x15_33.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TqiUabT7Jf3onsEP3cCnyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_33.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UKiUacPKIuesnsEPyseT6QE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_33.json`

**Score:** 3.19%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, down, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,down,right,right,right,right,down,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UaiUaYjNKemekdUPoPLrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=117,
  prompt_token_count=27636,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27636
    ),
  ],
  total_token_count=27753
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=117 candidates_tokens_details=None prompt_token_count=27636 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27636
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27753 traffic_type=None
```

### `maze_occupancy_15x15_adj_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U6iUadCFL4minsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7736,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7736
    ),
  ],
  total_token_count=8386
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7736 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7736
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8386 traffic_type=None
```

### `maze_occupancy_15x15_ascii_33.txt`

**Score:** 1.06%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VaiUacr7L4minsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_tokenized_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, up, up, up, up, right, right, down, down, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, left, left, left, left, left, left, up, up, right, right, right, right, up, up, left, left, left, left, up, up, left, left, up, up, left, left, down, down, left, left, down, down, down, down, right, right, down, down, left, left, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, up, up, up, up, up, up, right, right, down, down, right, right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, left, left, down, down, right, right, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V6iUabzvEb3ukdUP_eOHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

