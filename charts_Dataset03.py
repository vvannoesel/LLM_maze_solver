import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi


x_axis_line = ['3x3', '6x6', '15x15']
x_axis_occ = ['7x7', '13x13', '31x31']

def sample_size(sigma):
    """Calculates the required sample size for a given standard deviation and margin of error."""
    Z = 1.96  # Z-score for 95% confidence level
    E = 5.0   # Margin of error
    n = (Z * sigma / E) ** 2
    return np.ceil(n)

# --- Plotting mean accuracy with stdev error bars for all types and sizes until run 10 ----------

# NR -- Coords -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Coords 3x3
# line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 42.857142857142854, 100.0, 100.0])
# line_jpg = np.array([40.0, 20.0, 40.0, 60.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
# line_json = np.array([100.0, 20.0, 60.0, 20.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
# line_tokenized_txt = np.array([20.0, 0.0, 0.0, 60.0, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 20.0])
# occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 110.00000000000001])
# occupancy_jpg = np.array([0.0, 0.0, 55.55555555555556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json = np.array([100.0, 110.00000000000001, 100.0, 110.00000000000001, 7.6923076923076925, 100.0, 110.00000000000001, 100.0, 100.0, 110.00000000000001])
# occupancy_tokenized_txt = np.array([11.11111111111111, 110.00000000000001, 100.0, 100.0, 7.6923076923076925, 11.11111111111111, 100.0, 100.0, 7.6923076923076925, 110.00000000000001])
# # Averages and std deviation 3x3
# avg_coords_line_adj_json = np.mean(line_adj_json)
# avg_coords_line_adj_txt = np.mean(line_adj_txt)
# avg_coords_line_jpg = np.mean(line_jpg)
# avg_coords_line_json = np.mean(line_json)
# avg_coords_line_tokenized_txt = np.mean(line_tokenized_txt)
# avg_coords_occupancy_adj_json = np.mean(occupancy_adj_json)
# avg_coords_occupancy_adj_txt = np.mean(occupancy_adj_txt)
# avg_coords_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
# avg_coords_occupancy_jpg = np.mean(occupancy_jpg)
# avg_coords_occupancy_json = np.mean(occupancy_json)
# avg_coords_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_coords_line_adj_json = np.std(line_adj_json)
# sd_coords_line_adj_txt = np.std(line_adj_txt)
# sd_coords_line_jpg = np.std(line_jpg)
# sd_coords_line_json = np.std(line_json)
# sd_coords_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_coords_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_coords_occupancy_jpg = np.std(occupancy_jpg)
# sd_coords_occupancy_json = np.std(occupancy_json)
# sd_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# # Accuracy NR Coords 6x6
# line_adj_json_6 = np.array([52.94117647058824, 100.0, 40.0, 44.827586206896555, 100.0, 76.19047619047619, 96.0, 81.81818181818183, 58.82352941176471, 76.19047619047619])
# line_adj_txt_6 = np.array([52.94117647058824, 42.10526315789473, 14.285714285714285, 24.137931034482758, 100.0, 100.0, 96.0, 100.0, 58.82352941176471, 47.61904761904761])
# line_jpg_6 = np.array([11.76470588235294, 10.526315789473683, 2.857142857142857, 3.4482758620689653, 26.666666666666668, 4.761904761904762, 8.0, 9.090909090909092, 11.76470588235294, 4.761904761904762])
# line_json_6 = np.array([11.76470588235294, 10.526315789473683, 5.714285714285714, 13.793103448275861, 26.666666666666668, 14.285714285714285, 16.0, 36.36363636363637, 11.76470588235294, 4.761904761904762])
# line_tokenized_txt_6 = np.array([35.294117647058826, 5.263157894736842, 2.857142857142857, 3.4482758620689653, 20.0, 4.761904761904762, 4.0, 9.090909090909092, 0.0, 4.761904761904762])
# occupancy_adj_json_6 = np.array([100.0, 78.37837837837837, 100.0, 85.96491228070175, 100.0, 100.0, 100.0, 100.0, 75.75757575757575, 46.34146341463415])
# occupancy_adj_txt_6 = np.array([51.515151515151516, 100.0, 24.637681159420293, 100.0, 100.0, 41.46341463414634, 42.857142857142854, 100.0, 57.57575757575758, 46.34146341463415])
# occupancy_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 29.82456140350877, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 80.95238095238095, 3.0303030303030303, 12.195121951219512])
# occupancy_tokenized_txt_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 22.807017543859647, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 52.38095238095239, 15.151515151515152, 12.195121951219512])
# # Averages and std deviation 6x6
# avg_coords_line_adj_json_6 = np.mean(line_adj_json_6)
# avg_coords_line_adj_txt_6 = np.mean(line_adj_txt_6)
# avg_coords_line_jpg_6 = np.mean(line_jpg_6)
# avg_coords_line_json_6 = np.mean(line_json_6)
# avg_coords_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
# avg_coords_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
# avg_coords_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
# avg_coords_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
# avg_coords_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
# avg_coords_occupancy_json_6 = np.mean(occupancy_json_6)
# avg_coords_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_coords_line_adj_json_6 = np.std(line_adj_json_6)
# sd_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_coords_line_jpg_6 = np.std(line_jpg_6)
# sd_coords_line_json_6 = np.std(line_json_6)
# sd_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_coords_occupancy_json_6 = np.std(occupancy_json_6)
# sd_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy NR Coords 15x15

# Averages and std deviation 15x15
# avg_coords_line_adj_json_15 = np.mean(line_adj_json_15)
# avg_coords_line_adj_txt_15 = np.mean(line_adj_txt_15)
# avg_coords_line_jpg_15 = np.mean(line_jpg_15)
# avg_coords_line_json_15 = np.mean(line_json_15)
# avg_coords_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
# avg_coords_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
# avg_coords_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
# avg_coords_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
# avg_coords_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
# avg_coords_occupancy_json_15 = np.mean(occupancy_json_15)
# avg_coords_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_coords_line_adj_json_15 = np.std(line_adj_json_15)
# sd_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_coords_line_jpg_15 = np.std(line_jpg_15)
# sd_coords_line_json_15 = np.std(line_json_15)
# sd_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_coords_occupancy_json_15 = np.std(occupancy_json_15)
# sd_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# # Statistical analysis
# max_sd_jpg_line = max(sd_coords_line_jpg, sd_coords_line_jpg_6)#, sd_coords_line_jpg_15)
# max_sd_jpg_occupancy = max(sd_coords_occupancy_jpg, sd_coords_occupancy_jpg_6)#, sd_coords_occupancy_jpg_15)
# max_sd_tokenized_line = max(sd_coords_line_tokenized_txt, sd_coords_line_tokenized_txt_6)#, sd_coords_line_tokenized_txt_15)
# max_sd_tokenized_occupancy = max(sd_coords_occupancy_tokenized_txt, sd_coords_occupancy_tokenized_txt_6)#, sd_coords_occupancy_tokenized_txt_15)
# max_sd_json_line = max(sd_coords_line_json, sd_coords_line_json_6)#, sd_coords_line_json_15)
# max_sd_json_occupancy = max(sd_coords_occupancy_json, sd_coords_occupancy_json_6)#, sd_coords_occupancy_json_15)
# max_sd_adj_txt_line = max(sd_coords_line_adj_txt, sd_coords_line_adj_txt_6)#, sd_coords_line_adj_txt_15)
# max_sd_adj_txt_occupancy = max(sd_coords_occupancy_adj_txt, sd_coords_occupancy_adj_txt_6)#, sd_coords_occupancy_adj_txt_15)
# max_sd_adj_json_line = max(sd_coords_line_adj_json, sd_coords_line_adj_json_6)#, sd_coords_line_adj_json_15)
# max_sd_adj_json_occupancy = max(sd_coords_occupancy_adj_json, sd_coords_occupancy_adj_json_6)#, sd_coords_occupancy_adj_json_15)
# max_sd_ascii_occupancy = max(sd_coords_occupancy_ascii_txt, sd_coords_occupancy_ascii_txt_6)#, sd_coords_occupancy_ascii_txt_15)
# n_line_jpg = sample_size(max_sd_jpg_line)
# n_occupancy_jpg = sample_size(max_sd_jpg_occupancy)
# n_line_tokenized_txt = sample_size(max_sd_tokenized_line)
# n_occupancy_tokenized_txt = sample_size(max_sd_tokenized_occupancy)
# n_line_json = sample_size(max_sd_json_line)
# n_occupancy_json = sample_size(max_sd_json_occupancy)
# n_line_adj_txt = sample_size(max_sd_adj_txt_line)
# n_occupancy_adj_txt = sample_size(max_sd_adj_txt_occupancy)
# n_line_adj_json = sample_size(max_sd_adj_json_line)
# n_occupancy_adj_json = sample_size(max_sd_adj_json_occupancy)
# n_occupancy_ascii_txt = sample_size(max_sd_ascii_occupancy)
# representations = [
#     "Line Adj JSON",
#     "Line Adj TXT",
#     "Line JPG",
#     "Line JSON",
#     "Line Tokenized TXT",
#     "Occupancy Adj JSON",
#     "Occupancy Adj TXT",
#     "Occupancy ASCII TXT",
#     "Occupancy JPG",
#     "Occupancy JSON",
#     "Occupancy Tokenized TXT"
# ]

# sample_sizes = [
#     n_line_adj_json,
#     n_line_adj_txt,
#     n_line_jpg,
#     n_line_json,
#     n_line_tokenized_txt,
#     n_occupancy_adj_json,
#     n_occupancy_adj_txt,
#     n_occupancy_ascii_txt,
#     n_occupancy_jpg,
#     n_occupancy_json,
#     n_occupancy_tokenized_txt]

# std_3x3 = [
#     sd_coords_line_adj_json,
#     sd_coords_line_adj_txt,
#     sd_coords_line_jpg,
#     sd_coords_line_json,
#     sd_coords_line_tokenized_txt,
#     sd_coords_occupancy_adj_json,
#     sd_coords_occupancy_adj_txt,
#     sd_coords_occupancy_ascii_txt,
#     sd_coords_occupancy_jpg,
#     sd_coords_occupancy_json,
#     sd_coords_occupancy_tokenized_txt]

# std_6x6 = [
#     sd_coords_line_adj_json_6,
#     sd_coords_line_adj_txt_6,
#     sd_coords_line_jpg_6,
#     sd_coords_line_json_6,
#     sd_coords_line_tokenized_txt_6,
#     sd_coords_occupancy_adj_json_6,
#     sd_coords_occupancy_adj_txt_6,
#     sd_coords_occupancy_ascii_txt_6,
#     sd_coords_occupancy_jpg_6,
#     sd_coords_occupancy_json_6,
#     sd_coords_occupancy_tokenized_txt_6]

# std_15x15 = [
#     sd_coords_line_adj_json_15,
#     sd_coords_line_adj_txt_15,
#     sd_coords_line_jpg_15,
#     sd_coords_line_json_15,
#     sd_coords_line_tokenized_txt_15,
#     sd_coords_occupancy_adj_json_15,
#     sd_coords_occupancy_adj_txt_15,
#     sd_coords_occupancy_ascii_txt_15,
#     sd_coords_occupancy_jpg_15,
#     sd_coords_occupancy_json_15,
#     sd_coords_occupancy_tokenized_txt_15]

# df = pd.DataFrame({
#     "Representation": representations,
#     "Sample Size": sample_sizes,
#     "Std Dev 3x3": std_3x3,
#     "Std Dev 6x6": std_6x6,
#     "Std Dev 15x15": std_15x15
# })

# # Create table image

# fig, ax = plt.subplots(figsize=(12, 6))
# ax.axis("off")

