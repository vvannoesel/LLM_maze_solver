# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_21.jpg` | **0.88%** | `input: 436 , ouput: 650` | `right, down, down, right, down, down, right, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down` |
| `maze_line_15x15_21.json` | **0.00%** | `input: 9807 , ouput: 650` | `down, down, right, right, right, down, right, down, right, right, down, right, down, down, down, right, down, right, right, down, right, right, down, right, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down` |
| `maze_line_15x15_adj_21.json` | **nan%** | `input: 13488 , ouput: 0` | `` |
| `maze_line_15x15_adj_21.txt` | **nan%** | `input: 3680 , ouput: 0` | `` |
| `maze_line_15x15_tokenized_21.txt` | **0.00%** | `input: 3282 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down` |
| `maze_occupancy_15x15_21.jpg` | **0.88%** | `input: 431 , ouput: 650` | `right, right, down, right, down, down, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, down, down, right, right, down, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down` |
| `maze_occupancy_15x15_21.json` | **1.75%** | `input: 4246 , ouput: 650` | `right, right, right, right, right, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_21.json` | **2.19%** | `input: 27633 , ouput: 650` | `right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_21.txt` | **0.00%** | `input: 7730 , ouput: 650` | `down, down, right, right, right, right, down, down, down, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_21.txt` | **0.00%** | `input: 536 , ouput: 650` | `the, maze, solving, process, involves, systematically, exploring, the, paths, from, the, start, 's', to, the, end, 'e'., as, a, maze-solving, expert, i, will, trace, a, valid, path, avoiding, walls, '#', and, only, moving, horizontally, or, vertically., starting, at, (0, 1), i, will, move:, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_tokenized_21.txt` | **1.75%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_21.jpg`

**Score:** 0.88%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right, down, right, right, down, left, down, right, down, left, left, left, down, down, right, up, right, down, down, left, down, left, up, left, down, down, right, right, down, right, right, right, right, right, up, up, up, right, right, down, down, left, down, right, down, right, down, right, up, right, up, left, left, up, up, up, right, up, left, left, up, left, down, left, left, down, left, up, left, up, right, up, up, up, up, right, up, left, up, up, right, right, down, right, right, right, right, down, down, down, down, down, down, right, down, right, up, right, down, down, down, down, down, left, down, right, down
```

**Extracted Answer:**
```
right, down, down, right, down, down, right, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, down, down, right, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down, right, up, right, down, right, down, right, up, right, down, right, down, right, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='YaaUadDzKqeN7M8P04OMiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_21.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right, down, right, right, down, left, down, right, down, left, left, left, down, down, right, up, right, down, down, left, down, left, up, left, down, down, right, right, down, right, right, right, right, right, up, up, up, right, right, down, down, left, down, right, down, right, down, right, up, right, up, left, left, up, up, up, right, up, left, left, up, left, down, left, left, down, left, up, left, up, right, up, up, up, up, right, up, left, up, up, right, right, down, right, right, right, right, down, down, down, down, down, down, right, down, right, up, right, down, down, down, down, down, left, down, right, down
```

**Extracted Answer:**
```
down, down, right, right, right, down, right, down, right, right, down, right, down, down, down, right, down, right, right, down, right, right, down, right, right, down, right, down, right, right, down, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down, right, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,down,right,down,right,right,down,right,down,down,down,right,down,right,right,down,right,right,down,right,right,down,right,down,right,right,down,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,right,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Y6aUaYDqO8iOkdUPuavdqQI' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_21.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right, down, right, right, down, left, down, right, down, left, left, left, down, down, right, up, right, down, down, left, down, left, up, left, down, down, right, right, down, right, right, right, right, right, up, up, up, right, right, down, down, left, down, right, down, right, down, right, up, right, up, left, left, up, up, up, right, up, left, left, up, left, down, left, left, down, left, up, left, up, right, up, up, up, up, right, up, left, up, up, right, right, down, right, right, right, right, down, down, down, down, down, down, right, down, right, up, right, down, down, down, down, down, left, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='ZqaUaeG7OP3onsEP3cCnyQM' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=13488,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13488
    ),
  ],
  total_token_count=13488
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=13488 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13488
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13488 traffic_type=None
```

