# LLM Maze Solving Comparison Report

**Maze Dimensions:** 15x15
**Model Used:** `gemini-2.5-flash-lite`

## Comparison Results

| Representation File | Score (%) | Tokens |Extracted LLM Answer |
|---|---|---|---|
| `maze_line_15x15_38.jpg` | **3.75%** | `input: 436 , ouput: 650` | `right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right` |
| `maze_line_15x15_38.json` | **0.00%** | `input: 9807 , ouput: 650` | `down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down` |
| `maze_line_15x15_adj_38.json` | **1.25%** | `input: 13485 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_adj_38.txt` | **1.25%** | `input: 3677 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down` |
| `maze_line_15x15_tokenized_38.txt` | **nan%** | `input: 3282 , ouput: 0` | `` |
| `maze_occupancy_15x15_38.jpg` | **0.62%** | `input: 431 , ouput: 650` | `right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right` |
| `maze_occupancy_15x15_38.json` | **nan%** | `input: 4246 , ouput: 0` | `` |
| `maze_occupancy_15x15_adj_38.json` | **1.88%** | `input: 27629 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_adj_38.txt` | **1.88%** | `input: 7731 , ouput: 650` | `right, right, down, right, right, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_ascii_38.txt` | **0.00%** | `input: 541 , ouput: 650` | `down, down, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right` |
| `maze_occupancy_15x15_tokenized_38.txt` | **1.25%** | `input: 12134 , ouput: 650` | `right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left` |

---

## Full LLM Responses

### `maze_line_15x15_38.jpg`

**Score:** 3.75%

**Ground Truth Solution:**
```
right, down, right, right, right, right, up, right, down, right, up, right, right, down, down, down, down, right, right, down, down, left, left, up, left, up, up, left, left, down, left, left, down, left, up, up, left, down, left, left, down, down, right, up, right, down, right, right, right, up, right, right, down, right, down, left, down, down, left, down, right, down, down, right, right, right, right, up, right, down, down, down, right, up, up, up, right, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, up, right, up, right, up, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right, down, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  citation_metadata=CitationMetadata(
    citations=[
      Citation(
        end_index=1774,
        license='',
        start_index=229,
        uri='https://americanarchive.org/catalog/cpb-aacip-b6e75cd0ce5'
      ),
    ]
  ),
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,up,right,up,right,up,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,down,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='2aiUadaoM8eqnsEPypadgQU' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_38.json`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, down, right, right, right, right, up, right, down, right, up, right, right, down, down, down, down, right, right, down, down, left, left, up, left, up, up, left, left, down, left, left, down, left, up, up, left, down, left, left, down, down, right, up, right, down, right, right, right, up, right, right, down, right, down, left, down, down, left, down, right, down, down, right, right, right, right, up, right, down, down, down, right, up, up, up, right, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='26iUaeeQLdjpnsEPmcvxyAE' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_line_15x15_adj_38.json`

**Score:** 1.25%

**Ground Truth Solution:**
```
right, down, right, right, right, right, up, right, down, right, up, right, right, down, down, down, down, right, right, down, down, left, left, up, left, up, up, left, left, down, left, left, down, left, up, up, left, down, left, left, down, down, right, up, right, down, right, right, right, up, right, right, down, right, down, left, down, down, left, down, right, down, down, right, right, right, right, up, right, down, down, down, right, up, up, up, right, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='3aiUaeXmK8DzkdUPloGV4Ag' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=13485,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=13485
    ),
  ],
  total_token_count=14135
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=13485 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=13485
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=14135 traffic_type=None
```

### `maze_line_15x15_adj_38.txt`

**Score:** 1.25%

**Ground Truth Solution:**
```
right, down, right, right, right, right, up, right, down, right, up, right, right, down, down, down, down, right, right, down, down, left, left, up, left, up, up, left, left, down, left, left, down, left, up, up, left, down, left, left, down, down, right, up, right, down, right, right, right, up, right, right, down, right, down, left, down, down, left, down, right, down, down, right, right, right, right, up, right, down, down, down, right, up, up, up, right, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, down, down, down, down, down, down, down, down, down, down, down
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,down,down,down,down,down,down,down,down,down,down,down,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='36iUacK5N8GknsEPzKbYmAI' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=3677,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3677
    ),
  ],
  total_token_count=4327
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=3677 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3677
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4327 traffic_type=None
```

### `maze_line_15x15_tokenized_38.txt`

**Score:** nan%

**Ground Truth Solution:**
```
right, down, right, right, right, right, up, right, down, right, up, right, right, down, down, down, down, right, right, down, down, left, left, up, left, up, up, left, left, down, left, left, down, left, up, up, left, down, left, left, down, down, right, up, right, down, right, right, right, up, right, right, down, right, down, left, down, down, left, down, right, down, down, right, right, right, right, up, right, down, down, down, right, up, up, up, right, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='4qiUaYnyFovw7M8PibDEsAI' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=3282,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=3282
    ),
  ],
  total_token_count=3282
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=3282 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=3282
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=3282 traffic_type=None
```

### `maze_occupancy_15x15_38.jpg`

**Score:** 0.62%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, up, up, left, left, up, up, up, up, left, left, left, left, down, down, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, left, down, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right, down, right, down, right, down, left, down, right, down, right, down, right, up, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,left,down,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,down,right,down,right,down,left,down,right,down,right,down,right,up,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='5aiUaeqkLemekdUPuPLrcQ' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_38.json`

