# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_5.jpg` | **0.79%** | `input: 436 , ouput: 650` | `right, down, right, down, down, right, down, right, down, left, down, right, down, right, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, up, right, down, right, down, left, down, left, down, right, down, right, right, down, right, down, right, up, right, up, right, down, right, down, right, down, left, down, right, right, down, right, down, right, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right` |
| `maze_line_15x15_5.json` | **1.59%** | `input: 9807 , ouput: 650` | `right, right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right` |
| `maze_line_15x15_adj_5.json` | **3.17%** | `input: 13483 , ouput: 57` | `right, right, right, down, down, right, right, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_5.txt` | **3.97%** | `input: 3675 , ouput: 650` | `right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_5.txt` | **0.00%** | `input: 3282 , ouput: 650` | `the, maze, starts, at, (0, 0), and, ends, at, (14, 14)., (0, 0), <|origin|>, (0, 1), <|updown_wall|>, -, cannot, go, up, or, down, (1, 0), <|uprightleft_wall|>, -, cannot, go, right, or, left., must, go, down., move:, down, (1, 0), (1, 1), <|upleft_wall|>, -, cannot, go, up, or, left, (2, 0), <|left_wall|>, -, cannot, go, left, (0, 0), <|origin|>, -, already, visited, move:, down, (2, 0), (2, 1), <|downright_wall|>, -, cannot, go, down, or, right, (1, 0), <|uprightleft_wall|>, -, already, visited, (3, 0), <|downleft_wall|>, -, cannot, go, down, or, left, must, go, up., (2, 0), (1, 0), -, visited, (0, 0), -, visited, cannot, move, up, from, (2, 0)., let's, re-evaluate., start, at, (0, 0)., (0, 0), has, <|updownleft_wall|>, and, <|origin|>., can, only, go, right., move:, right, (0, 1), <|updown_wall|>, (0, 0), -, visited, (0, 2), <|updown_wall|>, must, go, right., move:, right, (0, 2), <|updown_wall|>, (0, 1), -, visited, (0, 3), <|updown_wall|>, must, go, right., move:, right, (0, 3), <|updown_wall|>, (0, 2), -, visited, (0, 4), <|upleft_wall|>, must, go, right., move:, right, (0, 4), <|upleft_wall|>, (0, 3), -, visited, (0, 5), <|upright_wall|>, must, go, right., move:, right, (0, 5), <|upright_wall|>, (0, 4), -, visited, (0, 6), <|updownleft_wall|>, must, go, right., move:, right, (0, 6), <|updownleft_wall|>, (0, 5), -, visited, (0, 7), <|updown_wall|>, must, go, right., move:, right, (0, 7), <|updown_wall|>, (0, 6), -, visited, (0, 8), <|updown_wall|>, must, go, right., move:, right, (0, 8), <|updown_wall|>, (0, 7), -, visited, (0, 9), <|up_wall|>, must, go, right., move:, right, (0, 9), <|up_wall|>, (0, 8), -, visited, (0, 10)` |
| `maze_occupancy_15x15_5.jpg` | **nan%** | `input: 431 , ouput: 0` | `` |
| `maze_occupancy_15x15_5.json` | **2.38%** | `input: 4246 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_5.json` | **2.38%** | `input: 27639 , ouput: 650` | `right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_15x15_adj_5.txt` | **0.00%** | `input: 7733 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_5.txt` | **0.00%** | `input: 527 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_5.txt` | **2.38%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |

---

## Full LLM Responses

### `maze_line_15x15_5.jpg`

**Score:** 0.79%

**Ground Truth Solution:**
```
right, right, right, down, right, up, right, down, right, right, right, down, left, left, down, left, left, up, left, left, up, left, down, left, down, right, down, down, down, down, down, left, down, right, right, down, right, right, right, up, left, up, left, left, up, up, right, up, up, right, right, right, down, right, right, up, up, right, right, right, right, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, left, down, left, up, up, left, down, left, left, left, down, down, down, left, left, down, right, down, left, left, left, down, right, right, right, right, right, up, up, up, right, up, up, right, down, down, right, right, up, right, right, up, right, down, down, down, left, down, down, right
```

**Extracted Answer:**
```
right, down, right, down, down, right, down, right, down, left, down, right, down, right, right, up, right, down, right, down, left, down, right, down, right, up, right, up, right, up, right, down, right, down, left, down, left, down, right, down, right, right, down, right, down, right, up, right, up, right, down, right, down, right, down, left, down, right, right, down, right, down, right, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right, right, down, right, down, right, down, left, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,down,right,down,right,down,left,down,right,down,right,right,up,right,down,right,down,left,down,right,down,right,up,right,up,right,up,right,down,right,down,left,down,left,down,right,down,right,right,down,right,down,right,up,right,up,right,down,right,down,right,down,left,down,right,right,down,right,down,right,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,right,down,right,down,right,down,left,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='QP0labKqJKijvdIPvcbN8A0' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_5.json`

