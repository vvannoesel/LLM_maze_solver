# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_50.jpg` | **4.17%** | `input: 434 , ouput: 23` | `down, down, right, right, down, down, right, right, up, right, down, down` |
| `maze_line_6x6_50.json` | **4.17%** | `input: 1809 , ouput: 23` | `down, down, right, down, right, down, right, right, down, right, down, right` |
| `maze_line_6x6_adj_50.json` | **4.17%** | `input: 2258 , ouput: 19` | `down, down, down, down, down, right, right, right, right, right` |
| `maze_line_6x6_adj_50.txt` | **0.00%** | `input: 729 , ouput: 27` | `right, down, right, right, down, down, right, right, down, right, down, down, right, right` |
| `maze_line_6x6_tokenized_50.txt` | **0.00%** | `input: 673 , ouput: 650` | `the, maze, is, represented, as, follows, where, 'o', is, the, origin, and, 't', is, the, target:, (0, 0), o, (no, walls), |, (0, 1), |, (0, 2), |, (0, 3), |, (0, 4), |, (0, 5), -------------------------------------------------------, (1, 0), |, (1, 1), |, (1, 2), |, (1, 3), |, (1, 4), |, (1, 5), -------------------------------------------------------, (2, 0), |, (2, 1), |, (2, 2), |, (2, 3), |, (2, 4), |, (2, 5), -------------------------------------------------------, (3, 0), |, (3, 1), |, (3, 2), |, (3, 3), |, (3, 4), |, (3, 5), -------------------------------------------------------, (4, 0), |, (4, 1), |, (4, 2), |, (4, 3), |, (4, 4), |, (4, 5), -------------------------------------------------------, (5, 0), |, (5, 1), |, (5, 2), |, (5, 3), |, (5, 4), |, (5, 5), t, let's, analyze, the, walls, for, each, cell:, (0, 0):, <|origin|>, (no, walls, can, move, right, down), (0, 1):, <|updownleft_wall|>, (no, right, wall), (0, 2):, <|up_wall|>, (can, move, down), (0, 3):, <|upright_wall|>, (can, move, left), (0, 4):, <|upleft_wall|>, (can, move, right), (0, 5):, <|updownright_wall|>, (can, move, left), (1, 0):, <|downleft_wall|>, (can, move, up, right), (1, 1):, <|updown_wall|>, (can, move, left, right), (1, 2):, <|downright_wall|>, (can, move, up, left), (1, 3):, <|rightleft_wall|>, (can, move, up, down), (1, 4):, <|left_wall|>, (can, move, up, right), (1, 5):, <|upright_wall|>, (can, move, down, left), (2, 0):, <|uprightleft_wall|>, (can, move, down), (2, 1):, <|upleft_wall|>, (can, move, down, right), (2, 2):, <|updown_wall|>, (can, move, left, right), (2, 3):, <|downright_wall|>, (can, move, up, left), (2, 4):, <|downrightleft_wall|>, (can, move, up, right), (2, 5):, <|rightleft_wall|>, (can, move, up, down), (3, 0):, <|rightleft_wall|>, (can, move, up, down)` |
| `maze_occupancy_6x6_50.jpg` | **0.00%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, up, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, up, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right` |
| `maze_occupancy_6x6_50.json` | **0.00%** | `input: 988 , ouput: 650` | `right, down, down, right, right, right, right, right, down, down, right, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down` |
| `maze_occupancy_6x6_adj_50.json` | **12.50%** | `input: 4339 , ouput: 650` | `down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down` |
| `maze_occupancy_6x6_adj_50.txt` | **4.17%** | `input: 1276 , ouput: 59` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up` |
| `maze_occupancy_6x6_ascii_50.txt` | **4.17%** | `input: 253 , ouput: 650` | `down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, down, down, down, right, right, right, right, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, right` |
| `maze_occupancy_6x6_tokenized_50.txt` | **0.00%** | `input: 2162 , ouput: 650` | `right, down, down, down, right, right, down, right, right, down, down, down, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right` |

