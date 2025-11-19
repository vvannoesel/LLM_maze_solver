# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_8.jpg` | **9.09%** | `input: 435 , ouput: 45` | `(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_8.json` | **36.36%** | `input: 1810 , ouput: 53` | `(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_8.json` | **81.82%** | `input: 2259 , ouput: 45` | `(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_8.txt` | **100.00%** | `input: 730 , ouput: 45` | `(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5)` |
| `maze_line_6x6_tokenized_8.txt` | **9.09%** | `input: 674 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_8.jpg` | **0.00%** | `input: 432 , ouput: 219` | `(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (5, 2), (6, 2), (6, 1), (6, 0), (7, 0), (7, 1), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_8.json` | **80.95%** | `input: 989 , ouput: 139` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_8.json` | **100.00%** | `input: 4343 , ouput: 91` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_8.txt` | **100.00%** | `input: 1275 , ouput: 91` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_ascii_8.txt` | **0.00%** | `input: 254 , ouput: 235` | `(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (12, 11)` |
| `maze_occupancy_6x6_tokenized_8.txt` | **52.38%** | `input: 2163 , ouput: 179` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_8.jpg`

**Score:** 9.09%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(3,1),(3,2),(4,2),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ht4dacP2COXNkdUPpKHQuQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_8.json`

**Score:** 36.36%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(4,3),(4,2),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ht4dacLlM8fwnsEPq8SFyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_8.json`

**Score:** 81.82%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4),(3,4),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='H94daaOALcOdkdUP6PmE2QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=2259,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2259
    ),
  ],
  total_token_count=2304
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=2259 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2259
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2304 traffic_type=None
```

### `maze_line_6x6_adj_8.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IN4dabK4M8__nsEP6fGFiQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
  prompt_token_count=730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=730
    ),
  ],
  total_token_count=775
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=775 traffic_type=None
```

### `maze_line_6x6_tokenized_8.txt`

**Score:** 9.09%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Id4dadPfJNPjkdUPquPosAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_8.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (5, 2), (6, 2), (6, 1), (6, 0), (7, 0), (7, 1), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (8, 7), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(2,2),(2,3),(2,4),(3,4),(4,4),(4,3),(4,2),(5,2),(6,2),(6,1),(6,0),(7,0),(7,1),(7,2),(8,2),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(8,7),(7,7),(6,7),(5,7),(4,7),(3,7),(2,7),(1,7),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I94dacX5MpO4nsEPsNue6AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=219,
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
  total_token_count=651
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=219 candidates_tokens_details=None prompt_token_count=432 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=174
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=651 traffic_type=None
```

### `maze_occupancy_6x6_8.json`

**Score:** 80.95%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(10,5),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JN4daaDnNJuI7M8P-dfOuQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=139,
  prompt_token_count=989,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=989
    ),
  ],
  total_token_count=1128
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=139 candidates_tokens_details=None prompt_token_count=989 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=989
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1128 traffic_type=None
```

### `maze_occupancy_6x6_adj_8.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Jt4daf_8A-nd7M8PlPjCwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=91,
  prompt_token_count=4343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4343
    ),
  ],
  total_token_count=4434
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=91 candidates_tokens_details=None prompt_token_count=4343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4343
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4434 traffic_type=None
```

### `maze_occupancy_6x6_adj_8.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Jt4dadKLL5zo7M8PmunkwAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=91,
  prompt_token_count=1275,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1275
    ),
  ],
  total_token_count=1366
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=91 candidates_tokens_details=None prompt_token_count=1275 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1275
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1366 traffic_type=None
```

### `maze_occupancy_6x6_ascii_8.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (12, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(9,1),(8,1),(7,1),(6,1),(5,1),(4,1),(3,1),(3,2),(3,3),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(12,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KN4daZnPDrO9kdUPou6g8QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=235,
  prompt_token_count=254,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=254
    ),
  ],
  total_token_count=489
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=235 candidates_tokens_details=None prompt_token_count=254 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=254
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=489 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_8.txt`

**Score:** 52.38%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,9),(3,9),(3,8),(3,7),(3,6),(3,5),(4,5),(5,5),(5,4),(5,3),(5,2),(5,1),(6,1),(7,1),(7,2),(7,3),(8,3),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Kd4dacyDEbHi7M8Pme_B-AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=179,
  prompt_token_count=2163,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2163
    ),
  ],
  total_token_count=2342
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=179 candidates_tokens_details=None prompt_token_count=2163 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2163
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2342 traffic_type=None
```

