# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_28.jpg` | **7.69%** | `input: 442 , ouput: 61` | `(0, 0), (1, 0), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_28.json` | **7.69%** | `input: 1817 , ouput: 57` | `(0, 0), (1, 1), (2, 1), (2, 2), (2, 3), (3, 2), (4, 2), (4, 1), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_28.json` | **100.00%** | `input: 2266 , ouput: 53` | `(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_28.txt` | **100.00%** | `input: 737 , ouput: 53` | `(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)` |
| `maze_line_6x6_tokenized_28.txt` | **0.00%** | `input: 681 , ouput: 49` | `(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_28.jpg` | **0.00%** | `input: 439 , ouput: 139` | `(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (8, 9), (8, 10), (8, 11), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_28.json` | **100.00%** | `input: 996 , ouput: 115` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_28.json` | **100.00%** | `input: 4348 , ouput: 115` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_28.txt` | **100.00%** | `input: 1285 , ouput: 115` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_28.txt` | **0.00%** | `input: 257 , ouput: 443` | `(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (10, 2), (9, 2), (8, 2), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (11, 11), (11, 12)` |
| `maze_occupancy_6x6_tokenized_28.txt` | **76.00%** | `input: 2170 , ouput: 650` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (7, 3), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (8, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (3, 10), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (0, 1), (1, 1), (11, 11), (1, 1), (1, 2), (1, 2), (1, 3), (1, 3), (2, 3), (2, 3), (3, 3), (3, 3), (3, 4), (3, 4), (3, 5), (3, 5), (3, 6), (3, 6), (3, 7), (3, 7), (2, 7), (2, 7), (1, 7), (1, 7), (1, 8), (1, 8), (1, 9), (1, 9), (1, 10), (1, 10), (1, 11), (1, 11), (2, 11), (2, 11), (3, 11), (3, 11), (4, 11), (4, 11), (5, 11), (5, 11), (5, 10), (5, 10), (5, 9)` |

---

## Full LLM Responses

### `maze_line_6x6_28.jpg`

**Score:** 7.69%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,3),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5XyVafOuLobIvdIPqfe6oAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=442,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=184
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=503
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=442 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=442 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=184
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=503 traffic_type=None
```

### `maze_line_6x6_28.json`

**Score:** 7.69%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 1), (2, 1), (2, 2), (2, 3), (3, 2), (4, 2), (4, 1), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,1),(2,1),(2,2),(2,3),(3,2),(4,2),(4,1),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5nyVafu5Feb1xN8PzZ3x8QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=1817,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1817
    ),
  ],
  total_token_count=1874
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=200 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=1817 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1817
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1874 traffic_type=None
```

