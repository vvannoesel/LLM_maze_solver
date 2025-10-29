# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools. The maze is represented as a 5x5 grid. The top-left corner is (0,0). Instructions: 1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell. 2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1). 3. Provide only the final list of coordinates from start to end in your response.`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_3.txt` | **7.69%** | `input: 234 , ouput: 6653` | `[(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_3.txt`

**Score:** 7.69%

**Ground Truth Solution:**
```
(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(3,4),(4,4)
```

**Internal Thoughts:**
```
**Navigating the Maze: Finding the Path from O to T**

Alright, let's get down to brass tacks. I've been handed a 5x5 grid with some walls, a starting point 'O' at (0,0), and a target 'T' at (4,4). The goal is clear: find a valid path from 'O' to 'T'. My strategy? I'll treat this like any expert problem – brute force, combined with smart backtracking.

First, I mentally mapped out the maze's structure. That means translating those `+---+` and `|` symbols into actual allowed and blocked movements. I thought about analyzing each cell meticulously but quickly realized that would be a recipe for tedium and potential errors. No, the better approach is to trace the *open* paths.

So, I started from the origin, 'O'. The only way out from (0,0) is downward to (1,0). From there, I saw two options: right to (1,1) or down to (2,0). I went right. At (1,1), things got interesting. I could go right, down, or potentially revisit my past. I chose to go down to (2,1) and then right to (2,2) and down to (3,2). Now, (3,2) was a decision point. I could go right, left, or up. I tried the right path, but it led to a dead end. I went back to (3,2) and then took the right path, which finally led to T.

I then went back and explored an alternate path from (1,1) going right, and this also works. But the initial solution (0,0), (1,0), (1,1), (2,1), (2,2), (3,2), (3,3), (3,4), (4,4) is valid and looks clean. It avoids loops and dead ends, and I've double-checked my work. So, here's my answer, presented as a sequence of coordinates: (0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(3,4),(4,4).

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Navigating the Maze: Finding the Path from O to T**

Alright, let's get down to brass tacks. I've been handed a 5x5 grid with some walls, a starting point 'O' at (0,0), and a target 'T' at (4,4). The goal is clear: find a valid path from 'O' to 'T'. My strategy? I'll treat this like any expert problem – brute force, combined with smart backtracking.

First, I mentally mapped out the maze's structure. That means translating those `+---+` and `|` symbols into actual allowed and blocked movements. I thought about analyzing each cell meticulously but quickly realized that would be a recipe for tedium and potential errors. No, the better approach is to trace the *open* paths.

So, I started from the origin, 'O'. The only way out from (0,0) is downward to (1,0). From there, I saw two options: right to (1,1) or down to (2,0). I went right. At (1,1), things got interesting. I could go right, down, or potentially revisit my past. I chose to go down to (2,1) and then right to (2,2) and down to (3,2). Now, (3,2) was a decision point. I could go right, left, or up. I tried the right path, but it led to a dead end. I went back to (3,2) and then took the right path, which finally led to T.

I then went back and explored an alternate path from (1,1) going right, and this also works. But the initial solution (0,0), (1,0), (1,1), (2,1), (2,2), (3,2), (3,3), (3,4), (4,4) is valid and looks clean. It avoids loops and dead ends, and I've double-checked my work. So, here's my answer, presented as a sequence of coordinates: (0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(3,4),(4,4).
""",
        thought=True
      ),
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(3,4),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='aDMCaZCgJcu4kdUPtK7p0AU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=234,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=234
    ),
  ],
  thoughts_token_count=6616,
  total_token_count=6887
) automatic_function_calling_history=[] parsed=None
```
**total_tokens:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) total_tokens=145 cached_content_token_count=None
```
**Metadata:**
```
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=234 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=234
)] thoughts_token_count=6616 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=6887 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Navigating the Maze: Finding the Path from O to T**

Alright, let's get down to brass tacks. I've been handed a 5x5 grid with some walls, a starting point 'O' at (0,0), and a target 'T' at (4,4). The goal is clear: find a valid path from 'O' to 'T'. My strategy? I'll treat this like any expert problem – brute force, combined with smart backtracking.

First, I mentally mapped out the maze's structure. That means translating those `+---+` and `|` symbols into actual allowed and blocked movements. I thought about analyzing each cell meticulously but quickly realized that would be a recipe for tedium and potential errors. No, the better approach is to trace the *open* paths.

So, I started from the origin, 'O'. The only way out from (0,0) is downward to (1,0). From there, I saw two options: right to (1,1) or down to (2,0). I went right. At (1,1), things got interesting. I could go right, down, or potentially revisit my past. I chose to go down to (2,1) and then right to (2,2) and down to (3,2). Now, (3,2) was a decision point. I could go right, left, or up. I tried the right path, but it led to a dead end. I went back to (3,2) and then took the right path, which finally led to T.

I then went back and explored an alternate path from (1,1) going right, and this also works. But the initial solution (0,0), (1,0), (1,1), (2,1), (2,2), (3,2), (3,3), (3,4), (4,4) is valid and looks clean. It avoids loops and dead ends, and I've double-checked my work. So, here's my answer, presented as a sequence of coordinates: (0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(3,4),(4,4).
""",
        thought=True
      ),
      Part(
        text='(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(3,4),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