# table = ax.table(
#     cellText=df.values,
#     colLabels=df.columns,
#     loc="center",
#     cellLoc="center"
# )

# table.auto_set_font_size(False)
# table.set_fontsize(10)
# table.scale(1.2, 1.5)

# plt.tight_layout()
# plt.show()



# # Top plot data
# means_line = [
#     [avg_coords_line_adj_json,       avg_coords_line_adj_json_6,       0],#line_adj_json_15],
#     [avg_coords_line_adj_txt,        avg_coords_line_adj_txt_6,        0],#line_adj_txt_15],
#     [avg_coords_line_jpg,            avg_coords_line_jpg_6,            0],#line_jpg_15],
#     [avg_coords_line_json,           avg_coords_line_json_6,           0],#line_json_15],
#     [avg_coords_line_tokenized_txt,  avg_coords_line_tokenized_txt_6,  0]#line_tokenized_txt_15]
# ]

# std_line = [
#     [sd_coords_line_adj_json,       sd_coords_line_adj_json_6,       0], #sd_coords_line_adj_json_15],
#     [sd_coords_line_adj_txt,        sd_coords_line_adj_txt_6,        0], #sd_coords_line_adj_txt_15],
#     [sd_coords_line_jpg,            sd_coords_line_jpg_6,            0], #sd_coords_line_jpg_15],
#     [sd_coords_line_json,           sd_coords_line_json_6,           0], #sd_coords_line_json_15],
#     [sd_coords_line_tokenized_txt,  sd_coords_line_tokenized_txt_6,  0]  #sd_coords_line_tokenized_txt_15
# ]

# labels_line = [
#     "Line Adjacency JSON",
#     "Line Adjacency txt",
#     "Line JPG",
#     "Line JSON",
#     "Line Tokenized"
# ]

# # Bottom plot data
# means_occ = [
#     [avg_coords_occupancy_adj_json,       avg_coords_occupancy_adj_json_6,       0],#occupancy_adj_json_15],
#     [avg_coords_occupancy_adj_txt,        avg_coords_occupancy_adj_txt_6,        0],#occupancy_adj_txt_15],
#     [avg_coords_occupancy_ascii_txt,      avg_coords_occupancy_ascii_txt_6,      0],#occupancy_ascii_txt_15],
#     [avg_coords_occupancy_jpg,            avg_coords_occupancy_jpg_6,            0],#occupancy_jpg_15],
#     [avg_coords_occupancy_json,           avg_coords_occupancy_json_6,           0],#occupancy_json_15],
#     [avg_coords_occupancy_tokenized_txt,  avg_coords_occupancy_tokenized_txt_6,  0]#occupancy_tokenized_txt_15]
# ]

# std_occ = [
#     [sd_coords_occupancy_adj_json,       sd_coords_occupancy_adj_json_6,       0], #sd_coords_occupancy_adj_json_15],
#     [sd_coords_occupancy_adj_txt,        sd_coords_occupancy_adj_txt_6,        0], #sd_coords_occupancy_adj_txt_15],
#     [sd_coords_occupancy_ascii_txt,      sd_coords_occupancy_ascii_txt_6,      0], #sd_coords_occupancy_ascii_txt_15],
#     [sd_coords_occupancy_jpg,            sd_coords_occupancy_jpg_6,            0], #sd_coords_occupancy_jpg_15],
#     [sd_coords_occupancy_json,           sd_coords_occupancy_json_6,           0], #sd_coords_occupancy_json_15],
#     [sd_coords_occupancy_tokenized_txt,  sd_coords_occupancy_tokenized_txt_6,  0] #sd_coords_occupancy_tokenized_txt_15
# ]

# labels_occ = [
#     "Occupancy Adjacency JSON",
#     "Occupancy Adjacency txt",
#     "Occupancy ASCII",
#     "Occupancy JPG",
#     "Occupancy JSON",
#     "Occupancy Tokenized"
# ]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02
# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line, std_line, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax1.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel("Complexity")
# ax1.set_ylabel("Accuracy [%]")
# ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Coordinates Output")
# ax1.legend(loc='best')
# ax1.grid(axis='y', linestyle='--', alpha=0.3)

# # Create bottom plot
# for means, stds, label in zip(means_occ, std_occ, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_occ[1]))
#     ax2.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_axis_occ)
# ax2.set_xlabel("Complexity")
# ax2.set_ylabel("Accuracy [%]")
# ax2.set_title("Mean Accuracy Per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Coordinates Output")
# ax2.legend(loc='best')
# ax2.grid(axis='y', linestyle='--', alpha=0.3)

# plt.tight_layout()
# plt.show()


# NR -- Allo -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Allo 3x3
# line_adj_json = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 100.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
# line_adj_txt = np.array([0.0, 100.0, 0.0, 100.0, 0.0, 0.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
# line_jpg = np.array([50.0, 0.0, 50.0, 100.0, 33.33333333333333, 50.0, 100.0, 0.0, 0.0, 0.0])
# line_json = np.array([100.0, 0.0, 100.0, 0.0, 33.33333333333333, 100.0, 0.0, 0.0, 33.33333333333333, 0.0])
# line_tokenized_txt = np.array([0.0, 100.0, 0.0, 25.0, 0.0, 0.0, 25.0, 33.33333333333333, 0.0, 25.0])
# occupancy_adj_json = np.array([50.0, 25.0, 75.0, 110.00000000000001, 0.0, 50.0, 110.00000000000001, 33.33333333333333, 0.0, 110.00000000000001])
# occupancy_adj_txt = np.array([62.5, 25.0, 0.0, 37.5, 33.33333333333333, 25.0, 37.5, 33.33333333333333, 0.0, 110.00000000000001])
# occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 62.5, 33.33333333333333, 33.33333333333333, 0.0])
# occupancy_jpg = np.array([12.5, 0.0, 12.5, 0.0, 8.333333333333332, 12.5, 12.5, 8.333333333333332, 8.333333333333332, 0.0])
# occupancy_json = np.array([62.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 33.33333333333333, 0.0, 87.5])
# occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 50.0, 8.333333333333332, 12.5, 0.0, 8.333333333333332, 0.0, 110.00000000000001])
# # Averages and std deviation 3x3
# avg_coords_line_adj_json = np.mean(line_adj_json)
# avg_coords_line_adj_txt = np.mean(line_adj_txt)
# avg_coords_line_jpg = np.mean(line_jpg)
# avg_coords_line_json = np.mean(line_json)
# avg_coords_line_tokenized_txt = np.mean(line_tokenized_txt)
# avg_coords_occupancy_adj_json = np.mean(occupancy_adj_json)
# avg_coords_occupancy_adj_txt = np.mean(occupancy_adj_txt)
# avg_coords_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
# avg_coords_occupancy_jpg = np.mean(occupancy_jpg)
# avg_coords_occupancy_json = np.mean(occupancy_json)
# avg_coords_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_coords_line_adj_json = np.std(line_adj_json)
# sd_coords_line_adj_txt = np.std(line_adj_txt)
# sd_coords_line_jpg = np.std(line_jpg)
# sd_coords_line_json = np.std(line_json)
# sd_coords_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_coords_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_coords_occupancy_jpg = np.std(occupancy_jpg)
# sd_coords_occupancy_json = np.std(occupancy_json)
# sd_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# # Accuracy NR Allo 6x6
# line_adj_json_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 0.0, 20.0, 8.333333333333332, 110.00000000000001, 12.5, 15.0])
# line_adj_txt_6 = np.array([25.0, 0.0, 11.76470588235294, 17.857142857142858, 21.428571428571427, 5.0, 0.0, 60.0, 0.0, 5.0])
# line_jpg_6 = np.array([6.25, 0.0, 2.941176470588235, 0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 10.0])
# line_json_6 = np.array([12.5, 5.555555555555555, 0.0, 17.857142857142858, 21.428571428571427, 0.0, 12.5, 0.0, 18.75, 0.0])
# line_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 3.571428571428571, 21.428571428571427, 5.0, 0.0, 10.0, 0.0, 10.0])
# occupancy_adj_json_6 = np.array([18.75, 5.555555555555555, 7.352941176470589, 17.857142857142858, 14.285714285714285, 5.0, 8.333333333333332, 50.0, 6.25, 5.0])
# occupancy_adj_txt_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 14.285714285714285, 17.5, 8.333333333333332, 90.0, 18.75, 0.0])
# occupancy_ascii_txt_6 = np.array([6.25, 11.11111111111111, 0.0, 21.428571428571427, 0.0, nan, 2.083333333333333, 55.00000000000001, 0.0, 7.5])
# occupancy_jpg_6 = np.array([0.0, 0.0, 1.4705882352941175, 10.714285714285714, 3.571428571428571, 2.5, 4.166666666666666, 5.0, 3.125, 0.0])
# occupancy_json_6 = np.array([0.0, 0.0, 5.88235294117647, 14.285714285714285, 0.0, 10.0, 0.0, 80.0, 0.0, 10.0])
# occupancy_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 14.285714285714285, nan, 0.0, 0.0, 40.0, 0.0, 2.5])
# # Averages and std deviation 6x6
# avg_coords_line_adj_json_6 = np.mean(line_adj_json_6)
# avg_coords_line_adj_txt_6 = np.mean(line_adj_txt_6)
# avg_coords_line_jpg_6 = np.mean(line_jpg_6)
# avg_coords_line_json_6 = np.mean(line_json_6)
# avg_coords_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
# avg_coords_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
# avg_coords_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
# avg_coords_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
# avg_coords_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
# avg_coords_occupancy_json_6 = np.mean(occupancy_json_6)
# avg_coords_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_coords_line_adj_json_6 = np.std(line_adj_json_6)
# sd_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_coords_line_jpg_6 = np.std(line_jpg_6)
# sd_coords_line_json_6 = np.std(line_json_6)
# sd_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_coords_occupancy_json_6 = np.std(occupancy_json_6)
# sd_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# # Accuracy NR Allo 15x15

# # Averages and std deviation 15x15
# avg_coords_line_adj_json_15 = np.mean(line_adj_json_15)
# avg_coords_line_adj_txt_15 = np.mean(line_adj_txt_15)
# avg_coords_line_jpg_15 = np.mean(line_jpg_15)
# avg_coords_line_json_15 = np.mean(line_json_15)
# avg_coords_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
# avg_coords_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
# avg_coords_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
# avg_coords_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
# avg_coords_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
# avg_coords_occupancy_json_15 = np.mean(occupancy_json_15)
# avg_coords_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_coords_line_adj_json_15 = np.std(line_adj_json_15)
# sd_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_coords_line_jpg_15 = np.std(line_jpg_15)
# sd_coords_line_json_15 = np.std(line_json_15)
# sd_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_coords_occupancy_json_15 = np.std(occupancy_json_15)
# sd_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)


# # Top plot data
# means_line = [
#     [avg_coords_line_adj_json,       avg_coords_line_adj_json_6,       0],#line_adj_json_15],
#     [avg_coords_line_adj_txt,        avg_coords_line_adj_txt_6,        0],#line_adj_txt_15],
#     [avg_coords_line_jpg,            avg_coords_line_jpg_6,            0],#line_jpg_15],
#     [avg_coords_line_json,           avg_coords_line_json_6,           0],#line_json_15],
#     [avg_coords_line_tokenized_txt,  avg_coords_line_tokenized_txt_6,  0]#line_tokenized_txt_15]
# ]

