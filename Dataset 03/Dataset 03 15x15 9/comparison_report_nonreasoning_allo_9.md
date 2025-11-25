# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_9.jpg` | **0.00%** | `input: 436 , ouput: 103` | `right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, up, right, down, right, down` |
| `maze_line_15x15_9.json` | **0.76%** | `input: 9807 , ouput: 55` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_line_15x15_adj_9.json` | **0.00%** | `input: 13486 , ouput: 57` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_9.txt` | **0.00%** | `input: 3678 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up` |
| `maze_line_15x15_tokenized_9.txt` | **0.00%** | `input: 3282 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_9.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_9.json` | **0.00%** | `input: 4246 , ouput: 57` | `right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_9.json` | **1.52%** | `input: 27633 , ouput: 650` | `down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down` |
| `maze_occupancy_15x15_adj_9.txt` | **0.76%** | `input: 7729 , ouput: 113` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_9.txt` | **0.00%** | `input: 543 , ouput: 650` | `right, right, down, down, right, right, right, down, right, right, right, right, down, right, down, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right` |
| `maze_occupancy_15x15_tokenized_9.txt` | **0.00%** | `input: 12134 , ouput: 650` | `right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_9.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, right, up, up, right, up, left, left, up, right, right, right, right, down, right, up, right, down, right, up, right, down, down, down, left, left, up, left, left, down, left, left, down, down, right, up, right, down, right, down, right, right, up, up, right, right, right, right, down, down, down, down, left, up, up, left, up, left, down, down, right, down, down, left, down, right, down, left, down, left, left, left, left, up, up, up, right, up, up, left, down, left, up, left, left, left, down, down, right, right, down, left, down, left, up, left, down, left, left, down, down, down, right, up, up, right, right, down, left, down, right, right, right, right, right, right, right, up, right, right, down, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, left, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, up, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,left,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,up,right,up,right,up,right,down,right,down,right,up,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2f4laamsJLrwnsEPyYGxQA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=103,
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
  total_token_count=539
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=103 candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=539 traffic_type=None
```

### `maze_line_15x15_9.json`

**Score:** 0.76%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, right, up, up, right, up, left, left, up, right, right, right, right, down, right, up, right, down, right, up, right, down, down, down, left, left, up, left, left, down, left, left, down, down, right, up, right, down, right, down, right, right, up, up, right, right, right, right, down, down, down, down, left, up, up, left, up, left, down, down, right, down, down, left, down, right, down, left, down, left, left, left, left, up, up, up, right, up, up, left, down, left, up, left, left, left, down, down, right, right, down, left, down, left, up, left, down, left, left, down, down, down, right, up, up, right, right, down, left, down, right, right, right, right, right, right, right, up, right, right, down, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2v4lafvDF9OskdUPsdG58A0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, right, up, up, right, up, left, left, up, right, right, right, right, down, right, up, right, down, right, up, right, down, down, down, left, left, up, left, left, down, left, left, down, down, right, up, right, down, right, down, right, right, up, up, right, right, right, right, down, down, down, down, left, up, up, left, up, left, down, down, right, down, down, left, down, right, down, left, down, left, left, left, left, up, up, up, right, up, up, left, down, left, up, left, left, left, down, down, right, right, down, left, down, left, up, left, down, left, left, down, down, down, right, up, up, right, right, down, left, down, right, right, right, right, right, right, right, up, right, right, down, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2_4laZebJvCvkdUP5fOdiQs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, right, up, up, right, up, left, left, up, right, right, right, right, down, right, up, right, down, right, up, right, down, down, down, left, left, up, left, left, down, left, left, down, down, right, up, right, down, right, down, right, right, up, up, right, right, right, right, down, down, down, down, left, up, up, left, up, left, down, down, right, down, down, left, down, right, down, left, down, left, left, left, left, up, up, up, right, up, up, left, down, left, up, left, left, left, down, down, right, right, down, left, down, left, up, left, down, left, left, down, down, down, right, up, up, right, right, down, left, down, right, right, right, right, right, right, right, up, right, right, down, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3v4lae2VNae5nsEProqb8AE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, down, right, down, down, right, up, up, right, up, left, left, up, right, right, right, right, down, right, up, right, down, right, up, right, down, down, down, left, left, up, left, left, down, left, left, down, down, right, up, right, down, right, down, right, right, up, up, right, right, right, right, down, down, down, down, left, up, up, left, up, left, down, down, right, down, down, left, down, right, down, left, down, left, left, left, left, up, up, up, right, up, up, left, down, left, up, left, left, left, down, down, right, right, down, left, down, left, up, left, down, left, left, down, down, down, right, up, up, right, right, down, left, down, right, right, right, right, right, right, right, up, right, right, down, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4P4laa7WNLSnkdUPtKq0YA' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_9.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, up, up, left, left, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5f4laZXhD9XonsEPnbre8Q0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_9.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, up, up, left, left, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5v4labioHunskdUPnc7FGQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4303
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4303 traffic_type=None
```

### `maze_occupancy_15x15_adj_9.json`

**Score:** 1.52%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, up, up, left, left, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6v4laaqXHu2cnsEPk_b96A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27633,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27633
    ),
  ],
  total_token_count=28283
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27633 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27633
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28283 traffic_type=None
```

### `maze_occupancy_15x15_adj_9.txt`

**Score:** 0.76%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, up, up, left, left, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6_4labvUJcaYkdUPx9Xo4A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=113,
  prompt_token_count=7729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7729
    ),
  ],
  total_token_count=7842
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=113 candidates_tokens_details=None prompt_token_count=7729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=7842 traffic_type=None
```

### `maze_occupancy_15x15_ascii_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, up, up, left, left, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, right, right, right, right, down, right, down, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,right,right,right,right,down,right,down,right,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7v4labf9EJmJ7M8PmN722A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=543,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=543
    ),
  ],
  total_token_count=1193
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=543 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=543
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1193 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, down, down, right, right, down, down, down, down, right, right, up, up, up, up, right, right, up, up, left, left, left, left, up, up, right, right, right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, left, left, left, left, up, up, left, left, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, left, left, up, up, up, up, left, left, up, up, left, left, down, down, down, down, right, right, down, down, down, down, left, left, down, down, right, right, down, down, left, left, down, down, left, left, left, left, left, left, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, down, down, left, left, up, up, left, left, left, left, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, left, left, up, up, left, left, down, down, left, left, left, left, down, down, down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8P4labe0Ku2cnsEPk_b96A0' usage_metadata=GenerateContentResponseUsageMetadata(
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

