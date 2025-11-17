# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_3.jpg` | **0.00%** | `input: 531 , ouput: 15` | `right, forward, forward, right, forward, forward, right, forward` |
| `maze_line_3x3_3.json` | **0.00%** | `input: 754 , ouput: 13` | `right, forward, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_3.json` | **25.00%** | `input: 816 , ouput: 11` | `forward, forward, right, forward, right, forward` |
| `maze_line_3x3_adj_3.txt` | **0.00%** | `input: 448 , ouput: 13` | `right, forward, right, forward, forward, left, forward` |
| `maze_line_3x3_tokenized_3.txt` | **0.00%** | `input: 419 , ouput: 17` | `right, forward, right, forward, right, forward, right, forward, forward` |
| `maze_occupancy_3x3_3.jpg` | **12.50%** | `input: 526 , ouput: 33` | `forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward` |
| `maze_occupancy_3x3_3.json` | **0.00%** | `input: 569 , ouput: 79` | `right, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, right, forward` |
| `maze_occupancy_3x3_adj_3.json` | **12.50%** | `input: 1278 , ouput: 31` | `forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_3x3_adj_3.txt` | **0.00%** | `input: 560 , ouput: 4000` | `right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left` |
| `maze_occupancy_3x3_ascii_3.txt` | **0.00%** | `input: 295 , ouput: 4000` | `right, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward` |
| `maze_occupancy_3x3_tokenized_3.txt` | **0.00%** | `input: 848 , ouput: 1029` | `the, agent, starts, at, (1, 1), facing, an, unknown, direction., based, on, the, maze, layout, it, is, likely, facing, right, (towards, (1, 2), which, is, occupied, by, a, wall)., to, navigate, the, agent, needs, to, move, around, the, central, occupied, columns., let's, assume, the, agent, starts, facing, right., 1., **(1, 1), to, (1, 3):**, the, agent, needs, to, move, from, (1, 1), to, (1, 3)., *, `forward`, (moves, to, (1, 2), which, is, a, wall., this, implies, the, agent, must, not, be, facing, right., let's, re-evaluate.), let's, assume, the, agent, starts, at, (1, 1), and, must, move, to, an, accessible, cell., the, adjacent, accessible, cells, are, (1, 3), (2, 1), (3, 1)., the, target, is, at, (5, 5)., let's, assume, the, agent, starts, facing, right., *, at, (1, 1), adjacent, to, <|origin|>., *, target, is, <|target|>, at, (5, 5)., the, accessible, path, seems, to, be:, (1, 1), ->, (1, 3), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), ->, (5, 5), let's, try, to, plot, a, path, from, (1, 1), to, (5, 5)., assuming, the, agent, starts, at, (1, 1), and, facing, right., 1., `forward`, -, this, would, move, to, (1, 2), which, is, <|occupied_wall|>., so, the, agent, must, not, be, facing, right., let's, assume, the, agent, starts, at, (1, 1), and, facing, down., 1., `forward`, -, moves, to, (2, 1)., 2., `forward`, -, moves, to, (3, 1)., 3., `right`, -, turns, to, face, right., 4., `forward`, -, moves, to, (3, 2)., 5., `forward`, -, moves, to, (3, 3)., 6., `forward`, -, moves, to, (3, 4)., 7., `forward`, -, moves, to, (3, 5)., 8., `right`, -, turns, to, face, right., 9., `forward`, -, moves, to, (4, 5)., 10., `forward`, -, moves, to, (5, 5), -, target!, let's, check, if, there's, a, more, direct, path, assuming, the, agent, can, start, facing, any, direction., the, most, logical, starting, direction, for, a, path, to, be, immediately, accessible, is, facing, towards, an, adjacent, blank, space., from, (1, 1), the, blank, spaces, are, (1, 3), (2, 1), (3, 1)., however, (1, 3), is, blocked, by, a, wall, at, (1, 2)., so, the, agent, must, be, facing, either, down, or, diagonally, down-left., since, diagonal, moves, are, not, allowed, it, must, be, facing, down., so, assuming, agent, starts, at, (1, 1), facing, down:, 1., `forward`, (moves, to, 2, 1), 2., `forward`, (moves, to, 3, 1), 3., `right`, (now, facing, right), 4., `forward`, (moves, to, 3, 2), 5., `forward`, (moves, to, 3, 3), 6., `forward`, (moves, to, 3, 4), 7., `forward`, (moves, to, 3, 5), 8., `right`, (now, facing, right, but, it's, already, at, the, rightmost, edge, of, this, horizontal, path., this, is, not, correct., let's, retrace., the, path, is, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), ->, (5, 5)., let's, try, again, from, (1, 1), facing, down:, 1., `forward`, (at, 2, 1), 2., `forward`, (at, 3, 1), 3., `right`, (facing, right), 4., `forward`, (at, 3, 2), 5., `forward`, (at, 3, 3), 6., `forward`, (at, 3, 4), 7., `forward`, (at, 3, 5), 8., `right`, (facing, right., now, at, 3, 5., next, step, should, be, towards, (4, 5)., so, facing, right, is, correct), 9., `forward`, (at, 4, 5), 10., `forward`, (at, 5, 5), -, target., this, sequence, seems, correct., forward, forward, right, forward, forward, forward, forward, right, forward, forward` |

