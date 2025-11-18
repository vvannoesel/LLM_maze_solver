# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_10.jpg` | **0.00%** | `input: 427 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_10.json` | **0.00%** | `input: 650 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_adj_10.json` | **100.00%** | `input: 712 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_adj_10.txt` | **100.00%** | `input: 344 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_tokenized_10.txt` | **25.00%** | `input: 315 , ouput: 7` | `right, down, right, down` |
| `maze_occupancy_3x3_10.jpg` | **0.00%** | `input: 422 , ouput: 198` | `the, maze, can, be, represented, as, a, grid., the, start, is, at, (0, 1), and, the, end, is, at, (4, 5)., here, is, a, step-by-step, solution:, from, (0, 1), move, down, to, (1, 1)., from, (1, 1), move, right, to, (1, 2)., from, (1, 2), move, right, to, (1, 3)., from, (1, 3), move, down, to, (2, 3)., from, (2, 3), move, down, to, (3, 3)., from, (3, 3), move, right, to, (3, 4)., from, (3, 4), move, right, to, (3, 5)., from, (3, 5), move, down, to, (4, 5)., the, sequence, of, moves, is:, down, right, right, down, down, right, right, down., down, right, right, down, down, right, right, down` |
| `maze_occupancy_3x3_10.json` | **87.50%** | `input: 465 , ouput: 35` | `right, right, right, right, down, down, down, right, down, left, left, left, left, down, right, right, right, right` |
| `maze_occupancy_3x3_adj_10.json` | **110.00%** | `input: 1174 , ouput: 19` | `right, right, right, right, down, down, down, down, right, right` |
| `maze_occupancy_3x3_adj_10.txt` | **110.00%** | `input: 456 , ouput: 19` | `right, right, right, right, down, down, down, down, right, right` |
| `maze_occupancy_3x3_ascii_10.txt` | **0.00%** | `input: 191 , ouput: 29` | `down, right, right, right, right, down, down, down, left, left, left, down, down, right, right` |
| `maze_occupancy_3x3_tokenized_10.txt` | **110.00%** | `input: 743 , ouput: 650` | `right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right` |

---

## Full LLM Responses

### `maze_line_3x3_10.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
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
        text='down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='goocafPtLM-5kdUPlt7QyAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=427,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=169
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=434
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=427 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=434 traffic_type=None
```

### `maze_line_3x3_10.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down
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
        text='down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='g4ocaeSUIoPOnsEP9aWA-AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=650,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=650
    ),
  ],
  total_token_count=657
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=185 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=650 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=650
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=657 traffic_type=None
```

### `maze_line_3x3_adj_10.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hIocafjSDJK0nsEPg4zDwAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=712,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=712
    ),
  ],
  total_token_count=719
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=712 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=712
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=719 traffic_type=None
```

### `maze_line_3x3_adj_10.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hIocadjdMPG4kdUPtcqRwAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=344,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=344
    ),
  ],
  total_token_count=351
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=344 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=344
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=351 traffic_type=None
```

### `maze_line_3x3_tokenized_10.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hYocadjjIq6mkdUP4uDPsQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=322
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=187 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=322 traffic_type=None
```

### `maze_occupancy_3x3_10.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
the, maze, can, be, represented, as, a, grid., the, start, is, at, (0, 1), and, the, end, is, at, (4, 5)., here, is, a, step-by-step, solution:, from, (0, 1), move, down, to, (1, 1)., from, (1, 1), move, right, to, (1, 2)., from, (1, 2), move, right, to, (1, 3)., from, (1, 3), move, down, to, (2, 3)., from, (2, 3), move, down, to, (3, 3)., from, (3, 3), move, right, to, (3, 4)., from, (3, 4), move, right, to, (3, 5)., from, (3, 5), move, down, to, (4, 5)., the, sequence, of, moves, is:, down, right, right, down, down, right, right, down., down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze can be represented as a grid. The start is at (0,1) and the end is at (4,5).
Here is a step-by-step solution:
From (0,1) move down to (1,1).
From (1,1) move right to (1,2).
From (1,2) move right to (1,3).
From (1,3) move down to (2,3).
From (2,3) move down to (3,3).
From (3,3) move right to (3,4).
From (3,4) move right to (3,5).
From (3,5) move down to (4,5).

The sequence of moves is: down, right, right, down, down, right, right, down.

down,right,right,down,down,right,right,down"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iIocaeGqFf7tkdUPu_KDwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=198,
  prompt_token_count=422,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=164
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=620
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=422 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=198 candidates_tokens_details=None prompt_token_count=422 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=164
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=620 traffic_type=None
```

### `maze_occupancy_3x3_10.json`

**Score:** 87.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, right, down, left, left, left, left, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,right,down,left,left,left,left,down,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iYocaZydFNDk7M8P5Jv86AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=465,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=465
    ),
  ],
  total_token_count=500
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=465 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=465
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=500 traffic_type=None
```

### `maze_occupancy_3x3_adj_10.json`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iYocabf5O4WQkdUPppzakAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1174,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1174
    ),
  ],
  total_token_count=1193
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1174 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1174
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1193 traffic_type=None
```

### `maze_occupancy_3x3_adj_10.txt`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ioocaff0JOCckdUPvdnj0QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=456,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=456
    ),
  ],
  total_token_count=475
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=456 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=456
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=475 traffic_type=None
```

### `maze_occupancy_3x3_ascii_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, right, right, right, down, down, down, left, left, left, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,down,down,down,left,left,left,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i4ocac3XDKXrkdUPm7nk2AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=191,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=191
    ),
  ],
  total_token_count=220
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=164 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=191 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=191
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=220 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_10.txt`

**Score:** 110.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, up, up, up, up, up, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,right,down,down,down,down,left,left,left,left,down,down,right,right,right,right,up,up,up,up,up,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jYocadycNIu3nsEP6N6_uAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=743,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=743
    ),
  ],
  total_token_count=1393
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=188 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=743 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=743
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1393 traffic_type=None
```

