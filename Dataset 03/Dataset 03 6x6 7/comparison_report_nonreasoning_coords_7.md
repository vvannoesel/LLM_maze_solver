# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_7.jpg` | **8.00%** | `input: 435 , ouput: 53` | `(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_7.json` | **16.00%** | `input: 1810 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_7.json` | **96.00%** | `input: 2259 , ouput: 141` | `(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (4, 3), (5, 5)` |
| `maze_line_6x6_adj_7.txt` | **96.00%** | `input: 730 , ouput: 149` | `(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_tokenized_7.txt` | **4.00%** | `input: 674 , ouput: 61` | `(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_7.jpg` | **0.00%** | `input: 432 , ouput: 296` | `(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1), (5, 1), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (9, 3), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (11, 7), (12, 7), (12, 8), (12, 9), (12, 10), (11, 10), (10, 10), (10, 9), (9, 9), (9, 8), (8, 8), (8, 9), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10), (3, 10), (3, 9), (3, 8), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_7.json` | **2.04%** | `input: 989 , ouput: 172` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_7.json` | **100.00%** | `input: 4346 , ouput: 214` | `(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_7.txt` | **42.86%** | `input: 1277 , ouput: 246` | `(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_7.txt` | **0.00%** | `input: 255 , ouput: 117` | `(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), (8, 0), (9, 0), (9, 1), (9, 2), (9, 3), (10, 3), (11, 3), (11, 2), (11, 1), (11, 0), (11, 0), (12, 12)` |
| `maze_occupancy_6x6_tokenized_7.txt` | **2.04%** | `input: 2163 , ouput: 232` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 7), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_7.jpg`

**Score:** 8.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(2,2),(3,2),(3,1),(4,1),(4,2),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Dd4daYezIcyBkdUP7b2V-Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
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
  total_token_count=488
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=435 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=177
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=488 traffic_type=None
```

### `maze_line_6x6_7.json`

**Score:** 16.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(2,2),(2,3),(3,3),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Dt4daeLtKq6mkdUP4uDPsQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_7.json`

**Score:** 96.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (4, 3), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3),(2,2),(3,2),(4,2),(4,1),(3,1),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(4,4),(4,5),(3,5),(2,5),(1,5),(0,5),(0,4),(1,4),(2,4),(3,4),(3,3),(4,3),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EN4daYv6B_i0nsEP8qnlsAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=141,
  prompt_token_count=2259,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2259
    ),
  ],
  total_token_count=2400
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=141 candidates_tokens_details=None prompt_token_count=2259 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2259
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2400 traffic_type=None
```

### `maze_line_6x6_adj_7.txt`

**Score:** 96.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3),(2,2),(3,2),(4,2),(4,1),(3,1),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(4,4),(4,5),(3,5),(2,5),(1,5),(0,5),(0,4),(1,4),(2,4),(3,4),(3,3),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Et4dafakCK3d7M8PgYaN4AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=149,
  prompt_token_count=730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=730
    ),
  ],
  total_token_count=879
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=149 candidates_tokens_details=None prompt_token_count=730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=879 traffic_type=None
```

### `maze_line_6x6_tokenized_7.txt`

**Score:** 4.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='E94daYzKBOCckdUPvdnj0QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=674,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=674
    ),
  ],
  total_token_count=735
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=674 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=674
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=735 traffic_type=None
```

### `maze_occupancy_6x6_7.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1), (5, 1), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (9, 3), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (11, 7), (12, 7), (12, 8), (12, 9), (12, 10), (11, 10), (10, 10), (10, 9), (9, 9), (9, 8), (8, 8), (8, 9), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10), (3, 10), (3, 9), (3, 8), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(2,2),(2,3),(3,3),(4,3),(4,2),(4,1),(5,1),(6,1),(6,2),(6,3),(6,4),(6,5),(7,5),(8,5),(8,4),(8,3),(9,3),(10,3),(10,4),(10,5),(10,6),(10,7),(11,7),(12,7),(12,8),(12,9),(12,10),(11,10),(10,10),(10,9),(9,9),(9,8),(8,8),(8,9),(8,10),(7,10),(6,10),(5,10),(4,10),(3,10),(3,9),(3,8),(3,7),(2,7),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Fd4dabOeMPnk7M8PyOWhkQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=296,
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
  total_token_count=728
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=296 candidates_tokens_details=None prompt_token_count=432 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=174
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=728 traffic_type=None
```

### `maze_occupancy_6x6_7.json`

**Score:** 2.04%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(7,6),(7,5),(7,4),(7,3),(7,2),(8,2),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ft4daZmsPIPOnsEP9aWA-AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=172,
  prompt_token_count=989,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=989
    ),
  ],
  total_token_count=1161
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=172 candidates_tokens_details=None prompt_token_count=989 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=989
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1161 traffic_type=None
```

### `maze_occupancy_6x6_adj_7.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(4,3),(3,3),(2,3),(1,3),(1,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,7),(5,7),(5,6),(5,5),(6,5),(7,5),(8,5),(9,5),(9,4),(9,3),(8,3),(7,3),(7,2),(7,1),(8,1),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(10,9),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GN4daZLJO9eqkdUPjMfHwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=214,
  prompt_token_count=4346,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4346
    ),
  ],
  total_token_count=4560
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=214 candidates_tokens_details=None prompt_token_count=4346 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4346
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4560 traffic_type=None
```

### `maze_occupancy_6x6_adj_7.txt`

**Score:** 42.86%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(4,3),(3,3),(2,3),(1,3),(1,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,7),(5,7),(5,6),(5,5),(4,5),(3,5),(3,9),(4,9),(5,9),(6,9),(7,9),(7,8),(7,7),(8,7),(9,7),(9,5),(9,4),(9,3),(8,3),(7,3),(7,2),(7,1),(8,1),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(10,9),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Gt4dabSuMPjMkdUP3_nxkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=246,
  prompt_token_count=1277,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1277
    ),
  ],
  total_token_count=1523
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=246 candidates_tokens_details=None prompt_token_count=1277 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1277
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1523 traffic_type=None
```

### `maze_occupancy_6x6_ascii_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), (8, 0), (9, 0), (9, 1), (9, 2), (9, 3), (10, 3), (11, 3), (11, 2), (11, 1), (11, 0), (11, 0), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(6,4),(7,4),(7,3),(7,2),(7,1),(7,0),(8,0),(9,0),(9,1),(9,2),(9,3),(10,3),(11,3),(11,2),(11,1),(11,0),(11,0),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G94dafrKMtTrnsEP4-m16QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=117,
  prompt_token_count=255,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=255
    ),
  ],
  total_token_count=372
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=117 candidates_tokens_details=None prompt_token_count=255 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=255
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=372 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_7.txt`

**Score:** 2.04%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 7), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(2,7),(3,7),(3,6),(3,5),(4,5),(5,5),(5,4),(5,3),(5,2),(5,1),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(7,10),(7,11),(8,11),(9,11),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Hd4dabfjBpO4nsEPsNue6AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=232,
  prompt_token_count=2163,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2163
    ),
  ],
  total_token_count=2395
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=232 candidates_tokens_details=None prompt_token_count=2163 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2163
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2395 traffic_type=None
```