**Score:** 1.59%

**Ground Truth Solution:**
```
right, right, right, down, right, up, right, down, right, right, right, down, left, left, down, left, left, up, left, left, up, left, down, left, down, right, down, down, down, down, down, left, down, right, right, down, right, right, right, up, left, up, left, left, up, up, right, up, up, right, right, right, down, right, right, up, up, right, right, right, right, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, left, down, left, up, up, left, down, left, left, left, down, down, down, left, left, down, right, down, left, left, left, down, right, right, right, right, right, up, up, up, right, up, up, right, down, down, right, right, up, right, right, up, right, down, down, down, left, down, down, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, down, down, down, down, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,down,down,down,down,down,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Q_0laeaVBMOFvdIPq8eRoAg' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_5.json`

**Score:** 3.17%

**Ground Truth Solution:**
```
right, right, right, down, right, up, right, down, right, right, right, down, left, left, down, left, left, up, left, left, up, left, down, left, down, right, down, down, down, down, down, left, down, right, right, down, right, right, right, up, left, up, left, left, up, up, right, up, up, right, right, right, down, right, right, up, up, right, right, right, right, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, left, down, left, up, up, left, down, left, left, left, down, down, down, left, left, down, right, down, left, left, left, down, right, right, right, right, right, up, up, up, right, up, up, right, down, down, right, right, up, right, right, up, right, down, down, down, left, down, down, right
```

**Extracted Answer:**
```
right, right, right, down, down, right, right, down, down, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,down,right,right,down,down,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='RP0lacLXAqTCvdIPwej94A0' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=57,
  prompt_token_count=13483,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13483
    ),
  ],
  total_token_count=13540
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=57 candidates_tokens_details=None prompt_token_count=13483 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13483
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=13540 traffic_type=None
```

### `maze_line_15x15_adj_5.txt`

**Score:** 3.97%

**Ground Truth Solution:**
```
right, right, right, down, right, up, right, down, right, right, right, down, left, left, down, left, left, up, left, left, up, left, down, left, down, right, down, down, down, down, down, left, down, right, right, down, right, right, right, up, left, up, left, left, up, up, right, up, up, right, right, right, down, right, right, up, up, right, right, right, right, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, left, down, left, up, up, left, down, left, left, left, down, down, down, left, left, down, right, down, left, left, left, down, right, right, right, right, right, up, up, up, right, up, up, right, down, down, right, right, up, right, right, up, right, down, down, down, left, down, down, right
```

**Extracted Answer:**
```
right, right, right, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Rv0lafbmOuu_vdIP9tzPYA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3675,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3675
    ),
  ],
  total_token_count=4325
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3675 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3675
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4325 traffic_type=None
```

### `maze_line_15x15_tokenized_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, down, right, up, right, down, right, right, right, down, left, left, down, left, left, up, left, left, up, left, down, left, down, right, down, down, down, down, down, left, down, right, right, down, right, right, right, up, left, up, left, left, up, up, right, up, up, right, right, right, down, right, right, up, up, right, right, right, right, up, up, up, right, right, down, down, down, down, down, down, down, down, left, left, left, down, left, up, up, left, down, left, left, left, down, down, down, left, left, down, right, down, left, left, left, down, right, right, right, right, right, up, up, up, right, up, up, right, down, down, right, right, up, right, right, up, right, down, down, down, left, down, down, right
```

**Extracted Answer:**
```
the, maze, starts, at, (0, 0), and, ends, at, (14, 14)., (0, 0), <|origin|>, (0, 1), <|updown_wall|>, -, cannot, go, up, or, down, (1, 0), <|uprightleft_wall|>, -, cannot, go, right, or, left., must, go, down., move:, down, (1, 0), (1, 1), <|upleft_wall|>, -, cannot, go, up, or, left, (2, 0), <|left_wall|>, -, cannot, go, left, (0, 0), <|origin|>, -, already, visited, move:, down, (2, 0), (2, 1), <|downright_wall|>, -, cannot, go, down, or, right, (1, 0), <|uprightleft_wall|>, -, already, visited, (3, 0), <|downleft_wall|>, -, cannot, go, down, or, left, must, go, up., (2, 0), (1, 0), -, visited, (0, 0), -, visited, cannot, move, up, from, (2, 0)., let's, re-evaluate., start, at, (0, 0)., (0, 0), has, <|updownleft_wall|>, and, <|origin|>., can, only, go, right., move:, right, (0, 1), <|updown_wall|>, (0, 0), -, visited, (0, 2), <|updown_wall|>, must, go, right., move:, right, (0, 2), <|updown_wall|>, (0, 1), -, visited, (0, 3), <|updown_wall|>, must, go, right., move:, right, (0, 3), <|updown_wall|>, (0, 2), -, visited, (0, 4), <|upleft_wall|>, must, go, right., move:, right, (0, 4), <|upleft_wall|>, (0, 3), -, visited, (0, 5), <|upright_wall|>, must, go, right., move:, right, (0, 5), <|upright_wall|>, (0, 4), -, visited, (0, 6), <|updownleft_wall|>, must, go, right., move:, right, (0, 6), <|updownleft_wall|>, (0, 5), -, visited, (0, 7), <|updown_wall|>, must, go, right., move:, right, (0, 7), <|updown_wall|>, (0, 6), -, visited, (0, 8), <|updown_wall|>, must, go, right., move:, right, (0, 8), <|updown_wall|>, (0, 7), -, visited, (0, 9), <|up_wall|>, must, go, right., move:, right, (0, 9), <|up_wall|>, (0, 8), -, visited, (0, 10)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The maze starts at (0,0) and ends at (14,14).

