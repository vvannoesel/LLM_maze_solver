import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi


x_axis_line = ['3x3', '6x6', '15x15']
x_axis_occ = ['7x7', '13x13', '31x31']

# R -- Coords -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Raw Scores R Coords 3x3
line_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_jpg_raw_score = np.array([2.0, 5.0, 5.0, 5.0, 2.0, 2.0, 2.0, 7.0, 7.0, 5.0])
line_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_tokenized_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
occupancy_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_ascii_txt_raw_score = np.array([2.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 6.0, 7.0])
occupancy_jpg_raw_score = np.array([1.0, 2.0, 5.0, 0.0, 1.0, 1.0, 3.0, 0.0, 1.0, 9.0])
occupancy_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_tokenized_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9])
# 3x3 averages
avg_coords_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
avg_coords_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
avg_coords_line_jpg_raw_score = np.mean(line_jpg_raw_score)
avg_coords_line_json_raw_score = np.mean(line_json_raw_score)
avg_coords_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
avg_coords_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
avg_coords_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
avg_coords_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
avg_coords_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
avg_coords_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
avg_coords_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# Raw Scores R Coords 6x6
line_adj_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
line_adj_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
line_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
line_tokenized_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
occupancy_adj_json_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0])
occupancy_adj_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0])
occupancy_ascii_txt_raw_score_6 = np.array([8.0, 12.0, 8.0, 1.0, 9.0, 1.0, 1.0, 0.0, 9.0, 1.0])
occupancy_jpg_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_raw_score_6 = np.array([9.0, 18.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 20.0, 41.0])
occupancy_tokenized_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41])
# 6x6 averages
avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# Raw Scores R Coords 15x15
line_adj_json_raw_score_15 = np.array([131.0])
line_adj_txt_raw_score_15 = np.array([25.0])
line_jpg_raw_score_15 = np.array([0.0])
line_json_raw_score_15 = np.array([31.0])
line_tokenized_txt_raw_score_15 = np.array([126.0])
occupancy_adj_json_raw_score_15 = np.array([261.0])
occupancy_adj_txt_raw_score_15 = np.array([89.0])
occupancy_ascii_txt_raw_score_15 = np.array([0.0])
occupancy_jpg_raw_score_15 = np.array([5.0])
occupancy_json_raw_score_15 = np.array([31.0])
occupancy_tokenized_txt_raw_score_15 = np.array([103])

# Dataset for top chart
jpg_line = [avg_coords_line_jpg_raw_score , line_jpg_raw_score_15.item()]
json_line = [avg_coords_line_json_raw_score , line_json_raw_score_15.item()]
adj_json_line = [avg_coords_line_adj_json_raw_score , line_adj_json_raw_score_15.item()]
adj_txt_line = [avg_coords_line_adj_txt_raw_score , line_adj_txt_raw_score_15.item()]
tokenized_line = [avg_coords_line_tokenized_txt_raw_score, line_tokenized_txt_raw_score_15.item()]
dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# Dataset for bottom chart
jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , occupancy_jpg_raw_score_15.item()]
json_occupancy = [avg_coords_occupancy_json_raw_score , occupancy_json_raw_score_15.item()]
adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , occupancy_adj_json_raw_score_15.item()]
adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , occupancy_adj_txt_raw_score_15.item()]
tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score, occupancy_tokenized_txt_raw_score_15.item()]
ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score, occupancy_ascii_txt_raw_score_15.item()]
dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

x_pos = np.array([0, 1])   # two x-axis positions
jitter_strength = 0.01
# Build figure
fig, (ax1, ax2) = plt.subplots(
    nrows=2,
    ncols=1,
    figsize=(10, 8),
    sharex=False  # ensures the two subplots align vertically
)

# Top Plot
for data, label in zip(dataset_line, labels_line):
    ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
    jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
    ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

ax1.set_xticks(x_pos)
ax1.set_xticklabels(x_axis_line)

ax1.set_xlabel("Maze Complexity")
ax1.set_ylabel("Number of Correct Steps")
ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Coordinates Output")

