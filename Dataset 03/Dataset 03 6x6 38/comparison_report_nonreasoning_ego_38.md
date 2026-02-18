# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_38.jpg` | **0.00%** | `input: 551 , ouput: 39` | `forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, left, forward, left, forward, forward` |
| `maze_line_6x6_38.json` | **0.00%** | `input: 1926 , ouput: 47` | `right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_line_6x6_adj_38.json` | **0.00%** | `input: 2375 , ouput: 49` | `right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_line_6x6_adj_38.txt` | **0.00%** | `input: 846 , ouput: 650` | `the, agent, starts, at, (0, 0), facing, south., the, target, is, at, (5, 5)., here's, a, possible, path, to, solve, the, maze:, 1., **from, (0, 0), facing, south:**, *, turn, right, (now, facing, west)., *, forward, (move, to, (0, 1))., *, turn, right, (now, facing, north)., *, forward, (move, to, (1, 1))., *, turn, right, (now, facing, east)., *, forward, (move, to, (1, 0))., *, turn, right, (now, facing, south)., *, forward, (move, to, (2, 0))., *, turn, right, (now, facing, west)., *, forward, (move, to, (3, 0))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 0))., *, turn, right, (now, facing, east)., *, forward, (move, to, (4, 1))., *, turn, right, (now, facing, south)., *, forward, (move, to, (5, 1))., *, turn, right, (now, facing, west)., *, forward, (move, to, (5, 0))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 0))., *, turn, right, (now, facing, east)., *, forward, (move, to, (4, 1))., *, turn, right, (now, facing, south)., *, forward, (move, to, (5, 1))., *, turn, right, (now, facing, west)., *, forward, (move, to, (5, 2))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 2))., *, turn, right, (now, facing, east)., *, forward, (move, to, (4, 3))., *, turn, right, (now, facing, south)., *, forward, (move, to, (5, 3))., *, turn, right, (now, facing, west)., *, forward, (move, to, (5, 4))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 4))., *, turn, right, (now, facing, east)., *, forward, (move, to, (3, 4))., *, turn, right, (now, facing, south)., *, forward, (move, to, (4, 4))., *, turn, right, (now, facing, west)., *, forward, (move, to, (4, 3))., *, turn, right, (now, facing, north)., *, forward, (move, to, (3, 3))., *, turn, right, (now, facing, east)., *, forward, (move, to, (3, 2))., *, turn, right, (now, facing, south)., *, forward, (move, to, (2, 2))., *, turn, right, (now, facing, west)., *, forward, (move, to, (2, 1))., *` |
| `maze_line_6x6_tokenized_38.txt` | **0.00%** | `input: 790 , ouput: 650` | `right, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_6x6_38.jpg` | **0.00%** | `input: 548 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_6x6_38.json` | **0.00%** | `input: 1105 , ouput: 650` | `forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_6x6_adj_38.json` | **0.00%** | `input: 4457 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_6x6_adj_38.txt` | **0.00%** | `input: 1394 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_ascii_38.txt` | **0.00%** | `input: 365 , ouput: 650` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_tokenized_38.txt` | **0.00%** | `input: 2279 , ouput: 650` | `forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_6x6_38.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, left, forward, left, forward, forward, left, right, right, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, left, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,right,forward,forward,left,forward,left,forward,forward,right,forward,forward,left,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dYqVaYrREtHMkdUPy8C6kAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
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
  total_token_count=590
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=590 traffic_type=None
```

### `maze_line_6x6_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, left, forward, left, forward, forward, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dYqVafz5NbW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=1926,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1926
    ),
  ],
  total_token_count=1973
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=1926 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1926
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1973 traffic_type=None
```

### `maze_line_6x6_adj_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, left, forward, left, forward, forward, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='doqVaZuQKK2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, left, forward, left, forward, forward, left, right, right, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), facing, south., the, target, is, at, (5, 5)., here's, a, possible, path, to, solve, the, maze:, 1., **from, (0, 0), facing, south:**, *, turn, right, (now, facing, west)., *, forward, (move, to, (0, 1))., *, turn, right, (now, facing, north)., *, forward, (move, to, (1, 1))., *, turn, right, (now, facing, east)., *, forward, (move, to, (1, 0))., *, turn, right, (now, facing, south)., *, forward, (move, to, (2, 0))., *, turn, right, (now, facing, west)., *, forward, (move, to, (3, 0))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 0))., *, turn, right, (now, facing, east)., *, forward, (move, to, (4, 1))., *, turn, right, (now, facing, south)., *, forward, (move, to, (5, 1))., *, turn, right, (now, facing, west)., *, forward, (move, to, (5, 0))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 0))., *, turn, right, (now, facing, east)., *, forward, (move, to, (4, 1))., *, turn, right, (now, facing, south)., *, forward, (move, to, (5, 1))., *, turn, right, (now, facing, west)., *, forward, (move, to, (5, 2))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 2))., *, turn, right, (now, facing, east)., *, forward, (move, to, (4, 3))., *, turn, right, (now, facing, south)., *, forward, (move, to, (5, 3))., *, turn, right, (now, facing, west)., *, forward, (move, to, (5, 4))., *, turn, right, (now, facing, north)., *, forward, (move, to, (4, 4))., *, turn, right, (now, facing, east)., *, forward, (move, to, (3, 4))., *, turn, right, (now, facing, south)., *, forward, (move, to, (4, 4))., *, turn, right, (now, facing, west)., *, forward, (move, to, (4, 3))., *, turn, right, (now, facing, north)., *, forward, (move, to, (3, 3))., *, turn, right, (now, facing, east)., *, forward, (move, to, (3, 2))., *, turn, right, (now, facing, south)., *, forward, (move, to, (2, 2))., *, turn, right, (now, facing, west)., *, forward, (move, to, (2, 1))., *
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (0,0) facing South. The target is at (5,5).

