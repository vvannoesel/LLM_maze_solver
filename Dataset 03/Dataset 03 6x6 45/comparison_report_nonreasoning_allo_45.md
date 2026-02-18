# LLM Maze Solving Comparison Report

**Maze Dimensions:** 6x6
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_6x6_45.jpg` | **15.00%** | `input: 434 , ouput: 17` | `right, down, right, down, right, down, right, down, right` |
| `maze_line_6x6_45.json` | **0.00%** | `input: 1809 , ouput: 23` | `down, down, right, right, down, down, right, down, right, right, down, right` |
| `maze_line_6x6_adj_45.json` | **10.00%** | `input: 2258 , ouput: 35` | `right, down, down, right, right, right, down, down, down, right, right, down, down, right, right, down, down, right` |
| `maze_line_6x6_adj_45.txt` | **0.00%** | `input: 729 , ouput: 650` | `i, will, represent, the, maze, as, a, graph, using, the, provided, adjacency, list, where, nodes, are, cells, (row, col), and, edges, represent, valid, moves, between, adjacent, cells., i, will, use, a, breadth-first, search, (bfs), algorithm, to, find, the, shortest, path, from, the, origin, (0, 0), to, the, target, (5, 5)., bfs, guarantees, finding, the, shortest, path, in, an, unweighted, graph., the, bfs, will, proceed, as, follows:, 1., initialize, a, queue, and, add, the, starting, node, (0, 0), along, with, an, empty, path., 2., maintain, a, set, of, visited, nodes, to, avoid, cycles, and, redundant, exploration., 3., while, the, queue, is, not, empty:, a., dequeue, a, node, (current\_cell, current\_path)., b., if, current\_cell, is, the, target, (5, 5), return, current\_path., c., if, current\_cell, has, not, been, visited:, i., mark, current\_cell, as, visited., ii., for, each, neighbor, of, current\_cell:, -, determine, the, move, (up, down, left, right), from, current\_cell, to, neighbor., -, enqueue, (neighbor, current\_path, +, [move])., let's, trace, the, bfs:, queue:, [((0, 0), [])], visited:, {}, dequeue, ((0, 0), []), visited:, {(0, 0)}, neighbors, of, (0, 0):, (0, 1), enqueue, ((0, 1), [right]), queue:, [((0, 1), [right])], dequeue, ((0, 1), [right]), visited:, {(0, 0), (0, 1)}, neighbors, of, (0, 1):, (0, 0), (1, 1), (0, 0), is, visited., enqueue, ((1, 1), [right, down]), queue:, [((1, 1), [right, down])], dequeue, ((1, 1), [right, down]), visited:, {(0, 0), (0, 1), (1, 1)}, neighbors, of, (1, 1):, (0, 1), (1, 0), (1, 2), (0, 1), is, visited., enqueue, ((1, 0), [right, down, left]), enqueue, ((1, 2), [right, down, right]), queue:, [((1, 0), [right, down, left]), ((1, 2), [right, down, right])], dequeue, ((1, 0), [right, down, left]), visited:, {(0, 0), (0, 1), (1, 1), (1, 0)}, neighbors, of, (1, 0):, (1, 1), (2, 0), (1, 1), is, visited., enqueue, ((2, 0), [right, down, left, down]), queue:, [((1, 2), [right, down, right]), ((2, 0), [right, down, left, down])], dequeue, ((1, 2), [right, down, right]), visited:, {(0, 0), (0, 1)` |
| `maze_line_6x6_tokenized_45.txt` | **5.00%** | `input: 673 , ouput: 99` | `right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down` |
| `maze_occupancy_6x6_45.jpg` | **0.00%** | `input: 431 , ouput: 67` | `down, right, down, right, down, right, down, right, down, left, down, left, down, right, right, right, down, right, down, left, down, left, down, right, right, right, up, right, down, right, right, right, down, right` |
| `maze_occupancy_6x6_45.json` | **15.00%** | `input: 988 , ouput: 289` | `right, right, down, down, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right` |
| `maze_occupancy_6x6_adj_45.json` | **15.00%** | `input: 4343 , ouput: 650` | `right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right` |
| `maze_occupancy_6x6_adj_45.txt` | **0.00%** | `input: 1279 , ouput: 650` | `down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right` |
| `maze_occupancy_6x6_ascii_45.txt` | **0.00%** | `input: 248 , ouput: 101` | `down, down, right, right, down, down, right, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_occupancy_6x6_tokenized_45.txt` | **15.00%** | `input: 2162 , ouput: 650` | `right, right, down, down, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right` |

---

## Full LLM Responses