# Legend centered above subplot
ax1.legend(
    loc='best',
    # bbox_to_anchor=(0.5, 1.18),
    ncol=3,
    fontsize=9
)

ax1.grid(axis='y', linestyle='--', alpha=0.8)

# Bottom Plot
for data, label in zip(dataset_occupancy, labels_occupancy):
    ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
    jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
    ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

ax2.set_xticks(x_pos)
ax2.set_xticklabels(x_axis_occ)

ax2.set_xlabel("Maze Complexity")
ax2.set_ylabel("Number of Correct Steps")
ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Coordinates Output")

# Legend centered above subplot
ax2.legend(
    loc='best',
    # bbox_to_anchor=(0.5, 1.18),
    ncol=3,
    fontsize=9
)

ax2.grid(axis='y', linestyle='--', alpha=0.8)

plt.tight_layout()
plt.show()

# R -- Allo -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Raw Scores R Allo 3x3
line_adj_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_adj_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_jpg_raw_score = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 1.0, 4.0, 1.0, 6.0, 0.0])
line_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
occupancy_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 5.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_jpg_raw_score = np.array([0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 2.0, 2.0, 0.0, 3.0])
occupancy_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_tokenized_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8])
# 3x3 averages
avg_allo_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
avg_allo_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
avg_allo_line_jpg_raw_score = np.mean(line_jpg_raw_score)
avg_allo_line_json_raw_score = np.mean(line_json_raw_score)
avg_allo_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
avg_allo_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
avg_allo_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
avg_allo_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
avg_allo_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
avg_allo_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
avg_allo_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# Raw Scores R Allo 6x6
line_adj_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_adj_txt_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_jpg_raw_score_6 = np.array([1.0, 1.0, 0.0, 0.0, 4.0, 3.0, 1.0, 0.0, 3.0, 0.0])
line_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_tokenized_txt_raw_score_6 = np.array([16.0, 18.0, 13.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
occupancy_adj_json_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
occupancy_adj_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
occupancy_ascii_txt_raw_score_6 = np.array([2.0, 0.0, 0.0, 14.0, 4.0, 22.0, 6.0, 7.0, 8.0, 4.0])
occupancy_jpg_raw_score_6 = np.array([6.0, 2.0, 3.0, 8.0, 2.0, 2.0, 2.0, 0.0, 3.0, 2.0])
occupancy_json_raw_score_6 = np.array([18.0, 36.0, 68.0, 4.0, 28.0, 40.0, 48.0, 20.0, 32.0, 15.0])
occupancy_tokenized_txt_raw_score_6 = np.array([32.0, 36.0, 35.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40])
# 6x6 averages
avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# Raw Scores R Allo 15x15
line_adj_json_raw_score_15 = np.array([61])
line_adj_txt_raw_score_15 = np.array([10])
line_jpg_raw_score_15 = np.array([1])
line_json_raw_score_15 = np.array([36])
line_tokenized_txt_raw_score_15 = np.array([43])
occupancy_adj_json_raw_score_15 = np.array([120])
occupancy_adj_txt_raw_score_15 = np.array([72])
occupancy_ascii_txt_raw_score_15 = np.array([4])
occupancy_jpg_raw_score_15 = np.array([3])
occupancy_json_raw_score_15 = np.array([1])
occupancy_tokenized_txt_raw_score_15 = np.array([66])

# # Dataset for top chart
# jpg_line = [avg_allo_line_jpg_raw_score , line_jpg_raw_score_15.item()]
# json_line = [avg_allo_line_json_raw_score , line_json_raw_score_15.item()]
# adj_json_line = [avg_allo_line_adj_json_raw_score , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_allo_line_adj_txt_raw_score , line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_allo_line_tokenized_txt_raw_score, line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_allo_occupancy_jpg_raw_score , occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_allo_occupancy_json_raw_score , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_allo_occupancy_adj_json_raw_score , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_allo_occupancy_adj_txt_raw_score , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_allo_occupancy_tokenized_txt_raw_score, occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_allo_occupancy_ascii_txt_raw_score, occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1])   # two x-axis positions
# jitter_strength = 0.02
# # Build figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2,
#     ncols=1,
#     figsize=(10, 8),
#     sharex=False  # ensures the two subplots align vertically
# )

# # Top Plot
# for data, label in zip(dataset_line, labels_line):
#     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax1.set_xticks(x_pos)
# ax1.set_xticklabels(x_axis_line)

# ax1.set_xlabel("Maze Complexity")
# ax1.set_ylabel("Number of Correct Steps")
# ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Allocentric Output")

# # Legend centered above subplot
# ax1.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Bottom Plot
# for data, label in zip(dataset_occupancy, labels_occupancy):
#     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax2.set_xticks(x_pos)
# ax2.set_xticklabels(x_axis_occ)

# ax2.set_xlabel("Maze Complexity")
# ax2.set_ylabel("Number of Correct Steps")
# ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Allocentric Output")

# # Legend centered above subplot
# ax2.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax2.grid(axis='y', linestyle='--', alpha=0.3)

# plt.tight_layout()
# plt.show()





# R -- Ego -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Raw Scores R Ego 3x3
line_adj_json_raw_score = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_adj_txt_raw_score = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_jpg_raw_score = np.array([1.0, 0.0, 2.0, 2.0, 2.0, 0.0, 0.0, 6.0, 1.0, 4.0])
line_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
occupancy_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 4.0, 12.0, 12.0, 6.0])
occupancy_jpg_raw_score = np.array([1.0, 0.0, 0.0, 4.0, 4.0, 0.0, 1.0, 11.0, 1.0, 3.0])
occupancy_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_tokenized_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8])
# 3x3 averages
avg_ego_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
avg_ego_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
avg_ego_line_jpg_raw_score = np.mean(line_jpg_raw_score)
avg_ego_line_json_raw_score = np.mean(line_json_raw_score)
avg_ego_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
avg_ego_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
avg_ego_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
avg_ego_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
avg_ego_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
avg_ego_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
avg_ego_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
#Raw Scores R Ego 6x6
line_adj_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_adj_txt_raw_score_6 = np.array([16.0, 1.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_jpg_raw_score_6 = np.array([2.0, 2.0, 0.0, 0.0, 3.0, 0.0, 1.0, 0.0, 5.0, 0.0])
line_json_raw_score_6 = np.array([16.0, 3.0, 34.0, 28.0, 14.0, 20.0, 20.0, 10.0, 1.0, 20.0])
line_tokenized_txt_raw_score_6 = np.array([16.0, 18.0, 13.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
occupancy_adj_json_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 0.0, 32.0, 40.0])
occupancy_adj_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
occupancy_ascii_txt_raw_score_6 = np.array([4.0, 12.0, 0.0, 10.0, 8.0, 2.0, 5.0, 7.0, 0.0, 4.0])
occupancy_jpg_raw_score_6 = np.array([2.0, 6.0, 4.0, 0.0, 6.0, 1.0, 6.0, 10.0, 4.0, 0.0])
occupancy_json_raw_score_6 = np.array([32.0, 36.0, 6.0, 10.0, 28.0, 36.0, 48.0, 20.0, 18.0, 4.0])
occupancy_tokenized_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 14.0, 20.0, 32.0, 40])
#6x6 averages
avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# Raw Scores R Ego 15x15
line_adj_json_raw_score_15 = np.array([4.0])
line_adj_txt_raw_score_15 = np.array([3.0])
line_jpg_raw_score_15 = np.array([1.0])
line_json_raw_score_15 = np.array([4.0])
line_tokenized_txt_raw_score_15 = np.array([2.0])
occupancy_jpg_raw_score_15 = np.array([4.0])
occupancy_json_raw_score_15 = np.array([10.0])
occupancy_adj_json_raw_score_15 = np.array([89.0])
occupancy_adj_txt_raw_score_15 = np.array([4.0])
occupancy_ascii_txt_raw_score_15 = np.array([2.0])
occupancy_tokenized_txt_raw_score_15 = np.array([71])


