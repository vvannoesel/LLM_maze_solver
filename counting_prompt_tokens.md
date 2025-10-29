# LLM Maze Solving Comparison Report

**Model Used:** `gemini-2.5-flash-lite`

**Prompt Used:** `You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools. The maze is represented as a 5x5 grid. The top-left corner is (0,0). The agent in the maze has a starting orientation facing southward. Instructions: 1. Give instructions to an agent in the maze. You can only use the following four actions: Forward: this moves the agent 1 step in the direction it is facing. Left: this turns the agent 90° to the left and then moves the agent 1 step in the new direction it is facing. Right: this turns the agent 90° to the right and then moves the agent 1 step in the new direction it is facing. Backward: this turns the agent 180° and then moves the agent 1 step in the new direction it is facing. 2. You cannot move diagonally or through walls, only from one cell to an adjacent cell. 3. Your output must be a single, comma-separated sequence of steps. For example: forward, left, right, forward, right. 4. Provide only the final list of instructions in your response.`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `None` | **1.00%** | `input: 250 , ouput: 1` | `None` |

---

## Full LLM Responses

### `None`

**Score:** 1.00%

**Extracted Answer:**
```
None
```

**Full Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='The'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='EYYAaZz3AuyPvdIP6LL16Ac' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=1,
  prompt_token_count=250,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=250
    ),
  ],
  total_token_count=251
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=250 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=1 candidates_tokens_details=None prompt_token_count=250 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=250
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=251 traffic_type=None
```

