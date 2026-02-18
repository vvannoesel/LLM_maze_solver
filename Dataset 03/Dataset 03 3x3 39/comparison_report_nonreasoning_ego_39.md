# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_39.jpg` | **0.00%** | `input: 551 , ouput: 27` | `right, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_39.json` | **0.00%** | `input: 774 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_39.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, right, forward, left, forward` |
| `maze_line_3x3_adj_39.txt` | **0.00%** | `input: 468 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_line_3x3_tokenized_39.txt` | **0.00%** | `input: 439 , ouput: 650` | `the, maze, representation, is, a, bit, tricky, to, interpret, directly, as, it, lists, walls, for, each, cell., let's, break, down, the, maze, structure, first., **maze, structure, interpretation:**, *, **cell, (0, 0):**, `<|updownleft_wall|>`, -, this, means, cell, (0, 0), has, walls, on, its, top, bottom, and, left, sides., since, it's, on, the, edge, the, 'up', and, 'left', walls, are, external, boundaries., the, 'down', wall, is, the, boundary, to, (1, 0)., the, 'right', is, open., *, **cell, (0, 1):**, `<|updown_wall|>`, -, this, means, cell, (0, 1), has, walls, on, its, top, and, bottom., the, 'up', wall, is, an, external, boundary., the, 'down', wall, is, the, boundary, to, (1, 1)., the, 'left', and, 'right', are, open., *, **cell, (0, 2):**, `<|upright_wall|>`, -, this, means, cell, (0, 2), has, walls, on, its, top, and, right., the, 'up', wall, is, an, external, boundary., the, 'right', wall, is, an, external, boundary., the, 'down', and, 'left', are, open., *, **cell, (1, 0):**, `<|upleft_wall|>`, -, this, means, cell, (1, 0), has, walls, on, its, top, and, left., the, 'left', wall, is, an, external, boundary., the, 'top', wall, is, the, boundary, to, (0, 0)., the, 'down', and, 'right', are, open., *, **cell, (1, 1):**, `<|upright_wall|>`, -, this, means, cell, (1, 1), has, walls, on, its, top, and, right., the, 'top', wall, is, the, boundary, to, (0, 1)., the, 'right', wall, is, the, boundary, to, (1, 2)., the, 'down', and, 'left', are, open., *, **cell, (1, 2):**, `<|rightleft_wall|>`, -, this, means, cell, (1, 2), has, walls, on, its, right, and, left., the, 'right', wall, is, an, external, boundary., the, 'left', wall, is, the, boundary, to, (1, 1)., the, 'up', and, 'down', are, open., *, **cell, (2, 0):**, `<|downrightleft_wall|>`, -, this, means, cell, (2, 0), has, walls, on, its, bottom, right, and, left., the, 'bottom', wall, is, an, external, boundary., the, 'right', wall, is, the, boundary, to, (2, 1)., the, 'left', wall, is, an, external, boundary., the, 'up', is, open., *, **cell, (2, 1):**, `<|downleft_wall|>`, -, this, means, cell, (2, 1), has, walls, on, its, bottom, and, left., the, 'bottom', wall, is, an, external, boundary., the, 'left', wall, is, the, boundary, to, (2, 0)., the, 'up', and, 'right', are, open., *, **cell, (2, 2):**, `<|downright_wall|>`, -, this, means, cell, (2` |
| `maze_occupancy_3x3_39.jpg` | **0.00%** | `input: 546 , ouput: 28` | `right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, left, forward.` |
| `maze_occupancy_3x3_39.json` | **0.00%** | `input: 589 , ouput: 67` | `right, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_39.json` | **0.00%** | `input: 1292 , ouput: 39` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_39.txt` | **0.00%** | `input: 580 , ouput: 39` | `right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_ascii_39.txt` | **0.00%** | `input: 317 , ouput: 650` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_tokenized_39.txt` | **0.00%** | `input: 867 , ouput: 59` | `forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_39.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o5qVaemOIub1xN8PzZ3x8QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
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
  total_token_count=578
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=578 traffic_type=None
```