# # Dataset for top chart
# jpg_line = [avg_ego_line_jpg_raw_score , line_jpg_raw_score_15.item()]
# json_line = [avg_ego_line_json_raw_score , line_json_raw_score_15.item()]
# adj_json_line = [avg_ego_line_adj_json_raw_score , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_ego_line_adj_txt_raw_score , line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_ego_line_tokenized_txt_raw_score, line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_ego_occupancy_jpg_raw_score , occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_ego_occupancy_json_raw_score , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_ego_occupancy_adj_json_raw_score , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_ego_occupancy_adj_txt_raw_score , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_ego_occupancy_tokenized_txt_raw_score, occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_ego_occupancy_ascii_txt_raw_score, occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1])   # two x-axis positions
# jitter_strength = 0.01
# # Build figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2,
#     ncols=1,
#     figsize=(10, 8),
#     sharex=False  # ensures the two subplots align vertically
# )

# # Top Plot
# for data, label in zip(dataset_line, labels_line):
#     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax1.set_xticks(x_pos)
# ax1.set_xticklabels(x_axis_line)

# ax1.set_xlabel("Maze Complexity")
# ax1.set_ylabel("Number of Correct Steps")
# ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Egocentric Output")

# # Legend centered above subplot
# ax1.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Bottom Plot
# for data, label in zip(dataset_occupancy, labels_occupancy):
#     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax2.set_xticks(x_pos)
# ax2.set_xticklabels(x_axis_occ)

