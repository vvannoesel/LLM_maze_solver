# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_1.jpg` | **11.76%** | `input: 435 , ouput: 41` | `(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4)` |
| `maze_line_6x6_1.json` | **11.76%** | `input: 1810 , ouput: 45` | `(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_1.json` | **52.94%** | `input: 2259 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_adj_1.txt` | **52.94%** | `input: 730 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_tokenized_1.txt` | **35.29%** | `input: 674 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_1.jpg` | **0.00%** | `input: 432 , ouput: 152` | `(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (10, 4), (11, 4), (12, 4), (12, 5), (12, 6), (11, 6), (10, 6), (10, 7), (10, 8), (11, 8), (11, 9), (11, 10), (12, 10), (12, 11), (12, 12)` |
| `maze_occupancy_6x6_1.json` | **3.03%** | `input: 989 , ouput: 99` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_1.json` | **100.00%** | `input: 4350 , ouput: 150` | `(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_adj_1.txt` | **51.52%** | `input: 1280 , ouput: 87` | `(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_ascii_1.txt` | **0.00%** | `input: 253 , ouput: 119` | `(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)` |
| `maze_occupancy_6x6_tokenized_1.txt` | **3.03%** | `input: 2163 , ouput: 269` | `(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_1.jpg`

**Score:** 11.76%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(2,2),(3,2),(3,3),(3,4),(4,4),(5,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='l90dadiuG-HMkdUPlY_CwAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
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
  total_token_count=476
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=435 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=177
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=476 traffic_type=None
```

### `maze_line_6x6_1.json`

**Score:** 11.76%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mN0dabn2DKrPnsEPw4G2yAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_1.json`

**Score:** 52.94%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='md0daaGWFc3MnsEP2patsQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_1.txt`

**Score:** 52.94%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mt0daaHHFJGbkdUP04fEyAY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_1.txt`

**Score:** 35.29%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(4,1),(4,2),(5,2),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='mt0dabmBO_KkkdUPyJazuQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_1.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (10, 4), (11, 4), (12, 4), (12, 5), (12, 6), (11, 6), (10, 6), (10, 7), (10, 8), (11, 8), (11, 9), (11, 10), (12, 10), (12, 11), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(2,2),(3,2),(4,2),(4,1),(4,0),(5,0),(6,0),(7,0),(7,1),(7,2),(8,2),(9,2),(9,3),(9,4),(10,4),(11,4),(12,4),(12,5),(12,6),(11,6),(10,6),(10,7),(10,8),(11,8),(11,9),(11,10),(12,10),(12,11),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nd0daar-I9afkdUPhY38wAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=152,
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
  total_token_count=584
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=152 candidates_tokens_details=None prompt_token_count=432 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=174
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=584 traffic_type=None
```

### `maze_occupancy_6x6_1.json`

**Score:** 3.03%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n90daduTF_O8kdUPjqqWwAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=99,
  prompt_token_count=989,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=989
    ),
  ],
  total_token_count=1088
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=99 candidates_tokens_details=None prompt_token_count=989 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=989
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1088 traffic_type=None
```

### `maze_occupancy_6x6_adj_1.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(8,3),(9,3),(10,3),(11,3),(11,4),(11,5),(11,6),(11,7),(10,7),(9,7),(9,8),(9,9),(8,9),(7,9),(6,9),(5,9),(5,10),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oN0daaPGJvqAkdUPsrDQ2QY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=150,
  prompt_token_count=4350,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4350
    ),
  ],
  total_token_count=4500
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=150 candidates_tokens_details=None prompt_token_count=4350 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4350
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4500 traffic_type=None
```

### `maze_occupancy_6x6_adj_1.txt`

**Score:** 51.52%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(7,3),(8,3),(9,3),(10,3),(11,3),(11,4),(11,5),(11,6),(11,7),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='od0dabrEK-_rkdUPvuTBgQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=87,
  prompt_token_count=1280,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1280
    ),
  ],
  total_token_count=1367
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=87 candidates_tokens_details=None prompt_token_count=1280 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1280
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1367 traffic_type=None
```

### `maze_occupancy_6x6_ascii_1.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(5,3),(5,4),(5,5),(6,5),(7,5),(7,6),(7,7),(7,8),(7,9),(8,9),(9,9),(9,8),(9,7),(10,7),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='o90dafGhB-GtkdUPi-rdyQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=119,
  prompt_token_count=253,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=253
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=119 candidates_tokens_details=None prompt_token_count=253 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=253
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=372 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_1.txt`

**Score:** 3.03%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(3,10),(3,9),(3,8),(3,7),(4,7),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(5,1),(6,1),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(7,10),(7,11),(8,11),(9,11),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(9,1),(10,1),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pN0daY2GIrO9kdUPou6g8QI' usage_metadata=GenerateContentResponseUsageMetadata(
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

