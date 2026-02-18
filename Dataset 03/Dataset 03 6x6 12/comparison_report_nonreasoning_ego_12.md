# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_12.jpg` | **0.00%** | `input: 551 , ouput: 45` | `right, forward, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_line_6x6_12.json` | **0.00%** | `input: 1926 , ouput: 75` | `right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_line_6x6_adj_12.json` | **0.00%** | `input: 2375 , ouput: 47` | `right, forward, right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward` |
| `maze_line_6x6_adj_12.txt` | **14.29%** | `input: 846 , ouput: 39` | `forward, forward, forward, forward, right, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, forward, forward, forward, forward` |
| `maze_line_6x6_tokenized_12.txt` | **0.00%** | `input: 790 , ouput: 650` | `right, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right` |
| `maze_occupancy_6x6_12.jpg` | **0.00%** | `input: 548 , ouput: 650` | `right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_6x6_12.json` | **0.00%** | `input: 1105 , ouput: 650` | `right, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_adj_12.json` | **0.00%** | `input: 4459 , ouput: 650` | `right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward` |
| `maze_occupancy_6x6_adj_12.txt` | **0.00%** | `input: 1391 , ouput: 482` | `the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (11, 11)., 1., the, agent, needs, to, move, from, (1, 1), to, (2, 1)., since, it's, facing, south, it, can, move, forward., *, current, position:, (1, 1), facing:, south, *, action:, forward, *, new, position:, (2, 1), facing:, south, 2., the, agent, needs, to, move, down, the, left, wall, towards, the, target., it, continues, moving, forward, until, it, reaches, (11, 1)., *, current, position:, (2, 1), facing:, south, *, action:, forward, *, new, position:, (3, 1), facing:, south, *, ..., (repeat, 8, more, times), *, current, position:, (10, 1), facing:, south, *, action:, forward, *, new, position:, (11, 1), facing:, south, 3., at, (11, 1), the, agent, needs, to, move, towards, the, target, at, (11, 11)., it, needs, to, turn, east., *, current, position:, (11, 1), facing:, south, *, action:, right, *, new, position:, (11, 1), facing:, west, *, action:, right, *, new, position:, (11, 1), facing:, north, *, action:, right, *, new, position:, (11, 1), facing:, east, 4., now, the, agent, is, at, (11, 1), facing, east, and, needs, to, reach, (11, 11)., it, can, move, forward, repeatedly., *, current, position:, (11, 1), facing:, east, *, action:, forward, *, new, position:, (11, 2), facing:, east, *, ..., (repeat, 9, more, times), *, current, position:, (11, 10), facing:, east, *, action:, forward, *, new, position:, (11, 11), facing:, east, the, sequence, of, moves:, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, right, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_ascii_12.txt` | **0.00%** | `input: 366 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_6x6_tokenized_12.txt` | **0.00%** | `input: 2279 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_6x6_12.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, right, forward, left, left, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,left,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UoeVaemPNPfnnsEPornoiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
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
  total_token_count=596
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=596 traffic_type=None
```

