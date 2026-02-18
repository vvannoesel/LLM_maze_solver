# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_42.jpg` | **14.29%** | `input: 434 , ouput: 21` | `right, down, right, down, down, right, right, up, right, down, down` |
| `maze_line_6x6_42.json` | **14.29%** | `input: 1809 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_adj_42.json` | **14.29%** | `input: 2258 , ouput: 19` | `right, down, down, down, down, right, right, right, right, down` |
| `maze_line_6x6_adj_42.txt` | **7.14%** | `input: 729 , ouput: 19` | `right, right, right, right, right, down, down, down, down, down` |
| `maze_line_6x6_tokenized_42.txt` | **0.00%** | `input: 673 , ouput: 650` | `the, maze, is, 6x6., let's, denote, cells, by, (row, column)., the, start, is, at, (0, 0), and, the, end, is, at, (5, 5)., here, is, a, breakdown, of, the, maze, and, the, walls:, (0, 0):, <|updownleft_wall|>, <|origin|>, -, walls:, up, down, left., can, move, right., (0, 1):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (0, 2):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (0, 3):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (0, 4):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (0, 5):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (1, 0):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (1, 1):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (1, 2):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (1, 3):, <|downleft_wall|>, -, walls:, down, left., can, move, up, right., (1, 4):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (1, 5):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (2, 0):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (2, 1):, <|updownleft_wall|>, -, walls:, up, down, left., can, move, right., (2, 2):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (2, 3):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (2, 4):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (2, 5):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (3, 0):, <|downleft_wall|>, -, walls:, down, left., can, move, up, right., (3, 1):, <|updown_wall|>, -, walls:, up, down., can, move, left, right., (3, 2):, <|updown_wall|>, -, walls:, up, down., can, move, left, right., (3, 3):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (3, 4):, <|downleft_wall|>, -, walls:, down, left., can, move` |
| `maze_occupancy_6x6_42.jpg` | **0.00%** | `input: 431 , ouput: 650` | `down, right, down, right, down, left, down, right, down, right, right, up, right, down, right, down, left, down, right, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down` |
| `maze_occupancy_6x6_42.json` | **14.29%** | `input: 988 , ouput: 650` | `right, right, down, down, down, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, right, down, right, down, down, down, down, down, down, down, down, down, down, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |
| `maze_occupancy_6x6_adj_42.json` | **7.14%** | `input: 4341 , ouput: 49` | `right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_42.txt` | **nan%** | `input: 1278 , ouput: 0` | `` |
| `maze_occupancy_6x6_ascii_42.txt` | **0.00%** | `input: 245 , ouput: 650` | `down, down, right, right, down, down, right, right, right, down, down, right, right, down, right, down, right, right, right, down, right, down, down, right, right, right, right, right, up, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_tokenized_42.txt` | **nan%** | `input: 2162 , ouput: 0` | `` |

---

## Full LLM Responses

### `maze_line_6x6_42.jpg`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, right, up, right, down, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4oSVae3DDK2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
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
  total_token_count=455
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=455 traffic_type=None
```

### `maze_line_6x6_42.json`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, right, up, right, down, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4oSVafXbL_367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1828
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1828 traffic_type=None
```

### `maze_line_6x6_adj_42.json`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, right, up, right, down, right, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, down, down, right, right, right, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='44SVab_LIo65kdUPzNPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_42.txt`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, right, up, right, down, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5ISVaYuqEeO9kdUPqsTX2Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=748
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=748 traffic_type=None
```

### `maze_line_6x6_tokenized_42.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, right, up, right, down, right, down, down
```

**Extracted Answer:**
```
the, maze, is, 6x6., let's, denote, cells, by, (row, column)., the, start, is, at, (0, 0), and, the, end, is, at, (5, 5)., here, is, a, breakdown, of, the, maze, and, the, walls:, (0, 0):, <|updownleft_wall|>, <|origin|>, -, walls:, up, down, left., can, move, right., (0, 1):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (0, 2):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (0, 3):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (0, 4):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (0, 5):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (1, 0):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (1, 1):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (1, 2):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (1, 3):, <|downleft_wall|>, -, walls:, down, left., can, move, up, right., (1, 4):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (1, 5):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (2, 0):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (2, 1):, <|updownleft_wall|>, -, walls:, up, down, left., can, move, right., (2, 2):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (2, 3):, <|upleft_wall|>, -, walls:, up, left., can, move, down, right., (2, 4):, <|upright_wall|>, -, walls:, up, right., can, move, down, left., (2, 5):, <|rightleft_wall|>, -, walls:, right, left., can, move, up, down., (3, 0):, <|downleft_wall|>, -, walls:, down, left., can, move, up, right., (3, 1):, <|updown_wall|>, -, walls:, up, down., can, move, left, right., (3, 2):, <|updown_wall|>, -, walls:, up, down., can, move, left, right., (3, 3):, <|downright_wall|>, -, walls:, down, right., can, move, up, left., (3, 4):, <|downleft_wall|>, -, walls:, down, left., can, move
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is 6x6. Let's denote cells by (row, column). The start is at (0,0) and the end is at (5,5).

