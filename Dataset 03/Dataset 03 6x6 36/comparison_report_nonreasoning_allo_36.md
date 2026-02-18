# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_36.jpg` | **6.67%** | `input: 434 , ouput: 21` | `down, right, down, right, down, right, down, right, up, right, down` |
| `maze_line_6x6_36.json` | **6.67%** | `input: 1809 , ouput: 27` | `down, right, right, down, down, right, right, right, down, down, right, down, right, right` |
| `maze_line_6x6_adj_36.json` | **3.33%** | `input: 2258 , ouput: 23` | `down, down, right, right, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_36.txt` | **0.00%** | `input: 729 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_tokenized_36.txt` | **0.00%** | `input: 673 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_occupancy_6x6_36.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, down, right, up, right, down, down, right, down, left, down, right, down, right, up, right, up, left, up, left, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right` |
| `maze_occupancy_6x6_36.json` | **3.33%** | `input: 988 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down` |
| `maze_occupancy_6x6_adj_36.json` | **6.67%** | `input: 4335 , ouput: 650` | `down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right` |
| `maze_occupancy_6x6_adj_36.txt` | **3.33%** | `input: 1273 , ouput: 61` | `down, down, down, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_ascii_36.txt` | **1.67%** | `input: 243 , ouput: 650` | `down, right, down, right, right, down, right, down, right, right, right, down, down, left, down, left, down, right, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right` |
| `maze_occupancy_6x6_tokenized_36.txt` | **1.67%** | `input: 2162 , ouput: 650` | `down, right, right, down, down, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, up, up, up, right, up, up, up, up, up, up, right, right, up, up, up, up, up, up, up, up, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up` |

---

## Full LLM Responses

### `maze_line_6x6_36.jpg`

**Score:** 6.67%

**Ground Truth Solution:**
```
down, right, up, right, down, right, up, right, right, down, down, down, left, left, left, up, left, left, down, right, down, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, up, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,up,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YYSVaf6rKYyD7M8PobrS-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=434,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=176
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
) total_tokens=434 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=455 traffic_type=None
```

### `maze_line_6x6_36.json`

**Score:** 6.67%

**Ground Truth Solution:**
```
down, right, up, right, down, right, up, right, right, down, down, down, left, left, left, up, left, left, down, right, down, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, right, down, down, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, right, right, down, down, right, right, right, down, down, right, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YoSVabDhFoOunsEPisjO2Qc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1836
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=192 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1836 traffic_type=None
```

### `maze_line_6x6_adj_36.json`

**Score:** 3.33%

**Ground Truth Solution:**
```
down, right, up, right, down, right, up, right, right, down, down, down, left, left, left, up, left, left, down, right, down, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
down, down, right, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Y4SVaZzLCMPPnsEPpfqayAc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2281
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=163 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2281 traffic_type=None
```

### `maze_line_6x6_adj_36.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, right, up, right, right, down, down, down, left, left, left, up, left, left, down, right, down, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, down, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Y4SVaZmyMajlnsEP1bugwAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=748
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=196 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=748 traffic_type=None
```

### `maze_line_6x6_tokenized_36.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, up, right, down, right, up, right, right, down, down, down, left, left, left, up, left, left, down, right, down, left, down, right, right, right, right, up, right, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZISVadfuG4DHnsEPq_XX6Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=692
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=194 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=692 traffic_type=None
```

### `maze_occupancy_6x6_36.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, up, right, down, down, right, down, left, down, right, down, right, up, right, up, left, up, left, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, up, right, down, right, down, left, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, left, up, left, down, left, down, left, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,up,right,down,down,right,down,left,down,right,down,right,up,right,up,left,up,left,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,up,right,down,right,down,left,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,left,up,left,down,left,down,left,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Z4SVafWGLITw7M8P482J-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=431,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=173
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=1081
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=431 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1081 traffic_type=None
```

### `maze_occupancy_6x6_36.json`

**Score:** 3.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aoSVaZXGAvjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1638
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1638 traffic_type=None
```

### `maze_occupancy_6x6_adj_36.json`

**Score:** 6.67%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bISVab2RF9HMkdUPy8C6kAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4335,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4335
    ),
  ],
  total_token_count=4985
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=165 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4335 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4335
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4985 traffic_type=None
```

### `maze_occupancy_6x6_adj_36.txt`

**Score:** 3.33%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, down, down, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,down,down,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bYSVaefrCvrhnsEP9oTP2Qk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=1273,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1273
    ),
  ],
  total_token_count=1334
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=1273 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1273
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1334 traffic_type=None
```

### `maze_occupancy_6x6_ascii_36.txt`

**Score:** 1.67%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, right, down, right, right, down, right, down, right, right, right, down, down, left, down, left, down, right, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, up, right, up, right, up, up, left, up, up, left, left, down, left, down, down, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,right,down,right,down,right,right,right,down,down,left,down,left,down,right,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,up,right,up,right,up,up,left,up,up,left,left,down,left,down,down,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='b4SVafObGNnn7M8P8fieuAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=243,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=243
    ),
  ],
  total_token_count=893
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=243 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=243
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=893 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_36.txt`

**Score:** 1.67%

**Ground Truth Solution:**
```
down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, left, left, left, left, left, left, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, right, right, down, down, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, up, up, up, right, up, up, up, up, up, up, right, right, up, up, up, up, up, up, up, up, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,up,up,up,right,up,up,up,up,up,up,right,right,up,up,up,up,up,up,up,up,up,up,right,right,up,up,up,up,up,up,up,up,up,up,up,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cISVafusOqeN7M8P6NXVwQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2812
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2812 traffic_type=None
```

