# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_5.jpg` | **0.00%** | `input: 551 , ouput: 261` | `the, maze, can, be, represented, as, a, 3x3, grid., the, start, is, at, (0, 0), and, the, end, is, at, (2, 2)., the, agent, starts, at, (0, 0), facing, south., the, walls, are:, -, between, (0, 0), and, (0, 1), (vertical, wall), -, between, (0, 1), and, (1, 1), (horizontal, wall), -, between, (1, 1), and, (1, 2), (vertical, wall), -, between, (1, 2), and, (2, 2), (horizontal, wall), -, outer, boundaries, are, also, walls., the, agent, starts, at, (0, 0), facing, south., 1., **forward**:, moves, to, (1, 0)., agent, is, now, at, (1, 0), facing, south., 2., **right**:, turns, east, moves, to, (1, 1)., agent, is, now, at, (1, 1), facing, east., 3., **forward**:, moves, to, (1, 2)., agent, is, now, at, (1, 2), facing, east., 4., **right**:, turns, south, moves, to, (2, 2)., agent, is, now, at, (2, 2), facing, south., this, is, the, end., forward, right, forward, right` |
| `maze_line_3x3_5.json` | **0.00%** | `input: 774 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_5.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_5.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_5.txt` | **0.00%** | `input: 439 , ouput: 650` | `the, maze, is, 3x3., the, start, is, at, (0, 0), and, the, end, is, at, (2, 2)., the, agent, starts, facing, south., let's, analyze, the, walls:, -, (0, 0):, <|uprightleft_wall|>, -, walls, to, the, right, and, up, and, left., this, means, it, can, only, go, down., -, (0, 1):, <|upleft_wall|>, -, walls, to, the, up, and, left., it, can, go, right, and, down., -, (0, 2):, <|upright_wall|>, -, walls, to, the, up, and, right., it, can, go, left, and, down., -, (1, 0):, <|downleft_wall|>, -, walls, to, the, down, and, left., it, can, go, up, and, right., -, (1, 1):, <|downright_wall|>, -, walls, to, the, down, and, right., it, can, go, up, and, left., -, (1, 2):, <|rightleft_wall|>, -, walls, to, the, right, and, left., it, can, go, up, and, down., -, (2, 0):, <|updownleft_wall|>, -, walls, to, the, up, down, and, left., this, is, impossible, as, it, would, mean, it's, a, dead, end., assuming, this, means, only, up, and, left, walls., so, it, can, go, right., -, (2, 1):, <|updown_wall|>, -, walls, to, the, up, and, down., it, can, go, left, and, right., -, (2, 2):, <|target|>, <|downright_wall|>, -, walls, to, the, down, and, right., it, can, go, up, and, left., let's, re-evaluate, the, walls, with, the, assumption, that, it, means, walls, blocking, movement, in, those, directions., -, (0, 0):, <|uprightleft_wall|>, -, no, access, up, right, or, left., must, go, down., -, (0, 1):, <|upleft_wall|>, -, no, access, up, or, left., can, go, right, or, down., -, (0, 2):, <|upright_wall|>, -, no, access, up, or, right., can, go, left, or, down., -, (1, 0):, <|downleft_wall|>, -, no, access, down, or, left., can, go, up, or, right., -, (1, 1):, <|downright_wall|>, -, no, access, down, or, right., can, go, up, or, left., -, (1, 2):, <|rightleft_wall|>, -, no, access, right, or, left., can, go, up, or, down., -, (2, 0):, <|updownleft_wall|>, -, no, access, up, down, or, left., this, cell, is, blocked., i, will, assume, this, means, only, up, and, left, are, blocked., so, it, can, go, right., -, (2, 1):, <|updown_wall|>, -, no, access, up, or, down., can, go, left, or, right., -, (2, 2):, <|target|>, <|downright_wall|>, -, no, access, down, or, right., can, go, up, or, left., the, agent, starts, at, (0, 0), facing, south., 1., **from, (0` |
| `maze_occupancy_3x3_5.jpg` | **0.00%** | `input: 546 , ouput: 27` | `right, forward, right, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_5.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_adj_5.json` | **8.33%** | `input: 1298 , ouput: 49` | `forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_5.txt` | **0.00%** | `input: 580 , ouput: 650` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left` |
| `maze_occupancy_3x3_ascii_5.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_5.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_5.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
the, maze, can, be, represented, as, a, 3x3, grid., the, start, is, at, (0, 0), and, the, end, is, at, (2, 2)., the, agent, starts, at, (0, 0), facing, south., the, walls, are:, -, between, (0, 0), and, (0, 1), (vertical, wall), -, between, (0, 1), and, (1, 1), (horizontal, wall), -, between, (1, 1), and, (1, 2), (vertical, wall), -, between, (1, 2), and, (2, 2), (horizontal, wall), -, outer, boundaries, are, also, walls., the, agent, starts, at, (0, 0), facing, south., 1., **forward**:, moves, to, (1, 0)., agent, is, now, at, (1, 0), facing, south., 2., **right**:, turns, east, moves, to, (1, 1)., agent, is, now, at, (1, 1), facing, east., 3., **forward**:, moves, to, (1, 2)., agent, is, now, at, (1, 2), facing, east., 4., **right**:, turns, south, moves, to, (2, 2)., agent, is, now, at, (2, 2), facing, south., this, is, the, end., forward, right, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze can be represented as a 3x3 grid. The start is at (0,0) and the end is at (2,2). The agent starts at (0,0) facing south.