# ax2.set_xlabel("Maze Complexity")
# ax2.set_ylabel("Number of Correct Steps")
# ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Egocentric Output")

# # Legend centered above subplot
# ax2.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()




# NR -- Coords -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Raw Scores NR Coords 3x3
line_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 3.0, 7.0, 5.0])
line_jpg_raw_score = np.array([2.0, 1.0, 2.0, 3.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_json_raw_score = np.array([5.0, 1.0, 3.0, 1.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_tokenized_txt_raw_score = np.array([1.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0])
occupancy_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_ascii_txt_raw_score = np.array([0.0, 9.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.0])  
occupancy_jpg_raw_score = np.array([0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 1.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_tokenized_txt_raw_score = np.array([1.0, 9.0, 9.0, 9.0, 1.0, 1.0, 9.0, 13.0, 1.0, 9])
# 3x3 averages
avg_coords_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
avg_coords_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
avg_coords_line_jpg_raw_score = np.mean(line_jpg_raw_score)
avg_coords_line_json_raw_score = np.mean(line_json_raw_score)
avg_coords_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
avg_coords_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
avg_coords_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
avg_coords_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
avg_coords_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
avg_coords_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
avg_coords_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# Raw Scores NR Coords 6x6
line_adj_json_raw_score_6 = np.array([9.0, 19.0, 14.0, 13.0, 15.0, 16.0, 24.0, 9.0, 10.0, 16.0])
line_adj_txt_raw_score_6 = np.array([9.0, 8.0, 5.0, 7.0, 15.0, 21.0, 24.0, 11.0, 10.0, 10.0])
line_jpg_raw_score_6 = np.array([2.0, 2.0, 1.0, 1.0, 4.0, 1.0, 2.0, 1.0, 2.0, 1.0])
line_json_raw_score_6 = np.array([2.0, 2.0, 2.0, 4.0, 4.0, 3.0, 4.0, 4.0, 2.0, 1.0])
line_tokenized_txt_raw_score_6 = np.array([6.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 1.0, 0.0, 1.0])
occupancy_adj_json_raw_score_6 = np.array([33.0, 29.0, 69.0, 49.0, 29.0, 41.0, 49.0, 21.0, 25.0, 19.0])
occupancy_adj_txt_raw_score_6 = np.array([17.0, 37.0, 17.0, 57.0, 29.0, 17.0, 21.0, 21.0, 19.0, 19.0])
occupancy_ascii_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_raw_score_6 = np.array([1.0, 1.0, 7.0, 17.0, 1.0, 9.0, 1.0, 17.0, 1.0, 5.0])
occupancy_tokenized_txt_raw_score_6 = np.array([1.0, 1.0, 7.0, 13.0, 1.0, 9.0, 1.0, 11.0, 5.0, 5])
# 6x6 averages
avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# Raw Scores NR Coords 15x15
line_adj_json_raw_score_15 = np.array([3])
line_adj_txt_raw_score_15 = np.array([11])
line_jpg_raw_score_15 = np.array([4])
line_json_raw_score_15 = np.array([2])
line_tokenized_txt_raw_score_15 = np.array([1])
occupancy_adj_json_raw_score_15 = np.array([67])
occupancy_adj_txt_raw_score_15 = np.array([15])
occupancy_ascii_txt_raw_score_15 = np.array([0])
occupancy_jpg_raw_score_15 = np.array([0])
occupancy_json_raw_score_15 = np.array([1])
occupancy_tokenized_txt_raw_score_15 = np.array([1])

# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , line_jpg_raw_score_15.item()]
# json_line = [avg_coords_line_json_raw_score , line_json_raw_score_15.item()]
# adj_json_line = [avg_coords_line_adj_json_raw_score , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_coords_occupancy_json_raw_score , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score, occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score, occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1])   # two x-axis positions
# jitter_strength = 0.01
# # Build figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2,
#     ncols=1,
#     figsize=(10, 8),
#     sharex=False  # ensures the two subplots align vertically
# )

# # Top Plot
# for data, label in zip(dataset_line, labels_line):
#     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax1.set_xticks(x_pos)
# ax1.set_xticklabels(x_axis_line)

# ax1.set_xlabel("Maze Complexity")
# ax1.set_ylabel("Number of Correct Steps")
# ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Coordinates Output")

# # Legend centered above subplot
# ax1.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Bottom Plot
# for data, label in zip(dataset_occupancy, labels_occupancy):
#     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax2.set_xticks(x_pos)
# ax2.set_xticklabels(x_axis_occ)

# ax2.set_xlabel("Maze Complexity")
# ax2.set_ylabel("Number of Correct Steps")
# ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Coordinates Output")

# # Legend centered above subplot
# ax2.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()




# NR -- Allo -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Raw Scores NR Allo 3x3
line_adj_json_raw_score = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 4.0, 4.0, 2.0, 2.0, 4.0])
line_adj_txt_raw_score = np.array([0.0, 4.0, 0.0, 4.0, 0.0, 0.0, 4.0, 2.0, 2.0, 4.0])
line_jpg_raw_score = np.array([2.0, 0.0, 2.0, 4.0, 2.0, 2.0, 4.0, 0.0, 0.0, 0.0])
line_json_raw_score = np.array([4.0, 0.0, 4.0, 0.0, 2.0, 4.0, 0.0, 0.0, 2.0, 0.0])
line_tokenized_txt_raw_score = np.array([0.0, 4.0, 0.0, 1.0, 0.0, 0.0, 1.0, 2.0, 0.0, 1.0])
occupancy_adj_json_raw_score = np.array([4.0, 2.0, 6.0, 8.0, 0.0, 4.0, 8.0, 4.0, 0.0, 8.0])
occupancy_adj_txt_raw_score = np.array([5.0, 2.0, 0.0, 3.0, 4.0, 2.0, 3.0, 4.0, 0.0, 8.0])
occupancy_ascii_txt_raw_score = np.array([0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 5.0, 4.0, 4.0, 0.0])
occupancy_jpg_raw_score = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
occupancy_json_raw_score = np.array([5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 7.0])
occupancy_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 4.0, 1.0, 1.0, 0.0, 1.0, 0.0, 8])
# 3x3 averages
avg_allo_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
avg_allo_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
avg_allo_line_jpg_raw_score = np.mean(line_jpg_raw_score)
avg_allo_line_json_raw_score = np.mean(line_json_raw_score)
avg_allo_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
avg_allo_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
avg_allo_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
avg_allo_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
avg_allo_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
avg_allo_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
avg_allo_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
#Raw Scores NR Allo 6x6
line_adj_json_raw_score_6 = np.array([3.0, 1.0, 3.0, 5.0, 0.0, 4.0, 2.0, 10.0, 2.0, 3.0])
line_adj_txt_raw_score_6 = np.array([4.0, 0.0, 4.0, 5.0, 3.0, 1.0, 0.0, 6.0, 0.0, 1.0])
line_jpg_raw_score_6 = np.array([1.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0])
line_json_raw_score_6 = np.array([2.0, 1.0, 0.0, 5.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0])
line_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 1.0, 3.0, 1.0, 0.0, 1.0, 0.0, 2.0])
occupancy_adj_json_raw_score_6 = np.array([6.0, 2.0, 5.0, 10.0, 4.0, 2.0, 4.0, 10.0, 2.0, 2.0])
occupancy_adj_txt_raw_score_6 = np.array([6.0, 2.0, 6.0, 10.0, 4.0, 7.0, 4.0, 18.0, 6.0, 0.0])
occupancy_ascii_txt_raw_score_6 = np.array([2.0, 4.0, 0.0, 12.0, 0.0, 0.0, 1.0, 11.0, 0.0, 3.0])
occupancy_jpg_raw_score_6 = np.array([0.0, 0.0, 1.0, 6.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.0])
occupancy_json_raw_score_6 = np.array([0.0, 0.0, 4.0, 8.0, 0.0, 4.0, 0.0, 16.0, 0.0, 4.0])
occupancy_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 8.0, 0.0, 1])
#6x6 averages
avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# Raw Scores NR Allo 15x15
line_adj_json_raw_score_15 = np.array([0])
line_adj_txt_raw_score_15 = np.array([0])
line_jpg_raw_score_15 = np.array([np.nan])
line_json_raw_score_15 = np.array([2])
line_tokenized_txt_raw_score_15 = np.array([0])
occupancy_adj_json_raw_score_15 = np.array([2])
occupancy_adj_txt_raw_score_15 = np.array([0])
occupancy_ascii_txt_raw_score_15 = np.array([0])
occupancy_jpg_raw_score_15 = np.array([np.nan])
occupancy_json_raw_score_15 = np.array([0])
occupancy_tokenized_txt_raw_score_15 = np.array([0])

