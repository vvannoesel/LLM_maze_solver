# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_43.jpg` | **4.35%** | `input: 442 , ouput: 45` | `(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_43.json` | **13.04%** | `input: 1817 , ouput: 45` | `(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_43.json` | **100.00%** | `input: 2266 , ouput: 93` | `(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_43.txt` | **43.48%** | `input: 737 , ouput: 97` | `(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 1), (2, 2), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (3, 5), (5, 5)` |
| `maze_line_6x6_tokenized_43.txt` | **8.70%** | `input: 681 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_43.jpg` | **0.00%** | `input: 439 , ouput: 366` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (4, 6), (3, 6), (2, 6), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (8, 6), (8, 5), (7, 5), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (11, 3), (11, 2), (12, 2), (12, 3), (12, 4), (12, 5), (11, 5), (10, 5), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (12, 9), (12, 10), (12, 11), (11, 11), (10, 11), (10, 10), (10, 9), (9, 9), (9, 8), (9, 7), (8, 8), (7, 8), (7, 9), (7, 10), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_43.json` | **2.22%** | `input: 996 , ouput: 147` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (8, 4), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_43.json` | **20.00%** | `input: 4351 , ouput: 650` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (8, 11), (7, 11), (7, 10), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (2, 9), (3, 9), (2, 9), (1, 9), (2, 9), (3, 9), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (7, 8), (7, 9), (6, 9), (5, 9), (5, 8), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (8, 11), (7, 11), (7, 10), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (2, 9), (3, 9), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (7, 8), (7, 9), (6, 9), (5, 9), (5, 8), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1)` |
| `maze_occupancy_6x6_adj_43.txt` | **20.00%** | `input: 1287 , ouput: 140` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_43.txt` | **0.00%** | `input: 257 , ouput: 303` | `(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (11, 12)` |
| `maze_occupancy_6x6_tokenized_43.txt` | **2.22%** | `input: 2170 , ouput: 213` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_43.jpg`

**Score:** 4.35%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5H2VaeXHKfDm7M8Po7vO6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
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
  total_token_count=487
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=442 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=184
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=487 traffic_type=None
```

### `maze_line_6x6_43.json`

**Score:** 13.04%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5X2VaeuAHvT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_43.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(0,2),(0,3),(1,3),(2,3),(3,3),(3,2),(2,2),(2,1),(3,1),(3,0),(4,0),(5,0),(5,1),(5,2),(4,2),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5n2VaYX8G9ihnsEPoYDhmQo' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_43.txt`

