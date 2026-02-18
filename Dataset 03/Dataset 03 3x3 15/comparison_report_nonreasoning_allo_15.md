# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_15.jpg` | **0.00%** | `input: 434 , ouput: 7` | `down, right, down, right` |
| `maze_line_3x3_15.json` | **0.00%** | `input: 657 , ouput: 7` | `down, right, right, down` |
| `maze_line_3x3_adj_15.json` | **37.50%** | `input: 719 , ouput: 7` | `right, right, down, down` |
| `maze_line_3x3_adj_15.txt` | **37.50%** | `input: 351 , ouput: 9` | `right, right, down, right, down` |
| `maze_line_3x3_tokenized_15.txt` | **0.00%** | `input: 322 , ouput: 282` | `this, maze, description, is, a, bit, confusing., it, seems, like, it's, describing, the, walls, of, each, cell, but, the, representation, is, not, standard., usually, a, maze, is, represented, by, showing, the, paths, or, walls, between, cells., let's, assume, the, following, interpretation:, *, each, token, like, `<|0-0|>, <|updownleft_wall|>`, describes, cell, (0, 0), and, its, walls., *, `<|updownleft_wall|>`, means, there's, a, wall, going, up, down, and, left, from, that, cell., this, implies, a, wall, on, the, right., *, `<|origin|>`, marks, the, start., *, `<|target|>`, marks, the, end., given, the, limitations, and, the, unusual, format, it's, very, difficult, to, definitively, solve, this, maze, without, a, clearer, representation., the, walls, described, for, each, cell, seem, contradictory, or, incomplete., for, example, for, `<|0-0|>, <|updownleft_wall|>, <|origin|>`:, if, there, are, walls, up, down, and, left, it, means, we, can, only, move, right, from, (0, 0)., however, the, description, is, very, ambiguous., if, you, can, provide, a, clearer, representation, of, the, maze, i'd, be, happy, to, help, solve, it., **due, to, the, ambiguity, and, potential, incompleteness, of, the, maze, description, i, cannot, confidently, provide, a, solution.**` |
| `maze_occupancy_3x3_15.jpg` | **6.25%** | `input: 429 , ouput: 15` | `right, down, right, down, right, down, right, down` |
| `maze_occupancy_3x3_15.json` | **25.00%** | `input: 472 , ouput: 29` | `right, right, right, right, right, down, down, down, down, down, left, left, left, left, left` |
| `maze_occupancy_3x3_adj_15.json` | **37.50%** | `input: 1181 , ouput: 19` | `right, right, right, right, down, down, down, down, right, right` |
| `maze_occupancy_3x3_adj_15.txt` | **37.50%** | `input: 463 , ouput: 21` | `right, right, right, right, down, down, right, right, right, down, down` |
| `maze_occupancy_3x3_ascii_15.txt` | **37.50%** | `input: 196 , ouput: 27` | `right, right, right, right, down, down, down, left, left, left, down, down, right, right` |
| `maze_occupancy_3x3_tokenized_15.txt` | **25.00%** | `input: 750 , ouput: 21` | `right, right, right, right, right, down, down, down, down, down, right` |

---

## Full LLM Responses

### `maze_line_3x3_15.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dZGVaYRb9-eewQ-iueiICQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
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
  total_token_count=441
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=441 traffic_type=None
```

### `maze_line_3x3_15.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dZGVaYmmItqfnsEPxvyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=657,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=657
    ),
  ],
  total_token_count=664
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=657 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=657
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=664 traffic_type=None
```

### `maze_line_3x3_adj_15.json`

**Score:** 37.50%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dpGVaeyeF9HMkdUPy8C6kAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=7,
  prompt_token_count=719,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=719
    ),
  ],
  total_token_count=726
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=7 candidates_tokens_details=None prompt_token_count=719 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=719
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=726 traffic_type=None
```

### `maze_line_3x3_adj_15.txt`

