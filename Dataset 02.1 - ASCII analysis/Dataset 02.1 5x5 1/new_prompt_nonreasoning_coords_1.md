# LLM Maze Solving Comparison Report

 NEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-flash-lite`

**Prompt Used:** `You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools. The maze is represented as a 5x5 grid. The top-left corner is (0,0).Instructions: 1. You cannot move diagonally or through walls ('-' and '|'), only from one cell to an adjacent cell. 2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1). 3. Provide only the final list of coordinates from start to end in your response.`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_1.txt` | **27.27%** | `input: 218 , ouput: 53` | `(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_1.txt`

**Score:** 27.27%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)
```

**Extracted Answer:**
```
(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)
```

**Full Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(4,2),(4,3),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ngICaby4K-uE7M8PgfqOkQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=218,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=218
    ),
  ],
  total_token_count=271
) automatic_function_calling_history=[] parsed=None
```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(4,1),(4,2),(4,3),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ngICaby4K-uE7M8PgfqOkQQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=53,
  prompt_token_count=218,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=218
    ),
  ],
  total_token_count=271
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=144 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=53 candidates_tokens_details=None prompt_token_count=218 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=218
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=271 traffic_type=None
```