The walls are:
- Between (0,0) and (0,1) (vertical wall)
- Between (0,1) and (1,1) (horizontal wall)
- Between (1,1) and (1,2) (vertical wall)
- Between (1,2) and (2,2) (horizontal wall)
- Outer boundaries are also walls.

The agent starts at (0,0) facing South.

1. **Forward**: Moves to (1,0). Agent is now at (1,0) facing South.
2. **Right**: Turns East, moves to (1,1). Agent is now at (1,1) facing East.
3. **Forward**: Moves to (1,2). Agent is now at (1,2) facing East.
4. **Right**: Turns South, moves to (2,2). Agent is now at (2,2) facing South. This is the end.

forward,right,forward,right"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tJMcacjHG6Wd28oP46bOiAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=261,
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
  total_token_count=812
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=261 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=812 traffic_type=None
```

### `maze_line_3x3_5.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tZMcafbpDa-8xN8Plpr0oAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=787
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=787 traffic_type=None
```

### `maze_line_3x3_adj_5.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tZMcadX7M6_9xN8Pgt6ymQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=851
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=851 traffic_type=None
```

### `maze_line_3x3_adj_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tpMcaZH0FvuDvdIPn_iEyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=481
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=481 traffic_type=None
```

### `maze_line_3x3_tokenized_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, left, right, right, forward
```

**Extracted Answer:**
```
the, maze, is, 3x3., the, start, is, at, (0, 0), and, the, end, is, at, (2, 2)., the, agent, starts, facing, south., let's, analyze, the, walls:, -, (0, 0):, <|uprightleft_wall|>, -, walls, to, the, right, and, up, and, left., this, means, it, can, only, go, down., -, (0, 1):, <|upleft_wall|>, -, walls, to, the, up, and, left., it, can, go, right, and, down., -, (0, 2):, <|upright_wall|>, -, walls, to, the, up, and, right., it, can, go, left, and, down., -, (1, 0):, <|downleft_wall|>, -, walls, to, the, down, and, left., it, can, go, up, and, right., -, (1, 1):, <|downright_wall|>, -, walls, to, the, down, and, right., it, can, go, up, and, left., -, (1, 2):, <|rightleft_wall|>, -, walls, to, the, right, and, left., it, can, go, up, and, down., -, (2, 0):, <|updownleft_wall|>, -, walls, to, the, up, down, and, left., this, is, impossible, as, it, would, mean, it's, a, dead, end., assuming, this, means, only, up, and, left, walls., so, it, can, go, right., -, (2, 1):, <|updown_wall|>, -, walls, to, the, up, and, down., it, can, go, left, and, right., -, (2, 2):, <|target|>, <|downright_wall|>, -, walls, to, the, down, and, right., it, can, go, up, and, left., let's, re-evaluate, the, walls, with, the, assumption, that, it, means, walls, blocking, movement, in, those, directions., -, (0, 0):, <|uprightleft_wall|>, -, no, access, up, right, or, left., must, go, down., -, (0, 1):, <|upleft_wall|>, -, no, access, up, or, left., can, go, right, or, down., -, (0, 2):, <|upright_wall|>, -, no, access, up, or, right., can, go, left, or, down., -, (1, 0):, <|downleft_wall|>, -, no, access, down, or, left., can, go, up, or, right., -, (1, 1):, <|downright_wall|>, -, no, access, down, or, right., can, go, up, or, left., -, (1, 2):, <|rightleft_wall|>, -, no, access, right, or, left., can, go, up, or, down., -, (2, 0):, <|updownleft_wall|>, -, no, access, up, down, or, left., this, cell, is, blocked., i, will, assume, this, means, only, up, and, left, are, blocked., so, it, can, go, right., -, (2, 1):, <|updown_wall|>, -, no, access, up, or, down., can, go, left, or, right., -, (2, 2):, <|target|>, <|downright_wall|>, -, no, access, down, or, right., can, go, up, or, left., the, agent, starts, at, (0, 0), facing, south., 1., **from, (0
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is 3x3. The start is at (0,0) and the end is at (2,2). The agent starts facing south.

