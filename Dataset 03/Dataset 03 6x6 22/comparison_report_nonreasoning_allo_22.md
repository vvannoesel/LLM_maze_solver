# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_22.jpg` | **0.00%** | `input: 434 , ouput: 51` | `right, down, right, down, right, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right, up, right, up, right, down, right` |
| `maze_line_6x6_22.json` | **4.55%** | `input: 1809 , ouput: 39` | `down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_22.json` | **13.64%** | `input: 2258 , ouput: 33` | `down, right, right, right, down, down, down, down, down, right, right, right, right, down, down, right, right` |
| `maze_line_6x6_adj_22.txt` | **0.00%** | `input: 729 , ouput: 23` | `right, right, right, down, right, down, down, right, down, right, down, right` |
| `maze_line_6x6_tokenized_22.txt` | **0.00%** | `input: 673 , ouput: 649` | `the, maze, description, is, a, bit, confusing, as, it, describes, walls, for, each, cell, without, specifying, the, connections, between, cells., however, based, on, typical, maze, representations, and, the, provided, wall, descriptions, i, will, infer, the, possible, paths., the, start, is, at, (0, 0), and, the, end, is, at, (5, 5)., let's, break, down, the, maze, cell, by, cell, and, infer, connections:, *, **(0, 0), <|uprightleft_wall|>, <|origin|>:**, has, a, wall, on, the, right, and, left., since, it's, the, origin, and, top-left, it's, likely, that, "up", and, "left", walls, mean, those, directions, are, blocked, from, this, cell., so, we, can, potentially, move, down., *, **(0, 1), <|updownleft_wall|>:, **, this, cell, has, walls, on, the, up, down, and, left., this, implies, we, can, move, right., *, **(0, 2), <|up_wall|>, :**, has, an, up, wall., we, can, move, left, down, or, right, from, here., *, **(0, 3), <|upright_wall|>, :**, has, an, up, and, right, wall., we, can, move, left, or, down., *, **(0, 4), <|updownleft_wall|>, :**, has, up, down, and, left, walls., we, can, move, right., *, **(0, 5), <|upright_wall|>, :**, has, up, and, right, walls., we, can, move, left., *, **(1, 0), <|downleft_wall|>, :**, has, down, and, left, walls., we, can, move, up, or, right., *, **(1, 1), <|updown_wall|>, :**, has, up, and, down, walls., we, can, move, left, or, right., *, **(1, 2), <|downright_wall|>, :**, has, down, and, right, walls., we, can, move, up, or, left., *, **(1, 3), <|downleft_wall|>, :**, has, down, and, left, walls., we, can, move, up, or, right., *, **(1, 4), <|upright_wall|>, :**, has, up, and, right, walls., we, can, move, left, or, down., *, **(1, 5), <|rightleft_wall|>, :**, has, right, and, left, walls., we, can, move, up, or, down., *, **(2, 0), <|uprightleft_wall|>, :**, has, up, right, and, left, walls., we, can, move, down., *, **(2, 1), <|upleft_wall|>, :**, has, up, and, left, walls., we, can, move, right, or, down., *, **(2, 2), <|updown_wall|>, :**, has, up, and, down, walls., we, can, move, left, or, right., *, **(2, 3), <|upright_wall|>, :**, has, up, and, right, walls., we, can, move, left, or, down., *, **(2, 4), <|rightleft_wall|>, :**, has, right, and, left, walls., we, can, move, up, or, down., *, **(2, 5)` |
| `maze_occupancy_6x6_22.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right` |
| `maze_occupancy_6x6_22.json` | **0.00%** | `input: 988 , ouput: 650` | `right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left` |
| `maze_occupancy_6x6_adj_22.json` | **4.55%** | `input: 4347 , ouput: 55` | `down, down, down, right, right, right, down, right, down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_22.txt` | **4.55%** | `input: 1278 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_ascii_22.txt` | **0.00%** | `input: 251 , ouput: 650` | `right, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_6x6_tokenized_22.txt` | **2.27%** | `input: 2162 , ouput: 650` | `down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_6x6_22.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, down, down, down, left, up, up, left, left, down, down, right, down, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right, up, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, left, down, right, right, up, right, down, down, left, down, right, right, up, right, up, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TYKVafGAKZuZ28oPjdqtsAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=434,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=176
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=485
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=434 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=485 traffic_type=None
```

### `maze_line_6x6_22.json`

**Score:** 4.55%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, down, down, down, left, up, up, left, left, down, down, right, down, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ToKVaemPFdfIvdIPlo3gqAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1848
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=192 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1848 traffic_type=None
```

### `maze_line_6x6_adj_22.json`

**Score:** 13.64%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, down, down, down, left, up, up, left, left, down, down, right, down, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, down, down, down, down, down, right, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, right, down, down, down, down, down, right, right, right, right, down, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T4KVacaJCdrbxs0P1qTOyAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2291
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=163 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2291 traffic_type=None
```

