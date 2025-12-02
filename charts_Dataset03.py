import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi
# import matplotlib.pyplot.axes as axs


x_axis_line = ['3x3', '6x6', '15x15']
x_axis_occ = ['7x7', '13x13', '31x31']

def confidence_interval(vector):
    z = 1.96
    n = len(vector)
    sd = np.nanstd(vector, ddof=1)  # Sample standard deviation
    mean = np.nanmean(vector)
    error = z * (sd / np.sqrt(n))
    # lower_bound = mean-error
    # upper_bound = mean+error
    return error #lower_bound, upper_bound 

# --- Plotting mean accuracy with stdev error bars for all types and sizes until run 10 ----------

# NR -- Coords -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Coords 3x3
line_NR_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_NR_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 42.857142857142854, 100.0, 100.0])
line_NR_coords_jpg = np.array([40.0, 20.0, 40.0, 60.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_json = np.array([100.0, 20.0, 60.0, 20.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_tokenized_txt = np.array([20.0, 0.0, 0.0, 60.0, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 20.0])
occupancy_NR_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 110.00000000000001])
occupancy_NR_coords_jpg = np.array([0.0, 0.0, 55.55555555555556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json = np.array([100.0, 110.00000000000001, 100.0, 110.00000000000001, 7.6923076923076925, 100.0, 110.00000000000001, 100.0, 100.0, 110.00000000000001])
occupancy_NR_coords_tokenized_txt = np.array([11.11111111111111, 110.00000000000001, 100.0, 100.0, 7.6923076923076925, 11.11111111111111, 100.0, 100.0, 7.6923076923076925, 110.00000000000001])
# Averages and std deviation 3x3
avg_line_NR_coords_adj_json = np.mean(line_NR_coords_adj_json)
avg_line_NR_coords_adj_txt = np.mean(line_NR_coords_adj_txt)
avg_line_NR_coords_jpg = np.mean(line_NR_coords_jpg)
avg_line_NR_coords_json = np.mean(line_NR_coords_json)
avg_line_NR_coords_tokenized_txt = np.mean(line_NR_coords_tokenized_txt)
avg_occupancy_NR_coords_adj_json = np.mean(occupancy_NR_coords_adj_json)
avg_occupancy_NR_coords_adj_txt = np.mean(occupancy_NR_coords_adj_txt)
avg_occupancy_NR_coords_ascii_txt = np.mean(occupancy_NR_coords_ascii_txt)  
avg_occupancy_NR_coords_jpg = np.mean(occupancy_NR_coords_jpg)
avg_occupancy_NR_coords_json = np.mean(occupancy_NR_coords_json)
avg_occupancy_NR_coords_tokenized_txt = np.mean(occupancy_NR_coords_tokenized_txt)
sd_line_NR_coords_adj_json = np.std(line_NR_coords_adj_json)
sd_line_NR_coords_adj_txt = np.std(line_NR_coords_adj_txt)
sd_line_NR_coords_jpg = np.std(line_NR_coords_jpg)
sd_line_NR_coords_json = np.std(line_NR_coords_json)
sd_line_NR_coords_tokenized_txt = np.std(line_NR_coords_tokenized_txt)
sd_occupancy_NR_coords_adj_json = np.std(occupancy_NR_coords_adj_json)
sd_occupancy_NR_coords_adj_txt = np.std(occupancy_NR_coords_adj_txt)
sd_occupancy_NR_coords_ascii_txt = np.std(occupancy_NR_coords_ascii_txt)  
sd_occupancy_NR_coords_jpg = np.std(occupancy_NR_coords_jpg)
sd_occupancy_NR_coords_json = np.std(occupancy_NR_coords_json)
sd_occupancy_NR_coords_tokenized_txt = np.std(occupancy_NR_coords_tokenized_txt)
# Accuracy NR Coords 6x6
line_NR_coords_adj_json_6 = np.array([52.94117647058824, 100.0, 40.0, 44.827586206896555, 100.0, 76.19047619047619, 96.0, 81.81818181818183, 58.82352941176471, 76.19047619047619])
line_NR_coords_adj_txt_6 = np.array([52.94117647058824, 42.10526315789473, 14.285714285714285, 24.137931034482758, 100.0, 100.0, 96.0, 100.0, 58.82352941176471, 47.61904761904761])
line_NR_coords_jpg_6 = np.array([11.76470588235294, 10.526315789473683, 2.857142857142857, 3.4482758620689653, 26.666666666666668, 4.761904761904762, 8.0, 9.090909090909092, 11.76470588235294, 4.761904761904762])
line_NR_coords_json_6 = np.array([11.76470588235294, 10.526315789473683, 5.714285714285714, 13.793103448275861, 26.666666666666668, 14.285714285714285, 16.0, 36.36363636363637, 11.76470588235294, 4.761904761904762])
line_NR_coords_tokenized_txt_6 = np.array([35.294117647058826, 5.263157894736842, 2.857142857142857, 3.4482758620689653, 20.0, 4.761904761904762, 4.0, 9.090909090909092, 0.0, 4.761904761904762])
occupancy_NR_coords_adj_json_6 = np.array([100.0, 78.37837837837837, 100.0, 85.96491228070175, 100.0, 100.0, 100.0, 100.0, 75.75757575757575, 46.34146341463415])
occupancy_NR_coords_adj_txt_6 = np.array([51.515151515151516, 100.0, 24.637681159420293, 100.0, 100.0, 41.46341463414634, 42.857142857142854, 100.0, 57.57575757575758, 46.34146341463415])
occupancy_NR_coords_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 29.82456140350877, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 80.95238095238095, 3.0303030303030303, 12.195121951219512])
occupancy_NR_coords_tokenized_txt_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 22.807017543859647, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 52.38095238095239, 15.151515151515152, 12.195121951219512])
# Averages and std deviation 6x6
avg_line_NR_coords_adj_json_6 = np.mean(line_NR_coords_adj_json_6)
avg_line_NR_coords_adj_txt_6 = np.mean(line_NR_coords_adj_txt_6)
avg_line_NR_coords_jpg_6 = np.mean(line_NR_coords_jpg_6)
avg_line_NR_coords_json_6 = np.mean(line_NR_coords_json_6)
avg_line_NR_coords_tokenized_txt_6 = np.mean(line_NR_coords_tokenized_txt_6)
avg_occupancy_NR_coords_adj_json_6 = np.mean(occupancy_NR_coords_adj_json_6)
avg_occupancy_NR_coords_adj_txt_6 = np.mean(occupancy_NR_coords_adj_txt_6)
avg_occupancy_NR_coords_ascii_txt_6 = np.mean(occupancy_NR_coords_ascii_txt_6)  
avg_occupancy_NR_coords_jpg_6 = np.mean(occupancy_NR_coords_jpg_6)
avg_occupancy_NR_coords_json_6 = np.mean(occupancy_NR_coords_json_6)
avg_occupancy_NR_coords_tokenized_txt_6 = np.mean(occupancy_NR_coords_tokenized_txt_6)
sd_line_NR_coords_adj_json_6 = np.std(line_NR_coords_adj_json_6)
sd_line_NR_coords_adj_txt_6 = np.std(line_NR_coords_adj_txt_6)
sd_line_NR_coords_jpg_6 = np.std(line_NR_coords_jpg_6)
sd_line_NR_coords_json_6 = np.std(line_NR_coords_json_6)
sd_line_NR_coords_tokenized_txt_6 = np.std(line_NR_coords_tokenized_txt_6)
sd_occupancy_NR_coords_adj_json_6 = np.std(occupancy_NR_coords_adj_json_6)
sd_occupancy_NR_coords_adj_txt_6 = np.std(occupancy_NR_coords_adj_txt_6)
sd_occupancy_NR_coords_ascii_txt_6 = np.std(occupancy_NR_coords_ascii_txt_6)  
sd_occupancy_NR_coords_jpg_6 = np.std(occupancy_NR_coords_jpg_6)
sd_occupancy_NR_coords_json_6 = np.std(occupancy_NR_coords_json_6)
sd_occupancy_NR_coords_tokenized_txt_6 = np.std(occupancy_NR_coords_tokenized_txt_6)
# Accuracy NR Coords 15x15
line_NR_coords_adj_json_15 = np.array([2.2900763358778624, 28.985507246376812, 31.654676258992804, 40.35087719298245, 3.937007874015748, 18.81188118811881, 7.462686567164178, 36.708860759493675, 11.278195488721805, 27.659574468085108])
line_NR_coords_adj_txt_15 = np.array([8.396946564885496, 27.536231884057973, 10.79136690647482, 15.789473684210526, 4.724409448818897, 23.762376237623762, 4.477611940298507, 3.79746835443038, 5.263157894736842, 34.04255319148936])
line_NR_coords_jpg_15 = np.array([3.0534351145038165, 1.4492753623188406, 2.158273381294964, 1.7543859649122806, 0.7874015748031495, 0.9900990099009901, 1.4925373134328357, 1.2658227848101267, 2.2556390977443606, 2.127659574468085])
line_NR_coords_json_15 = np.array([1.5267175572519083, 5.797101449275362, 1.4388489208633095, 1.7543859649122806, 3.937007874015748, 0.9900990099009901, 1.4925373134328357, 2.5316455696202533, 2.2556390977443606, 2.127659574468085])
line_NR_coords_tokenized_txt_15 = np.array([0.7633587786259541, 0.0, 0.0, 7.017543859649122, 1.574803149606299, 0.9900990099009901, 0.0, 0.0, 0.0, 2.127659574468085])
occupancy_NR_coords_adj_json_15 = np.array([25.67049808429119, 8.02919708029197, 3.2490974729241873, 54.86725663716814, 14.624505928853754, 42.28855721393035, 63.90977443609023, 14.64968152866242, 6.415094339622642, 13.978494623655912])
occupancy_NR_coords_adj_txt_15 = np.array([5.747126436781609, 6.569343065693431, 3.2490974729241873, 32.743362831858406, 9.881422924901186, 24.378109452736318, 26.31578947368421, 32.48407643312102, 26.037735849056602, 34.40860215053764])
occupancy_NR_coords_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_jpg_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_15 = np.array([0.38314176245210724, 0.7299270072992701, 0.36101083032490977, 6.1946902654867255, 3.557312252964427, 8.45771144278607, 3.7593984962406015, 3.1847133757961785, 0.37735849056603776, 9.67741935483871])
occupancy_NR_coords_tokenized_txt_15 = np.array([0.38314176245210724, 0.7299270072992701, 0.36101083032490977, 6.1946902654867255, 4.3478260869565215, 6.467661691542288, 8.270676691729323, 5.7324840764331215, 0.37735849056603776, 11.827956989247312])
# Averages and std deviation 15x15
avg_line_NR_coords_adj_json_15 = np.mean(line_NR_coords_adj_json_15)
avg_line_NR_coords_adj_txt_15 = np.mean(line_NR_coords_adj_txt_15)
avg_line_NR_coords_jpg_15 = np.mean(line_NR_coords_jpg_15)
avg_line_NR_coords_json_15 = np.mean(line_NR_coords_json_15)
avg_line_NR_coords_tokenized_txt_15 = np.mean(line_NR_coords_tokenized_txt_15)
avg_occupancy_NR_coords_adj_json_15 = np.mean(occupancy_NR_coords_adj_json_15)
avg_occupancy_NR_coords_adj_txt_15 = np.mean(occupancy_NR_coords_adj_txt_15)
avg_occupancy_NR_coords_ascii_txt_15 = np.mean(occupancy_NR_coords_ascii_txt_15)  
avg_occupancy_NR_coords_jpg_15 = np.mean(occupancy_NR_coords_jpg_15)
avg_occupancy_NR_coords_json_15 = np.mean(occupancy_NR_coords_json_15)
avg_occupancy_NR_coords_tokenized_txt_15 = np.mean(occupancy_NR_coords_tokenized_txt_15)
sd_line_NR_coords_adj_json_15 = np.std(line_NR_coords_adj_json_15)
sd_line_NR_coords_adj_txt_15 = np.std(line_NR_coords_adj_txt_15)
sd_line_NR_coords_jpg_15 = np.std(line_NR_coords_jpg_15)
sd_line_NR_coords_json_15 = np.std(line_NR_coords_json_15)
sd_line_NR_coords_tokenized_txt_15 = np.std(line_NR_coords_tokenized_txt_15)
sd_occupancy_NR_coords_adj_json_15 = np.std(occupancy_NR_coords_adj_json_15)
sd_occupancy_NR_coords_adj_txt_15 = np.std(occupancy_NR_coords_adj_txt_15)
sd_occupancy_NR_coords_ascii_txt_15 = np.std(occupancy_NR_coords_ascii_txt_15)  
sd_occupancy_NR_coords_jpg_15 = np.std(occupancy_NR_coords_jpg_15)
sd_occupancy_NR_coords_json_15 = np.std(occupancy_NR_coords_json_15)
sd_occupancy_NR_coords_tokenized_txt_15 = np.std(occupancy_NR_coords_tokenized_txt_15)

# Top plot data
means_line_NR_coords = [
    [avg_line_NR_coords_adj_json,       avg_line_NR_coords_adj_json_6,       avg_line_NR_coords_adj_json_15],
    [avg_line_NR_coords_adj_txt,        avg_line_NR_coords_adj_txt_6,        avg_line_NR_coords_adj_txt_15],
    [avg_line_NR_coords_jpg,            avg_line_NR_coords_jpg_6,            avg_line_NR_coords_jpg_15],
    [avg_line_NR_coords_json,           avg_line_NR_coords_json_6,           avg_line_NR_coords_json_15],
    [avg_line_NR_coords_tokenized_txt,  avg_line_NR_coords_tokenized_txt_6,  avg_line_NR_coords_tokenized_txt_15]
]

std_line_NR_coords = [
    [sd_line_NR_coords_adj_json,       sd_line_NR_coords_adj_json_6,       sd_line_NR_coords_adj_json_15],
    [sd_line_NR_coords_adj_txt,        sd_line_NR_coords_adj_txt_6,        sd_line_NR_coords_adj_txt_15],
    [sd_line_NR_coords_jpg,            sd_line_NR_coords_jpg_6,            sd_line_NR_coords_jpg_15],
    [sd_line_NR_coords_json,           sd_line_NR_coords_json_6,           sd_line_NR_coords_tokenized_txt_15]
]

error_line_NR_coords = [
    [confidence_interval(line_NR_coords_adj_json),       confidence_interval(line_NR_coords_adj_json_6),       confidence_interval(line_NR_coords_adj_json_15)],
    [confidence_interval(line_NR_coords_adj_txt),        confidence_interval(line_NR_coords_adj_txt_6),        confidence_interval(line_NR_coords_adj_txt_15)],
    [confidence_interval(line_NR_coords_jpg),            confidence_interval(line_NR_coords_jpg_6),            confidence_interval(line_NR_coords_jpg_15)],
    [confidence_interval(line_NR_coords_json),           confidence_interval(line_NR_coords_json_6),           confidence_interval(line_NR_coords_json_15)],
    [confidence_interval(line_NR_coords_tokenized_txt),  confidence_interval(line_NR_coords_tokenized_txt_6),  confidence_interval(line_NR_coords_tokenized_txt_15)]
]

labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data
means_occ_NR_coords = [
    [avg_occupancy_NR_coords_adj_json,       avg_occupancy_NR_coords_adj_json_6,      avg_occupancy_NR_coords_adj_json_15],
    [avg_occupancy_NR_coords_adj_txt,        avg_occupancy_NR_coords_adj_txt_6,        avg_occupancy_NR_coords_adj_txt_15],
    [avg_occupancy_NR_coords_ascii_txt,      avg_occupancy_NR_coords_ascii_txt_6,      avg_occupancy_NR_coords_ascii_txt_15],
    [avg_occupancy_NR_coords_jpg,            avg_occupancy_NR_coords_jpg_6,            avg_occupancy_NR_coords_jpg_15],
    [avg_occupancy_NR_coords_json,           avg_occupancy_NR_coords_json_6,           avg_occupancy_NR_coords_json_15],
    [avg_occupancy_NR_coords_tokenized_txt,  avg_occupancy_NR_coords_tokenized_txt_6,  avg_occupancy_NR_coords_tokenized_txt_15]
]

std_occ_NR_coords = [
    [sd_occupancy_NR_coords_adj_json,       sd_occupancy_NR_coords_adj_json_6,       sd_occupancy_NR_coords_adj_json_15],
    [sd_occupancy_NR_coords_adj_txt,        sd_occupancy_NR_coords_adj_txt_6,        sd_occupancy_NR_coords_adj_txt_15],
    [sd_occupancy_NR_coords_jpg,            sd_occupancy_NR_coords_jpg_6,            sd_occupancy_NR_coords_jpg_15],
    [sd_occupancy_NR_coords_json,           sd_occupancy_NR_coords_json_6,           sd_occupancy_NR_coords_json_15],
    [sd_occupancy_NR_coords_tokenized_txt,  sd_occupancy_NR_coords_tokenized_txt_6,  sd_occupancy_NR_coords_tokenized_txt_15],
    [sd_occupancy_NR_coords_ascii_txt,      sd_occupancy_NR_coords_ascii_txt_6,      sd_occupancy_NR_coords_ascii_txt_15]
]

