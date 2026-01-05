# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_7.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_7.json` | **0.00%** | `input: 774 , ouput: 17` | `right, forward, right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_adj_7.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_adj_7.txt` | **0.00%** | `input: 468 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_tokenized_7.txt` | **0.00%** | `input: 439 , ouput: 650` | `the, maze, is, represented, as, follows:, (0, 0):, <|updownleft_wall|>, <|origin|>, (0, 1):, <|upright_wall|>, (0, 2):, <|uprightleft_wall|>, (1, 0):, <|uprightleft_wall|>, (1, 1):, <|downleft_wall|>, (1, 2):, <|right_wall|>, (2, 0):, <|downleft_wall|>, (2, 1):, <|updown_wall|>, (2, 2):, <|downright_wall|>, <|target|>, the, agent, starts, at, (0, 0), facing, south., let's, analyze, the, walls:, (0, 0), has, walls, up, down, left., this, means, it, can, only, move, right., (0, 1), has, walls, up, right., this, means, it, can, move, down, left., (0, 2), has, walls, up, right, left., this, means, it, can, only, move, down., (1, 0), has, walls, up, right, left., this, means, it, can, only, move, down., (1, 1), has, walls, down, left., this, means, it, can, move, up, right., (1, 2), has, walls, right., this, means, it, can, move, up, down, left., (2, 0), has, walls, down, left., this, means, it, can, move, up, right., (2, 1), has, walls, up, down., this, means, it, can, move, left, right., (2, 2), has, walls, down, right., this, means, it, can, move, up, left., the, agent, starts, at, (0, 0), facing, south., from, (0, 0), the, only, possible, move, is, to, the, right., 1., **start, at, (0, 0), facing, south.**, -, the, agent, cannot, move, forward, (south), due, to, a, wall., -, the, agent, cannot, move, left, (east), due, to, a, wall., -, the, agent, must, turn, right, to, face, east, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (0, 1), facing, east), 2., **at, (0, 1), facing, east.**, -, the, agent, cannot, move, forward, (east), due, to, a, wall., -, the, agent, must, turn, right, to, face, south, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (1, 1), facing, south), 3., **at, (1, 1), facing, south.**, -, the, agent, cannot, move, forward, (south), due, to, a, wall., -, the, agent, must, turn, right, to, face, west, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (1, 0), facing, west), 4., **at, (1, 0), facing, west.**, -, the, agent, cannot, move, forward, (west), due, to, a, wall., -, the, agent, must, turn, right, to, face, north, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (` |
| `maze_occupancy_3x3_7.jpg` | **0.00%** | `input: 546 , ouput: 35` | `forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, left, forward` |
| `maze_occupancy_3x3_7.json` | **0.00%** | `input: 589 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_7.json` | **0.00%** | `input: 1298 , ouput: 41` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_7.txt` | **0.00%** | `input: 580 , ouput: 49` | `right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_ascii_7.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward` |
| `maze_occupancy_3x3_tokenized_7.txt` | **0.00%** | `input: 867 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left` |

---

## Full LLM Responses

### `maze_line_3x3_7.jpg`

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
        text='right,forward,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3pMcadKFKq3-vdIPhvD6kAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_7.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,right,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='35McaZGrFe64vdIP3oP06Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=791
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=791 traffic_type=None
```

