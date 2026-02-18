# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_49.jpg` | **0.00%** | `input: 551 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_49.json` | **0.00%** | `input: 774 , ouput: 21` | `right, forward, right, forward, left, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_49.json` | **0.00%** | `input: 836 , ouput: 23` | `right, forward, right, forward, forward, right, forward, forward, left, forward, left, forward` |
| `maze_line_3x3_adj_49.txt` | **0.00%** | `input: 468 , ouput: 15` | `right, forward, right, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_49.txt` | **0.00%** | `input: 439 , ouput: 145` | `the, maze, description, provided, is, incomplete, as, it, does, not, specify, the, connections, between, cells, only, their, walls., without, knowing, which, walls, are, present, between, adjacent, cells, it, is, impossible, to, determine, a, valid, path., please, provide, a, complete, description, of, the, maze, indicating, the, walls, for, each, cell, and, the, connections, to, adjacent, cells., for, example, a, cell, description, might, look, like:, "<|0-0|>, <|up_wall|>, <|down_wall|>, <|left_wall|>, <|origin|>", indicating, that, there, are, walls, to, the, up, down, and, left, of, cell, (0, 0), and, it, is, the, origin., once, a, complete, maze, description, is, provided, i, can, generate, the, sequence, of, instructions.` |
| `maze_occupancy_3x3_49.jpg` | **0.00%** | `input: 546 , ouput: 29` | `forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward` |
| `maze_occupancy_3x3_49.json` | **0.00%** | `input: 589 , ouput: 650` | `forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward` |
| `maze_occupancy_3x3_adj_49.json` | **0.00%** | `input: 1292 , ouput: 45` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_49.txt` | **0.00%** | `input: 580 , ouput: 49` | `forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_49.txt` | **0.00%** | `input: 313 , ouput: 650` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left` |
| `maze_occupancy_3x3_tokenized_49.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_49.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='C5yVaaPZJrW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
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
  total_token_count=564
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=564 traffic_type=None
```

### `maze_line_3x3_49.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, left, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Left, Forward, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DJyVafrbIYTensEP6bbt4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=795
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=795 traffic_type=None
```

### `maze_line_3x3_adj_49.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, right, forward, forward, left, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DJyVaYS6PKeN7M8P-7HT8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=859
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=859 traffic_type=None
```

### `maze_line_3x3_adj_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DZyVabPbF9qgkdUPg_fLkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=483
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=483 traffic_type=None
```

### `maze_line_3x3_tokenized_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, right, forward, left, left, forward
```

**Extracted Answer:**
```
the, maze, description, provided, is, incomplete, as, it, does, not, specify, the, connections, between, cells, only, their, walls., without, knowing, which, walls, are, present, between, adjacent, cells, it, is, impossible, to, determine, a, valid, path., please, provide, a, complete, description, of, the, maze, indicating, the, walls, for, each, cell, and, the, connections, to, adjacent, cells., for, example, a, cell, description, might, look, like:, "<|0-0|>, <|up_wall|>, <|down_wall|>, <|left_wall|>, <|origin|>", indicating, that, there, are, walls, to, the, up, down, and, left, of, cell, (0, 0), and, it, is, the, origin., once, a, complete, maze, description, is, provided, i, can, generate, the, sequence, of, instructions.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze description provided is incomplete, as it does not specify the connections between cells, only their walls. Without knowing which walls are present between adjacent cells, it is impossible to determine a valid path.

Please provide a complete description of the maze, indicating the walls for each cell and the connections to adjacent cells. For example, a cell description might look like: "<|0-0|> <|up_wall|> <|down_wall|> <|left_wall|> <|origin|>" indicating that there are walls to the up, down, and left of cell (0,0), and it is the origin.

Once a complete maze description is provided, I can generate the sequence of instructions."""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DpyVafn8F4OH7M8PxuqcmAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=145,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=584
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=145 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=584 traffic_type=None
```

### `maze_occupancy_3x3_49.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,left,forward,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DpyVafzcOqnw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
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
  total_token_count=575
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=575 traffic_type=None
```

### `maze_occupancy_3x3_49.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,forward,left,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EJyVaaSGEKSDkdUP5IaYkQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_49.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EJyVad21Lu3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1337
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1337 traffic_type=None
```

### `maze_occupancy_3x3_adj_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,forward,forward,right,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EZyVadOzGqPwnsEPgLOouAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, backward, forward, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,backward,forward,forward,forward,forward,forward,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EpyVaZ7wMpHw7M8Pi4iBgAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=313,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=313
    ),
  ],
  total_token_count=963
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=313 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=313
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=963 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_49.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FJyVaf2MMYOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
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