Let's analyze the walls:
- (0,0): <|uprightleft_wall|> - Walls to the right and up and left. This means it can only go down.
- (0,1): <|upleft_wall|> - Walls to the up and left. It can go right and down.
- (0,2): <|upright_wall|> - Walls to the up and right. It can go left and down.
- (1,0): <|downleft_wall|> - Walls to the down and left. It can go up and right.
- (1,1): <|downright_wall|> - Walls to the down and right. It can go up and left.
- (1,2): <|rightleft_wall|> - Walls to the right and left. It can go up and down.
- (2,0): <|updownleft_wall|> - Walls to the up, down, and left. This is impossible as it would mean it's a dead end. Assuming this means only up and left walls. So it can go right.
- (2,1): <|updown_wall|> - Walls to the up and down. It can go left and right.
- (2,2): <|target|> <|downright_wall|> - Walls to the down and right. It can go up and left.

Let's re-evaluate the walls with the assumption that it means walls blocking movement in those directions.
- (0,0): <|uprightleft_wall|> - No access up, right, or left. Must go down.
- (0,1): <|upleft_wall|> - No access up or left. Can go right or down.
- (0,2): <|upright_wall|> - No access up or right. Can go left or down.
- (1,0): <|downleft_wall|> - No access down or left. Can go up or right.
- (1,1): <|downright_wall|> - No access down or right. Can go up or left.
- (1,2): <|rightleft_wall|> - No access right or left. Can go up or down.
- (2,0): <|updownleft_wall|> - No access up, down, or left. This cell is blocked. I will assume this means only up and left are blocked. So it can go right.
- (2,1): <|updown_wall|> - No access up or down. Can go left or right.
- (2,2): <|target|> <|downright_wall|> - No access down or right. Can go up or left.

The agent starts at (0,0) facing South.

1.  **From (0,"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='uZMcaYirNcLBvdIPla2QkAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=1089
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1089 traffic_type=None
```

### `maze_occupancy_3x3_5.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='u5McafDqOOeP28oP2dzIyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=546,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=288
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=573
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=546 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=573 traffic_type=None
```

### `maze_occupancy_3x3_5.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vpMcaaigNueP28oP2dzIyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=1239
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=289 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1239 traffic_type=None
```

### `maze_occupancy_3x3_adj_5.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v5McafybNsLBvdIPla2QkAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1347
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1347 traffic_type=None
```

### `maze_occupancy_3x3_adj_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Right,Forward,Forward,Left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wpMcadDVBaa_vdIPwLzvqQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=1230
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1230 traffic_type=None
```

### `maze_occupancy_3x3_ascii_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2484,
        license='',
        start_index=74,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,forward,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xJMcacm8LeuDvdIP_LDHoQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=967
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=288 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=967 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, left, forward, right, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, forward, forward, right, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xpMcaZzKPJ7sxs0P6peA-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1517
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=312 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1517 traffic_type=None
```