### `maze_line_3x3_39.json`

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
        text='Right, forward, right, forward, forward, left, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pJqVaYygDJXIvdIP-oyG2AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=789
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=789 traffic_type=None
```

### `maze_line_3x3_adj_39.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pJqVafjKN7SDvdIP45SUiQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_adj_39.txt`

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
        text='Right, Forward, Right, Forward, Right, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pZqVaYzyHrSDvdIP45SUiQE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_3x3_tokenized_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
the, maze, representation, is, a, bit, tricky, to, interpret, directly, as, it, lists, walls, for, each, cell., let's, break, down, the, maze, structure, first., **maze, structure, interpretation:**, *, **cell, (0, 0):**, `<|updownleft_wall|>`, -, this, means, cell, (0, 0), has, walls, on, its, top, bottom, and, left, sides., since, it's, on, the, edge, the, 'up', and, 'left', walls, are, external, boundaries., the, 'down', wall, is, the, boundary, to, (1, 0)., the, 'right', is, open., *, **cell, (0, 1):**, `<|updown_wall|>`, -, this, means, cell, (0, 1), has, walls, on, its, top, and, bottom., the, 'up', wall, is, an, external, boundary., the, 'down', wall, is, the, boundary, to, (1, 1)., the, 'left', and, 'right', are, open., *, **cell, (0, 2):**, `<|upright_wall|>`, -, this, means, cell, (0, 2), has, walls, on, its, top, and, right., the, 'up', wall, is, an, external, boundary., the, 'right', wall, is, an, external, boundary., the, 'down', and, 'left', are, open., *, **cell, (1, 0):**, `<|upleft_wall|>`, -, this, means, cell, (1, 0), has, walls, on, its, top, and, left., the, 'left', wall, is, an, external, boundary., the, 'top', wall, is, the, boundary, to, (0, 0)., the, 'down', and, 'right', are, open., *, **cell, (1, 1):**, `<|upright_wall|>`, -, this, means, cell, (1, 1), has, walls, on, its, top, and, right., the, 'top', wall, is, the, boundary, to, (0, 1)., the, 'right', wall, is, the, boundary, to, (1, 2)., the, 'down', and, 'left', are, open., *, **cell, (1, 2):**, `<|rightleft_wall|>`, -, this, means, cell, (1, 2), has, walls, on, its, right, and, left., the, 'right', wall, is, an, external, boundary., the, 'left', wall, is, the, boundary, to, (1, 1)., the, 'up', and, 'down', are, open., *, **cell, (2, 0):**, `<|downrightleft_wall|>`, -, this, means, cell, (2, 0), has, walls, on, its, bottom, right, and, left., the, 'bottom', wall, is, an, external, boundary., the, 'right', wall, is, the, boundary, to, (2, 1)., the, 'left', wall, is, an, external, boundary., the, 'up', is, open., *, **cell, (2, 1):**, `<|downleft_wall|>`, -, this, means, cell, (2, 1), has, walls, on, its, bottom, and, left., the, 'bottom', wall, is, an, external, boundary., the, 'left', wall, is, the, boundary, to, (2, 0)., the, 'up', and, 'right', are, open., *, **cell, (2, 2):**, `<|downright_wall|>`, -, this, means, cell, (2
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze representation is a bit tricky to interpret directly as it lists walls for each cell. Let's break down the maze structure first.

**Maze Structure Interpretation:**

*   **Cell (0,0):** `<|updownleft_wall|>` - This means cell (0,0) has walls on its top, bottom, and left sides. Since it's on the edge, the 'up' and 'left' walls are external boundaries. The 'down' wall is the boundary to (1,0). The 'right' is open.
*   **Cell (0,1):** `<|updown_wall|>` - This means cell (0,1) has walls on its top and bottom. The 'up' wall is an external boundary. The 'down' wall is the boundary to (1,1). The 'left' and 'right' are open.
*   **Cell (0,2):** `<|upright_wall|>` - This means cell (0,2) has walls on its top and right. The 'up' wall is an external boundary. The 'right' wall is an external boundary. The 'down' and 'left' are open.
*   **Cell (1,0):** `<|upleft_wall|>` - This means cell (1,0) has walls on its top and left. The 'left' wall is an external boundary. The 'top' wall is the boundary to (0,0). The 'down' and 'right' are open.
*   **Cell (1,1):** `<|upright_wall|>` - This means cell (1,1) has walls on its top and right. The 'top' wall is the boundary to (0,1). The 'right' wall is the boundary to (1,2). The 'down' and 'left' are open.
*   **Cell (1,2):** `<|rightleft_wall|>` - This means cell (1,2) has walls on its right and left. The 'right' wall is an external boundary. The 'left' wall is the boundary to (1,1). The 'up' and 'down' are open.
*   **Cell (2,0):** `<|downrightleft_wall|>` - This means cell (2,0) has walls on its bottom, right, and left. The 'bottom' wall is an external boundary. The 'right' wall is the boundary to (2,1). The 'left' wall is an external boundary. The 'up' is open.
*   **Cell (2,1):** `<|downleft_wall|>` - This means cell (2,1) has walls on its bottom and left. The 'bottom' wall is an external boundary. The 'left' wall is the boundary to (2,0). The 'up' and 'right' are open.
*   **Cell (2,2):** `<|downright_wall|>` - This means cell (2,"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='p5qVaZaDE9--xN8Puvy7kAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_39.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, left, forward.
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, left, forward.'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qJqVaeP8B_bzxs0P0ID50Aw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=28,
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
  total_token_count=574
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=28 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=574 traffic_type=None
```

### `maze_occupancy_3x3_39.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qJqVaaWVM4uX28oPlq_ciQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=67,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=656
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=67 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=656 traffic_type=None
```

### `maze_occupancy_3x3_adj_39.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qZqVafPUHdKwxN8PyNH2gQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1331
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1331 traffic_type=None
```

### `maze_occupancy_3x3_adj_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qpqVaY9X4tK90g_Q7dPBDA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=39,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=619
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=39 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=619 traffic_type=None
```

### `maze_occupancy_3x3_ascii_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,Forward,Left,Forward,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rJqVaZGmCOGlxN8Ppv3riAo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_3x3_tokenized_39.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, forward, forward, left, forward, forward, forward, right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, left, forward, forward, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Forward,forward,right,forward,forward,forward,forward,left,forward,forward,forward,right,forward,right,forward,forward,forward,forward,left,forward,forward,forward,left,forward,forward,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rJqVabylKbnwxN8P8smN8QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=926
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=926 traffic_type=None
```

