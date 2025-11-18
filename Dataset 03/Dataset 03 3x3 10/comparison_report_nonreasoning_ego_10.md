# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_10.jpg` | **0.00%** | `input: 551 , ouput: 19` | `right, forward, right, forward, forward, left, forward, forward, right, forward` |
| `maze_line_3x3_10.json` | **0.00%** | `input: 774 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_10.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_10.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_10.txt` | **0.00%** | `input: 439 , ouput: 650` | `the, maze, is, represented, as, follows:, (0, 0), -, <|updownleft_wall|>, <|origin|>, (0, 1), -, <|updown_wall|>, (0, 2), -, <|upright_wall|>, (1, 0), -, <|upleft_wall|>, (1, 1), -, <|updownright_wall|>, (1, 2), -, <|rightleft_wall|>, (2, 0), -, <|downleft_wall|>, (2, 1), -, <|updown_wall|>, (2, 2), -, <|downright_wall|>, <|target|>, let's, break, down, the, maze, structure:, **row, 0:**, *, (0, 0):, origin., has, walls, on, the, up, down, and, left., this, means, it's, only, accessible, from, the, right., *, (0, 1):, has, walls, on, the, up, and, down., this, means, it, can, only, be, accessed, from, (0, 0), or, (0, 2)., *, (0, 2):, has, walls, on, the, up, and, right., this, means, it, can, only, be, accessed, from, (0, 1), or, (1, 2)., **row, 1:**, *, (1, 0):, has, walls, on, the, up, and, left., this, means, it, can, only, be, accessed, from, (2, 0), or, (0, 1), (though, (0, 1), is, blocked, from, above)., *, (1, 1):, has, walls, on, the, up, down, and, right., this, means, it, can, only, be, accessed, from, (1, 0), or, (2, 1)., *, (1, 2):, has, walls, on, the, right, and, left., this, means, it, can, only, be, accessed, from, (0, 2), or, (2, 2)., **row, 2:**, *, (2, 0):, has, walls, on, the, down, and, left., this, means, it, can, only, be, accessed, from, (1, 0), or, (2, 1)., *, (2, 1):, has, walls, on, the, up, and, down., this, means, it, can, only, be, accessed, from, (2, 0), or, (2, 2)., *, (2, 2):, target., has, walls, on, the, down, and, right., this, means, it, can, only, be, accessed, from, (1, 2), or, (2, 1)., the, agent, starts, at, (0, 0), facing, south., let's, trace, a, path:, 1., **start, at, (0, 0), facing, south.**, 2., from, (0, 0), the, only, possible, move, is, to, the, right., to, move, right, we, need, to, turn, left, (since, we, are, facing, south, left, will, make, us, face, east)., *, action:, left, *, now, at, (0, 0), facing, east., 3., move, forward, to, (0, 1)., *, action:, forward, *, now, at, (0, 1), facing, east., 4., move, forward, to, (0, 2)., *, action:` |
| `maze_occupancy_3x3_10.jpg` | **0.00%** | `input: 546 , ouput: 43` | `right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_10.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_adj_10.json` | **0.00%** | `input: 1298 , ouput: 29` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_10.txt` | **0.00%** | `input: 580 , ouput: 49` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_ascii_10.txt` | **0.00%** | `input: 315 , ouput: 47` | `right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_10.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_10.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G5Qcac7pHODTvdIPsdP1mAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
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
  total_token_count=570
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=570 traffic_type=None
```

