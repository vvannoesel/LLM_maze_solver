# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_35.jpg` | **4.55%** | `input: 434 , ouput: 23` | `down, right, down, right, down, down, right, right, up, right, down, down` |
| `maze_line_6x6_35.json` | **13.64%** | `input: 1809 , ouput: 33` | `down, down, down, down, right, right, right, right, right, up, right, down, down, down, down, right, right` |
| `maze_line_6x6_adj_35.json` | **13.64%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_35.txt` | **22.73%** | `input: 729 , ouput: 21` | `down, down, down, right, right, right, down, down, right, right, right` |
| `maze_line_6x6_tokenized_35.txt` | **0.00%** | `input: 673 , ouput: 650` | `the, maze, is, represented, as, follows:, (0, 0), origin, no, walls, (0, 1), up, left, walls, (0, 2), up, wall, (0, 3), up, down, walls, (0, 4), up, right, walls, (0, 5), up, right, left, walls, (1, 0), right, left, walls, (1, 1), right, left, walls, (1, 2), down, left, walls, (1, 3), up, right, walls, (1, 4), down, left, walls, (1, 5), right, wall, (2, 0), right, left, walls, (2, 1), down, left, walls, (2, 2), up, down, right, walls, (2, 3), right, left, walls, (2, 4), up, right, left, walls, (2, 5), right, left, walls, (3, 0), down, left, walls, (3, 1), up, down, walls, (3, 2), up, right, walls, (3, 3), right, left, walls, (3, 4), right, left, walls, (3, 5), right, left, walls, (4, 0), up, left, walls, (4, 1), up, right, walls, (4, 2), right, left, walls, (4, 3), right, left, walls, (4, 4), right, left, walls, (4, 5), right, left, walls, (5, 0), down, right, left, walls, (5, 1), down, left, walls, (5, 2), down, wall, (5, 3), down, right, walls, (5, 4), down, left, walls, (5, 5), target, down, right, walls, let's, trace, a, path:, start, at, (0, 0)., from, (0, 0), we, can, move, right, to, (0, 1), (no, left, wall)., from, (0, 1), we, can, move, right, to, (0, 2), (no, left, wall)., from, (0, 2), we, can, move, right, to, (0, 3), (no, up, wall)., from, (0, 3), we, can, move, down, to, (1, 3), (no, down, wall)., from, (1, 3), we, can, move, down, to, (2, 3), (no, down, wall)., from, (2, 3), we, can, move, down, to, (3, 3), (no, down, wall)., from, (3, 3), we, can, move, down, to, (4, 3), (no, down, wall)., from, (4, 3), we, can, move, down, to, (5, 3), (no, down, wall)., from, (5, 3), we, can, move, right, to, (5, 4), (no, right, wall)., from, (5, 4), we, can, move, right, to, (5, 5), (no, right, wall, which, is, the, target)., the, sequence, of, moves, is:, right, right, right, down, down, down, down, down, right, right., right, right, right, down, down` |
| `maze_occupancy_6x6_35.jpg` | **2.27%** | `input: 431 , ouput: 650` | `down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, up, right, down, right, down, down, right, down, right, down, right, up, right, up, right, down, right, down, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down` |
| `maze_occupancy_6x6_35.json` | **13.64%** | `input: 988 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right` |
| `maze_occupancy_6x6_adj_35.json` | **11.36%** | `input: 4343 , ouput: 650` | `down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down` |
| `maze_occupancy_6x6_adj_35.txt` | **13.64%** | `input: 1279 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left` |
| `maze_occupancy_6x6_ascii_35.txt` | **6.82%** | `input: 257 , ouput: 67` | `down, down, down, right, right, right, down, right, down, down, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, down, right, right, right` |
| `maze_occupancy_6x6_tokenized_35.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_35.jpg`

**Score:** 4.55%

**Ground Truth Solution:**
```
down, down, down, right, right, down, down, right, up, up, up, up, left, up, right, right, down, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UYSVaYKCIdqfnsEPvPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=457
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=457 traffic_type=None
```

### `maze_line_6x6_35.json`

**Score:** 13.64%

**Ground Truth Solution:**
```
down, down, down, right, right, down, down, right, up, up, up, up, left, up, right, right, down, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, right, right, up, right, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,right,right,right,right,right,up,right,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UoSVaay4C8yynsEPyd_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1842
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1842 traffic_type=None
```

### `maze_line_6x6_adj_35.json`

**Score:** 13.64%

**Ground Truth Solution:**
```
down, down, down, right, right, down, down, right, up, up, up, up, left, up, right, right, down, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UoSVabTnMaL17M8Pt6zc8AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2277
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2277 traffic_type=None
```

### `maze_line_6x6_adj_35.txt`

**Score:** 22.73%

**Ground Truth Solution:**
```
down, down, down, right, right, down, down, right, up, up, up, up, left, up, right, right, down, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, right, right, right, down, down, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4SVaaHDIdqgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=750
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=750 traffic_type=None
```

