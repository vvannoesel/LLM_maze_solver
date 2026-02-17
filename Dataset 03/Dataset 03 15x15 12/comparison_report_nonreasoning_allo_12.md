# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_12.jpg` | **2.38%** | `input: 436 , ouput: 650` | `right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right` |
| `maze_line_15x15_12.json` | **0.00%** | `input: 9807 , ouput: 650` | `down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_12.json` | **1.19%** | `input: 13486 , ouput: 55` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_12.txt` | **nan%** | `input: 3678 , ouput: 0` | `` |
| `maze_line_15x15_tokenized_12.txt` | **2.38%** | `input: 3284 , ouput: 650` | `right, down, right, right, right, right, right, down, right, down, down, down, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_12.jpg` | **0.60%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right` |
| `maze_occupancy_15x15_12.json` | **2.38%** | `input: 4246 , ouput: 650` | `right, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down` |
| `maze_occupancy_15x15_adj_12.json` | **1.79%** | `input: 27636 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_12.txt` | **0.00%** | `input: 7731 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right` |
| `maze_occupancy_15x15_ascii_12.txt` | **1.79%** | `input: 529 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_12.txt` | **2.38%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_12.jpg`

**Score:** 2.38%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, up, up, up, right, right, right, right, down, left, left, left, down, down, down, right, right, right, up, up, right, right, down, left, down, down, right, right, down, left, down, right, down, right, right, down, down, right, right, up, left, up, up, up, right, up, up, left, up, right, up, left, up, left, up, right, right, right, down, down, down, down, down, down, down, left, down, right, down, down, down, left, left, down, right, down, down, right
```

**Extracted Answer:**
```
right, down, right, down, left, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,left,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='DJ-UaYyALpeBkdUP9--_-AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=436,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=178
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=1086
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=436 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=436 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=178
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1086 traffic_type=None
```

### `maze_line_15x15_12.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, up, up, up, right, right, right, right, down, left, left, left, down, down, down, right, right, right, up, up, right, right, down, left, down, down, right, right, down, left, down, right, down, right, right, down, down, right, right, up, left, up, up, up, right, up, up, left, up, right, up, left, up, left, up, right, right, right, down, down, down, down, down, down, down, left, down, right, down, down, down, left, left, down, right, down, down, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Dp-UaZqBJ8iOkdUPuavdqQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=9807,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9807
    ),
  ],
  total_token_count=10457
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=9807 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=9807
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=10457 traffic_type=None
```

### `maze_line_15x15_adj_12.json`

**Score:** 1.19%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, up, up, up, right, right, right, right, down, left, left, left, down, down, down, right, right, right, up, up, right, right, down, left, down, down, right, right, down, left, down, right, down, right, right, down, down, right, right, up, left, up, up, up, right, up, up, left, up, right, up, left, up, left, up, right, right, right, down, down, down, down, down, down, down, left, down, right, down, down, down, left, left, down, right, down, down, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='D5-UadnmCtX1kdUPq5K00AM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=13486,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13486
    ),
  ],
  total_token_count=13541
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=13486 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13486
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13541 traffic_type=None
```

### `maze_line_15x15_adj_12.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, up, up, up, right, right, right, right, down, left, left, left, down, down, down, right, right, right, up, up, right, right, down, left, down, down, right, right, down, left, down, right, down, right, right, down, down, right, right, up, left, up, up, up, right, up, up, left, up, right, up, left, up, left, up, right, right, right, down, down, down, down, down, down, down, left, down, right, down, down, down, left, left, down, right, down, down, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Ep-Uaeb1E9jpnsEPp8vxyAE' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=3678,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3678
    ),
  ],
  total_token_count=3678
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=3678 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3678
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3678 traffic_type=None
```

### `maze_line_15x15_tokenized_12.txt`

**Score:** 2.38%

**Ground Truth Solution:**
```
right, down, left, down, down, right, right, up, up, up, right, right, right, right, down, left, left, left, down, down, down, right, right, right, up, up, right, right, down, left, down, down, right, right, down, left, down, right, down, right, right, down, down, right, right, up, left, up, up, up, right, up, up, left, up, right, up, left, up, left, up, right, right, right, down, down, down, down, down, down, down, left, down, right, down, down, down, left, left, down, right, down, down, right
```

**Extracted Answer:**
```
right, down, right, right, right, right, right, down, right, down, down, down, down, down, down, right, right, right, down, right, right, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,right,right,right,right,down,right,down,down,down,down,down,down,right,right,right,down,right,right,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='FJ-Uad7NHrK7nsEPp-bmmQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3284,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3284
    ),
  ],
  total_token_count=3934
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3284 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3284
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3934 traffic_type=None
```

### `maze_occupancy_15x15_12.jpg`

**Score:** 0.60%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, up, up, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, up, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,up,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='F5-Uacc66Z6R1Q-g8utx' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_12.json`

**Score:** 2.38%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, up, up, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down, down, down, down, down, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,down,down,down,down,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='GJ-Uad7gOOmekdUPoPLrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4896
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4896 traffic_type=None
```

### `maze_occupancy_15x15_adj_12.json`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, up, up, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Gp-Uacf9G8_HnsEPxMXdkAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27636,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27636
    ),
  ],
  total_token_count=28286
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27636 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27636
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28286 traffic_type=None
```

### `maze_occupancy_15x15_adj_12.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, up, up, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,right,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='G5-UaYW_L4P3kdUPieGruQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7731,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7731
    ),
  ],
  total_token_count=8381
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7731 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7731
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8381 traffic_type=None
```

### `maze_occupancy_15x15_ascii_12.txt`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, up, up, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, down, down, right, right, right, right, right, down, down, down, right, right, right, right, right, down, down, down, down, down, down, left, left, left, down, down, left, left, left, left, left, left, left, left, left, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,down,down,right,right,right,right,right,down,down,down,right,right,right,right,right,down,down,down,down,down,down,left,left,left,down,down,left,left,left,left,left,left,left,left,left,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='HZ-UaZ6_PLDHnsEPzv7l8QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=529,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=529
    ),
  ],
  total_token_count=1179
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=529 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=529
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1179 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_12.txt`

**Score:** 2.38%

**Ground Truth Solution:**
```
right, right, down, down, left, left, down, down, down, down, right, right, right, right, up, up, up, up, up, up, right, right, right, right, right, right, right, right, down, down, left, left, left, left, left, left, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, right, right, right, right, down, down, left, left, down, down, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, up, up, left, left, up, up, up, up, up, up, right, right, up, up, up, up, left, left, up, up, right, right, up, up, left, left, up, up, left, left, up, up, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='H5-Uad63E5S8nsEPnPGoiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=12134,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=12134
    ),
  ],
  total_token_count=12784
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=12134 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=12134
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=12784 traffic_type=None
```