### `maze_line_3x3_10.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HJQcaZXsAd20xN8P1r_twQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=785
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=785 traffic_type=None
```

### `maze_line_3x3_adj_10.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
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
        text='right, forward, right, forward, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HJQcafjhJ7jUvdIPjbOpuQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
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
        text='Right, Forward, Right, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HZQcabjRGf_axs0P3PW82Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows:, (0, 0), -, <|updownleft_wall|>, <|origin|>, (0, 1), -, <|updown_wall|>, (0, 2), -, <|upright_wall|>, (1, 0), -, <|upleft_wall|>, (1, 1), -, <|updownright_wall|>, (1, 2), -, <|rightleft_wall|>, (2, 0), -, <|downleft_wall|>, (2, 1), -, <|updown_wall|>, (2, 2), -, <|downright_wall|>, <|target|>, let's, break, down, the, maze, structure:, **row, 0:**, *, (0, 0):, origin., has, walls, on, the, up, down, and, left., this, means, it's, only, accessible, from, the, right., *, (0, 1):, has, walls, on, the, up, and, down., this, means, it, can, only, be, accessed, from, (0, 0), or, (0, 2)., *, (0, 2):, has, walls, on, the, up, and, right., this, means, it, can, only, be, accessed, from, (0, 1), or, (1, 2)., **row, 1:**, *, (1, 0):, has, walls, on, the, up, and, left., this, means, it, can, only, be, accessed, from, (2, 0), or, (0, 1), (though, (0, 1), is, blocked, from, above)., *, (1, 1):, has, walls, on, the, up, down, and, right., this, means, it, can, only, be, accessed, from, (1, 0), or, (2, 1)., *, (1, 2):, has, walls, on, the, right, and, left., this, means, it, can, only, be, accessed, from, (0, 2), or, (2, 2)., **row, 2:**, *, (2, 0):, has, walls, on, the, down, and, left., this, means, it, can, only, be, accessed, from, (1, 0), or, (2, 1)., *, (2, 1):, has, walls, on, the, up, and, down., this, means, it, can, only, be, accessed, from, (2, 0), or, (2, 2)., *, (2, 2):, target., has, walls, on, the, down, and, right., this, means, it, can, only, be, accessed, from, (1, 2), or, (2, 1)., the, agent, starts, at, (0, 0), facing, south., let's, trace, a, path:, 1., **start, at, (0, 0), facing, south.**, 2., from, (0, 0), the, only, possible, move, is, to, the, right., to, move, right, we, need, to, turn, left, (since, we, are, facing, south, left, will, make, us, face, east)., *, action:, left, *, now, at, (0, 0), facing, east., 3., move, forward, to, (0, 1)., *, action:, forward, *, now, at, (0, 1), facing, east., 4., move, forward, to, (0, 2)., *, action:
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

(0,0) - <|updownleft_wall|> <|origin|>
(0,1) - <|updown_wall|>
(0,2) - <|upright_wall|>
(1,0) - <|upleft_wall|>
(1,1) - <|updownright_wall|>
(1,2) - <|rightleft_wall|>
(2,0) - <|downleft_wall|>
(2,1) - <|updown_wall|>
(2,2) - <|downright_wall|> <|target|>

Let's break down the maze structure:

**Row 0:**
*   (0,0): Origin. Has walls on the up, down, and left. This means it's only accessible from the right.
*   (0,1): Has walls on the up and down. This means it can only be accessed from (0,0) or (0,2).
*   (0,2): Has walls on the up and right. This means it can only be accessed from (0,1) or (1,2).

**Row 1:**
*   (1,0): Has walls on the up and left. This means it can only be accessed from (2,0) or (0,1) (though (0,1) is blocked from above).
*   (1,1): Has walls on the up, down, and right. This means it can only be accessed from (1,0) or (2,1).
*   (1,2): Has walls on the right and left. This means it can only be accessed from (0,2) or (2,2).

**Row 2:**
*   (2,0): Has walls on the down and left. This means it can only be accessed from (1,0) or (2,1).
*   (2,1): Has walls on the up and down. This means it can only be accessed from (2,0) or (2,2).
*   (2,2): Target. Has walls on the down and right. This means it can only be accessed from (1,2) or (2,1).

The agent starts at (0,0) facing South.

Let's trace a path:

1.  **Start at (0,0) facing South.**
2.  From (0,0), the only possible move is to the right. To move right, we need to turn Left (since we are facing South, Left will make us face East).
    *   Action: Left
    *   Now at (0,0) facing East.
3.  Move forward to (0,1).
    *   Action: Forward
    *   Now at (0,1) facing East.
4.  Move forward to (0,2).
    *   Action:"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IJQcadnGAoDXvdIPwbrDyAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_10.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,left,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IZQcac3mBLDTxN8Pj8DlmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
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
  total_token_count=589
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=589 traffic_type=None
```

### `maze_occupancy_3x3_10.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, Right, forward, forward, forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward, forward, forward, forward, Forward, Right, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I5QcaeiUE-XZxs0P5LjvsAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_10.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JJQcaaj7Dc3VvdIP5qGjwQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1327
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1327 traffic_type=None
```

### `maze_occupancy_3x3_adj_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JZQcafrODev_vdIP4IWYuAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=629
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=629 traffic_type=None
```

### `maze_occupancy_3x3_ascii_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JZQcaabGOu61vdIP3vbMwQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=362
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=362 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, right, forward, forward, forward, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KJQcaeXAEKTyxs0PnYinqAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