### `maze_line_6x6_tokenized_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, right, right, down, down, right, up, up, up, up, left, up, right, right, down, right, down, down, down, down
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows:, (0, 0), origin, no, walls, (0, 1), up, left, walls, (0, 2), up, wall, (0, 3), up, down, walls, (0, 4), up, right, walls, (0, 5), up, right, left, walls, (1, 0), right, left, walls, (1, 1), right, left, walls, (1, 2), down, left, walls, (1, 3), up, right, walls, (1, 4), down, left, walls, (1, 5), right, wall, (2, 0), right, left, walls, (2, 1), down, left, walls, (2, 2), up, down, right, walls, (2, 3), right, left, walls, (2, 4), up, right, left, walls, (2, 5), right, left, walls, (3, 0), down, left, walls, (3, 1), up, down, walls, (3, 2), up, right, walls, (3, 3), right, left, walls, (3, 4), right, left, walls, (3, 5), right, left, walls, (4, 0), up, left, walls, (4, 1), up, right, walls, (4, 2), right, left, walls, (4, 3), right, left, walls, (4, 4), right, left, walls, (4, 5), right, left, walls, (5, 0), down, right, left, walls, (5, 1), down, left, walls, (5, 2), down, wall, (5, 3), down, right, walls, (5, 4), down, left, walls, (5, 5), target, down, right, walls, let's, trace, a, path:, start, at, (0, 0)., from, (0, 0), we, can, move, right, to, (0, 1), (no, left, wall)., from, (0, 1), we, can, move, right, to, (0, 2), (no, left, wall)., from, (0, 2), we, can, move, right, to, (0, 3), (no, up, wall)., from, (0, 3), we, can, move, down, to, (1, 3), (no, down, wall)., from, (1, 3), we, can, move, down, to, (2, 3), (no, down, wall)., from, (2, 3), we, can, move, down, to, (3, 3), (no, down, wall)., from, (3, 3), we, can, move, down, to, (4, 3), (no, down, wall)., from, (4, 3), we, can, move, down, to, (5, 3), (no, down, wall)., from, (5, 3), we, can, move, right, to, (5, 4), (no, right, wall)., from, (5, 4), we, can, move, right, to, (5, 5), (no, right, wall, which, is, the, target)., the, sequence, of, moves, is:, right, right, right, down, down, down, down, down, right, right., right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is represented as follows:

(0,0) Origin, no walls
(0,1) Up, Left walls
(0,2) Up wall
(0,3) Up, Down walls
(0,4) Up, Right walls
(0,5) Up, Right, Left walls

(1,0) Right, Left walls
(1,1) Right, Left walls
(1,2) Down, Left walls
(1,3) Up, Right walls
(1,4) Down, Left walls
(1,5) Right wall

(2,0) Right, Left walls
(2,1) Down, Left walls
(2,2) Up, Down, Right walls
(2,3) Right, Left walls
(2,4) Up, Right, Left walls
(2,5) Right, Left walls

(3,0) Down, Left walls
(3,1) Up, Down walls
(3,2) Up, Right walls
(3,3) Right, Left walls
(3,4) Right, Left walls
(3,5) Right, Left walls

(4,0) Up, Left walls
(4,1) Up, Right walls
(4,2) Right, Left walls
(4,3) Right, Left walls
(4,4) Right, Left walls
(4,5) Right, Left walls

(5,0) Down, Right, Left walls
(5,1) Down, Left walls
(5,2) Down wall
(5,3) Down, Right walls
(5,4) Down, Left walls
(5,5) Target, Down, Right walls

Let's trace a path:

Start at (0,0).
From (0,0), we can move right to (0,1) (no left wall).
From (0,1), we can move right to (0,2) (no left wall).
From (0,2), we can move right to (0,3) (no up wall).
From (0,3), we can move down to (1,3) (no down wall).
From (1,3), we can move down to (2,3) (no down wall).
From (2,3), we can move down to (3,3) (no down wall).
From (3,3), we can move down to (4,3) (no down wall).
From (4,3), we can move down to (5,3) (no down wall).
From (5,3), we can move right to (5,4) (no right wall).
From (5,4), we can move right to (5,5) (no right wall, which is the target).

The sequence of moves is: right, right, right, down, down, down, down, down, right, right.

right,right,right,down,down,"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VYSVaY2gE6jlnsEP1bugwAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=1323
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1323 traffic_type=None
```

### `maze_occupancy_6x6_35.jpg`

**Score:** 2.27%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, right, up, right, down, right, down, down, right, down, right, down, right, up, right, up, right, down, right, down, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,right,up,right,down,right,down,down,right,down,right,down,right,up,right,up,right,down,right,down,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,right,up,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VoSVab3PNqeN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_35.json`

**Score:** 13.64%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WYSVabP8E_7MkdUPkdfHmAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_35.json`

**Score:** 11.36%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='W4SVaYjYMP367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4343
    ),
  ],
  total_token_count=4993
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4343
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4993 traffic_type=None
```

### `maze_occupancy_6x6_adj_35.txt`

**Score:** 13.64%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XYSVaYzJGNiCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1279,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1279
    ),
  ],
  total_token_count=1929
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1279 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1279
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1929 traffic_type=None
```

### `maze_occupancy_6x6_ascii_35.txt`

**Score:** 6.82%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, down, right, down, down, down, right, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,right,down,right,down,down,down,right,right,right,up,up,up,up,right,right,down,down,down,down,right,right,right,right,down,down,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XoSVaeKIE6nw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=67,
  prompt_token_count=257,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=257
    ),
  ],
  total_token_count=324
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=67 candidates_tokens_details=None prompt_token_count=257 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=257
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=324 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_35.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, down, down, right, right, right, right, down, down, down, down, right, right, up, up, up, up, up, up, up, up, left, left, up, up, right, right, right, right, down, down, right, right, down, down, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YISVae3jINHMkdUPy8C6kAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

