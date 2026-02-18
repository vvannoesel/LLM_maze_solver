# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_47.jpg` | **5.00%** | `input: 434 , ouput: 19` | `right, down, right, down, down, right, up, right, down, down` |
| `maze_line_6x6_47.json` | **5.00%** | `input: 1809 , ouput: 23` | `right, down, down, right, right, down, down, right, down, right, down, right` |
| `maze_line_6x6_adj_47.json` | **15.00%** | `input: 2258 , ouput: 21` | `right, right, down, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_adj_47.txt` | **15.00%** | `input: 729 , ouput: 25` | `right, right, down, right, right, down, right, down, right, down, right, down, down` |
| `maze_line_6x6_tokenized_47.txt` | **5.00%** | `input: 673 , ouput: 29` | `right, down, down, right, right, down, down, right, right, up, right, down, down, right, down` |
| `maze_occupancy_6x6_47.jpg` | **0.00%** | `input: 431 , ouput: 650` | `down, right, down, right, down, left, down, right, right, down, right, down, right, down, right, up, right, down, left, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down` |
| `maze_occupancy_6x6_47.json` | **0.00%** | `input: 988 , ouput: 650` | `down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down` |
| `maze_occupancy_6x6_adj_47.json` | **12.50%** | `input: 4343 , ouput: 61` | `right, right, right, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_adj_47.txt` | **15.00%** | `input: 1279 , ouput: 650` | `right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right` |
| `maze_occupancy_6x6_ascii_47.txt` | **10.00%** | `input: 255 , ouput: 97` | `right, right, right, right, right, down, down, left, down, down, down, right, right, right, right, right, down, down, left, left, left, left, left, up, left, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_tokenized_47.txt` | **10.00%** | `input: 2162 , ouput: 67` | `right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_47.jpg`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, down, left, down, down, left, down, right, down, right, up, up, up, right, right, down, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, down, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SIWVaZ_UOqnw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_47.json`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, down, left, down, down, left, down, right, down, right, up, up, up, right, right, down, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SYWVaZjOJ6nw7M8Pu5DvyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1832
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1832 traffic_type=None
```

### `maze_line_6x6_adj_47.json`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, right, down, left, down, down, left, down, right, down, right, up, up, up, right, right, down, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SoWVacTQD4TensEP6bbt4Ac' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_47.txt`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, right, down, left, down, down, left, down, right, down, right, up, up, up, right, right, down, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, down, right, down, right, down, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,right,down,right,down,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='S4WVacTnAuKAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=754
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=754 traffic_type=None
```

### `maze_line_6x6_tokenized_47.txt`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, right, down, left, down, down, left, down, right, down, right, up, up, up, right, right, down, right, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, down, down, right, right, up, right, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,down,down,right,right,up,right,down,down,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='S4WVaY_SMfT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=29,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=702
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=29 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=702 traffic_type=None
```

### `maze_occupancy_6x6_47.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, up, up, right, right, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, right, down, right, down, left, down, right, right, down, right, down, right, down, right, up, right, down, left, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1781,
        license='',
        start_index=187,
        uri='https://americanarchive.org/catalog/cpb-aacip-b6e75cd0ce5'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,left,down,right,right,down,right,down,right,down,right,up,right,down,left,down,right,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ToWVacmeHbyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_47.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, up, up, right, right, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down, right, down, down, right, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,right,down,down,right,right,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UIWVacz6Aa2WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_47.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, up, up, right, right, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, right, down, right, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,right,down,right,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UIWVaZfwOujpnsEP173biQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=4343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4343
    ),
  ],
  total_token_count=4404
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=61 candidates_tokens_details=None prompt_token_count=4343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4343
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4404 traffic_type=None
```

### `maze_occupancy_6x6_adj_47.txt`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, up, up, right, right, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4WVafaeB62WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1279,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1279
    ),
  ],
  total_token_count=1929
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1279 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1279
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1929 traffic_type=None
```

### `maze_occupancy_6x6_ascii_47.txt`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, up, up, right, right, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, left, down, down, down, right, right, right, right, right, down, down, left, left, left, left, left, up, left, up, up, up, up, right, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,left,down,down,down,right,right,right,right,right,down,down,left,left,left,left,left,up,left,up,up,up,up,right,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4WVafPxO6PwnsEPgLOouAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=97,
  prompt_token_count=255,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=255
    ),
  ],
  total_token_count=352
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=97 candidates_tokens_details=None prompt_token_count=255 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=255
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=352 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_47.txt`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, right, right, up, up, up, up, up, up, right, right, right, right, down, down, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VIWVaZmaJuTQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=67,
  prompt_token_count=2162,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2162
    ),
  ],
  total_token_count=2229
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=67 candidates_tokens_details=None prompt_token_count=2162 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2162
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2229 traffic_type=None
```

