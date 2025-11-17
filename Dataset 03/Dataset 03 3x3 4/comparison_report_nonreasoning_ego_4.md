# LLM Maze Solving Comparison Report

 NEW ASCII

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_4.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_4.json` | **0.00%** | `input: 774 , ouput: 19` | `right, forward, right, forward, forward, left, forward, forward, left, forward` |
| `maze_line_3x3_adj_4.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_4.txt` | **0.00%** | `input: 468 , ouput: 11` | `right, forward, forward, right, forward, forward` |
| `maze_line_3x3_tokenized_4.txt` | **0.00%** | `input: 439 , ouput: 649` | `the, maze, is, represented, as, follows:, (0, 0):, <|updownleft_wall|>, <|origin|>, (0, 1):, <|upright_wall|>, (0, 2):, <|uprightleft_wall|>, (1, 0):, <|uprightleft_wall|>, (1, 1):, <|downleft_wall|>, (1, 2):, <|right_wall|>, (2, 0):, <|downleft_wall|>, (2, 1):, <|updown_wall|>, (2, 2):, <|downright_wall|>, <|target|>, let's, analyze, the, walls, for, each, cell:, (0, 0):, no, walls, specified, except, for, the, origin, marker., assuming, it, has, walls, on, the, top, bottom, and, left, as, per, token., (0, 1):, wall, on, the, top, and, right., (0, 2):, wall, on, the, top, right, and, left., (1, 0):, wall, on, the, top, right, and, left., (1, 1):, wall, on, the, bottom, and, left., (1, 2):, wall, on, the, right., (2, 0):, wall, on, the, bottom, and, left., (2, 1):, wall, on, the, top, and, bottom., (2, 2):, wall, on, the, bottom, and, right, and, target, marker., the, agent, starts, at, (0, 0), facing, south., let's, trace, the, possible, moves:, start, at, (0, 0), facing, south., 1., **forward:**, agent, is, at, (0, 0), facing, south., the, cell, below, (0, 0), is, (1, 0)., cell, (1, 0), has, <|uprightleft_wall|>, meaning, it, has, walls, on, the, top, right, and, left., this, implies, a, wall, between, (0, 0), and, (1, 0)., so, cannot, move, forward., 2., **left:**, agent, is, at, (0, 0), facing, south., turning, left, means, facing, east., move, forward., agent, moves, to, (0, 1)., *, current, position:, (0, 1), *, facing:, east, *, cell, (0, 1), has, <|upright_wall|>., this, means, walls, on, top, and, right., there, is, no, wall, on, the, left, or, bottom., so, moving, from, (0, 0), to, (0, 1), is, valid., 3., **forward:**, agent, is, at, (0, 1), facing, east., the, cell, to, the, right, is, (0, 2)., cell, (0, 2), has, <|uprightleft_wall|>., this, means, walls, on, top, right, and, left., there, is, no, wall, on, the, bottom., so, moving, from, (0, 1), to, (0, 2), is, valid., *, current, position:, (0, 2), *, facing:, east, *, cell, (0, 2), has, <|uprightleft_wall|>., this, implies, a, wall, to, the, right., so, cannot, move, forward., 4.` |
| `maze_occupancy_3x3_4.jpg` | **0.00%** | `input: 546 , ouput: 23` | `forward, right, forward, forward, right, forward, left, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_4.json` | **0.00%** | `input: 589 , ouput: 55` | `right, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_4.json` | **0.00%** | `input: 1298 , ouput: 99` | `right, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_4.txt` | **0.00%** | `input: 580 , ouput: 49` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_4.txt` | **0.00%** | `input: 317 , ouput: 35` | `right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_tokenized_4.txt` | **0.00%** | `input: 868 , ouput: 49` | `right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_4.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aTQbacuEH4ubkdUPm9DxmAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
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
  total_token_count=566
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=566 traffic_type=None
```