error_occupancy_NR_coords = [
    [confidence_interval(occupancy_NR_coords_adj_json),       confidence_interval(occupancy_NR_coords_adj_json_6),       confidence_interval(occupancy_NR_coords_adj_json_15)],
    [confidence_interval(occupancy_NR_coords_adj_txt),        confidence_interval(occupancy_NR_coords_adj_txt_6),        confidence_interval(occupancy_NR_coords_adj_txt_15)],
    [confidence_interval(occupancy_NR_coords_jpg),            confidence_interval(occupancy_NR_coords_jpg_6),            confidence_interval(occupancy_NR_coords_jpg_15)],
    [confidence_interval(occupancy_NR_coords_json),           confidence_interval(occupancy_NR_coords_json_6),           confidence_interval(occupancy_NR_coords_json_15)],
    [confidence_interval(occupancy_NR_coords_tokenized_txt),  confidence_interval(occupancy_NR_coords_tokenized_txt_6),  confidence_interval(occupancy_NR_coords_tokenized_txt_15)],
    [ confidence_interval(occupancy_NR_coords_ascii_txt),     confidence_interval(occupancy_NR_coords_ascii_txt_6),      confidence_interval(occupancy_NR_coords_ascii_txt_15)]
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized",
    "Occupancy ASCII"
]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02
# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line_NR_coords, error_line_NR_coords, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_line_NR_coords[1]))
#     ax1.errorbar(
#         x_vals + jitter, means, yerr=stds, #change in for-loop definition to sd's if you want to display sd as error bars. Currently set to confidence intervals
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel("Complexity")
# ax1.set_ylabel("Accuracy [%]")
# ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Coordinates Output")
# ax1.legend(loc='best')
# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Create bottom plot
# for means, stds, label in zip(means_occ_NR_coords, error_occupancy_NR_coords, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_occupancy_NR_coords[1]))
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
# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()


# NR -- Allo -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Allo 3x3
line_NR_allo_adj_json = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 100.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_adj_txt = np.array([0.0, 100.0, 0.0, 100.0, 0.0, 0.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_jpg = np.array([50.0, 0.0, 50.0, 100.0, 33.33333333333333, 50.0, 100.0, 0.0, 0.0, 0.0])
line_NR_allo_json = np.array([100.0, 0.0, 100.0, 0.0, 33.33333333333333, 100.0, 0.0, 0.0, 33.33333333333333, 0.0])
line_NR_allo_tokenized_txt = np.array([0.0, 100.0, 0.0, 25.0, 0.0, 0.0, 25.0, 33.33333333333333, 0.0, 25.0])
occupancy_NR_allo_adj_json = np.array([50.0, 25.0, 75.0, 110.00000000000001, 0.0, 50.0, 110.00000000000001, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_NR_allo_adj_txt = np.array([62.5, 25.0, 0.0, 37.5, 33.33333333333333, 25.0, 37.5, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_NR_allo_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 62.5, 33.33333333333333, 33.33333333333333, 0.0])
occupancy_NR_allo_jpg = np.array([12.5, 0.0, 12.5, 0.0, 8.333333333333332, 12.5, 12.5, 8.333333333333332, 8.333333333333332, 0.0])
occupancy_NR_allo_json = np.array([62.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 33.33333333333333, 0.0, 87.5])
occupancy_NR_allo_tokenized_txt = np.array([0.0, 0.0, 0.0, 50.0, 8.333333333333332, 12.5, 0.0, 8.333333333333332, 0.0, 110.00000000000001])
# Averages and std deviation 3x3
avg_line_NR_allo_adj_json = np.mean(line_NR_allo_adj_json)
avg_line_NR_allo_adj_txt = np.mean(line_NR_allo_adj_txt)
avg_line_NR_allo_jpg = np.mean(line_NR_allo_jpg)
avg_line_NR_allo_json = np.mean(line_NR_allo_json)
avg_line_NR_allo_tokenized_txt = np.mean(line_NR_allo_tokenized_txt)
avg_occupancy_NR_allo_adj_json = np.mean(occupancy_NR_allo_adj_json)
avg_occupancy_NR_allo_adj_txt = np.mean(occupancy_NR_allo_adj_txt)
avg_occupancy_NR_allo_ascii_txt = np.mean(occupancy_NR_allo_ascii_txt)  
avg_occupancy_NR_allo_jpg = np.mean(occupancy_NR_allo_jpg)
avg_occupancy_NR_allo_json = np.mean(occupancy_NR_allo_json)
avg_occupancy_NR_allo_tokenized_txt = np.mean(occupancy_NR_allo_tokenized_txt)
sd_line_NR_allo_adj_json = np.std(line_NR_allo_adj_json)
sd_line_NR_allo_adj_txt = np.std(line_NR_allo_adj_txt)
sd_line_NR_allo_jpg = np.std(line_NR_allo_jpg)
sd_line_NR_allo_json = np.std(line_NR_allo_json)
sd_line_NR_allo_tokenized_txt = np.std(line_NR_allo_tokenized_txt)
sd_occupancy_NR_allo_adj_json = np.std(occupancy_NR_allo_adj_json)
sd_occupancy_NR_allo_adj_txt = np.std(occupancy_NR_allo_adj_txt)
sd_occupancy_NR_allo_ascii_txt = np.std(occupancy_NR_allo_ascii_txt)  
sd_occupancy_NR_allo_jpg = np.std(occupancy_NR_allo_jpg)
sd_occupancy_NR_allo_json = np.std(occupancy_NR_allo_json)
sd_occupancy_NR_allo_tokenized_txt = np.std(occupancy_NR_allo_tokenized_txt)
# Accuracy NR Allo 6x6
line_NR_allo_adj_json_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 0.0, 20.0, 8.333333333333332, 110.00000000000001, 12.5, 15.0])
line_NR_allo_adj_txt_6 = np.array([25.0, 0.0, 11.76470588235294, 17.857142857142858, 21.428571428571427, 5.0, 0.0, 60.0, 0.0, 5.0])
line_NR_allo_jpg_6 = np.array([6.25, 0.0, 2.941176470588235, 0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 10.0])
line_NR_allo_json_6 = np.array([12.5, 5.555555555555555, 0.0, 17.857142857142858, 21.428571428571427, 0.0, 12.5, 0.0, 18.75, 0.0])
line_NR_allo_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 3.571428571428571, 21.428571428571427, 5.0, 0.0, 10.0, 0.0, 10.0])
occupancy_NR_allo_adj_json_6 = np.array([18.75, 5.555555555555555, 7.352941176470589, 17.857142857142858, 14.285714285714285, 5.0, 8.333333333333332, 50.0, 6.25, 5.0])
occupancy_NR_allo_adj_txt_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 14.285714285714285, 17.5, 8.333333333333332, 90.0, 18.75, 0.0])
occupancy_NR_allo_ascii_txt_6 = np.array([6.25, 11.11111111111111, 0.0, 21.428571428571427, 0.0, np.nan, 2.083333333333333, 55.00000000000001, 0.0, 7.5])
occupancy_NR_allo_jpg_6 = np.array([0.0, 0.0, 1.4705882352941175, 10.714285714285714, 3.571428571428571, 2.5, 4.166666666666666, 5.0, 3.125, 0.0])
occupancy_NR_allo_json_6 = np.array([0.0, 0.0, 5.88235294117647, 14.285714285714285, 0.0, 10.0, 0.0, 80.0, 0.0, 10.0])
occupancy_NR_allo_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 14.285714285714285, np.nan, 0.0, 0.0, 40.0, 0.0, 2.5])
# Averages and std deviation 6x6
avg_line_NR_allo_adj_json_6 = np.mean(line_NR_allo_adj_json_6)
avg_line_NR_allo_adj_txt_6 = np.mean(line_NR_allo_adj_txt_6)
avg_line_NR_allo_jpg_6 = np.mean(line_NR_allo_jpg_6)
avg_line_NR_allo_json_6 = np.mean(line_NR_allo_json_6)
avg_line_NR_allo_tokenized_txt_6 = np.mean(line_NR_allo_tokenized_txt_6)
avg_occupancy_NR_allo_adj_json_6 = np.mean(occupancy_NR_allo_adj_json_6)
avg_occupancy_NR_allo_adj_txt_6 = np.mean(occupancy_NR_allo_adj_txt_6)
avg_occupancy_NR_allo_ascii_txt_6 = np.mean(occupancy_NR_allo_ascii_txt_6)  
avg_occupancy_NR_allo_jpg_6 = np.mean(occupancy_NR_allo_jpg_6)
avg_occupancy_NR_allo_json_6 = np.mean(occupancy_NR_allo_json_6)
avg_occupancy_NR_allo_tokenized_txt_6 = np.mean(occupancy_NR_allo_tokenized_txt_6)
sd_line_NR_allo_adj_json_6 = np.std(line_NR_allo_adj_json_6)
sd_line_NR_allo_adj_txt_6 = np.std(line_NR_allo_adj_txt_6)
sd_line_NR_allo_jpg_6 = np.std(line_NR_allo_jpg_6)
sd_line_NR_allo_json_6 = np.std(line_NR_allo_json_6)
sd_line_NR_allo_tokenized_txt_6 = np.std(line_NR_allo_tokenized_txt_6)
sd_occupancy_NR_allo_adj_json_6 = np.std(occupancy_NR_allo_adj_json_6)
sd_occupancy_NR_allo_adj_txt_6 = np.std(occupancy_NR_allo_adj_txt_6)
sd_occupancy_NR_allo_ascii_txt_6 = np.std(occupancy_NR_allo_ascii_txt_6)  
sd_occupancy_NR_allo_jpg_6 = np.std(occupancy_NR_allo_jpg_6)
sd_occupancy_NR_allo_json_6 = np.std(occupancy_NR_allo_json_6)
sd_occupancy_NR_allo_tokenized_txt_6 = np.std(occupancy_NR_allo_tokenized_txt_6)
# Accuracy NR Allo 15x15
line_NR_allo_adj_json_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 3.1746031746031744, 8.0, 1.5151515151515151, 1.282051282051282, 0.0, 2.1739130434782608])
line_NR_allo_adj_txt_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 3.968253968253968, 10.0, 1.5151515151515151, 1.282051282051282, 0.0, 2.1739130434782608])
line_NR_allo_jpg_15 = np.array([np.nan, 0.0, 0.0, 3.571428571428571, 0.7936507936507936, np.nan, np.nan, np.nan, 0.0, 10.869565217391305])
line_NR_allo_json_15 = np.array([1.5384615384615385, 4.411764705882353, 0.7246376811594203, 1.7857142857142856, 1.5873015873015872, 8.0, 0.0, np.nan, 0.7575757575757576, np.nan])
line_NR_allo_tokenized_txt_15 = np.array([0.0, np.nan, 0.0, 0.0, 0.0, np.nan, 3.0303030303030303, 0.0, 0.0, np.nan])
occupancy_NR_allo_adj_json_15 = np.array([0.7692307692307693, 1.4705882352941175, 2.1739130434782608, np.nan, 2.380952380952381, 7.000000000000001, 2.272727272727273, 2.564102564102564, 1.5151515151515151, 8.695652173913043])
occupancy_NR_allo_adj_txt_15 = np.array([0.0, np.nan, 0.7246376811594203, 0.0, 0.0, 8.0, 3.0303030303030303, np.nan, 0.7575757575757576, 0.0])
occupancy_NR_allo_ascii_txt_15 = np.array([0.0, 0.0, 0.7246376811594203, 2.6785714285714284, 0.0, np.nan, 2.272727272727273, 1.9230769230769231, 0.0, 3.260869565217391])
occupancy_NR_allo_jpg_15 = np.array([0.0, 0.0, 0.0, 0.8928571428571428, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
occupancy_NR_allo_json_15 = np.array([0.0, 0.0, 0.0, 0.8928571428571428, 2.380952380952381, 0.0, 0.7575757575757576, 0.641025641025641, 0.0, 1.0869565217391304])
occupancy_NR_allo_tokenized_txt_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 2.380952380952381, 6.0, 3.0303030303030303, 1.9230769230769231, 0.0, 4.3478260869565215])
# Averages and std deviation 15x15
avg_line_NR_allo_adj_json_15 = np.mean(line_NR_allo_adj_json_15)
avg_line_NR_allo_adj_txt_15 = np.mean(line_NR_allo_adj_txt_15)
avg_line_NR_allo_jpg_15 = np.mean(line_NR_allo_jpg_15)
avg_line_NR_allo_json_15 = np.mean(line_NR_allo_json_15)
avg_line_NR_allo_tokenized_txt_15 = np.mean(line_NR_allo_tokenized_txt_15)
avg_occupancy_NR_allo_adj_json_15 = np.mean(occupancy_NR_allo_adj_json_15)
avg_occupancy_NR_allo_adj_txt_15 = np.mean(occupancy_NR_allo_adj_txt_15)
avg_occupancy_NR_allo_ascii_txt_15 = np.mean(occupancy_NR_allo_ascii_txt_15)  
avg_occupancy_NR_allo_jpg_15 = np.mean(occupancy_NR_allo_jpg_15)
avg_occupancy_NR_allo_json_15 = np.mean(occupancy_NR_allo_json_15)
avg_occupancy_NR_allo_tokenized_txt_15 = np.mean(occupancy_NR_allo_tokenized_txt_15)
sd_line_NR_allo_adj_json_15 = np.std(line_NR_allo_adj_json_15)
sd_line_NR_allo_adj_txt_15 = np.std(line_NR_allo_adj_txt_15)
sd_line_NR_allo_jpg_15 = np.std(line_NR_allo_jpg_15)
sd_line_NR_allo_json_15 = np.std(line_NR_allo_json_15)
sd_line_NR_allo_tokenized_txt_15 = np.std(line_NR_allo_tokenized_txt_15)
sd_occupancy_NR_allo_adj_json_15 = np.std(occupancy_NR_allo_adj_json_15)
sd_occupancy_NR_allo_adj_txt_15 = np.std(occupancy_NR_allo_adj_txt_15)
sd_occupancy_NR_allo_ascii_txt_15 = np.std(occupancy_NR_allo_ascii_txt_15)  
sd_occupancy_NR_allo_jpg_15 = np.std(occupancy_NR_allo_jpg_15)
sd_occupancy_NR_allo_json_15 = np.std(occupancy_NR_allo_json_15)
sd_occupancy_NR_allo_tokenized_txt_15 = np.std(occupancy_NR_allo_tokenized_txt_15)


# Top plot data
means_line_NR_allo = [
    [avg_line_NR_allo_adj_json,       avg_line_NR_allo_adj_json_6,       avg_line_NR_allo_adj_json_15],
    [avg_line_NR_allo_adj_txt,        avg_line_NR_allo_adj_txt_6,        avg_line_NR_allo_adj_txt_15],
    [avg_line_NR_allo_jpg,            avg_line_NR_allo_jpg_6,            avg_line_NR_allo_jpg_15],
    [avg_line_NR_allo_json,           avg_line_NR_allo_json_6,           avg_line_NR_allo_json_15],
    [avg_line_NR_allo_tokenized_txt,  avg_line_NR_allo_tokenized_txt_6,  avg_line_NR_allo_tokenized_txt_15]
]

std_line_NR_allo = [
    [sd_line_NR_allo_adj_json,       sd_line_NR_allo_adj_json_6,       sd_line_NR_allo_adj_json_15],
    [sd_line_NR_allo_adj_txt,        sd_line_NR_allo_adj_txt_6,        sd_line_NR_allo_adj_txt_15],
    [sd_line_NR_allo_jpg,            sd_line_NR_allo_jpg_6,            sd_line_NR_allo_jpg_15],
    [sd_line_NR_allo_json,           sd_line_NR_allo_json_6,           sd_line_NR_allo_json_15],
    [sd_line_NR_allo_tokenized_txt,  sd_line_NR_allo_tokenized_txt_6,  sd_line_NR_allo_tokenized_txt_15]
]

error_line_NR_allo = [
    [confidence_interval(line_NR_allo_adj_json),       confidence_interval(line_NR_allo_adj_json_6),       confidence_interval(line_NR_allo_adj_json_15)],
    [confidence_interval(line_NR_allo_adj_txt),        confidence_interval(line_NR_allo_adj_txt_6),        confidence_interval(line_NR_allo_adj_txt_15)],
    [confidence_interval(line_NR_allo_jpg),            confidence_interval(line_NR_allo_jpg_6),            confidence_interval(line_NR_allo_jpg_15)],
    [confidence_interval(line_NR_allo_json),           confidence_interval(line_NR_allo_json_6),           confidence_interval(line_NR_allo_json_15)],
    [confidence_interval(line_NR_allo_tokenized_txt),  confidence_interval(line_NR_allo_tokenized_txt_6),  confidence_interval(line_NR_allo_tokenized_txt_15)]
]


labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data
means_occ_NR_allo = [
    [avg_occupancy_NR_allo_adj_json,       avg_occupancy_NR_allo_adj_json_6,       avg_occupancy_NR_allo_adj_json_15],
    [avg_occupancy_NR_allo_adj_txt,        avg_occupancy_NR_allo_adj_txt_6,        avg_occupancy_NR_allo_adj_txt_15],
    [avg_occupancy_NR_allo_ascii_txt,      avg_occupancy_NR_allo_ascii_txt_6,      avg_occupancy_NR_allo_ascii_txt_15],
    [avg_occupancy_NR_allo_jpg,            avg_occupancy_NR_allo_jpg_6,            avg_occupancy_NR_allo_jpg_15],
    [avg_occupancy_NR_allo_json,           avg_occupancy_NR_allo_json_6,           avg_occupancy_NR_allo_json_15],
    [avg_occupancy_NR_allo_tokenized_txt,  avg_occupancy_NR_allo_tokenized_txt_6,  avg_occupancy_NR_allo_tokenized_txt_15]
]

