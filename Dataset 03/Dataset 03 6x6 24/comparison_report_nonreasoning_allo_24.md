# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_24.jpg` | **16.67%** | `input: 434 , ouput: 23` | `down, right, down, down, right, up, right, down, down, right, right, down` |
| `maze_line_6x6_24.json` | **4.17%** | `input: 1809 , ouput: 29` | `down, down, down, down, right, right, right, down, right, down, right, right, down, down, right` |
| `maze_line_6x6_adj_24.json` | **4.17%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_24.txt` | **0.00%** | `input: 729 , ouput: 521` | `the, maze, can, be, visualized, as, follows:, (0, 0), -, (1, 0), (0, 1), -, (0, 2), -, (0, 3), -, (0, 4), -, (0, 5), |, |, |, |, (1, 0), -, (1, 1), (1, 2), -, (1, 3), (1, 4), -, (1, 5), |, |, |, |, (2, 0), (2, 1), -, (2, 2), -, (2, 3), (2, 4), -, (2, 5), |, |, |, |, (3, 0), -, (3, 1), -, (3, 2), (3, 3), -, (3, 4), (3, 5), |, |, |, |, (4, 0), -, (4, 1), -, (4, 2), (4, 3), -, (4, 4), -, (4, 5), |, |, |, |, (5, 0), -, (5, 1), -, (5, 2), -, (5, 3), -, (5, 4), -, (5, 5), start, is, (0, 0), and, end, is, (5, 5)., here's, a, path, from, (0, 0), to, (5, 5):, 1., (0, 0), ->, (1, 0), (down), 2., (1, 0), ->, (1, 1), (right), 3., (1, 1), ->, (2, 1), (down), 4., (2, 1), ->, (3, 1), (down), 5., (3, 1), ->, (4, 1), (down), 6., (4, 1), ->, (4, 2), (right), 7., (4, 2), ->, (4, 3), (right), 8., (4, 3), ->, (5, 3), (down), 9., (5, 3), ->, (5, 4), (right), 10., (5, 4), ->, (5, 5), (right), so, the, sequence, of, moves, is:, down, right, down, down, down, right, right, down, right, right., down, right, down, down, down, right, right, down, right, right` |
| `maze_line_6x6_tokenized_24.txt` | **0.00%** | `input: 673 , ouput: 184` | `the, provided, maze, description, is, difficult, to, parse, as, a, grid, with, explicit, wall, information, for, each, cell., the, notation, `<|updownleft_wall|>`, etc., seems, to, indicate, walls, around, cells, but, without, a, clear, grid, structure, or, consistent, notation, for, walls, it's, impossible, to, accurately, determine, valid, paths., the, problem, description, also, states, the, maze, is, 6x6, but, the, provided, tokens, do, not, neatly, align, to, this, structure., to, solve, this, i, would, need, a, clear, representation, of, the, maze, grid, where, each, cell's, connections, (or, lack, thereof, due, to, walls), are, unambiguously, defined., given, these, limitations, i, cannot, provide, a, step-by-step, solution., if, you, can, provide, the, maze, in, a, more, standard, format, (e.g., a, 2d, array, with, characters, representing, walls, and, open, paths, or, a, list, of, cell, coordinates, with, their, wall, information), i, would, be, happy, to, help.` |
| `maze_occupancy_6x6_24.jpg` | **2.08%** | `input: 431 , ouput: 57` | `down, right, right, right, down, down, left, down, right, down, right, down, right, right, right, up, right, down, right, down, left, down, right, right, down, right, down, right, right` |
| `maze_occupancy_6x6_24.json` | **0.00%** | `input: 988 , ouput: 251` | `right, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_24.json` | **4.17%** | `input: 4345 , ouput: 65` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_6x6_adj_24.txt` | **4.17%** | `input: 1276 , ouput: 43` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_24.txt` | **0.00%** | `input: 249 , ouput: 45` | `right, right, right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_24.txt` | **2.08%** | `input: 2162 , ouput: 123` | `down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up` |

---

## Full LLM Responses

### `maze_line_6x6_24.jpg`

**Score:** 16.67%

**Ground Truth Solution:**
```
down, right, down, down, down, right, up, up, up, up, right, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, right, down, down, right, up, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,down,right,up,right,down,down,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bIKVaaujIvWNxs0PtLSW2QE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_24.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, down, down, down, right, up, up, up, up, right, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, right, right, right, down, right, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, right, right, right, down, right, down, right, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bYKVadm-FNPevdIP3abOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1838
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1838 traffic_type=None
```

### `maze_line_6x6_adj_24.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, down, down, down, right, up, up, up, up, right, right, right, down, left, down, right, down, down, left, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bYKVaaaIOYbIvdIPqfe6oAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, down, right, up, up, up, up, right, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
the, maze, can, be, visualized, as, follows:, (0, 0), -, (1, 0), (0, 1), -, (0, 2), -, (0, 3), -, (0, 4), -, (0, 5), |, |, |, |, (1, 0), -, (1, 1), (1, 2), -, (1, 3), (1, 4), -, (1, 5), |, |, |, |, (2, 0), (2, 1), -, (2, 2), -, (2, 3), (2, 4), -, (2, 5), |, |, |, |, (3, 0), -, (3, 1), -, (3, 2), (3, 3), -, (3, 4), (3, 5), |, |, |, |, (4, 0), -, (4, 1), -, (4, 2), (4, 3), -, (4, 4), -, (4, 5), |, |, |, |, (5, 0), -, (5, 1), -, (5, 2), -, (5, 3), -, (5, 4), -, (5, 5), start, is, (0, 0), and, end, is, (5, 5)., here's, a, path, from, (0, 0), to, (5, 5):, 1., (0, 0), ->, (1, 0), (down), 2., (1, 0), ->, (1, 1), (right), 3., (1, 1), ->, (2, 1), (down), 4., (2, 1), ->, (3, 1), (down), 5., (3, 1), ->, (4, 1), (down), 6., (4, 1), ->, (4, 2), (right), 7., (4, 2), ->, (4, 3), (right), 8., (4, 3), ->, (5, 3), (down), 9., (5, 3), ->, (5, 4), (right), 10., (5, 4), ->, (5, 5), (right), so, the, sequence, of, moves, is:, down, right, down, down, down, right, right, down, right, right., down, right, down, down, down, right, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze can be visualized as follows:

