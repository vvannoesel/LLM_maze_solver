# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_9.jpg` | **11.76%** | `input: 435 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_9.json` | **11.76%** | `input: 1810 , ouput: 53` | `(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_9.json` | **58.82%** | `input: 2259 , ouput: 53` | `(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_9.txt` | **58.82%** | `input: 730 , ouput: 53` | `(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_tokenized_9.txt` | **0.00%** | `input: 674 , ouput: 89` | `(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)` |
| `maze_occupancy_6x6_9.jpg` | **0.00%** | `input: 432 , ouput: 283` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (6, 12), (5, 12), (4, 12), (3, 12), (2, 12), (1, 12), (0, 12), (0, 11), (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)` |
| `maze_occupancy_6x6_9.json` | **3.03%** | `input: 989 , ouput: 149` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (6, 6), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_9.json` | **75.76%** | `input: 4346 , ouput: 216` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (10, 3), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_9.txt` | **57.58%** | `input: 1277 , ouput: 107` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_9.txt` | **0.00%** | `input: 253 , ouput: 182` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_tokenized_9.txt` | **15.15%** | `input: 2163 , ouput: 269` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_9.jpg`

**Score:** 11.76%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Kt4daeaNH_GbkdUP8oCjgQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_9.json`

**Score:** 11.76%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(3,3),(3,4),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K94dacrrIK3d7M8PgYaN4AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=1810,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1810
    ),
  ],
  total_token_count=1863
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=1810 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1810
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1863 traffic_type=None
```

### `maze_line_6x6_adj_9.json`

**Score:** 58.82%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(3,1),(3,2),(2,2),(2,3),(2,4),(3,4),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LN4daeH_Je_NkdUPhoC4sAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=2259,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2259
    ),
  ],
  total_token_count=2312
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=2259 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2259
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2312 traffic_type=None
```

### `maze_line_6x6_adj_9.txt`

**Score:** 58.82%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(3,1),(3,2),(2,2),(2,3),(2,4),(3,4),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ld4dae6vGMP2nsEPn4G88AY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=730
    ),
  ],
  total_token_count=783
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=783 traffic_type=None
```

### `maze_line_6x6_tokenized_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(4,1),(5,1),(5,2),(5,3),(5,4),(4,4),(3,4),(2,4),(1,4),(1,5),(2,5),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Lt4dabTdHNPjkdUPquPosAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=89,
  prompt_token_count=674,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=674
    ),
  ],
  total_token_count=763
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=89 candidates_tokens_details=None prompt_token_count=674 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=674
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=763 traffic_type=None
```

### `maze_occupancy_6x6_9.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 2), (7, 1), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (6, 12), (5, 12), (4, 12), (3, 12), (2, 12), (1, 12), (0, 12), (0, 11), (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(4,5),(5,5),(5,4),(5,3),(6,3),(7,3),(7,2),(7,1),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(7,6),(7,7),(7,8),(7,9),(7,10),(7,11),(7,12),(6,12),(5,12),(4,12),(3,12),(2,12),(1,12),(0,12),(0,11),(0,10),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MN4daef5Ju_rkdUPvuTBgQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=283,
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
  total_token_count=715
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=283 candidates_tokens_details=None prompt_token_count=432 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=174
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=715 traffic_type=None
```

### `maze_occupancy_6x6_9.json`

**Score:** 3.03%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (6, 6), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(2,5),(3,5),(3,4),(3,3),(3,2),(4,2),(5,2),(6,2),(7,2),(7,3),(7,4),(7,5),(7,6),(6,6),(5,6),(5,7),(5,8),(5,9),(6,9),(7,9),(8,9),(9,9),(9,8),(9,7),(10,7),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Md4dadWQO_DjkdUP2eDb-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=149,
  prompt_token_count=989,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=989
    ),
  ],
  total_token_count=1138
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=149 candidates_tokens_details=None prompt_token_count=989 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=989
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1138 traffic_type=None
```

### `maze_occupancy_6x6_adj_9.json`

**Score:** 75.76%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (10, 3), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(5,3),(6,3),(7,3),(7,4),(7,5),(6,5),(5,5),(5,6),(5,7),(5,8),(5,9),(6,9),(7,9),(7,8),(7,7),(8,7),(9,7),(10,7),(11,7),(11,6),(11,5),(11,4),(11,3),(10,3),(9,3),(9,2),(9,1),(10,1),(11,1),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(10,9),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M94daZnZIZfMkdUP0o7A8QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=216,
  prompt_token_count=4346,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4346
    ),
  ],
  total_token_count=4562
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=216 candidates_tokens_details=None prompt_token_count=4346 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4346
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4562 traffic_type=None
```

### `maze_occupancy_6x6_adj_9.txt`

**Score:** 57.58%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(5,3),(6,3),(7,3),(7,4),(7,5),(6,5),(5,5),(5,6),(5,7),(5,8),(5,9),(6,9),(7,9),(8,9),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NN4daaODO-CckdUPvdnj0QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=107,
  prompt_token_count=1277,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1277
    ),
  ],
  total_token_count=1384
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=107 candidates_tokens_details=None prompt_token_count=1277 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1277
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1384 traffic_type=None
```

### `maze_occupancy_6x6_ascii_9.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Nt4dab7EB5vhkdUPw-PJkQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=182,
  prompt_token_count=253,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=253
    ),
  ],
  total_token_count=435
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=182 candidates_tokens_details=None prompt_token_count=253 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=253
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=435 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_9.txt`

**Score:** 15.15%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (10, 9), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),(4,11),(5,11),(5,10),(5,9),(5,8),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(5,1),(6,1),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(7,10),(7,11),(8,11),(9,11),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ON4daYKsF-bd7M8P3NWc6QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=269,
  prompt_token_count=2163,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2163
    ),
  ],
  total_token_count=2432
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=269 candidates_tokens_details=None prompt_token_count=2163 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2163
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2432 traffic_type=None
```

