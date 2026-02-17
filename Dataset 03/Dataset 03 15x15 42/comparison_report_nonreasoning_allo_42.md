# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_42.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_line_15x15_42.json` | **1.45%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_42.json` | **1.45%** | `input: 13486 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right` |
| `maze_line_15x15_adj_42.txt` | **1.45%** | `input: 3678 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_42.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_42.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_42.json` | **0.00%** | `input: 4246 , ouput: 59` | `right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down` |
| `maze_occupancy_15x15_adj_42.json` | **0.00%** | `input: 27629 , ouput: 650` | `right, right, right, down, right, right, down, down, right, right, right, down, down, down, right, right, down, down, right, right, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right` |
| `maze_occupancy_15x15_adj_42.txt` | **1.45%** | `input: 7731 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_42.txt` | **0.00%** | `input: 556 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, down, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_42.txt` | **0.00%** | `input: 12134 , ouput: 121` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_42.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, left, left, down, right, down, down, down, right, down, down, left, up, left, down, down, down, down, down, right, up, up, up, right, down, right, right, right, right, down, left, left, left, down, left, down, right, right, right, right, right, right, right, right, up, right, up, left, left, left, down, left, up, up, up, left, left, up, up, up, left, up, left, up, right, up, up, up, left, up, up, right, right, down, down, down, down, down, right, up, right, right, down, left, down, down, down, right, right, up, left, up, right, up, right, up, right, up, up, up, up, right, down, down, down, down, right, down, right, down, down, left, up, left, up, left, down, down, right, down, left, down, left, down, down, right, up, right, down, down, down, right, right, down
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1777,
        license='',
        start_index=210,
        uri='https://americanarchive.org/catalog/cpb-aacip-b6e75cd0ce5'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SqmUaeCrCf3onsEP3cCnyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_42.json`

**Score:** 1.45%

**Ground Truth Solution:**
```
down, down, right, right, down, left, left, down, right, down, down, down, right, down, down, left, up, left, down, down, down, down, down, right, up, up, up, right, down, right, right, right, right, down, left, left, left, down, left, down, right, right, right, right, right, right, right, right, up, right, up, left, left, left, down, left, up, up, up, left, left, up, up, up, left, up, left, up, right, up, up, up, left, up, up, right, right, down, down, down, down, down, right, up, right, right, down, left, down, down, down, right, right, up, left, up, right, up, right, up, right, up, up, up, up, right, down, down, down, down, right, down, right, down, down, left, up, left, up, left, down, down, right, down, left, down, left, down, down, right, up, right, down, down, down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SqmUaanuNZTlnsEP9NTwiQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_42.json`

**Score:** 1.45%

**Ground Truth Solution:**
```
down, down, right, right, down, left, left, down, right, down, down, down, right, down, down, left, up, left, down, down, down, down, down, right, up, up, up, right, down, right, right, right, right, down, left, left, left, down, left, down, right, right, right, right, right, right, right, right, up, right, up, left, left, left, down, left, up, up, up, left, left, up, up, up, left, up, left, up, right, up, up, up, left, up, up, right, right, down, down, down, down, down, right, up, right, right, down, left, down, down, down, right, right, up, left, up, right, up, right, up, right, up, up, up, up, right, down, down, down, down, right, down, right, down, down, left, up, left, up, left, down, down, right, down, left, down, left, down, down, right, up, right, down, down, down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TamUaZumGYWjnsEPtLnfyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_42.txt`

**Score:** 1.45%

**Ground Truth Solution:**
```
down, down, right, right, down, left, left, down, right, down, down, down, right, down, down, left, up, left, down, down, down, down, down, right, up, up, up, right, down, right, right, right, right, down, left, left, left, down, left, down, right, right, right, right, right, right, right, right, up, right, up, left, left, left, down, left, up, up, up, left, left, up, up, up, left, up, left, up, right, up, up, up, left, up, up, right, right, down, down, down, down, down, right, up, right, right, down, left, down, down, down, right, right, up, left, up, right, up, right, up, right, up, up, up, up, right, down, down, down, down, right, down, right, down, down, left, up, left, up, left, down, down, right, down, left, down, left, down, down, right, up, right, down, down, down, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TqmUaaf4FKDxnsEP86zG2AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=3678,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3678
    ),
  ],
  total_token_count=3733
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=3678 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3678
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3733 traffic_type=None
```

### `maze_line_15x15_tokenized_42.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, left, left, down, right, down, down, down, right, down, down, left, up, left, down, down, down, down, down, right, up, up, up, right, down, right, right, right, right, down, left, left, left, down, left, down, right, right, right, right, right, right, right, right, up, right, up, left, left, left, down, left, up, up, up, left, left, up, up, up, left, up, left, up, right, up, up, up, left, up, up, right, right, down, down, down, down, down, right, up, right, right, down, left, down, down, down, right, right, up, left, up, right, up, right, up, right, up, up, up, up, right, down, down, down, down, right, down, right, down, down, left, up, left, up, left, down, down, right, down, left, down, left, down, down, right, up, right, down, down, down, right, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UKmUab2nEYvw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_42.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, up, up, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U6mUafCLH-LUkdUPgcXX-A4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_42.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, up, up, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VKmUaf7tFL3ukdUPl-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_42.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, up, up, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, right, right, down, down, right, right, right, down, down, down, right, right, down, down, right, right, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, right, right, down, down, down, right, right, right, right, down, down, right, right, right, down, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right, right, right, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,right,down,down,right,right,right,down,down,down,right,right,down,down,right,right,right,right,right,down,down,down,right,right,right,down,down,right,right,right,down,down,right,right,down,down,down,right,right,right,right,down,down,right,right,right,down,down,down,right,right,right,down,down,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,right,right,down,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VqmUadLrKominsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27629,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27629
    ),
  ],
  total_token_count=28279
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27629 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27629
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28279 traffic_type=None
```

### `maze_occupancy_15x15_adj_42.txt`

**Score:** 1.45%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, up, up, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WKmUac61LseUnsEPgvzb-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_ascii_42.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, up, up, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, down, down, right, right, down, down, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,down,down,right,right,down,down,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WqmUad8j25eR1Q-x1JKgAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=556,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=556
    ),
  ],
  total_token_count=1206
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=556 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=556
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1206 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_42.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, down, down, down, down, right, right, down, down, down, down, left, left, up, up, left, left, down, down, down, down, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, up, up, up, up, up, up, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, left, left, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, right, right, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, right, right, down, down, right, right, down, down, down, down, left, left, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, left, left, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WqmUadGvIcGknsEPzKbYmAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=121,
  prompt_token_count=12134,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=12134
    ),
  ],
  total_token_count=12255
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=121 candidates_tokens_details=None prompt_token_count=12134 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=12134
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=12255 traffic_type=None
```