# std_line = [
#     [sd_coords_line_adj_json,       sd_coords_line_adj_json_6,       0], #sd_coords_line_adj_json_15],
#     [sd_coords_line_adj_txt,        sd_coords_line_adj_txt_6,        0], #sd_coords_line_adj_txt_15],
#     [sd_coords_line_jpg,            sd_coords_line_jpg_6,            0], #sd_coords_line_jpg_15],
#     [sd_coords_line_json,           sd_coords_line_json_6,           0], #sd_coords_line_json_15],
#     [sd_coords_line_tokenized_txt,  sd_coords_line_tokenized_txt_6,  0]  #sd_coords_line_tokenized_txt_15
# ]

# labels_line = [
#     "Line Adjacency JSON",
#     "Line Adjacency txt",
#     "Line JPG",
#     "Line JSON",
#     "Line Tokenized"
# ]

# # Bottom plot data
# means_occ = [
#     [avg_coords_occupancy_adj_json,       avg_coords_occupancy_adj_json_6,       0],#occupancy_adj_json_15],
#     [avg_coords_occupancy_adj_txt,        avg_coords_occupancy_adj_txt_6,        0],#occupancy_adj_txt_15],
#     [avg_coords_occupancy_ascii_txt,      avg_coords_occupancy_ascii_txt_6,      0],#occupancy_ascii_txt_15],
#     [avg_coords_occupancy_jpg,            avg_coords_occupancy_jpg_6,            0],#occupancy_jpg_15],
#     [avg_coords_occupancy_json,           avg_coords_occupancy_json_6,           0],#occupancy_json_15],
#     [avg_coords_occupancy_tokenized_txt,  avg_coords_occupancy_tokenized_txt_6,  0]#occupancy_tokenized_txt_15]
# ]

# std_occ = [
#     [sd_coords_occupancy_adj_json,       sd_coords_occupancy_adj_json_6,       0], #sd_coords_occupancy_adj_json_15],
#     [sd_coords_occupancy_adj_txt,        sd_coords_occupancy_adj_txt_6,        0], #sd_coords_occupancy_adj_txt_15],
#     [sd_coords_occupancy_ascii_txt,      sd_coords_occupancy_ascii_txt_6,      0], #sd_coords_occupancy_ascii_txt_15],
#     [sd_coords_occupancy_jpg,            sd_coords_occupancy_jpg_6,            0], #sd_coords_occupancy_jpg_15],
#     [sd_coords_occupancy_json,           sd_coords_occupancy_json_6,           0], #sd_coords_occupancy_json_15],
#     [sd_coords_occupancy_tokenized_txt,  sd_coords_occupancy_tokenized_txt_6,  0] #sd_coords_occupancy_tokenized_txt_15
# ]

# labels_occ = [
#     "Occupancy Adjacency JSON",
#     "Occupancy Adjacency txt",
#     "Occupancy ASCII",
#     "Occupancy JPG",
#     "Occupancy JSON",
#     "Occupancy Tokenized"
# ]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02
# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# Create top plot
# for means, stds, label in zip(means_line, std_line, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax1.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel("Complexity")
# ax1.set_ylabel("Accuracy [%]")
# ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Allocentric Output")
# ax1.legend(loc='best')
# ax1.grid(axis='y', linestyle='--', alpha=0.3)

# # Create bottom plot
# for means, stds, label in zip(means_occ, std_occ, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax2.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_axis_occ)
# ax2.set_xlabel("Complexity")
# ax2.set_ylabel("Accuracy [%]")
# ax2.set_title("Mean Accuracy Per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Allocentric Output")
# ax2.legend(loc='best')
# ax2.grid(axis='y', linestyle='--', alpha=0.3)

# plt.tight_layout()
# plt.show()

# # NR -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Accuracy NR Ego 3x3
# line_adj_json = np.array([25.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_json = np.array([25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_adj_json = np.array([0.0, 0.0, 12.5, 0.0, 8.333333333333332, 0.0, 0.0, 0.0, 8.333333333333332, 0.0])
# occupancy_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_ascii_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg = np.array([0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# # Averages and std deviation 3x3
# avg_coords_line_adj_json = np.mean(line_adj_json)
# avg_coords_line_adj_txt = np.mean(line_adj_txt)
# avg_coords_line_jpg = np.mean(line_jpg)
# avg_coords_line_json = np.mean(line_json)
# avg_coords_line_tokenized_txt = np.mean(line_tokenized_txt)
# avg_coords_occupancy_adj_json = np.mean(occupancy_adj_json)
# avg_coords_occupancy_adj_txt = np.mean(occupancy_adj_txt)
# avg_coords_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
# avg_coords_occupancy_jpg = np.mean(occupancy_jpg)
# avg_coords_occupancy_json = np.mean(occupancy_json)
# avg_coords_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_coords_line_adj_json = np.std(line_adj_json)
# sd_coords_line_adj_txt = np.std(line_adj_txt)
# sd_coords_line_jpg = np.std(line_jpg)
# sd_coords_line_json = np.std(line_json)
# sd_coords_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_coords_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_coords_occupancy_jpg = np.std(occupancy_jpg)
# sd_coords_occupancy_json = np.std(occupancy_json)
# sd_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# # Accuracy NR Ego 6x6
# line_adj_json_6 = np.array([18.75, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_adj_txt_6 = np.array([12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 0.0, 0.0, 4.166666666666666, 0.0, 0.0, 0.0])
# line_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.25, 0.0])
# occupancy_adj_json_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_adj_txt_6 = np.array([0.0, 2.7777777777777777, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg_6 = np.array([3.125, 2.7777777777777777, 0.0, 0.0, 3.571428571428571, 0.0, 2.083333333333333, 0.0, 0.0, 0.0])
# occupancy_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 3.571428571428571, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# # Averages and std deviation 6x6
# avg_coords_line_adj_json_6 = np.mean(line_adj_json_6)
# avg_coords_line_adj_txt_6 = np.mean(line_adj_txt_6)
# avg_coords_line_jpg_6 = np.mean(line_jpg_6)
# avg_coords_line_json_6 = np.mean(line_json_6)
# avg_coords_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
# avg_coords_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
# avg_coords_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
# avg_coords_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
# avg_coords_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
# avg_coords_occupancy_json_6 = np.mean(occupancy_json_6)
# avg_coords_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_coords_line_adj_json_6 = np.std(line_adj_json_6)
# sd_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_coords_line_jpg_6 = np.std(line_jpg_6)
# sd_coords_line_json_6 = np.std(line_json_6)
# sd_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_coords_occupancy_json_6 = np.std(occupancy_json_6)
# sd_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# # Accuracy NR Ego 15x15

# # Averages and std deviation 15x15
# avg_coords_line_adj_json_15 = np.mean(line_adj_json_15)
# avg_coords_line_adj_txt_15 = np.mean(line_adj_txt_15)
# avg_coords_line_jpg_15 = np.mean(line_jpg_15)
# avg_coords_line_json_15 = np.mean(line_json_15)
# avg_coords_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
# avg_coords_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
# avg_coords_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
# avg_coords_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
# avg_coords_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
# avg_coords_occupancy_json_15 = np.mean(occupancy_json_15)
# avg_coords_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_coords_line_adj_json_15 = np.std(line_adj_json_15)
# sd_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_coords_line_jpg_15 = np.std(line_jpg_15)
# sd_coords_line_json_15 = np.std(line_json_15)
# sd_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_coords_occupancy_json_15 = np.std(occupancy_json_15)
# sd_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)


# # Top plot data
# means_line = [
#     [avg_coords_line_adj_json,       avg_coords_line_adj_json_6,       0],#line_adj_json_15],
#     [avg_coords_line_adj_txt,        avg_coords_line_adj_txt_6,        0],#line_adj_txt_15],
#     [avg_coords_line_jpg,            avg_coords_line_jpg_6,            0],#line_jpg_15],
#     [avg_coords_line_json,           avg_coords_line_json_6,           0],#line_json_15],
#     [avg_coords_line_tokenized_txt,  avg_coords_line_tokenized_txt_6,  0]#line_tokenized_txt_15]
# ]

# std_line = [
#     [sd_coords_line_adj_json,       sd_coords_line_adj_json_6,       0], #sd_coords_line_adj_json_15],
#     [sd_coords_line_adj_txt,        sd_coords_line_adj_txt_6,        0], #sd_coords_line_adj_txt_15],
#     [sd_coords_line_jpg,            sd_coords_line_jpg_6,            0], #sd_coords_line_jpg_15],
#     [sd_coords_line_json,           sd_coords_line_json_6,           0], #sd_coords_line_json_15],
#     [sd_coords_line_tokenized_txt,  sd_coords_line_tokenized_txt_6,  0]  #sd_coords_line_tokenized_txt_15
# ]

# labels_line = [
#     "Line Adjacency JSON",
#     "Line Adjacency txt",
#     "Line JPG",
#     "Line JSON",
#     "Line Tokenized"
# ]

# # Bottom plot data
# means_occ = [
#     [avg_coords_occupancy_adj_json,       avg_coords_occupancy_adj_json_6,       0],#occupancy_adj_json_15],
#     [avg_coords_occupancy_adj_txt,        avg_coords_occupancy_adj_txt_6,        0],#occupancy_adj_txt_15],
#     [avg_coords_occupancy_ascii_txt,      avg_coords_occupancy_ascii_txt_6,      0],#occupancy_ascii_txt_15],
#     [avg_coords_occupancy_jpg,            avg_coords_occupancy_jpg_6,            0],#occupancy_jpg_15],
#     [avg_coords_occupancy_json,           avg_coords_occupancy_json_6,           0],#occupancy_json_15],
#     [avg_coords_occupancy_tokenized_txt,  avg_coords_occupancy_tokenized_txt_6,  0]#occupancy_tokenized_txt_15]
# ]

# std_occ = [
#     [sd_coords_occupancy_adj_json,       sd_coords_occupancy_adj_json_6,       0], #sd_coords_occupancy_adj_json_15],
#     [sd_coords_occupancy_adj_txt,        sd_coords_occupancy_adj_txt_6,        0], #sd_coords_occupancy_adj_txt_15],
#     [sd_coords_occupancy_ascii_txt,      sd_coords_occupancy_ascii_txt_6,      0], #sd_coords_occupancy_ascii_txt_15],
#     [sd_coords_occupancy_jpg,            sd_coords_occupancy_jpg_6,            0], #sd_coords_occupancy_jpg_15],
#     [sd_coords_occupancy_json,           sd_coords_occupancy_json_6,           0], #sd_coords_occupancy_json_15],
#     [sd_coords_occupancy_tokenized_txt,  sd_coords_occupancy_tokenized_txt_6,  0] #sd_coords_occupancy_tokenized_txt_15
# ]

# labels_occ = [
#     "Occupancy Adjacency JSON",
#     "Occupancy Adjacency txt",
#     "Occupancy ASCII",
#     "Occupancy JPG",
#     "Occupancy JSON",
#     "Occupancy Tokenized"
# ]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02

# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# Create top plot
# for means, stds, label in zip(means_line, std_line, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax1.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel("Complexity")
# ax1.set_ylabel("Accuracy [%]")
# ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Egocentric Output")
# ax1.legend(loc='best')
# ax1.grid(axis='y', linestyle='--', alpha=0.3)

# Create bottom plot
# for means, stds, label in zip(means_occ, std_occ, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax2.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_axis_occ)
# ax2.set_xlabel("Complexity")
# ax2.set_ylabel("Accuracy [%]")
# ax2.set_title("Mean Accuracy Per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Egocentric Output")
# ax2.legend(loc='best')
# ax2.grid(axis='y', linestyle='--', alpha=0.3)

# plt.tight_layout()
# plt.show()



