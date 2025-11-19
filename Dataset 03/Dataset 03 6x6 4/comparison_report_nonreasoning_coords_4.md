# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_4.jpg` | **3.45%** | `input: 435 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_4.json` | **13.79%** | `input: 1810 , ouput: 45` | `(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_4.json` | **44.83%** | `input: 2259 , ouput: 93` | `(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_4.txt` | **24.14%** | `input: 730 , ouput: 61` | `(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_tokenized_4.txt` | **3.45%** | `input: 674 , ouput: 53` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_occupancy_6x6_4.jpg` | **0.00%** | `input: 432 , ouput: 125` | `(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (7, 6), (7, 5), (7, 4), (8, 4), (9, 4), (9, 5), (9, 6), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_4.json` | **29.82%** | `input: 989 , ouput: 154` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 2), (10, 2), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_4.json` | **85.96%** | `input: 4347 , ouput: 236` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_4.txt` | **100.00%** | `input: 1278 , ouput: 244` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_ascii_4.txt` | **0.00%** | `input: 250 , ouput: 139` | `(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)` |
| `maze_occupancy_6x6_tokenized_4.txt` | **22.81%** | `input: 2163 , ouput: 650` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_4.jpg`

**Score:** 3.45%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xt0dadbEAq3d7M8PgYaN4AY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_4.json`

**Score:** 13.79%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xt0daYXlK_qAkdUPsrDQ2QY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_4.json`

**Score:** 44.83%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(1,3),(2,3),(2,2),(1,2),(1,1),(1,0),(2,0),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='x90dafq6N8-5kdUPlt7QyAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=93,
  prompt_token_count=2259,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2259
    ),
  ],
  total_token_count=2352
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=93 candidates_tokens_details=None prompt_token_count=2259 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2259
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2352 traffic_type=None
```

### `maze_line_6x6_adj_4.txt`

**Score:** 24.14%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(1,3),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yd0daZioDs__nsEP6fGFiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=730
    ),
  ],
  total_token_count=791
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=791 traffic_type=None
```

### `maze_line_6x6_tokenized_4.txt`

**Score:** 3.45%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(4,1),(5,1),(5,2),(5,3),(4,3),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yt0daYvJBJvhkdUPw-PJkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=674,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=674
    ),
  ],
  total_token_count=727
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=674 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=674
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=727 traffic_type=None
```

### `maze_occupancy_6x6_4.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (7, 6), (7, 5), (7, 4), (8, 4), (9, 4), (9, 5), (9, 6), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(2,2),(2,3),(3,3),(4,3),(4,4),(4,5),(4,6),(5,6),(6,6),(7,6),(7,5),(7,4),(8,4),(9,4),(9,5),(9,6),(9,7),(10,7),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zN0daayTBrfz7M8Pn_rtkAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=125,
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
  total_token_count=557
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=125 candidates_tokens_details=None prompt_token_count=432 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=174
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=557 traffic_type=None
```

### `maze_occupancy_6x6_4.json`

**Score:** 29.82%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 2), (10, 2), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(3,8),(3,7),(4,7),(5,7),(5,6),(5,5),(6,5),(7,5),(7,4),(7,3),(8,3),(9,3),(9,2),(10,2),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zd0dac_RJJvhkdUPwuPJkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=154,
  prompt_token_count=989,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=989
    ),
  ],
  total_token_count=1143
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=154 candidates_tokens_details=None prompt_token_count=989 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=989
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1143 traffic_type=None
```

### `maze_occupancy_6x6_adj_4.json`

**Score:** 85.96%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(3,8),(3,7),(4,7),(5,7),(5,6),(5,5),(4,5),(3,5),(3,4),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(6,3),(7,3),(7,4),(7,5),(8,5),(9,5),(9,4),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(10,7),(9,7),(8,7),(7,7),(8,9),(9,9),(10,9),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='zt0daZbjPMfwnsEPq8SFyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=236,
  prompt_token_count=4347,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4347
    ),
  ],
  total_token_count=4583
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=236 candidates_tokens_details=None prompt_token_count=4347 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4347
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4583 traffic_type=None
```

### `maze_occupancy_6x6_adj_4.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(3,8),(3,7),(4,7),(5,7),(5,6),(5,5),(4,5),(3,5),(3,4),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(6,3),(7,3),(7,4),(7,5),(8,5),(9,5),(9,4),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(10,7),(9,7),(8,7),(7,7),(7,8),(7,9),(8,9),(9,9),(10,9),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0N0dacG2JvDjkdUP2eDb-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=244,
  prompt_token_count=1278,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1278
    ),
  ],
  total_token_count=1522
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=244 candidates_tokens_details=None prompt_token_count=1278 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1278
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1522 traffic_type=None
```

### `maze_occupancy_6x6_ascii_4.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(4,4),(5,4),(5,3),(5,2),(6,2),(7,2),(7,3),(7,4),(7,5),(8,5),(9,5),(9,4),(9,3),(10,3),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='0d0dab7eMP7tkdUPu_KDwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=139,
  prompt_token_count=250,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=250
    ),
  ],
  total_token_count=389
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=139 candidates_tokens_details=None prompt_token_count=250 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=250
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=389 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_4.txt`

**Score:** 22.81%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (2, 9), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(3,8),(3,7),(3,6),(3,5),(3,4),(3,3),(3,2),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(4,11),(3,11),(2,11),(1,11),(1,10),(1,9),(1,8),(1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(4,11),(3,11),(2,11),(1,11),(1,10),(1,9),(1,8),(1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(2,9),(1,9),(1,8),(1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(4,11),(3,11),(2,11),(1,11),(1,10),(1,9),(1,8),(1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(2,9),(1,9),(1,8),(1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(4,11),(3'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='1N0daeW6NPGbkdUP8oCjgQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2163,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2163
    ),
  ],
  total_token_count=2813
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2163 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2163
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2813 traffic_type=None
```