(0,0) <|origin|>
(0,1) <|updown_wall|> - cannot go up or down
(1,0) <|uprightleft_wall|> - cannot go right or left. Must go down.
Move: down

(1,0)
(1,1) <|upleft_wall|> - cannot go up or left
(2,0) <|left_wall|> - cannot go left
(0,0) <|origin|> - already visited
Move: down

(2,0)
(2,1) <|downright_wall|> - cannot go down or right
(1,0) <|uprightleft_wall|> - already visited
(3,0) <|downleft_wall|> - cannot go down or left
Must go up.

(2,0)
(1,0) - visited
(0,0) - visited
Cannot move up from (2,0). Let's re-evaluate.

Start at (0,0).
(0,0) has <|updownleft_wall|> and <|origin|>. Can only go right.
Move: right

(0,1) <|updown_wall|>
(0,0) - visited
(0,2) <|updown_wall|>
Must go right.
Move: right

(0,2) <|updown_wall|>
(0,1) - visited
(0,3) <|updown_wall|>
Must go right.
Move: right

(0,3) <|updown_wall|>
(0,2) - visited
(0,4) <|upleft_wall|>
Must go right.
Move: right

(0,4) <|upleft_wall|>
(0,3) - visited
(0,5) <|upright_wall|>
Must go right.
Move: right

(0,5) <|upright_wall|>
(0,4) - visited
(0,6) <|updownleft_wall|>
Must go right.
Move: right

(0,6) <|updownleft_wall|>
(0,5) - visited
(0,7) <|updown_wall|>
Must go right.
Move: right

(0,7) <|updown_wall|>
(0,6) - visited
(0,8) <|updown_wall|>
Must go right.
Move: right

(0,8) <|updown_wall|>
(0,7) - visited
(0,9) <|up_wall|>
Must go right.
Move: right

(0,9) <|up_wall|>
(0,8) - visited
(0,10)"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Sf0ladm5HoDDvdIPqKaxkA4' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_5.jpg`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, up, up, left, left, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, left, left, up, up, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Tf0laYWLIbnaxs0P9PfZiA8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_5.json`

**Score:** 2.38%

**Ground Truth Solution:**
```
right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, up, up, left, left, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, left, left, up, up, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Uf0laaKaBNbsxN8PltXK-AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_adj_5.json`

**Score:** 2.38%

**Ground Truth Solution:**
```
right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, up, up, left, left, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, left, left, up, up, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VP0lafX3J8OFvdIPq8eRoAg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27639,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27639
    ),
  ],
  total_token_count=28289
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27639 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27639
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28289 traffic_type=None
```

### `maze_occupancy_15x15_adj_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, up, up, left, left, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, left, left, up, up, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='V_0lab-hF4DDvdIPqKaxkA4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=7733,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=7733
    ),
  ],
  total_token_count=8383
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=7733 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=7733
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=8383 traffic_type=None
```

### `maze_occupancy_15x15_ascii_5.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, up, up, left, left, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, left, left, up, up, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='Wv0lad3FCZfYxs0P243yYA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=527,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=527
    ),
  ],
  total_token_count=1177
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=527 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=527
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1177 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_5.txt`

**Score:** 2.38%

**Ground Truth Solution:**
```
right, right, right, right, right, right, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, down, down, left, left, left, left, down, down, left, left, left, left, up, up, left, left, left, left, up, up, left, left, down, down, left, left, down, down, right, right, down, down, down, down, down, down, down, down, down, down, left, left, down, down, right, right, right, right, down, down, right, right, right, right, right, right, up, up, left, left, up, up, left, left, left, left, up, up, up, up, right, right, up, up, up, up, right, right, right, right, right, right, down, down, right, right, right, right, up, up, up, up, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, left, left, down, down, down, down, down, down, left, left, left, left, down, down, right, right, down, down, left, left, left, left, left, left, down, down, right, right, right, right, right, right, right, right, right, right, up, up, up, up, up, up, right, right, up, up, up, up, right, right, down, down, down, down, right, right, right, right, up, up, right, right, right, right, up, up, right, right, down, down, down, down, down, down, left, left, down, down, down, down, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='XP0labWmOfmkvdIPpNW50AY' usage_metadata=GenerateContentResponseUsageMetadata(
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