---

## Full LLM Responses

### `maze_line_6x6_50.jpg`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, left, left, down, down, left, down, right, right, up, up, right, down, right, up, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, up, right, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,up,right,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d4WVaa-ZIa2xnsEPvd25uQM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=23,
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
  total_token_count=457
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=23 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=457 traffic_type=None
```

### `maze_line_6x6_50.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, left, left, down, down, left, down, right, right, up, up, right, down, right, up, right, down, down
```

**Extracted Answer:**
```
down, down, right, down, right, down, right, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, down, right, down, right, right, down, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eIWVaeeZNqG-nsEPq8WDwQc' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_50.json`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, left, left, down, down, left, down, right, right, up, up, right, down, right, up, right, down, down
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
        text='down, down, down, down, down, right, right, right, right, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eYWVafiyI4KN7M8Pn42j8Qg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=19,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2277
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=19 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2277 traffic_type=None
```

### `maze_line_6x6_adj_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, left, left, down, down, left, down, right, right, up, up, right, down, right, up, right, down, down
```

**Extracted Answer:**
```
right, down, right, right, down, down, right, right, down, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,down,down,right,right,down,right,down,down,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='eoWVaf36H8yynsEP0d_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, right, right, up, right, down, down, left, left, down, down, left, down, right, right, up, up, right, down, right, up, right, down, down
```

**Extracted Answer:**
```
the, maze, is, represented, as, follows, where, 'o', is, the, origin, and, 't', is, the, target:, (0, 0), o, (no, walls), |, (0, 1), |, (0, 2), |, (0, 3), |, (0, 4), |, (0, 5), -------------------------------------------------------, (1, 0), |, (1, 1), |, (1, 2), |, (1, 3), |, (1, 4), |, (1, 5), -------------------------------------------------------, (2, 0), |, (2, 1), |, (2, 2), |, (2, 3), |, (2, 4), |, (2, 5), -------------------------------------------------------, (3, 0), |, (3, 1), |, (3, 2), |, (3, 3), |, (3, 4), |, (3, 5), -------------------------------------------------------, (4, 0), |, (4, 1), |, (4, 2), |, (4, 3), |, (4, 4), |, (4, 5), -------------------------------------------------------, (5, 0), |, (5, 1), |, (5, 2), |, (5, 3), |, (5, 4), |, (5, 5), t, let's, analyze, the, walls, for, each, cell:, (0, 0):, <|origin|>, (no, walls, can, move, right, down), (0, 1):, <|updownleft_wall|>, (no, right, wall), (0, 2):, <|up_wall|>, (can, move, down), (0, 3):, <|upright_wall|>, (can, move, left), (0, 4):, <|upleft_wall|>, (can, move, right), (0, 5):, <|updownright_wall|>, (can, move, left), (1, 0):, <|downleft_wall|>, (can, move, up, right), (1, 1):, <|updown_wall|>, (can, move, left, right), (1, 2):, <|downright_wall|>, (can, move, up, left), (1, 3):, <|rightleft_wall|>, (can, move, up, down), (1, 4):, <|left_wall|>, (can, move, up, right), (1, 5):, <|upright_wall|>, (can, move, down, left), (2, 0):, <|uprightleft_wall|>, (can, move, down), (2, 1):, <|upleft_wall|>, (can, move, down, right), (2, 2):, <|updown_wall|>, (can, move, left, right), (2, 3):, <|downright_wall|>, (can, move, up, left), (2, 4):, <|downrightleft_wall|>, (can, move, up, right), (2, 5):, <|rightleft_wall|>, (can, move, up, down), (3, 0):, <|rightleft_wall|>, (can, move, up, down)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze is represented as follows, where 'O' is the origin and 'T' is the target:

