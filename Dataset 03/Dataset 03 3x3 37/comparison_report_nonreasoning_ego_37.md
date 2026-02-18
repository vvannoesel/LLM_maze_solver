# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_37.jpg` | **0.00%** | `input: 551 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_37.json` | **0.00%** | `input: 774 , ouput: 414` | `the, agent, starts, at, (0, 0), facing, south., 1., **start, at, (0, 0), facing, south.**, -, the, wall, to, the, north, is, true, east, is, true, south, is, false, west, is, true., -, since, south, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (1, 0), facing, south., 2., **at, (1, 0), facing, south.**, -, the, wall, to, the, north, is, false, east, is, true, south, is, false, west, is, true., -, since, south, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (2, 0), facing, south., 3., **at, (2, 0), facing, south.**, -, the, wall, to, the, north, is, false, east, is, false, south, is, true, west, is, true., -, since, south, is, true, we, cannot, move, forward., we, need, to, turn., -, to, move, east, we, need, to, turn, left., -, **action:, left**, -, agent, is, now, at, (2, 0), facing, east., 4., **at, (2, 0), facing, east.**, -, the, wall, to, the, north, is, false, east, is, false, south, is, true, west, is, true., -, since, east, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (2, 1), facing, east., 5., **at, (2, 1), facing, east.**, -, the, wall, to, the, north, is, true, east, is, false, south, is, true, west, is, false., -, since, east, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (2, 2), facing, east., the, agent, has, reached, the, end, at, (2, 2)., forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_37.json` | **0.00%** | `input: 836 , ouput: 15` | `right, forward, right, forward, forward, left, forward, forward` |
| `maze_line_3x3_adj_37.txt` | **0.00%** | `input: 468 , ouput: 13` | `right, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_tokenized_37.txt` | **0.00%** | `input: 439 , ouput: 11` | `right, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_37.jpg` | **25.00%** | `input: 546 , ouput: 35` | `forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_37.json` | **0.00%** | `input: 589 , ouput: 57` | `right, forward, right, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward` |
| `maze_occupancy_3x3_adj_37.json` | **0.00%** | `input: 1292 , ouput: 43` | `right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward` |
| `maze_occupancy_3x3_adj_37.txt` | **0.00%** | `input: 580 , ouput: 41` | `right, forward, right, forward, right, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_ascii_37.txt` | **0.00%** | `input: 318 , ouput: 47` | `right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward` |
| `maze_occupancy_3x3_tokenized_37.txt` | **0.00%** | `input: 867 , ouput: 47` | `right, forward, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_37.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hpqVae_GDOKAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
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
  total_token_count=566
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=566 traffic_type=None
```

### `maze_line_3x3_37.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), facing, south., 1., **start, at, (0, 0), facing, south.**, -, the, wall, to, the, north, is, true, east, is, true, south, is, false, west, is, true., -, since, south, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (1, 0), facing, south., 2., **at, (1, 0), facing, south.**, -, the, wall, to, the, north, is, false, east, is, true, south, is, false, west, is, true., -, since, south, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (2, 0), facing, south., 3., **at, (2, 0), facing, south.**, -, the, wall, to, the, north, is, false, east, is, false, south, is, true, west, is, true., -, since, south, is, true, we, cannot, move, forward., we, need, to, turn., -, to, move, east, we, need, to, turn, left., -, **action:, left**, -, agent, is, now, at, (2, 0), facing, east., 4., **at, (2, 0), facing, east.**, -, the, wall, to, the, north, is, false, east, is, false, south, is, true, west, is, true., -, since, east, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (2, 1), facing, east., 5., **at, (2, 1), facing, east.**, -, the, wall, to, the, north, is, true, east, is, false, south, is, true, west, is, false., -, since, east, is, false, we, can, move, forward., -, **action:, forward**, -, agent, is, now, at, (2, 2), facing, east., the, agent, has, reached, the, end, at, (2, 2)., forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (0,0) facing South.

