# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_3.jpg` | **40.00%** | `input: 429 , ouput: 33` | `(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (1, 1), (0, 1)` |
| `maze_line_3x3_3.json` | **60.00%** | `input: 652 , ouput: 21` | `(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)` |
| `maze_line_3x3_adj_3.json` | **100.00%** | `input: 714 , ouput: 21` | `(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)` |
| `maze_line_3x3_adj_3.txt` | **100.00%** | `input: 346 , ouput: 21` | `(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)` |
| `maze_line_3x3_tokenized_3.txt` | **0.00%** | `input: 317 , ouput: 13` | `(0, 2), (1, 2), (2, 2)` |
| `maze_occupancy_3x3_3.jpg` | **55.56%** | `input: 424 , ouput: 41` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (5, 6)` |
| `maze_occupancy_3x3_3.json` | **100.00%** | `input: 467 , ouput: 37` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)` |
| `maze_occupancy_3x3_adj_3.json` | **100.00%** | `input: 1176 , ouput: 37` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)` |
| `maze_occupancy_3x3_adj_3.txt` | **100.00%** | `input: 458 , ouput: 37` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)` |
| `maze_occupancy_3x3_ascii_3.txt` | **0.00%** | `input: 193 , ouput: 125` | `(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)` |
| `maze_occupancy_3x3_tokenized_3.txt` | **100.00%** | `input: 746 , ouput: 37` | `(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)` |

---

## Full LLM Responses

### `maze_line_3x3_3.jpg`

**Score:** 40.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (1, 1), (0, 1)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='w60VadzEL6e0kdUP55eQCQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=429,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=171
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=462
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=429 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=429 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=171
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=462 traffic_type=None
```

### `maze_line_3x3_3.json`

**Score:** 60.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(2,2)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xK0VadLNC8HknsEP9ebw6Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=652,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=652
    ),
  ],
  total_token_count=673
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=187 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=652 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=652
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=673 traffic_type=None
```

### `maze_line_3x3_adj_3.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(2,2)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xK0VaZDxMqmxkdUPs_HW2A4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=714,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=714
    ),
  ],
  total_token_count=735
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=158 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=714 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=714
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=735 traffic_type=None
```

### `maze_line_3x3_adj_3.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(2,2)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xa0Vaa7VD9X7nsEP4KKHkQ4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=346,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=346
    ),
  ],
  total_token_count=367
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=191 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=346 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=346
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=367 traffic_type=None
```

### `maze_line_3x3_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```
(0, 2), (1, 2), (2, 2)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,2),(1,2),(2,2)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='xa0VadqRK_Lk7M8P67LJCA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=317,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=317
    ),
  ],
  total_token_count=330
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=189 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=317 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=317
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=330 traffic_type=None
```

### `maze_occupancy_3x3_3.jpg`

**Score:** 55.56%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (5, 6)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(5,3),(5,4),(5,5),(5,6)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='x60VaZj5G9X7nsEP4KKHkQ4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=424,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=166
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=465
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=424 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=465 traffic_type=None
```

### `maze_occupancy_3x3_3.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='x60VaeTYNuvgnsEPq7fKyQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=467,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=467
    ),
  ],
  total_token_count=504
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=167 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=467 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=467
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=504 traffic_type=None
```

### `maze_occupancy_3x3_adj_3.json`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yK0VaYb-I6ybkdUP95qhEQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=1176,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1176
    ),
  ],
  total_token_count=1213
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=158 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=1176 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1176
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1213 traffic_type=None
```

### `maze_occupancy_3x3_adj_3.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ya0VaZv9AYjPnsEP5vrAMA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=458,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=458
    ),
  ],
  total_token_count=495
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=191 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=458 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=458
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=495 traffic_type=None
```

### `maze_occupancy_3x3_ascii_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(4,5),(3,5),(2,5),(1,5),(1,4),(2,4),(3,4),(4,4),(4,3),(4,2),(5,2),(5,3),(5,4),(5,5),(5,6)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ya0Vab-vN4XpnsEPqoTzmQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=125,
  prompt_token_count=193,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=193
    ),
  ],
  total_token_count=318
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=125 candidates_tokens_details=None prompt_token_count=193 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=193
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=318 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_3.txt`

**Score:** 100.00%

**Ground Truth Solution:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```
(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(4,5),(5,5)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='yq0VaeKWIrrNkdUP-7bbCA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=746,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=746
    ),
  ],
  total_token_count=783
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=191 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=746 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=746
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=783 traffic_type=None
```

