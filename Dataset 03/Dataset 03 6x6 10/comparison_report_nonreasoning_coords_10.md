# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_10.jpg` | **4.76%** | `input: 435 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_10.json` | **4.76%** | `input: 1810 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_10.json` | **76.19%** | `input: 2259 , ouput: 69` | `(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_10.txt` | **47.62%** | `input: 730 , ouput: 650` | `(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)` |
| `maze_line_6x6_tokenized_10.txt` | **4.76%** | `input: 674 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_10.jpg` | **0.00%** | `input: 432 , ouput: 171` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (6, 6), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (9, 3), (9, 2), (9, 1), (9, 0), (10, 0), (11, 0), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)` |
| `maze_occupancy_6x6_10.json` | **12.20%** | `input: 989 , ouput: 147` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_10.json` | **46.34%** | `input: 4343 , ouput: 267` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (7, 4), (7, 3), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 5), (2, 5), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_10.txt` | **46.34%** | `input: 1275 , ouput: 284` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (7, 4), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_10.txt` | **0.00%** | `input: 247 , ouput: 150` | `(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (9, 0), (10, 0), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)` |
| `maze_occupancy_6x6_tokenized_10.txt` | **12.20%** | `input: 2163 , ouput: 196` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_10.jpg`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 4), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(3,1),(3,2),(4,2),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Od4daa6mKoy3nsEP9Num8QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=435,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=177
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=480
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=435 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=435 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=177
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=480 traffic_type=None
```

### `maze_line_6x6_10.json`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 4), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(2,2),(3,2),(3,3),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ot4daez7JKCvkdUPpoG7wQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=1810,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1810
    ),
  ],
  total_token_count=1855
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=193 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=1810 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1810
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1855 traffic_type=None
```

### `maze_line_6x6_adj_10.json`

**Score:** 76.19%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 4), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(2,2),(2,3),(2,4),(3,4),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='O94daevXHK-0nsEPo5aT6Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=69,
  prompt_token_count=2259,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2259
    ),
  ],
  total_token_count=2328
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=164 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=69 candidates_tokens_details=None prompt_token_count=2259 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2259
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2328 traffic_type=None
```

### `maze_line_6x6_adj_10.txt`

**Score:** 47.62%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 4), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,1),(2,1),(1,1),(0,1),(0,0),(1,0),(2,0),(3,0),(4'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Pd4daZzTMtH3nsEPo6qHyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=730
    ),
  ],
  total_token_count=1380
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1380 traffic_type=None
```

### `maze_line_6x6_tokenized_10.txt`

**Score:** 4.76%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 4), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(3,1),(4,1),(4,2),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Pt4daZifOKXrkdUPm7nk2AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=674,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=674
    ),
  ],
  total_token_count=719
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=674 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=674
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=719 traffic_type=None
```

### `maze_occupancy_6x6_10.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (6, 6), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (9, 3), (9, 2), (9, 1), (9, 0), (10, 0), (11, 0), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(2,4),(2,5),(3,5),(4,5),(4,6),(4,7),(5,7),(6,7),(6,6),(6,5),(7,5),(8,5),(8,4),(8,3),(9,3),(9,2),(9,1),(9,0),(10,0),(11,0),(12,0),(12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QN4daZG_OcOdkdUP2_mE2QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=171,
  prompt_token_count=432,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=174
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=603
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=432 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=171 candidates_tokens_details=None prompt_token_count=432 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=174
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=603 traffic_type=None
```

### `maze_occupancy_6x6_10.json`

**Score:** 12.20%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(4,9),(5,9),(5,8),(5,7),(5,6),(5,5),(5,4),(6,4),(7,4),(7,3),(7,2),(8,2),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Qt4dadfdBZzo7M8PmunkwAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=147,
  prompt_token_count=989,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=989
    ),
  ],
  total_token_count=1136
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=175 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=147 candidates_tokens_details=None prompt_token_count=989 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=989
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1136 traffic_type=None
```

### `maze_occupancy_6x6_adj_10.json`

**Score:** 46.34%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (7, 4), (7, 3), (7, 7), (8, 7), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 5), (2, 5), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(4,3),(5,3),(5,2),(5,1),(6,1),(7,1),(8,1),(9,1),(9,2),(9,3),(9,4),(9,5),(8,5),(7,5),(7,4),(7,3),(7,7),(8,7),(9,7),(9,8),(9,9),(9,10),(9,11),(8,11),(7,11),(6,11),(5,11),(4,11),(3,11),(2,11),(1,11),(1,10),(1,9),(1,8),(1,7),(1,5),(2,5),(3,5),(3,6),(3,7),(3,8),(3,9),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,7),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RN4daYysEv36nsEP492R-AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=267,
  prompt_token_count=4343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4343
    ),
  ],
  total_token_count=4610
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=166 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=267 candidates_tokens_details=None prompt_token_count=4343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4343
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4610 traffic_type=None
```

### `maze_occupancy_6x6_adj_10.txt`

**Score:** 46.34%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (7, 4), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""(1,1),(1,2),(1,3),(2,3),(3,3),(4,3),(5,3),(5,2),(5,1),(6,1),(7,1),(8,1),(9,1),(9,2),(9,3),(9,4),(9,5),(8,5),(7,5),(7,4),(7,3),(6,3),(5,3),(4,3),(3,3),(2,3),(1,3),(1,2),(1,1) is not a valid path. I apologize for the mistake. Let me re-evaluate the path using a proper search algorithm.

(1,1),(1,2),(1,3),(2,3),(3,3),(4,3),(5,3),(5,2),(5,1),(6,1),(7,1),(8,1),(9,1),(9,2),(9,3),(9,4),(9,5),(8,5),(7,5),(6,5),(5,5),(5,6),(5,7),(5,8),(5,9),(6,9),(7,9),(7,10),(7,11),(8,11),(9,11),(10,11),(11,11)"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Rt4dabTMDML_nsEPmfvl0AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=284,
  prompt_token_count=1275,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1275
    ),
  ],
  total_token_count=1559
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=199 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=284 candidates_tokens_details=None prompt_token_count=1275 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1275
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1559 traffic_type=None
```

### `maze_occupancy_6x6_ascii_10.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (9, 0), (10, 0), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(6,3),(7,3),(7,4),(7,5),(8,5),(9,5),(9,4),(9,3),(9,2),(9,1),(9,0),(10,0),(11,0),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='R94dae3cKqaRkdUPzOGGuAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=150,
  prompt_token_count=247,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=247
    ),
  ],
  total_token_count=397
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=150 candidates_tokens_details=None prompt_token_count=247 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=247
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=397 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_10.txt`

**Score:** 12.20%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(7,6),(7,5),(7,4),(7,3),(8,3),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(10,7),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Sd4dacbOL6XrkdUPm7nk2AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=196,
  prompt_token_count=2163,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2163
    ),
  ],
  total_token_count=2359
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=196 candidates_tokens_details=None prompt_token_count=2163 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2163
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2359 traffic_type=None
```