### `maze_line_6x6_45.jpg`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, left, down, right, down, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='H4WVafTUM9uxnsEPg_7zyAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=17,
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
  total_token_count=451
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=17 candidates_tokens_details=None prompt_token_count=434 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=176
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=451 traffic_type=None
```

### `maze_line_6x6_45.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, left, down, right, down, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, down, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, right, right, down, down, right, down, right, right, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IIWVaYfGGOKAkdUPiI2EmQs' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_6x6_adj_45.json`

**Score:** 10.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, left, down, right, down, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, down, down, right, right, right, down, down, down, right, right, down, down, right, right, down, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right, down, down, right, right, right, down, down, down, right, right, down, down, right, right, down, down, right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IYWVaYvaB-TQnsEPhvGb-Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=35,
  prompt_token_count=2258,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=2258
    ),
  ],
  total_token_count=2293
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=35 candidates_tokens_details=None prompt_token_count=2258 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=2258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=2293 traffic_type=None
```

### `maze_line_6x6_adj_45.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, left, down, right, down, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
i, will, represent, the, maze, as, a, graph, using, the, provided, adjacency, list, where, nodes, are, cells, (row, col), and, edges, represent, valid, moves, between, adjacent, cells., i, will, use, a, breadth-first, search, (bfs), algorithm, to, find, the, shortest, path, from, the, origin, (0, 0), to, the, target, (5, 5)., bfs, guarantees, finding, the, shortest, path, in, an, unweighted, graph., the, bfs, will, proceed, as, follows:, 1., initialize, a, queue, and, add, the, starting, node, (0, 0), along, with, an, empty, path., 2., maintain, a, set, of, visited, nodes, to, avoid, cycles, and, redundant, exploration., 3., while, the, queue, is, not, empty:, a., dequeue, a, node, (current\_cell, current\_path)., b., if, current\_cell, is, the, target, (5, 5), return, current\_path., c., if, current\_cell, has, not, been, visited:, i., mark, current\_cell, as, visited., ii., for, each, neighbor, of, current\_cell:, -, determine, the, move, (up, down, left, right), from, current\_cell, to, neighbor., -, enqueue, (neighbor, current\_path, +, [move])., let's, trace, the, bfs:, queue:, [((0, 0), [])], visited:, {}, dequeue, ((0, 0), []), visited:, {(0, 0)}, neighbors, of, (0, 0):, (0, 1), enqueue, ((0, 1), [right]), queue:, [((0, 1), [right])], dequeue, ((0, 1), [right]), visited:, {(0, 0), (0, 1)}, neighbors, of, (0, 1):, (0, 0), (1, 1), (0, 0), is, visited., enqueue, ((1, 1), [right, down]), queue:, [((1, 1), [right, down])], dequeue, ((1, 1), [right, down]), visited:, {(0, 0), (0, 1), (1, 1)}, neighbors, of, (1, 1):, (0, 1), (1, 0), (1, 2), (0, 1), is, visited., enqueue, ((1, 0), [right, down, left]), enqueue, ((1, 2), [right, down, right]), queue:, [((1, 0), [right, down, left]), ((1, 2), [right, down, right])], dequeue, ((1, 0), [right, down, left]), visited:, {(0, 0), (0, 1), (1, 1), (1, 0)}, neighbors, of, (1, 0):, (1, 1), (2, 0), (1, 1), is, visited., enqueue, ((2, 0), [right, down, left, down]), queue:, [((1, 2), [right, down, right]), ((2, 0), [right, down, left, down])], dequeue, ((1, 2), [right, down, right]), visited:, {(0, 0), (0, 1)
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""I will represent the maze as a graph using the provided adjacency list, where nodes are cells (row, col) and edges represent valid moves between adjacent cells. I will use a Breadth-First Search (BFS) algorithm to find the shortest path from the origin (0,0) to the target (5,5). BFS guarantees finding the shortest path in an unweighted graph.

The BFS will proceed as follows:
1. Initialize a queue and add the starting node (0,0) along with an empty path.
2. Maintain a set of visited nodes to avoid cycles and redundant exploration.
3. While the queue is not empty:
    a. Dequeue a node (current\_cell, current\_path).
    b. If current\_cell is the target (5,5), return current\_path.
    c. If current\_cell has not been visited:
        i. Mark current\_cell as visited.
        ii. For each neighbor of current\_cell:
            - Determine the move (up, down, left, right) from current\_cell to neighbor.
            - Enqueue (neighbor, current\_path + [move]).

Let's trace the BFS:

Queue: [((0,0), [])]
Visited: {}

Dequeue ((0,0), [])
Visited: {(0,0)}
Neighbors of (0,0): (0,1)
Enqueue ((0,1), [right])

