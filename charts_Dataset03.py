import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi


# NR - EGO - 1-3 ----------------------------------------------------------------
line_adj_json = np.array([25.0, 0.0, 25.0])
line_adj_txt = np.array([0.0, 0.0, 0.0])
line_jpg = np.array([0.0, 0.0, 0.0])
line_json = np.array([25.0, 0.0, 0.0])
line_tokenized_txt = np.array([0.0, 0.0, 0.0])
occupancy_adj_json = np.array([0.0, 0.0, 12.5])
occupancy_adj_txt = np.array([0.0, 0.0, 0.0])
occupancy_ascii_txt = np.array([0.0, 0.0, 0.0])
occupancy_jpg = np.array([0.0, 0.0, 12.5])
occupancy_json = np.array([0.0, 0.0, 0.0])
occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0])

tokens_run_3 = np.array([11, 13, 15, 13, 17, 31, 4000, 4000, 33, 79, 1029])

x_axis = ['3x3', '7x7']

div_line_adj_json = line_adj_json[2]/tokens_run_3[0]
div_line_adj_txt = line_adj_txt[2]/tokens_run_3[1]
div_line_jpg = line_jpg[2]/tokens_run_3[2]
div_line_json = line_json[2]/tokens_run_3[3]
div_line_tokenized_txt = line_tokenized_txt[2]/tokens_run_3[4]
div_occupancy_adj_json = occupancy_adj_json[2]/tokens_run_3[5]
div_occupancy_adj_txt = occupancy_adj_txt[2]/tokens_run_3[6]
div_occupancy_ascii_txt = occupancy_ascii_txt[2]/tokens_run_3[7]
div_occupancy_jpg = occupancy_jpg[2]/tokens_run_3[8]
div_occupancy_json = occupancy_json[2]/tokens_run_3[9]
div_occupancy_tokenized_txt = occupancy_tokenized_txt[2]/tokens_run_3[10]

# 5 values belonging to complexity 3x3
div_3x3 = [
    div_line_adj_json,
    div_line_adj_txt,
    div_line_jpg,
    div_line_json,
    div_line_tokenized_txt
]
labels_3x3 = [
    "div_line_adj_json",
    "div_line_adj_txt",
    "div_line_jpg",
    "div_line_json",
    "div_line_tokenized_txt"
]

# 6 values belonging to complexity 7x7
div_7x7 = [
    div_occupancy_adj_json,
    div_occupancy_adj_txt,
    div_occupancy_ascii_txt,
    div_occupancy_jpg,
    div_occupancy_json,
    div_occupancy_tokenized_txt
]

labels_7x7 = [
    "div_occupancy_adj_json",
    "div_occupancy_adj_txt",
    "div_occupancy_ascii_txt",
    "div_occupancy_jpg",
    "div_occupancy_json",
    "div_occupancy_tokenized_txt"
]

fig, ax = plt.subplots(figsize=(8, 6))

# x positions for the two groups
x_pos = np.array([0, 1])   # 0 = 3x3, 1 = 7x7

# Add jitter so points don’t overlap vertically
jitter_3x3 = np.random.uniform(-0.05, 0.05, len(div_3x3))
jitter_7x7 = np.random.uniform(-0.05, 0.05, len(div_7x7))
for i, (value, label) in enumerate(zip(div_3x3, labels_3x3)):
    ax.scatter(
        0 + jitter_3x3[i],   # x-position with jitter
        value,               # y-value
        label=label,         # unique legend entry
        s=80
    )


for i, (value, label) in enumerate(zip(div_7x7, labels_7x7)):
    ax.scatter(
        1 + jitter_7x7[i],   # x-position with jitter
        value,
        label=label,
        s=80
    )


ax.set_xticks(x_pos)
ax.set_xticklabels(x_axis)

ax.set_xlabel('complexity')
ax.set_ylabel('accuracy/outputtoken [%/token]')

ax.set_title('Contribution of Individual Output Tokens To Accuracy, Gemini 2.5 Flash Lite, Egocentric Output, Run 3')

ax.grid(axis='y', linestyle='--', alpha=0.3)

ax.legend(
    loc='lower center',
    bbox_to_anchor=(0.5, 1.15),
    ncol=3,
    fontsize=9
)

plt.tight_layout()
plt.show()