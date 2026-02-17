# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_37.jpg` | **2.33%** | `input: 436 , ouput: 650` | `right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_line_15x15_37.json` | **nan%** | `input: 9807 , ouput: 0` | `` |
| `maze_line_15x15_adj_37.json` | **1.16%** | `input: 13486 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_37.txt` | **1.16%** | `input: 3678 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_37.txt` | **2.33%** | `input: 3282 , ouput: 650` | `right, down, right, right, right, down, down, right, right, right, down, right, down, down, down, right, down, down, right, right, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down` |
| `maze_occupancy_15x15_37.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_37.json` | **1.16%** | `input: 4246 , ouput: 650` | `right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_37.json` | **1.74%** | `input: 27630 , ouput: 650` | `right, right, down, right, right, down, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down` |
| `maze_occupancy_15x15_adj_37.txt` | **0.00%** | `input: 7732 , ouput: 650` | `down, down, right, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right` |
| `maze_occupancy_15x15_ascii_37.txt` | **0.00%** | `input: 545 , ouput: 650` | `down, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, down, right, right, down, right, right, down, right, right, right, down, right, right, down, right, right, right, down, right, right, right, down, right, right, down, right, down, right, down, right, down, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, down, down, right, down, right, down, right, down, down, right, right, right, right, down, right, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, down, right` |
| `maze_occupancy_15x15_tokenized_37.txt` | **2.33%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_37.jpg`

**Score:** 2.33%

**Ground Truth Solution:**
```
right, down, left, down, down, down, right, down, right, down, right, down, left, left, left, down, right, down, down, down, left, down, right, right, up, right, down, down, down, right, right, right, right, right, right, up, left, up, left, down, left, left, left, up, up, up, up, right, up, left, up, up, right, down, right, right, down, left, down, down, right, up, right, down, down, right, down, right, right, down, down, right, right, up, left, up, right, up, up, up, right, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1776,
        license='',
        start_index=209,
        uri='https://americanarchive.org/catalog/cpb-aacip-b6e75cd0ce5'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vaiUafvjDqiSkdUPmsP7uA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_37.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, left, down, down, down, right, down, right, down, right, down, left, left, left, down, right, down, down, down, left, down, right, right, up, right, down, down, down, right, right, right, right, right, right, up, left, up, left, down, left, left, left, up, up, up, up, right, up, left, up, up, right, down, right, right, down, left, down, down, right, up, right, down, down, right, down, right, right, down, down, right, right, up, left, up, right, up, up, up, right, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wKiUadK7A6eN7M8P04OMiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=9807
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=9807 traffic_type=None
```

### `maze_line_15x15_adj_37.json`

**Score:** 1.16%

**Ground Truth Solution:**
```
right, down, left, down, down, down, right, down, right, down, right, down, left, left, left, down, right, down, down, down, left, down, right, right, up, right, down, down, down, right, right, right, right, right, right, up, left, up, left, down, left, left, left, up, up, up, up, right, up, left, up, up, right, down, right, right, down, left, down, down, right, up, right, down, down, right, down, right, right, down, down, right, right, up, left, up, right, up, up, up, right, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wKiUaYevN5S8nsEPnPGoiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=13486,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13486
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=13486 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13486
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13543 traffic_type=None
```

### `maze_line_15x15_adj_37.txt`

**Score:** 1.16%

**Ground Truth Solution:**
```
right, down, left, down, down, down, right, down, right, down, right, down, left, left, left, down, right, down, down, down, left, down, right, right, up, right, down, down, down, right, right, right, right, right, right, up, left, up, left, down, left, left, left, up, up, up, up, right, up, left, up, up, right, down, right, right, down, left, down, down, right, up, right, down, down, right, down, right, right, down, down, right, right, up, left, up, right, up, up, up, right, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wqiUaZ3qDumekdUPuPLrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_37.txt`

**Score:** 2.33%

**Ground Truth Solution:**
```
right, down, left, down, down, down, right, down, right, down, right, down, left, left, left, down, right, down, down, down, left, down, right, right, up, right, down, down, down, right, right, right, right, right, right, up, left, up, left, down, left, left, left, up, up, up, up, right, up, left, up, up, right, down, right, right, down, left, down, down, right, up, right, down, down, right, down, right, right, down, down, right, right, up, left, up, right, up, up, up, right, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, right, right, down, down, right, right, right, down, right, down, down, down, right, down, down, right, right, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,down,down,right,right,right,down,right,down,down,down,right,down,down,right,right,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,down,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w6iUaePPLPOekdUPoeqlcA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_37.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, left, left, up, up, left, left, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='x6iUaZ2aB_X6nsEP2_KP8AI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_37.json`

**Score:** 1.16%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, left, left, up, up, left, left, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yKiUabO3J4vw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_37.json`

**Score:** 1.74%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, left, left, up, up, left, left, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, down, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yqiUaaf7LominsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27630,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27630
    ),
  ],
  total_token_count=28280
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27630 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27630
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28280 traffic_type=None
```

### `maze_occupancy_15x15_adj_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, left, left, up, up, left, left, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right, down, down, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,down,down,right,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zKiUaaOnA-mekdUPn_LrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7732,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7732
    ),
  ],
  total_token_count=8382
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7732 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7732
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8382 traffic_type=None
```

### `maze_occupancy_15x15_ascii_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, left, left, up, up, left, left, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, down, down, right, right, right, right, down, right, down, right, down, right, down, down, right, right, down, right, right, down, right, right, right, down, right, right, down, right, right, right, down, right, right, right, down, right, right, down, right, down, right, down, right, down, down, right, right, right, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, down, down, right, down, right, down, right, down, down, right, right, right, right, down, right, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, right, right, down, right, right, down, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, down, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, down, down, right, right, right, right, down, right, right, down, down, down, right, right, right, right, down, down, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,right,down,down,down,right,right,right,right,down,right,down,right,down,right,down,down,right,right,down,right,right,down,right,right,right,down,right,right,down,right,right,right,down,right,right,right,down,right,right,down,right,down,right,down,right,down,down,right,right,right,right,down,right,right,down,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,down,down,right,down,right,down,right,down,down,right,right,right,right,down,right,right,down,down,down,right,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,right,down,right,right,down,right,right,down,right,right,down,right,down,down,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,right,down,right,right,down,down,down,right,right,right,right,down,down,down,right,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,right,down,down,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,right,down,right,right,down,down,down,right,right,right,right,down,down,down,right,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,right,down,down,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,down,down,right,right,right,right,down,right,right,down,down,down,right,right,right,right,down,down,down,right,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zaiUaaaYOeesnsEPyseT6QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=545,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=545
    ),
  ],
  total_token_count=1195
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=545 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=545
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1195 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_37.txt`

**Score:** 2.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, down, down, down, down, down, down, left, left, down, down, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, left, left, up, up, left, left, down, down, left, left, left, left, left, left, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, down, down, right, right, right, right, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0KiUad-wBbiMkdUP6OakcA' usage_metadata=GenerateContentResponseUsageMetadata(
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

