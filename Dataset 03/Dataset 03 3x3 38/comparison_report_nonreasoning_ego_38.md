# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_38.jpg` | **0.00%** | `input: 551 , ouput: 19` | `right, forward, right, forward, forward, left, forward, forward, right, forward` |
| `maze_line_3x3_38.json` | **0.00%** | `input: 774 , ouput: 17` | `right, forward, right, forward, forward, left, forward, left, forward` |
| `maze_line_3x3_adj_38.json` | **0.00%** | `input: 836 , ouput: 17` | `right, forward, right, forward, backward, forward, left, forward, forward` |
| `maze_line_3x3_adj_38.txt` | **0.00%** | `input: 468 , ouput: 23` | `right, forward, right, forward, right, forward, left, forward, left, forward, left, forward` |
| `maze_line_3x3_tokenized_38.txt` | **0.00%** | `input: 439 , ouput: 27` | `right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, left, forward` |
| `maze_occupancy_3x3_38.jpg` | **0.00%** | `input: 546 , ouput: 43` | `right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, forward` |
| `maze_occupancy_3x3_38.json` | **0.00%** | `input: 589 , ouput: 69` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_38.json` | **0.00%** | `input: 1292 , ouput: 33` | `right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_38.txt` | **0.00%** | `input: 580 , ouput: 31` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_occupancy_3x3_ascii_38.txt` | **0.00%** | `input: 315 , ouput: 43` | `right, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward` |
| `maze_occupancy_3x3_tokenized_38.txt` | **0.00%** | `input: 867 , ouput: 143` | `right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_38.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, forward, left, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nJqVaYHKNrSDvdIP45SUiQE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=551,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=293
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=570
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=551 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=570 traffic_type=None
```

### `maze_line_3x3_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Left,Forward,Left,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nZqVaZqtGsCRvdIP1KnS4QI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=791
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=309 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=791 traffic_type=None
```

### `maze_line_3x3_adj_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, backward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,backward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='nZqVad28M-GlxN8Pk__ssAs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=853
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=280 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=853 traffic_type=None
```

### `maze_line_3x3_adj_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, left, forward, left, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, right, forward, left, forward, left, forward, left, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='npqVacXxE9PevdIPk6fOoQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=491
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=313 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=491 traffic_type=None
```

### `maze_line_3x3_tokenized_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, left, forward, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Left, Forward, Forward, Right, Forward, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='npqVaa_CNP6o28oP8YeKkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=27,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=466
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=311 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=27 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=466 traffic_type=None
```

### `maze_occupancy_3x3_38.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, right, forward, forward, left, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,right,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward,right,forward,forward,left,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='n5qVaeOlHNqb28oPgemZoQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=546,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=288
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=589
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=546 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=589 traffic_type=None
```

### `maze_occupancy_3x3_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oJqVad6yFO-0xN8P0rGNyQw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=69,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=658
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=289 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=69 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=658 traffic_type=None
```

### `maze_occupancy_3x3_adj_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,left,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oZqVadAMnLzE3w-Xl4LQDA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1325
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=280 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1325 traffic_type=None
```

### `maze_occupancy_3x3_adj_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='oZqVab-bJryLxs0Pjd6hiAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=611
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=313 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=611 traffic_type=None
```

### `maze_occupancy_3x3_ascii_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, right, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Forward,Forward,Right,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Forward,Right,Forward,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='opqVaa6qBfHXvdIPssLX-QQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=315,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=315
    ),
  ],
  total_token_count=358
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=288 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=315 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=315
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=358 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, forward, forward, right, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=625,
        license='',
        start_index=0,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='opqVadO8OryLxs0Pjd6hiAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=143,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=1010
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=312 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=143 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1010 traffic_type=None
```

