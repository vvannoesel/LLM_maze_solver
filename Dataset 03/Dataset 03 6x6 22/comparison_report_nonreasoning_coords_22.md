# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_22.jpg` | **17.39%** | `input: 442 , ouput: 69` | `(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_22.json` | **13.04%** | `input: 1817 , ouput: 53` | `(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_22.json` | **100.00%** | `input: 2266 , ouput: 93` | `(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_22.txt` | **21.74%** | `input: 737 , ouput: 650` | `(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (0, 0), (5, 5), (0, 0), (0, 0), (0, 0), (1, 0), (1, 0), (0, 0), (1, 0), (1, 0), (0, 0), (1, 0), (1, 0), (0, 0), (1, 1), (0, 0), (1, 1), (0, 0), (1, 0), (1, 1), (1, 0), (0, 0), (1, 1), (1, 0), (1, 1), (1, 1), (1, 0), (1, 2), (1, 0), (1, 2), (0, 0), (1, 0), (1, 1), (1, 2), (1, 0), (0, 0), (1, 1), (1, 0), (1, 2), (1, 1), (1, 2), (1, 2), (0, 2), (1, 1), (1, 1), (0, 2), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (1, 0), (0, 0), (1, 1), (1, 0), (1, 2), (1, 1), (0, 2), (1, 2), (0, 2), (0, 2), (0, 1), (0, 3), (1, 2), (1, 2), (0, 1), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (1, 0), (0, 0), (1, 1), (1, 0), (1, 2), (1, 1), (0, 2), (1, 2), (0, 1), (0, 2), (0, 3), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 3), (1, 0), (0, 0)` |
| `maze_line_6x6_tokenized_22.txt` | **0.00%** | `input: 681 , ouput: 45` | `(0, 2), (1, 2), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_22.jpg` | **0.00%** | `input: 439 , ouput: 199` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (9, 6), (10, 6), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (10, 12), (9, 12), (8, 12), (7, 12), (6, 12), (5, 12)` |
| `maze_occupancy_6x6_22.json` | **2.22%** | `input: 996 , ouput: 218` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_22.json` | **20.00%** | `input: 4355 , ouput: 89` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1)` |
| `maze_occupancy_6x6_adj_22.txt` | **20.00%** | `input: 1286 , ouput: 111` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_22.txt` | **0.00%** | `input: 259 , ouput: 156` | `(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (8, 2), (8, 3), (8, 4), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (10, 10), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (11, 0)` |
| `maze_occupancy_6x6_tokenized_22.txt` | **2.22%** | `input: 2170 , ouput: 174` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_22.jpg`

**Score:** 17.39%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(2,2),(3,2),(3,1),(3,0),(4,0),(5,0),(5,1),(5,2),(4,2),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cHyVacS_NLnwxN8P8smN8QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=69,
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
  total_token_count=511
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=69 candidates_tokens_details=None prompt_token_count=442 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=184
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=511 traffic_type=None
```

### `maze_line_6x6_22.json`

**Score:** 13.04%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(4,2),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cXyVaZGZKPjwxN8Px9POiQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=1817,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1817
    ),
  ],
  total_token_count=1870
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=1817 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1817
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1870 traffic_type=None
```

### `maze_line_6x6_adj_22.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(0,2),(0,3),(1,3),(1,4),(2,4),(3,4),(4,4),(4,3),(3,3),(2,3),(2,2),(2,1),(3,1),(4,1),(4,2),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cnyVab3HGfHXvdIP-aPZgQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=93,
  prompt_token_count=2266,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2266
    ),
  ],
  total_token_count=2359
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=93 candidates_tokens_details=None prompt_token_count=2266 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2266
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2359 traffic_type=None
```

### `maze_line_6x6_adj_22.txt`

**Score:** 21.74%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (0, 0), (5, 5), (0, 0), (0, 0), (0, 0), (1, 0), (1, 0), (0, 0), (1, 0), (1, 0), (0, 0), (1, 0), (1, 0), (0, 0), (1, 1), (0, 0), (1, 1), (0, 0), (1, 0), (1, 1), (1, 0), (0, 0), (1, 1), (1, 0), (1, 1), (1, 1), (1, 0), (1, 2), (1, 0), (1, 2), (0, 0), (1, 0), (1, 1), (1, 2), (1, 0), (0, 0), (1, 1), (1, 0), (1, 2), (1, 1), (1, 2), (1, 2), (0, 2), (1, 1), (1, 1), (0, 2), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (1, 0), (0, 0), (1, 1), (1, 0), (1, 2), (1, 1), (0, 2), (1, 2), (0, 2), (0, 2), (0, 1), (0, 3), (1, 2), (1, 2), (0, 1), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (1, 0), (0, 0), (1, 1), (1, 0), (1, 2), (1, 1), (0, 2), (1, 2), (0, 1), (0, 2), (0, 3), (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 3), (1, 0), (0, 0)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""(0,0),(1,0),(1,1),(1,2),(0,2),(0,1),(0,0) This is not a valid path. Let me try again.

I will use a Breadth-First Search (BFS) approach to find the shortest path.

Start: (0,0)
Target: (5,5)

Queue: [(0,0)]
Visited: {(0,0)}
Parent: {}

1. Dequeue (0,0). Neighbors: (1,0).
   Enqueue (1,0). Visited: {(0,0), (1,0)}. Parent: {(1,0): (0,0)}.
   Queue: [(1,0)]

2. Dequeue (1,0). Neighbors: (0,0), (1,1). (0,0) is visited.
   Enqueue (1,1). Visited: {(0,0), (1,0), (1,1)}. Parent: {(1,0): (0,0), (1,1): (1,0)}.
   Queue: [(1,1)]

3. Dequeue (1,1). Neighbors: (1,0), (1,2). (1,0) is visited.
   Enqueue (1,2). Visited: {(0,0), (1,0), (1,1), (1,2)}. Parent: {(1,0): (0,0), (1,1): (1,0), (1,2): (1,1)}.
   Queue: [(1,2)]

4. Dequeue (1,2). Neighbors: (0,2), (1,1). (1,1) is visited.
   Enqueue (0,2). Visited: {(0,0), (1,0), (1,1), (1,2), (0,2)}. Parent: {(1,0): (0,0), (1,1): (1,0), (1,2): (1,1), (0,2): (1,2)}.
   Queue: [(0,2)]

5. Dequeue (0,2). Neighbors: (0,1), (0,3), (1,2). (1,2) is visited.
   Enqueue (0,1). Visited: {(0,0), (1,0), (1,1), (1,2), (0,2), (0,1)}. Parent: {(1,0): (0,0), (1,1): (1,0), (1,2): (1,1), (0,2): (1,2), (0,1): (0,2)}.
   Enqueue (0,3). Visited: {(0,0), (1,0), (1,1), (1,2), (0,2), (0,1), (0,3)}. Parent: {(1,0): (0,0), (1"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dHyVafbcHozYxs0P5_PJ2Qo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=737,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=737
    ),
  ],
  total_token_count=1387
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=737 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=737
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1387 traffic_type=None
```