---

## Full LLM Responses

### `maze_line_3x3_3.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qLwVaYzJFr_onsEPwuTD0Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=15,
  prompt_token_count=531,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=273
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=546
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=531 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=15 candidates_tokens_details=None prompt_token_count=531 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=273
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=546 traffic_type=None
```

### `maze_line_3x3_3.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, right, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qLwVadzKL9_4nsEPhqmbOA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=754,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=754
    ),
  ],
  total_token_count=767
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=754 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=754
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=767 traffic_type=None
```

### `maze_line_3x3_adj_3.json`

**Score:** 25.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Forward,forward,right,forward,right,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qbwVaavbF8DjnsEPs7PoMQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=11,
  prompt_token_count=816,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=816
    ),
  ],
  total_token_count=827
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=260 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=11 candidates_tokens_details=None prompt_token_count=816 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=816
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=827 traffic_type=None
```

### `maze_line_3x3_adj_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Left, Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qbwVaf6tMPuSkdUPt_Ge2Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=13,
  prompt_token_count=448,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=448
    ),
  ],
  total_token_count=461
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=293 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=13 candidates_tokens_details=None prompt_token_count=448 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=448
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=461 traffic_type=None
```

### `maze_line_3x3_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, left, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, right, forward, right, forward, right, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qrwVaeKoE83xnsEPm_61-Q4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
  prompt_token_count=419,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=419
    ),
  ],
  total_token_count=436
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=291 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=419 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=419
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=436 traffic_type=None
```

### `maze_occupancy_3x3_3.jpg`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,right,forward,forward,right,forward,forward,forward,left,forward,forward,left,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='qrwVad-jPJj6nsEPgKnRwQo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=33,
  prompt_token_count=526,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=268
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=559
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=526 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=33 candidates_tokens_details=None prompt_token_count=526 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=268
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=559 traffic_type=None
```

### `maze_occupancy_3x3_3.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, right, forward, forward, left, forward, left, forward, forward, right, forward, forward, right, forward, left, forward, forward, forward, right, forward, forward, forward, left, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Right,Forward,Forward,Right,Forward,Forward,Left,Forward,Left,Forward,Forward,Right,Forward,Forward,Right,Forward,Left,Forward,Forward,Forward,Right,Forward,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Left,Forward,Forward,Forward,Right,Forward,Right,Forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='q7wVae7pJLz7nsEPh7viEA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=79,
  prompt_token_count=569,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=569
    ),
  ],
  total_token_count=648
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=269 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=79 candidates_tokens_details=None prompt_token_count=569 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=569
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=648 traffic_type=None
```

### `maze_occupancy_3x3_adj_3.json`

**Score:** 12.50%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward,right,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='rLwVafv2EaKckdUPwuS40A4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=31,
  prompt_token_count=1278,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1278
    ),
  ],
  total_token_count=1309
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=260 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=31 candidates_tokens_details=None prompt_token_count=1278 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1278
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1309 traffic_type=None
```

