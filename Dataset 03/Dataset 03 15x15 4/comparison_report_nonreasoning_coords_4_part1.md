# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_4.jpg` | **1.75%** | `input: 444 , ouput: 164` | `(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (9, 7), (10, 7), (10, 8), (10, 9), (11, 9), (12, 9), (12, 8), (13, 8), (13, 7), (13, 6), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14)` |
| `maze_line_15x15_4.json` | **1.75%** | `input: 9815 , ouput: 213` | `(0, 0), (1, 1), (2, 0), (3, 1), (4, 1), (4, 0), (5, 0), (6, 0), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 0), (13, 1), (14, 2), (14, 3), (13, 4), (12, 4), (11, 4), (10, 4), (9, 4), (8, 5), (7, 5), (6, 6), (5, 7), (4, 8), (3, 9), (2, 10), (1, 11), (0, 12), (1, 13), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14), (14, 14)` |
| `maze_line_15x15_adj_4.json` | **40.35%** | `input: 13497 , ouput: 202` | `(0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5), (7, 5), (7, 6), (8, 6), (8, 7), (9, 7), (9, 6), (10, 6), (10, 5), (11, 5), (11, 6), (11, 7), (12, 7), (12, 8), (12, 9), (13, 9), (13, 10), (12, 10), (11, 10), (11, 11), (12, 11), (13, 11), (14, 11), (14, 12), (14, 13), (14, 14)` |

---

## Full LLM Responses

### `maze_line_15x15_4.jpg`

**Score:** 1.75%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5), (7, 5), (7, 6), (8, 6), (8, 7), (9, 7), (10, 7), (10, 8), (11, 8), (11, 9), (10, 9), (10, 10), (9, 10), (9, 9), (9, 8), (8, 8), (7, 8), (7, 7), (6, 7), (6, 8), (6, 9), (6, 10), (7, 10), (8, 10), (8, 11), (7, 11), (7, 12), (8, 12), (9, 12), (10, 12), (10, 13), (10, 14), (11, 14), (11, 13), (12, 13), (12, 14), (13, 14), (13, 13), (14, 13), (14, 14)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (9, 7), (10, 7), (10, 8), (10, 9), (11, 9), (12, 9), (12, 8), (13, 8), (13, 7), (13, 6), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(6,3),(7,3),(7,4),(7,5),(8,5),(8,6),(8,7),(9,7),(10,7),(10,8),(10,9),(11,9),(12,9),(12,8),(13,8),(13,7),(13,6),(14,6),(14,7),(14,8),(14,9),(14,10),(14,11),(14,12),(14,13),(14,14)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8fglaf3FJOu_vdIP9tzPYA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=164,
  prompt_token_count=444,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=186
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=608
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=444 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=164 candidates_tokens_details=None prompt_token_count=444 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=186
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=608 traffic_type=None
```

### `maze_line_15x15_4.json`

**Score:** 1.75%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5), (7, 5), (7, 6), (8, 6), (8, 7), (9, 7), (10, 7), (10, 8), (11, 8), (11, 9), (10, 9), (10, 10), (9, 10), (9, 9), (9, 8), (8, 8), (7, 8), (7, 7), (6, 7), (6, 8), (6, 9), (6, 10), (7, 10), (8, 10), (8, 11), (7, 11), (7, 12), (8, 12), (9, 12), (10, 12), (10, 13), (10, 14), (11, 14), (11, 13), (12, 13), (12, 14), (13, 14), (13, 13), (14, 13), (14, 14)
```

**Extracted Answer:**
```
(0, 0), (1, 1), (2, 0), (3, 1), (4, 1), (4, 0), (5, 0), (6, 0), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 0), (13, 1), (14, 2), (14, 3), (13, 4), (12, 4), (11, 4), (10, 4), (9, 4), (8, 5), (7, 5), (6, 6), (5, 7), (4, 8), (3, 9), (2, 10), (1, 11), (0, 12), (1, 13), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14), (14, 14)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,1),(2,0),(3,1),(4,1),(4,0),(5,0),(6,0),(7,1),(8,1),(9,1),(10,1),(11,1),(12,0),(13,1),(14,2),(14,3),(13,4),(12,4),(11,4),(10,4),(9,4),(8,5),(7,5),(6,6),(5,7),(4,8),(3,9),(2,10),(1,11),(0,12),(1,13),(2,14),(3,14),(4,14),(5,14),(6,14),(7,14),(8,14),(9,14),(10,14),(11,14),(12,14),(13,14),(14,14)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8_glaYWuBqXsxs0PoOuFmAE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=213,
  prompt_token_count=9815,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9815
    ),
  ],
  total_token_count=10028
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=213 candidates_tokens_details=None prompt_token_count=9815 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9815
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=10028 traffic_type=None
```

### `maze_line_15x15_adj_4.json`

**Score:** 40.35%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5), (7, 5), (7, 6), (8, 6), (8, 7), (9, 7), (10, 7), (10, 8), (11, 8), (11, 9), (10, 9), (10, 10), (9, 10), (9, 9), (9, 8), (8, 8), (7, 8), (7, 7), (6, 7), (6, 8), (6, 9), (6, 10), (7, 10), (8, 10), (8, 11), (7, 11), (7, 12), (8, 12), (9, 12), (10, 12), (10, 13), (10, 14), (11, 14), (11, 13), (12, 13), (12, 14), (13, 14), (13, 13), (14, 13), (14, 14)
```

**Extracted Answer:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5), (7, 5), (7, 6), (8, 6), (8, 7), (9, 7), (9, 6), (10, 6), (10, 5), (11, 5), (11, 6), (11, 7), (12, 7), (12, 8), (12, 9), (13, 9), (13, 10), (12, 10), (11, 10), (11, 11), (12, 11), (13, 11), (14, 11), (14, 12), (14, 13), (14, 14)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(0,1),(1,1),(1,2),(0,2),(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(4,2),(5,2),(6,2),(6,3),(6,4),(6,5),(7,5),(7,6),(8,6),(8,7),(9,7),(9,6),(10,6),(10,5),(11,5),(11,6),(11,7),(12,7),(12,8),(12,9),(13,9),(13,10),(12,10),(11,10),(11,11),(12,11),(13,11),(14,11),(14,12),(14,13),(14,14)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9PglaYrgMPqvxN8PvLjv8QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=202,
  prompt_token_count=13497,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13497
    ),
  ],
  total_token_count=13699
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=202 candidates_tokens_details=None prompt_token_count=13497 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13497
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13699 traffic_type=None
```