1. **Start at (0,0) facing South.**
   - The wall to the North is True, East is True, South is False, West is True.
   - Since South is False, we can move forward.
   - **Action: forward**
   - Agent is now at (1,0) facing South.

2. **At (1,0) facing South.**
   - The wall to the North is False, East is True, South is False, West is True.
   - Since South is False, we can move forward.
   - **Action: forward**
   - Agent is now at (2,0) facing South.

3. **At (2,0) facing South.**
   - The wall to the North is False, East is False, South is True, West is True.
   - Since South is True, we cannot move forward. We need to turn.
   - To move East, we need to turn left.
   - **Action: left**
   - Agent is now at (2,0) facing East.

4. **At (2,0) facing East.**
   - The wall to the North is False, East is False, South is True, West is True.
   - Since East is False, we can move forward.
   - **Action: forward**
   - Agent is now at (2,1) facing East.

5. **At (2,1) facing East.**
   - The wall to the North is True, East is False, South is True, West is False.
   - Since East is False, we can move forward.
   - **Action: forward**
   - Agent is now at (2,2) facing East.

The agent has reached the end at (2,2).

forward,forward,left,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='h5qVaZLDO9WbkdUPuuCoyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=414,
  prompt_token_count=774,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=774
    ),
  ],
  total_token_count=1188
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=414 candidates_tokens_details=None prompt_token_count=774 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=774
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1188 traffic_type=None
```

### `maze_line_3x3_adj_37.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iJqVaZHaJvT77M8Prpvt6Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=836,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=836
    ),
  ],
  total_token_count=851
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=836 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=836
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=851 traffic_type=None
```

### `maze_line_3x3_adj_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iZqVafi8DJHw7M8Pi4iBgAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=468,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=468
    ),
  ],
  total_token_count=481
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=468 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=468
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=481 traffic_type=None
```

### `maze_line_3x3_tokenized_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iZqVaeXyMNqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=439,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=439
    ),
  ],
  total_token_count=450
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=439 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=439
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=450 traffic_type=None
```

### `maze_occupancy_3x3_37.jpg`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
forward, forward, right, forward, forward, left, forward, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,forward,right,forward,forward,left,forward,forward,forward,right,forward,forward,left,forward,forward,left,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ipqVafPxGtqfnsEPuPyNyAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
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
  total_token_count=581
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=546 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=288
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=581 traffic_type=None
```

### `maze_occupancy_3x3_37.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, right, forward, forward, right, forward, forward, forward, left, forward, left, forward, forward, right, forward, forward, forward, forward, left, forward, left, forward, forward, right, forward, right, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i5qVacLTAq2WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=589,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=589
    ),
  ],
  total_token_count=646
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=589 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=589
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=646 traffic_type=None
```

### `maze_occupancy_3x3_adj_37.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='i5qVaYyGKeeGkdUPsqK74AQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=43,
  prompt_token_count=1292,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1292
    ),
  ],
  total_token_count=1335
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=43 candidates_tokens_details=None prompt_token_count=1292 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1292
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1335 traffic_type=None
```

### `maze_occupancy_3x3_adj_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jJqVadiUEMyynsEPyd_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=41,
  prompt_token_count=580,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=580
    ),
  ],
  total_token_count=621
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=41 candidates_tokens_details=None prompt_token_count=580 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=580
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=621 traffic_type=None
```

### `maze_occupancy_3x3_ascii_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Right, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward, Left, Forward, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jJqVaYKGLqG-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=318,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=318
    ),
  ],
  total_token_count=365
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=318 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=318
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=365 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_37.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, forward, forward, left, forward, forward, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='jZqVaaLJKffo7M8PiZSSoQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=47,
  prompt_token_count=867,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=867
    ),
  ],
  total_token_count=914
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=47 candidates_tokens_details=None prompt_token_count=867 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=867
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=914 traffic_type=None
```

