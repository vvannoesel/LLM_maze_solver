# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_6.jpg` | **10.00%** | `input: 427 , ouput: 25` | `right, down, down, right, down, right, down, right, up, right, down, down, right` |
| `maze_line_6x6_6.json` | **0.00%** | `input: 1802 , ouput: 23` | `down, down, right, down, right, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_6.json` | **20.00%** | `input: 2251 , ouput: 21` | `right, down, right, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_adj_6.txt` | **5.00%** | `input: 722 , ouput: 23` | `right, right, right, down, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_tokenized_6.txt` | **5.00%** | `input: 666 , ouput: 59` | `right, right, right, down, down, down, right, up, right, down, down, down, left, down, down, right, right, up, right, up, up, up, right, right, down, down, down, right, right, right` |
| `maze_occupancy_6x6_6.jpg` | **2.50%** | `input: 424 , ouput: 31` | `right, down, right, down, right, down, right, up, right, down, down, right, down, right, down, right` |
| `maze_occupancy_6x6_6.json` | **10.00%** | `input: 981 , ouput: 650` | `right, right, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down` |
| `maze_occupancy_6x6_adj_6.json` | **5.00%** | `input: 4341 , ouput: 650` | `right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right` |
| `maze_occupancy_6x6_adj_6.txt` | **17.50%** | `input: 1271 , ouput: 650` | `right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right` |
| `maze_occupancy_6x6_ascii_6.txt` | **nan%** | `input: 240 , ouput: 0` | `` |
| `maze_occupancy_6x6_tokenized_6.txt` | **0.00%** | `input: 2155 , ouput: 650` | `down, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up` |

---

## Full LLM Responses

### `maze_line_6x6_6.jpg`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, down, left, left, down, down, right, up, right, right, down
```

**Extracted Answer:**
```
right, down, down, right, down, right, down, right, up, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,down,right,down,right,up,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m98dabu-BImHxN8PivzW-Q8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=427,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=169
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=452
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=427 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=452 traffic_type=None
```

### `maze_line_6x6_6.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, down, left, left, down, down, right, up, right, right, down
```

**Extracted Answer:**
```
down, down, right, down, right, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, right, down, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='m98dadP4OpGavdIPxvbZkQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1825
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=185 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1825 traffic_type=None
```

### `maze_line_6x6_adj_6.json`

**Score:** 20.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, down, left, left, down, down, right, up, right, right, down
```

**Extracted Answer:**
```
right, down, right, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nN8dace9JfXzxs0Pn66hoAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2272
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=156 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2272 traffic_type=None
```

### `maze_line_6x6_adj_6.txt`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, down, left, left, down, down, right, up, right, right, down
```

**Extracted Answer:**
```
right, right, right, down, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nd8dadnIFpGavdIPxvbZkQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=745
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=745 traffic_type=None
```

### `maze_line_6x6_tokenized_6.txt`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, down, right, right, up, right, right, down, left, down, down, left, left, down, down, right, up, right, right, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, right, up, right, down, down, down, left, down, down, right, right, up, right, up, up, up, right, right, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,right,up,right,down,down,down,left,down,down,right,right,up,right,up,up,up,right,right,down,down,down,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nt8dac7sGa__xN8P2om7gQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=725
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=725 traffic_type=None
```

### `maze_occupancy_6x6_6.jpg`

**Score:** 2.50%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,up,right,down,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n98dabCJHM3VvdIP5qGjwQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
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
  total_token_count=455
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=424 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=166
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=455 traffic_type=None
```

### `maze_occupancy_6x6_6.json`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='od8daciAGaTyxs0PnYinqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=981,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=981
    ),
  ],
  total_token_count=1631
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=981 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=981
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1631 traffic_type=None
```

### `maze_occupancy_6x6_adj_6.json`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='pN8daZLCIN_UvdIPtoDHyAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4341,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4341
    ),
  ],
  total_token_count=4991
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4341 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4341
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4991 traffic_type=None
```

### `maze_occupancy_6x6_adj_6.txt`

**Score:** 17.50%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='p98daeviMqTyxs0PnYinqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1271,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1271
    ),
  ],
  total_token_count=1921
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1271 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1271
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1921 traffic_type=None
```

### `maze_occupancy_6x6_ascii_6.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```

```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  finish_reason=<FinishReason.RECITATION: 'RECITATION'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='q98dacKNBI_gxN8Pgq_QmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=240,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=240
    ),
  ],
  total_token_count=240
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=240 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=240
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=240 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_6.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, up, up, right, right, right, right, down, down, left, left, down, down, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rt8daYTrDOalvdIPmN-H4QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2155,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2155
    ),
  ],
  total_token_count=2805
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=190 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2155 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2155
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2805 traffic_type=None
```