### `maze_line_6x6_tokenized_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 2), (1, 2), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,2),(1,2),(2,2),(2,1),(3,1),(4,1),(4,2),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dXyVafa0CIuX28oPlq_ciQw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_22.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (9, 6), (10, 6), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (10, 12), (9, 12), (8, 12), (7, 12), (6, 12), (5, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(4,6),(3,6),(2,6),(1,6),(1,7),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(8,7),(8,6),(9,6),(10,6),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12),(10,12),(9,12),(8,12),(7,12),(6,12),(5,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d3yVabSmBNqb28oPgOmZoQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=199,
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
  total_token_count=638
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=199 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=181
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=638 traffic_type=None
```

### `maze_occupancy_6x6_22.json`

**Score:** 2.22%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,7),(3,7),(3,6),(3,5),(3,4),(3,3),(3,2),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(8,7),(7,7),(6,7),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d3yVacu9OI3ZvdIPlZKdgQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=218,
  prompt_token_count=996,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=996
    ),
  ],
  total_token_count=1214
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=218 candidates_tokens_details=None prompt_token_count=996 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=996
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1214 traffic_type=None
```

### `maze_occupancy_6x6_adj_22.json`

**Score:** 20.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(2,5),(1,5),(1,4),(1,3),(1,3),(1,4),(1,5),(2,5),(3,5),(3,4),(3,3),(3,2),(3,1),(2,1),(1,1)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eHyVafOeNanFvdIP2N2Q8Qc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=89,
  prompt_token_count=4355,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4355
    ),
  ],
  total_token_count=4444
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=89 candidates_tokens_details=None prompt_token_count=4355 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4355
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4444 traffic_type=None
```

### `maze_occupancy_6x6_adj_22.txt`

**Score:** 20.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(2,5),(1,5),(1,4),(1,3),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eXyVaYPoNvT1xs0PlO7m0AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=111,
  prompt_token_count=1286,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1286
    ),
  ],
  total_token_count=1397
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=111 candidates_tokens_details=None prompt_token_count=1286 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1286
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1397 traffic_type=None
```

### `maze_occupancy_6x6_ascii_22.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (8, 2), (8, 3), (8, 4), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (10, 10), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (11, 0)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(4,4),(5,4),(5,3),(5,2),(6,2),(7,2),(8,2),(8,3),(8,4),(8,5),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(10,10),(11,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(11,1),(11,0)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='enyVabK5I4uX28oPlq_ciQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=156,
  prompt_token_count=259,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=259
    ),
  ],
  total_token_count=415
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=156 candidates_tokens_details=None prompt_token_count=259 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=259
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=415 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_22.txt`

**Score:** 2.22%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(5,10),(5,9),(5,8),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(6,1),(7,1),(8,1),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='e3yVad-aGpme28oPkrijmAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=174,
  prompt_token_count=2170,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2170
    ),
  ],
  total_token_count=2344
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=174 candidates_tokens_details=None prompt_token_count=2170 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2170
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2344 traffic_type=None
```