Here is a breakdown of the maze and the walls:

(0,0): <|updownleft_wall|> <|origin|> - Walls: Up, Down, Left. Can move Right.
(0,1): <|upright_wall|> - Walls: Up, Right. Can move Down, Left.
(0,2): <|upleft_wall|> - Walls: Up, Left. Can move Down, Right.
(0,3): <|upright_wall|> - Walls: Up, Right. Can move Down, Left.
(0,4): <|upleft_wall|> - Walls: Up, Left. Can move Down, Right.
(0,5): <|upright_wall|> - Walls: Up, Right. Can move Down, Left.

(1,0): <|upleft_wall|> - Walls: Up, Left. Can move Down, Right.
(1,1): <|downright_wall|> - Walls: Down, Right. Can move Up, Left.
(1,2): <|rightleft_wall|> - Walls: Right, Left. Can move Up, Down.
(1,3): <|downleft_wall|> - Walls: Down, Left. Can move Up, Right.
(1,4): <|downright_wall|> - Walls: Down, Right. Can move Up, Left.
(1,5): <|rightleft_wall|> - Walls: Right, Left. Can move Up, Down.

(2,0): <|rightleft_wall|> - Walls: Right, Left. Can move Up, Down.
(2,1): <|updownleft_wall|> - Walls: Up, Down, Left. Can move Right.
(2,2): <|downright_wall|> - Walls: Down, Right. Can move Up, Left.
(2,3): <|upleft_wall|> - Walls: Up, Left. Can move Down, Right.
(2,4): <|upright_wall|> - Walls: Up, Right. Can move Down, Left.
(2,5): <|rightleft_wall|> - Walls: Right, Left. Can move Up, Down.

(3,0): <|downleft_wall|> - Walls: Down, Left. Can move Up, Right.
(3,1): <|updown_wall|> - Walls: Up, Down. Can move Left, Right.
(3,2): <|updown_wall|> - Walls: Up, Down. Can move Left, Right.
(3,3): <|downright_wall|> - Walls: Down, Right. Can move Up, Left.
(3,4): <|downleft_wall|> - Walls: Down, Left. Can move"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5oSVaY-LKOTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_42.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, left, down, right, down, right, right, up, right, down, right, down, left, down, right, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down, left, down, left, down, right, right, up, right, up, left, up, right, up, right, down, right, down, down, right, down, left, down, left, down, right, right, up, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,left,down,right,down,right,right,up,right,down,right,down,left,down,right,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,left,down,left,down,right,right,up,right,up,left,up,right,up,right,down,right,down,down,right,down,left,down,left,down,right,right,up,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6ISVadytJsPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_42.json`

**Score:** 14.29%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, right, down, down, down, down, down, down, right, right, right, right, right, right, right, up, right, down, right, down, down, down, down, down, down, down, down, down, down, left, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,right,down,down,down,down,down,down,right,right,right,right,right,right,right,up,right,down,right,down,down,down,down,down,down,down,down,down,down,left,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6oSVacGdLvT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_42.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='64SVacXdGNuxnsEPg_7zyAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=4341,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4341
    ),
  ],
  total_token_count=4390
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=4341 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4341
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4390 traffic_type=None
```

### `maze_occupancy_6x6_adj_42.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```

```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  finish_reason=<FinishReason.RECITATION: 'RECITATION'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7YSVaev_Kqrw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=1278,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1278
    ),
  ],
  total_token_count=1278
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=1278 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1278
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1278 traffic_type=None
```

### `maze_occupancy_6x6_ascii_42.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, right, down, down, right, right, down, right, down, right, right, right, down, right, down, down, right, right, right, right, right, up, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,right,down,down,right,right,down,right,down,right,right,right,down,right,down,down,right,right,right,right,right,up,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='74SVaenuKsPe7M8PidibyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=245,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=245
    ),
  ],
  total_token_count=895
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=245 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=245
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=895 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_42.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```

```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  finish_reason=<FinishReason.RECITATION: 'RECITATION'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8oSVabqLLqzu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2162
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2162 traffic_type=None
```

