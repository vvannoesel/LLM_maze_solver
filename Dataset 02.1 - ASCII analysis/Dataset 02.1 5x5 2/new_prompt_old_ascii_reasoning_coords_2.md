# LLM Maze Solving Comparison Report

MEW ASCII

**Maze Dimensions:** 5x5
**Model Used:** `gemini-2.5-pro`

**Prompt Used:** `You are a maze-solving expert. Your goal is to find the path from start to end. Do not use external tools. The maze is represented as a 5x5 grid. The top-left corner is (0,0). Instructions: 1. You cannot move diagonally or through walls ('---' and '|'), only from one cell to an adjacent cell. 2. Create a comma-separated sequence all coordinates on the path from start to end, including the start and end points. For example: (0,0),(1,0),(1,1),(2,1),(3,1). 3. Provide only the final list of coordinates from start to end in your response.`

## Comparison Results

| Representation File | Score (%) | Token count |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_5x5_ascii_2.txt` | **18.18%** | `input: 241 , ouput: 1614` | `[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 4)]` |

---

## Full LLM Responses

### `maze_line_5x5_ascii_2.txt`

**Score:** 18.18%

**Ground Truth Solution:**
```
(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3), (3, 4), (4, 4)
```

**Full User-Facing Response (Final Answer):**
```
(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(2,4),(3,4),(4,4)
```

**Internal Thoughts:**
```
**Finding a Path Through the Maze**

Alright, I've got this maze problem. First, I need to understand the layout. It's a 5x5 grid, 'O' is at (0,0), and 'T' is at (4,4). I've mentally mapped out the coordinates to keep track.

Now, I'm going to start tracing possible paths from 'O'. It looks like I need to go down to (1,0) first, since the starting point is blocked in every other direction. Then, it's pretty straightforward, just moving right to (1,1), then (1,2).

At (1,2) I see two possibilities: going right or down. I'll pick right for now and go to (1,3). From there, down to (2,3) seems natural. After that, I move right to (2,4). Next, down to (3,4) and finally down to (4,4), the end goal!

I double-checked to make sure all these moves are valid, no blocked paths. All good.

However, just to be thorough, I wanted to explore the alternate path from that earlier decision point at (1,2). Going down to (2,2) and then left leads to a different solution. It is longer, though.

I realized the problem didn't specify the shortest path, just *a* path. So, I'll go with the first path since it's more direct. It's (0,0), (1,0), (1,1), (1,2), (1,3), (2,3), (2,4), (3,4), (4,4).

I just re-verified each move is valid and there are no closed paths between. Done! I can present my results as a comma-separated list of coordinates, as needed.
(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(2,4),(3,4),(4,4)

```
**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Finding a Path Through the Maze**

Alright, I've got this maze problem. First, I need to understand the layout. It's a 5x5 grid, 'O' is at (0,0), and 'T' is at (4,4). I've mentally mapped out the coordinates to keep track.

Now, I'm going to start tracing possible paths from 'O'. It looks like I need to go down to (1,0) first, since the starting point is blocked in every other direction. Then, it's pretty straightforward, just moving right to (1,1), then (1,2).

At (1,2) I see two possibilities: going right or down. I'll pick right for now and go to (1,3). From there, down to (2,3) seems natural. After that, I move right to (2,4). Next, down to (3,4) and finally down to (4,4), the end goal!

I double-checked to make sure all these moves are valid, no blocked paths. All good.

However, just to be thorough, I wanted to explore the alternate path from that earlier decision point at (1,2). Going down to (2,2) and then left leads to a different solution. It is longer, though.

I realized the problem didn't specify the shortest path, just *a* path. So, I'll go with the first path since it's more direct. It's (0,0), (1,0), (1,1), (1,2), (1,3), (2,3), (2,4), (3,4), (4,4).

I just re-verified each move is valid and there are no closed paths between. Done! I can present my results as a comma-separated list of coordinates, as needed.
(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(2,4),(3,4),(4,4)
""",
        thought=True
      ),
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(2,4),(3,4),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-2.5-pro' prompt_feedback=None response_id='MjMCaeWCL525kdUPjoHckAU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=37,
  prompt_token_count=241,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=241
    ),
  ],
  thoughts_token_count=1577,
  total_token_count=1855
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=37 candidates_tokens_details=None prompt_token_count=241 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=241
)] thoughts_token_count=1577 tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1855 traffic_type=None
```
**Candidates:**
```
[Candidate(
  content=Content(
    parts=[
      Part(
        text="""**Finding a Path Through the Maze**

Alright, I've got this maze problem. First, I need to understand the layout. It's a 5x5 grid, 'O' is at (0,0), and 'T' is at (4,4). I've mentally mapped out the coordinates to keep track.

Now, I'm going to start tracing possible paths from 'O'. It looks like I need to go down to (1,0) first, since the starting point is blocked in every other direction. Then, it's pretty straightforward, just moving right to (1,1), then (1,2).

At (1,2) I see two possibilities: going right or down. I'll pick right for now and go to (1,3). From there, down to (2,3) seems natural. After that, I move right to (2,4). Next, down to (3,4) and finally down to (4,4), the end goal!

I double-checked to make sure all these moves are valid, no blocked paths. All good.

However, just to be thorough, I wanted to explore the alternate path from that earlier decision point at (1,2). Going down to (2,2) and then left leads to a different solution. It is longer, though.

I realized the problem didn't specify the shortest path, just *a* path. So, I'll go with the first path since it's more direct. It's (0,0), (1,0), (1,1), (1,2), (1,3), (2,3), (2,4), (3,4), (4,4).

I just re-verified each move is valid and there are no closed paths between. Done! I can present my results as a comma-separated list of coordinates, as needed.
(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(2,4),(3,4),(4,4)
""",
        thought=True
      ),
      Part(
        text='(0,0),(1,0),(1,1),(1,2),(1,3),(2,3),(2,4),(3,4),(4,4)'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)]
```

