# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_12.jpg` | **7.14%** | `input: 434 , ouput: 19` | `down, right, right, down, right, down, right, down, down, right` |
| `maze_line_6x6_12.json` | **21.43%** | `input: 1809 , ouput: 21` | `down, down, right, down, right, right, down, right, down, right, right` |
| `maze_line_6x6_adj_12.json` | **35.71%** | `input: 2258 , ouput: 23` | `down, down, right, right, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_12.txt` | **0.00%** | `input: 729 , ouput: 27` | `right, right, right, down, right, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_tokenized_12.txt` | **28.57%** | `input: 673 , ouput: 650` | `down, down, right, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down` |
| `maze_occupancy_6x6_12.jpg` | **3.57%** | `input: 431 , ouput: 650` | `down, right, right, down, down, right, right, up, right, down, down, down, left, down, right, right, right, up, right, down, down, down, left, left, left, up, left, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up` |
| `maze_occupancy_6x6_12.json` | **7.14%** | `input: 988 , ouput: 650` | `down, down, right, right, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down` |
| `maze_occupancy_6x6_adj_12.json` | **7.14%** | `input: 4342 , ouput: 650` | `down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right` |
| `maze_occupancy_6x6_adj_12.txt` | **14.29%** | `input: 1274 , ouput: 239` | `down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right` |
| `maze_occupancy_6x6_ascii_12.txt` | **7.14%** | `input: 249 , ouput: 650` | `down, down, right, right, right, down, right, right, down, left, down, right, right, right, right, down, right, right, right, right, up, up, right, down, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left` |
| `maze_occupancy_6x6_tokenized_12.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, down, right, right, down, down, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_6x6_12.jpg`

**Score:** 7.14%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, down, right, down, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,right,down,right,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hIGVadqKCryK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
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
  total_token_count=453
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=453 traffic_type=None
```

### `maze_line_6x6_12.json`

**Score:** 21.43%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, down, right, right, down, right, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, right, down, right, down, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hIGVaajFMZHw7M8Pi4iBgAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=21,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1830
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=21 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1830 traffic_type=None
```

### `maze_line_6x6_adj_12.json`

**Score:** 35.71%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, right, right, right, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hYGVaYaMJffo7M8PipSSoQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, down, right, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,down,down,down,down,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hoGVaefpCOyOkdUP_ZOcgQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=756
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=756 traffic_type=None
```

### `maze_line_6x6_tokenized_12.txt`

**Score:** 28.57%

**Ground Truth Solution:**
```
down, down, right, right, down, down, left, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1869,
        license='',
        start_index=143,
        uri='https://github.com/aszecsei/ArtificialIntelligenceSpr19'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down, down, left, left, up, up, right, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='h4GVadTxIq2WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=1323
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1323 traffic_type=None
```

### `maze_occupancy_6x6_12.jpg`

**Score:** 3.57%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, right, down, down, right, right, up, right, down, down, down, left, down, right, right, right, up, right, down, down, down, left, left, left, up, left, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up, right, right, up, up, right, right, down, right, down, down, down, right, right, right, up, right, up, right, down, right, right, right, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,right,down,down,right,right,up,right,down,down,down,left,down,right,right,right,up,right,down,down,down,left,left,left,up,left,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,right,right,up,up,right,right,down,right,down,down,down,right,right,right,up,right,up,right,down,right,right,right,up,up,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ioGVaeLhGtiCkdUPj_-PiQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_12.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,down,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jIGVafzlNN_x7M8P1Ouu-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_12.json`

**Score:** 7.14%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='j4GVaeWlBe3_nsEPyaqlqAk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4342,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4342
    ),
  ],
  total_token_count=4992
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4342 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4342
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4992 traffic_type=None
```

### `maze_occupancy_6x6_adj_12.txt`

**Score:** 14.29%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='kIGVaYKGG4KG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=239,
  prompt_token_count=1274,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1274
    ),
  ],
  total_token_count=1513
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=239 candidates_tokens_details=None prompt_token_count=1274 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1274
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1513 traffic_type=None
```

### `maze_occupancy_6x6_ascii_12.txt`

**Score:** 7.14%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, right, down, right, right, down, left, down, right, right, right, right, down, right, right, right, right, up, up, right, down, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left, left, left, down, right, right, right, right, down, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,right,right,down,left,down,right,right,right,right,down,right,right,right,right,up,up,right,down,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,left,left,down,right,right,right,right,down,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='koGVaYbuHsPwnsEPpffzuQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=249,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=249
    ),
  ],
  total_token_count=899
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=249 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=249
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=899 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, right, down, down, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,down,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='k4GVafnIPOjpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
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