### `maze_line_6x6_adj_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, down, down, down, left, up, up, left, left, down, down, right, down, right, right, right
```

**Extracted Answer:**
```
right, right, right, down, right, down, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, down, right, down, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UIKVaduPAraIvdIPwq3e4Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=752
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=752 traffic_type=None
```

### `maze_line_6x6_tokenized_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, right, down, down, down, left, up, up, left, left, down, down, right, down, right, right, right
```

**Extracted Answer:**
```
the, maze, description, is, a, bit, confusing, as, it, describes, walls, for, each, cell, without, specifying, the, connections, between, cells., however, based, on, typical, maze, representations, and, the, provided, wall, descriptions, i, will, infer, the, possible, paths., the, start, is, at, (0, 0), and, the, end, is, at, (5, 5)., let's, break, down, the, maze, cell, by, cell, and, infer, connections:, *, **(0, 0), <|uprightleft_wall|>, <|origin|>:**, has, a, wall, on, the, right, and, left., since, it's, the, origin, and, top-left, it's, likely, that, "up", and, "left", walls, mean, those, directions, are, blocked, from, this, cell., so, we, can, potentially, move, down., *, **(0, 1), <|updownleft_wall|>:, **, this, cell, has, walls, on, the, up, down, and, left., this, implies, we, can, move, right., *, **(0, 2), <|up_wall|>, :**, has, an, up, wall., we, can, move, left, down, or, right, from, here., *, **(0, 3), <|upright_wall|>, :**, has, an, up, and, right, wall., we, can, move, left, or, down., *, **(0, 4), <|updownleft_wall|>, :**, has, up, down, and, left, walls., we, can, move, right., *, **(0, 5), <|upright_wall|>, :**, has, up, and, right, walls., we, can, move, left., *, **(1, 0), <|downleft_wall|>, :**, has, down, and, left, walls., we, can, move, up, or, right., *, **(1, 1), <|updown_wall|>, :**, has, up, and, down, walls., we, can, move, left, or, right., *, **(1, 2), <|downright_wall|>, :**, has, down, and, right, walls., we, can, move, up, or, left., *, **(1, 3), <|downleft_wall|>, :**, has, down, and, left, walls., we, can, move, up, or, right., *, **(1, 4), <|upright_wall|>, :**, has, up, and, right, walls., we, can, move, left, or, down., *, **(1, 5), <|rightleft_wall|>, :**, has, right, and, left, walls., we, can, move, up, or, down., *, **(2, 0), <|uprightleft_wall|>, :**, has, up, right, and, left, walls., we, can, move, down., *, **(2, 1), <|upleft_wall|>, :**, has, up, and, left, walls., we, can, move, right, or, down., *, **(2, 2), <|updown_wall|>, :**, has, up, and, down, walls., we, can, move, left, or, right., *, **(2, 3), <|upright_wall|>, :**, has, up, and, right, walls., we, can, move, left, or, down., *, **(2, 4), <|rightleft_wall|>, :**, has, right, and, left, walls., we, can, move, up, or, down., *, **(2, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze description is a bit confusing as it describes walls for each cell without specifying the connections between cells. However, based on typical maze representations and the provided wall descriptions, I will infer the possible paths.

The start is at (0,0) and the end is at (5,5).

Let's break down the maze cell by cell and infer connections:

*   **(0,0) <|uprightleft_wall|> <|origin|>:** Has a wall on the right and left. Since it's the origin and top-left, it's likely that "up" and "left" walls mean those directions are blocked FROM this cell. So, we can potentially move down.
*   **(0,1) <|updownleft_wall|>: ** This cell has walls on the up, down, and left. This implies we can move right.
*   **(0,2) <|up_wall|> :** Has an up wall. We can move left, down, or right from here.
*   **(0,3) <|upright_wall|> :** Has an up and right wall. We can move left or down.
*   **(0,4) <|updownleft_wall|> :** Has up, down, and left walls. We can move right.
*   **(0,5) <|upright_wall|> :** Has up and right walls. We can move left.

*   **(1,0) <|downleft_wall|> :** Has down and left walls. We can move up or right.
*   **(1,1) <|updown_wall|> :** Has up and down walls. We can move left or right.
*   **(1,2) <|downright_wall|> :** Has down and right walls. We can move up or left.
*   **(1,3) <|downleft_wall|> :** Has down and left walls. We can move up or right.
*   **(1,4) <|upright_wall|> :** Has up and right walls. We can move left or down.
*   **(1,5) <|rightleft_wall|> :** Has right and left walls. We can move up or down.

*   **(2,0) <|uprightleft_wall|> :** Has up, right, and left walls. We can move down.
*   **(2,1) <|upleft_wall|> :** Has up and left walls. We can move right or down.
*   **(2,2) <|updown_wall|> :** Has up and down walls. We can move left or right.
*   **(2,3) <|upright_wall|> :** Has up and right walls. We can move left or down.
*   **(2,4) <|rightleft_wall|> :** Has right and left walls. We can move up or down.
*   **(2,5)"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UYKVae75OO-0xN8P0rGNyQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=649,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=1322
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=649 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1322 traffic_type=None
```

### `maze_occupancy_6x6_22.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, up, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4KVaZ7HK4rbxN8P14bjqQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1081
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1081 traffic_type=None
```

### `maze_occupancy_6x6_22.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VYKVaZniBNqb28oPgemZoQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1638
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1638 traffic_type=None
```

### `maze_occupancy_6x6_adj_22.json`

**Score:** 4.55%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, right, down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, right, right, right, down, right, down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VoKVac70CYePvdIP3vepyAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=4347,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4347
    ),
  ],
  total_token_count=4402
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=4347 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4347
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4402 traffic_type=None
```

### `maze_occupancy_6x6_adj_22.txt`

**Score:** 4.55%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WIKVad-IG5uZ28oPh4-usAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1278,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1278
    ),
  ],
  total_token_count=1928
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1278 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1278
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1928 traffic_type=None
```

### `maze_occupancy_6x6_ascii_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WoKVab3yMPT1xs0PlO7m0AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=251
    ),
  ],
  total_token_count=901
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=901 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_22.txt`

**Score:** 2.27%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down, down, down, left, left, up, up, up, up, left, left, left, left, down, down, down, down, right, right, down, down, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XYKVaZ6KBK_5vdIP_s_aiAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2812
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2812 traffic_type=None
```