**Score:** 43.48%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 1), (2, 2), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (3, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(0,2),(0,3),(1,3),(2,3),(3,3),(3,2),(2,1),(2,2),(3,1),(3,0),(4,0),(5,0),(5,1),(5,2),(4,2),(4,3),(4,4),(4,5),(3,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='532VaZmqGPfonsEPuaungAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_43.txt`

**Score:** 8.70%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(3,1),(4,1),(4,2),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6H2Vaa71CK2WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_43.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (4, 6), (3, 6), (2, 6), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (8, 6), (8, 5), (7, 5), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (11, 3), (11, 2), (12, 2), (12, 3), (12, 4), (12, 5), (11, 5), (10, 5), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (12, 9), (12, 10), (12, 11), (11, 11), (10, 11), (10, 10), (10, 9), (9, 9), (9, 8), (9, 7), (8, 8), (7, 8), (7, 9), (7, 10), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(4,4),(4,5),(4,6),(3,6),(2,6),(1,6),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(8,6),(8,5),(7,5),(7,4),(8,4),(9,4),(10,4),(11,4),(11,3),(11,2),(12,2),(12,3),(12,4),(12,5),(11,5),(10,5),(10,6),(10,7),(10,8),(11,8),(12,8),(12,9),(12,10),(12,11),(11,11),(10,11),(10,10),(10,9),(9,9),(9,8),(9,7),(8,8),(7,8),(7,9),(7,10),(7,11),(6,11),(5,11),(5,10),(5,9),(4,9),(3,9),(2,9),(1,9),(1,10),(1,11),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6n2Vac_eMqG-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=366,
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
  total_token_count=805
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=366 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=181
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=805 traffic_type=None
```

### `maze_occupancy_6x6_43.json`

**Score:** 2.22%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (8, 4), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(7,6),(7,5),(7,4),(8,4),(9,4),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='632Vae3pMa7pnsEP2M6v6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=147,
  prompt_token_count=996,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=996
    ),
  ],
  total_token_count=1143
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=147 candidates_tokens_details=None prompt_token_count=996 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=996
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1143 traffic_type=None
```

### `maze_occupancy_6x6_adj_43.json`

**Score:** 20.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (8, 11), (7, 11), (7, 10), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (2, 9), (3, 9), (2, 9), (1, 9), (2, 9), (3, 9), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (7, 8), (7, 9), (6, 9), (5, 9), (5, 8), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (8, 11), (7, 11), (7, 10), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (2, 9), (3, 9), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (7, 8), (7, 9), (6, 9), (5, 9), (5, 8), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(2,5),(1,5),(1,4),(1,3),(1,5),(2,5),(3,5),(4,5),(5,5),(5,4),(5,3),(6,3),(7,3),(7,2),(7,1),(8,1),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(10,5),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(8,11),(7,11),(7,10),(7,9),(6,9),(5,9),(5,10),(5,11),(4,11),(3,11),(2,11),(1,11),(1,10),(1,9),(2,9),(3,9),(2,9),(1,9),(2,9),(3,9),(3,7),(4,7),(5,7),(6,7),(7,7),(7,6),(7,5),(6,5),(5,5),(5,6),(5,7),(6,7),(7,7),(7,8),(7,9),(6,9),(5,9),(5,8),(5,7),(6,7),(7,7),(7,6),(7,5),(6,5),(5,5),(5,4),(5,3),(6,3),(7,3),(7,2),(7,1),(8,1),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(10,5),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(8,11),(7,11),(7,10),(7,9),(6,9),(5,9),(5,10),(5,11),(4,11),(3,11),(2,11),(1,11),(1,10),(1,9),(2,9),(3,9),(3,7),(4,7),(5,7),(6,7),(7,7),(7,6),(7,5),(6,5),(5,5),(5,6),(5,7),(6,7),(7,7),(7,8),(7,9),(6,9),(5,9),(5,8),(5,7),(6,7),(7,7),(7,6),(7,5),(6,5),(5,5),(5,4),(5,3),(6,3),(7,3),(7,2),(7,1),(8,1'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7X2VabSfFPujkdUP0fjD0QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4351,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4351
    ),
  ],
  total_token_count=5001
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4351 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4351
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=5001 traffic_type=None
```

### `maze_occupancy_6x6_adj_43.txt`

**Score:** 20.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(2,5),(1,5),(1,4),(1,3),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7n2VabeRA5nqkdUP3rjkuQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=140,
  prompt_token_count=1287,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1287
    ),
  ],
  total_token_count=1427
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=140 candidates_tokens_details=None prompt_token_count=1287 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1287
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1427 traffic_type=None
```

### `maze_occupancy_6x6_ascii_43.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (11, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(2,2),(2,3),(2,4),(3,4),(4,4),(5,4),(5,3),(5,2),(6,2),(7,2),(7,3),(7,4),(7,5),(8,5),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(10,11),(11,11),(11,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(11,1),(10,1),(9,1),(8,1),(7,1),(6,1),(5,1),(4,1),(3,1),(3,2),(3,3),(3,4),(2,4),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11),(11,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='732VacH0DLyK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=303,
  prompt_token_count=257,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=257
    ),
  ],
  total_token_count=560
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=303 candidates_tokens_details=None prompt_token_count=257 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=257
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=560 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_43.txt`

**Score:** 2.22%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (10, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(3,10),(3,9),(3,8),(3,7),(4,7),(5,7),(5,8),(5,9),(5,10),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(7,6),(7,5),(7,4),(7,3),(7,2),(7,1),(8,1),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8H2VadL4Gqnw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=213,
  prompt_token_count=2170,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2170
    ),
  ],
  total_token_count=2383
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=213 candidates_tokens_details=None prompt_token_count=2170 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2170
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2383 traffic_type=None
```

