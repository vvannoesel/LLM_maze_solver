# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_26.jpg` | **0.00%** | `input: 551 , ouput: 650` | `right, forward, forward, right, forward, forward, left, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right` |
| `maze_line_6x6_26.json` | **0.00%** | `input: 1926 , ouput: 107` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward` |
| `maze_line_6x6_adj_26.json` | **0.00%** | `input: 2375 , ouput: 51` | `right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_line_6x6_adj_26.txt` | **0.00%** | `input: 846 , ouput: 650` | `the, agent, starts, at, (0, 0), facing, south., here's, a, possible, path:, the, agent, needs, to, get, to, (5, 5)., 1., **start, at, (0, 0), facing, south.**, 2., move, south, to, (1, 0)., (forward), 3., move, south, to, (2, 0)., (forward), 4., move, south, to, (3, 0)., (forward), 5., move, east, to, (3, 1)., (right), 6., move, south, to, (4, 1)., (forward), 7., move, east, to, (4, 2)., (forward), 8., move, east, to, (4, 3)., (forward), 9., move, east, to, (4, 4)., (forward), 10., move, east, to, (4, 5)., (forward), 11., move, south, to, (5, 5)., (forward), however, the, prompt, doesn't, list, all, connections., let's, re-examine, the, provided, adjacency, list., okay, let's, plan, a, path, using, the, given, adjacency, list:, the, agent, starts, at, (0, 0), facing, south., 1., **(0, 0), facing, south**, ->, move, to, (1, 0), (forward), 2., **(1, 0), facing, south**, ->, move, to, (2, 0), (forward), 3., **(2, 0), facing, south**, ->, move, to, (2, 1), (right), 4., **(2, 1), facing, east**, ->, move, to, (3, 1), (forward), 5., **(3, 1), facing, east**, ->, move, to, (3, 0), (left), 6., **(3, 0), facing, north**, ->, move, to, (4, 0), (forward), 7., **(4, 0), facing, north**, ->, move, to, (5, 0), (forward), 8., **(5, 0), facing, north**, ->, move, to, (5, 1), (right), 9., **(5, 1), facing, east**, ->, move, to, (5, 2), (forward), 10., **(5, 2), facing, east**, ->, move, to, (4, 2), (left), 11., **(4, 2), facing, north**, ->, move, to, (4, 1), (left), 12., **(4, 1), facing, west**, ->, move, to, (4, 0), (forward), 13., **(4, 0), facing, west**, ->, move, to, (3, 0), (forward), 14., **(3, 0), facing, west**, ->, move, to, (2, 0), (forward), 15., **(2, 0), facing, west**, ->, move, to, (1, 0), (forward), 16., **(1, 0), facing, west**, ->, move, to, (0, 0), (forward), 17., **(0, 0), facing, west**, ->, move, to, (0, 1), (right), 18., **(0, 1), facing, north` |
| `maze_line_6x6_tokenized_26.txt` | **0.00%** | `input: 790 , ouput: 650` | `right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward` |
| `maze_occupancy_6x6_26.jpg` | **0.00%** | `input: 548 , ouput: 650` | `right, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward` |
| `maze_occupancy_6x6_26.json` | **0.00%** | `input: 1105 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward` |
| `maze_occupancy_6x6_adj_26.json` | **0.00%** | `input: 4459 , ouput: 650` | `right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right` |
| `maze_occupancy_6x6_adj_26.txt` | **0.00%** | `input: 1395 , ouput: 650` | `right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right` |
| `maze_occupancy_6x6_ascii_26.txt` | **0.00%** | `input: 364 , ouput: 650` | `right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward` |
| `maze_occupancy_6x6_tokenized_26.txt` | **0.00%** | `input: 2279 , ouput: 650` | `forward, right, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right` |

---

## Full LLM Responses

### `maze_line_6x6_26.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, left, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, right, forward, forward, left, forward, forward, right, forward, right, forward, forward, forward, right, forward, forward, left, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right, forward, forward, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='SomVadHgPNKwxN8PyNH2gQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
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
  total_token_count=1201
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=551 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=293
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1201 traffic_type=None
```

### `maze_line_6x6_26.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TImVadanDoaSxN8P5cLTkAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=107,
  prompt_token_count=1926,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1926
    ),
  ],
  total_token_count=2033
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=107 candidates_tokens_details=None prompt_token_count=1926 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1926
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2033 traffic_type=None
```

### `maze_line_6x6_adj_26.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
right, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='TYmVacv3AsPgvdIP96mU8Qw' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=51,
  prompt_token_count=2375,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2375
    ),
  ],
  total_token_count=2426
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=51 candidates_tokens_details=None prompt_token_count=2375 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2375
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2426 traffic_type=None
```

### `maze_line_6x6_adj_26.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
the, agent, starts, at, (0, 0), facing, south., here's, a, possible, path:, the, agent, needs, to, get, to, (5, 5)., 1., **start, at, (0, 0), facing, south.**, 2., move, south, to, (1, 0)., (forward), 3., move, south, to, (2, 0)., (forward), 4., move, south, to, (3, 0)., (forward), 5., move, east, to, (3, 1)., (right), 6., move, south, to, (4, 1)., (forward), 7., move, east, to, (4, 2)., (forward), 8., move, east, to, (4, 3)., (forward), 9., move, east, to, (4, 4)., (forward), 10., move, east, to, (4, 5)., (forward), 11., move, south, to, (5, 5)., (forward), however, the, prompt, doesn't, list, all, connections., let's, re-examine, the, provided, adjacency, list., okay, let's, plan, a, path, using, the, given, adjacency, list:, the, agent, starts, at, (0, 0), facing, south., 1., **(0, 0), facing, south**, ->, move, to, (1, 0), (forward), 2., **(1, 0), facing, south**, ->, move, to, (2, 0), (forward), 3., **(2, 0), facing, south**, ->, move, to, (2, 1), (right), 4., **(2, 1), facing, east**, ->, move, to, (3, 1), (forward), 5., **(3, 1), facing, east**, ->, move, to, (3, 0), (left), 6., **(3, 0), facing, north**, ->, move, to, (4, 0), (forward), 7., **(4, 0), facing, north**, ->, move, to, (5, 0), (forward), 8., **(5, 0), facing, north**, ->, move, to, (5, 1), (right), 9., **(5, 1), facing, east**, ->, move, to, (5, 2), (forward), 10., **(5, 2), facing, east**, ->, move, to, (4, 2), (left), 11., **(4, 2), facing, north**, ->, move, to, (4, 1), (left), 12., **(4, 1), facing, west**, ->, move, to, (4, 0), (forward), 13., **(4, 0), facing, west**, ->, move, to, (3, 0), (forward), 14., **(3, 0), facing, west**, ->, move, to, (2, 0), (forward), 15., **(2, 0), facing, west**, ->, move, to, (1, 0), (forward), 16., **(1, 0), facing, west**, ->, move, to, (0, 0), (forward), 17., **(0, 0), facing, west**, ->, move, to, (0, 1), (right), 18., **(0, 1), facing, north
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