### `maze_line_3x3_4.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ajQbaf34C7iG7M8P-tGX6Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=793
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=793 traffic_type=None
```

### `maze_line_3x3_adj_4.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ajQbaf6MKMri7M8PldH0sAs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='azQbaeO3FsPMnsEP3YrsqQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=479
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=479 traffic_type=None
```

### `maze_line_3x3_tokenized_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows:, (0, 0):, <|updownleft_wall|>, <|origin|>, (0, 1):, <|upright_wall|>, (0, 2):, <|uprightleft_wall|>, (1, 0):, <|uprightleft_wall|>, (1, 1):, <|downleft_wall|>, (1, 2):, <|right_wall|>, (2, 0):, <|downleft_wall|>, (2, 1):, <|updown_wall|>, (2, 2):, <|downright_wall|>, <|target|>, let's, analyze, the, walls, for, each, cell:, (0, 0):, no, walls, specified, except, for, the, origin, marker., assuming, it, has, walls, on, the, top, bottom, and, left, as, per, token., (0, 1):, wall, on, the, top, and, right., (0, 2):, wall, on, the, top, right, and, left., (1, 0):, wall, on, the, top, right, and, left., (1, 1):, wall, on, the, bottom, and, left., (1, 2):, wall, on, the, right., (2, 0):, wall, on, the, bottom, and, left., (2, 1):, wall, on, the, top, and, bottom., (2, 2):, wall, on, the, bottom, and, right, and, target, marker., the, agent, starts, at, (0, 0), facing, south., let's, trace, the, possible, moves:, start, at, (0, 0), facing, south., 1., **forward:**, agent, is, at, (0, 0), facing, south., the, cell, below, (0, 0), is, (1, 0)., cell, (1, 0), has, <|uprightleft_wall|>, meaning, it, has, walls, on, the, top, right, and, left., this, implies, a, wall, between, (0, 0), and, (1, 0)., so, cannot, move, forward., 2., **left:**, agent, is, at, (0, 0), facing, south., turning, left, means, facing, east., move, forward., agent, moves, to, (0, 1)., *, current, position:, (0, 1), *, facing:, east, *, cell, (0, 1), has, <|upright_wall|>., this, means, walls, on, top, and, right., there, is, no, wall, on, the, left, or, bottom., so, moving, from, (0, 0), to, (0, 1), is, valid., 3., **forward:**, agent, is, at, (0, 1), facing, east., the, cell, to, the, right, is, (0, 2)., cell, (0, 2), has, <|uprightleft_wall|>., this, means, walls, on, top, right, and, left., there, is, no, wall, on, the, bottom., so, moving, from, (0, 1), to, (0, 2), is, valid., *, current, position:, (0, 2), *, facing:, east, *, cell, (0, 2), has, <|uprightleft_wall|>., this, implies, a, wall, to, the, right., so, cannot, move, forward., 4.
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
(0,0): <|updownleft_wall|> <|origin|>
(0,1): <|upright_wall|>
(0,2): <|uprightleft_wall|>
(1,0): <|uprightleft_wall|>
(1,1): <|downleft_wall|>
(1,2): <|right_wall|>
(2,0): <|downleft_wall|>
(2,1): <|updown_wall|>
(2,2): <|downright_wall|> <|target|>

Let's analyze the walls for each cell:
(0,0): No walls specified except for the origin marker. Assuming it has walls on the top, bottom, and left as per token.
(0,1): Wall on the top and right.
(0,2): Wall on the top, right, and left.
(1,0): Wall on the top, right, and left.
(1,1): Wall on the bottom and left.
(1,2): Wall on the right.
(2,0): Wall on the bottom and left.
(2,1): Wall on the top and bottom.
(2,2): Wall on the bottom and right, and target marker.

The agent starts at (0,0) facing South.

Let's trace the possible moves:

Start at (0,0) facing South.

1.  **Forward:** Agent is at (0,0) facing South. The cell below (0,0) is (1,0). Cell (1,0) has <|uprightleft_wall|>, meaning it has walls on the top, right, and left. This implies a wall between (0,0) and (1,0). So, cannot move forward.

2.  **Left:** Agent is at (0,0) facing South. Turning left means facing East. Move forward. Agent moves to (0,1).
    *   Current position: (0,1)
    *   Facing: East
    *   Cell (0,1) has <|upright_wall|>. This means walls on top and right. There is no wall on the left or bottom. So moving from (0,0) to (0,1) is valid.

3.  **Forward:** Agent is at (0,1) facing East. The cell to the right is (0,2). Cell (0,2) has <|uprightleft_wall|>. This means walls on top, right, and left. There is no wall on the bottom. So moving from (0,1) to (0,2) is valid.
    *   Current position: (0,2)
    *   Facing: East
    *   Cell (0,2) has <|uprightleft_wall|>. This implies a wall to the right. So, cannot move forward.

4.  """
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bjQbaa-TGN63kdUP2uHNiA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=649,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=1088
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=649 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1088 traffic_type=None
```

### `maze_occupancy_3x3_4.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, left, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,left,forward,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bzQbaamsE5j6nsEPq4PH4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=569
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=569 traffic_type=None
```

### `maze_occupancy_3x3_4.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,forward,forward,forward,right,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,right,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bzQbaYSgON63kdUP2uHNiA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=644
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=644 traffic_type=None
```

### `maze_occupancy_3x3_adj_4.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cDQbaaaZNpm4nsEPzJTKkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=99,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1397
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=99 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1397 traffic_type=None
```

### `maze_occupancy_3x3_adj_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cTQbab3ZJ6LnnsEPzJum2A4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,right,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cjQbaaSiGPHikdUPq5K_6Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=352
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=352 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='czQbafDqBtWpnsEPms2uiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=868,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=868
    ),
  ],
  total_token_count=917
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=868 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=868
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=917 traffic_type=None
```

