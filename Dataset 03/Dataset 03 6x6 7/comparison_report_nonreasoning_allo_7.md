# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_7.jpg` | **0.00%** | `input: 427 , ouput: 45` | `the, start, is, at, (0, 0), and, the, end, is, at, (5, 5)., down, down, right, down, right, down, right, down, right, up, right, down, right` |
| `maze_line_6x6_7.json` | **12.50%** | `input: 1802 , ouput: 21` | `down, down, right, right, down, right, down, right, right, down, right` |
| `maze_line_6x6_adj_7.json` | **8.33%** | `input: 2251 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_7.txt` | **0.00%** | `input: 722 , ouput: 27` | `right, down, down, down, right, right, down, down, right, right, down, down, right, right` |
| `maze_line_6x6_tokenized_7.txt` | **0.00%** | `input: 666 , ouput: 27` | `right, down, right, right, right, down, down, right, down, down, left, down, right, right` |
| `maze_occupancy_6x6_7.jpg` | **4.17%** | `input: 424 , ouput: 41` | `down, down, right, right, down, right, down, down, right, right, right, down, down, right, up, right, down, down, right, right, down` |
| `maze_occupancy_6x6_7.json` | **0.00%** | `input: 981 , ouput: 650` | `right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_adj_7.json` | **8.33%** | `input: 4338 , ouput: 650` | `down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_7.txt` | **8.33%** | `input: 1269 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_ascii_7.txt` | **2.08%** | `input: 247 , ouput: 137` | `down, right, right, right, right, down, down, right, down, down, left, down, down, right, right, right, right, right, up, right, right, up, up, left, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right` |
| `maze_occupancy_6x6_tokenized_7.txt` | **0.00%** | `input: 2155 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_7.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, down, left, down, down, left, up, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
the, start, is, at, (0, 0), and, the, end, is, at, (5, 5)., down, down, right, down, right, down, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The start is at (0,0) and the end is at (5,5).

Down, Down, Right, Down, Right, Down, Right, Down, Right, Up, Right, Down, Right"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='r98dacK8G-2CvdIP7eiBkAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=45,
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
  total_token_count=472
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=45 candidates_tokens_details=None prompt_token_count=427 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=169
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=472 traffic_type=None
```

### `maze_line_6x6_7.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, down, left, down, down, left, up, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, right, down, right, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sN8daf6lH-3Zxs0PsZuluAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1802,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1802
    ),
  ],
  total_token_count=1823
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1802 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1802
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1823 traffic_type=None
```

### `maze_line_6x6_adj_7.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, down, left, down, down, left, up, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sd8daZyqDP2cxN8PyYLUsAE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=2251,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2251
    ),
  ],
  total_token_count=2270
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=2251 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2251
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2270 traffic_type=None
```

### `maze_line_6x6_adj_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, down, left, down, down, left, up, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, down, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,down,down,right,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='sd8daYTSOO61vdIP3vbMwQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=722,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=722
    ),
  ],
  total_token_count=749
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=722 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=722
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=749 traffic_type=None
```

### `maze_line_6x6_tokenized_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, up, up, right, right, down, down, left, down, down, left, up, left, down, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, right, right, down, down, right, down, down, left, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,down,down,right,down,down,left,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='st8daa-_NoGOvdIP28nzuQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=666,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=666
    ),
  ],
  total_token_count=693
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=666 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=666
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=693 traffic_type=None
```

### `maze_occupancy_6x6_7.jpg`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, down, right, right, right, down, down, right, up, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,right,down,down,right,right,right,down,down,right,up,right,down,down,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tN8dab-mGP-ivdIPxr60wAk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_7.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='t98daYqmGITVxs0P2sbnuAg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_7.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, up, up, up, up, up, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,up,up,up,up,up,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ut8dabGuIY-7vdIP1aSIwAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4338,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4338
    ),
  ],
  total_token_count=4988
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4338 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4338
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4988 traffic_type=None
```

### `maze_occupancy_6x6_adj_7.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vd8dae-lN-3Zxs0PsZuluAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1269,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1269
    ),
  ],
  total_token_count=1919
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1269 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1269
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1919 traffic_type=None
```

### `maze_occupancy_6x6_ascii_7.txt`

**Score:** 2.08%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, right, right, down, down, right, down, down, left, down, down, right, right, right, right, right, up, right, right, up, up, left, up, up, up, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,right,right,down,down,right,down,down,left,down,down,right,right,right,right,right,up,right,right,up,up,left,up,up,up,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='v98daZf3CI7WvdIP2uCBoAw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=137,
  prompt_token_count=247,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=247
    ),
  ],
  total_token_count=384
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=137 candidates_tokens_details=None prompt_token_count=247 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=247
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=384 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_7.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wd8daeqKF6q-vdIPkaK54Ak' usage_metadata=GenerateContentResponseUsageMetadata(
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