(0,0) O (no walls) | (0,1) | (0,2) | (0,3) | (0,4) | (0,5)
-------------------------------------------------------
(1,0) | (1,1) | (1,2) | (1,3) | (1,4) | (1,5)
-------------------------------------------------------
(2,0) | (2,1) | (2,2) | (2,3) | (2,4) | (2,5)
-------------------------------------------------------
(3,0) | (3,1) | (3,2) | (3,3) | (3,4) | (3,5)
-------------------------------------------------------
(4,0) | (4,1) | (4,2) | (4,3) | (4,4) | (4,5)
-------------------------------------------------------
(5,0) | (5,1) | (5,2) | (5,3) | (5,4) | (5,5) T

Let's analyze the walls for each cell:

(0,0): <|origin|> (no walls, can move right, down)
(0,1): <|updownleft_wall|> (no right wall)
(0,2): <|up_wall|> (can move down)
(0,3): <|upright_wall|> (can move left)
(0,4): <|upleft_wall|> (can move right)
(0,5): <|updownright_wall|> (can move left)

(1,0): <|downleft_wall|> (can move up, right)
(1,1): <|updown_wall|> (can move left, right)
(1,2): <|downright_wall|> (can move up, left)
(1,3): <|rightleft_wall|> (can move up, down)
(1,4): <|left_wall|> (can move up, right)
(1,5): <|upright_wall|> (can move down, left)

(2,0): <|uprightleft_wall|> (can move down)
(2,1): <|upleft_wall|> (can move down, right)
(2,2): <|updown_wall|> (can move left, right)
(2,3): <|downright_wall|> (can move up, left)
(2,4): <|downrightleft_wall|> (can move up, right)
(2,5): <|rightleft_wall|> (can move up, down)

(3,0): <|rightleft_wall|> (can move up, down)"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='fIWVaeqUNtqI7M8Plt3AoAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_50.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, up, right, up, right, down, right, down, left, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, up, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right, down, right, down, right, up, right, down, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,up,right,up,right,up,right,up,right,down,right,down,left,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,up,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,down,right,down,right,up,right,down,right,up,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='f4WVaaigIbW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_50.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, right, down, down, right, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, down, down, right, right, right, down, down, right, right, right, down, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,right,down,down,right,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,down,down,right,right,right,down,down,right,right,right,down,down,down,right,right,right,right,right,down,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='gYWVaYf3J7zhnsEPwLCgiQY' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_6x6_adj_50.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down, down, right, right, right, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,down,right,right,right,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='g4WVaaKMNbyK7M8PiJiNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4339,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4339
    ),
  ],
  total_token_count=4989
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4339 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4339
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4989 traffic_type=None
```

### `maze_occupancy_6x6_adj_50.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hIWVaZvMJbT7nsEPovPikQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=59,
  prompt_token_count=1276,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1276
    ),
  ],
  total_token_count=1335
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=59 candidates_tokens_details=None prompt_token_count=1276 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1276
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1335 traffic_type=None
```

### `maze_occupancy_6x6_ascii_50.txt`

**Score:** 4.17%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, up, up, up, up, up, left, left, left, left, left, down, down, down, down, down, right, right, right, right, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,right,up,up,up,up,up,left,left,left,left,left,down,down,down,down,down,right,right,right,right,down,down,down,right,right,right,right,right,right,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,right,right,right,right,right,right,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,down,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,up,up,up,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='hoWVaYSqK6jlnsEP1bugwAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=253,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=253
    ),
  ],
  total_token_count=903
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=253 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=253
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=903 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_50.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
down, down, right, right, right, right, up, up, right, right, down, down, down, down, left, left, left, left, down, down, down, down, left, left, down, down, right, right, right, right, up, up, up, up, right, right, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, down, right, right, down, right, right, down, down, down, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,down,right,right,down,right,right,down,down,down,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='iIWVaaKJO_nOnsEPkprNkQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