# # Dataset for top chart
# jpg_line = [avg_allo_line_jpg_raw_score , line_jpg_raw_score_15.item()]
# json_line = [avg_allo_line_json_raw_score , line_json_raw_score_15.item()]
# adj_json_line = [avg_allo_line_adj_json_raw_score , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_allo_line_adj_txt_raw_score , line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_allo_line_tokenized_txt_raw_score, line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_allo_occupancy_jpg_raw_score , occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_allo_occupancy_json_raw_score , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_allo_occupancy_adj_json_raw_score , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_allo_occupancy_adj_txt_raw_score , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_allo_occupancy_tokenized_txt_raw_score, occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_allo_occupancy_ascii_txt_raw_score, occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1])   # two x-axis positions
# jitter_strength = 0.02
# # Build figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2,
#     ncols=1,
#     figsize=(10, 8),
#     sharex=False  # ensures the two subplots align vertically
# )

# # Top Plot
# for data, label in zip(dataset_line, labels_line):
#     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax1.set_xticks(x_pos)
# ax1.set_xticklabels(x_axis_line)

# ax1.set_xlabel("Maze Complexity")
# ax1.set_ylabel("Number of Correct Steps")
# ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Allocentric Output")

# # Legend centered above subplot
# ax1.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Bottom Plot
# for data, label in zip(dataset_occupancy, labels_occupancy):
#     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax2.set_xticks(x_pos)
# ax2.set_xticklabels(x_axis_occ)

