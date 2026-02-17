# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_48.jpg` | **1.79%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, left, down, right, right, down, right, down, left, down, right, down, left, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right` |
| `maze_line_15x15_48.json` | **0.89%** | `input: 9807 , ouput: 650` | `right, right, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right` |
| `maze_line_15x15_adj_48.json` | **0.89%** | `input: 13489 , ouput: 55` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_48.txt` | **0.89%** | `input: 3681 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right` |
| `maze_line_15x15_tokenized_48.txt` | **0.00%** | `input: 3283 , ouput: 650` | `down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right` |
| `maze_occupancy_15x15_48.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_48.json` | **0.45%** | `input: 4246 , ouput: 650` | `right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, right, right, down, right, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, down, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right` |
| `maze_occupancy_15x15_adj_48.json` | **1.34%** | `input: 27630 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_48.txt` | **1.34%** | `input: 7732 , ouput: 650` | `right, right, down, right, down, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_48.txt` | **1.34%** | `input: 538 , ouput: 650` | `right, right, down, right, right, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right` |
| `maze_occupancy_15x15_tokenized_48.txt` | **2.68%** | `input: 12134 , ouput: 650` | `right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_48.jpg`

**Score:** 1.79%

**Ground Truth Solution:**
```
right, down, down, right, right, right, up, right, down, right, up, up, right, right, down, down, right, down, right, down, right, up, right, right, up, right, down, down, down, left, down, right, down, left, left, up, left, left, left, down, left, up, up, up, left, left, down, right, down, left, down, left, up, up, left, left, left, left, down, left, down, right, down, down, right, down, right, up, right, up, right, down, right, down, left, left, down, left, down, right, down, right, down, right, up, up, right, up, up, up, up, right, down, down, right, up, right, down, right, up, right, right, down, down, left, down, down, right, up, right, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, right, down, right, down, left, down, right, down, left, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,right,down,right,down,left,down,right,down,left,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,up,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='X6uUaZKiKcewnsEPm4ag0QM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_48.json`

**Score:** 0.89%

**Ground Truth Solution:**
```
right, down, down, right, right, right, up, right, down, right, up, up, right, right, down, down, right, down, right, down, right, up, right, right, up, right, down, down, down, left, down, right, down, left, left, up, left, left, left, down, left, up, up, up, left, left, down, right, down, left, down, left, up, up, left, left, left, left, down, left, down, right, down, down, right, down, right, up, right, up, right, down, right, down, left, left, down, left, down, right, down, right, down, right, up, up, right, up, up, up, up, right, down, down, right, up, right, down, right, up, right, right, down, down, left, down, down, right, up, right, down, down
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right, right, right, right, right, down, down, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,right,right,right,right,down,down,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YauUacPlK8eUnsEPgvzb-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_48.json`

**Score:** 0.89%

**Ground Truth Solution:**
```
right, down, down, right, right, right, up, right, down, right, up, up, right, right, down, down, right, down, right, down, right, up, right, right, up, right, down, down, down, left, down, right, down, left, left, up, left, left, left, down, left, up, up, up, left, left, down, right, down, left, down, left, up, up, left, left, left, left, down, left, down, right, down, down, right, down, right, up, right, up, right, down, right, down, left, left, down, left, down, right, down, right, down, right, up, up, right, up, up, up, up, right, down, down, right, up, right, down, right, up, right, right, down, down, left, down, down, right, up, right, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YquUaZ7XJ5z07M8PqPy4oQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=55,
  prompt_token_count=13489,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13489
    ),
  ],
  total_token_count=13544
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=55 candidates_tokens_details=None prompt_token_count=13489 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13489
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13544 traffic_type=None
```

### `maze_line_15x15_adj_48.txt`

**Score:** 0.89%

**Ground Truth Solution:**
```
right, down, down, right, right, right, up, right, down, right, up, up, right, right, down, down, right, down, right, down, right, up, right, right, up, right, down, down, down, left, down, right, down, left, left, up, left, left, left, down, left, up, up, up, left, left, down, right, down, left, down, left, up, up, left, left, left, left, down, left, down, right, down, down, right, down, right, up, right, up, right, down, right, down, left, left, down, left, down, right, down, right, down, right, up, up, right, up, up, up, up, right, down, down, right, up, right, down, right, up, right, right, down, down, left, down, down, right, up, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZKuUaYTKIo3hnsEP38LqiQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3681,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3681
    ),
  ],
  total_token_count=4331
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3681 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3681
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4331 traffic_type=None
```

### `maze_line_15x15_tokenized_48.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, down, right, right, right, up, right, down, right, up, up, right, right, down, down, right, down, right, down, right, up, right, right, up, right, down, down, down, left, down, right, down, left, left, up, left, left, left, down, left, up, up, up, left, left, down, right, down, left, down, left, up, up, left, left, left, left, down, left, down, right, down, down, right, down, right, up, right, up, right, down, right, down, left, left, down, left, down, right, down, right, down, right, up, up, right, up, up, up, up, right, down, down, right, up, right, down, right, up, right, right, down, down, left, down, down, right, up, right, down, down
```

**Extracted Answer:**
```
down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZquUaYKjGaDxnsEP86zG2AI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3283,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3283
    ),
  ],
  total_token_count=3933
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3283 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3283
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3933 traffic_type=None
```

### `maze_occupancy_15x15_48.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aquUaaipMf3onsEP3cCnyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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
  total_token_count=431
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=431 traffic_type=None
```

### `maze_occupancy_15x15_48.json`

**Score:** 0.45%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, down, down, right, right, right, right, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, right, right, down, right, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, right, right, right, down, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,down,right,right,right,right,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,right,right,down,right,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,right,right,right,down,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bKuUacWLNominsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_48.json`

**Score:** 1.34%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bquUafvvGaeN7M8P04OMiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27630,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27630
    ),
  ],
  total_token_count=28280
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27630 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27630
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28280 traffic_type=None
```

### `maze_occupancy_15x15_adj_48.txt`

**Score:** 1.34%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cKuUaZ3WGceqnsEPypadgQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7732,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7732
    ),
  ],
  total_token_count=8382
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7732 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7732
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8382 traffic_type=None
```

### `maze_occupancy_15x15_ascii_48.txt`

**Score:** 1.34%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right, right, down, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,right,down,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cquUab79HK3hnsEPxYDs0QE' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=538,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=538
    ),
  ],
  total_token_count=1188
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=538 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=538
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1188 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_48.txt`

**Score:** 2.68%

**Ground Truth Solution:**
```
right, right, down, down, down, down, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, up, up, right, right, right, right, down, down, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, right, right, down, down, left, left, left, left, up, up, left, left, left, left, left, left, down, down, left, left, up, up, up, up, up, up, left, left, left, left, down, down, right, right, down, down, left, left, down, down, left, left, up, up, up, up, left, left, left, left, left, left, left, left, down, down, left, left, down, down, right, right, down, down, down, down, right, right, down, down, right, right, up, up, right, right, up, up, right, right, down, down, right, right, down, down, left, left, left, left, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, up, up, right, right, up, up, up, up, up, up, up, up, right, right, down, down, down, down, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down
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
        text='right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dKuUad23EaeN7M8P04OMiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