(0,0) - (1,0)
(0,1) - (0,2) - (0,3) - (0,4) - (0,5)
       |       |       |       |
(1,0) - (1,1) (1,2) - (1,3) (1,4) - (1,5)
       |       |       |       |
(2,0) (2,1) - (2,2) - (2,3) (2,4) - (2,5)
       |       |       |       |
(3,0) - (3,1) - (3,2) (3,3) - (3,4) (3,5)
       |       |       |       |
(4,0) - (4,1) - (4,2) (4,3) - (4,4) - (4,5)
       |       |       |       |
(5,0) - (5,1) - (5,2) - (5,3) - (5,4) - (5,5)

Start is (0,0) and End is (5,5).

Here's a path from (0,0) to (5,5):

1. (0,0) -> (1,0) (down)
2. (1,0) -> (1,1) (right)
3. (1,1) -> (2,1) (down)
4. (2,1) -> (3,1) (down)
5. (3,1) -> (4,1) (down)
6. (4,1) -> (4,2) (right)
7. (4,2) -> (4,3) (right)
8. (4,3) -> (5,3) (down)
9. (5,3) -> (5,4) (right)
10. (5,4) -> (5,5) (right)

So the sequence of moves is: down, right, down, down, down, right, right, down, right, right.

down,right,down,down,down,right,right,down,right,right"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cIKVaYSYEPWNxs0PtLSW2QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=521,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=1250
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=521 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1250 traffic_type=None
```

### `maze_line_6x6_tokenized_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, down, down, down, right, up, up, up, up, right, right, right, down, left, down, right, down, down, left, left, down, right, right
```

**Extracted Answer:**
```
the, provided, maze, description, is, difficult, to, parse, as, a, grid, with, explicit, wall, information, for, each, cell., the, notation, `<|updownleft_wall|>`, etc., seems, to, indicate, walls, around, cells, but, without, a, clear, grid, structure, or, consistent, notation, for, walls, it's, impossible, to, accurately, determine, valid, paths., the, problem, description, also, states, the, maze, is, 6x6, but, the, provided, tokens, do, not, neatly, align, to, this, structure., to, solve, this, i, would, need, a, clear, representation, of, the, maze, grid, where, each, cell's, connections, (or, lack, thereof, due, to, walls), are, unambiguously, defined., given, these, limitations, i, cannot, provide, a, step-by-step, solution., if, you, can, provide, the, maze, in, a, more, standard, format, (e.g., a, 2d, array, with, characters, representing, walls, and, open, paths, or, a, list, of, cell, coordinates, with, their, wall, information), i, would, be, happy, to, help.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The provided maze description is difficult to parse as a grid with explicit wall information for each cell. The notation `<|updownleft_wall|>` etc. seems to indicate walls around cells, but without a clear grid structure or consistent notation for walls, it's impossible to accurately determine valid paths. The problem description also states the maze is 6x6, but the provided tokens do not neatly align to this structure.

To solve this, I would need a clear representation of the maze grid, where each cell's connections (or lack thereof due to walls) are unambiguously defined.

Given these limitations, I cannot provide a step-by-step solution.

If you can provide the maze in a more standard format (e.g., a 2D array with characters representing walls and open paths, or a list of cell coordinates with their wall information), I would be happy to help."""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cYKVadmNK4KVxN8Pts2XoAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=184,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=857
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=184 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=857 traffic_type=None
```

### `maze_occupancy_6x6_24.jpg`

**Score:** 2.08%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, down, down, left, down, right, down, right, down, right, right, right, up, right, down, right, down, left, down, right, right, down, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,down,down,left,down,right,down,right,down,right,right,right,up,right,down,right,down,left,down,right,right,down,right,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='coKVadLLMeKO28oPte7eiAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
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
  total_token_count=488
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=488 traffic_type=None
```

### `maze_occupancy_6x6_24.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, up, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,up,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,up,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,up,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,up,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,up,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,up,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dIKVac6MBYePvdIP3vepyAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=251,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1239
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=251 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1239 traffic_type=None
```

### `maze_occupancy_6x6_adj_24.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dIKVaZvhPNPevdIPk6fOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=65,
  prompt_token_count=4345,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4345
    ),
  ],
  total_token_count=4410
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=65 candidates_tokens_details=None prompt_token_count=4345 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4345
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4410 traffic_type=None
```

### `maze_occupancy_6x6_adj_24.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='doKVaY3BBqrKvdIP2OLB4QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=1276,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1276
    ),
  ],
  total_token_count=1319
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=1276 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1276
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1319 traffic_type=None
```

### `maze_occupancy_6x6_ascii_24.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, down, down, right, down, down, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,down,down,right,down,down,down,down,down,down,down,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='doKVaZXCOoKVxN8Pts2XoAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=249,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=249
    ),
  ],
  total_token_count=294
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=249 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=249
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=294 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_24.txt`

**Score:** 2.08%

**Ground Truth Solution:**
```
down, down, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, left, left, down, down, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d4KVaYDxLvfpxN8P0qO4yQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=123,
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2285
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=123 candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2285 traffic_type=None
```