**Score:** nan%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, up, up, left, left, up, up, up, up, left, left, left, left, down, down, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down
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
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6KiUab-yFd_x7M8P3PK2gQE' usage_metadata=GenerateContentResponseUsageMetadata(
  prompt_token_count=4246,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=4246
    ),
  ],
  total_token_count=4246
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=None candidates_tokens_details=None prompt_token_count=4246 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=4246
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=4246 traffic_type=None
```

### `maze_occupancy_15x15_adj_38.json`

**Score:** 1.88%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, up, up, left, left, up, up, up, up, left, left, left, left, down, down, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='6qiUaf36H5TlnsEP9NTwiQU' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=27629,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=27629
    ),
  ],
  total_token_count=28279
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=27629 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=27629
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=28279 traffic_type=None
```

### `maze_occupancy_15x15_adj_38.txt`

**Score:** 1.88%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, up, up, left, left, up, up, up, up, left, left, left, left, down, down, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, down, right, right, right, right, right, right, right, down, right, down, right, right, right, right, right, down, right, right, right, right, right, right, down, right, right, right, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,down,right,right,right,right,right,right,right,down,right,down,right,right,right,right,right,down,right,right,right,right,right,right,down,right,right,right,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7KiUab2ZHubgnsEP6p2VqQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

### `maze_occupancy_15x15_ascii_38.txt`

**Score:** 0.00%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, up, up, left, left, up, up, up, up, left, left, left, left, down, down, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
down, down, right, right, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='down,down,right,right,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='7qiUafPGH5S8nsEPnPGoiQ8' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=650,
  prompt_token_count=541,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=541
    ),
  ],
  total_token_count=1191
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
cache_tokens_details=None cached_content_token_count=None candidates_token_count=650 candidates_tokens_details=None prompt_token_count=541 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=541
)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=1191 traffic_type=None
```

### `maze_occupancy_15x15_tokenized_38.txt`

**Score:** 1.25%

**Ground Truth Solution:**
```
right, right, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, right, right, up, up, right, right, right, right, down, down, down, down, down, down, down, down, right, right, right, right, down, down, down, down, left, left, left, left, up, up, left, left, up, up, up, up, left, left, left, left, down, down, left, left, left, left, down, down, left, left, up, up, up, up, left, left, down, down, left, left, left, left, down, down, down, down, right, right, up, up, right, right, down, down, right, right, right, right, right, right, up, up, right, right, right, right, down, down, right, right, down, down, left, left, down, down, down, down, left, left, down, down, right, right, down, down, down, down, right, right, right, right, right, right, right, right, up, up, right, right, down, down, down, down, down, down, right, right, up, up, up, up, up, up, right, right, down, down, down, down, down, down
```

**Extracted Answer:**
```
right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, up, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, right, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, down, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left, left
```

**Unfiltered Response:**
```
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,up,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,right,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,down,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.MAX_TOKENS: 'MAX_TOKENS'>,
  index=0
)] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='76iUaZ6cMcKHnsEPkpLbwQ8' usage_metadata=GenerateContentResponseUsageMetadata(
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

