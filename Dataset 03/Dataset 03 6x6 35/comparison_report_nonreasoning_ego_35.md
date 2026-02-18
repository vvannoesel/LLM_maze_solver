# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_35.jpg` | **0.00%** | `input: 551 , ouput: 35` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_line_6x6_35.json` | **0.00%** | `input: 1926 , ouput: 51` | `right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward` |
| `maze_line_6x6_adj_35.json` | **0.00%** | `input: 2375 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_line_6x6_adj_35.txt` | **0.00%** | `input: 846 , ouput: 53` | `right, forward, right, forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_line_6x6_tokenized_35.txt` | **0.00%** | `input: 790 , ouput: 39` | `right, forward, forward, forward, right, forward, forward, forward, backward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_6x6_35.jpg` | **2.27%** | `input: 548 , ouput: 650` | `forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_6x6_35.json` | **2.27%** | `input: 1105 , ouput: 650` | `forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_6x6_adj_35.json` | **0.00%** | `input: 4460 , ouput: 650` | `right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right` |
| `maze_occupancy_6x6_adj_35.txt` | **0.00%** | `input: 1396 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_6x6_ascii_35.txt` | **0.00%** | `input: 374 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right` |
| `maze_occupancy_6x6_tokenized_35.txt` | **0.00%** | `input: 2279 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_6x6_35.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, left, forward, right, forward, left, left, forward, forward, forward, left, right, right, forward, right, left, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IIqVaaXAIITensEP6bbt4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=551,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=293
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=586
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=551 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=586 traffic_type=None
```

### `maze_line_6x6_35.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, left, forward, right, forward, left, left, forward, forward, forward, left, right, right, forward, right, left, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IYqVadOVGoqwnsEPl8W4mAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=1926,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1926
    ),
  ],
  total_token_count=1977
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=309 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=1926 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1926
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1977 traffic_type=None
```

### `maze_line_6x6_adj_35.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, left, forward, right, forward, left, left, forward, forward, forward, left, right, right, forward, right, left, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I4qVac3LFqrw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2375,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2375
    ),
  ],
  total_token_count=3025
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=280 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2375 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2375
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3025 traffic_type=None
```

### `maze_line_6x6_adj_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, left, forward, right, forward, left, left, forward, forward, forward, left, right, right, forward, right, left, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JIqVacO8BJnqkdUP57jkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=846,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=846
    ),
  ],
  total_token_count=899
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=313 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=846 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=846
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=899 traffic_type=None
```

### `maze_line_6x6_tokenized_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, left, forward, right, forward, left, left, forward, forward, forward, left, right, right, forward, right, left, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, backward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, right, forward, forward, forward, backward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JIqVaYGpM_nOnsEPkprNkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=790,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=790
    ),
  ],
  total_token_count=829
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=311 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=790 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=790
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=829 traffic_type=None
```

### `maze_occupancy_6x6_35.jpg`

**Score:** 2.27%

**Ground Truth Solution:**
```
forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, right, forward, left, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,right,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JoqVabDtH_fonsEPwaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=548,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=290
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=1198
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=548 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=548 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=290
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1198 traffic_type=None
```

### `maze_occupancy_6x6_35.json`

**Score:** 2.27%

**Ground Truth Solution:**
```
forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, right, forward, left, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,right,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,right,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KIqVadKDM8eC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1105,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1105
    ),
  ],
  total_token_count=1755
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=291 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1105 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1105
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1755 traffic_type=None
```

### `maze_occupancy_6x6_adj_35.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, right, forward, left, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K4qVada3BNqfnsEPvPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4460,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4460
    ),
  ],
  total_token_count=5110
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=282 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4460 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4460
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=5110 traffic_type=None
```

### `maze_occupancy_6x6_adj_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, right, forward, left, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2862,
        license='',
        start_index=147,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LIqVaYu7JsPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1396,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1396
    ),
  ],
  total_token_count=2046
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=315 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1396 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1396
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2046 traffic_type=None
```

### `maze_occupancy_6x6_ascii_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, right, forward, left, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2835,
        license='',
        start_index=136,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LoqVabeFM4qjkdUPl43u2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=374,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=374
    ),
  ],
  total_token_count=1024
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=290 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=374 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=374
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1024 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, right, forward, left, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2870,
        license='',
        start_index=0,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MIqVaYjwOtqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2279,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2279
    ),
  ],
  total_token_count=2929
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=314 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2279 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2279
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2929 traffic_type=None
```