Here's a possible path to solve the maze:

1.  **From (0,0) facing South:**
    *   Turn Right (now facing West).
    *   Forward (move to (0,1)).
    *   Turn Right (now facing North).
    *   Forward (move to (1,1)).
    *   Turn Right (now facing East).
    *   Forward (move to (1,0)).
    *   Turn Right (now facing South).
    *   Forward (move to (2,0)).
    *   Turn Right (now facing West).
    *   Forward (move to (3,0)).
    *   Turn Right (now facing North).
    *   Forward (move to (4,0)).
    *   Turn Right (now facing East).
    *   Forward (move to (4,1)).
    *   Turn Right (now facing South).
    *   Forward (move to (5,1)).
    *   Turn Right (now facing West).
    *   Forward (move to (5,0)).
    *   Turn Right (now facing North).
    *   Forward (move to (4,0)).
    *   Turn Right (now facing East).
    *   Forward (move to (4,1)).
    *   Turn Right (now facing South).
    *   Forward (move to (5,1)).
    *   Turn Right (now facing West).
    *   Forward (move to (5,2)).
    *   Turn Right (now facing North).
    *   Forward (move to (4,2)).
    *   Turn Right (now facing East).
    *   Forward (move to (4,3)).
    *   Turn Right (now facing South).
    *   Forward (move to (5,3)).
    *   Turn Right (now facing West).
    *   Forward (move to (5,4)).
    *   Turn Right (now facing North).
    *   Forward (move to (4,4)).
    *   Turn Right (now facing East).
    *   Forward (move to (3,4)).
    *   Turn Right (now facing South).
    *   Forward (move to (4,4)).
    *   Turn Right (now facing West).
    *   Forward (move to (4,3)).
    *   Turn Right (now facing North).
    *   Forward (move to (3,3)).
    *   Turn Right (now facing East).
    *   Forward (move to (3,2)).
    *   Turn Right (now facing South).
    *   Forward (move to (2,2)).
    *   Turn Right (now facing West).
    *   Forward (move to (2,1)).
    *"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eIqVadbcL7yK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, left, forward, left, forward, forward, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eoqVadm8N4-VkdUPpZbhqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_38.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fIqVaZKVJIKG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=270,
        license='',
        start_index=0,
        uri='https://github.com/lucashlz/Zappy'
      ),
      Citation(
        end_index=2546,
        license='',
        start_index=164,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='f4qVaZSUDdihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gIqVaYDKLeyOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4457,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4457
    ),
  ],
  total_token_count=5107
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4457 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4457
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=5107 traffic_type=None
```

### `maze_occupancy_6x6_adj_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='goqVaffKMJC-nsEPxMmk4QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1394,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1394
    ),
  ],
  total_token_count=2044
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1394 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1394
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2044 traffic_type=None
```

### `maze_occupancy_6x6_ascii_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=318,
        license='',
        start_index=50,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hIqVaa_lLryK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=365,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=365
    ),
  ],
  total_token_count=1015
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=365 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=365
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1015 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2522,
        license='',
        start_index=14,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hoqVabHuN5Pe7M8PjqaxkQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