# ax2.set_xlabel("Maze Complexity")
# ax2.set_ylabel("Number of Correct Steps")
# ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Allocentric Output")

# # Legend centered above subplot
# ax2.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax2.grid(axis='y', linestyle='--', alpha=0.3)

# plt.tight_layout()
# plt.show()


# NR -- Ego -- raw scores ----------- 3x3 & 15x15 -----------------------------------
# Raw Scores NR Ego 3x3
line_adj_json_raw_score = np.array([1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_jpg_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_raw_score = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_adj_json_raw_score = np.array([0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0])
occupancy_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg_raw_score = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0])
# 3x3 averages
avg_ego_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
avg_ego_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
avg_ego_line_jpg_raw_score = np.mean(line_jpg_raw_score)
avg_ego_line_json_raw_score = np.mean(line_json_raw_score)
avg_ego_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
avg_ego_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
avg_ego_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
avg_ego_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
avg_ego_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
avg_ego_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
avg_ego_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
#Raw Scores NR Ego 6x6
line_adj_json_raw_score_6 = np.array([3.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_adj_txt_raw_score_6 = np.array([2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
line_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
occupancy_adj_json_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_adj_txt_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg_raw_score_6 = np.array([1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0])
occupancy_json_raw_score_6 = np.array([0.0, 2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0])
#6x6 averages
avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# Raw Scores NR Ego 15x15
line_adj_json_raw_score_15 = np.array([0])
line_adj_txt_raw_score_15 = np.array([2])
line_jpg_raw_score_15 = np.array([2])
line_json_raw_score_15 = np.array([2])
line_tokenized_txt_raw_score_15 = np.array([1])
occupancy_adj_json_raw_score_15 = np.array([0])
occupancy_adj_txt_raw_score_15 = np.array([4])
occupancy_ascii_txt_raw_score_15 = np.array([0])
occupancy_jpg_raw_score_15 = np.array([2])
occupancy_json_raw_score_15 = np.array([0])
occupancy_tokenized_txt_raw_score_15 = np.array([1])


# # Dataset for top chart
# jpg_line = [avg_ego_line_jpg_raw_score , line_jpg_raw_score_15.item()]
# json_line = [avg_ego_line_json_raw_score , line_json_raw_score_15.item()]
# adj_json_line = [avg_ego_line_adj_json_raw_score , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_ego_line_adj_txt_raw_score , line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_ego_line_tokenized_txt_raw_score, line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_ego_occupancy_jpg_raw_score , occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_ego_occupancy_json_raw_score , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_ego_occupancy_adj_json_raw_score , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_ego_occupancy_adj_txt_raw_score , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_ego_occupancy_tokenized_txt_raw_score, occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_ego_occupancy_ascii_txt_raw_score, occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1])   # two x-axis positions
# jitter_strength = 0.01
# # Build figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2,
#     ncols=1,
#     figsize=(10, 8),
#     sharex=False  # ensures the two subplots align vertically
# )

# # Top Plot
# for data, label in zip(dataset_line, labels_line):
#     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax1.set_xticks(x_pos)
# ax1.set_xticklabels(x_axis_line)

# ax1.set_xlabel("Maze Complexity")
# ax1.set_ylabel("Number of Correct Steps")
# ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Egocentric Output")

# # Legend centered above subplot
# ax1.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Bottom Plot
# for data, label in zip(dataset_occupancy, labels_occupancy):
#     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
#     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# ax2.set_xticks(x_pos)
# ax2.set_xticklabels(x_axis_occ)

# ax2.set_xlabel("Maze Complexity")
# ax2.set_ylabel("Number of Correct Steps")
# ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Egocentric Output")

# # Legend centered above subplot
# ax2.legend(
#     loc='best',
#     # bbox_to_anchor=(0.5, 1.18),
#     ncol=3,
#     fontsize=9
# )

# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()








# NR - EGO - 1-3 -----------acc/tokens vs. complexity -----------------------------
# line_adj_json = np.array([25.0, 0.0, 25.0])
# line_adj_txt = np.array([0.0, 0.0, 0.0])
# line_jpg = np.array([0.0, 0.0, 0.0])
# line_json = np.array([25.0, 0.0, 0.0])
# line_tokenized_txt = np.array([0.0, 0.0, 0.0])
# occupancy_adj_json = np.array([0.0, 0.0, 12.5])
# occupancy_adj_txt = np.array([0.0, 0.0, 0.0])
# occupancy_ascii_txt = np.array([0.0, 0.0, 0.0])
# occupancy_jpg = np.array([0.0, 0.0, 12.5])
# occupancy_json = np.array([0.0, 0.0, 0.0])
# occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0])

# tokens_run_3 = np.array([11, 13, 15, 13, 17, 31, 4000, 4000, 33, 79, 1029])

# x_axis = ['3x3', '7x7']

# div_line_adj_json = line_adj_json[2]/tokens_run_3[0]
# div_line_adj_txt = line_adj_txt[2]/tokens_run_3[1]
# div_line_jpg = line_jpg[2]/tokens_run_3[2]
# div_line_json = line_json[2]/tokens_run_3[3]
# div_line_tokenized_txt = line_tokenized_txt[2]/tokens_run_3[4]
# div_occupancy_adj_json = occupancy_adj_json[2]/tokens_run_3[5]
# div_occupancy_adj_txt = occupancy_adj_txt[2]/tokens_run_3[6]
# div_occupancy_ascii_txt = occupancy_ascii_txt[2]/tokens_run_3[7]
# div_occupancy_jpg = occupancy_jpg[2]/tokens_run_3[8]
# div_occupancy_json = occupancy_json[2]/tokens_run_3[9]
# div_occupancy_tokenized_txt = occupancy_tokenized_txt[2]/tokens_run_3[10]

# # 5 values belonging to complexity 3x3
# div_3x3 = [
#     div_line_adj_json,
#     div_line_adj_txt,
#     div_line_jpg,
#     div_line_json,
#     div_line_tokenized_txt
# ]
# labels_3x3 = [
#     "div_line_adj_json",
#     "div_line_adj_txt",
#     "div_line_jpg",
#     "div_line_json",
#     "div_line_tokenized_txt"
# ]

# # 6 values belonging to complexity 7x7
# div_7x7 = [
#     div_occupancy_adj_json,
#     div_occupancy_adj_txt,
#     div_occupancy_ascii_txt,
#     div_occupancy_jpg,
#     div_occupancy_json,
#     div_occupancy_tokenized_txt
# ]

# labels_7x7 = [
#     "div_occupancy_adj_json",
#     "div_occupancy_adj_txt",
#     "div_occupancy_ascii_txt",
#     "div_occupancy_jpg",
#     "div_occupancy_json",
#     "div_occupancy_tokenized_txt"
# ]

# fig, ax = plt.subplots(figsize=(8, 6))

# # x positions for the two groups
# x_pos = np.array([0, 1])   # 0 = 3x3, 1 = 7x7

# # Add jitter so points don’t overlap vertically
# jitter_3x3 = np.random.uniform(-0.05, 0.05, len(div_3x3))
# jitter_7x7 = np.random.uniform(-0.05, 0.05, len(div_7x7))
# for i, (value, label) in enumerate(zip(div_3x3, labels_3x3)):
#     ax.scatter(
#         0 + jitter_3x3[i],   # x-position with jitter
#         value,               # y-value
#         label=label,         # unique legend entry
#         s=80
#     )


# for i, (value, label) in enumerate(zip(div_7x7, labels_7x7)):
#     ax.scatter(
#         1 + jitter_7x7[i],   # x-position with jitter
#         value,
#         label=label,
#         s=80
#     )


# ax.set_xticks(x_pos)
# ax.set_xticklabels(x_axis)

# ax.set_xlabel('complexity')
# ax.set_ylabel('accuracy/outputtoken [%/token]')

# ax.set_title('Contribution of Individual Output Tokens To Accuracy, Gemini 2.5 Flash Lite, Egocentric Output, Run 3')

# ax.grid(axis='y', linestyle='--', alpha=0.3)

# ax.legend(
#     loc='lower center',
#     bbox_to_anchor=(0.5, 1.15),
#     ncol=3,
#     fontsize=9
# )

# plt.tight_layout()
# plt.show()