### `maze_line_6x6_adj_28.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,2),(1,3),(0,3),(0,4),(0,5),(1,5),(2,5),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='53yVaZHCCdfIvdIPlo3gqAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=2266,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2266
    ),
  ],
  total_token_count=2319
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=2266 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2266
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2319 traffic_type=None
```

### `maze_line_6x6_adj_28.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,2),(1,3),(0,3),(0,4),(0,5),(1,5),(2,5),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='53yVaYrKMcHwvdIPhbD0iAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=737,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=737
    ),
  ],
  total_token_count=790
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=204 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=737 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=737
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=790 traffic_type=None
```

### `maze_line_6x6_tokenized_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6HyVafPLIqbTvdIP79ai6Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=681,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=681
    ),
  ],
  total_token_count=730
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=202 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=681 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=681
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=730 traffic_type=None
```

### `maze_occupancy_6x6_28.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (8, 9), (8, 10), (8, 11), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(3,2),(2,2),(2,3),(2,4),(3,4),(4,4),(4,5),(4,6),(5,6),(6,6),(6,5),(7,5),(7,6),(7,7),(8,7),(9,7),(9,8),(9,9),(8,9),(8,10),(8,11),(8,12),(9,12),(10,12),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6nyVabrnJKbZvdIPiYDjiQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=139,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=181
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
) total_tokens=439 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=139 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=181
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=578 traffic_type=None
```

### `maze_occupancy_6x6_28.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(2,7),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='63yVacekGOH1xs0Pw6qN8Qs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=115,
  prompt_token_count=996,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=996
    ),
  ],
  total_token_count=1111
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=182 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=115 candidates_tokens_details=None prompt_token_count=996 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=996
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1111 traffic_type=None
```

### `maze_occupancy_6x6_adj_28.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(2,7),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7HyVafH6GfT1xs0PlO7m0AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=115,
  prompt_token_count=4348,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4348
    ),
  ],
  total_token_count=4463
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=115 candidates_tokens_details=None prompt_token_count=4348 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4348
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4463 traffic_type=None
```

### `maze_occupancy_6x6_adj_28.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(2,7),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7XyVaZaaGs_c28oPsY6G4AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=115,
  prompt_token_count=1285,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1285
    ),
  ],
  total_token_count=1400
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=206 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=115 candidates_tokens_details=None prompt_token_count=1285 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1285
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1400 traffic_type=None
```

### `maze_occupancy_6x6_ascii_28.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (10, 2), (9, 2), (8, 2), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (11, 11), (11, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(1,11),(2,11),(3,11),(4,11),(5,11),(5,10),(5,9),(5,8),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(5,1),(4,1),(3,1),(2,1),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(8,2),(7,2),(6,2),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(6,10),(7,10),(8,10),(9,10),(10,10),(11,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(10,2),(9,2),(8,2),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(7,10),(8,10),(9,10),(10,10),(11,10),(11,11),(11,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='73yVac21Ddrzxs0PvK7U4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=443,
  prompt_token_count=257,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=257
    ),
  ],
  total_token_count=700
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=443 candidates_tokens_details=None prompt_token_count=257 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=257
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=700 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_28.txt`

**Score:** 76.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (7, 3), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (8, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (3, 10), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (0, 1), (1, 1), (11, 11), (1, 1), (1, 2), (1, 2), (1, 3), (1, 3), (2, 3), (2, 3), (3, 3), (3, 3), (3, 4), (3, 4), (3, 5), (3, 5), (3, 6), (3, 6), (3, 7), (3, 7), (2, 7), (2, 7), (1, 7), (1, 7), (1, 8), (1, 8), (1, 9), (1, 9), (1, 10), (1, 10), (1, 11), (1, 11), (2, 11), (2, 11), (3, 11), (3, 11), (4, 11), (4, 11), (5, 11), (5, 11), (5, 10), (5, 10), (5, 9)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(2,7),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(5,10),(5,9),(5,8),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(6,2),(7,2),(7,3),(7,1),(8,1),(9,1),(9,2),(9,3),(8,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(8,9),(7,9),(6,9),(5,9),(4,9),(3,9),(3,10),(2,11),(1,11),(1,10),(1,9),(1,8),(1,7),(2,7),(3,7),(3,6),(3,5),(3,4),(3,3),(2,3),(1,3),(1,2),(1,1),(0,1) is not a valid path. Let's try again.

The start is at (1,1) and the target is at (11,11).
From (1,1), we can move to (1,2).
From (1,2), we can move to (1,3).
From (1,3), we can move to (2,3).
From (2,3), we can move to (3,3).
From (3,3), we can move to (3,4).
From (3,4), we can move to (3,5).
From (3,5), we can move to (3,6).
From (3,6), we can move to (3,7).
From (3,7), we can move to (2,7).
From (2,7), we can move to (1,7).
From (1,7), we can move to (1,8).
From (1,8), we can move to (1,9).
From (1,9), we can move to (1,10).
From (1,10), we can move to (1,11).
From (1,11), we can move to (2,11).
From (2,11), we can move to (3,11).
From (3,11), we can move to (4,11).
From (4,11), we can move to (5,11).
From (5,11), we can move to (5,10).
From (5,10), we can move to (5,9).
From"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8XyVaeCTHaPWvdIP2_2OmQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2170,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2170
    ),
  ],
  total_token_count=2820
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=205 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2170 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2170
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2820 traffic_type=None
```

