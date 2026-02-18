# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_29.jpg` | **4.00%** | `input: 442 , ouput: 53` | `(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_29.json` | **4.00%** | `input: 1817 , ouput: 61` | `(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_29.json` | **64.00%** | `input: 2266 , ouput: 129` | `(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (2, 2), (2, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_29.txt` | **56.00%** | `input: 737 , ouput: 97` | `(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)` |
| `maze_line_6x6_tokenized_29.txt` | **0.00%** | `input: 681 , ouput: 41` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)` |
| `maze_occupancy_6x6_29.jpg` | **0.00%** | `input: 439 , ouput: 112` | `(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7), (8, 7), (8, 8), (9, 8), (9, 9), (10, 9), (10, 10), (11, 10), (11, 11), (12, 11), (12, 12)` |
| `maze_occupancy_6x6_29.json` | **30.61%** | `input: 996 , ouput: 244` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (6, 7), (5, 7), (4, 7), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_29.json` | **63.27%** | `input: 4345 , ouput: 183` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_29.txt` | **63.27%** | `input: 1283 , ouput: 393` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 11), (5, 10), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (2, 5), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (8, 5), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_29.txt` | **0.00%** | `input: 257 , ouput: 119` | `(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)` |
| `maze_occupancy_6x6_tokenized_29.txt` | **18.37%** | `input: 2170 , ouput: 147` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 5), (7, 4), (7, 3), (7, 2), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 11), (10, 11), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_29.jpg`

**Score:** 4.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8nyVaanqMYzLvdIP8raG-Qs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
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
  total_token_count=495
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=442 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=184
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=495 traffic_type=None
```

### `maze_line_6x6_29.json`

**Score:** 4.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3),(3,3),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='83yVaYH8JczXvdIPq7fiiAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=1817,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1817
    ),
  ],
  total_token_count=1878
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=1817 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1817
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1878 traffic_type=None
```

### `maze_line_6x6_adj_29.json`

**Score:** 64.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (2, 2), (2, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,3),(4,4),(3,4),(3,3),(2,3),(1,3),(1,2),(2,2),(2,1),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,3),(4,4),(3,4),(2,4),(2,5),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9HyVaemEMpXIvdIP-oyG2AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=129,
  prompt_token_count=2266,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2266
    ),
  ],
  total_token_count=2395
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=129 candidates_tokens_details=None prompt_token_count=2266 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2266
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2395 traffic_type=None
```

### `maze_line_6x6_adj_29.txt`

**Score:** 56.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,3),(4,4),(3,4),(3,3),(2,3),(1,2),(0,2),(0,3),(0,4),(1,4),(2,4),(2,5),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9XyVaaKMJaS9xN8PvoPm4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=97,
  prompt_token_count=737,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=737
    ),
  ],
  total_token_count=834
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=97 candidates_tokens_details=None prompt_token_count=737 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=737
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=834 traffic_type=None
```

### `maze_line_6x6_tokenized_29.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9nyVaYKXGYaSxN8P5cLTkAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=681,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=681
    ),
  ],
  total_token_count=722
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=681 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=681
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=722 traffic_type=None
```

### `maze_occupancy_6x6_29.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7), (8, 7), (8, 8), (9, 8), (9, 9), (10, 9), (10, 10), (11, 10), (11, 11), (12, 11), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(4,3),(4,4),(5,4),(5,5),(6,5),(6,6),(7,6),(7,7),(8,7),(8,8),(9,8),(9,9),(10,9),(10,10),(11,10),(11,11),(12,11),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='93yVafCRLaS9xN8P6rzX8AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=112,
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
  total_token_count=551
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=112 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=181
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=551 traffic_type=None
```

### `maze_occupancy_6x6_29.json`

**Score:** 30.61%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (6, 7), (5, 7), (4, 7), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(6,7),(5,7),(4,7),(3,7),(3,8),(3,9),(3,10),(3,11),(2,11),(1,11),(1,10),(1,9),(1,8),(1,7),(1,6),(1,5),(1,4),(2,4),(3,4),(4,4),(5,4),(5,3),(6,3),(7,3),(8,3),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-HyVaaKPK4bIvdIPqfe6oAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=244,
  prompt_token_count=996,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=996
    ),
  ],
  total_token_count=1240
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=244 candidates_tokens_details=None prompt_token_count=996 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=996
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1240 traffic_type=None
```

### `maze_occupancy_6x6_adj_29.json`

**Score:** 63.27%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(7,4),(7,5),(8,5),(9,5),(9,6),(9,7),(9,8),(9,9),(8,9),(7,9),(7,8),(7,7),(6,7),(5,7),(4,7),(3,7),(3,6),(3,5),(4,5),(5,5),(5,4),(5,3),(5,10),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-XyVacjzMtPevdIPk6fOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=183,
  prompt_token_count=4345,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4345
    ),
  ],
  total_token_count=4528
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=183 candidates_tokens_details=None prompt_token_count=4345 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4345
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4528 traffic_type=None
```

### `maze_occupancy_6x6_adj_29.txt`

**Score:** 63.27%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 11), (5, 10), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (2, 5), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (8, 5), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(7,4),(7,5),(8,5),(9,5),(9,6),(9,7),(9,8),(9,9),(8,9),(7,9),(7,8),(7,7),(6,7),(5,7),(4,7),(3,7),(3,6),(3,5),(4,5),(5,5),(5,4),(5,3),(5,11),(5,10),(5,9),(4,9),(3,9),(2,9),(1,9),(1,8),(1,7),(1,6),(1,5),(2,5),(3,5),(3,6),(3,7),(4,7),(5,7),(6,7),(7,7),(7,8),(7,9),(8,9),(9,9),(9,8),(9,7),(9,6),(9,5),(8,5),(7,5),(7,4),(7,3),(7,2),(7,1),(6,1),(5,1),(4,1),(3,1),(3,2),(3,3),(2,3),(1,3),(1,2),(1,1),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(4,9),(5,9),(5,10),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-3yVaYugJOb1xN8PzZ3x8QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=393,
  prompt_token_count=1283,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1283
    ),
  ],
  total_token_count=1676
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=393 candidates_tokens_details=None prompt_token_count=1283 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1283
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1676 traffic_type=None
```

### `maze_occupancy_6x6_ascii_29.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(5,3),(5,4),(5,5),(6,5),(7,5),(7,4),(7,3),(8,3),(9,3),(9,4),(9,5),(9,6),(9,7),(10,7),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_HyVabawD8L1xs0Pl-qmkAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=119,
  prompt_token_count=257,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=257
    ),
  ],
  total_token_count=376
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=119 candidates_tokens_details=None prompt_token_count=257 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=257
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=376 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_29.txt`

**Score:** 18.37%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 5), (7, 4), (7, 3), (7, 2), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,3),(5,4),(5,5),(5,9),(5,10),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(7,5),(7,4),(7,3),(7,2),(8,5),(9,5),(9,6),(9,7),(9,8),(9,9),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_XyVaevwBs2pvdIP5cbXoAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=147,
  prompt_token_count=2170,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2170
    ),
  ],
  total_token_count=2317
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=147 candidates_tokens_details=None prompt_token_count=2170 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2170
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2317 traffic_type=None
```