# # R -- Coords -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Coords 3x3
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg = np.array([40.0, 100.0, 100.0, 100.0, 28.57142857142857, 40.0, 40.0, 100.0, 100.0, 100.0])
line_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([22.22222222222222, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 46.15384615384615, 77.77777777777779])
occupancy_jpg = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556, 0.0, 7.6923076923076925, 11.11111111111111, 33.33333333333333, 0.0, 7.6923076923076925, 100.0])
occupancy_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 3x3
avg_coords_line_adj_json = np.mean(line_adj_json)
avg_coords_line_adj_txt = np.mean(line_adj_txt)
avg_coords_line_jpg = np.mean(line_jpg)
avg_coords_line_json = np.mean(line_json)
avg_coords_line_tokenized_txt = np.mean(line_tokenized_txt)
avg_coords_occupancy_adj_json = np.mean(occupancy_adj_json)
avg_coords_occupancy_adj_txt = np.mean(occupancy_adj_txt)
avg_coords_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
avg_coords_occupancy_jpg = np.mean(occupancy_jpg)
avg_coords_occupancy_json = np.mean(occupancy_json)
avg_coords_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
sd_coords_line_adj_json = np.std(line_adj_json)
sd_coords_line_adj_txt = np.std(line_adj_txt)
sd_coords_line_jpg = np.std(line_jpg)
sd_coords_line_json = np.std(line_json)
sd_coords_line_tokenized_txt = np.std(line_tokenized_txt)
sd_coords_occupancy_adj_json = np.std(occupancy_adj_json)
sd_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
sd_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
sd_coords_occupancy_jpg = np.std(occupancy_jpg)
sd_coords_occupancy_json = np.std(occupancy_json)
sd_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# Accuracy R Coords 6x6
line_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt_6 = np.array([24.242424242424242, 32.432432432432435, 11.594202898550725, 1.7543859649122806, 31.03448275862069, 2.4390243902439024, 2.0408163265306123, 0.0, 27.27272727272727, 2.4390243902439024])
occupancy_jpg_6 = np.array([0.0, 2.7027027027027026, 0.0, 0.0, 0.0, 2.4390243902439024, 0.0, 0.0, 0.0, 0.0])
occupancy_json_6 = np.array([27.27272727272727, 48.64864864864865, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 60.60606060606061, 100.0])
occupancy_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 6x6
avg_coords_line_adj_json_6 = np.mean(line_adj_json_6)
avg_coords_line_adj_txt_6 = np.mean(line_adj_txt_6)
avg_coords_line_jpg_6 = np.mean(line_jpg_6)
avg_coords_line_json_6 = np.mean(line_json_6)
avg_coords_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
avg_coords_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
avg_coords_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
avg_coords_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
avg_coords_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
avg_coords_occupancy_json_6 = np.mean(occupancy_json_6)
avg_coords_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
sd_coords_line_adj_json_6 = np.std(line_adj_json_6)
sd_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
sd_coords_line_jpg_6 = np.std(line_jpg_6)
sd_coords_line_json_6 = np.std(line_json_6)
sd_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
sd_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
sd_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
sd_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
sd_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
sd_coords_occupancy_json_6 = np.std(occupancy_json_6)
sd_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy R Coords 15x15
line_adj_json_15 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt_15 = np.array([19.083969465648856, 14.492753623188406, 51.798561151079134, 100.0, 60.629921259842526, 92.07920792079209, 100.0, 62.02531646, 46.616541353383454, 100.0])
line_jpg_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_15 = np.array([23.66412213740458, 15.942028985507244, 7.194244604316546, 7.017543859649122, 12.598425196850393, 9.900990099009901, 56.71641791044776, 50.63291139240506, 1.5037593984962405, 42.5531914893617])
line_tokenized_txt_15 = np.array([96.18320610687023, 100.0, 100.0, 100.0, 92.1259842519685, 22.772277227722775, 100.0, 62.0253164556962, 100.0, 100.0])
occupancy_adj_json_15 = np.array([100.0, 100.0, 68.95306859205776, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt_15 = np.array([34.099616858237546, 15.328467153284672, 24.90974729241877, 29.20353982300885, 12.25296442687747, 42.28855721393035, 3.7593984962406015, 57.961783439490446, 46.41509433962264, 95.6989247311828])
occupancy_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.301075268817205])
occupancy_jpg_15 = np.array([1.9157088122605364, 4.37956204379562, 1.083032490974729, 0.8849557522123894, 0.3952569169960474, 0.0, 0.7518796992481203, 0.0, 0.0, 0.0])
occupancy_json_15 = np.array([11.877394636015326, 35.03649635036496, 1.8050541516245486, 15.04424778761062, 3.557312252964427, 21.393034825870647, 30.075187969924812, 15.92356687898089, 7.169811320754717, 33.33333333333333])
occupancy_tokenized_txt_15 = np.array([39.46360153256705, 100.0, 7.581227436823104, 100.0, 7.905138339920949, 7.462686567164178, 100.0, 13.375796178343949, 6.415094339622642, 11.827956989247312])
# Averages and std deviation 15x15
avg_coords_line_adj_json_15 = np.mean(line_adj_json_15)
avg_coords_line_adj_txt_15 = np.mean(line_adj_txt_15)
avg_coords_line_jpg_15 = np.mean(line_jpg_15)
avg_coords_line_json_15 = np.mean(line_json_15)
avg_coords_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
avg_coords_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
avg_coords_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
avg_coords_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
avg_coords_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
avg_coords_occupancy_json_15 = np.mean(occupancy_json_15)
avg_coords_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
sd_coords_line_adj_json_15 = np.std(line_adj_json_15)
sd_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
sd_coords_line_jpg_15 = np.std(line_jpg_15)
sd_coords_line_json_15 = np.std(line_json_15)
sd_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
sd_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
sd_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
sd_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
sd_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
sd_coords_occupancy_json_15 = np.std(occupancy_json_15)
sd_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# Statistical analysis
max_sd_jpg_line = max(sd_coords_line_jpg, sd_coords_line_jpg_6, sd_coords_line_jpg_15)
max_sd_jpg_occupancy = max(sd_coords_occupancy_jpg, sd_coords_occupancy_jpg_6, sd_coords_occupancy_jpg_15)
max_sd_tokenized_line = max(sd_coords_line_tokenized_txt, sd_coords_line_tokenized_txt_6, sd_coords_line_tokenized_txt_15)
max_sd_tokenized_occupancy = max(sd_coords_occupancy_tokenized_txt, sd_coords_occupancy_tokenized_txt_6)#, sd_coords_occupancy_tokenized_txt_15)
max_sd_json_line = max(sd_coords_line_json, sd_coords_line_json_6, sd_coords_line_json_15)
max_sd_json_occupancy = max(sd_coords_occupancy_json, sd_coords_occupancy_json_6, sd_coords_occupancy_json_15)
max_sd_adj_txt_line = max(sd_coords_line_adj_txt, sd_coords_line_adj_txt_6, sd_coords_line_adj_txt_15)
max_sd_adj_txt_occupancy = max(sd_coords_occupancy_adj_txt, sd_coords_occupancy_adj_txt_6, sd_coords_occupancy_adj_txt_15)
max_sd_adj_json_line = max(sd_coords_line_adj_json, sd_coords_line_adj_json_6, sd_coords_line_adj_json_15)
max_sd_adj_json_occupancy = max(sd_coords_occupancy_adj_json, sd_coords_occupancy_adj_json_6, sd_coords_occupancy_adj_json_15)
max_sd_ascii_occupancy = max(sd_coords_occupancy_ascii_txt, sd_coords_occupancy_ascii_txt_6, sd_coords_occupancy_ascii_txt_15)
n_line_jpg = sample_size(max_sd_jpg_line)
n_occupancy_jpg = sample_size(max_sd_jpg_occupancy)
n_line_tokenized_txt = sample_size(max_sd_tokenized_line)
n_occupancy_tokenized_txt = sample_size(max_sd_tokenized_occupancy)
n_line_json = sample_size(max_sd_json_line)
n_occupancy_json = sample_size(max_sd_json_occupancy)
n_line_adj_txt = sample_size(max_sd_adj_txt_line)
n_occupancy_adj_txt = sample_size(max_sd_adj_txt_occupancy)
n_line_adj_json = sample_size(max_sd_adj_json_line)
n_occupancy_adj_json = sample_size(max_sd_adj_json_occupancy)
n_occupancy_ascii_txt = sample_size(max_sd_ascii_occupancy)
print(max)
representations = [
    "Line Adj JSON",
    "Line Adj TXT",
    "Line JPG",
    "Line JSON",
    "Line Tokenized TXT",
    "Occupancy Adj JSON",
    "Occupancy Adj TXT",
    "Occupancy ASCII TXT",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized TXT"
]

sample_sizes = [
    n_line_adj_json,
    n_line_adj_txt,
    n_line_jpg,
    n_line_json,
    n_line_tokenized_txt,
    n_occupancy_adj_json,
    n_occupancy_adj_txt,
    n_occupancy_ascii_txt,
    n_occupancy_jpg,
    n_occupancy_json,
    n_occupancy_tokenized_txt]

std_3x3 = [
    sd_coords_line_adj_json,
    sd_coords_line_adj_txt,
    sd_coords_line_jpg,
    sd_coords_line_json,
    sd_coords_line_tokenized_txt,
    sd_coords_occupancy_adj_json,
    sd_coords_occupancy_adj_txt,
    sd_coords_occupancy_ascii_txt,
    sd_coords_occupancy_jpg,
    sd_coords_occupancy_json,
    sd_coords_occupancy_tokenized_txt]

std_6x6 = [
    sd_coords_line_adj_json_6,
    sd_coords_line_adj_txt_6,
    sd_coords_line_jpg_6,
    sd_coords_line_json_6,
    sd_coords_line_tokenized_txt_6,
    sd_coords_occupancy_adj_json_6,
    sd_coords_occupancy_adj_txt_6,
    sd_coords_occupancy_ascii_txt_6,
    sd_coords_occupancy_jpg_6,
    sd_coords_occupancy_json_6,
    sd_coords_occupancy_tokenized_txt_6]

std_15x15 = [
    sd_coords_line_adj_json_15,
    sd_coords_line_adj_txt_15,
    sd_coords_line_jpg_15,
    sd_coords_line_json_15,
    sd_coords_line_tokenized_txt_15,
    sd_coords_occupancy_adj_json_15,
    sd_coords_occupancy_adj_txt_15,
    sd_coords_occupancy_ascii_txt_15,
    sd_coords_occupancy_jpg_15,
    sd_coords_occupancy_json_15,
    sd_coords_occupancy_tokenized_txt_15]

df = pd.DataFrame({
    "Representation": representations,
    "Sample Size": sample_sizes,
    "Std Dev 3x3": std_3x3,
    "Std Dev 6x6": std_6x6,
    "Std Dev 15x15": std_15x15
})

# Create table image

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis("off")

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Pro Coordinates Output", fontsize=16, pad=20)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)

plt.tight_layout()
plt.show()

# Top plot data
means_line = [
    [avg_coords_line_adj_json,       avg_coords_line_adj_json_6,       0],#line_adj_json_15],
    [avg_coords_line_adj_txt,        avg_coords_line_adj_txt_6,        0],#line_adj_txt_15],
    [avg_coords_line_jpg,            avg_coords_line_jpg_6,            0],#line_jpg_15],
    [avg_coords_line_json,           avg_coords_line_json_6,           0],#line_json_15],
    [avg_coords_line_tokenized_txt,  avg_coords_line_tokenized_txt_6,  0]#line_tokenized_txt_15]
]

std_line = [
    [sd_coords_line_adj_json,       sd_coords_line_adj_json_6,       0], #sd_coords_line_adj_json_15],
    [sd_coords_line_adj_txt,        sd_coords_line_adj_txt_6,        0], #sd_coords_line_adj_txt_15],
    [sd_coords_line_jpg,            sd_coords_line_jpg_6,            0], #sd_coords_line_jpg_15],
    [sd_coords_line_json,           sd_coords_line_json_6,           0], #sd_coords_line_json_15],
    [sd_coords_line_tokenized_txt,  sd_coords_line_tokenized_txt_6,  0]  #sd_coords_line_tokenized_txt_15
]

labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data
means_occ = [
    [avg_coords_occupancy_adj_json,       avg_coords_occupancy_adj_json_6,       0],#occupancy_adj_json_15],
    [avg_coords_occupancy_adj_txt,        avg_coords_occupancy_adj_txt_6,        0],#occupancy_adj_txt_15],
    [avg_coords_occupancy_ascii_txt,      avg_coords_occupancy_ascii_txt_6,      0],#occupancy_ascii_txt_15],
    [avg_coords_occupancy_jpg,            avg_coords_occupancy_jpg_6,            0],#occupancy_jpg_15],
    [avg_coords_occupancy_json,           avg_coords_occupancy_json_6,           0],#occupancy_json_15],
    [avg_coords_occupancy_tokenized_txt,  avg_coords_occupancy_tokenized_txt_6,  0]#occupancy_tokenized_txt_15]
]

std_occ = [
    [sd_coords_occupancy_adj_json,       sd_coords_occupancy_adj_json_6,       0], #sd_coords_occupancy_adj_json_15],
    [sd_coords_occupancy_adj_txt,        sd_coords_occupancy_adj_txt_6,        0], #sd_coords_occupancy_adj_txt_15],
    [sd_coords_occupancy_ascii_txt,      sd_coords_occupancy_ascii_txt_6,      0], #sd_coords_occupancy_ascii_txt_15],
    [sd_coords_occupancy_jpg,            sd_coords_occupancy_jpg_6,            0], #sd_coords_occupancy_jpg_15],
    [sd_coords_occupancy_json,           sd_coords_occupancy_json_6,           0], #sd_coords_occupancy_json_15],
    [sd_coords_occupancy_tokenized_txt,  sd_coords_occupancy_tokenized_txt_6,  0] #sd_coords_occupancy_tokenized_txt_15
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy ASCII",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized"
]

x_vals = np.arange(3)   # positions [0,1,2]
jitter_strength = 0.02

# Create figure
fig, (ax1, ax2) = plt.subplots(
    nrows=2, ncols=1, figsize=(12, 10), sharex=False
)

# Create top plot
for means, stds, label in zip(means_line, std_line, labels_line):
    jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
    ax1.errorbar(
        x_vals + jitter, means, yerr=stds,
        fmt='o-', capsize=5, label=label, alpha=0.9
    )

ax1.set_xticks(x_vals)
ax1.set_xticklabels(x_axis_line)
ax1.set_xlabel("Complexity")
ax1.set_ylabel("Accuracy [%]")
ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Pro, Coordinates Output")
ax1.legend(loc='best')
ax1.grid(axis='y', linestyle='--', alpha=0.3)

# Create bottom plot
for means, stds, label in zip(means_occ, std_occ, labels_occ):
    jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
    ax2.errorbar(
        x_vals + jitter, means, yerr=stds,
        fmt='o-', capsize=5, label=label, alpha=0.9
    )

ax2.set_xticks(x_vals)
ax2.set_xticklabels(x_axis_occ)
ax2.set_xlabel("Complexity")
ax2.set_ylabel("Accuracy [%]")
ax2.set_title("Mean Accuracy Per Complexity, Occupancy Maze, Gemini 2.5 Pro, Coordinates Output")
ax2.legend(loc='best')
ax2.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()


# # R -- Allo -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Accuracy R Allo 3x3
# line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_jpg = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 25.0, 100.0, 16.666666666666664, 100.0, 0.0])
# line_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 41.66666666666667, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_jpg = np.array([0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 25.0, 16.666666666666664, 0.0, 37.5])
# occupancy_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# # Averages and std deviation 3x3
# avg_coords_line_adj_json = np.mean(line_adj_json)
# avg_coords_line_adj_txt = np.mean(line_adj_txt)
# avg_coords_line_jpg = np.mean(line_jpg)
# avg_coords_line_json = np.mean(line_json)
# avg_coords_line_tokenized_txt = np.mean(line_tokenized_txt)
# avg_coords_occupancy_adj_json = np.mean(occupancy_adj_json)
# avg_coords_occupancy_adj_txt = np.mean(occupancy_adj_txt)
# avg_coords_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
# avg_coords_occupancy_jpg = np.mean(occupancy_jpg)
# avg_coords_occupancy_json = np.mean(occupancy_json)
# avg_coords_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_coords_line_adj_json = np.std(line_adj_json)
# sd_coords_line_adj_txt = np.std(line_adj_txt)
# sd_coords_line_jpg = np.std(line_jpg)
# sd_coords_line_json = np.std(line_json)
# sd_coords_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_coords_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_coords_occupancy_jpg = np.std(occupancy_jpg)
# sd_coords_occupancy_json = np.std(occupancy_json)
# sd_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# # Accuracy R Allo 6x6
# line_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_jpg_6 = np.array([6.25, 5.555555555555555, 0.0, 0.0, 28.57142857142857, 15.0, 4.166666666666666, 0.0, 18.75, 0.0])
# line_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_ascii_txt_6 = np.array([6.25, 0.0, 0.0, 25.0, 14.285714285714285, 55.00000000000001, 12.5, 35.0, 25.0, 10.0])
# occupancy_jpg_6 = np.array([18.75, 5.555555555555555, 4.411764705882353, 14.285714285714285, 7.142857142857142, 5.0, 4.166666666666666, 0.0, 9.375, 5.0])
# occupancy_json_6 = np.array([56.25, 100.0, 100.0, 7.142857142857142, 100.0, 100.0, 100.0, 100.0, 100.0, 37.5])
# occupancy_tokenized_txt_6 = np.array([100.0, 100.0, 51.470588235294116, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# # Averages and std deviation 6x6
# avg_coords_line_adj_json_6 = np.mean(line_adj_json_6)
# avg_coords_line_adj_txt_6 = np.mean(line_adj_txt_6)
# avg_coords_line_jpg_6 = np.mean(line_jpg_6)
# avg_coords_line_json_6 = np.mean(line_json_6)
# avg_coords_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
# avg_coords_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
# avg_coords_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
# avg_coords_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
# avg_coords_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
# avg_coords_occupancy_json_6 = np.mean(occupancy_json_6)
# avg_coords_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_coords_line_adj_json_6 = np.std(line_adj_json_6)
# sd_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_coords_line_jpg_6 = np.std(line_jpg_6)
# sd_coords_line_json_6 = np.std(line_json_6)
# sd_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_coords_occupancy_json_6 = np.std(occupancy_json_6)
# sd_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# # Accuracy R Allo 15x15

# # Averages and std deviation 15x15
# avg_coords_line_adj_json_15 = np.mean(line_adj_json_15)
# avg_coords_line_adj_txt_15 = np.mean(line_adj_txt_15)
# avg_coords_line_jpg_15 = np.mean(line_jpg_15)
# avg_coords_line_json_15 = np.mean(line_json_15)
# avg_coords_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
# avg_coords_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
# avg_coords_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
# avg_coords_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
# avg_coords_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
# avg_coords_occupancy_json_15 = np.mean(occupancy_json_15)
# avg_coords_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_coords_line_adj_json_15 = np.std(line_adj_json_15)
# sd_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_coords_line_jpg_15 = np.std(line_jpg_15)
# sd_coords_line_json_15 = np.std(line_json_15)
# sd_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_coords_occupancy_json_15 = np.std(occupancy_json_15)
# sd_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# # Top plot data
# means_line = [
#     [avg_coords_line_adj_json,       avg_coords_line_adj_json_6,       0],#line_adj_json_15],
#     [avg_coords_line_adj_txt,        avg_coords_line_adj_txt_6,        0],#line_adj_txt_15],
#     [avg_coords_line_jpg,            avg_coords_line_jpg_6,            0],#line_jpg_15],
#     [avg_coords_line_json,           avg_coords_line_json_6,           0],#line_json_15],
#     [avg_coords_line_tokenized_txt,  avg_coords_line_tokenized_txt_6,  0]#line_tokenized_txt_15]
# ]

# std_line = [
#     [sd_coords_line_adj_json,       sd_coords_line_adj_json_6,       0], #sd_coords_line_adj_json_15],
#     [sd_coords_line_adj_txt,        sd_coords_line_adj_txt_6,        0], #sd_coords_line_adj_txt_15],
#     [sd_coords_line_jpg,            sd_coords_line_jpg_6,            0], #sd_coords_line_jpg_15],
#     [sd_coords_line_json,           sd_coords_line_json_6,           0], #sd_coords_line_json_15],
#     [sd_coords_line_tokenized_txt,  sd_coords_line_tokenized_txt_6,  0]  #sd_coords_line_tokenized_txt_15
# ]

# labels_line = [
#     "Line Adjacency JSON",
#     "Line Adjacency txt",
#     "Line JPG",
#     "Line JSON",
#     "Line Tokenized"
# ]

# # Bottom plot data
# means_occ = [
#     [avg_coords_occupancy_adj_json,       avg_coords_occupancy_adj_json_6,       0],#occupancy_adj_json_15],
#     [avg_coords_occupancy_adj_txt,        avg_coords_occupancy_adj_txt_6,        0],#occupancy_adj_txt_15],
#     [avg_coords_occupancy_ascii_txt,      avg_coords_occupancy_ascii_txt_6,      0],#occupancy_ascii_txt_15],
#     [avg_coords_occupancy_jpg,            avg_coords_occupancy_jpg_6,            0],#occupancy_jpg_15],
#     [avg_coords_occupancy_json,           avg_coords_occupancy_json_6,           0],#occupancy_json_15],
#     [avg_coords_occupancy_tokenized_txt,  avg_coords_occupancy_tokenized_txt_6,  0]#occupancy_tokenized_txt_15]
# ]

# std_occ = [
#     [sd_coords_occupancy_adj_json,       sd_coords_occupancy_adj_json_6,       0], #sd_coords_occupancy_adj_json_15],
#     [sd_coords_occupancy_adj_txt,        sd_coords_occupancy_adj_txt_6,        0], #sd_coords_occupancy_adj_txt_15],
#     [sd_coords_occupancy_ascii_txt,      sd_coords_occupancy_ascii_txt_6,      0], #sd_coords_occupancy_ascii_txt_15],
#     [sd_coords_occupancy_jpg,            sd_coords_occupancy_jpg_6,            0], #sd_coords_occupancy_jpg_15],
#     [sd_coords_occupancy_json,           sd_coords_occupancy_json_6,           0], #sd_coords_occupancy_json_15],
#     [sd_coords_occupancy_tokenized_txt,  sd_coords_occupancy_tokenized_txt_6,  0] #sd_coords_occupancy_tokenized_txt_15
# ]

# labels_occ = [
#     "Occupancy Adjacency JSON",
#     "Occupancy Adjacency txt",
#     "Occupancy ASCII",
#     "Occupancy JPG",
#     "Occupancy JSON",
#     "Occupancy Tokenized"
# ]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02

# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line, std_line, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax1.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel("Complexity")
# ax1.set_ylabel("Accuracy [%]")
# ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Pro, Allocentric Output")
# ax1.legend(loc='best')
# ax1.grid(axis='y', linestyle='--', alpha=0.3)

# # Create bottom plot
# for means, stds, label in zip(means_occ, std_occ, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax2.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_axis_occ)
# ax2.set_xlabel("Complexity")
# ax2.set_ylabel("Accuracy [%]")
# ax2.set_title("Mean Accuracy Per Complexity, Occupancy Maze, Gemini 2.5 Pro, Allocentric Output")
# ax2.legend(loc='best')
# ax2.grid(axis='y', linestyle='--', alpha=0.3)

