# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_29.jpg` | **8.33%** | `input: 434 , ouput: 33` | `right, down, right, down, right, down, right, down, left, down, right, right, up, right, down, down, right` |
| `maze_line_6x6_29.json` | **0.00%** | `input: 1809 , ouput: 31` | `down, down, right, right, down, down, right, right, up, right, down, down, right, down, right, right` |
| `maze_line_6x6_adj_29.json` | **8.33%** | `input: 2258 , ouput: 21` | `right, down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_29.txt` | **4.17%** | `input: 729 , ouput: 21` | `right, right, down, right, down, down, right, right, down, down, right` |
| `maze_line_6x6_tokenized_29.txt` | **8.33%** | `input: 673 , ouput: 103` | `right, down, right, down, right, down, left, down, right, right, down, left, left, down, right, right, up, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down` |
| `maze_occupancy_6x6_29.jpg` | **2.08%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right` |
| `maze_occupancy_6x6_29.json` | **2.08%** | `input: 988 , ouput: 650` | `right, down, down, down, right, right, down, down, down, right, right, right, right, down, left, left, down, right, right, down, right, right, right, down, right, down, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right` |
| `maze_occupancy_6x6_adj_29.json` | **nan%** | `input: 4337 , ouput: 0` | `` |
| `maze_occupancy_6x6_adj_29.txt` | **8.33%** | `input: 1275 , ouput: 650` | `right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right` |
| `maze_occupancy_6x6_ascii_29.txt` | **8.33%** | `input: 249 , ouput: 71` | `right, right, down, down, right, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_29.txt` | **8.33%** | `input: 2162 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_29.jpg`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, down, right, right, up, left, up, up, left, up, right, right, down, down, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, left, down, right, right, up, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,left,down,right,right,up,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6oKVad2rFaS1xN8P7ILa-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
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
  total_token_count=467
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=467 traffic_type=None
```

### `maze_line_6x6_29.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, down, right, right, up, left, up, up, left, up, right, right, down, down, right, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, up, right, down, down, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, down, right, right, up, right, down, down, right, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='64KVaYSbAYuX28oPlq_ciQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1840
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1840 traffic_type=None
```

### `maze_line_6x6_adj_29.json`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, down, right, right, up, left, up, up, left, up, right, right, down, down, right, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='64KVacWuMPHXvdIP-aPZgQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2279
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2279 traffic_type=None
```

### `maze_line_6x6_adj_29.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, down, right, right, up, left, up, up, left, up, right, right, down, down, right, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, right, down, down, right, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7IKVadS_IdfIvdIPlo3gqAY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=750
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=750 traffic_type=None
```

### `maze_line_6x6_tokenized_29.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, down, right, right, up, left, up, up, left, up, right, right, down, down, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, down, left, left, down, right, right, up, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,down,left,left,down,right,right,up,right,down,down,left,left,up,up,right,right,down,down,left,left,up,up,right,right,down,down,left,left,up,up,right,right,down,down,left,left,up,up,right,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7YKVaaLQFJuZ28oPh4-usAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=103,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=776
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=103 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=776 traffic_type=None
```

### `maze_occupancy_6x6_29.jpg`

**Score:** 2.08%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right, down, right, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,down,right,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8IKVafftG6S9xN8PvoPm4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_29.json`

**Score:** 2.08%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, down, down, right, right, right, right, down, left, left, down, right, right, down, right, right, right, down, right, down, right, right, right, down, down, down, down, down, right, right, right, right, right, right, down, right, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,down,down,down,right,right,right,right,down,left,left,down,right,right,down,right,right,right,down,right,down,right,right,right,down,down,down,down,down,right,right,right,right,right,right,down,right,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='8oKVacOxIsPgvdIP96mU8Qw' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_29.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='9YKVaaSeJdrzxs0PvK7U4Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=4337,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4337
    ),
  ],
  total_token_count=4337
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=4337 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4337
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4337 traffic_type=None
```

### `maze_occupancy_6x6_adj_29.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='94KVaZngAeLSvdIP0O3TwQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1275,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1275
    ),
  ],
  total_token_count=1925
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1275 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1275
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1925 traffic_type=None
```

### `maze_occupancy_6x6_ascii_29.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, down, down, right, right, right, right, down, down, left, left, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,down,down,right,right,right,right,down,down,left,left,left,left,left,left,left,left,down,down,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-IKVae_nAsTdvdIPxenY-Ak' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=71,
  prompt_token_count=249,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=249
    ),
  ],
  total_token_count=320
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=71 candidates_tokens_details=None prompt_token_count=249 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=249
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=320 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_29.txt`

**Score:** 8.33%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, up, up, left, left, up, up, up, up, left, left, up, up, right, right, right, right, down, down, down, down, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='-oKVaYrfHPyc28oP7rOrsAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