std_occ_NR_allo = [
    [sd_occupancy_NR_allo_adj_json,       sd_occupancy_NR_allo_adj_json_6,       sd_occupancy_NR_allo_adj_json_15],
    [sd_occupancy_NR_allo_adj_txt,        sd_occupancy_NR_allo_adj_txt_6,        sd_occupancy_NR_allo_adj_txt_15],
    [sd_occupancy_NR_allo_jpg,            sd_occupancy_NR_allo_jpg_6,            sd_occupancy_NR_allo_jpg_15],
    [sd_occupancy_NR_allo_json,           sd_occupancy_NR_allo_json_6,           sd_occupancy_NR_allo_json_15],
    [sd_occupancy_NR_allo_tokenized_txt,  sd_occupancy_NR_allo_tokenized_txt_6,  sd_occupancy_NR_allo_tokenized_txt_15],
    [sd_occupancy_NR_allo_ascii_txt,      sd_occupancy_NR_allo_ascii_txt_6,      sd_occupancy_NR_allo_ascii_txt_15]
]

error_occupancy_NR_allo = [
    [confidence_interval(occupancy_NR_allo_adj_json),       confidence_interval(occupancy_NR_allo_adj_json_6),       confidence_interval(occupancy_NR_allo_adj_json_15)],
    [confidence_interval(occupancy_NR_allo_adj_txt),        confidence_interval(occupancy_NR_allo_adj_txt_6),        confidence_interval(occupancy_NR_allo_adj_txt_15)],
    [confidence_interval(occupancy_NR_allo_jpg),            confidence_interval(occupancy_NR_allo_jpg_6),            confidence_interval(occupancy_NR_allo_jpg_15)],
    [confidence_interval(occupancy_NR_allo_json),           confidence_interval(occupancy_NR_allo_json_6),           confidence_interval(occupancy_NR_allo_json_15)],
    [confidence_interval(occupancy_NR_allo_tokenized_txt),  confidence_interval(occupancy_NR_allo_tokenized_txt_6),  confidence_interval(occupancy_NR_allo_tokenized_txt_15)],
    [ confidence_interval(occupancy_NR_allo_ascii_txt),     confidence_interval(occupancy_NR_allo_ascii_txt_6),      confidence_interval(occupancy_NR_allo_ascii_txt_15)]
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized",
    "Occupancy ASCII"
]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02
# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line_NR_allo, error_line_NR_allo, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line_NR_allo[1]))
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
# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Create bottom plot
# for means, stds, label in zip(means_occ_NR_allo, error_occupancy_NR_allo, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_occupancy_NR_allo[1]))
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
# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()