Queue: [((0,1), [right])]

Dequeue ((0,1), [right])
Visited: {(0,0), (0,1)}
Neighbors of (0,1): (0,0), (1,1)
(0,0) is visited.
Enqueue ((1,1), [right, down])

Queue: [((1,1), [right, down])]

Dequeue ((1,1), [right, down])
Visited: {(0,0), (0,1), (1,1)}
Neighbors of (1,1): (0,1), (1,0), (1,2)
(0,1) is visited.
Enqueue ((1,0), [right, down, left])
Enqueue ((1,2), [right, down, right])

Queue: [((1,0), [right, down, left]), ((1,2), [right, down, right])]

Dequeue ((1,0), [right, down, left])
Visited: {(0,0), (0,1), (1,1), (1,0)}
Neighbors of (1,0): (1,1), (2,0)
(1,1) is visited.
Enqueue ((2,0), [right, down, left, down])

Queue: [((1,2), [right, down, right]), ((2,0), [right, down, left, down])]

Dequeue ((1,2), [right, down, right])
Visited: {(0,0), (0,1),"""
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='IoWVadzXM6rw7M8P4OXQkQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=729,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=729
    ),
  ],
  total_token_count=1379
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=729 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=729
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1379 traffic_type=None
```

### `maze_line_6x6_tokenized_45.txt`

**Score:** 5.00%

**Ground Truth Solution:**
```
right, down, right, up, right, down, down, left, left, left, down, right, down, left, down, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down, left, left, left, left, left, up, up, up, up, up, right, right, right, right, right, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down,left,left,left,left,left,up,up,up,up,up,right,right,right,right,right,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='I4WVaZOiLsyynsEPyd_uiAQ' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=99,
  prompt_token_count=673,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=673
    ),
  ],
  total_token_count=772
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=99 candidates_tokens_details=None prompt_token_count=673 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=673
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=772 traffic_type=None
```

### `maze_occupancy_6x6_45.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, right, down, right, down, right, down, right, down, left, down, left, down, right, right, right, down, right, down, left, down, left, down, right, right, right, up, right, down, right, right, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,right,down,right,down,right,down,right,down,left,down,left,down,right,right,right,down,right,down,left,down,left,down,right,right,right,up,right,down,right,right,right,down,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JIWVaYXMM7zhnsEPwLCgiQY' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=67,
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
  total_token_count=498
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=67 candidates_tokens_details=None prompt_token_count=431 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=173
), ModalityTokenCount(
  modality=<MediaModality.IMAGE: 'IMAGE'>,
  token_count=258
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=498 traffic_type=None
```

### `maze_occupancy_6x6_45.json`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, up, right, down, down, down, down, down, down, right, right, right, right, right, right, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,up,right,down,down,down,down,down,down,right,right,right,right,right,right,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,right,right,right,right,right,right'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='JYWVafKgKq2WkdUPiJ3nmQk' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=289,
  prompt_token_count=988,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=988
    ),
  ],
  total_token_count=1277
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=289 candidates_tokens_details=None prompt_token_count=988 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=988
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1277 traffic_type=None
```

### `maze_occupancy_6x6_adj_45.json`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right, right, right, right, right, down, down, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,right,right,right,right,down,down,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='J4WVaYnUBrW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=4343,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4343
    ),
  ],
  total_token_count=4993
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=4343 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4343
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4993 traffic_type=None
```

### `maze_occupancy_6x6_adj_45.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KYWVafH8BLyK7M8Ph5iNuAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=1279,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=1279
    ),
  ],
  total_token_count=1929
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=1279 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=1279
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1929 traffic_type=None
```

### `maze_occupancy_6x6_ascii_45.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
down, down, right, right, down, down, right, right, right, right, right, down, down, down, down, left, left, left, left, left, left, left, left, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,right,right,right,right,right,down,down,down,down,left,left,left,left,left,left,left,left,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='KoWVae_LAbW5kdUPzM_0sAM' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=101,
  prompt_token_count=248,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=248
    ),
  ],
  total_token_count=349
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=101 candidates_tokens_details=None prompt_token_count=248 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=248
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=349 traffic_type=None
```

### `maze_occupancy_6x6_tokenized_45.txt`

**Score:** 15.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, up, up, right, right, down, down, down, down, left, left, left, left, left, left, down, down, right, right, down, down, left, left, down, down, right, right, right, right, right, right, right, right, right, right
```

**Extracted Answer:**
```
right, right, down, down, right, right, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,down,right,right,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='LIWVacvxEOeGkdUPsqK74AQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

