# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_44.jpg` | **4.76%** | `input: 442 , ouput: 61` | `(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_44.json` | **4.76%** | `input: 1817 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_44.json` | **90.48%** | `input: 2266 , ouput: 109` | `(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (2, 4), (3, 3), (4, 3), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_44.txt` | **14.29%** | `input: 737 , ouput: 69` | `(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (4, 5), (5, 5)` |
| `maze_line_6x6_tokenized_44.txt` | **0.00%** | `input: 681 , ouput: 41` | `(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_occupancy_6x6_44.jpg` | **0.00%** | `input: 439 , ouput: 116` | `(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 5), (7, 6), (8, 6), (9, 6), (9, 7), (9, 8), (10, 8), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_44.json` | **51.22%** | `input: 996 , ouput: 127` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_44.json` | **90.24%** | `input: 4347 , ouput: 267` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 8), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_44.txt` | **100.00%** | `input: 1284 , ouput: 182` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_44.txt` | **0.00%** | `input: 261 , ouput: 178` | `(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (8, 5), (9, 5), (10, 5), (10, 4), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (12, 11)` |
| `maze_occupancy_6x6_tokenized_44.txt` | **21.95%** | `input: 2170 , ouput: 650` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (7, 7), (7, 5), (7, 3), (7, 2), (7, 1), (8, 5), (8, 7), (8, 9), (8, 11), (6, 11), (6, 7), (6, 5), (6, 3), (6, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (7, 7), (7, 5), (7, 3), (7, 2), (7, 1), (8, 5), (8, 7), (8, 9), (8, 11), (6, 11), (6, 7), (6, 5), (6, 3), (6, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (7, 7), (7, 5), (7, 3), (7, 2), (7, 1), (8, 5), (8, 7), (8, 9), (8, 11), (6, 11), (6, 7), (6, 5), (6, 3), (6, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9)` |

---

## Full LLM Responses

### `maze_line_6x6_44.jpg`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(3,1),(4,1),(4,0),(5,0),(5,1),(5,2),(4,2),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_n2VacenHPjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_44.json`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='_32Vaf2BHoqjkdUP-qvu2QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_44.json`

**Score:** 90.48%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (2, 4), (3, 3), (4, 3), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(2,1),(2,2),(3,2),(4,2),(4,1),(5,1),(5,2),(5,3),(5,4),(4,4),(3,4),(3,5),(2,5),(1,5),(1,4),(2,4),(3,3),(4,3),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AH6Vaf2WH6zd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=109,
  prompt_token_count=2266,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2266
    ),
  ],
  total_token_count=2375
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=109 candidates_tokens_details=None prompt_token_count=2266 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2266
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2375 traffic_type=None
```

### `maze_line_6x6_adj_44.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(2,1),(2,2),(3,2),(4,2),(4,1),(5,1),(5,2),(5,3),(5,4),(4,4),(3,4),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='AX6VacqcG6G-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=69,
  prompt_token_count=737,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=737
    ),
  ],
  total_token_count=806
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=69 candidates_tokens_details=None prompt_token_count=737 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=737
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=806 traffic_type=None
```

### `maze_line_6x6_tokenized_44.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(2,2),(2,3),(3,3),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='An6VaZbZBryK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_44.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 5), (7, 6), (8, 6), (9, 6), (9, 7), (9, 8), (10, 8), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(5,2),(5,3),(5,4),(6,4),(7,4),(7,5),(7,6),(8,6),(9,6),(9,7),(9,8),(10,8),(11,8),(11,9),(11,10),(11,11),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BH6VafeVAq7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=116,
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
  total_token_count=555
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=116 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=181
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=555 traffic_type=None
```

### `maze_occupancy_6x6_44.json`

**Score:** 51.22%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(6,3),(5,3),(5,4),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='BH6VaZT-M4KG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=127,
  prompt_token_count=996,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=996
    ),
  ],
  total_token_count=1123
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=127 candidates_tokens_details=None prompt_token_count=996 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=996
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1123 traffic_type=None
```