# NR -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Ego 3x3
line_NR_ego_adj_json = np.array([25.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json = np.array([25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json = np.array([0.0, 0.0, 12.5, 0.0, 8.333333333333332, 0.0, 0.0, 0.0, 8.333333333333332, 0.0])
occupancy_NR_ego_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg = np.array([0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_json = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# Averages and std deviation 3x3
avg_line_NR_ego_adj_json = np.mean(line_NR_ego_adj_json)
avg_line_NR_ego_adj_txt = np.mean(line_NR_ego_adj_txt)
avg_line_NR_ego_jpg = np.mean(line_NR_ego_jpg)
avg_line_NR_ego_json = np.mean(line_NR_ego_json)
avg_line_NR_ego_tokenized_txt = np.mean(line_NR_ego_tokenized_txt)
avg_occupancy_NR_ego_adj_json = np.mean(occupancy_NR_ego_adj_json)
avg_occupancy_NR_ego_adj_txt = np.mean(occupancy_NR_ego_adj_txt)
avg_occupancy_NR_ego_ascii_txt = np.mean(occupancy_NR_ego_ascii_txt)  
avg_occupancy_NR_ego_jpg = np.mean(occupancy_NR_ego_jpg)
avg_occupancy_NR_ego_json = np.mean(occupancy_NR_ego_json)
avg_occupancy_NR_ego_tokenized_txt = np.mean(occupancy_NR_ego_tokenized_txt)
sd_line_NR_ego_adj_json = np.std(line_NR_ego_adj_json)
sd_line_NR_ego_adj_txt = np.std(line_NR_ego_adj_txt)
sd_line_NR_ego_jpg = np.std(line_NR_ego_jpg)
sd_line_NR_ego_json = np.std(line_NR_ego_json)
sd_line_NR_ego_tokenized_txt = np.std(line_NR_ego_tokenized_txt)
sd_occupancy_NR_ego_adj_json = np.std(occupancy_NR_ego_adj_json)
sd_occupancy_NR_ego_adj_txt = np.std(occupancy_NR_ego_adj_txt)
sd_occupancy_NR_ego_ascii_txt = np.std(occupancy_NR_ego_ascii_txt)  
sd_occupancy_NR_ego_jpg = np.std(occupancy_NR_ego_jpg)
sd_occupancy_NR_ego_json = np.std(occupancy_NR_ego_json)
sd_occupancy_NR_ego_tokenized_txt = np.std(occupancy_NR_ego_tokenized_txt)
# Accuracy NR Ego 6x6
line_NR_ego_adj_json_6 = np.array([18.75, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_6 = np.array([12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 0.0, 0.0, 4.166666666666666, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.25, 0.0])
occupancy_NR_ego_adj_json_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_txt_6 = np.array([0.0, 2.7777777777777777, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_6 = np.array([3.125, 2.7777777777777777, 0.0, 0.0, 3.571428571428571, 0.0, 2.083333333333333, 0.0, 0.0, 0.0])
occupancy_NR_ego_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 3.571428571428571, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# Averages and std deviation 6x6
avg_line_NR_ego_adj_json_6 = np.mean(line_NR_ego_adj_json_6)
avg_line_NR_ego_adj_txt_6 = np.mean(line_NR_ego_adj_txt_6)
avg_line_NR_ego_jpg_6 = np.mean(line_NR_ego_jpg_6)
avg_line_NR_ego_json_6 = np.mean(line_NR_ego_json_6)
avg_line_NR_ego_tokenized_txt_6 = np.mean(line_NR_ego_tokenized_txt_6)
avg_occupancy_NR_ego_adj_json_6 = np.mean(occupancy_NR_ego_adj_json_6)
avg_occupancy_NR_ego_adj_txt_6 = np.mean(occupancy_NR_ego_adj_txt_6)
avg_occupancy_NR_ego_ascii_txt_6 = np.mean(occupancy_NR_ego_ascii_txt_6)  
avg_occupancy_NR_ego_jpg_6 = np.mean(occupancy_NR_ego_jpg_6)
avg_occupancy_NR_ego_json_6 = np.mean(occupancy_NR_ego_json_6)
avg_occupancy_NR_ego_tokenized_txt_6 = np.mean(occupancy_NR_ego_tokenized_txt_6)
sd_line_NR_ego_adj_json_6 = np.std(line_NR_ego_adj_json_6)
sd_line_NR_ego_adj_txt_6 = np.std(line_NR_ego_adj_txt_6)
sd_line_NR_ego_jpg_6 = np.std(line_NR_ego_jpg_6)
sd_line_NR_ego_json_6 = np.std(line_NR_ego_json_6)
sd_line_NR_ego_tokenized_txt_6 = np.std(line_NR_ego_tokenized_txt_6)
sd_occupancy_NR_ego_adj_json_6 = np.std(occupancy_NR_ego_adj_json_6)
sd_occupancy_NR_ego_adj_txt_6 = np.std(occupancy_NR_ego_adj_txt_6)
sd_occupancy_NR_ego_ascii_txt_6 = np.std(occupancy_NR_ego_ascii_txt_6)  
sd_occupancy_NR_ego_jpg_6 = np.std(occupancy_NR_ego_jpg_6)
sd_occupancy_NR_ego_json_6 = np.std(occupancy_NR_ego_json_6)
sd_occupancy_NR_ego_tokenized_txt_6 = np.std(occupancy_NR_ego_tokenized_txt_6)
# Accuracy NR Ego 15x15
line_NR_ego_adj_json_15 = np.array([0.0, 0.0, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_15 = np.array([1.5384615384615385, 4.411764705882353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_NR_ego_jpg_15 = np.array([1.5384615384615385, 5.88235294117647, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_NR_ego_json_15 = np.array([1.5384615384615385, 0.0, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_NR_ego_tokenized_txt_15 = np.array([0.7692307692307693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_NR_ego_adj_txt_15 = np.array([1.5384615384615385, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_NR_ego_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_15 = np.array([0.7692307692307693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
occupancy_NR_ego_json_15 = np.array([0.0, 0.0, 0.36231884057971014, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
occupancy_NR_ego_tokenized_txt_15 = np.array([0.38461538461538464, 4.411764705882353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
# Averages and std deviation 15x15
avg_line_NR_ego_adj_json_15 = np.mean(line_NR_ego_adj_json_15)
avg_line_NR_ego_adj_txt_15 = np.mean(line_NR_ego_adj_txt_15)
avg_line_NR_ego_jpg_15 = np.mean(line_NR_ego_jpg_15)
avg_line_NR_ego_json_15 = np.mean(line_NR_ego_json_15)
avg_line_NR_ego_tokenized_txt_15 = np.mean(line_NR_ego_tokenized_txt_15)
avg_occupancy_NR_ego_adj_json_15 = np.mean(occupancy_NR_ego_adj_json_15)
avg_occupancy_NR_ego_adj_txt_15 = np.mean(occupancy_NR_ego_adj_txt_15)
avg_occupancy_NR_ego_ascii_txt_15 = np.mean(occupancy_NR_ego_ascii_txt_15)  
avg_occupancy_NR_ego_jpg_15 = np.mean(occupancy_NR_ego_jpg_15)
avg_occupancy_NR_ego_json_15 = np.mean(occupancy_NR_ego_json_15)
avg_occupancy_NR_ego_tokenized_txt_15 = np.mean(occupancy_NR_ego_tokenized_txt_15)
sd_line_NR_ego_adj_json_15 = np.std(line_NR_ego_adj_json_15)
sd_line_NR_ego_adj_txt_15 = np.std(line_NR_ego_adj_txt_15)
sd_line_NR_ego_jpg_15 = np.std(line_NR_ego_jpg_15)
sd_line_NR_ego_json_15 = np.std(line_NR_ego_json_15)
sd_line_NR_ego_tokenized_txt_15 = np.std(line_NR_ego_tokenized_txt_15)
sd_occupancy_NR_ego_adj_json_15 = np.std(occupancy_NR_ego_adj_json_15)
sd_occupancy_NR_ego_adj_txt_15 = np.std(occupancy_NR_ego_adj_txt_15)
sd_occupancy_NR_ego_ascii_txt_15 = np.std(occupancy_NR_ego_ascii_txt_15)  
sd_occupancy_NR_ego_jpg_15 = np.std(occupancy_NR_ego_jpg_15)
sd_occupancy_NR_ego_json_15 = np.std(occupancy_NR_ego_json_15)
sd_occupancy_NR_ego_tokenized_txt_15 = np.std(occupancy_NR_ego_tokenized_txt_15)


# Top plot data
means_line_NR_ego = [
    [avg_line_NR_ego_adj_json,       avg_line_NR_ego_adj_json_6,       avg_line_NR_ego_adj_json_15],
    [avg_line_NR_ego_adj_txt,        avg_line_NR_ego_adj_txt_6,        avg_line_NR_ego_adj_txt_15],
    [avg_line_NR_ego_jpg,            avg_line_NR_ego_jpg_6,            avg_line_NR_ego_jpg_15],
    [avg_line_NR_ego_json,           avg_line_NR_ego_json_6,           avg_line_NR_ego_json_15],
    [avg_line_NR_ego_tokenized_txt,  avg_line_NR_ego_tokenized_txt_6,  avg_line_NR_ego_tokenized_txt_15]
]

std_line_NR_ego = [
    [sd_line_NR_ego_adj_json,       sd_line_NR_ego_adj_json_6,       sd_line_NR_ego_adj_json_15],
    [sd_line_NR_ego_adj_txt,        sd_line_NR_ego_adj_txt_6,        sd_line_NR_ego_adj_txt_15],
    [sd_line_NR_ego_jpg,            sd_line_NR_ego_jpg_6,            sd_line_NR_ego_jpg_15],
    [sd_line_NR_ego_json,           sd_line_NR_ego_json_6,           sd_line_NR_ego_json_15],
    [sd_line_NR_ego_tokenized_txt,  sd_line_NR_ego_tokenized_txt_6,  sd_line_NR_ego_tokenized_txt_15]
]

error_line_NR_ego = [
    [confidence_interval(line_NR_ego_adj_json),       confidence_interval(line_NR_ego_adj_json_6),       confidence_interval(line_NR_ego_adj_json_15)],
    [confidence_interval(line_NR_ego_adj_txt),        confidence_interval(line_NR_ego_adj_txt_6),        confidence_interval(line_NR_ego_adj_txt_15)],
    [confidence_interval(line_NR_ego_jpg),            confidence_interval(line_NR_ego_jpg_6),            confidence_interval(line_NR_ego_jpg_15)],
    [confidence_interval(line_NR_ego_json),           confidence_interval(line_NR_ego_json_6),           confidence_interval(line_NR_ego_json_15)],
    [confidence_interval(line_NR_ego_tokenized_txt),  confidence_interval(line_NR_ego_tokenized_txt_6),  confidence_interval(line_NR_ego_tokenized_txt_15)]
]

labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data
means_occ_NR_ego = [
    [avg_occupancy_NR_ego_adj_json,       avg_occupancy_NR_ego_adj_json_6,       avg_occupancy_NR_ego_adj_json_15],
    [avg_occupancy_NR_ego_adj_txt,        avg_occupancy_NR_ego_adj_txt_6,        avg_occupancy_NR_ego_adj_txt_15],
    [avg_occupancy_NR_ego_ascii_txt,      avg_occupancy_NR_ego_ascii_txt_6,      avg_occupancy_NR_ego_ascii_txt_15],
    [avg_occupancy_NR_ego_jpg,            avg_occupancy_NR_ego_jpg_6,            avg_occupancy_NR_ego_jpg_15],
    [avg_occupancy_NR_ego_json,           avg_occupancy_NR_ego_json_6,           avg_occupancy_NR_ego_json_15],
    [avg_occupancy_NR_ego_tokenized_txt,  avg_occupancy_NR_ego_tokenized_txt_6,  avg_occupancy_NR_ego_tokenized_txt_15]
]

std_occ_NR_ego = [
    [sd_occupancy_NR_ego_adj_json,       sd_occupancy_NR_ego_adj_json_6,       sd_occupancy_NR_ego_adj_json_15],
    [sd_occupancy_NR_ego_adj_txt,        sd_occupancy_NR_ego_adj_txt_6,        sd_occupancy_NR_ego_adj_txt_15],
    [sd_occupancy_NR_ego_jpg,            sd_occupancy_NR_ego_jpg_6,            sd_occupancy_NR_ego_jpg_15],
    [sd_occupancy_NR_ego_json,           sd_occupancy_NR_ego_json_6,           sd_occupancy_NR_ego_json_15],
    [sd_occupancy_NR_ego_tokenized_txt,  sd_occupancy_NR_ego_tokenized_txt_6,  sd_occupancy_NR_ego_tokenized_txt_15],
    [sd_occupancy_NR_ego_ascii_txt,      sd_occupancy_NR_ego_ascii_txt_6,      sd_occupancy_NR_ego_ascii_txt_15],
]

error_occupancy_NR_ego = [
    [confidence_interval(occupancy_NR_ego_adj_json),       confidence_interval(occupancy_NR_ego_adj_json_6),       confidence_interval(occupancy_NR_ego_adj_json_15)],
    [confidence_interval(occupancy_NR_ego_adj_txt),        confidence_interval(occupancy_NR_ego_adj_txt_6),        confidence_interval(occupancy_NR_ego_adj_txt_15)],
    [confidence_interval(occupancy_NR_ego_jpg),            confidence_interval(occupancy_NR_ego_jpg_6),            confidence_interval(occupancy_NR_ego_jpg_15)],
    [confidence_interval(occupancy_NR_ego_json),           confidence_interval(occupancy_NR_ego_json_6),           confidence_interval(occupancy_NR_ego_json_15)],
    [confidence_interval(occupancy_NR_ego_tokenized_txt),  confidence_interval(occupancy_NR_ego_tokenized_txt_6),  confidence_interval(occupancy_NR_ego_tokenized_txt_15)],
    [ confidence_interval(occupancy_NR_ego_ascii_txt),     confidence_interval(occupancy_NR_ego_ascii_txt_6),      confidence_interval(occupancy_NR_ego_ascii_txt_15)]
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized",
    "Occupancy ASCII"
]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02

# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line_NR_ego, error_line_NR_ego, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_line_NR_ego[1]))
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
# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Create bottom plot
# for means, stds, label in zip(means_occ_NR_ego, error_occupancy_NR_ego, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_occupancy_NR_ego[1]))
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
# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()



# R -- Coords -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Coords 3x3
line_R_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_jpg = np.array([40.0, 100.0, 100.0, 100.0, 28.57142857142857, 40.0, 40.0, 100.0, 100.0, 100.0])
line_R_coords_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_ascii_txt = np.array([22.22222222222222, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 46.15384615384615, 77.77777777777779])
occupancy_R_coords_jpg = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556, 0.0, 7.6923076923076925, 11.11111111111111, 33.33333333333333, 0.0, 7.6923076923076925, 100.0])
occupancy_R_coords_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 3x3
avg_line_R_coords_adj_json = np.mean(line_R_coords_adj_json)
avg_line_R_coords_adj_txt = np.mean(line_R_coords_adj_txt)
avg_line_R_coords_jpg = np.mean(line_R_coords_jpg)
avg_line_R_coords_json = np.mean(line_R_coords_json)
avg_line_R_coords_tokenized_txt = np.mean(line_R_coords_tokenized_txt)
avg_occupancy_R_coords_adj_json = np.mean(occupancy_R_coords_adj_json)
avg_occupancy_R_coords_adj_txt = np.mean(occupancy_R_coords_adj_txt)
avg_occupancy_R_coords_ascii_txt = np.mean(occupancy_R_coords_ascii_txt)  
avg_occupancy_R_coords_jpg = np.mean(occupancy_R_coords_jpg)
avg_occupancy_R_coords_json = np.mean(occupancy_R_coords_json)
avg_occupancy_R_coords_tokenized_txt = np.mean(occupancy_R_coords_tokenized_txt)
sd_line_R_coords_adj_json = np.std(line_R_coords_adj_json)
sd_line_R_coords_adj_txt = np.std(line_R_coords_adj_txt)
sd_line_R_coords_jpg = np.std(line_R_coords_jpg)
sd_line_R_coords_json = np.std(line_R_coords_json)
sd_line_R_coords_tokenized_txt = np.std(line_R_coords_tokenized_txt)
sd_occupancy_R_coords_adj_json = np.std(occupancy_R_coords_adj_json)
sd_occupancy_R_coords_adj_txt = np.std(occupancy_R_coords_adj_txt)
sd_occupancy_R_coords_ascii_txt = np.std(occupancy_R_coords_ascii_txt)  
sd_occupancy_R_coords_jpg = np.std(occupancy_R_coords_jpg)
sd_occupancy_R_coords_json = np.std(occupancy_R_coords_json)
sd_occupancy_R_coords_tokenized_txt = np.std(occupancy_R_coords_tokenized_txt)
# Accuracy R Coords 6x6
line_R_coords_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_ascii_txt_6 = np.array([24.242424242424242, 32.432432432432435, 11.594202898550725, 1.7543859649122806, 31.03448275862069, 2.4390243902439024, 2.0408163265306123, 0.0, 27.27272727272727, 2.4390243902439024])
occupancy_R_coords_jpg_6 = np.array([0.0, 2.7027027027027026, 0.0, 0.0, 0.0, 2.4390243902439024, 0.0, 0.0, 0.0, 0.0])
occupancy_R_coords_json_6 = np.array([27.27272727272727, 48.64864864864865, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 60.60606060606061, 100.0])
occupancy_R_coords_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 6x6
avg_line_R_coords_adj_json_6 = np.mean(line_R_coords_adj_json_6)
avg_line_R_coords_adj_txt_6 = np.mean(line_R_coords_adj_txt_6)
avg_line_R_coords_jpg_6 = np.mean(line_R_coords_jpg_6)
avg_line_R_coords_json_6 = np.mean(line_R_coords_json_6)
avg_line_R_coords_tokenized_txt_6 = np.mean(line_R_coords_tokenized_txt_6)
avg_occupancy_R_coords_adj_json_6 = np.mean(occupancy_R_coords_adj_json_6)
avg_occupancy_R_coords_adj_txt_6 = np.mean(occupancy_R_coords_adj_txt_6)
avg_occupancy_R_coords_ascii_txt_6 = np.mean(occupancy_R_coords_ascii_txt_6)  
avg_occupancy_R_coords_jpg_6 = np.mean(occupancy_R_coords_jpg_6)
avg_occupancy_R_coords_json_6 = np.mean(occupancy_R_coords_json_6)
avg_occupancy_R_coords_tokenized_txt_6 = np.mean(occupancy_R_coords_tokenized_txt_6)
sd_line_R_coords_adj_json_6 = np.std(line_R_coords_adj_json_6)
sd_line_R_coords_adj_txt_6 = np.std(line_R_coords_adj_txt_6)
sd_line_R_coords_jpg_6 = np.std(line_R_coords_jpg_6)
sd_line_R_coords_json_6 = np.std(line_R_coords_json_6)
sd_line_R_coords_tokenized_txt_6 = np.std(line_R_coords_tokenized_txt_6)
sd_occupancy_R_coords_adj_json_6 = np.std(occupancy_R_coords_adj_json_6)
sd_occupancy_R_coords_adj_txt_6 = np.std(occupancy_R_coords_adj_txt_6)
sd_occupancy_R_coords_ascii_txt_6 = np.std(occupancy_R_coords_ascii_txt_6)  
sd_occupancy_R_coords_jpg_6 = np.std(occupancy_R_coords_jpg_6)
sd_occupancy_R_coords_json_6 = np.std(occupancy_R_coords_json_6)
sd_occupancy_R_coords_tokenized_txt_6 = np.std(occupancy_R_coords_tokenized_txt_6)
# Accuracy R Coords 15x15
line_R_coords_adj_json_15 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt_15 = np.array([19.083969465648856, 14.492753623188406, 51.798561151079134, 100.0, 60.629921259842526, 92.07920792079209, 100.0, 56.9620253164557, 46.616541353383454, 100.0])
line_R_coords_jpg_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_15 = np.array([23.66412213740458, 15.942028985507244, 7.194244604316546, 7.017543859649122, 12.598425196850393, 9.900990099009901, 56.71641791044776, 50.63291139240506, 1.5037593984962405, 42.5531914893617])
line_R_coords_tokenized_txt_15 = np.array([96.18320610687023, 100.0, 100.0, 100.0, 92.1259842519685, 22.772277227722775, 100.0, 62.0253164556962, 100.0, 100.0])
occupancy_R_coords_adj_json_15 = np.array([100.0, 100.0, 68.95306859205776, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt_15 = np.array([34.099616858237546, 15.328467153284672, 24.90974729241877, 29.20353982300885, 12.25296442687747, 42.28855721393035, 3.7593984962406015, 57.961783439490446, 46.41509433962264, 95.6989247311828])
occupancy_R_coords_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.301075268817205])
occupancy_R_coords_jpg_15 = np.array([1.9157088122605364, 4.37956204379562, 1.083032490974729, 0.8849557522123894, 0.3952569169960474, 0.0, 0.7518796992481203, 0.0, 0.0, 0.0])
occupancy_R_coords_json_15 = np.array([11.877394636015326, 35.03649635036496, 1.8050541516245486, 15.04424778761062, 3.557312252964427, 21.393034825870647, 30.075187969924812, 15.92356687898089, 7.169811320754717, 33.33333333333333])
occupancy_R_coords_tokenized_txt_15 = np.array([39.46360153256705, 100.0, 7.581227436823104, 100.0, 7.905138339920949, 7.462686567164178, 100.0, 13.375796178343949, 6.415094339622642, 11.827956989247312])
# Averages and std deviation 15x15
avg_line_R_coords_adj_json_15 = np.mean(line_R_coords_adj_json_15)
avg_line_R_coords_adj_txt_15 = np.mean(line_R_coords_adj_txt_15)
avg_line_R_coords_jpg_15 = np.mean(line_R_coords_jpg_15)
avg_line_R_coords_json_15 = np.mean(line_R_coords_json_15)
avg_line_R_coords_tokenized_txt_15 = np.mean(line_R_coords_tokenized_txt_15)
avg_occupancy_R_coords_adj_json_15 = np.mean(occupancy_R_coords_adj_json_15)
avg_occupancy_R_coords_adj_txt_15 = np.mean(occupancy_R_coords_adj_txt_15)
avg_occupancy_R_coords_ascii_txt_15 = np.mean(occupancy_R_coords_ascii_txt_15)  
avg_occupancy_R_coords_jpg_15 = np.mean(occupancy_R_coords_jpg_15)
avg_occupancy_R_coords_json_15 = np.mean(occupancy_R_coords_json_15)
avg_occupancy_R_coords_tokenized_txt_15 = np.mean(occupancy_R_coords_tokenized_txt_15)
sd_line_R_coords_adj_json_15 = np.std(line_R_coords_adj_json_15)
sd_line_R_coords_adj_txt_15 = np.std(line_R_coords_adj_txt_15)
sd_line_R_coords_jpg_15 = np.std(line_R_coords_jpg_15)
sd_line_R_coords_json_15 = np.std(line_R_coords_json_15)
sd_line_R_coords_tokenized_txt_15 = np.std(line_R_coords_tokenized_txt_15)
sd_occupancy_R_coords_adj_json_15 = np.std(occupancy_R_coords_adj_json_15)
sd_occupancy_R_coords_adj_txt_15 = np.std(occupancy_R_coords_adj_txt_15)
sd_occupancy_R_coords_ascii_txt_15 = np.std(occupancy_R_coords_ascii_txt_15)  
sd_occupancy_R_coords_jpg_15 = np.std(occupancy_R_coords_jpg_15)
sd_occupancy_R_coords_json_15 = np.std(occupancy_R_coords_json_15)
sd_occupancy_R_coords_tokenized_txt_15 = np.std(occupancy_R_coords_tokenized_txt_15)

# Top plot data
means_line_R_coords = [
    [avg_line_R_coords_adj_json,       avg_line_R_coords_adj_json_6,       avg_line_R_coords_adj_json_15],
    [avg_line_R_coords_adj_txt,        avg_line_R_coords_adj_txt_6,        avg_line_R_coords_adj_txt_15],
    [avg_line_R_coords_jpg,            avg_line_R_coords_jpg_6,            avg_line_R_coords_jpg_15],
    [avg_line_R_coords_json,           avg_line_R_coords_json_6,           avg_line_R_coords_json_15],
    [avg_line_R_coords_tokenized_txt,  avg_line_R_coords_tokenized_txt_6,  avg_line_R_coords_tokenized_txt_15]
]

std_line_R_coords = [
    [sd_line_R_coords_adj_json,       sd_line_R_coords_adj_json_6,       sd_line_R_coords_adj_json_15],
    [sd_line_R_coords_adj_txt,        sd_line_R_coords_adj_txt_6,        sd_line_R_coords_adj_txt_15],
    [sd_line_R_coords_jpg,            sd_line_R_coords_jpg_6,            sd_line_R_coords_jpg_15],
    [sd_line_R_coords_json,           sd_line_R_coords_json_6,           sd_line_R_coords_json_15],
    [sd_line_R_coords_tokenized_txt,  sd_line_R_coords_tokenized_txt_6,  sd_line_R_coords_tokenized_txt_15]
]

error_line_R_coords = [
    [confidence_interval(line_R_coords_adj_json),       confidence_interval(line_R_coords_adj_json_6),       confidence_interval(line_R_coords_adj_json_15)],
    [confidence_interval(line_R_coords_adj_txt),        confidence_interval(line_R_coords_adj_txt_6),        confidence_interval(line_R_coords_adj_txt_15)],
    [confidence_interval(line_R_coords_jpg),            confidence_interval(line_R_coords_jpg_6),            confidence_interval(line_R_coords_jpg_15)],
    [confidence_interval(line_R_coords_json),           confidence_interval(line_R_coords_json_6),           confidence_interval(line_R_coords_json_15)],
    [confidence_interval(line_R_coords_tokenized_txt),  confidence_interval(line_R_coords_tokenized_txt_6),  confidence_interval(line_R_coords_tokenized_txt_15)]
]

labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data
means_occ_R_coords = [
    [avg_occupancy_R_coords_adj_json,       avg_occupancy_R_coords_adj_json_6,       avg_occupancy_R_coords_adj_json_15],
    [avg_occupancy_R_coords_adj_txt,        avg_occupancy_R_coords_adj_txt_6,        avg_occupancy_R_coords_adj_txt_15],
    [avg_occupancy_R_coords_ascii_txt,      avg_occupancy_R_coords_ascii_txt_6,      avg_occupancy_R_coords_ascii_txt_15],
    [avg_occupancy_R_coords_jpg,            avg_occupancy_R_coords_jpg_6,            avg_occupancy_R_coords_jpg_15],
    [avg_occupancy_R_coords_json,           avg_occupancy_R_coords_json_6,           avg_occupancy_R_coords_json_15],
    [avg_occupancy_R_coords_tokenized_txt,  avg_occupancy_R_coords_tokenized_txt_6,  avg_occupancy_R_coords_tokenized_txt_15]
]

std_occ_R_coords = [
    [sd_occupancy_R_coords_adj_json,       sd_occupancy_R_coords_adj_json_6,       sd_occupancy_R_coords_adj_json_15],
    [sd_occupancy_R_coords_adj_txt,        sd_occupancy_R_coords_adj_txt_6,        sd_occupancy_R_coords_adj_txt_15],
    [sd_occupancy_R_coords_jpg,            sd_occupancy_R_coords_jpg_6,            sd_occupancy_R_coords_jpg_15],
    [sd_occupancy_R_coords_json,           sd_occupancy_R_coords_json_6,           sd_occupancy_R_coords_json_15],
    [sd_occupancy_R_coords_tokenized_txt,  sd_occupancy_R_coords_tokenized_txt_6,  sd_occupancy_R_coords_tokenized_txt_15],
    [sd_occupancy_R_coords_ascii_txt,      sd_occupancy_R_coords_ascii_txt_6,      sd_occupancy_R_coords_ascii_txt_15]
]

error_occupancy_R_coords = [
    [confidence_interval(occupancy_R_coords_adj_json),       confidence_interval(occupancy_R_coords_adj_json_6),       confidence_interval(occupancy_R_coords_adj_json_15)],
    [confidence_interval(occupancy_R_coords_adj_txt),        confidence_interval(occupancy_R_coords_adj_txt_6),        confidence_interval(occupancy_R_coords_adj_txt_15)],
    [confidence_interval(occupancy_R_coords_jpg),            confidence_interval(occupancy_R_coords_jpg_6),            confidence_interval(occupancy_R_coords_jpg_15)],
    [confidence_interval(occupancy_R_coords_json),           confidence_interval(occupancy_R_coords_json_6),           confidence_interval(occupancy_R_coords_json_15)],
    [confidence_interval(occupancy_R_coords_tokenized_txt),  confidence_interval(occupancy_R_coords_tokenized_txt_6),  confidence_interval(occupancy_R_coords_tokenized_txt_15)],
    [ confidence_interval(occupancy_R_coords_ascii_txt),     confidence_interval(occupancy_R_coords_ascii_txt_6),      confidence_interval(occupancy_R_coords_ascii_txt_15)]
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized",
    "Occupancy ASCII"
]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02

# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line_R_coords, error_line_R_coords, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(std_line_R_coords[1]))
#     ax1.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel("Complexity")
# ax1.set_ylabel("Accuracy [%]")
# ax1.set_title("Mean Accuracy Per Complexity, Line Maze, Gemini 2.5 Pro, Coordinates Output")
# ax1.legend(loc='best')
# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Create bottom plot
# for means, stds, label in zip(means_occ_R_coords, error_occupancy_R_coords, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_occupancy_R_coords[1]))
#     ax2.errorbar(
#         x_vals + jitter, means, yerr=stds,
#         fmt='o-', capsize=5, label=label, alpha=0.9
#     )

# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_axis_occ)
# ax2.set_xlabel("Complexity")
# ax2.set_ylabel("Accuracy [%]")
# ax2.set_title("Mean Accuracy Per Complexity, Occupancy Maze, Gemini 2.5 Pro, Coordinates Output")
# ax2.legend(loc='best')
# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()


# R -- Allo -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Allo 3x3
line_R_allo_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_jpg = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 25.0, 100.0, 16.666666666666664, 100.0, 0.0])
line_R_allo_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 41.66666666666667, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_jpg = np.array([0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 25.0, 16.666666666666664, 0.0, 37.5])
occupancy_R_allo_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 3x3
avg_line_R_allo_adj_json = np.mean(line_R_allo_adj_json)
avg_line_R_allo_adj_txt = np.mean(line_R_allo_adj_txt)
avg_line_R_allo_jpg = np.mean(line_R_allo_jpg)
avg_line_R_allo_json = np.mean(line_R_allo_json)
avg_line_R_allo_tokenized_txt = np.mean(line_R_allo_tokenized_txt)
avg_occupancy_R_allo_adj_json = np.mean(occupancy_R_allo_adj_json)
avg_occupancy_R_allo_adj_txt = np.mean(occupancy_R_allo_adj_txt)
avg_occupancy_R_allo_ascii_txt = np.mean(occupancy_R_allo_ascii_txt)  
avg_occupancy_R_allo_jpg = np.mean(occupancy_R_allo_jpg)
avg_occupancy_R_allo_json = np.mean(occupancy_R_allo_json)
avg_occupancy_R_allo_tokenized_txt = np.mean(occupancy_R_allo_tokenized_txt)
sd_line_R_allo_adj_json = np.std(line_R_allo_adj_json)
sd_line_R_allo_adj_txt = np.std(line_R_allo_adj_txt)
sd_line_R_allo_jpg = np.std(line_R_allo_jpg)
sd_line_R_allo_json = np.std(line_R_allo_json)
sd_line_R_allo_tokenized_txt = np.std(line_R_allo_tokenized_txt)
sd_occupancy_R_allo_adj_json = np.std(occupancy_R_allo_adj_json)
sd_occupancy_R_allo_adj_txt = np.std(occupancy_R_allo_adj_txt)
sd_occupancy_R_allo_ascii_txt = np.std(occupancy_R_allo_ascii_txt)  
sd_occupancy_R_allo_jpg = np.std(occupancy_R_allo_jpg)
sd_occupancy_R_allo_json = np.std(occupancy_R_allo_json)
sd_occupancy_R_allo_tokenized_txt = np.std(occupancy_R_allo_tokenized_txt)
# Accuracy R Allo 6x6
line_R_allo_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_jpg_6 = np.array([6.25, 5.555555555555555, 0.0, 0.0, 28.57142857142857, 15.0, 4.166666666666666, 0.0, 18.75, 0.0])
line_R_allo_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_ascii_txt_6 = np.array([6.25, 0.0, 0.0, 25.0, 14.285714285714285, 55.00000000000001, 12.5, 35.0, 25.0, 10.0])
occupancy_R_allo_jpg_6 = np.array([18.75, 5.555555555555555, 4.411764705882353, 14.285714285714285, 7.142857142857142, 5.0, 4.166666666666666, 0.0, 9.375, 5.0])
occupancy_R_allo_json_6 = np.array([56.25, 100.0, 100.0, 7.142857142857142, 100.0, 100.0, 100.0, 100.0, 100.0, 37.5])
occupancy_R_allo_tokenized_txt_6 = np.array([100.0, 100.0, 51.470588235294116, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 6x6
avg_line_R_allo_adj_json_6 = np.mean(line_R_allo_adj_json_6)
avg_line_R_allo_adj_txt_6 = np.mean(line_R_allo_adj_txt_6)
avg_line_R_allo_jpg_6 = np.mean(line_R_allo_jpg_6)
avg_line_R_allo_json_6 = np.mean(line_R_allo_json_6)
avg_line_R_allo_tokenized_txt_6 = np.mean(line_R_allo_tokenized_txt_6)
avg_occupancy_R_allo_adj_json_6 = np.mean(occupancy_R_allo_adj_json_6)
avg_occupancy_R_allo_adj_txt_6 = np.mean(occupancy_R_allo_adj_txt_6)
avg_occupancy_R_allo_ascii_txt_6 = np.mean(occupancy_R_allo_ascii_txt_6)  
avg_occupancy_R_allo_jpg_6 = np.mean(occupancy_R_allo_jpg_6)
avg_occupancy_R_allo_json_6 = np.mean(occupancy_R_allo_json_6)
avg_occupancy_R_allo_tokenized_txt_6 = np.mean(occupancy_R_allo_tokenized_txt_6)
sd_line_R_allo_adj_json_6 = np.std(line_R_allo_adj_json_6)
sd_line_R_allo_adj_txt_6 = np.std(line_R_allo_adj_txt_6)
sd_line_R_allo_jpg_6 = np.std(line_R_allo_jpg_6)
sd_line_R_allo_json_6 = np.std(line_R_allo_json_6)
sd_line_R_allo_tokenized_txt_6 = np.std(line_R_allo_tokenized_txt_6)
sd_occupancy_R_allo_adj_json_6 = np.std(occupancy_R_allo_adj_json_6)
sd_occupancy_R_allo_adj_txt_6 = np.std(occupancy_R_allo_adj_txt_6)
sd_occupancy_R_allo_ascii_txt_6 = np.std(occupancy_R_allo_ascii_txt_6)  
sd_occupancy_R_allo_jpg_6 = np.std(occupancy_R_allo_jpg_6)
sd_occupancy_R_allo_json_6 = np.std(occupancy_R_allo_json_6)
sd_occupancy_R_allo_tokenized_txt_6 = np.std(occupancy_R_allo_tokenized_txt_6)
# Accuracy R Allo 15x15
line_R_allo_adj_json_15 = np.array([46.92307692307692, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt_15 = np.array([7.6923076923076925, 100.0, 53.62318840579711, 100.0, 0.7936507936507936, 98.0, 100.0, 2.564102564102564, 58.333333333333336, 100.0])
line_R_allo_jpg_15 = np.array([0.7692307692307693, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_R_allo_json_15 = np.array([27.692307692307693, 14.705882352941178, 10.144927536231885, 12.5, 9.523809523809524, 26.0, 19.696969696969695, 29.48717948717949, 1.5151515151515151, 32.608695652173914])
line_R_allo_tokenized_txt_15 = np.array([33.07692307692307, 39.705882352941174, 7.971014492753622, 5.357142857142857, 39.682539682539684, 100.0, 100.0, 50.0, 60.60606060606061, 100.0])
occupancy_R_allo_adj_json_15 = np.array([46.15384615384615, 100.0, 38.405797101449274, 100.0, 34.523809523809526, 100.0, 100.0, 100.0, 71.21212121212122, 100.0])
occupancy_R_allo_adj_txt_15 = np.array([27.692307692307693, 100.0, 7.246376811594203, 14.285714285714285, 9.126984126984127, 77.0, 25.757575757575758, 67.94871794871796, 39.39393939393939, 100.0])
occupancy_R_allo_ascii_txt_15 = np.array([1.5384615384615385, 5.88235294117647, 0.0, 0.0, 0.0, 0.0, 3.0303030303030303, 1.282051282051282, 1.5151515151515151, 0.0])
occupancy_R_allo_jpg_15 = np.array([1.153846153846154, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_R_allo_json_15 = np.array([0.38461538461538464, 27.941176470588236, 5.797101449275362, 39.285714285714285, 3.1746031746031744, 7.000000000000001, 3.0303030303030303, 0.0, 3.0303030303030303, 7.608695652173914])
occupancy_R_allo_tokenized_txt_15 = np.array([25.384615384615383, 100.0, 4.3478260869565215, 100.0, 50.79365079365079, 10.0, 18.181818181818183, 61.53846153846154, 0.7575757575757576, 100.0])
# Averages and std deviation 15x15
avg_line_R_allo_adj_json_15 = np.mean(line_R_allo_adj_json_15)
avg_line_R_allo_adj_txt_15 = np.mean(line_R_allo_adj_txt_15)
avg_line_R_allo_jpg_15 = np.mean(line_R_allo_jpg_15)
avg_line_R_allo_json_15 = np.mean(line_R_allo_json_15)
avg_line_R_allo_tokenized_txt_15 = np.mean(line_R_allo_tokenized_txt_15)
avg_occupancy_R_allo_adj_json_15 = np.mean(occupancy_R_allo_adj_json_15)
avg_occupancy_R_allo_adj_txt_15 = np.mean(occupancy_R_allo_adj_txt_15)
avg_occupancy_R_allo_ascii_txt_15 = np.mean(occupancy_R_allo_ascii_txt_15)  
avg_occupancy_R_allo_jpg_15 = np.mean(occupancy_R_allo_jpg_15)
avg_occupancy_R_allo_json_15 = np.mean(occupancy_R_allo_json_15)
avg_occupancy_R_allo_tokenized_txt_15 = np.mean(occupancy_R_allo_tokenized_txt_15)
sd_line_R_allo_adj_json_15 = np.std(line_R_allo_adj_json_15)
sd_line_R_allo_adj_txt_15 = np.std(line_R_allo_adj_txt_15)
sd_line_R_allo_jpg_15 = np.std(line_R_allo_jpg_15)
sd_line_R_allo_json_15 = np.std(line_R_allo_json_15)
sd_line_R_allo_tokenized_txt_15 = np.std(line_R_allo_tokenized_txt_15)
sd_occupancy_R_allo_adj_json_15 = np.std(occupancy_R_allo_adj_json_15)
sd_occupancy_R_allo_adj_txt_15 = np.std(occupancy_R_allo_adj_txt_15)
sd_occupancy_R_allo_ascii_txt_15 = np.std(occupancy_R_allo_ascii_txt_15)  
sd_occupancy_R_allo_jpg_15 = np.std(occupancy_R_allo_jpg_15)
sd_occupancy_R_allo_json_15 = np.std(occupancy_R_allo_json_15)
sd_occupancy_R_allo_tokenized_txt_15 = np.std(occupancy_R_allo_tokenized_txt_15)

# Top plot data
means_line_R_allo = [
    [avg_line_R_allo_adj_json,       avg_line_R_allo_adj_json_6,       avg_line_R_allo_adj_json_15],
    [avg_line_R_allo_adj_txt,        avg_line_R_allo_adj_txt_6,        avg_line_R_allo_adj_txt_15],
    [avg_line_R_allo_jpg,            avg_line_R_allo_jpg_6,            avg_line_R_allo_jpg_15],
    [avg_line_R_allo_json,           avg_line_R_allo_json_6,           avg_line_R_allo_json_15],
    [avg_line_R_allo_tokenized_txt,  avg_line_R_allo_tokenized_txt_6,  avg_line_R_allo_tokenized_txt_15]
]

std_line_R_allo = [
    [sd_line_R_allo_adj_json,       sd_line_R_allo_adj_json_6,       sd_line_R_allo_adj_json_15],
    [sd_line_R_allo_adj_txt,        sd_line_R_allo_adj_txt_6,        sd_line_R_allo_adj_txt_15],
    [sd_line_R_allo_jpg,            sd_line_R_allo_jpg_6,            sd_line_R_allo_jpg_15],
    [sd_line_R_allo_json,           sd_line_R_allo_json_6,           sd_line_R_allo_json_15],
    [sd_line_R_allo_tokenized_txt,  sd_line_R_allo_tokenized_txt_6,  sd_line_R_allo_tokenized_txt_15]
]

error_line_R_allo = [
    [confidence_interval(line_R_allo_adj_json),       confidence_interval(line_R_allo_adj_json_6),       confidence_interval(line_R_allo_adj_json_15)],
    [confidence_interval(line_R_allo_adj_txt),        confidence_interval(line_R_allo_adj_txt_6),        confidence_interval(line_R_allo_adj_txt_15)],
    [confidence_interval(line_R_allo_jpg),            confidence_interval(line_R_allo_jpg_6),            confidence_interval(line_R_allo_jpg_15)],
    [confidence_interval(line_R_allo_json),           confidence_interval(line_R_allo_json_6),           confidence_interval(line_R_allo_json_15)],
    [confidence_interval(line_R_allo_tokenized_txt),  confidence_interval(line_R_allo_tokenized_txt_6),  confidence_interval(line_R_allo_tokenized_txt_15)]
]

labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data
means_occ_R_allo = [
    [avg_occupancy_R_allo_adj_json,       avg_occupancy_R_allo_adj_json_6,       avg_occupancy_R_allo_adj_json_15],
    [avg_occupancy_R_allo_adj_txt,        avg_occupancy_R_allo_adj_txt_6,        avg_occupancy_R_allo_adj_txt_15],
    [avg_occupancy_R_allo_ascii_txt,      avg_occupancy_R_allo_ascii_txt_6,      avg_occupancy_R_allo_ascii_txt_15],
    [avg_occupancy_R_allo_jpg,            avg_occupancy_R_allo_jpg_6,            avg_occupancy_R_allo_jpg_15],
    [avg_occupancy_R_allo_json,           avg_occupancy_R_allo_json_6,           avg_occupancy_R_allo_json_15],
    [avg_occupancy_R_allo_tokenized_txt,  avg_occupancy_R_allo_tokenized_txt_6,  avg_occupancy_R_allo_tokenized_txt_15]
]

std_occ_R_allo = [
    [sd_occupancy_R_allo_adj_json,       sd_occupancy_R_allo_adj_json_6,       sd_occupancy_R_allo_adj_json_15],
    [sd_occupancy_R_allo_adj_txt,        sd_occupancy_R_allo_adj_txt_6,        sd_occupancy_R_allo_adj_txt_15],
    [sd_occupancy_R_allo_jpg,            sd_occupancy_R_allo_jpg_6,            sd_occupancy_R_allo_jpg_15],
    [sd_occupancy_R_allo_json,           sd_occupancy_R_allo_json_6,           sd_occupancy_R_allo_json_15],
    [sd_occupancy_R_allo_tokenized_txt,  sd_occupancy_R_allo_tokenized_txt_6,  sd_occupancy_R_allo_tokenized_txt_15],
    [sd_occupancy_R_allo_ascii_txt,      sd_occupancy_R_allo_ascii_txt_6,      sd_occupancy_R_allo_ascii_txt_15]
]

error_occupancy_R_allo = [
    [confidence_interval(occupancy_R_allo_adj_json),       confidence_interval(occupancy_R_allo_adj_json_6),       confidence_interval(occupancy_R_allo_adj_json_15)],
    [confidence_interval(occupancy_R_allo_adj_txt),        confidence_interval(occupancy_R_allo_adj_txt_6),        confidence_interval(occupancy_R_allo_adj_txt_15)],
    [confidence_interval(occupancy_R_allo_jpg),            confidence_interval(occupancy_R_allo_jpg_6),            confidence_interval(occupancy_R_allo_jpg_15)],
    [confidence_interval(occupancy_R_allo_json),           confidence_interval(occupancy_R_allo_json_6),           confidence_interval(occupancy_R_allo_json_15)],
    [confidence_interval(occupancy_R_allo_tokenized_txt),  confidence_interval(occupancy_R_allo_tokenized_txt_6),  confidence_interval(occupancy_R_allo_tokenized_txt_15)],
    [ confidence_interval(occupancy_R_allo_ascii_txt),     confidence_interval(occupancy_R_allo_ascii_txt_6),      confidence_interval(occupancy_R_allo_ascii_txt_15)]
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized",
    "Occupancy ASCII"
]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02

# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line_R_allo, error_line_R_allo, labels_line):
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
# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Create bottom plot
# for means, stds, label in zip(means_occ_R_allo, error_occupancy_R_allo, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_occupancy_R_allo[1]))
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
# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()

# R -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Ego 3x3
line_R_ego_adj_json = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_adj_txt = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_jpg = np.array([25.0, 0.0, 50.0, 50.0, 33.33333333333333, 0.0, 0.0, 100.0, 16.666666666666664, 110.00000000000001])
line_R_ego_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 100.0, 100.0, 75.0])
occupancy_R_ego_jpg = np.array([12.5, 0.0, 0.0, 50.0, 33.33333333333333, 0.0, 12.5, 91.66666666666666, 8.333333333333332, 37.5])
occupancy_R_ego_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 3x3
avg_line_R_ego_adj_json = np.mean(line_R_ego_adj_json)
avg_line_R_ego_adj_txt = np.mean(line_R_ego_adj_txt)
avg_line_R_ego_jpg = np.mean(line_R_ego_jpg)
avg_line_R_ego_json = np.mean(line_R_ego_json)
avg_line_R_ego_tokenized_txt = np.mean(line_R_ego_tokenized_txt)
avg_occupancy_R_ego_adj_json = np.mean(occupancy_R_ego_adj_json)
avg_occupancy_R_ego_adj_txt = np.mean(occupancy_R_ego_adj_txt)
avg_occupancy_R_ego_ascii_txt = np.mean(occupancy_R_ego_ascii_txt)  
avg_occupancy_R_ego_jpg = np.mean(occupancy_R_ego_jpg)
avg_occupancy_R_ego_json = np.mean(occupancy_R_ego_json)
avg_occupancy_R_ego_tokenized_txt = np.mean(occupancy_R_ego_tokenized_txt)
sd_line_R_ego_adj_json = np.std(line_R_ego_adj_json)
sd_line_R_ego_adj_txt = np.std(line_R_ego_adj_txt)
sd_line_R_ego_jpg = np.std(line_R_ego_jpg)
sd_line_R_ego_json = np.std(line_R_ego_json)
sd_line_R_ego_tokenized_txt = np.std(line_R_ego_tokenized_txt)
sd_occupancy_R_ego_adj_json = np.std(occupancy_R_ego_adj_json)
sd_occupancy_R_ego_adj_txt = np.std(occupancy_R_ego_adj_txt)
sd_occupancy_R_ego_ascii_txt = np.std(occupancy_R_ego_ascii_txt)  
sd_occupancy_R_ego_jpg = np.std(occupancy_R_ego_jpg)
sd_occupancy_R_ego_json = np.std(occupancy_R_ego_json)
sd_occupancy_R_ego_tokenized_txt = np.std(occupancy_R_ego_tokenized_txt)
# Accuracy R Ego 6x6
line_R_ego_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_adj_txt_6 = np.array([100.0, 5.555555555555555, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_jpg_6 = np.array([12.5, 11.11111111111111, 0.0, 0.0, 21.428571428571427, 0.0, 4.166666666666666, 0.0, 31.25, 0.0])
line_R_ego_json_6 = np.array([100.0, 16.666666666666664, 100.0, 100.0, 100.0, 100.0, 83.33333333333334, 100.0, 6.25, 100.0])
line_R_ego_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_json_6 = np.array([100.0, 100.0, 110.00000000000001, 100.0, 100.0, 100.0, 100.0, 0.0, 100.0, 100.0])
occupancy_R_ego_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_ascii_txt_6 = np.array([12.5, 33.33333333333333, 0.0, 17.857142857142858, 28.57142857142857, 5.0, 10.416666666666668, 35.0, 0.0, 10.0])
occupancy_R_ego_jpg_6 = np.array([6.25, 16.666666666666664, 5.88235294117647, 0.0, 21.428571428571427, 2.5, 12.5, 50.0, 12.5, 0.0])
occupancy_R_ego_json_6 = np.array([100.0, 100.0, 8.823529411764707, 17.857142857142858, 100.0, 90.0, 100.0, 100.0, 56.25, 10.0])
occupancy_R_ego_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 29.166666666666668, 100.0, 100.0, 100.0])
# Averages and std deviation 6x6
avg_line_R_ego_adj_json_6 = np.mean(line_R_ego_adj_json_6)
avg_line_R_ego_adj_txt_6 = np.mean(line_R_ego_adj_txt_6)
avg_line_R_ego_jpg_6 = np.mean(line_R_ego_jpg_6)
avg_line_R_ego_json_6 = np.mean(line_R_ego_json_6)
avg_line_R_ego_tokenized_txt_6 = np.mean(line_R_ego_tokenized_txt_6)
avg_occupancy_R_ego_adj_json_6 = np.mean(occupancy_R_ego_adj_json_6)
avg_occupancy_R_ego_adj_txt_6 = np.mean(occupancy_R_ego_adj_txt_6)
avg_occupancy_R_ego_ascii_txt_6 = np.mean(occupancy_R_ego_ascii_txt_6)  
avg_occupancy_R_ego_jpg_6 = np.mean(occupancy_R_ego_jpg_6)
avg_occupancy_R_ego_json_6 = np.mean(occupancy_R_ego_json_6)
avg_occupancy_R_ego_tokenized_txt_6 = np.mean(occupancy_R_ego_tokenized_txt_6)
sd_line_R_ego_adj_json_6 = np.std(line_R_ego_adj_json_6)
sd_line_R_ego_adj_txt_6 = np.std(line_R_ego_adj_txt_6)
sd_line_R_ego_jpg_6 = np.std(line_R_ego_jpg_6)
sd_line_R_ego_json_6 = np.std(line_R_ego_json_6)
sd_line_R_ego_tokenized_txt_6 = np.std(line_R_ego_tokenized_txt_6)
sd_occupancy_R_ego_adj_json_6 = np.std(occupancy_R_ego_adj_json_6)
sd_occupancy_R_ego_adj_txt_6 = np.std(occupancy_R_ego_adj_txt_6)
sd_occupancy_R_ego_ascii_txt_6 = np.std(occupancy_R_ego_ascii_txt_6)  
sd_occupancy_R_ego_jpg_6 = np.std(occupancy_R_ego_jpg_6)
sd_occupancy_R_ego_json_6 = np.std(occupancy_R_ego_json_6)
sd_occupancy_R_ego_tokenized_txt_6 = np.std(occupancy_R_ego_tokenized_txt_6)
# Accuracy R Ego 15x15
line_R_ego_adj_json_15 = np.array([3.076923076923077, 100.0, 15.217391304347828, 100.0, 35.714285714285715, 100.0, 100.0, 100.0, 62.121212121212125, 100.0])
line_R_ego_adj_txt_15 = np.array([2.307692307692308, 20.588235294117645, 0.7246376811594203, 100.0, 0.0, 11.0, 0.0, 0.0, 46.21212121212121, 0.0])
line_R_ego_jpg_15 = np.array([0.7692307692307693, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5151515151515151, 0.0])
line_R_ego_json_15 = np.array([3.076923076923077, 36.76470588235294, 9.420289855072465, 0.0, 14.285714285714285, 26.0, 18.181818181818183, 7.6923076923076925, 7.575757575757576, 30.434782608695656])
line_R_ego_tokenized_txt_15 = np.array([1.5384615384615385, 29.411764705882355, 1.4492753623188406, 100.0, 0.0, 0.0, 100.0, 100.0, 0.7575757575757576, 100.0])
occupancy_R_ego_adj_json_15 = np.array([34.23076923076923, 38.23529411764706, 10.869565217391305, 100.0, 0.0, 36.0, 65.15151515151516, 50.0, 0.7575757575757576, 100.0])
occupancy_R_ego_adj_txt_15 = np.array([1.5384615384615385, 41.17647058823529, 13.768115942028986, 0.0, 0.0, 0.0, 26.515151515151516, 100.0, 5.303030303030303, 14.130434782608695])
occupancy_R_ego_ascii_txt_15 = np.array([0.7692307692307693, 6.61764705882353, 0.36231884057971014, 4.464285714285714, 3.1746031746031744, 5.5, 0.0, 0.0, 0.3787878787878788, 4.3478260869565215])
occupancy_R_ego_jpg_15 = np.array([1.5384615384615385, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_R_ego_json_15 = np.array([3.8461538461538463, 5.88235294117647, 2.1739130434782608, 10.714285714285714, 15.873015873015872, 0.0, 10.606060606060606, 6.41025641025641, 1.5151515151515151, 10.869565217391305])
occupancy_R_ego_tokenized_txt_15 = np.array([27.307692307692307, 48.529411764705884, 5.797101449275362, 0.0, 2.380952380952381, 3.5000000000000004, 39.39393939393939, 23.076923076923077, 6.0606060606060606, 15.217391304347828])
# Averages and std deviation 15x15
avg_line_R_ego_adj_json_15 = np.mean(line_R_ego_adj_json_15)
avg_line_R_ego_adj_txt_15 = np.mean(line_R_ego_adj_txt_15)
avg_line_R_ego_jpg_15 = np.mean(line_R_ego_jpg_15)
avg_line_R_ego_json_15 = np.mean(line_R_ego_json_15)
avg_line_R_ego_tokenized_txt_15 = np.mean(line_R_ego_tokenized_txt_15)
avg_occupancy_R_ego_adj_json_15 = np.mean(occupancy_R_ego_adj_json_15)
avg_occupancy_R_ego_adj_txt_15 = np.mean(occupancy_R_ego_adj_txt_15)
avg_occupancy_R_ego_ascii_txt_15 = np.mean(occupancy_R_ego_ascii_txt_15)  
avg_occupancy_R_ego_jpg_15 = np.mean(occupancy_R_ego_jpg_15)
avg_occupancy_R_ego_json_15 = np.mean(occupancy_R_ego_json_15)
avg_occupancy_R_ego_tokenized_txt_15 = np.mean(occupancy_R_ego_tokenized_txt_15)
sd_line_R_ego_adj_json_15 = np.std(line_R_ego_adj_json_15)
sd_line_R_ego_adj_txt_15 = np.std(line_R_ego_adj_txt_15)
sd_line_R_ego_jpg_15 = np.std(line_R_ego_jpg_15)
sd_line_R_ego_json_15 = np.std(line_R_ego_json_15)
sd_line_R_ego_tokenized_txt_15 = np.std(line_R_ego_tokenized_txt_15)
sd_occupancy_R_ego_adj_json_15 = np.std(occupancy_R_ego_adj_json_15)
sd_occupancy_R_ego_adj_txt_15 = np.std(occupancy_R_ego_adj_txt_15)
sd_occupancy_R_ego_ascii_txt_15 = np.std(occupancy_R_ego_ascii_txt_15)  
sd_occupancy_R_ego_jpg_15 = np.std(occupancy_R_ego_jpg_15)
sd_occupancy_R_ego_json_15 = np.std(occupancy_R_ego_json_15)
sd_occupancy_R_ego_tokenized_txt_15 = np.std(occupancy_R_ego_tokenized_txt_15)

# Top plot data
means_line_R_ego = [
    [avg_line_R_ego_adj_json,       avg_line_R_ego_adj_json_6,       avg_line_R_ego_adj_json_15],
    [avg_line_R_ego_adj_txt,        avg_line_R_ego_adj_txt_6,        avg_line_R_ego_adj_txt_15],
    [avg_line_R_ego_jpg,            avg_line_R_ego_jpg_6,            avg_line_R_ego_jpg_15],
    [avg_line_R_ego_json,           avg_line_R_ego_json_6,           avg_line_R_ego_json_15],
    [avg_line_R_ego_tokenized_txt,  avg_line_R_ego_tokenized_txt_6,  avg_line_R_ego_tokenized_txt_15]
]

std_line_R_ego = [
    [sd_line_R_ego_adj_json,       sd_line_R_ego_adj_json_6,       sd_line_R_ego_adj_json_15],
    [sd_line_R_ego_adj_txt,        sd_line_R_ego_adj_txt_6,        sd_line_R_ego_adj_txt_15],
    [sd_line_R_ego_jpg,            sd_line_R_ego_jpg_6,            sd_line_R_ego_jpg_15],
    [sd_line_R_ego_json,           sd_line_R_ego_json_6,           sd_line_R_ego_json_15],
    [sd_line_R_ego_tokenized_txt,  sd_line_R_ego_tokenized_txt_6,  sd_line_R_ego_tokenized_txt_15]
]
error_line_R_ego = [
    [confidence_interval(line_R_ego_adj_json),       confidence_interval(line_R_ego_adj_json_6),       confidence_interval(line_R_ego_adj_json_15)],
    [confidence_interval(line_R_ego_adj_txt),        confidence_interval(line_R_ego_adj_txt_6),        confidence_interval(line_R_ego_adj_txt_15)],
    [confidence_interval(line_R_ego_jpg),            confidence_interval(line_R_ego_jpg_6),            confidence_interval(line_R_ego_jpg_15)],
    [confidence_interval(line_R_ego_json),           confidence_interval(line_R_ego_json_6),           confidence_interval(line_R_ego_json_15)],
    [confidence_interval(line_R_ego_tokenized_txt),  confidence_interval(line_R_ego_tokenized_txt_6),  confidence_interval(line_R_ego_tokenized_txt_15)]
]

labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data
means_occ_R_ego = [
    [avg_occupancy_R_ego_adj_json,       avg_occupancy_R_ego_adj_json_6,       avg_occupancy_R_ego_adj_json_15],
    [avg_occupancy_R_ego_adj_txt,        avg_occupancy_R_ego_adj_txt_6,        avg_occupancy_R_ego_adj_txt_15],
    [avg_occupancy_R_ego_ascii_txt,      avg_occupancy_R_ego_ascii_txt_6,      avg_occupancy_R_ego_ascii_txt_15],
    [avg_occupancy_R_ego_jpg,            avg_occupancy_R_ego_jpg_6,            avg_occupancy_R_ego_jpg_15],
    [avg_occupancy_R_ego_json,           avg_occupancy_R_ego_json_6,           avg_occupancy_R_ego_json_15],
    [avg_occupancy_R_ego_tokenized_txt,  avg_occupancy_R_ego_tokenized_txt_6,  avg_occupancy_R_ego_tokenized_txt_15]
]

std_occ_R_ego = [
    [sd_occupancy_R_ego_adj_json,       sd_occupancy_R_ego_adj_json_6,      sd_occupancy_R_ego_adj_json_15],
    [sd_occupancy_R_ego_adj_txt,        sd_occupancy_R_ego_adj_txt_6,        sd_occupancy_R_ego_adj_txt_15],
    [sd_occupancy_R_ego_jpg,            sd_occupancy_R_ego_jpg_6,            sd_occupancy_R_ego_jpg_15],
    [sd_occupancy_R_ego_json,           sd_occupancy_R_ego_json_6,           sd_occupancy_R_ego_json_15],
    [sd_occupancy_R_ego_tokenized_txt,  sd_occupancy_R_ego_tokenized_txt_6,  sd_occupancy_R_ego_tokenized_txt_15],
    [sd_occupancy_R_ego_ascii_txt,      sd_occupancy_R_ego_ascii_txt_6,      sd_occupancy_R_ego_ascii_txt_15]
]

error_occupancy_R_ego = [
    [confidence_interval(occupancy_R_ego_adj_json),       confidence_interval(occupancy_R_ego_adj_json_6),       confidence_interval(occupancy_R_ego_adj_json_15)],
    [confidence_interval(occupancy_R_ego_adj_txt),        confidence_interval(occupancy_R_ego_adj_txt_6),        confidence_interval(occupancy_R_ego_adj_txt_15)],
    [confidence_interval(occupancy_R_ego_jpg),            confidence_interval(occupancy_R_ego_jpg_6),            confidence_interval(occupancy_R_ego_jpg_15)],
    [confidence_interval(occupancy_R_ego_json),           confidence_interval(occupancy_R_ego_json_6),           confidence_interval(occupancy_R_ego_json_15)],
    [confidence_interval(occupancy_R_ego_tokenized_txt),  confidence_interval(occupancy_R_ego_tokenized_txt_6),  confidence_interval(occupancy_R_ego_tokenized_txt_15)],
    [ confidence_interval(occupancy_R_ego_ascii_txt),     confidence_interval(occupancy_R_ego_ascii_txt_6),      confidence_interval(occupancy_R_ego_ascii_txt_15)]
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized",
    "Occupancy ASCII"
]

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02

# # Create figure
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(12, 10), sharex=False
# )

# # Create top plot
# for means, stds, label in zip(means_line_R_ego, error_line_R_ego, labels_line):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_line_R_ego[1]))
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
# ax1.grid(axis='y', linestyle='--', alpha=0.8)

# # Create bottom plot
# for means, stds, label in zip(means_occ_R_ego, error_occupancy_R_ego, labels_occ):
#     jitter = np.random.uniform(-jitter_strength, jitter_strength, size=len(error_occupancy_R_ego[1]))
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
# ax2.grid(axis='y', linestyle='--', alpha=0.8)

# plt.tight_layout()
# plt.show()


# subplot_groups = [
#     means_line_R_coords,  # top-left  (methods x 3)
#     means_line_R_allo,    # top-middle
#     means_line_R_ego,     # top-right
#     means_occ_R_coords,   # bottom-left
#     means_occ_R_allo,     # bottom-middle
#     means_occ_R_ego       # bottom-right
# ]

# subplot_errors = [
#     error_line_R_coords,  # same indexing as subplot_groups
#     error_line_R_allo,
#     error_line_R_ego,
#     error_occupancy_R_coords,
#     error_occupancy_R_allo,
#     error_occupancy_R_ego
# ]


# # Plot shared figure of all 6 accuracies

# x_vals = np.arange(3)   # positions [0,1,2]
# jitter_strength = 0.02
# # Create figure
# fig, axes = plt.subplots(
#     nrows=2, ncols=3, figsize=(18, 10), sharey=True, sharex = True
# )

# titles = [
#     "Average Accuracy Per Complexity, \n Line Maze, Coordinates Output",
#     "Average Accuracy Per Complexity, \n Line Maze, Allocentric Output",
#     "Average Accuracy Per Complexity, \n Line Maze, Egocentric Output",
#     "Average Accuracy Per Complexity, \n Occupancy, Coordinates Output",
#     "Average Accuracy Per Complexity, \n Occupancy, Allocentric Output",
#     "Average Accuracy Per Complexity, \n Occupancy, Egocentric Output",
# ]
# groups = []
# errs = []

# for i, (g, e) in enumerate(zip(subplot_groups, subplot_errors)):
#     ga = np.asarray(g)
#     ea = np.asarray(e)

#     # Accept either shape (n_methods, 3) OR a list-of-lists with same shape
#     if ga.ndim != 2 or ea.ndim != 2:
#         raise ValueError(f"subplot index {i}: each group/error must be 2D arrays. got shapes: group {ga.shape}, error {ea.shape}")

#     if ga.shape[1] != 3 or ea.shape[1] != 3:
#         raise ValueError(f"subplot index {i}: second dimension must be 3 (three complexities). got: group {ga.shape}, error {ea.shape}")

#     if ga.shape[0] != ea.shape[0]:
#         raise ValueError(f"subplot index {i}: number of methods (rows) must match between group and error. got: {ga.shape[0]} vs {ea.shape[0]}")

#     groups.append(ga)
#     errs.append(ea)

# print("All group/error shapes OK:", [g.shape for g in groups])


# # Plotting: 2x3 grid
# fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8), sharey=True)

# jitter_strength = 0.02

# for idx, ax in enumerate(axes.flat):
#     group = groups[idx]   # shape (n_methods, 3)
#     err   = errs[idx]     # shape (n_methods, 3)
#     n_methods = group.shape[0]

#     # choose label set and xtick labels
#     if n_methods == len(labels_line):
#         method_labels = labels_line
#         x_tick_lbls = x_axis_line
#     elif n_methods == len(labels_occ):
#         method_labels = labels_occ
#         x_tick_lbls = x_axis_occ
#     else:
#         # fallback: auto-generate labels
#         method_labels = [f"Method {i}" for i in range(n_methods)]
#         x_tick_lbls = x_axis_line  # default
#     # jitter: one scalar per method
#     jitter = np.linspace(-jitter_strength, jitter_strength, n_methods)

#     # Plot each method row-by-row
#     for m in range(n_methods):
#         y = group[m]        # shape (3,)
#         yerr = err[m]       # shape (3,)
#         x_shifted = x_vals + jitter[m]  # scalar shift per-method

#         # final safety check
#         if x_shifted.shape[0] != y.shape[0]:
#             raise ValueError(f"subplot {idx} method {m}: x and y lengths mismatch: {x_shifted.shape} vs {y.shape}")

#         ax.errorbar(
#             x_shifted,
#             y,
#             yerr=yerr,
#             fmt='o-',
#             capsize=5,
#             label=method_labels[m],
#             alpha=0.9
#         )

#     # Formatting
#     ax.set_title(titles[idx])
#     ax.set_xticks(x_vals)
#     ax.set_xticklabels(x_tick_lbls)
#     ax.grid(axis='y', linestyle='--', alpha=0.8)

#     # Only left column gets y-axis label
#     if idx % 3 == 0:
#         ax.set_ylabel("Accuracy [%]")

#     ax.set_xlabel("Maze Complexity")
#     ax.legend(loc='best', fontsize='small')

# plt.tight_layout()
# plt.show()



# 1. Define the Legend Labels
single_legend = [
    'Adjacency Json - Gemini 2.5 Flash Lite', 
    'Adjacency Text - Gemini 2.5 Flash Lite', 
    'JPG - Gemini 2.5 Flash Lite', 
    'JSON - Gemini 2.5 Flash Lite', 
    'Tokenized - Gemini 2.5 Flash Lite', 
    'ASCII - Gemini 2.5 Flash Lite', 
    'Adjacency Json - Gemini 2.5 Pro', 
    'Adjacency Text - Gemini 2.5 Pro', 
    'JPG - Gemini 2.5 Pro', 
    'JSON - Gemini 2.5 Pro', 
    'Tokenized - Gemini 2.5 Pro', 
    'ASCII - Gemini 2.5 Pro'
]

# 2. Organize Data into Groups for the 6 Subplots
# Structure: (Means_NR, Means_R, Err_NR, Err_R, Title)
# NR = Non-Reasoning (Solid), R = Reasoning (Dotted)
plot_configs = [
    # Top-Left
    (means_line_NR_coords, means_line_R_coords, 
     error_line_NR_coords, error_line_R_coords, 
     "Accuracy Per Complexity, \n Line Maze, Coordinates Output"),
    
    # Top-Middle
    (means_line_NR_allo, means_line_R_allo, 
     error_line_NR_allo, error_line_R_allo, 
     "Accuracy Per Complexity, \n Line Maze, Allocentric Output"),
    
    # Top-Right
    (means_line_NR_ego, means_line_R_ego, 
     error_line_NR_ego, error_line_R_ego, 
     "Accuracy Per Complexity, \n Line Maze, Egocentric Output"),
    
    # Bottom-Left
    (means_occ_NR_coords, means_occ_R_coords, 
     error_occupancy_NR_coords, error_occupancy_R_coords, 
     "Accuracy Per Complexity, \n Occupancy Maze, Coordinates Output"),
    
    # Bottom-Middle
    (means_occ_NR_allo, means_occ_R_allo, 
     error_occupancy_NR_allo, error_occupancy_R_allo, 
     "Accuracy Per Complexity, \n Occupancy Maze, Allocentric Output"),
    
    # Bottom-Right
    (means_occ_NR_ego, means_occ_R_ego, 
     error_occupancy_NR_ego, error_occupancy_R_ego, 
     "Accuracy Per Complexity, \n Occupancy Maze, Egocentric Output"),
]

# 3. Setup Plotting Parameters
x_vals = np.arange(3)
x_tick_lbls_line = ["3x3", "6x6", "15x15"] # Assuming complexity levels
x_tick_lbls_occupancy = ["7x7", "13x13", "31x31"] # Assuming complexity levels
# Define a color palette for the 6 distinct methods (ignoring model version)
# We have 6 base methods (Adj Json, Adj Text, JPG, JSON, Tok, ASCII)
colors = plt.cm.tab10(np.linspace(0, 1, 10))[:6] 

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(9, 8), sharey=True, sharex=False)

# Container to grab handles/labels for the global legend later
handles_for_legend = []
labels_for_legend = []

# 4. Main Plotting Loop
for idx, ax in enumerate(axes.flat):
    means_nr, means_r, err_nr, err_r, title = plot_configs[idx]
    
    # Convert to numpy arrays just in case
    means_nr = np.array(means_nr)
    means_r = np.array(means_r)
    err_nr = np.array(err_nr)
    err_r = np.array(err_r)

    # Determine number of lines (5 for top row, 6 for bottom row)
    n_rows = means_nr.shape[0] 
    
    # Calculate jitter
    # We have n_rows * 2 lines (NR + R). We spread them slightly around x.
    total_lines = n_rows * 2
    jitter_arr = np.linspace(-0.1, 0.1, total_lines)
    
    # --- Plot NR Lines (Solid) ---
    # These correspond to the first 'n_rows' of the single_legend
    for i in range(n_rows):
        # Specific jitter for this line
        x_shifted = x_vals + jitter_arr[i]
        
        ax.errorbar(
            x_shifted,
            means_nr[i],
            yerr=err_nr[i],
            fmt='o-',            # Solid line with markers
            linewidth=2,
            capsize=4,
            label=single_legend[i],
            color=colors[i],      # Assign color based on method type
            alpha=0.9
        )

    # --- Plot R Lines (Dotted) ---
    # These correspond to the second half of the single_legend, adjusted by offset
    # Legend structure is [6 items FL] + [6 items Pro]. 
    # Index for R corresponds to i + 6.
    for i in range(n_rows):
        # Specific jitter for this line (offset from NR lines)
        x_shifted = x_vals + jitter_arr[i + n_rows]
        
        # Calculate legend index (jump over the 6 FL items)
        leg_idx = i + 6
        
        ax.errorbar(
            x_shifted,
            means_r[i],
            yerr=err_r[i],
            fmt='o:',            # Dotted line (:) with markers
            linewidth=2,
            capsize=4,
            label=single_legend[leg_idx],
            color=colors[i],      # Same color as the NR counterpart
            alpha=0.9
        )

    # Formatting
    if idx < 3:
        x_tick_lbls = x_tick_lbls_line
    else:
        x_tick_lbls = x_tick_lbls_occupancy
        ax.set_xlabel("Maze Complexity")
    ax.set_title(title, fontsize=11)
    ax.set_xticks(x_vals)
    ax.set_xticklabels(x_tick_lbls)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    if idx % 3 == 0:
        ax.set_ylabel("Accuracy (%)")
    


    
    # Save handles from the last plot (Bottom-Right) because it contains all 12 lines
    if idx == 5:
        handles_for_legend, labels_for_legend = ax.get_legend_handles_labels()

# 5. Create Single Global Legend to the Right
# We take the handles from the bottom-right plot which covers all 12 cases.
# We stop the plots at 70% of the width, leaving 30% white space on the right.
plt.subplots_adjust(right=0.70)
# Position the legend within that white space
fig.legend(
    handles_for_legend, 
    labels_for_legend, 
    loc='center left',           # Align the LEFT side of the legend...
    bbox_to_anchor=(0.78, 0.5),  # ...to the point just after the plots (0.72)
    title="Representations & Models",
    borderaxespad=0.
)

plt.tight_layout()
# Adjust right margin to make room for the legend
plt.subplots_adjust(right=0.88) 
plt.show()
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
# # 3x3 s
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
# line_adj_json_raw_score_15 = np.array([3.0, 20.0, 44.0, 23.0, 5.0, 19.0, 5.0, 29.0, 15.0, 13.0])
# line_adj_txt_raw_score_15 = np.array([11.0, 19.0, 15.0, 9.0, 6.0, 24.0, 3.0, 3.0, 7.0, 16.0])
# line_jpg_raw_score_15 = np.array([4.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0])
# line_json_raw_score_15 = np.array([2.0, 4.0, 2.0, 1.0, 5.0, 1.0, 1.0, 2.0, 3.0, 1.0])
# line_tokenized_txt_raw_score_15 = np.array([1.0, 0.0, 0.0, 4.0, 2.0, 1.0, 0.0, 0.0, 0.0, 1.0])
# occupancy_adj_json_raw_score_15 = np.array([67.0, 11.0, 9.0, 62.0, 37.0, 85.0, 85.0, 23.0, 17.0, 13.0])
# occupancy_adj_txt_raw_score_15 = np.array([15.0, 9.0, 9.0, 37.0, 25.0, 49.0, 35.0, 51.0, 69.0, 32.0])
# occupancy_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score_15 = np.array([1.0, 1.0, 1.0, 7.0, 9.0, 17.0, 5.0, 5.0, 1.0, 9.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([1.0, 1.0, 1.0, 7, 11.0, 13.0, 11.0, 9.0, 1.0, 11.0])
# # 15x15 averages
# avg_coords_line_adj_json_raw_score_15 = np.mean(line_adj_json_raw_score_15)
# avg_coords_line_adj_txt_raw_score_15 = np.mean(line_adj_txt_raw_score_15)
# avg_coords_line_jpg_raw_score_15 = np.mean(line_jpg_raw_score_15)
# avg_coords_line_json_raw_score_15 = np.mean(line_json_raw_score_15)
# avg_coords_line_tokenized_txt_raw_score_15 = np.mean(line_tokenized_txt_raw_score_15)   
# avg_coords_occupancy_adj_json_raw_score_15 = np.mean(occupancy_adj_json_raw_score_15)
# avg_coords_occupancy_adj_txt_raw_score_15 = np.mean(occupancy_adj_txt_raw_score_15)
# avg_coords_occupancy_ascii_txt_raw_score_15 = np.mean(occupancy_ascii_txt_raw_score_15)
# avg_coords_occupancy_jpg_raw_score_15 = np.mean(occupancy_jpg_raw_score_15)
# avg_coords_occupancy_json_raw_score_15 = np.mean(occupancy_json_raw_score_15)
# avg_coords_occupancy_tokenized_txt_raw_score_15 = np.mean(occupancy_tokenized_txt_raw_score_15)

# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , avg_coords_line_jpg_raw_score_15]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  avg_coords_line_json_raw_score_15]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , avg_coords_line_adj_json_raw_score_15]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  avg_coords_line_adj_txt_raw_score_15]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , avg_coords_line_tokenized_txt_raw_score_15]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  avg_coords_occupancy_jpg_raw_score_15]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , avg_coords_occupancy_json_raw_score_15]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , avg_coords_occupancy_adj_json_raw_score_15]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , avg_coords_occupancy_adj_txt_raw_score_15]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , avg_coords_occupancy_tokenized_txt_raw_score_15]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , avg_coords_occupancy_ascii_txt_raw_score_15]
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
# ax1.set_ylabel("Average Number of Correct Steps")
# ax1.set_title("Average Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Coordinates Output")

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
# ax2.set_ylabel("Average Number of Correct Steps")
# ax2.set_title("Average Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Coordinates Output")

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
# avg_allo_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_allo_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_allo_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_allo_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_allo_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_allo_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_allo_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_allo_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_allo_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_allo_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_allo_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores NR Allo 15x15
# line_adj_json_raw_score_15 = np.array([0.0, 0.0, 0.0, 1.0, 4.0, 8.0, 1.0, 1.0, 0.0, 1.0])
# line_adj_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 1.0, 5.0, 10.0, 1.0, 1.0, 0.0, 1.0])
# line_jpg_raw_score_15 = np.array([0.0, 0.0, 0.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, 5.0])
# line_json_raw_score_15 = np.array([2.0, 3.0, 1.0, 1.0, 2.0, 8.0, 0.0, 0.0, 1.0, 0.0])
# line_tokenized_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0])
# occupancy_adj_json_raw_score_15 = np.array([2.0, 2.0, 6.0, 0.0, 6.0, 14.0, 3.0, 4.0, 4.0, 8.0])
# occupancy_adj_txt_raw_score_15 = np.array([0.0, 0.0, 2.0, 0.0, 0.0, 16.0, 4.0, 0.0, 2.0, 0.0])
# occupancy_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 2.0, 3.0, 0.0, 0.0, 3.0, 3.0, 0.0, 3.0])
# occupancy_jpg_raw_score_15 = np.array([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score_15 = np.array([0.0, 0.0, 0.0, 1.0, 6.0, 0.0, 1.0, 1.0, 0.0, 1.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 2.0, 6.0, 12.0, 4.0, 3.0, 0.0, 4.0])
# # 15x15 averages
# avg_allo_line_adj_json_raw_score_15 = np.mean(line_adj_json_raw_score_15)
# avg_allo_line_adj_txt_raw_score_15 = np.mean(line_adj_txt_raw_score_15)
# avg_allo_line_jpg_raw_score_15 = np.mean(line_jpg_raw_score_15)
# avg_allo_line_json_raw_score_15 = np.mean(line_json_raw_score_15)
# avg_allo_line_tokenized_txt_raw_score_15 = np.mean(line_tokenized_txt_raw_score_15)
# avg_allo_occupancy_adj_json_raw_score_15 = np.mean(occupancy_adj_json_raw_score_15)
# avg_allo_occupancy_adj_txt_raw_score_15 = np.mean(occupancy_adj_txt_raw_score_15)
# avg_allo_occupancy_ascii_txt_raw_score_15 = np.mean(occupancy_ascii_txt_raw_score_15) 
# avg_allo_occupancy_jpg_raw_score_15 = np.mean(occupancy_jpg_raw_score_15)
# avg_allo_occupancy_json_raw_score_15 = np.mean(occupancy_json_raw_score_15)
# avg_allo_occupancy_tokenized_txt_raw_score_15 = np.mean(occupancy_tokenized_txt_raw_score_15)

# # Dataset for top chart
# jpg_line = [avg_allo_line_jpg_raw_score , avg_allo_line_jpg_raw_score_6 , avg_allo_line_jpg_raw_score_15]
# json_line = [avg_allo_line_json_raw_score , avg_allo_line_json_raw_score_6 ,  avg_allo_line_json_raw_score_15]
# adj_json_line = [avg_allo_line_adj_json_raw_score , avg_allo_line_adj_json_raw_score_6 , avg_allo_line_adj_json_raw_score_15]
# adj_txt_line = [avg_allo_line_adj_txt_raw_score , avg_allo_line_adj_txt_raw_score_6,  avg_allo_line_adj_txt_raw_score_15]
# tokenized_line = [avg_allo_line_tokenized_txt_raw_score, avg_allo_line_tokenized_txt_raw_score_6 , avg_allo_line_tokenized_txt_raw_score_15]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_allo_occupancy_jpg_raw_score , avg_allo_occupancy_jpg_raw_score_6 ,  avg_allo_occupancy_jpg_raw_score_15]
# json_occupancy = [avg_allo_occupancy_json_raw_score , avg_allo_occupancy_json_raw_score_6 , avg_allo_occupancy_json_raw_score_15]
# adj_json_occupancy = [avg_allo_occupancy_adj_json_raw_score , avg_allo_occupancy_adj_json_raw_score_6 , avg_allo_occupancy_adj_json_raw_score_15]
# adj_txt_occupancy = [avg_allo_occupancy_adj_txt_raw_score , avg_allo_occupancy_adj_txt_raw_score_6 , avg_allo_occupancy_adj_txt_raw_score_15]
# tokenized_occupancy = [avg_allo_occupancy_tokenized_txt_raw_score , avg_allo_occupancy_tokenized_txt_raw_score_6 , avg_allo_occupancy_tokenized_txt_raw_score_15]
# ascii_occupancy = [avg_allo_occupancy_ascii_txt_raw_score , avg_allo_occupancy_ascii_txt_raw_score_6 , avg_allo_occupancy_ascii_txt_raw_score_15]
# dataset_occupancy = [ jpg_occupancy, json_occupancy, adj_json_occupancy, adj_txt_occupancy, tokenized_occupancy, ascii_occupancy]
# labels_occupancy = ['Occupancy JPG', 'Occupancy JSON', 'Occupancy Adjacency JSON', 'Occupancy Adjacency txt', 'Occupancy Tokenized' , 'Occupancy ASCII']

# x_pos = np.array([0, 1, 2])   # three x-axis positions
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
# ax1.set_ylabel("Average Number of Correct Steps")
# ax1.set_title("Average Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Allocentric Output")

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
# ax2.set_ylabel("Average Number of Correct Steps")
# ax2.set_title("Average Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Allocentric Output")

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
# avg_ego_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_ego_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_ego_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_ego_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_ego_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_ego_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_ego_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_ego_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_ego_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_ego_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_ego_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores NR Ego 15x15
# line_adj_json_raw_score_15 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_adj_txt_raw_score_15 = np.array([2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# line_jpg_raw_score_15 = np.array([2.0, 4.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# line_json_raw_score_15 = np.array([2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# line_tokenized_txt_raw_score_15 = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_adj_json_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
# occupancy_adj_txt_raw_score_15 = np.array([4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
# occupancy_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_jpg_raw_score_15 = np.array([2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# occupancy_json_raw_score_15 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([1.0, 6.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 1.0, 0.0])
# # 15x15 averages
# avg_ego_line_adj_json_raw_score_15 = np.mean(line_adj_json_raw_score_15)
# avg_ego_line_adj_txt_raw_score_15 = np.mean(line_adj_txt_raw_score_15)
# avg_ego_line_jpg_raw_score_15 = np.mean(line_jpg_raw_score_15)
# avg_ego_line_json_raw_score_15 = np.mean(line_json_raw_score_15)
# avg_ego_line_tokenized_txt_raw_score_15 = np.mean(line_tokenized_txt_raw_score_15)
# avg_ego_occupancy_adj_json_raw_score_15 = np.mean(occupancy_adj_json_raw_score_15)
# avg_ego_occupancy_adj_txt_raw_score_15 = np.mean(occupancy_adj_txt_raw_score_15)
# avg_ego_occupancy_ascii_txt_raw_score_15 = np.mean(occupancy_ascii_txt_raw_score_15)
# avg_ego_occupancy_jpg_raw_score_15 = np.mean(occupancy_jpg_raw_score_15)
# avg_ego_occupancy_json_raw_score_15 = np.mean(occupancy_json_raw_score_15)
# avg_ego_occupancy_tokenized_txt_raw_score_15 = np.mean(occupancy_tokenized_txt_raw_score_15)


# # Dataset for top chart
# jpg_line = [avg_ego_line_jpg_raw_score , avg_ego_line_jpg_raw_score_6 , avg_ego_line_jpg_raw_score_15]
# json_line = [avg_ego_line_json_raw_score , avg_ego_line_json_raw_score_6 ,  avg_ego_line_json_raw_score_15]
# adj_json_line = [avg_ego_line_adj_json_raw_score , avg_ego_line_adj_json_raw_score_6 , avg_ego_line_adj_json_raw_score_15]
# adj_txt_line = [avg_ego_line_adj_txt_raw_score , avg_ego_line_adj_txt_raw_score_6,  avg_ego_line_adj_txt_raw_score_15]
# tokenized_line = [avg_ego_line_tokenized_txt_raw_score, avg_ego_line_tokenized_txt_raw_score_6 , avg_ego_line_tokenized_txt_raw_score_15]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_ego_occupancy_jpg_raw_score , avg_ego_occupancy_jpg_raw_score_6 ,  avg_ego_occupancy_jpg_raw_score_15]
# json_occupancy = [avg_ego_occupancy_json_raw_score , avg_ego_occupancy_json_raw_score_6 , avg_ego_occupancy_json_raw_score_15]
# adj_json_occupancy = [avg_ego_occupancy_adj_json_raw_score , avg_ego_occupancy_adj_json_raw_score_6 , avg_ego_occupancy_adj_json_raw_score_15]
# adj_txt_occupancy = [avg_ego_occupancy_adj_txt_raw_score , avg_ego_occupancy_adj_txt_raw_score_6 , avg_ego_occupancy_adj_txt_raw_score_15]
# tokenized_occupancy = [avg_ego_occupancy_tokenized_txt_raw_score , avg_ego_occupancy_tokenized_txt_raw_score_6 , avg_ego_occupancy_tokenized_txt_raw_score_15]
# ascii_occupancy = [avg_ego_occupancy_ascii_txt_raw_score , avg_ego_occupancy_ascii_txt_raw_score_6 , avg_ego_occupancy_ascii_txt_raw_score_15]
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
# ax1.set_ylabel("Average Number of Correct Steps")
# ax1.set_title("Average Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Egocentric Output")

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
# ax2.set_ylabel("Average Number of Correct Steps")
# ax2.set_title("Average Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Egocentric Output")

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
# line_adj_json_raw_score_15 = np.array([131.0, 69.0, 139.0, 57.0, 127.0, 101.0, 67.0, 79.0, 133.0, 47.0])
# line_adj_txt_raw_score_15 = np.array([25.0, 10.0, 72.0, 57.0, 77.0, 93.0, 67.0, 45.0, 62.0, 47.0])
# line_jpg_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_json_raw_score_15 = np.array([31.0, 11.0, 10.0, 4.0, 16.0, 10.0, 38.0, 40.0, 2.0, 20.0])
# line_tokenized_txt_raw_score_15 = np.array([126.0, 69.0, 139.0, 57.0, 117.0, 23.0, 67.0, 49.0, 133.0, 47.0])
# occupancy_adj_json_raw_score_15 = np.array([261.0, 137.0, 191.0, 113.0, 253.0, 201.0, 133.0, 157.0, 265.0, 93.0])
# occupancy_adj_txt_raw_score_15 = np.array([89.0, 21.0, 69.0, 33.0, 31.0, 85.0, 5.0, 91.0, 123.0, 89.0])
# occupancy_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0])
# occupancy_jpg_raw_score_15 = np.array([5.0, 6.0, 3.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score_15 = np.array([31.0, 48.0, 5.0, 17.0, 9.0, 43.0, 40.0, 25.0, 19.0, 31.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([103.0, 137.0, 21.0, 113.0, 20, 15.0, 133.0, 21.0, 17.0, 11.0])
# # 15x15 averages
# avg_coords_line_adj_json_raw_score_15 = np.mean(line_adj_json_raw_score_15)
# avg_coords_line_adj_txt_raw_score_15 = np.mean(line_adj_txt_raw_score_15)
# avg_coords_line_jpg_raw_score_15 = np.mean(line_jpg_raw_score_15)
# avg_coords_line_json_raw_score_15 = np.mean(line_json_raw_score_15)
# avg_coords_line_tokenized_txt_raw_score_15 = np.mean(line_tokenized_txt_raw_score_15)
# avg_coords_occupancy_adj_json_raw_score_15 = np.mean(occupancy_adj_json_raw_score_15)
# avg_coords_occupancy_adj_txt_raw_score_15 = np.mean(occupancy_adj_txt_raw_score_15)
# avg_coords_occupancy_ascii_txt_raw_score_15 = np.mean(occupancy_ascii_txt_raw_score_15)
# avg_coords_occupancy_jpg_raw_score_15 = np.mean(occupancy_jpg_raw_score_15)
# avg_coords_occupancy_json_raw_score_15 = np.mean(occupancy_json_raw_score_15)
# avg_coords_occupancy_tokenized_txt_raw_score_15 = np.mean(occupancy_tokenized_txt_raw_score_15)


# # Dataset for top chart
# jpg_line = [avg_coords_line_jpg_raw_score , avg_coords_line_jpg_raw_score_6 , avg_coords_line_jpg_raw_score_15]
# json_line = [avg_coords_line_json_raw_score , avg_coords_line_json_raw_score_6 ,  avg_coords_line_json_raw_score_15]
# adj_json_line = [avg_coords_line_adj_json_raw_score , avg_coords_line_adj_json_raw_score_6 , avg_coords_line_adj_json_raw_score_15]
# adj_txt_line = [avg_coords_line_adj_txt_raw_score , avg_coords_line_adj_txt_raw_score_6,  avg_coords_line_adj_txt_raw_score_15]
# tokenized_line = [avg_coords_line_tokenized_txt_raw_score, avg_coords_line_tokenized_txt_raw_score_6 , avg_coords_line_tokenized_txt_raw_score_15]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_coords_occupancy_jpg_raw_score , avg_coords_occupancy_jpg_raw_score_6 ,  avg_coords_occupancy_jpg_raw_score_15]
# json_occupancy = [avg_coords_occupancy_json_raw_score , avg_coords_occupancy_json_raw_score_6 , avg_coords_occupancy_json_raw_score_15]
# adj_json_occupancy = [avg_coords_occupancy_adj_json_raw_score , avg_coords_occupancy_adj_json_raw_score_6 , avg_coords_occupancy_adj_json_raw_score_15]
# adj_txt_occupancy = [avg_coords_occupancy_adj_txt_raw_score , avg_coords_occupancy_adj_txt_raw_score_6 , avg_coords_occupancy_adj_txt_raw_score_15]
# tokenized_occupancy = [avg_coords_occupancy_tokenized_txt_raw_score , avg_coords_occupancy_tokenized_txt_raw_score_6 , avg_coords_occupancy_tokenized_txt_raw_score_15]
# ascii_occupancy = [avg_coords_occupancy_ascii_txt_raw_score , avg_coords_occupancy_ascii_txt_raw_score_6 , avg_coords_occupancy_ascii_txt_raw_score_15]
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
# ax1.set_ylabel("Average Number of Correct Steps")
# ax1.set_title("Average Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Coordinates Output")

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
# ax2.set_ylabel("Average Number of Correct Steps")
# ax2.set_title("Average Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Coordinates Output")

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
# avg_allo_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_allo_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_allo_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_allo_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_allo_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_allo_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_allo_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_allo_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_allo_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_allo_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_allo_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores R Allo 15x15
# line_adj_json_raw_score_15 = np.array([61.0, 68.0, 138.0, 56.0, 126.0, 100.0, 66.0, 78.0, 132.0, 46.0])
# line_adj_txt_raw_score_15 = np.array([10.0, 68.0, 74.0, 56.0, 1.0, 98.0, 66.0, 2.0, 77.0, 46.0])
# line_jpg_raw_score_15 = np.array([1.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
# line_json_raw_score_15 = np.array([36.0, 10.0, 14.0, 7.0, 12.0, 26.0, 13.0, 23.0, 2.0, 15.0])
# line_tokenized_txt_raw_score_15 = np.array([43.0, 27.0, 11.0, 3.0, 50.0, 100.0, 66.0, 39.0, 80.0, 46.0])
# occupancy_adj_json_raw_score_15 = np.array([120.0, 136.0, 106.0, 112.0, 87.0, 200.0, 132.0, 156.0, 188.0, 92.0])
# occupancy_adj_txt_raw_score_15 = np.array([72.0, 136.0, 20.0, 16.0, 23.0, 154.0, 34.0, 106.0, 104.0, 92.0])
# occupancy_ascii_txt_raw_score_15 = np.array([4.0, 8.0, 0.0, 0.0, 0.0, 0.0, 4.0, 2.0, 4.0, 0.0])
# occupancy_jpg_raw_score_15 = np.array([3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json_raw_score_15 = np.array([1.0, 38.0, 16.0, 44.0, 8.0, 14.0, 4.0, 0.0, 8.0, 7.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([66.0, 136.0, 12.0, 112.0, 128.0, 20.0, 24.0, 96.0, 2.0, 92])
# # 15x15 averages
# avg_allo_line_adj_json_raw_score_15 = np.mean(line_adj_json_raw_score_15)
# avg_allo_line_adj_txt_raw_score_15 = np.mean(line_adj_txt_raw_score_15)
# avg_allo_line_jpg_raw_score_15 = np.mean(line_jpg_raw_score_15)
# avg_allo_line_json_raw_score_15 = np.mean(line_json_raw_score_15)
# avg_allo_line_tokenized_txt_raw_score_15 = np.mean(line_tokenized_txt_raw_score_15)
# avg_allo_occupancy_adj_json_raw_score_15 = np.mean(occupancy_adj_json_raw_score_15)
# avg_allo_occupancy_adj_txt_raw_score_15 = np.mean(occupancy_adj_txt_raw_score_15)
# avg_allo_occupancy_ascii_txt_raw_score_15 = np.mean(occupancy_ascii_txt_raw_score_15)
# avg_allo_occupancy_jpg_raw_score_15 = np.mean(occupancy_jpg_raw_score_15)
# avg_allo_occupancy_json_raw_score_15 = np.mean(occupancy_json_raw_score_15)
# avg_allo_occupancy_tokenized_txt_raw_score_15 = np.mean(occupancy_tokenized_txt_raw_score_15)


# # Dataset for top chart
# jpg_line = [avg_allo_line_jpg_raw_score , avg_allo_line_jpg_raw_score_6 , avg_allo_line_jpg_raw_score_15]
# json_line = [avg_allo_line_json_raw_score , avg_allo_line_json_raw_score_6 ,  avg_allo_line_json_raw_score_15]
# adj_json_line = [avg_allo_line_adj_json_raw_score , avg_allo_line_adj_json_raw_score_6 , avg_allo_line_adj_json_raw_score_15]
# adj_txt_line = [avg_allo_line_adj_txt_raw_score , avg_allo_line_adj_txt_raw_score_6,  avg_allo_line_adj_txt_raw_score_15]
# tokenized_line = [avg_allo_line_tokenized_txt_raw_score, avg_allo_line_tokenized_txt_raw_score_6 , avg_allo_line_tokenized_txt_raw_score_15]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_allo_occupancy_jpg_raw_score , avg_allo_occupancy_jpg_raw_score_6 ,  avg_allo_occupancy_jpg_raw_score_15]
# json_occupancy = [avg_allo_occupancy_json_raw_score , avg_allo_occupancy_json_raw_score_6 , avg_allo_occupancy_json_raw_score_15]
# adj_json_occupancy = [avg_allo_occupancy_adj_json_raw_score , avg_allo_occupancy_adj_json_raw_score_6 , avg_allo_occupancy_adj_json_raw_score_15]
# adj_txt_occupancy = [avg_allo_occupancy_adj_txt_raw_score , avg_allo_occupancy_adj_txt_raw_score_6 , avg_allo_occupancy_adj_txt_raw_score_15]
# tokenized_occupancy = [avg_allo_occupancy_tokenized_txt_raw_score , avg_allo_occupancy_tokenized_txt_raw_score_6 , avg_allo_occupancy_tokenized_txt_raw_score_15]
# ascii_occupancy = [avg_allo_occupancy_ascii_txt_raw_score , avg_allo_occupancy_ascii_txt_raw_score_6 , avg_allo_occupancy_ascii_txt_raw_score_15]
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
# ax1.set_ylabel("Average Number of Correct Steps")
# ax1.set_title("Average Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Allocentric Output")

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
# ax2.set_ylabel("Average Number of Correct Steps")
# ax2.set_title("Average Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Allocentric Output")

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
# avg_ego_line_adj_json_raw_score_6 = np.mean(line_adj_json_raw_score_6)
# avg_ego_line_adj_txt_raw_score_6 = np.mean(line_adj_txt_raw_score_6)
# avg_ego_line_jpg_raw_score_6 = np.mean(line_jpg_raw_score_6)
# avg_ego_line_json_raw_score_6 = np.mean(line_json_raw_score_6)
# avg_ego_line_tokenized_txt_raw_score_6 = np.mean(line_tokenized_txt_raw_score_6)
# avg_ego_occupancy_adj_json_raw_score_6 = np.mean(occupancy_adj_json_raw_score_6)
# avg_ego_occupancy_adj_txt_raw_score_6 = np.mean(occupancy_adj_txt_raw_score_6)
# avg_ego_occupancy_ascii_txt_raw_score_6 = np.mean(occupancy_ascii_txt_raw_score_6)  
# avg_ego_occupancy_jpg_raw_score_6 = np.mean(occupancy_jpg_raw_score_6)
# avg_ego_occupancy_json_raw_score_6 = np.mean(occupancy_json_raw_score_6)
# avg_ego_occupancy_tokenized_txt_raw_score_6 = np.mean(occupancy_tokenized_txt_raw_score_6)
# # Raw Scores R Ego 15x15
# line_adj_json_raw_score_15 = np.array([4.0, 68.0, 21.0, 56.0, 45.0, 100.0, 66.0, 78.0, 82.0, 46.0])
# line_adj_txt_raw_score_15 = np.array([3.0, 14.0, 1.0, 56.0, 0.0, 11.0, 0.0, 0.0, 61.0, 0.0])
# line_jpg_raw_score_15 = np.array([1.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
# line_json_raw_score_15 = np.array([4.0, 25.0, 13.0, 0.0, 18.0, 26.0, 12.0, 6.0, 10.0, 14.0])
# line_tokenized_txt_raw_score_15 = np.array([2.0, 20.0, 2.0, 56.0, 0.0, 0.0, 66.0, 78.0, 1.0, 46.0])
# occupancy_adj_json_raw_score_15 = np.array([89.0, 52.0, 30.0, 112.0, 0.0, 72.0, 86.0, 78.0, 2.0, 92.0])
# occupancy_adj_txt_raw_score_15 = np.array([4.0, 56.0, 38.0, 0.0, 0.0, 0.0, 35.0, 156.0, 14.0, 13.0])
# occupancy_ascii_txt_raw_score_15 = np.array([2.0, 9.0, 1.0, 5.0, 8.0, 11.0, 0.0, 0.0, 1.0, 4.0])
# occupancy_jpg_raw_score_15 = np.array([4.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
# occupancy_json_raw_score_15 = np.array([10.0, 8.0, 6.0, 12.0, 40.0, 0.0, 14.0, 10.0, 4.0, 10.0])
# occupancy_tokenized_txt_raw_score_15 = np.array([71.0, 66.0, 16.0, 0.0, 6.0, 7.0, 52.0, 36.0, 16.0, 14])

# # 15x15 averages
# avg_ego_line_adj_json_raw_score_15 = np.mean(line_adj_json_raw_score_15)
# avg_ego_line_adj_txt_raw_score_15 = np.mean(line_adj_txt_raw_score_15)
# avg_ego_line_jpg_raw_score_15 = np.mean(line_jpg_raw_score_15)
# avg_ego_line_json_raw_score_15 = np.mean(line_json_raw_score_15)
# avg_ego_line_tokenized_txt_raw_score_15 = np.mean(line_tokenized_txt_raw_score_15)
# avg_ego_occupancy_adj_json_raw_score_15 = np.mean(occupancy_adj_json_raw_score_15)
# avg_ego_occupancy_adj_txt_raw_score_15 = np.mean(occupancy_adj_txt_raw_score_15)
# avg_ego_occupancy_ascii_txt_raw_score_15 = np.mean(occupancy_ascii_txt_raw_score_15)
# avg_ego_occupancy_jpg_raw_score_15 = np.mean(occupancy_jpg_raw_score_15)
# avg_ego_occupancy_json_raw_score_15 = np.mean(occupancy_json_raw_score_15)
# avg_ego_occupancy_tokenized_txt_raw_score_15 = np.mean(occupancy_tokenized_txt_raw_score_15)


# # Dataset for top chart
# jpg_line = [avg_ego_line_jpg_raw_score , avg_ego_line_jpg_raw_score_6 , avg_ego_line_jpg_raw_score_15]
# json_line = [avg_ego_line_json_raw_score , avg_ego_line_json_raw_score_6 ,  avg_ego_line_json_raw_score_15]
# adj_json_line = [avg_ego_line_adj_json_raw_score , avg_ego_line_adj_json_raw_score_6 , avg_ego_line_adj_json_raw_score_15]
# adj_txt_line = [avg_ego_line_adj_txt_raw_score , avg_ego_line_adj_txt_raw_score_6,  avg_ego_line_adj_txt_raw_score_15]
# tokenized_line = [avg_ego_line_tokenized_txt_raw_score, avg_ego_line_tokenized_txt_raw_score_6 , avg_ego_line_tokenized_txt_raw_score_15]
# dataset_line = [ jpg_line, json_line, adj_json_line, adj_txt_line, tokenized_line]
# labels_line = ['Line JPG', 'Line JSON', 'Line Adjacency JSON', 'Line Adjacency txt', 'Line Tokenized' ]

# # Dataset for bottom chart
# jpg_occupancy = [avg_ego_occupancy_jpg_raw_score , avg_ego_occupancy_jpg_raw_score_6 ,  avg_ego_occupancy_jpg_raw_score_15]
# json_occupancy = [avg_ego_occupancy_json_raw_score , avg_ego_occupancy_json_raw_score_6 , avg_ego_occupancy_json_raw_score_15]
# adj_json_occupancy = [avg_ego_occupancy_adj_json_raw_score , avg_ego_occupancy_adj_json_raw_score_6 , avg_ego_occupancy_adj_json_raw_score_15]
# adj_txt_occupancy = [avg_ego_occupancy_adj_txt_raw_score , avg_ego_occupancy_adj_txt_raw_score_6 , avg_ego_occupancy_adj_txt_raw_score_15]
# tokenized_occupancy = [avg_ego_occupancy_tokenized_txt_raw_score , avg_ego_occupancy_tokenized_txt_raw_score_6 , avg_ego_occupancy_tokenized_txt_raw_score_15]
# ascii_occupancy = [avg_ego_occupancy_ascii_txt_raw_score , avg_ego_occupancy_ascii_txt_raw_score_6 , avg_ego_occupancy_ascii_txt_raw_score_15]
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
# ax1.set_ylabel("Average Number of Correct Steps")
# ax1.set_title("Average Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Egocentric Output")

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
# ax2.set_ylabel("Average Number of Correct Steps")
# ax2.set_title("Average Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Egocentric Output")

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









# # NR - EGO - 1-3 -----------acc/tokens vs. complexity -----------------------------
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

# ax.grid(axis='y', linestyle='--', alpha=0.8)

# ax.legend(
#     loc='lower center',
#     bbox_to_anchor=(0.5, 1.15),
#     ncol=3,
#     fontsize=9
# )

# plt.tight_layout()
# plt.show()