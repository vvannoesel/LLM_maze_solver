# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_7.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_7.json` | **0.00%** | `input: 9807 , ouput: 650` | `down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right` |
| `maze_line_15x15_adj_7.json` | **1.52%** | `input: 13485 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_7.txt` | **1.52%** | `input: 3677 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_7.txt` | **3.03%** | `input: 3282 , ouput: 650` | `right, down, down, down, right, down, down, down, down, right, down, down, down, down, right, right, right, down, down, right, down, down, right, right, right, right, right, up, right, up, up, up, right, up, up, right, up, up, up, up, right, up, right, right, right, down, right, down, down, down, left, down, left, left, down, left, left, up, left, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up` |
| `maze_occupancy_15x15_7.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_7.json` | **0.76%** | `input: 4246 , ouput: 650` | `right, down, down, right, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down` |
| `maze_occupancy_15x15_adj_7.json` | **2.27%** | `input: 27640 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_7.txt` | **3.03%** | `input: 7735 , ouput: 59` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_ascii_7.txt` | **2.27%** | `input: 535 , ouput: 650` | `right, right, down, right, right, down, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_7.txt` | **3.03%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_7.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, left, down, right, down, down, right, right, right, up, right, up, right, down, down, down, down, left, down, left, up, left, up, left, left, down, down, down, left, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, left, up, up, right, right, down, right, right, down, right, right, right, down, down, right, right, up, right, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m_4lafGvIdGpkdUP1MSeKQ' usage_metadata=GenerateContentResponseUsageMetadata(
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
  total_token_count=436
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=436 traffic_type=None
```

### `maze_line_15x15_7.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, right, down, down, right, right, right, up, right, up, right, down, down, down, down, left, down, left, up, left, up, left, left, down, down, down, left, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, left, up, up, right, right, down, right, right, down, right, right, right, down, down, right, right, up, right, right, right, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nv4lae3GK_jMkdUPy-PZSQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_7.json`

**Score:** 1.52%

**Ground Truth Solution:**
```
right, down, left, down, right, down, down, right, right, right, up, right, up, right, down, down, down, down, left, down, left, up, left, up, left, left, down, down, down, left, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, left, up, up, right, right, down, right, right, down, right, right, right, down, down, right, right, up, right, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n_4labPROPPi7M8PlYuCeQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=13485,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13485
    ),
  ],
  total_token_count=13542
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=13485 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13485
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13542 traffic_type=None
```

### `maze_line_15x15_adj_7.txt`

**Score:** 1.52%

**Ground Truth Solution:**
```
right, down, left, down, right, down, down, right, right, right, up, right, up, right, down, down, down, down, left, down, left, up, left, up, left, left, down, down, down, left, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, left, up, up, right, right, down, right, right, down, right, right, right, down, down, right, right, up, right, right, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o_4laYadBPjMkdUPy-PZSQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3677,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3677
    ),
  ],
  total_token_count=4327
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3677 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3677
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4327 traffic_type=None
```

### `maze_line_15x15_tokenized_7.txt`

**Score:** 3.03%

**Ground Truth Solution:**
```
right, down, left, down, right, down, down, right, right, right, up, right, up, right, down, down, down, down, left, down, left, up, left, up, left, left, down, down, down, left, down, right, down, left, down, right, down, left, down, right, down, right, up, right, up, left, up, up, right, right, down, right, right, down, right, right, right, down, down, right, right, up, right, right, right, down
```

**Extracted Answer:**
```
right, down, down, down, right, down, down, down, down, right, down, down, down, down, right, right, right, down, down, right, down, down, right, right, right, right, right, up, right, up, up, up, right, up, up, right, up, up, up, up, right, up, right, right, right, down, right, down, down, down, left, down, left, left, down, left, left, up, left, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up, left, left, left, up, left, up, up, up, left, up, up, left, up, up, up, left, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,down,down,down,down,right,down,down,down,down,right,right,right,down,down,right,down,down,right,right,right,right,right,up,right,up,up,up,right,up,up,right,up,up,up,up,right,up,right,right,right,down,right,down,down,down,left,down,left,left,down,left,left,up,left,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,left,left,left,up,left,up,up,up,left,up,up,left,up,up,up,left,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pf4laaaJLvXrkdUPk_vy-Q0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_7.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qf4laZ3fB-zgkdUP4vSTWA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_7.json`

**Score:** 0.76%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,down,down,right,right,right,right,down,down,down,down,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rP4lacrFCOmFkdUPmpCR8A0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_7.json`

**Score:** 2.27%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='r_4labyCOrSnkdUPlKu0YA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27640,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27640
    ),
  ],
  total_token_count=28290
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27640 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27640
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28290 traffic_type=None
```

### `maze_occupancy_15x15_adj_7.txt`

**Score:** 3.03%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sf4lafKuAqfknsEP64etWQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=7735,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7735
    ),
  ],
  total_token_count=7794
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=7735 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7735
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7794 traffic_type=None
```

### `maze_occupancy_15x15_ascii_7.txt`

**Score:** 2.27%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, down, down, right, right, right, right, down, down, left, left, left, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,down,right,right,right,right,down,down,left,left,left,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sv4labCaOOzgkdUP4vSTWA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_tokenized_7.txt`

**Score:** 3.03%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, up, up, right, right, down, down, down, down, down, down, down, down, left, left, down, down, left, left, up, up, left, left, up, up, left, left, left, left, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, left, left, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tf4ladTVEt36nsEPgoPD8A0' usage_metadata=GenerateContentResponseUsageMetadata(
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