### `maze_line_15x15_adj_21.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right, down, right, right, down, left, down, right, down, left, left, left, down, down, right, up, right, down, down, left, down, left, up, left, down, down, right, right, down, right, right, right, right, right, up, up, up, right, right, down, down, left, down, right, down, right, down, right, up, right, up, left, left, up, up, up, right, up, left, left, up, left, down, left, left, down, left, up, left, up, right, up, up, up, up, right, up, left, up, up, right, right, down, right, right, right, right, down, down, down, down, down, down, right, down, right, up, right, down, down, down, down, down, left, down, right, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='aaaUaYXGJ8DzkdUPloGV4Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=3680,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3680
    ),
  ],
  total_token_count=3680
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=3680 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3680
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3680 traffic_type=None
```

### `maze_line_15x15_tokenized_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, left, left, down, right, right, down, right, right, down, left, down, right, down, left, left, left, down, down, right, up, right, down, down, left, down, left, up, left, down, down, right, right, down, right, right, right, right, right, up, up, up, right, right, down, down, left, down, right, down, right, down, right, up, right, up, left, left, up, up, up, right, up, left, left, up, left, down, left, left, down, left, up, left, up, right, up, up, up, up, right, up, left, up, up, right, right, down, right, right, right, right, down, down, down, down, down, down, right, down, right, up, right, down, down, down, down, down, left, down, right, down
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='a6aUadnBGL3ukdUPjeSHsAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3282,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3282
    ),
  ],
  total_token_count=3932
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3282 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3282
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3932 traffic_type=None
```

### `maze_occupancy_15x15_21.jpg`

**Score:** 0.88%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, down, right, down, down, right, down, right, down, down, right, down, right, right, down, right, down, down, right, down, right, down, down, right, right, down, down, right, down, right, right, down, down, down, right, down, right, down, right, down, down, right, down, right, down, right, down, down, right, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down, down, right, down, right, down, right, down, down, right, down, down, right, down, right, down, right, down, down, right, down, right, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,down,down,right,down,right,down,down,right,down,right,right,down,right,down,down,right,down,right,down,down,right,right,down,down,right,down,right,right,down,down,down,right,down,right,down,right,down,down,right,down,right,down,right,down,down,right,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,down,right,down,right,down,right,down,down,right,down,down,right,down,right,down,right,down,down,right,down,right,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='bqaUacrZC5S8nsEPnPGoiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_21.json`

**Score:** 1.75%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, down, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,down,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cKaUaebfCv27nsEPhr2MyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_21.json`

**Score:** 2.19%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='cqaUaafqD4minsEP87S6kAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27633,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27633
    ),
  ],
  total_token_count=28283
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27633 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27633
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28283 traffic_type=None
```

### `maze_occupancy_15x15_adj_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, down, down, down, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right, right, right, down, down, down, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,down,down,down,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,right,right,down,down,down,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='dKaUaYulA7-NkdUPkILV0AM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7730,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7730
    ),
  ],
  total_token_count=8380
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7730 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7730
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8380 traffic_type=None
```

### `maze_occupancy_15x15_ascii_21.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down
```

**Extracted Answer:**
```
the, maze, solving, process, involves, systematically, exploring, the, paths, from, the, start, 's', to, the, end, 'e'., as, a, maze-solving, expert, i, will, trace, a, valid, path, avoiding, walls, '#', and, only, moving, horizontally, or, vertically., starting, at, (0, 1), i, will, move:, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze solving process involves systematically exploring the paths from the start 'S' to the end 'E'. As a maze-solving expert, I will trace a valid path, avoiding walls '#' and only moving horizontally or vertically.

Starting at (0,1), I will move:
right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down,"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='daaUaeaeO8SzkdUP4ZaoqQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=536,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=536
    ),
  ],
  total_token_count=1186
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=536 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=536
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1186 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_21.txt`

**Score:** 1.75%

**Ground Truth Solution:**
```
right, right, right, right, down, down, left, left, left, left, down, down, right, right, right, right, down, down, right, right, right, right, down, down, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, down, down, left, left, down, down, left, left, up, up, left, left, down, down, down, down, right, right, right, right, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, left, left, down, down, right, right, down, down, right, right, down, down, right, right, up, up, right, right, up, up, left, left, left, left, up, up, up, up, up, up, right, right, up, up, left, left, left, left, up, up, left, left, down, down, left, left, left, left, down, down, left, left, up, up, left, left, up, up, right, right, up, up, up, up, up, up, up, up, right, right, up, up, left, left, up, up, up, up, right, right, right, right, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, right, right, down, down, right, right, up, up, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='d6aUafmpO_3onsEP3cCnyQM' usage_metadata=GenerateContentResponseUsageMetadata(
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