Here's a possible path:
The agent needs to get to (5,5).

1. **Start at (0,0), facing South.**
2. Move South to (1,0). (forward)
3. Move South to (2,0). (forward)
4. Move South to (3,0). (forward)
5. Move East to (3,1). (right)
6. Move South to (4,1). (forward)
7. Move East to (4,2). (forward)
8. Move East to (4,3). (forward)
9. Move East to (4,4). (forward)
10. Move East to (4,5). (forward)
11. Move South to (5,5). (forward)

However, the prompt doesn't list all connections. Let's re-examine the provided adjacency list.

Okay, let's plan a path using the given adjacency list:

The agent starts at (0,0) facing South.

1. **(0,0) facing South** -> Move to (1,0) (forward)
2. **(1,0) facing South** -> Move to (2,0) (forward)
3. **(2,0) facing South** -> Move to (2,1) (right)
4. **(2,1) facing East** -> Move to (3,1) (forward)
5. **(3,1) facing East** -> Move to (3,0) (left)
6. **(3,0) facing North** -> Move to (4,0) (forward)
7. **(4,0) facing North** -> Move to (5,0) (forward)
8. **(5,0) facing North** -> Move to (5,1) (right)
9. **(5,1) facing East** -> Move to (5,2) (forward)
10. **(5,2) facing East** -> Move to (4,2) (left)
11. **(4,2) facing North** -> Move to (4,1) (left)
12. **(4,1) facing West** -> Move to (4,0) (forward)
13. **(4,0) facing West** -> Move to (3,0) (forward)
14. **(3,0) facing West** -> Move to (2,0) (forward)
15. **(2,0) facing West** -> Move to (1,0) (forward)
16. **(1,0) facing West** -> Move to (0,0) (forward)
17. **(0,0) facing West** -> Move to (0,1) (right)
18. **(0,1) facing North"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='T4mVabOHEJXIvdIP-oyG2AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=846,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=846
    ),
  ],
  total_token_count=1496
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=846 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=846
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1496 traffic_type=None
```

### `maze_line_6x6_tokenized_26.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, right, right, left, left, right, right, left, forward, left, forward, left, right, forward, forward, right
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='UImVabObL9qb28oPgemZoQg' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=790,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=790
    ),
  ],
  total_token_count=1440
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=790 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=790
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1440 traffic_type=None
```

### `maze_occupancy_6x6_26.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward, forward, forward, forward, left, forward, forward, left, forward, forward, forward, forward, right, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,forward,right,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,forward,forward,forward,left,forward,forward,left,forward,forward,forward,forward,right,forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='U4mVabSHCKbTvdIP79ai6Ao' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=548,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=290
    ),
    ModalityTokenCount(
      modality=<MediaModality.IMAGE: 'IMAGE'>,
      token_count=258
    ),
  ],
  total_token_count=1198
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=548 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=548 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=290
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1198 traffic_type=None
```

### `maze_occupancy_6x6_26.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward, right, forward, forward, forward, forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VImVaeiBKt--xN8Puvy7kAo' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1105,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1105
    ),
  ],
  total_token_count=1755
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1105 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1105
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1755 traffic_type=None
```

### `maze_occupancy_6x6_adj_26.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2544,
        license='',
        start_index=0,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='VomVaYmWKozLvdIP8raG-Qs' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4459,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4459
    ),
  ],
  total_token_count=5109
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=282 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4459 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4459
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=5109 traffic_type=None
```

### `maze_occupancy_6x6_adj_26.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right, Forward, Right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WImVafbKC_6o28oPm8yLkQI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1395,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1395
    ),
  ],
  total_token_count=2045
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=315 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1395 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1395
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2045 traffic_type=None
```

### `maze_occupancy_6x6_ascii_26.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
right, forward, forward, right, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, right, forward, forward, forward, forward, forward, forward, forward, forward, forward, left, forward, forward, forward, forward, forward, forward, forward, forward, forward
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=2839,
        license='',
        start_index=160,
        uri='https://github.com/lucashlz/Zappy'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='Right, Forward, Forward, Right, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Right, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Left, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward, Forward,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='WYmVaZK7JbPUvdIPi6LC6QU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=364,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=364
    ),
  ],
  total_token_count=1014
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=290 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=364 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=364
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1014 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_26.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
left, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, left, forward, forward, forward, left, forward, forward, forward, left, forward, right, forward, forward, forward, forward, forward, right, forward
```

**Extracted Answer:**
```
forward, right, forward, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, left, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right, forward, right, forward, right, forward, right, forward, right, forward, right, forward, left, forward, left, forward, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='forward,right,forward,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,left,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,forward,right,forward,right,forward,right,forward,right,forward,right,forward,left,forward,left,forward,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='W4mVafCsBLT4xs0P_M6xgA8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=2279,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2279
    ),
  ],
  total_token_count=2929
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=314 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=2279 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2279
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2929 traffic_type=None
```

