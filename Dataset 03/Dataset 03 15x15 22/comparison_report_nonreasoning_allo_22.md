# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_22.jpg` | **0.00%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, left, down, left, down, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_line_15x15_22.json` | **1.35%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_22.json` | **0.00%** | `input: 13488 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_22.txt` | **nan%** | `input: 3680 , ouput: 0` | `` |
| `maze_line_15x15_tokenized_22.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, right, down, right, down, right, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right` |
| `maze_occupancy_15x15_22.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_22.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_22.json` | **5.41%** | `input: 27646 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down` |
| `maze_occupancy_15x15_adj_22.txt` | **1.35%** | `input: 7739 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_22.txt` | **1.35%** | `input: 532 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_22.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_22.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, right, up, right, right, right, down, left, left, down, right, down, left, down, down, down, left, left, left, left, down, right, right, down, down, down, right, right, down, down, down, right, down, right, right, right, up, right, right, down, right, up, up, left, left, left, up, left, up, up, up, right, right, right, right, up, right, down, right, right, down, left, down, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, down, left, down, left, down, left, up, left, up, right, up, right, down, right, down, right, down, right, up, right, up, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1764,
        license='',
        start_index=219,
        uri='https://americanarchive.org/catalog/cpb-aacip-b6e75cd0ce5'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,down,left,down,left,down,left,up,left,up,right,up,right,down,right,down,right,down,right,up,right,up,right,up,right,up,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='g6aUabiEPLK7nsEPp-bmmQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_22.json`

**Score:** 1.35%

**Ground Truth Solution:**
```
down, right, right, right, up, right, right, right, down, left, left, down, right, down, left, down, down, down, left, left, left, left, down, right, right, down, down, down, right, right, down, down, down, right, down, right, right, right, up, right, right, down, right, up, up, left, left, left, up, left, up, up, up, right, right, right, right, up, right, down, right, right, down, left, down, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='haaUafHoHOiXkdUPtIrQkAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_22.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, right, up, right, right, right, down, left, left, down, right, down, left, down, down, down, left, left, left, left, down, right, right, down, down, down, right, right, down, down, down, right, down, right, right, right, up, right, right, down, right, up, up, left, left, left, up, left, up, up, up, right, right, right, right, up, right, down, right, right, down, left, down, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hqaUaYPIAoqB7M8P4pHemAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=13488,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13488
    ),
  ],
  total_token_count=13545
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=13488 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13488
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13545 traffic_type=None
```

### `maze_line_15x15_adj_22.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, right, right, right, up, right, right, right, down, left, left, down, right, down, left, down, down, down, left, left, left, left, down, right, right, down, down, down, right, right, down, down, down, right, down, right, right, right, up, right, right, down, right, up, up, left, left, left, up, left, up, up, up, right, right, right, right, up, right, down, right, right, down, left, down, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iKaUacf-Bob1kdUP8IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=3680,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3680
    ),
  ],
  total_token_count=3680
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=3680 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3680
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3680 traffic_type=None
```

### `maze_line_15x15_tokenized_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, right, up, right, right, right, down, left, left, down, right, down, left, down, down, down, left, left, left, left, down, right, right, down, down, down, right, right, down, down, down, right, down, right, right, right, up, right, right, down, right, up, up, left, left, left, up, left, up, up, up, right, right, right, right, up, right, down, right, right, down, left, down, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, down, right, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, right, down, right, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iqaUae-KCJqAkdUP4OXyyQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_22.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jaaUaZzQCeesnsEPyseT6QE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_22.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j6aUaZC2CcSzkdUP4ZaoqQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_22.json`

**Score:** 5.41%

**Ground Truth Solution:**
```
down, down, right, right, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kKaUafeeMtrOnsEPw-rG0AM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27646,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27646
    ),
  ],
  total_token_count=28296
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27646 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27646
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28296 traffic_type=None
```

### `maze_occupancy_15x15_adj_22.txt`

**Score:** 1.35%

**Ground Truth Solution:**
```
down, down, right, right, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kqaUaZalCdrOnsEPw-rG0AM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7739,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7739
    ),
  ],
  total_token_count=8389
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7739 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7739
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8389 traffic_type=None
```

### `maze_occupancy_15x15_ascii_22.txt`

**Score:** 1.35%

**Ground Truth Solution:**
```
down, down, right, right, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lKaUaYzuA_CMkdUPpaWNwAE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=532,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=532
    ),
  ],
  total_token_count=1182
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=532 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=532
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1182 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, left, left, down, down, right, right, down, down, left, left, down, down, down, down, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, up, up, up, up, left, left, left, left, left, left, up, up, left, left, up, up, up, up, up, up, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, down, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lqaUac7FA8f5nsEPi7DUqAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