# plt.tight_layout()
# plt.show()

# # R -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Accuracy R Ego 3x3
# line_adj_json = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_adj_txt = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_jpg = np.array([25.0, 0.0, 50.0, 50.0, 33.33333333333333, 0.0, 0.0, 100.0, 16.666666666666664, 110.00000000000001])
# line_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 100.0, 100.0, 75.0])
# occupancy_jpg = np.array([12.5, 0.0, 0.0, 50.0, 33.33333333333333, 0.0, 12.5, 91.66666666666666, 8.333333333333332, 37.5])
# occupancy_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# # Averages and std deviation 3x3
# avg_coords_line_adj_json = np.mean(line_adj_json)
# avg_coords_line_adj_txt = np.mean(line_adj_txt)
# avg_coords_line_jpg = np.mean(line_jpg)
# avg_coords_line_json = np.mean(line_json)
# avg_coords_line_tokenized_txt = np.mean(line_tokenized_txt)
# avg_coords_occupancy_adj_json = np.mean(occupancy_adj_json)
# avg_coords_occupancy_adj_txt = np.mean(occupancy_adj_txt)
# avg_coords_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
# avg_coords_occupancy_jpg = np.mean(occupancy_jpg)
# avg_coords_occupancy_json = np.mean(occupancy_json)
# avg_coords_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_coords_line_adj_json = np.std(line_adj_json)
# sd_coords_line_adj_txt = np.std(line_adj_txt)
# sd_coords_line_jpg = np.std(line_jpg)
# sd_coords_line_json = np.std(line_json)
# sd_coords_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_coords_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_coords_occupancy_jpg = np.std(occupancy_jpg)
# sd_coords_occupancy_json = np.std(occupancy_json)
# sd_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# # Accuracy R Ego 6x6
# line_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_adj_txt_6 = np.array([100.0, 5.555555555555555, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# line_jpg_6 = np.array([12.5, 11.11111111111111, 0.0, 0.0, 21.428571428571427, 0.0, 4.166666666666666, 0.0, 31.25, 0.0])
# line_json_6 = np.array([100.0, 16.666666666666664, 100.0, 100.0, 100.0, 100.0, 83.33333333333334, 100.0, 6.25, 100.0])
# line_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_adj_json_6 = np.array([100.0, 100.0, 110.00000000000001, 100.0, 100.0, 100.0, 100.0, 0.0, 100.0, 100.0])
# occupancy_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# occupancy_ascii_txt_6 = np.array([12.5, 33.33333333333333, 0.0, 17.857142857142858, 28.57142857142857, 5.0, 10.416666666666668, 35.0, 0.0, 10.0])
# occupancy_jpg_6 = np.array([6.25, 16.666666666666664, 5.88235294117647, 0.0, 21.428571428571427, 2.5, 12.5, 50.0, 12.5, 0.0])
# occupancy_json_6 = np.array([100.0, 100.0, 8.823529411764707, 17.857142857142858, 100.0, 90.0, 100.0, 100.0, 56.25, 10.0])
# occupancy_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 29.166666666666668, 100.0, 100.0, 100.0])
# # Averages and std deviation 6x6
# avg_coords_line_adj_json_6 = np.mean(line_adj_json_6)
# avg_coords_line_adj_txt_6 = np.mean(line_adj_txt_6)
# avg_coords_line_jpg_6 = np.mean(line_jpg_6)
# avg_coords_line_json_6 = np.mean(line_json_6)
# avg_coords_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
# avg_coords_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
# avg_coords_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
# avg_coords_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
# avg_coords_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
# avg_coords_occupancy_json_6 = np.mean(occupancy_json_6)
# avg_coords_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_coords_line_adj_json_6 = np.std(line_adj_json_6)
# sd_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_coords_line_jpg_6 = np.std(line_jpg_6)
# sd_coords_line_json_6 = np.std(line_json_6)
# sd_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_coords_occupancy_json_6 = np.std(occupancy_json_6)
# sd_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# # Accuracy R Ego 15x15

# # Averages and std deviation 15x15
# avg_coords_line_adj_json_15 = np.mean(line_adj_json_15)
# avg_coords_line_adj_txt_15 = np.mean(line_adj_txt_15)
# avg_coords_line_jpg_15 = np.mean(line_jpg_15)
# avg_coords_line_json_15 = np.mean(line_json_15)
# avg_coords_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
# avg_coords_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
# avg_coords_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
# avg_coords_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
# avg_coords_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
# avg_coords_occupancy_json_15 = np.mean(occupancy_json_15)
# avg_coords_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_coords_line_adj_json_15 = np.std(line_adj_json_15)
# sd_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_coords_line_jpg_15 = np.std(line_jpg_15)
# sd_coords_line_json_15 = np.std(line_json_15)
# sd_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_coords_occupancy_json_15 = np.std(occupancy_json_15)
# sd_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# # Top plot data
# means_line = [
#     [avg_coords_line_adj_json,       avg_coords_line_adj_json_6,       0],#line_adj_json_15],
#     [avg_coords_line_adj_txt,        avg_coords_line_adj_txt_6,        0],#line_adj_txt_15],
#     [avg_coords_line_jpg,            avg_coords_line_jpg_6,            0],#line_jpg_15],
#     [avg_coords_line_json,           avg_coords_line_json_6,           0],#line_json_15],
#     [avg_coords_line_tokenized_txt,  avg_coords_line_tokenized_txt_6,  0]#line_tokenized_txt_15]
# ]

# std_line = [
#     [sd_coords_line_adj_json,       sd_coords_line_adj_json_6,       0], #sd_coords_line_adj_json_15],
#     [sd_coords_line_adj_txt,        sd_coords_line_adj_txt_6,        0], #sd_coords_line_adj_txt_15],
#     [sd_coords_line_jpg,            sd_coords_line_jpg_6,            0], #sd_coords_line_jpg_15],
#     [sd_coords_line_json,           sd_coords_line_json_6,           0], #sd_coords_line_json_15],
#     [sd_coords_line_tokenized_txt,  sd_coords_line_tokenized_txt_6,  0]  #sd_coords_line_tokenized_txt_15
# ]

# labels_line = [
#     "Line Adjacency JSON",
#     "Line Adjacency txt",
#     "Line JPG",
#     "Line JSON",
#     "Line Tokenized"
# ]

# # Bottom plot data
# means_occ = [
#     [avg_coords_occupancy_adj_json,       avg_coords_occupancy_adj_json_6,       0],#occupancy_adj_json_15],
#     [avg_coords_occupancy_adj_txt,        avg_coords_occupancy_adj_txt_6,        0],#occupancy_adj_txt_15],
#     [avg_coords_occupancy_ascii_txt,      avg_coords_occupancy_ascii_txt_6,      0],#occupancy_ascii_txt_15],
#     [avg_coords_occupancy_jpg,            avg_coords_occupancy_jpg_6,            0],#occupancy_jpg_15],
#     [avg_coords_occupancy_json,           avg_coords_occupancy_json_6,           0],#occupancy_json_15],
#     [avg_coords_occupancy_tokenized_txt,  avg_coords_occupancy_tokenized_txt_6,  0]#occupancy_tokenized_txt_15]
# ]

# std_occ = [
#     [sd_coords_occupancy_adj_json,       sd_coords_occupancy_adj_json_6,       0], #sd_coords_occupancy_adj_json_15],
#     [sd_coords_occupancy_adj_txt,        sd_coords_occupancy_adj_txt_6,        0], #sd_coords_occupancy_adj_txt_15],
#     [sd_coords_occupancy_ascii_txt,      sd_coords_occupancy_ascii_txt_6,      0], #sd_coords_occupancy_ascii_txt_15],
#     [sd_coords_occupancy_jpg,            sd_coords_occupancy_jpg_6,            0], #sd_coords_occupancy_jpg_15],
#     [sd_coords_occupancy_json,           sd_coords_occupancy_json_6,           0], #sd_coords_occupancy_json_15],
#     [sd_coords_occupancy_tokenized_txt,  sd_coords_occupancy_tokenized_txt_6,  0] #sd_coords_occupancy_tokenized_txt_15
# ]

# labels_occ = [
#     "Occupancy Adjacency JSON",
#     "Occupancy Adjacency txt",
#     "Occupancy ASCII",
#     "Occupancy JPG",
#     "Occupancy JSON",
#     "Occupancy Tokenized"
# ]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02

# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line, std_line, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax1.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel("Complexity")
# ax1.set_ylabel("Accuracy [%]")
# ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Pro, Egocentric Output")
# ax1.legend(loc='best')
# ax1.grid(axis='y', linestyle='--', alpha=0.3)

# # Create bottom plot
# for means, stds, label in zip(means_occ, std_occ, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line[1]))
#     ax2.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_axis_occ)
# ax2.set_xlabel("Complexity")
# ax2.set_ylabel("Accuracy [%]")
# ax2.set_title("Mean Accuracy Per Complexity, Occupancy Maze, Gemini 2.5 Pro, Egocentric Output")
# ax2.legend(loc='best')
# ax2.grid(axis='y', linestyle='--', alpha=0.3)

# plt.tight_layout()
# plt.show()






#------------- Plotting raw scores for all types and sizes until run 10 ----------------------


# # NR -- Coords -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Raw Scores NR Coords 3x3
# line_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
# line_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 3.0, 7.0, 5.0])
# line_jpg_raw_score = np.array([2.0, 1.0, 2.0, 3.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
# line_json_raw_score = np.array([5.0, 1.0, 3.0, 1.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
# line_tokenized_txt_raw_score = np.array([1.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0])
# occupancy_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
# occupancy_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
# occupancy_ascii_txt_raw_score = np.array([0.0, 9.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.0])  
# occupancy_jpg_raw_score = np.array([0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 1.0, 9.0, 9.0, 13.0, 13.0, 9.0])
# occupancy_tokenized_txt_raw_score = np.array([1.0, 9.0, 9.0, 9.0, 1.0, 1.0, 9.0, 13.0, 1.0, 9])
# # 3x3 averages
# avg_coords_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
# avg_coords_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
# avg_coords_line_jpg_raw_score = np.mean(line_jpg_raw_score)
# avg_coords_line_json_raw_score = np.mean(line_json_raw_score)
# avg_coords_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
# avg_coords_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
# avg_coords_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
# avg_coords_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
# avg_coords_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
# avg_coords_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
# avg_coords_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# # Raw Scores NR Coords 6x6
# line_adj_json_raw_score_6 = np.array([9.0, 19.0, 14.0, 13.0, 15.0, 16.0, 24.0, 9.0, 10.0, 16.0])
# line_adj_txt_raw_score_6 = np.array([9.0, 8.0, 5.0, 7.0, 15.0, 21.0, 24.0, 11.0, 10.0, 10.0])
# line_jpg_raw_score_6 = np.array([2.0, 2.0, 1.0, 1.0, 4.0, 1.0, 2.0, 1.0, 2.0, 1.0])
# line_json_raw_score_6 = np.array([2.0, 2.0, 2.0, 4.0, 4.0, 3.0, 4.0, 4.0, 2.0, 1.0])
# line_tokenized_txt_raw_score_6 = np.array([6.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 1.0, 0.0, 1.0])
# occupancy_adj_json_raw_score_6 = np.array([33.0, 29.0, 69.0, 49.0, 29.0, 41.0, 49.0, 21.0, 25.0, 19.0])
# occupancy_adj_txt_raw_score_6 = np.array([17.0, 37.0, 17.0, 57.0, 29.0, 17.0, 21.0, 21.0, 19.0, 19.0])
# occupancy_ascii_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score_6 = np.array([1.0, 1.0, 7.0, 17.0, 1.0, 9.0, 1.0, 17.0, 1.0, 5.0])
# occupancy_tokenized_txt_raw_score_6 = np.array([1.0, 1.0, 7.0, 13.0, 1.0, 9.0, 1.0, 11.0, 5.0, 5])
# # 6x6 averages
# avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores NR Coords 15x15
# line_adj_json_raw_score_15 = np.array([3])
# line_adj_txt_raw_score_15 = np.array([11])
# line_jpg_raw_score_15 = np.array([4])
# line_json_raw_score_15 = np.array([2])
# line_tokenized_txt_raw_score_15 = np.array([1])
# occupancy_adj_json_raw_score_15 = np.array([67])
# occupancy_adj_txt_raw_score_15 = np.array([15])
# occupancy_ascii_txt_raw_score_15 = np.array([0])
# occupancy_jpg_raw_score_15 = np.array([0])
# occupancy_json_raw_score_15 = np.array([1])
# occupancy_tokenized_txt_raw_score_15 = np.array([1])

# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , line_jpg_raw_score_15.item()]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  line_json_raw_score_15.item()]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# # x_pos = np.array([0, 1, 2])   # three x-axis positions
# # jitter_strength = 0.01
# # # Build figure
# # fig, (ax1, ax2) = plt.subplots(
# #     nrows=2,
# #     ncols=1,
# #     figsize=(10, 8),
# #     sharex=False  # ensures the two subplots align vertically
# # )

# # # Top Plot
# # for data, label in zip(dataset_line, labels_line):
# #     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax1.set_xticks(x_pos)
# # ax1.set_xticklabels(x_axis_line)

# # ax1.set_xlabel("Maze Complexity")
# # ax1.set_ylabel("Number of Correct Steps")
# # ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Coordinates Output")

# # # Legend centered above subplot
# # ax1.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # # Bottom Plot
# # for data, label in zip(dataset_occupancy, labels_occupancy):
# #     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax2.set_xticks(x_pos)
# # ax2.set_xticklabels(x_axis_occ)

# # ax2.set_xlabel("Maze Complexity")
# # ax2.set_ylabel("Number of Correct Steps")
# # ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Coordinates Output")

# # # Legend centered above subplot
# # ax2.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax2.grid(axis='y', linestyle='--', alpha=0.8)

# # plt.tight_layout()
# # plt.show()




# # NR -- Allo -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Raw Scores NR Allo 3x3
# line_adj_json_raw_score = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 4.0, 4.0, 2.0, 2.0, 4.0])
# line_adj_txt_raw_score = np.array([0.0, 4.0, 0.0, 4.0, 0.0, 0.0, 4.0, 2.0, 2.0, 4.0])
# line_jpg_raw_score = np.array([2.0, 0.0, 2.0, 4.0, 2.0, 2.0, 4.0, 0.0, 0.0, 0.0])
# line_json_raw_score = np.array([4.0, 0.0, 4.0, 0.0, 2.0, 4.0, 0.0, 0.0, 2.0, 0.0])
# line_tokenized_txt_raw_score = np.array([0.0, 4.0, 0.0, 1.0, 0.0, 0.0, 1.0, 2.0, 0.0, 1.0])
# occupancy_adj_json_raw_score = np.array([4.0, 2.0, 6.0, 8.0, 0.0, 4.0, 8.0, 4.0, 0.0, 8.0])
# occupancy_adj_txt_raw_score = np.array([5.0, 2.0, 0.0, 3.0, 4.0, 2.0, 3.0, 4.0, 0.0, 8.0])
# occupancy_ascii_txt_raw_score = np.array([0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 5.0, 4.0, 4.0, 0.0])
# occupancy_jpg_raw_score = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
# occupancy_json_raw_score = np.array([5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 7.0])
# occupancy_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 4.0, 1.0, 1.0, 0.0, 1.0, 0.0, 8])
# # 3x3 averages
# avg_allo_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
# avg_allo_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
# avg_allo_line_jpg_raw_score = np.mean(line_jpg_raw_score)
# avg_allo_line_json_raw_score = np.mean(line_json_raw_score)
# avg_allo_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
# avg_allo_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
# avg_allo_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
# avg_allo_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
# avg_allo_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
# avg_allo_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
# avg_allo_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# #Raw Scores NR Allo 6x6
# line_adj_json_raw_score_6 = np.array([3.0, 1.0, 3.0, 5.0, 0.0, 4.0, 2.0, 10.0, 2.0, 3.0])
# line_adj_txt_raw_score_6 = np.array([4.0, 0.0, 4.0, 5.0, 3.0, 1.0, 0.0, 6.0, 0.0, 1.0])
# line_jpg_raw_score_6 = np.array([1.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0])
# line_json_raw_score_6 = np.array([2.0, 1.0, 0.0, 5.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0])
# line_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 1.0, 3.0, 1.0, 0.0, 1.0, 0.0, 2.0])
# occupancy_adj_json_raw_score_6 = np.array([6.0, 2.0, 5.0, 10.0, 4.0, 2.0, 4.0, 10.0, 2.0, 2.0])
# occupancy_adj_txt_raw_score_6 = np.array([6.0, 2.0, 6.0, 10.0, 4.0, 7.0, 4.0, 18.0, 6.0, 0.0])
# occupancy_ascii_txt_raw_score_6 = np.array([2.0, 4.0, 0.0, 12.0, 0.0, 0.0, 1.0, 11.0, 0.0, 3.0])
# occupancy_jpg_raw_score_6 = np.array([0.0, 0.0, 1.0, 6.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.0])
# occupancy_json_raw_score_6 = np.array([0.0, 0.0, 4.0, 8.0, 0.0, 4.0, 0.0, 16.0, 0.0, 4.0])
# occupancy_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 8.0, 0.0, 1])
# #6x6 averages
# avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores NR Allo 15x15
# line_adj_json_raw_score_15 = np.array([0])
# line_adj_txt_raw_score_15 = np.array([0])
# line_jpg_raw_score_15 = np.array([np.nan])
# line_json_raw_score_15 = np.array([2])
# line_tokenized_txt_raw_score_15 = np.array([0])
# occupancy_adj_json_raw_score_15 = np.array([2])
# occupancy_adj_txt_raw_score_15 = np.array([0])
# occupancy_ascii_txt_raw_score_15 = np.array([0])
# occupancy_jpg_raw_score_15 = np.array([np.nan])
# occupancy_json_raw_score_15 = np.array([0])
# occupancy_tokenized_txt_raw_score_15 = np.array([0])

# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , line_jpg_raw_score_15.item()]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  line_json_raw_score_15.item()]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# # x_pos = np.array([0, 1, 2])   # three x-axis positions
# # jitter_strength = 0.02
# # # Build figure
# # fig, (ax1, ax2) = plt.subplots(
# #     nrows=2,
# #     ncols=1,
# #     figsize=(10, 8),
# #     sharex=False  # ensures the two subplots align vertically
# # )

# # # Top Plot
# # for data, label in zip(dataset_line, labels_line):
# #     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax1.set_xticks(x_pos)
# # ax1.set_xticklabels(x_axis_line)

# # ax1.set_xlabel("Maze Complexity")
# # ax1.set_ylabel("Number of Correct Steps")
# # ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Allocentric Output")

# # # Legend centered above subplot
# # ax1.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # # Bottom Plot
# # for data, label in zip(dataset_occupancy, labels_occupancy):
# #     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax2.set_xticks(x_pos)
# # ax2.set_xticklabels(x_axis_occ)

# # ax2.set_xlabel("Maze Complexity")
# # ax2.set_ylabel("Number of Correct Steps")
# # ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Allocentric Output")

# # # Legend centered above subplot
# # ax2.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax2.grid(axis='y', linestyle='--', alpha=0.8)

# # plt.tight_layout()
# # plt.show()


# # NR -- Ego -- raw scores ----------- 3x3 & 15x15 -----------------------------------
# # Raw Scores NR Ego 3x3
# line_adj_json_raw_score = np.array([1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_jpg_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_json_raw_score = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_adj_json_raw_score = np.array([0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# occupancy_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_ascii_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg_raw_score = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0])
# # 3x3 averages
# avg_ego_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
# avg_ego_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
# avg_ego_line_jpg_raw_score = np.mean(line_jpg_raw_score)
# avg_ego_line_json_raw_score = np.mean(line_json_raw_score)
# avg_ego_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
# avg_ego_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
# avg_ego_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
# avg_ego_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
# avg_ego_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
# avg_ego_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
# avg_ego_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# #Raw Scores NR Ego 6x6
# line_adj_json_raw_score_6 = np.array([3.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_adj_txt_raw_score_6 = np.array([2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_json_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
# line_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# occupancy_adj_json_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_adj_txt_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_ascii_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg_raw_score_6 = np.array([1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score_6 = np.array([0.0, 2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0])
# #6x6 averages
# avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores NR Ego 15x15
# line_adj_json_raw_score_15 = np.array([0])
# line_adj_txt_raw_score_15 = np.array([2])
# line_jpg_raw_score_15 = np.array([2])
# line_json_raw_score_15 = np.array([2])
# line_tokenized_txt_raw_score_15 = np.array([1])
# occupancy_adj_json_raw_score_15 = np.array([0])
# occupancy_adj_txt_raw_score_15 = np.array([4])
# occupancy_ascii_txt_raw_score_15 = np.array([0])
# occupancy_jpg_raw_score_15 = np.array([2])
# occupancy_json_raw_score_15 = np.array([0])
# occupancy_tokenized_txt_raw_score_15 = np.array([1])


# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , line_jpg_raw_score_15.item()]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  line_json_raw_score_15.item()]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1, 2])   # three x-axis positions
# # jitter_strength = 0.01
# # # Build figure
# # fig, (ax1, ax2) = plt.subplots(
# #     nrows=2,
# #     ncols=1,
# #     figsize=(10, 8),
# #     sharex=False  # ensures the two subplots align vertically
# # )

# # # Top Plot
# # for data, label in zip(dataset_line, labels_line):
# #     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax1.set_xticks(x_pos)
# # ax1.set_xticklabels(x_axis_line)

# # ax1.set_xlabel("Maze Complexity")
# # ax1.set_ylabel("Number of Correct Steps")
# # ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Egocentric Output")

# # # Legend centered above subplot
# # ax1.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # # Bottom Plot
# # for data, label in zip(dataset_occupancy, labels_occupancy):
# #     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax2.set_xticks(x_pos)
# # ax2.set_xticklabels(x_axis_occ)

# # ax2.set_xlabel("Maze Complexity")
# # ax2.set_ylabel("Number of Correct Steps")
# # ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Egocentric Output")

# # # Legend centered above subplot
# # ax2.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax2.grid(axis='y', linestyle='--', alpha=0.8)

# # plt.tight_layout()
# # plt.show()


