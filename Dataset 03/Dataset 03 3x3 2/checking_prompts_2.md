# LLM Maze Solving Comparison Report

**Maze Dimensions:** 3x3
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_3x3_2.jpg` | **0.00%** | `` |
| `maze_line_3x3_2.json` | **0.00%** | `` |
| `maze_line_3x3_adj_2.json` | **0.00%** | `` |
| `maze_line_3x3_adj_2.txt` | **0.00%** | `` |
| `maze_line_3x3_tokenized_2.txt` | **0.00%** | `` |
| `maze_occupancy_3x3_2.jpg` | **0.00%** | `` |
| `maze_occupancy_3x3_2.json` | **0.00%** | `` |
| `maze_occupancy_3x3_adj_2.json` | **0.00%** | `` |
| `maze_occupancy_3x3_adj_2.txt` | **0.00%** | `` |
| `maze_occupancy_3x3_ascii_2.txt` | **0.00%** | `` |
| `maze_occupancy_3x3_tokenized_2.txt` | **0.00%** | `` |

---

## Full LLM Responses

### `maze_line_3x3_2.jpg`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 3x3 maze is shown as an image, where thick black lines are impassable walls, thin light gray lines are passable cell borders, the circle is the start and the star is the end; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_line_3x3_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_line_3x3_2.json`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 3x3 maze is represented as a JSON grid, which describes each cell as a set of four (N/E/S/W) walls with boolean 'True' (impassable) or 'False' (passable) values and includes start/end coordinates; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_line_3x3_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_line_3x3_adj_2.json`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 3x3 maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_line_3x3_adj_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_line_3x3_adj_2.txt`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 3x3 maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_line_3x3_adj_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_line_3x3_tokenized_2.txt`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 3x3 maze is represented as a grid in a tokenized manner, where each cell is described by its walls (e.g., <|updownleft_wall|>) and the start and end cells are marked with <|origin|> and <|target|>, respectively; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_line_3x3_tokenized_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_occupancy_3x3_2.jpg`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 7x7 maze is shown as an image, where white cells are passable, black cells are impassable walls, the circle is the start and the star is the end; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_occupancy_3x3_2.jpg`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_occupancy_3x3_2.json`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 7x7 maze is represented as a JSON grid, where cells are '1' (inaccessible) or '0' (accessible), and start/end coordinates are provided; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_occupancy_3x3_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_occupancy_3x3_adj_2.json`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 7x7 maze is represented as a JSON adjacency list, which lists all available neighbors for each cell and provides start/end coordinates; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_occupancy_3x3_adj_2.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_occupancy_3x3_adj_2.txt`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 7x7 maze is represented as a graph via an adjacency list that lists which cells are connected (e.g., (0,0) <–> (0,1)) and marks the start and end with <ORIGIN> and <TARGET> tags; when converted to a grid, the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_occupancy_3x3_adj_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_occupancy_3x3_ascii_2.txt`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The maze is represented as a 7x7 ASCII grid using '#' for walls, ' ' for corridors, 'S' for the start, and 'E' for the end; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_occupancy_3x3_ascii_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
### `maze_occupancy_3x3_tokenized_2.txt`

**Prompt:**
```
You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools.The 7x7 maze is represented as a grid in a tokenized manner, where inaccessible cells are tagged as <|occupied_wall|>,  accessible cells are tagged as <|blank|>, and the start and end cells are tagged with <|origin|> and <|target|>, respectively; the top-left corner is (0,0).
 
 Instructions:
1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell.
2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1).
3. Provide only the final list of coordinates from start to end in your response.
```

### `maze_occupancy_3x3_tokenized_2.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)
```

**Extracted Answer:**
```

```

**total_tokens:**
```
0
```
