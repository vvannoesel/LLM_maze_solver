# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_2.jpg` | **0.00%** | `input: 421 , ouput: 218` | `the, maze, can, be, represented, as, a, 3x3, grid., the, start, (circle), is, in, cell, (0, 0)., the, end, (star), is, in, cell, (2, 2)., the, walls, are, located, as, follows:, -, between, (0, 0), and, (0, 1), -, between, (1, 0), and, (1, 1), -, between, (0, 1), and, (1, 1), -, between, (1, 1), and, (1, 2), -, between, (1, 1), and, (2, 1), let's, trace, a, path:, from, (0, 0), we, can, move, down, to, (1, 0)., from, (1, 0), we, can, move, right, to, (1, 1)., from, (1, 1), we, can, move, down, to, (2, 1)., from, (2, 1), we, can, move, right, to, (2, 2)., the, sequence, of, moves, is:, down, right, down, right., down, right, down, right` |
| `maze_line_3x3_2.json` | **0.00%** | `input: 644 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_2.json` | **0.00%** | `input: 706 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_2.txt` | **100.00%** | `input: 338 , ouput: 7` | `right, down, right, down` |
| `maze_line_3x3_tokenized_2.txt` | **100.00%** | `input: 309 , ouput: 7` | `right, down, right, down` |
| `maze_occupancy_3x3_2.jpg` | **0.00%** | `input: 416 , ouput: 15` | `down, right, right, down, right, down, right, down` |
| `maze_occupancy_3x3_2.json` | **0.00%** | `input: 459 , ouput: 21` | `down, right, right, down, down, right, right, down, down, right, right` |
| `maze_occupancy_3x3_adj_2.json` | **25.00%** | `input: 1168 , ouput: 15` | `right, right, right, down, down, right, right, right` |
| `maze_occupancy_3x3_adj_2.txt` | **25.00%** | `input: 450 , ouput: 17` | `right, right, right, down, right, down, right, down, right` |
| `maze_occupancy_3x3_ascii_2.txt` | **110.00%** | `input: 187 , ouput: 29` | `right, right, down, down, right, right, down, down, left, left, left, down, right, right, right` |
| `maze_occupancy_3x3_tokenized_2.txt` | **0.00%** | `input: 738 , ouput: 59` | `down, right, right, right, down, down, down, down, right, right, right, up, up, right, down, down, down, down, right, right, right, up, up, up, up, up, right, right, right, up` |

---

## Full LLM Responses

### `maze_line_3x3_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, down
```

**Extracted Answer:**
```
the, maze, can, be, represented, as, a, 3x3, grid., the, start, (circle), is, in, cell, (0, 0)., the, end, (star), is, in, cell, (2, 2)., the, walls, are, located, as, follows:, -, between, (0, 0), and, (0, 1), -, between, (1, 0), and, (1, 1), -, between, (0, 1), and, (1, 1), -, between, (1, 1), and, (1, 2), -, between, (1, 1), and, (2, 1), let's, trace, a, path:, from, (0, 0), we, can, move, down, to, (1, 0)., from, (1, 0), we, can, move, right, to, (1, 1)., from, (1, 1), we, can, move, down, to, (2, 1)., from, (2, 1), we, can, move, right, to, (2, 2)., the, sequence, of, moves, is:, down, right, down, right., down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze can be represented as a 3x3 grid.
The start (circle) is in cell (0,0).
The end (star) is in cell (2,2).

The walls are located as follows:
- Between (0,0) and (0,1)
- Between (1,0) and (1,1)
- Between (0,1) and (1,1)
- Between (1,1) and (1,2)
- Between (1,1) and (2,1)

Let's trace a path:
From (0,0), we can move down to (1,0).
From (1,0), we can move right to (1,1).
From (1,1), we can move down to (2,1).
From (2,1), we can move right to (2,2).

The sequence of moves is: down, right, down, right.

down,right,down,right"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hLkVacnsHvXpvdIPiq_ziA0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=218,
  prompt_token_count=421,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=163
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=639
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=421 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=218 candidates_tokens_details=None prompt_token_count=421 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=163
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=639 traffic_type=None
```

### `maze_line_3x3_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, down
```

**Extracted Answer:**
```
down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hLkVadXZN7SavdIP45PkmAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=644,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=644
    ),
  ],
  total_token_count=651
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=179 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=644 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=644
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=651 traffic_type=None
```

### `maze_line_3x3_adj_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, down
```

**Extracted Answer:**
```
down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hbkVadCVHMPvxN8P6_-b-Aw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=706,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=706
    ),
  ],
  total_token_count=713
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=150 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=706 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=706
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=713 traffic_type=None
```

### `maze_line_3x3_adj_2.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, down, right, down
```

**Extracted Answer:**
```
right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hbkVabWlM_TDxN8P6pOj-Aw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=338,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=338
    ),
  ],
  total_token_count=345
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=183 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=338 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=338
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=345 traffic_type=None
```

### `maze_line_3x3_tokenized_2.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, down, right, down
```

**Extracted Answer:**
```
right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hrkVaa2aHYLwxN8Pi7z2aQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=309,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=309
    ),
  ],
  total_token_count=316
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=181 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=309 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=309
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=316 traffic_type=None
```

### `maze_occupancy_3x3_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='h7kVadGyMLzzxs0PzYav8QM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=416,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=158
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
) total_tokens=416 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=416 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=158
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=431 traffic_type=None
```

### `maze_occupancy_3x3_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iLkVabmFGfeO28oP4JqDiAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=459,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=459
    ),
  ],
  total_token_count=480
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=159 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=459 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=459
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=480 traffic_type=None
```

### `maze_occupancy_3x3_adj_2.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iLkVad7UNeauvdIP9M6BoQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=1168,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1168
    ),
  ],
  total_token_count=1183
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=150 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=1168 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1168
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1183 traffic_type=None
```

### `maze_occupancy_3x3_adj_2.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ibkVaY32HfXpvdIPiq_ziA0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=450,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=450
    ),
  ],
  total_token_count=467
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=183 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=450 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=450
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=467 traffic_type=None
```

### `maze_occupancy_3x3_ascii_2.txt`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, left, left, left, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,left,left,left,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ibkVadngN7zYxs0P64im0Qw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=187,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=187
    ),
  ],
  total_token_count=216
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=158 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=187 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=187
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=216 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, right, down, down, down, down, right, right, right, up, up, right, down, down, down, down, right, right, right, up, up, up, up, up, right, right, right, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,down,down,down,down,right,right,right,up,up,right,down,down,down,down,right,right,right,up,up,up,up,up,right,right,right,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='irkVaY3hHovUxN8PmPOuoAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=738,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=738
    ),
  ],
  total_token_count=797
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=183 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=738 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=738
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=797 traffic_type=None
```

