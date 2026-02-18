# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_32.jpg` | **3.23%** | `input: 442 , ouput: 61` | `(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 0), (4, 0), (4, 1), (5, 1), (5, 2), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)` |
| `maze_line_6x6_32.json` | **3.23%** | `input: 1817 , ouput: 45` | `(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_32.json` | **45.16%** | `input: 2266 , ouput: 61` | `(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)` |
| `maze_line_6x6_adj_32.txt` | **12.90%** | `input: 737 , ouput: 133` | `(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (4, 5), (3, 5), (2, 5), (2, 4), (1, 4), (1, 5), (0, 5), (0, 4), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)` |
| `maze_line_6x6_tokenized_32.txt` | **0.00%** | `input: 681 , ouput: 49` | `(0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)` |
| `maze_occupancy_6x6_32.jpg` | **0.00%** | `input: 439 , ouput: 191` | `(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (4, 11), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)` |
| `maze_occupancy_6x6_32.json` | **14.75%** | `input: 996 , ouput: 162` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (8, 4), (9, 4), (9, 3), (9, 2), (10, 2), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_32.json` | **93.44%** | `input: 4350 , ouput: 281` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (11, 8), (11, 9), (11, 10), (11, 11)` |
| `maze_occupancy_6x6_adj_32.txt` | **27.87%** | `input: 1286 , ouput: 115` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)` |
| `maze_occupancy_6x6_ascii_32.txt` | **0.00%** | `input: 255 , ouput: 158` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)` |
| `maze_occupancy_6x6_tokenized_32.txt` | **14.75%** | `input: 2170 , ouput: 144` | `(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)` |

---

## Full LLM Responses

### `maze_line_6x6_32.jpg`

**Score:** 3.23%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (4, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 0), (4, 0), (4, 1), (5, 1), (5, 2), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(3,1),(3,0),(4,0),(4,1),(5,1),(5,2),(4,2),(4,3),(5,3),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K32VaaK6HKPwnsEPgLOouAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_32.json`

**Score:** 3.23%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (4, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LH2VaYqwDpHw7M8Pi4iBgAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_32.json`

**Score:** 45.16%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (4, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,2),(1,3),(0,3),(0,4),(0,5),(1,5),(1,4),(2,4),(2,5),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LX2VaZhF-uGewQ_2hM_ZCQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=2266,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2266
    ),
  ],
  total_token_count=2327
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=2266 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2266
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2327 traffic_type=None
```

### `maze_line_6x6_adj_32.txt`

**Score:** 12.90%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (4, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (4, 5), (3, 5), (2, 5), (2, 4), (1, 4), (1, 5), (0, 5), (0, 4), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,2),(2,2),(2,1),(2,0),(3,0),(4,0),(5,0),(5,1),(4,1),(3,1),(3,2),(3,3),(3,4),(4,4),(4,5),(3,5),(2,5),(2,4),(1,4),(1,5),(0,5),(0,4),(0,3),(1,3),(2,3),(3,3),(3,4),(4,4),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LX2VacvZOZjknsEPxt7C0AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=133,
  prompt_token_count=737,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=737
    ),
  ],
  total_token_count=870
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=133 candidates_tokens_details=None prompt_token_count=737 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=737
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=870 traffic_type=None
```

### `maze_line_6x6_tokenized_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5), (4, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(2,2),(2,1),(3,1),(3,2),(4,2),(4,3),(4,4),(5,4),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ln2VafWaLsPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=681,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=681
    ),
  ],
  total_token_count=730
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=681 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=681
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=730 traffic_type=None
```

### `maze_occupancy_6x6_32.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (4, 11), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(4,2),(5,2),(5,1),(5,0),(6,0),(7,0),(7,1),(7,2),(7,3),(7,4),(6,4),(5,4),(4,4),(4,5),(4,6),(3,6),(2,6),(1,6),(0,6),(0,7),(0,8),(0,9),(0,10),(1,10),(2,10),(3,10),(4,10),(4,11),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12),(12,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MH2Vae35EbzhnsEPwLCgiQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=191,
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
  total_token_count=630
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=191 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=181
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=630 traffic_type=None
```

### `maze_occupancy_6x6_32.json`

**Score:** 14.75%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (8, 4), (9, 4), (9, 3), (9, 2), (10, 2), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(4,7),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(5,1),(6,1),(7,1),(7,2),(7,3),(7,4),(8,4),(9,4),(9,3),(9,2),(10,2),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MX2VabmpG6eN7M8P6NXVwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=162,
  prompt_token_count=996,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=996
    ),
  ],
  total_token_count=1158
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=162 candidates_tokens_details=None prompt_token_count=996 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=996
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1158 traffic_type=None
```

### `maze_occupancy_6x6_adj_32.json`

**Score:** 93.44%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (10, 7), (9, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(2,7),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(3,10),(3,9),(4,9),(5,9),(5,10),(5,11),(6,11),(7,11),(8,11),(9,11),(9,10),(9,9),(8,9),(7,9),(7,8),(7,7),(7,6),(7,5),(6,5),(5,5),(5,4),(5,3),(5,2),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(11,2),(11,3),(10,3),(9,3),(9,4),(9,5),(10,5),(11,5),(11,6),(11,7),(10,7),(9,7),(11,8),(11,9),(11,10),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Mn2VaYLUMNqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=281,
  prompt_token_count=4350,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4350
    ),
  ],
  total_token_count=4631
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=281 candidates_tokens_details=None prompt_token_count=4350 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4350
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4631 traffic_type=None
```

### `maze_occupancy_6x6_adj_32.txt`

**Score:** 27.87%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(2,7),(1,7),(1,8),(1,9),(1,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='M32VaYHVGsyynsEP0d_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=115,
  prompt_token_count=1286,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1286
    ),
  ],
  total_token_count=1401
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=115 candidates_tokens_details=None prompt_token_count=1286 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1286
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1401 traffic_type=None
```

### `maze_occupancy_6x6_ascii_32.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(4,6),(5,6),(5,5),(5,4),(5,3),(5,2),(5,1),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NH2VabujG8PwnsEPpffzuQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=158,
  prompt_token_count=255,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=255
    ),
  ],
  total_token_count=413
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=158 candidates_tokens_details=None prompt_token_count=255 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=255
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=413 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_32.txt`

**Score:** 14.75%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 10), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (9, 10), (9, 9), (8, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (11, 2), (11, 3), (10, 3), (9, 3), (9, 4), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11)
```

**Extracted Answer:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 9), (5, 9), (5, 10), (5, 11), (6, 11), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (9, 4), (9, 5), (9, 7), (9, 9), (9, 10), (9, 11), (10, 11), (11, 11)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(3,5),(3,6),(3,7),(4,9),(5,9),(5,10),(5,11),(6,11),(7,11),(7,10),(7,9),(7,8),(7,7),(7,6),(7,5),(7,4),(7,3),(8,3),(9,3),(9,4),(9,5),(9,7),(9,9),(9,10),(9,11),(10,11),(11,11)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='NX2Vaa7QDdHMkdUPjY-7sAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=144,
  prompt_token_count=2170,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2170
    ),
  ],
  total_token_count=2314
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=144 candidates_tokens_details=None prompt_token_count=2170 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2170
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2314 traffic_type=None
```