### `maze_line_3x3_adj_7.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='35McaeGYN_bWvdIPtdaroQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_7.txt`

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
        text='Right, Forward, Right, Forward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4JMcafWeKofYxs0PzZjGyQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, left, right
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows:, (0, 0):, <|updownleft_wall|>, <|origin|>, (0, 1):, <|upright_wall|>, (0, 2):, <|uprightleft_wall|>, (1, 0):, <|uprightleft_wall|>, (1, 1):, <|downleft_wall|>, (1, 2):, <|right_wall|>, (2, 0):, <|downleft_wall|>, (2, 1):, <|updown_wall|>, (2, 2):, <|downright_wall|>, <|target|>, the, agent, starts, at, (0, 0), facing, south., let's, analyze, the, walls:, (0, 0), has, walls, up, down, left., this, means, it, can, only, move, right., (0, 1), has, walls, up, right., this, means, it, can, move, down, left., (0, 2), has, walls, up, right, left., this, means, it, can, only, move, down., (1, 0), has, walls, up, right, left., this, means, it, can, only, move, down., (1, 1), has, walls, down, left., this, means, it, can, move, up, right., (1, 2), has, walls, right., this, means, it, can, move, up, down, left., (2, 0), has, walls, down, left., this, means, it, can, move, up, right., (2, 1), has, walls, up, down., this, means, it, can, move, left, right., (2, 2), has, walls, down, right., this, means, it, can, move, up, left., the, agent, starts, at, (0, 0), facing, south., from, (0, 0), the, only, possible, move, is, to, the, right., 1., **start, at, (0, 0), facing, south.**, -, the, agent, cannot, move, forward, (south), due, to, a, wall., -, the, agent, cannot, move, left, (east), due, to, a, wall., -, the, agent, must, turn, right, to, face, east, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (0, 1), facing, east), 2., **at, (0, 1), facing, east.**, -, the, agent, cannot, move, forward, (east), due, to, a, wall., -, the, agent, must, turn, right, to, face, south, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (1, 1), facing, south), 3., **at, (1, 1), facing, south.**, -, the, agent, cannot, move, forward, (south), due, to, a, wall., -, the, agent, must, turn, right, to, face, west, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (1, 0), facing, west), 4., **at, (1, 0), facing, west.**, -, the, agent, cannot, move, forward, (west), due, to, a, wall., -, the, agent, must, turn, right, to, face, north, and, then, move, forward., -, **instruction:, right, forward**, (now, at, (
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

The agent starts at (0,0) facing South.

Let's analyze the walls:
(0,0) has walls up, down, left. This means it can only move right.
(0,1) has walls up, right. This means it can move down, left.
(0,2) has walls up, right, left. This means it can only move down.

(1,0) has walls up, right, left. This means it can only move down.
(1,1) has walls down, left. This means it can move up, right.
(1,2) has walls right. This means it can move up, down, left.

(2,0) has walls down, left. This means it can move up, right.
(2,1) has walls up, down. This means it can move left, right.
(2,2) has walls down, right. This means it can move up, left.

The agent starts at (0,0) facing South.
From (0,0), the only possible move is to the right.

1. **Start at (0,0), facing South.**
   - The agent cannot move forward (South) due to a wall.
   - The agent cannot move left (East) due to a wall.
   - The agent must turn right to face East and then move forward.
   - **Instruction: Right, Forward** (Now at (0,1), facing East)

2. **At (0,1), facing East.**
   - The agent cannot move forward (East) due to a wall.
   - The agent must turn right to face South and then move forward.
   - **Instruction: Right, Forward** (Now at (1,1), facing South)

3. **At (1,1), facing South.**
   - The agent cannot move forward (South) due to a wall.
   - The agent must turn right to face West and then move forward.
   - **Instruction: Right, Forward** (Now at (1,0), facing West)

4. **At (1,0), facing West.**
   - The agent cannot move forward (West) due to a wall.
   - The agent must turn right to face North and then move forward.
   - **Instruction: Right, Forward** (Now at ("""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5JMcabngDYLaxs0PwvHjwQ4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_7.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5pMcaZzWF9j9xN8PsaeMoAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
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
  total_token_count=581
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=581 traffic_type=None
```

### `maze_occupancy_3x3_7.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6JMcaazcHYrkvdIPipOBkQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_adj_7.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6ZMcaaLKDeaavdIPio31oQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=1298,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1298
    ),
  ],
  total_token_count=1339
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=1298 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1298
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1339 traffic_type=None
```

### `maze_occupancy_3x3_adj_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6pMcaYu4EO3Zxs0PsZuluAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_ascii_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Forward,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7JMcafCjJMidvdIPw_Pg0Ak' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='75McaajMFcidvdIPw_Pg0Ak' usage_metadata=GenerateContentResponseUsageMetadata(
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