### `maze_occupancy_6x6_adj_44.json`

**Score:** 90.24%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 8), (5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(6,3),(5,3),(5,4),(5,5),(6,5),(7,5),(8,5),(9,5),(9,4),(9,3),(10,3),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(10,9),(9,9),(8,9),(7,9),(7,10),(7,11),(6,11),(5,11),(4,11),(3,11),(3,10),(3,9),(4,9),(5,9),(5,8),(5,7),(4,7),(3,7),(3,6),(3,5),(2,5),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Bn6VafLlDYDHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=267,
  prompt_token_count=4347,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4347
    ),
  ],
  total_token_count=4614
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=267 candidates_tokens_details=None prompt_token_count=4347 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4347
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4614 traffic_type=None
```

### `maze_occupancy_6x6_adj_44.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(6,3),(5,3),(5,4),(5,5),(6,5),(7,5),(8,5),(9,5),(9,4),(9,3),(10,3),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(10,9),(9,9),(8,9),(7,9),(7,10),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='B36VabyAE-jpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=182,
  prompt_token_count=1284,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1284
    ),
  ],
  total_token_count=1466
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=182 candidates_tokens_details=None prompt_token_count=1284 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1284
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1466 traffic_type=None
```

### `maze_occupancy_6x6_ascii_44.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (8, 5), (9, 5), (10, 5), (10, 4), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (12, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(3,10),(3,9),(3,8),(3,7),(4,7),(5,7),(6,7),(7,7),(7,6),(7,5),(8,5),(9,5),(10,5),(10,4),(10,3),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(12,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CH6VaYzoFO3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=178,
  prompt_token_count=261,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=261
    ),
  ],
  total_token_count=439
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=178 candidates_tokens_details=None prompt_token_count=261 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=261
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=439 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_44.txt`

**Score:** 21.95%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (7, 7), (7, 5), (7, 3), (7, 2), (7, 1), (8, 5), (8, 7), (8, 9), (8, 11), (6, 11), (6, 7), (6, 5), (6, 3), (6, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (7, 7), (7, 5), (7, 3), (7, 2), (7, 1), (8, 5), (8, 7), (8, 9), (8, 11), (6, 11), (6, 7), (6, 5), (6, 3), (6, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (7, 7), (7, 5), (7, 3), (7, 2), (7, 1), (8, 5), (8, 7), (8, 9), (8, 11), (6, 11), (6, 7), (6, 5), (6, 3), (6, 1), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (5, 9), (7, 9), (7, 10), (7, 11), (11, 11), (11, 10), (11, 9)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,3),(5,4),(5,5),(5,7),(5,8),(5,9),(7,9),(7,10),(7,11),(11,11),(11,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(11,1),(10,1),(9,1),(9,3),(9,4),(9,5),(9,7),(9,9),(7,7),(7,5),(7,3),(7,2),(7,1),(8,5),(8,7),(8,9),(8,11),(6,11),(6,7),(6,5),(6,3),(6,1),(5,1),(5,3),(5,4),(5,5),(5,7),(5,8),(5,9),(7,9),(7,10),(7,11),(11,11),(11,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(11,1),(10,1),(9,1),(9,3),(9,4),(9,5),(9,7),(9,9),(7,7),(7,5),(7,3),(7,2),(7,1),(8,5),(8,7),(8,9),(8,11),(6,11),(6,7),(6,5),(6,3),(6,1),(5,1),(5,3),(5,4),(5,5),(5,7),(5,8),(5,9),(7,9),(7,10),(7,11),(11,11),(11,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(11,1),(10,1),(9,1),(9,3),(9,4),(9,5),(9,7),(9,9),(7,7),(7,5),(7,3),(7,2),(7,1),(8,5),(8,7),(8,9),(8,11),(6,11),(6,7),(6,5),(6,3),(6,1),(5,1),(5,3),(5,4),(5,5),(5,7),(5,8),(5,9),(7,9),(7,10),(7,11),(11,11),(11,10),(11,9),('
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='CX6VaazEO9qI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

