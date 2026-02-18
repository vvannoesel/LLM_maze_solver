# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_23.jpg` | **4.76%** | `input: 442 , ouput: 41` | `(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4)` |
| `maze_line_6x6_23.json` | **4.76%** | `input: 1817 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_23.json` | **52.38%** | `input: 2266 , ouput: 101` | `(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 3), (1, 3), (1, 2), (0, 2), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_23.txt` | **14.29%** | `input: 737 , ouput: 53` | `(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_tokenized_23.txt` | **4.76%** | `input: 681 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_23.jpg` | **0.00%** | `input: 439 , ouput: 286` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (8, 2), (9, 2), (10, 2), (10, 1), (10, 0), (11, 0), (12, 0), (12, 1), (12, 2), (12, 3), (11, 3), (10, 3), (10, 4), (10, 5), (11, 5), (12, 5), (12, 6), (11, 6), (10, 6), (9, 6), (8, 6), (8, 5), (8, 4), (7, 4), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (12, 9), (11, 9), (10, 9), (10, 10), (10, 11), (10, 12), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_23.json` | **41.46%** | `input: 996 , ouput: 179` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_23.json` | **51.22%** | `input: 4353 , ouput: 304` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 7), (9, 8), (9, 9), (10, 9), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_23.txt` | **51.22%** | `input: 1284 , ouput: 239` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_ascii_23.txt` | **0.00%** | `input: 255 , ouput: 153` | `(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 6), (9, 5), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_tokenized_23.txt` | **90.24%** | `input: 2170 , ouput: 175` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (9, 11), (10, 11), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_23.jpg`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(3,1),(3,2),(4,2),(4,3),(4,4),(5,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i3yVac6bCKPWvdIP2_2OmQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
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
  total_token_count=483
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=442 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=184
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=483 traffic_type=None
```

### `maze_line_6x6_23.json`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(3,1),(3,2),(3,3),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i3yVaZaUOtKwxN8PyNH2gQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=1817,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1817
    ),
  ],
  total_token_count=1862
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=1817 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1817
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1862 traffic_type=None
```

### `maze_line_6x6_adj_23.json`

**Score:** 52.38%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 3), (1, 3), (1, 2), (0, 2), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3),(2,4),(1,4),(0,4),(0,3),(1,3),(1,2),(0,2),(0,5),(1,5),(2,5),(3,5),(3,4),(3,3),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jHyVaePYLd7QxN8PgJLJyAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=101,
  prompt_token_count=2266,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2266
    ),
  ],
  total_token_count=2367
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=101 candidates_tokens_details=None prompt_token_count=2266 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2266
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2367 traffic_type=None
```

### `maze_line_6x6_adj_23.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(2,1),(2,2),(2,3),(2,4),(3,4),(3,3),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jXyVadKVK7T4xs0P_M6xgA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_23.txt`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jnyVaamSHLT4xs0P_M6xgA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=681,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=681
    ),
  ],
  total_token_count=726
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=681 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=681
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=726 traffic_type=None
```

### `maze_occupancy_6x6_23.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (8, 2), (9, 2), (10, 2), (10, 1), (10, 0), (11, 0), (12, 0), (12, 1), (12, 2), (12, 3), (11, 3), (10, 3), (10, 4), (10, 5), (11, 5), (12, 5), (12, 6), (11, 6), (10, 6), (9, 6), (8, 6), (8, 5), (8, 4), (7, 4), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (12, 9), (11, 9), (10, 9), (10, 10), (10, 11), (10, 12), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(2,2),(1,2),(1,3),(1,4),(1,5),(2,5),(3,5),(4,5),(5,5),(5,4),(5,3),(6,3),(7,3),(7,2),(8,2),(9,2),(10,2),(10,1),(10,0),(11,0),(12,0),(12,1),(12,2),(12,3),(11,3),(10,3),(10,4),(10,5),(11,5),(12,5),(12,6),(11,6),(10,6),(9,6),(8,6),(8,5),(8,4),(7,4),(6,4),(6,5),(6,6),(6,7),(6,8),(7,8),(8,8),(9,8),(10,8),(11,8),(12,8),(12,9),(11,9),(10,9),(10,10),(10,11),(10,12),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kHyVacrIGpuZ28oPi9qtsAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=286,
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
  total_token_count=725
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=286 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=181
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=725 traffic_type=None
```

### `maze_occupancy_6x6_23.json`

**Score:** 41.46%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(6,9),(7,9),(7,8),(7,7),(7,6),(7,5),(7,4),(7,3),(7,2),(7,1),(8,1),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kXyVab7II9rzxs0PvK7U4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=179,
  prompt_token_count=996,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=996
    ),
  ],
  total_token_count=1175
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=179 candidates_tokens_details=None prompt_token_count=996 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=996
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1175 traffic_type=None
```

### `maze_occupancy_6x6_adj_23.json`

**Score:** 51.22%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 7), (9, 8), (9, 9), (10, 9), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(4,9),(3,9),(2,9),(1,9),(1,8),(1,7),(2,7),(3,7),(3,6),(3,5),(2,5),(1,5),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(8,7),(9,7),(9,8),(9,9),(10,9),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(10,3),(9,3),(8,3),(7,3),(7,4),(7,5),(8,5),(9,5),(9,7),(9,8),(9,9),(10,9),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='knyVacqxK6PWvdIP-eeOmQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=304,
  prompt_token_count=4353,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4353
    ),
  ],
  total_token_count=4657
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=304 candidates_tokens_details=None prompt_token_count=4353 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4353
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4657 traffic_type=None
```

### `maze_occupancy_6x6_adj_23.txt`

**Score:** 51.22%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(4,9),(3,9),(2,9),(1,9),(1,8),(1,7),(2,7),(3,7),(3,6),(3,5),(2,5),(1,5),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(8,7),(9,7),(10,7),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k3yVaYzQO_jwxN8Px9POiQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=239,
  prompt_token_count=1284,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1284
    ),
  ],
  total_token_count=1523
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=239 candidates_tokens_details=None prompt_token_count=1284 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1284
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1523 traffic_type=None
```

### `maze_occupancy_6x6_ascii_23.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 6), (9, 5), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(8,7),(9,7),(9,6),(9,5),(10,5),(10,6),(10,7),(10,8),(10,9),(10,10),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lHyVaf-DO4uX28oPlq_ciQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=153,
  prompt_token_count=255,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=255
    ),
  ],
  total_token_count=408
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=153 candidates_tokens_details=None prompt_token_count=255 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=255
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=408 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_23.txt`

**Score:** 90.24%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(4,9),(3,9),(2,9),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(8,7),(9,7),(9,8),(9,9),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='lXyVaYq8PM_c28oPsY6G4AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=175,
  prompt_token_count=2170,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2170
    ),
  ],
  total_token_count=2345
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=175 candidates_tokens_details=None prompt_token_count=2170 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2170
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2345 traffic_type=None
```

