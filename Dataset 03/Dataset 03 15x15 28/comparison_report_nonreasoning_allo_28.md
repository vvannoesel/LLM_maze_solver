# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_28.jpg` | **nan%** | `input: 436 , ouput: 0` | `` |
| `maze_line_15x15_28.json` | **7.35%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_28.json` | **7.35%** | `input: 13488 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_28.txt` | **7.35%** | `input: 3680 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_28.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_28.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_28.json` | **0.00%** | `input: 4246 , ouput: 650` | `right, down, down, down, right, right, right, down, right, right, right, down, down, right, right, right, right, right, down, right, right, right, right, right, right, right, down, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, down, right, right, right, right, right, right, right, down, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, down, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down` |
| `maze_occupancy_15x15_adj_28.json` | **nan%** | `input: 27632 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_28.txt` | **7.35%** | `input: 7733 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_28.txt` | **nan%** | `input: 532 , ouput: 0` | `` |
| `maze_occupancy_15x15_tokenized_28.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_15x15_28.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, right, up, right, down, down, right, up, right, down, down, right, down, left, down, right, right, right, down, left, down, left, up, left, left, up, left, up, up, left, up, left, down, down, down, right, down, right, down, right, down, down, down, right, right, right, up, left, up, right, right, right, right, down, right, right, up, right, right, right, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='r6eUaY7YKubgnsEP3-2VSQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_28.json`

**Score:** 7.35%

**Ground Truth Solution:**
```
down, down, down, down, down, right, up, right, down, down, right, up, right, down, down, right, down, left, down, right, right, right, down, left, down, left, up, left, left, up, left, up, up, left, up, left, down, down, down, right, down, right, down, right, down, down, down, right, right, right, up, left, up, right, right, right, right, down, right, right, up, right, right, right, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sKeUaaLFC-6hnsEPsYODsAI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_28.json`

**Score:** 7.35%

**Ground Truth Solution:**
```
down, down, down, down, down, right, up, right, down, down, right, up, right, down, down, right, down, left, down, right, right, right, down, left, down, left, up, left, left, up, left, up, up, left, up, left, down, down, down, right, down, right, down, right, down, down, down, right, right, right, up, left, up, right, right, right, right, down, right, right, up, right, right, right, down, left, down, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sqeUaY7CD9uXkdUPsdSSoAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=13488,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13488
    ),
  ],
  total_token_count=14138
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13488 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13488
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14138 traffic_type=None
```

### `maze_line_15x15_adj_28.txt`

**Score:** 7.35%

**Ground Truth Solution:**
```
down, down, down, down, down, right, up, right, down, down, right, up, right, down, down, right, down, left, down, right, right, right, down, left, down, left, up, left, left, up, left, up, up, left, up, left, down, down, down, right, down, right, down, right, down, down, down, right, right, right, up, left, up, right, right, right, right, down, right, right, up, right, right, right, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sqeUaeiHNu6hnsEPsYODsAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=3680,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3680
    ),
  ],
  total_token_count=3735
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=3680 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3680
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3735 traffic_type=None
```

### `maze_line_15x15_tokenized_28.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, right, up, right, down, down, right, up, right, down, down, right, down, left, down, right, right, right, down, left, down, left, up, left, left, up, left, up, up, left, up, left, down, down, down, right, down, right, down, right, down, down, down, right, right, right, up, left, up, right, right, right, right, down, right, right, up, right, right, right, down, left, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='taeUab3IDob1kdUP8IrTsQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_28.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, up, up, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uqeUaf6_AtGxnsEPuvytyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_28.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, up, up, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, down, down, right, right, right, down, right, right, right, down, down, right, right, right, right, right, down, right, right, right, right, right, right, right, down, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, down, right, right, right, right, right, right, right, down, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, down, right, right, right, down, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,right,down,right,right,right,down,down,right,right,right,right,right,down,right,right,right,right,right,right,right,down,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,down,right,right,right,right,right,right,right,down,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,down,right,right,right,down,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vKeUaeMD6Z6R1Q-g8utx' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_28.json`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, up, up, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v6eUaYTdB73ukdUPh-SHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=27632,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27632
    ),
  ],
  total_token_count=27632
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=27632 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27632
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=27632 traffic_type=None
```

### `maze_occupancy_15x15_adj_28.txt`

**Score:** 7.35%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, up, up, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v6eUadT3OMiOkdUPuavdqQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7733,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7733
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7733 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7733
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7846 traffic_type=None
```

### `maze_occupancy_15x15_ascii_28.txt`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, up, up, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wqeUaYzKN837nsEP0869mQU' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=532,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=532
    ),
  ],
  total_token_count=532
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=532 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=532
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=532 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, left, left, up, up, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, down, down, right, right, down, down, right, right, down, down, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, right, right, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xKeUabz7EfWinsEPtZuzkQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

