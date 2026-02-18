# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_37.jpg` | **7.14%** | `input: 551 , ouput: 49` | `forward, right, forward, forward, forward, right, forward, forward, right, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward` |
| `maze_line_6x6_37.json` | **7.14%** | `input: 1926 , ouput: 650` | `forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_line_6x6_adj_37.json` | **0.00%** | `input: 2375 , ouput: 75` | `right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward` |
| `maze_line_6x6_adj_37.txt` | **7.14%** | `input: 846 , ouput: 63` | `forward, right, forward, right, forward, forward, left, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, right, forward, right, forward, right, forward` |
| `maze_line_6x6_tokenized_37.txt` | **0.00%** | `input: 790 , ouput: 650` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_6x6_37.jpg` | **0.00%** | `input: 548 , ouput: 650` | `right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right` |
| `maze_occupancy_6x6_37.json` | **0.00%** | `input: 1105 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_6x6_adj_37.json` | **0.00%** | `input: 4459 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_adj_37.txt` | **0.00%** | `input: 1395 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_6x6_ascii_37.txt` | **0.00%** | `input: 371 , ouput: 650` | `right, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_tokenized_37.txt` | **0.00%** | `input: 2279 , ouput: 650` | `the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (11, 11)., here's, a, step-by-step, plan, to, reach, the, target:, 1., **move, down, to, row, 2:**, the, start, is, at, (1, 1)., the, cell, below, it, (2, 1), is, accessible., *, `forward`, (agent, is, now, at, (2, 1), facing, south), 2., **navigate, through, the, left, side:**, *, `right`, (agent, is, now, at, (2, 1), facing, west), *, `forward`, (agent, is, now, at, (2, 0), facing, west), *, `forward`, (agent, is, now, at, (2, -1), but, this, is, not, valid., the, agent, needs, to, move, back, to, the, accessible, path., let's, retry, path, finding, from, (2, 1), facing, south), let's, re-evaluate, from, (1, 1), facing, south., the, goal, is, (11, 11)., from, (1, 1), facing, south:, -, `forward`, (to, (2, 1), facing, south), -, `left`, (to, (2, 0), facing, east), -, `forward`, (to, (2, 1), facing, east), -, `forward`, (to, (2, 2), facing, east), -, this, is, a, wall., let's, try, another, path., from, (1, 1), facing, south:, -, `forward`, (to, (2, 1), facing, south), -, `right`, (to, (3, 1), facing, west), -, `forward`, (to, (3, 0), facing, west), -, this, is, a, wall., let's, go, right, first., from, (1, 1), facing, south:, -, `right`, (to, (1, 2), facing, west), -, `forward`, (to, (1, 1), facing, west), -, `forward`, (to, (1, 0), facing, west), -, this, is, a, wall., let's, go, right, from, (1, 1), facing, south, and, then, move, right, to, reach, the, opening., from, (1, 1), facing, south:, -, `right`, (agent, is, at, (1, 1), facing, west), -, `forward`, (agent, is, at, (1, 0), facing, west), -, this, is, a, wall., let's, go, right, and, then, turn, to, go, east., from, (1, 1), facing, south:, -, `right`, (agent, is, at, (1, 1), facing, west), -, `left`, (agent, is, at, (1, 1), facing, south), -, `left`, (agent, is, at, (1, 1), facing, east), -, `forward`, (agent, is, at, (1, 2), facing, east), -, this, is, a, wall., let's, restart, from, (1, 1), facing, south., the, target, (11, 11), is, to, the, south, and, east., we, need, to, find, a, path, to, the, east., from, (1` |

---

## Full LLM Responses

### `maze_line_6x6_37.jpg`

**Score:** 7.14%

**Ground Truth Solution:**
```
forward, left, right, forward, left, forward, right, right, left, left, forward, left, right, right
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, right, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,right,forward,left,forward,forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QoqVae2zFaG-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
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
  total_token_count=600
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=600 traffic_type=None
```

### `maze_line_6x6_37.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
forward, left, right, forward, left, forward, right, right, left, left, forward, left, right, right
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,right,forward,forward,forward,right,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RIqVacLAE6fx7M8PiZPD-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_37.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, forward, left, forward, right, right, left, left, forward, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,forward,right,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,right,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,right,forward,right,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RYqVabeLEuTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=75,
  prompt_token_count=2375,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2375
    ),
  ],
  total_token_count=2450
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=75 candidates_tokens_details=None prompt_token_count=2375 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2375
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2450 traffic_type=None
```

### `maze_line_6x6_adj_37.txt`

**Score:** 7.14%

**Ground Truth Solution:**
```
forward, left, right, forward, left, forward, right, right, left, left, forward, left, right, right
```

**Extracted Answer:**
```
forward, right, forward, right, forward, forward, left, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Forward,Right,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Left,Forward,Right,Forward,Right,Forward,Right,Forward,Right,Forward,Left,Forward,Left,Forward,Left,Forward,Right,Forward,Right,Forward,Right,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RYqVaZfLONqfnsEPzfyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=63,
  prompt_token_count=846,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=846
    ),
  ],
  total_token_count=909
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=63 candidates_tokens_details=None prompt_token_count=846 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=846
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=909 traffic_type=None
```

### `maze_line_6x6_tokenized_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, right, forward, left, forward, right, right, left, left, forward, left, right, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R4qVafjaGseC7M8P_tvRkAs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_37.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, forward, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,left,forward,left,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SYqVac6RKcyynsEP0d_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_37.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, forward, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='S4qVaZrLBL-fkdUPtcm3yAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_37.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, forward, forward, left, forward, right, forward, right, forward
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
        text='right,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TIqVacT3K8jl7M8P9OOViAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, forward, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ToqVabyGOdqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1395,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1395
    ),
  ],
  total_token_count=2045
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1395 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1395
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2045 traffic_type=None
```

### `maze_occupancy_6x6_ascii_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, forward, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=650,
        license='',
        start_index=152,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UIqVaYvuE9qfnsEPxvyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=371,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=371
    ),
  ],
  total_token_count=1021
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=371 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=371
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1021 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, left, forward, left, forward, forward, forward, left, forward, right, forward, right, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (1, 1), facing, south., the, target, is, at, (11, 11)., here's, a, step-by-step, plan, to, reach, the, target:, 1., **move, down, to, row, 2:**, the, start, is, at, (1, 1)., the, cell, below, it, (2, 1), is, accessible., *, `forward`, (agent, is, now, at, (2, 1), facing, south), 2., **navigate, through, the, left, side:**, *, `right`, (agent, is, now, at, (2, 1), facing, west), *, `forward`, (agent, is, now, at, (2, 0), facing, west), *, `forward`, (agent, is, now, at, (2, -1), but, this, is, not, valid., the, agent, needs, to, move, back, to, the, accessible, path., let's, retry, path, finding, from, (2, 1), facing, south), let's, re-evaluate, from, (1, 1), facing, south., the, goal, is, (11, 11)., from, (1, 1), facing, south:, -, `forward`, (to, (2, 1), facing, south), -, `left`, (to, (2, 0), facing, east), -, `forward`, (to, (2, 1), facing, east), -, `forward`, (to, (2, 2), facing, east), -, this, is, a, wall., let's, try, another, path., from, (1, 1), facing, south:, -, `forward`, (to, (2, 1), facing, south), -, `right`, (to, (3, 1), facing, west), -, `forward`, (to, (3, 0), facing, west), -, this, is, a, wall., let's, go, right, first., from, (1, 1), facing, south:, -, `right`, (to, (1, 2), facing, west), -, `forward`, (to, (1, 1), facing, west), -, `forward`, (to, (1, 0), facing, west), -, this, is, a, wall., let's, go, right, from, (1, 1), facing, south, and, then, move, right, to, reach, the, opening., from, (1, 1), facing, south:, -, `right`, (agent, is, at, (1, 1), facing, west), -, `forward`, (agent, is, at, (1, 0), facing, west), -, this, is, a, wall., let's, go, right, and, then, turn, to, go, east., from, (1, 1), facing, south:, -, `right`, (agent, is, at, (1, 1), facing, west), -, `left`, (agent, is, at, (1, 1), facing, south), -, `left`, (agent, is, at, (1, 1), facing, east), -, `forward`, (agent, is, at, (1, 2), facing, east), -, this, is, a, wall., let's, restart, from, (1, 1), facing, south., the, target, (11, 11), is, to, the, south, and, east., we, need, to, find, a, path, to, the, east., from, (1
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (1,1) facing South. The target is at (11,11).

Here's a step-by-step plan to reach the target:

1.  **Move down to row 2:** The start is at (1,1). The cell below it, (2,1), is accessible.
    *   `forward` (agent is now at (2,1) facing South)

2.  **Navigate through the left side:**
    *   `right` (agent is now at (2,1) facing West)
    *   `forward` (agent is now at (2,0) facing West)
    *   `forward` (agent is now at (2,-1) but this is not valid. The agent needs to move back to the accessible path. Let's retry path finding from (2,1) facing South)

Let's re-evaluate from (1,1) facing South. The goal is (11,11).

From (1,1) facing South:
- `forward` (to (2,1), facing South)
- `left` (to (2,0), facing East)
- `forward` (to (2,1), facing East)
- `forward` (to (2,2), facing East) - This is a wall.
Let's try another path.

From (1,1) facing South:
- `forward` (to (2,1), facing South)
- `right` (to (3,1), facing West)
- `forward` (to (3,0), facing West) - This is a wall.

Let's go right first. From (1,1) facing South:
- `right` (to (1,2), facing West)
- `forward` (to (1,1), facing West)
- `forward` (to (1,0), facing West) - This is a wall.

Let's go right from (1,1) facing South, and then move right to reach the opening.
From (1,1) facing South:
- `right` (agent is at (1,1) facing West)
- `forward` (agent is at (1,0), facing West) - This is a wall.

Let's go right and then turn to go east.
From (1,1) facing South:
- `right` (agent is at (1,1) facing West)
- `left` (agent is at (1,1) facing South)
- `left` (agent is at (1,1) facing East)
- `forward` (agent is at (1,2), facing East) - This is a wall.

Let's restart from (1,1) facing South.
The target (11,11) is to the south and east.
We need to find a path to the east.
From (1,"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4qVacOVBPDm7M8Po7vO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
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