### `maze_occupancy_3x3_adj_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tbwVaaugFKOVkdUP8anpKA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=4000,
  prompt_token_count=560,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=560
    ),
  ],
  total_token_count=4560
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=293 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=4000 candidates_tokens_details=None prompt_token_count=560 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=560
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4560 traffic_type=None
```

### `maze_occupancy_3x3_ascii_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, right, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=255,
        license='',
        start_index=52,
        uri='https://github.com/LiardeauxQ/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Forward,Left,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,Forward,Forward,Forward,Forward,Forward,Right,Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='vrwVabPWK5HMnsEPs6ygCA' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=4000,
  prompt_token_count=295,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=295
    ),
  ],
  total_token_count=4295
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=268 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=4000 candidates_tokens_details=None prompt_token_count=295 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=295
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4295 traffic_type=None
```

### `maze_occupancy_3x3_tokenized_3.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
forward, forward, left, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
the, agent, starts, at, (1, 1), facing, an, unknown, direction., based, on, the, maze, layout, it, is, likely, facing, right, (towards, (1, 2), which, is, occupied, by, a, wall)., to, navigate, the, agent, needs, to, move, around, the, central, occupied, columns., let's, assume, the, agent, starts, facing, right., 1., **(1, 1), to, (1, 3):**, the, agent, needs, to, move, from, (1, 1), to, (1, 3)., *, `forward`, (moves, to, (1, 2), which, is, a, wall., this, implies, the, agent, must, not, be, facing, right., let's, re-evaluate.), let's, assume, the, agent, starts, at, (1, 1), and, must, move, to, an, accessible, cell., the, adjacent, accessible, cells, are, (1, 3), (2, 1), (3, 1)., the, target, is, at, (5, 5)., let's, assume, the, agent, starts, facing, right., *, at, (1, 1), adjacent, to, <|origin|>., *, target, is, <|target|>, at, (5, 5)., the, accessible, path, seems, to, be:, (1, 1), ->, (1, 3), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), ->, (5, 5), let's, try, to, plot, a, path, from, (1, 1), to, (5, 5)., assuming, the, agent, starts, at, (1, 1), and, facing, right., 1., `forward`, -, this, would, move, to, (1, 2), which, is, <|occupied_wall|>., so, the, agent, must, not, be, facing, right., let's, assume, the, agent, starts, at, (1, 1), and, facing, down., 1., `forward`, -, moves, to, (2, 1)., 2., `forward`, -, moves, to, (3, 1)., 3., `right`, -, turns, to, face, right., 4., `forward`, -, moves, to, (3, 2)., 5., `forward`, -, moves, to, (3, 3)., 6., `forward`, -, moves, to, (3, 4)., 7., `forward`, -, moves, to, (3, 5)., 8., `right`, -, turns, to, face, right., 9., `forward`, -, moves, to, (4, 5)., 10., `forward`, -, moves, to, (5, 5), -, target!, let's, check, if, there's, a, more, direct, path, assuming, the, agent, can, start, facing, any, direction., the, most, logical, starting, direction, for, a, path, to, be, immediately, accessible, is, facing, towards, an, adjacent, blank, space., from, (1, 1), the, blank, spaces, are, (1, 3), (2, 1), (3, 1)., however, (1, 3), is, blocked, by, a, wall, at, (1, 2)., so, the, agent, must, be, facing, either, down, or, diagonally, down-left., since, diagonal, moves, are, not, allowed, it, must, be, facing, down., so, assuming, agent, starts, at, (1, 1), facing, down:, 1., `forward`, (moves, to, 2, 1), 2., `forward`, (moves, to, 3, 1), 3., `right`, (now, facing, right), 4., `forward`, (moves, to, 3, 2), 5., `forward`, (moves, to, 3, 3), 6., `forward`, (moves, to, 3, 4), 7., `forward`, (moves, to, 3, 5), 8., `right`, (now, facing, right, but, it's, already, at, the, rightmost, edge, of, this, horizontal, path., this, is, not, correct., let's, retrace., the, path, is, (1, 1), ->, (2, 1), ->, (3, 1), ->, (3, 2), ->, (3, 3), ->, (3, 4), ->, (3, 5), ->, (4, 5), ->, (5, 5)., let's, try, again, from, (1, 1), facing, down:, 1., `forward`, (at, 2, 1), 2., `forward`, (at, 3, 1), 3., `right`, (facing, right), 4., `forward`, (at, 3, 2), 5., `forward`, (at, 3, 3), 6., `forward`, (at, 3, 4), 7., `forward`, (at, 3, 5), 8., `right`, (facing, right., now, at, 3, 5., next, step, should, be, towards, (4, 5)., so, facing, right, is, correct), 9., `forward`, (at, 4, 5), 10., `forward`, (at, 5, 5), -, target., this, sequence, seems, correct., forward, forward, right, forward, forward, forward, forward, right, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""The agent starts at (1,1) facing an unknown direction. Based on the maze layout, it is likely facing right (towards (1,2) which is occupied by a wall). To navigate, the agent needs to move around the central occupied columns.

Let's assume the agent starts facing right.

1. **(1,1) to (1,3):** The agent needs to move from (1,1) to (1,3).
   * `forward` (moves to (1,2), which is a wall. This implies the agent must not be facing right. Let's re-evaluate.)

Let's assume the agent starts at (1,1) and must move to an accessible cell. The adjacent accessible cells are (1,3), (2,1), (3,1). The target is at (5,5).

Let's assume the agent starts facing right.
* At (1,1), adjacent to <|origin|>.
* Target is <|target|> at (5,5).

The accessible path seems to be:
(1,1) -> (1,3) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (4,5) -> (5,5)

Let's try to plot a path from (1,1) to (5,5).

Assuming the agent starts at (1,1) and facing right.
1. `forward` - This would move to (1,2) which is <|occupied_wall|>. So the agent must not be facing right.

Let's assume the agent starts at (1,1) and facing down.
1. `forward` - moves to (2,1).
2. `forward` - moves to (3,1).
3. `right` - turns to face right.
4. `forward` - moves to (3,2).
5. `forward` - moves to (3,3).
6. `forward` - moves to (3,4).
7. `forward` - moves to (3,5).
8. `right` - turns to face right.
9. `forward` - moves to (4,5).
10. `forward` - moves to (5,5) - Target!

Let's check if there's a more direct path assuming the agent can start facing any direction.

The most logical starting direction for a path to be immediately accessible is facing towards an adjacent blank space. From (1,1), the blank spaces are (1,3), (2,1), (3,1). However, (1,3) is blocked by a wall at (1,2). So the agent must be facing either down or diagonally down-left. Since diagonal moves are not allowed, it must be facing down.

So, assuming agent starts at (1,1) facing down:
1. `forward` (moves to 2,1)
2. `forward` (moves to 3,1)
3. `right` (now facing right)
4. `forward` (moves to 3,2)
5. `forward` (moves to 3,3)
6. `forward` (moves to 3,4)
7. `forward` (moves to 3,5)
8. `right` (now facing right, but it's already at the rightmost edge of this horizontal path. This is not correct. Let's retrace.

The path is (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3) -> (3,4) -> (3,5) -> (4,5) -> (5,5).

Let's try again from (1,1) facing down:
1. `forward` (at 2,1)
2. `forward` (at 3,1)
3. `right` (facing right)
4. `forward` (at 3,2)
5. `forward` (at 3,3)
6. `forward` (at 3,4)
7. `forward` (at 3,5)
8. `right` (facing right. Now at 3,5. Next step should be towards (4,5). So facing right is correct)
9. `forward` (at 4,5)
10. `forward` (at 5,5) - Target.

This sequence seems correct.

forward,forward,right,forward,forward,forward,forward,right,forward,forward"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='wrwVaZXpL_3rnsEP5rCeSQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=1029,
  prompt_token_count=848,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=848
    ),
  ],
  total_token_count=1877
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=293 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=1029 candidates_tokens_details=None prompt_token_count=848 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=848
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1877 traffic_type=None
```