### `maze_line_6x6_12.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, right, forward, left, left, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4eVaY6XHYyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=75,
  prompt_token_count=1926,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1926
    ),
  ],
  total_token_count=2001
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=75 candidates_tokens_details=None prompt_token_count=1926 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1926
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2001 traffic_type=None
```

### `maze_line_6x6_adj_12.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, right, forward, left, left, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VIeVaZ2TEb-fkdUPtcm3yAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=2375,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2375
    ),
  ],
  total_token_count=2422
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=2375 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2375
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2422 traffic_type=None
```

### `maze_line_6x6_adj_12.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, right, forward, left, left, forward, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, forward, forward, right, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,forward,forward,right,forward,forward,forward,right,forward,right,forward,forward,right,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VIeVae72MYqwnsEPl8W4mAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=846,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=846
    ),
  ],
  total_token_count=885
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=846 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=846
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=885 traffic_type=None
```

### `maze_line_6x6_tokenized_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, right, forward, left, left, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VoeVaYmeCcPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=790,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=790
    ),
  ],
  total_token_count=1440
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=790 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=790
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1440 traffic_type=None
```

### `maze_occupancy_6x6_12.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,right,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V4eVafTuKK2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_12.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=247,
        license='',
        start_index=7,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WYeVaZnCOvKcnsEPtfCWuQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_12.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,forward,right,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XIeVac7qDpzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4459,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4459
    ),
  ],
  total_token_count=5109
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4459 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4459
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=5109 traffic_type=None
```

### `maze_occupancy_6x6_adj_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (11, 11)., 1., the, agent, needs, to, move, from, (1, 1), to, (2, 1)., since, it's, facing, south, it, can, move, forward., *, current, position:, (1, 1), facing:, south, *, action:, forward, *, new, position:, (2, 1), facing:, south, 2., the, agent, needs, to, move, down, the, left, wall, towards, the, target., it, continues, moving, forward, until, it, reaches, (11, 1)., *, current, position:, (2, 1), facing:, south, *, action:, forward, *, new, position:, (3, 1), facing:, south, *, ..., (repeat, 8, more, times), *, current, position:, (10, 1), facing:, south, *, action:, forward, *, new, position:, (11, 1), facing:, south, 3., at, (11, 1), the, agent, needs, to, move, towards, the, target, at, (11, 11)., it, needs, to, turn, east., *, current, position:, (11, 1), facing:, south, *, action:, right, *, new, position:, (11, 1), facing:, west, *, action:, right, *, new, position:, (11, 1), facing:, north, *, action:, right, *, new, position:, (11, 1), facing:, east, 4., now, the, agent, is, at, (11, 1), facing, east, and, needs, to, reach, (11, 11)., it, can, move, forward, repeatedly., *, current, position:, (11, 1), facing:, east, *, action:, forward, *, new, position:, (11, 2), facing:, east, *, ..., (repeat, 9, more, times), *, current, position:, (11, 10), facing:, east, *, action:, forward, *, new, position:, (11, 11), facing:, east, the, sequence, of, moves:, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, right, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (1,1) facing South.
The target is at (11,11).

1. The agent needs to move from (1,1) to (2,1). Since it's facing South, it can move forward.
   * Current position: (1,1), facing: South
   * Action: Forward
   * New position: (2,1), facing: South

2. The agent needs to move down the left wall towards the target. It continues moving forward until it reaches (11,1).
   * Current position: (2,1), facing: South
   * Action: Forward
   * New position: (3,1), facing: South
   * ... (repeat 8 more times)
   * Current position: (10,1), facing: South
   * Action: Forward
   * New position: (11,1), facing: South

3. At (11,1), the agent needs to move towards the target at (11,11). It needs to turn East.
   * Current position: (11,1), facing: South
   * Action: Right
   * New position: (11,1), facing: West
   * Action: Right
   * New position: (11,1), facing: North
   * Action: Right
   * New position: (11,1), facing: East

4. Now the agent is at (11,1) facing East and needs to reach (11,11). It can move forward repeatedly.
   * Current position: (11,1), facing: East
   * Action: Forward
   * New position: (11,2), facing: East
   * ... (repeat 9 more times)
   * Current position: (11,10), facing: East
   * Action: Forward
   * New position: (11,11), facing: East

The sequence of moves:
forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,right,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XoeVae-cDf367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=482,
  prompt_token_count=1391,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1391
    ),
  ],
  total_token_count=1873
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=482 candidates_tokens_details=None prompt_token_count=1391 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1391
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1873 traffic_type=None
```

### `maze_occupancy_6x6_ascii_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='X4eVaYD9JvDm7M8PqbvO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_tokenized_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2867,
        license='',
        start_index=7,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YYeVaeSQO5nqkdUP3rjkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