# # R -- Coords -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Raw Scores R Coords 3x3
# line_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
# line_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
# line_jpg_raw_score = np.array([2.0, 5.0, 5.0, 5.0, 2.0, 2.0, 2.0, 7.0, 7.0, 5.0])
# line_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
# line_tokenized_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
# occupancy_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
# occupancy_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
# occupancy_ascii_txt_raw_score = np.array([2.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 6.0, 7.0])
# occupancy_jpg_raw_score = np.array([1.0, 2.0, 5.0, 0.0, 1.0, 1.0, 3.0, 0.0, 1.0, 9.0])
# occupancy_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
# occupancy_tokenized_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9])
# # 3x3 averages
# avg_coords_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
# avg_coords_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
# avg_coords_line_jpg_raw_score = np.mean(line_jpg_raw_score)
# avg_coords_line_json_raw_score = np.mean(line_json_raw_score)
# avg_coords_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
# avg_coords_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
# avg_coords_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
# avg_coords_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
# avg_coords_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
# avg_coords_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
# avg_coords_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# # Raw Scores R Coords 6x6
# line_adj_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
# line_adj_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
# line_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
# line_tokenized_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
# occupancy_adj_json_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0])
# occupancy_adj_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0])
# occupancy_ascii_txt_raw_score_6 = np.array([8.0, 12.0, 8.0, 1.0, 9.0, 1.0, 1.0, 0.0, 9.0, 1.0])
# occupancy_jpg_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score_6 = np.array([9.0, 18.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 20.0, 41.0])
# occupancy_tokenized_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41])
# # 6x6 averages
# avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores R Coords 15x15
# line_adj_json_raw_score_15 = np.array([131.0])
# line_adj_txt_raw_score_15 = np.array([25.0])
# line_jpg_raw_score_15 = np.array([0.0])
# line_json_raw_score_15 = np.array([31.0])
# line_tokenized_txt_raw_score_15 = np.array([126.0])
# occupancy_adj_json_raw_score_15 = np.array([261.0])
# occupancy_adj_txt_raw_score_15 = np.array([89.0])
# occupancy_ascii_txt_raw_score_15 = np.array([0.0])
# occupancy_jpg_raw_score_15 = np.array([5.0])
# occupancy_json_raw_score_15 = np.array([31.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([103])

# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , line_jpg_raw_score_15.item()]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  line_json_raw_score_15.item()]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1, 2])   # three x-axis positions
# # jitter_strength = 0.01
# # # Build figure
# # fig, (ax1, ax2) = plt.subplots(
# #     nrows=2,
# #     ncols=1,
# #     figsize=(10, 8),
# #     sharex=False  # ensures the two subplots align vertically
# # )

# # # Top Plot
# # for data, label in zip(dataset_line, labels_line):
# #     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax1.set_xticks(x_pos)
# # ax1.set_xticklabels(x_axis_line)

# # ax1.set_xlabel("Maze Complexity")
# # ax1.set_ylabel("Number of Correct Steps")
# # ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Coordinates Output")

# # # Legend centered above subplot
# # ax1.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # # Bottom Plot
# # for data, label in zip(dataset_occupancy, labels_occupancy):
# #     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax2.set_xticks(x_pos)
# # ax2.set_xticklabels(x_axis_occ)

# # ax2.set_xlabel("Maze Complexity")
# # ax2.set_ylabel("Number of Correct Steps")
# # ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Coordinates Output")

# # # Legend centered above subplot
# # ax2.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax2.grid(axis='y', linestyle='--', alpha=0.8)

# # plt.tight_layout()
# # plt.show()

# # R -- Allo -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Raw Scores R Allo 3x3
# line_adj_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# line_adj_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# line_jpg_raw_score = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 1.0, 4.0, 1.0, 6.0, 0.0])
# line_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# line_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# occupancy_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
# occupancy_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
# occupancy_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 5.0, 8.0, 8.0, 12.0, 12.0, 8.0])
# occupancy_jpg_raw_score = np.array([0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 2.0, 2.0, 0.0, 3.0])
# occupancy_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
# occupancy_tokenized_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8])
# # 3x3 averages
# avg_allo_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
# avg_allo_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
# avg_allo_line_jpg_raw_score = np.mean(line_jpg_raw_score)
# avg_allo_line_json_raw_score = np.mean(line_json_raw_score)
# avg_allo_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
# avg_allo_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
# avg_allo_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
# avg_allo_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
# avg_allo_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
# avg_allo_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
# avg_allo_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# # Raw Scores R Allo 6x6
# line_adj_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
# line_adj_txt_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
# line_jpg_raw_score_6 = np.array([1.0, 1.0, 0.0, 0.0, 4.0, 3.0, 1.0, 0.0, 3.0, 0.0])
# line_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
# line_tokenized_txt_raw_score_6 = np.array([16.0, 18.0, 13.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
# occupancy_adj_json_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
# occupancy_adj_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
# occupancy_ascii_txt_raw_score_6 = np.array([2.0, 0.0, 0.0, 14.0, 4.0, 22.0, 6.0, 7.0, 8.0, 4.0])
# occupancy_jpg_raw_score_6 = np.array([6.0, 2.0, 3.0, 8.0, 2.0, 2.0, 2.0, 0.0, 3.0, 2.0])
# occupancy_json_raw_score_6 = np.array([18.0, 36.0, 68.0, 4.0, 28.0, 40.0, 48.0, 20.0, 32.0, 15.0])
# occupancy_tokenized_txt_raw_score_6 = np.array([32.0, 36.0, 35.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40])
# # 6x6 averages
# avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores R Allo 15x15
# line_adj_json_raw_score_15 = np.array([61])
# line_adj_txt_raw_score_15 = np.array([10])
# line_jpg_raw_score_15 = np.array([1])
# line_json_raw_score_15 = np.array([36])
# line_tokenized_txt_raw_score_15 = np.array([43])
# occupancy_adj_json_raw_score_15 = np.array([120])
# occupancy_adj_txt_raw_score_15 = np.array([72])
# occupancy_ascii_txt_raw_score_15 = np.array([4])
# occupancy_jpg_raw_score_15 = np.array([3])
# occupancy_json_raw_score_15 = np.array([1])
# occupancy_tokenized_txt_raw_score_15 = np.array([66])

# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , line_jpg_raw_score_15.item()]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  line_json_raw_score_15.item()]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# # x_pos = np.array([0, 1, 2])   # three x-axis positions
# # jitter_strength = 0.01
# # # Build figure
# # fig, (ax1, ax2) = plt.subplots(
# #     nrows=2,
# #     ncols=1,
# #     figsize=(10, 8),
# #     sharex=False  # ensures the two subplots align vertically
# # )

# # # Top Plot
# # for data, label in zip(dataset_line, labels_line):
# #     ax1.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax1.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax1.set_xticks(x_pos)
# # ax1.set_xticklabels(x_axis_line)

# # ax1.set_xlabel("Maze Complexity")
# # ax1.set_ylabel("Number of Correct Steps")
# # ax1.set_title("Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Allocentric Output")

# # # Legend centered above subplot
# # ax1.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # # Bottom Plot
# # for data, label in zip(dataset_occupancy, labels_occupancy):
# #     ax2.plot(x_pos, data, linewidth=1.5, marker='', label=label)
# #     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(data))
# #     ax2.scatter(x_pos + jitter, data, alpha=0.75, s=70, label=label)

# # ax2.set_xticks(x_pos)
# # ax2.set_xticklabels(x_axis_occ)

# # ax2.set_xlabel("Maze Complexity")
# # ax2.set_ylabel("Number of Correct Steps")
# # ax2.set_title("Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Allocentric Output")

# # # Legend centered above subplot
# # ax2.legend(
# #     loc='best',
# #     # bbox_to_anchor=(0.5, 1.18),
# #     ncol=3,
# #     fontsize=9
# # )

# # ax2.grid(axis='y', linestyle='--', alpha=0.8)

# # plt.tight_layout()
# # plt.show()





# # R -- Ego -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# # Raw Scores R Ego 3x3
# line_adj_json_raw_score = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# line_adj_txt_raw_score = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# line_jpg_raw_score = np.array([1.0, 0.0, 2.0, 2.0, 2.0, 0.0, 0.0, 6.0, 1.0, 4.0])
# line_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# line_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
# occupancy_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
# occupancy_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
# occupancy_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 4.0, 12.0, 12.0, 6.0])
# occupancy_jpg_raw_score = np.array([1.0, 0.0, 0.0, 4.0, 4.0, 0.0, 1.0, 11.0, 1.0, 3.0])
# occupancy_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
# occupancy_tokenized_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8])
# # 3x3 averages
# avg_ego_line_adj_json_raw_score = np.mean(line_adj_json_raw_score)
# avg_ego_line_adj_txt_raw_score = np.mean(line_adj_txt_raw_score)
# avg_ego_line_jpg_raw_score = np.mean(line_jpg_raw_score)
# avg_ego_line_json_raw_score = np.mean(line_json_raw_score)
# avg_ego_line_tokenized_txt_raw_score = np.mean(line_tokenized_txt_raw_score)
# avg_ego_occupancy_adj_json_raw_score = np.mean(occupancy_adj_json_raw_score)
# avg_ego_occupancy_adj_txt_raw_score = np.mean(occupancy_adj_txt_raw_score)
# avg_ego_occupancy_ascii_txt_raw_score = np.mean(occupancy_ascii_txt_raw_score)  
# avg_ego_occupancy_jpg_raw_score = np.mean(occupancy_jpg_raw_score)
# avg_ego_occupancy_json_raw_score = np.mean(occupancy_json_raw_score)
# avg_ego_occupancy_tokenized_txt_raw_score = np.mean(occupancy_tokenized_txt_raw_score)
# #Raw Scores R Ego 6x6
# line_adj_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
# line_adj_txt_raw_score_6 = np.array([16.0, 1.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
# line_jpg_raw_score_6 = np.array([2.0, 2.0, 0.0, 0.0, 3.0, 0.0, 1.0, 0.0, 5.0, 0.0])
# line_json_raw_score_6 = np.array([16.0, 3.0, 34.0, 28.0, 14.0, 20.0, 20.0, 10.0, 1.0, 20.0])
# line_tokenized_txt_raw_score_6 = np.array([16.0, 18.0, 13.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
# occupancy_adj_json_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 0.0, 32.0, 40.0])
# occupancy_adj_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
# occupancy_ascii_txt_raw_score_6 = np.array([4.0, 12.0, 0.0, 10.0, 8.0, 2.0, 5.0, 7.0, 0.0, 4.0])
# occupancy_jpg_raw_score_6 = np.array([2.0, 6.0, 4.0, 0.0, 6.0, 1.0, 6.0, 10.0, 4.0, 0.0])
# occupancy_json_raw_score_6 = np.array([32.0, 36.0, 6.0, 10.0, 28.0, 36.0, 48.0, 20.0, 18.0, 4.0])
# occupancy_tokenized_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 14.0, 20.0, 32.0, 40])
# #6x6 averages
# avg_coords_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_coords_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_coords_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_coords_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_coords_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_coords_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_coords_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_coords_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_coords_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_coords_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_coords_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores R Ego 15x15
# line_adj_json_raw_score_15 = np.array([4.0])
# line_adj_txt_raw_score_15 = np.array([3.0])
# line_jpg_raw_score_15 = np.array([1.0])
# line_json_raw_score_15 = np.array([4.0])
# line_tokenized_txt_raw_score_15 = np.array([2.0])
# occupancy_jpg_raw_score_15 = np.array([4.0])
# occupancy_json_raw_score_15 = np.array([10.0])
# occupancy_adj_json_raw_score_15 = np.array([89.0])
# occupancy_adj_txt_raw_score_15 = np.array([4.0])
# occupancy_ascii_txt_raw_score_15 = np.array([2.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([71])


# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , line_jpg_raw_score_15.item()]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  line_json_raw_score_15.item()]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , line_adj_json_raw_score_15.item()]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  line_adj_txt_raw_score_15.item()]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , line_tokenized_txt_raw_score_15.item()]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  occupancy_jpg_raw_score_15.item()]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , occupancy_json_raw_score_15.item()]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , occupancy_adj_json_raw_score_15.item()]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , occupancy_adj_txt_raw_score_15.item()]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , occupancy_tokenized_txt_raw_score_15.item()]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , occupancy_ascii_txt_raw_score_15.item()]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1, 2])   # three x-axis positions
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