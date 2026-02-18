# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_43.jpg` | **4.55%** | `input: 551 , ouput: 41` | `forward, right, forward, forward, right, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_line_6x6_43.json` | **4.55%** | `input: 1926 , ouput: 650` | `forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_line_6x6_adj_43.json` | **0.00%** | `input: 2375 , ouput: 49` | `right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_line_6x6_adj_43.txt` | **4.55%** | `input: 846 , ouput: 650` | `forward, forward, left, forward, forward, right, forward, left, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left` |
| `maze_line_6x6_tokenized_43.txt` | **0.00%** | `input: 790 , ouput: 99` | `right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_43.jpg` | **4.55%** | `input: 548 , ouput: 650` | `forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward` |
| `maze_occupancy_6x6_43.json` | **0.00%** | `input: 1105 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_6x6_adj_43.json` | **0.00%** | `input: 4460 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right` |
| `maze_occupancy_6x6_adj_43.txt` | **0.00%** | `input: 1396 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left` |
| `maze_occupancy_6x6_ascii_43.txt` | **0.00%** | `input: 366 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right` |
| `maze_occupancy_6x6_tokenized_43.txt` | **0.00%** | `input: 2279 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_6x6_43.jpg`

**Score:** 4.55%

**Ground Truth Solution:**
```
forward, left, forward, left, right, right, forward, forward, right, right, left, left, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,left,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4IqVafTNDpmG7M8PkeL4mAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
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
  total_token_count=592
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=592 traffic_type=None
```

### `maze_line_6x6_43.json`

**Score:** 4.55%

**Ground Truth Solution:**
```
forward, left, forward, left, right, right, forward, forward, right, right, left, left, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,left,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4oqVaYuUEtqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1926,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1926
    ),
  ],
  total_token_count=2576
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1926 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1926
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2576 traffic_type=None
```

### `maze_line_6x6_adj_43.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, left, right, right, forward, forward, right, right, left, left, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='44qVaf_nB9iCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=2375,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2375
    ),
  ],
  total_token_count=2424
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=2375 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2375
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2424 traffic_type=None
```

### `maze_line_6x6_adj_43.txt`

**Score:** 4.55%

**Ground Truth Solution:**
```
forward, left, forward, left, right, right, forward, forward, right, right, left, left, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
forward, forward, left, forward, forward, right, forward, left, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Forward,Forward,Left,Forward,Forward,Right,Forward,Left,Forward,Forward,Forward,Right,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5IqVaZTgH-OkkdUPvpSE8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=846,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=846
    ),
  ],
  total_token_count=1496
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=846 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=846
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1496 traffic_type=None
```

### `maze_line_6x6_tokenized_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, left, right, right, forward, forward, right, right, left, left, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5YqVaZLiEKfx7M8PiZPD-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=99,
  prompt_token_count=790,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=790
    ),
  ],
  total_token_count=889
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=99 candidates_tokens_details=None prompt_token_count=790 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=790
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=889 traffic_type=None
```

### `maze_occupancy_6x6_43.jpg`

**Score:** 4.55%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,forward,right,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5oqVaY7MOITw7M8P482J-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_43.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6YqVaYl3g4fszw_G6pyYCQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_43.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=284,
        license='',
        start_index=0,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=2538,
        license='',
        start_index=180,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6oqVaa7-JqL17M8Pt6zc8AU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=430,
        license='',
        start_index=111,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=789,
        license='',
        start_index=459,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=1148,
        license='',
        start_index=818,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=1507,
        license='',
        start_index=1177,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=1866,
        license='',
        start_index=1536,
        uri='https://github.com/lucashlz/Zappy'
      ),
      <... 3 more items ...>,
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7IqVaduJN9WbkdUPuuCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7oqVae-FPOTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=366,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=366
    ),
  ],
  total_token_count=1016
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=366 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=366
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1016 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2849,
        license='',
        start_index=122,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8YqVafaLCrW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

