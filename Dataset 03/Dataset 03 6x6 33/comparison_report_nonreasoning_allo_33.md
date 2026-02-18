# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_33.jpg` | **0.00%** | `input: 434 , ouput: 25` | `down, down, right, right, right, down, down, right, right, up, right, down, down` |
| `maze_line_6x6_33.json` | **12.50%** | `input: 1809 , ouput: 19` | `right, down, right, down, right, down, right, down, right, down` |
| `maze_line_6x6_adj_33.json` | **25.00%** | `input: 2258 , ouput: 21` | `right, down, down, down, right, right, down, down, right, right, down` |
| `maze_line_6x6_adj_33.txt` | **6.25%** | `input: 729 , ouput: 37` | `right, right, right, down, down, down, right, right, down, down, left, down, right, right, right, down, down, down, right` |
| `maze_line_6x6_tokenized_33.txt` | **6.25%** | `input: 673 , ouput: 219` | `right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_33.jpg` | **0.00%** | `input: 431 , ouput: 73` | `down, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, right, up, right, up, left, up, right, up, right, up, right, down, right, down, right, down, right` |
| `maze_occupancy_6x6_33.json` | **nan%** | `input: 988 , ouput: 0` | `` |
| `maze_occupancy_6x6_adj_33.json` | **25.00%** | `input: 4338 , ouput: 49` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_33.txt` | **0.00%** | `input: 1275 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_ascii_33.txt` | **12.50%** | `input: 258 , ouput: 650` | `right, right, down, down, right, right, right, down, down, left, down, right, right, right, down, left, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, down, left, left, left, down, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right` |
| `maze_occupancy_6x6_tokenized_33.txt` | **25.00%** | `input: 2162 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_6x6_33.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, down, left, down, down, right, up, right, right, down, right, up, right, down
```

**Extracted Answer:**
```
down, down, right, right, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I4SVaZbtIqfx7M8PiZPD-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=25,
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
  total_token_count=459
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=25 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=459 traffic_type=None
```

### `maze_line_6x6_33.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, down, down, down, left, down, down, right, up, right, right, down, right, up, right, down
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
        text='right, down, right, down, right, down, right, down, right, down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JISVaeKHGI65kdUPytPImQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=1809,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1809
    ),
  ],
  total_token_count=1828
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=1809 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1809
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1828 traffic_type=None
```

### `maze_line_6x6_adj_33.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, down, down, down, left, down, down, right, up, right, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, down, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,down,down,right,right,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JYSVafLHEvjHnsEP9ouZ4Qg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_33.txt`

**Score:** 6.25%

**Ground Truth Solution:**
```
right, down, down, down, left, down, down, right, up, right, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, down, down, down, right, right, down, down, left, down, right, right, right, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,down,right,right,down,down,left,down,right,right,right,down,down,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JoSVadjqCIKN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=766
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=766 traffic_type=None
```

### `maze_line_6x6_tokenized_33.txt`

**Score:** 6.25%

**Ground Truth Solution:**
```
right, down, down, down, left, down, down, right, up, right, right, down, right, up, right, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='J4SVafyBLP367M8P1uGygAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=219,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=892
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=219 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=892 traffic_type=None
```

### `maze_occupancy_6x6_33.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, down, right, down, right, down, right, up, right, up, right, down, right, down, left, down, right, down, right, up, right, up, left, up, right, up, right, up, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,down,right,down,right,down,right,up,right,up,right,down,right,down,left,down,right,down,right,up,right,up,left,up,right,up,right,up,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KISVaZahOqPwnsEPgLOouAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=73,
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
  total_token_count=504
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=73 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=504 traffic_type=None
```

### `maze_occupancy_6x6_33.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='K4SVaY36MKzd7M8PoNSSsQM' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=988
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=988 traffic_type=None
```

### `maze_occupancy_6x6_adj_33.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LISVabOPMIWF7M8PnoeMqQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=49,
  prompt_token_count=4338,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4338
    ),
  ],
  total_token_count=4387
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=49 candidates_tokens_details=None prompt_token_count=4338 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4338
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4387 traffic_type=None
```

### `maze_occupancy_6x6_adj_33.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LoSVacbBE7njnsEPxoKX6AU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_ascii_33.txt`

**Score:** 12.50%

**Ground Truth Solution:**
```
right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, left, down, right, right, right, down, left, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, down, left, left, left, down, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right, right, down, left, left, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,left,down,right,right,right,down,left,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,down,left,left,left,down,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,right,down,left,left,down,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MISVaYr0BKL17M8Pt6zc8AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=258
    ),
  ],
  total_token_count=908
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=908 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_33.txt`

**Score:** 25.00%

**Ground Truth Solution:**
```
right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, right, right, down, down, right, right, up, up, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='MoSVacDDFYKG7M8P78DBqQk' usage_metadata=GenerateContentResponseUsageMetadata(
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