**Score:** 37.50%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d5GVafH5AYWF7M8PnoeMqQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=9,
  prompt_token_count=351,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=351
    ),
  ],
  total_token_count=360
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=9 candidates_tokens_details=None prompt_token_count=351 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=351
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=360 traffic_type=None
```

### `maze_line_3x3_tokenized_15.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right
```

**Extracted Answer:**
```
this, maze, description, is, a, bit, confusing., it, seems, like, it's, describing, the, walls, of, each, cell, but, the, representation, is, not, standard., usually, a, maze, is, represented, by, showing, the, paths, or, walls, between, cells., let's, assume, the, following, interpretation:, *, each, token, like, `<|0-0|>, <|updownleft_wall|>`, describes, cell, (0, 0), and, its, walls., *, `<|updownleft_wall|>`, means, there's, a, wall, going, up, down, and, left, from, that, cell., this, implies, a, wall, on, the, right., *, `<|origin|>`, marks, the, start., *, `<|target|>`, marks, the, end., given, the, limitations, and, the, unusual, format, it's, very, difficult, to, definitively, solve, this, maze, without, a, clearer, representation., the, walls, described, for, each, cell, seem, contradictory, or, incomplete., for, example, for, `<|0-0|>, <|updownleft_wall|>, <|origin|>`:, if, there, are, walls, up, down, and, left, it, means, we, can, only, move, right, from, (0, 0)., however, the, description, is, very, ambiguous., if, you, can, provide, a, clearer, representation, of, the, maze, i'd, be, happy, to, help, solve, it., **due, to, the, ambiguity, and, potential, incompleteness, of, the, maze, description, i, cannot, confidently, provide, a, solution.**
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""This maze description is a bit confusing. It seems like it's describing the walls of each cell, but the representation is not standard. Usually, a maze is represented by showing the paths or walls between cells.

Let's assume the following interpretation:

*   Each token like `<|0-0|> <|updownleft_wall|>` describes cell (0,0) and its walls.
*   `<|updownleft_wall|>` means there's a wall going up, down, and left from that cell. This implies a wall on the right.
*   `<|origin|>` marks the start.
*   `<|target|>` marks the end.

Given the limitations and the unusual format, it's very difficult to definitively solve this maze without a clearer representation. The walls described for each cell seem contradictory or incomplete.

For example, for `<|0-0|> <|updownleft_wall|> <|origin|>`:
If there are walls up, down, and left, it means we can only move right from (0,0). However, the description is very ambiguous.

If you can provide a clearer representation of the maze, I'd be happy to help solve it.

**Due to the ambiguity and potential incompleteness of the maze description, I cannot confidently provide a solution.**"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eJGVaaDgCq7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=282,
  prompt_token_count=322,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=322
    ),
  ],
  total_token_count=604
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=282 candidates_tokens_details=None prompt_token_count=322 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=322
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=604 traffic_type=None
```

### `maze_occupancy_3x3_15.jpg`

**Score:** 6.25%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eZGVabL4DJzw7M8Pu9TR-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=429,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=171
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=444
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=429 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=444 traffic_type=None
```

### `maze_occupancy_3x3_15.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,left,left,left,left,left'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eZGVafHqOYDHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=472,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=472
    ),
  ],
  total_token_count=501
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=172 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=472 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=472
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=501 traffic_type=None
```

### `maze_occupancy_3x3_adj_15.json`

**Score:** 37.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='epGVaaTDI6zu7M8P7_W9-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1181,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1181
    ),
  ],
  total_token_count=1200
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1181 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1181
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1200 traffic_type=None
```

### `maze_occupancy_3x3_adj_15.txt`

**Score:** 37.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, right, right, down, down, right, right, right, down, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e5GVaZegD-OkkdUPvpSE8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=463,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=463
    ),
  ],
  total_token_count=484
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=463 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=463
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=484 traffic_type=None
```

### `maze_occupancy_3x3_ascii_15.txt`

**Score:** 37.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, left, left, left, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,left,left,left,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e5GVafvmOOOkkdUPvpSE8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=196,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=196
    ),
  ],
  total_token_count=223
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=171 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=196 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=196
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=223 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_15.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fJGVaZb2J7-fkdUPtcm3yAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=750,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=750
    ),
  ],
  total_token_count=771
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=195 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=750 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=750
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=771 traffic_type=None
```

