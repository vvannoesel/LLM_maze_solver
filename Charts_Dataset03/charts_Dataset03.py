# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import numpy as np
import matplotlib.pyplot as plt
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple


x_axis_line = ['3x3', '6x6', '15x15']
x_axis_occ = ['7x7', '13x13', '31x31']

def confidence_interval(vector):
    z = 1.96
    n = len(vector)
    sd = np.nanstd(vector, ddof=1)  # calculate standard deviation
    # mean = np.nanmean(vector)
    error = z * (sd / np.sqrt(n))
    # lower_bound = mean-error
    # upper_bound = mean+error
    return error #lower_bound, upper_bound 

# --- Plotting mean accuracy with stdev error bars for all types and sizes until run 10 ----------

# NR -- Coords -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Averages and std deviation 3x3
avg_line_NR_coords_adj_json = np.mean(r3.line_NR_coords_adj_json_3)
avg_line_NR_coords_adj_txt = np.mean(r3.line_NR_coords_adj_txt_3)
avg_line_NR_coords_jpg = np.mean(r3.line_NR_coords_jpg_3)
avg_line_NR_coords_json = np.mean(r3.line_NR_coords_json_3)
avg_line_NR_coords_tokenized_txt = np.mean(r3.line_NR_coords_tokenized_txt_3)
avg_occupancy_NR_coords_adj_json = np.mean(r3.occupancy_NR_coords_adj_json_3)
avg_occupancy_NR_coords_adj_txt = np.mean(r3.occupancy_NR_coords_adj_txt_3)
avg_occupancy_NR_coords_ascii_txt = np.mean(r3.occupancy_NR_coords_ascii_txt_3)  
avg_occupancy_NR_coords_jpg = np.mean(r3.occupancy_NR_coords_jpg_3)
avg_occupancy_NR_coords_json = np.mean(r3.occupancy_NR_coords_json_3)
avg_occupancy_NR_coords_tokenized_txt = np.mean(r3.occupancy_NR_coords_tokenized_txt_3)
sd_line_NR_coords_adj_json = np.std(r3.line_NR_coords_adj_json_3)
sd_line_NR_coords_adj_txt = np.std(r3.line_NR_coords_adj_txt_3)
sd_line_NR_coords_jpg = np.std(r3.line_NR_coords_jpg_3)
sd_line_NR_coords_json = np.std(r3.line_NR_coords_json_3)
sd_line_NR_coords_tokenized_txt = np.std(r3.line_NR_coords_tokenized_txt_3)
sd_occupancy_NR_coords_adj_json = np.std(r3.occupancy_NR_coords_adj_json_3)
sd_occupancy_NR_coords_adj_txt = np.std(r3.occupancy_NR_coords_adj_txt_3)
sd_occupancy_NR_coords_ascii_txt = np.std(r3.occupancy_NR_coords_ascii_txt_3)  
sd_occupancy_NR_coords_jpg = np.std(r3.occupancy_NR_coords_jpg_3)
sd_occupancy_NR_coords_json = np.std(r3.occupancy_NR_coords_json_3)
sd_occupancy_NR_coords_tokenized_txt = np.std(r3.occupancy_NR_coords_tokenized_txt_3)
# Averages and std deviation 6x6
avg_line_NR_coords_adj_json_6 = np.mean(r6.line_NR_coords_adj_json_6)
avg_line_NR_coords_adj_txt_6 = np.mean(r6.line_NR_coords_adj_txt_6)
avg_line_NR_coords_jpg_6 = np.mean(r6.line_NR_coords_jpg_6)
avg_line_NR_coords_json_6 = np.mean(r6.line_NR_coords_json_6)
avg_line_NR_coords_tokenized_txt_6 = np.mean(r6.line_NR_coords_tokenized_txt_6)
avg_occupancy_NR_coords_adj_json_6 = np.mean(r6.occupancy_NR_coords_adj_json_6)
avg_occupancy_NR_coords_adj_txt_6 = np.mean(r6.occupancy_NR_coords_adj_txt_6)
avg_occupancy_NR_coords_ascii_txt_6 = np.mean(r6.occupancy_NR_coords_ascii_txt_6)  
avg_occupancy_NR_coords_jpg_6 = np.mean(r6.occupancy_NR_coords_jpg_6)
avg_occupancy_NR_coords_json_6 = np.mean(r6.occupancy_NR_coords_json_6)
avg_occupancy_NR_coords_tokenized_txt_6 = np.mean(r6.occupancy_NR_coords_tokenized_txt_6)
sd_line_NR_coords_adj_json_6 = np.std(r6.line_NR_coords_adj_json_6)
sd_line_NR_coords_adj_txt_6 = np.std(r6.line_NR_coords_adj_txt_6)
sd_line_NR_coords_jpg_6 = np.std(r6.line_NR_coords_jpg_6)
sd_line_NR_coords_json_6 = np.std(r6.line_NR_coords_json_6)
sd_line_NR_coords_tokenized_txt_6 = np.std(r6.line_NR_coords_tokenized_txt_6)
sd_occupancy_NR_coords_adj_json_6 = np.std(r6.occupancy_NR_coords_adj_json_6)
sd_occupancy_NR_coords_adj_txt_6 = np.std(r6.occupancy_NR_coords_adj_txt_6)
sd_occupancy_NR_coords_ascii_txt_6 = np.std(r6.occupancy_NR_coords_ascii_txt_6)  
sd_occupancy_NR_coords_jpg_6 = np.std(r6.occupancy_NR_coords_jpg_6)
sd_occupancy_NR_coords_json_6 = np.std(r6.occupancy_NR_coords_json_6)
sd_occupancy_NR_coords_tokenized_txt_6 = np.std(r6.occupancy_NR_coords_tokenized_txt_6)
# Averages and std deviation 15x15
avg_line_NR_coords_adj_json_15 = np.mean(r15.line_NR_coords_adj_json_15)
avg_line_NR_coords_adj_txt_15 = np.mean(r15.line_NR_coords_adj_txt_15)
avg_line_NR_coords_jpg_15 = np.mean(r15.line_NR_coords_jpg_15)
avg_line_NR_coords_json_15 = np.mean(r15.line_NR_coords_json_15)
avg_line_NR_coords_tokenized_txt_15 = np.mean(r15.line_NR_coords_tokenized_txt_15)
avg_occupancy_NR_coords_adj_json_15 = np.mean(r15.occupancy_NR_coords_adj_json_15)
avg_occupancy_NR_coords_adj_txt_15 = np.mean(r15.occupancy_NR_coords_adj_txt_15)
avg_occupancy_NR_coords_ascii_txt_15 = np.mean(r15.occupancy_NR_coords_ascii_txt_15)  
avg_occupancy_NR_coords_jpg_15 = np.mean(r15.occupancy_NR_coords_jpg_15)
avg_occupancy_NR_coords_json_15 = np.mean(r15.occupancy_NR_coords_json_15)
avg_occupancy_NR_coords_tokenized_txt_15 = np.mean(r15.occupancy_NR_coords_tokenized_txt_15)
sd_line_NR_coords_adj_json_15 = np.std(r15.line_NR_coords_adj_json_15)
sd_line_NR_coords_adj_txt_15 = np.std(r15.line_NR_coords_adj_txt_15)
sd_line_NR_coords_jpg_15 = np.std(r15.line_NR_coords_jpg_15)
sd_line_NR_coords_json_15 = np.std(r15.line_NR_coords_json_15)
sd_line_NR_coords_tokenized_txt_15 = np.std(r15.line_NR_coords_tokenized_txt_15)
sd_occupancy_NR_coords_adj_json_15 = np.std(r15.occupancy_NR_coords_adj_json_15)
sd_occupancy_NR_coords_adj_txt_15 = np.std(r15.occupancy_NR_coords_adj_txt_15)
sd_occupancy_NR_coords_ascii_txt_15 = np.std(r15.occupancy_NR_coords_ascii_txt_15)  
sd_occupancy_NR_coords_jpg_15 = np.std(r15.occupancy_NR_coords_jpg_15)
sd_occupancy_NR_coords_json_15 = np.std(r15.occupancy_NR_coords_json_15)
sd_occupancy_NR_coords_tokenized_txt_15 = np.std(r15.occupancy_NR_coords_tokenized_txt_15)

# Top plot data: line-maze data vectors with the complexities as column entries and representations as row entries.
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
    [sd_line_NR_coords_json,           sd_line_NR_coords_json_6,           sd_line_NR_coords_json_15],
    [sd_line_NR_coords_tokenized_txt, sd_line_NR_coords_tokenized_txt_6, sd_line_NR_coords_tokenized_txt_15]
]

error_line_NR_coords = [
    [confidence_interval(r3.line_NR_coords_adj_json_3),       confidence_interval(r6.line_NR_coords_adj_json_6),       confidence_interval(r15.line_NR_coords_adj_json_15)],
    [confidence_interval(r3.line_NR_coords_adj_txt_3),        confidence_interval(r6.line_NR_coords_adj_txt_6),        confidence_interval(r15.line_NR_coords_adj_txt_15)],
    [confidence_interval(r3.line_NR_coords_jpg_3),            confidence_interval(r6.line_NR_coords_jpg_6),            confidence_interval(r15.line_NR_coords_jpg_15)],
    [confidence_interval(r3.line_NR_coords_json_3),           confidence_interval(r6.line_NR_coords_json_6),           confidence_interval(r15.line_NR_coords_json_15)],
    [confidence_interval(r3.line_NR_coords_tokenized_txt_3),  confidence_interval(r6.line_NR_coords_tokenized_txt_6),  confidence_interval(r15.line_NR_coords_tokenized_txt_15)]
]

labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

# Bottom plot data: occupancy-maze data vectors with the complexities as column entries and representations as row entries. 
means_occ_NR_coords = [
    [avg_occupancy_NR_coords_adj_json,       avg_occupancy_NR_coords_adj_json_6,      avg_occupancy_NR_coords_adj_json_15],
    [avg_occupancy_NR_coords_adj_txt,        avg_occupancy_NR_coords_adj_txt_6,        avg_occupancy_NR_coords_adj_txt_15],
    [avg_occupancy_NR_coords_jpg,            avg_occupancy_NR_coords_jpg_6,            avg_occupancy_NR_coords_jpg_15],
    [avg_occupancy_NR_coords_json,           avg_occupancy_NR_coords_json_6,           avg_occupancy_NR_coords_json_15],
    [avg_occupancy_NR_coords_tokenized_txt,  avg_occupancy_NR_coords_tokenized_txt_6,  avg_occupancy_NR_coords_tokenized_txt_15],
    [avg_occupancy_NR_coords_ascii_txt,      avg_occupancy_NR_coords_ascii_txt_6,      avg_occupancy_NR_coords_ascii_txt_15]
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
    [confidence_interval(r3.occupancy_NR_coords_adj_json_3),       confidence_interval(r6.occupancy_NR_coords_adj_json_6),       confidence_interval(r15.occupancy_NR_coords_adj_json_15)],
    [confidence_interval(r3.occupancy_NR_coords_adj_txt_3),        confidence_interval(r6.occupancy_NR_coords_adj_txt_6),        confidence_interval(r15.occupancy_NR_coords_adj_txt_15)],
    [confidence_interval(r3.occupancy_NR_coords_jpg_3),            confidence_interval(r6.occupancy_NR_coords_jpg_6),            confidence_interval(r15.occupancy_NR_coords_jpg_15)],
    [confidence_interval(r3.occupancy_NR_coords_json_3),           confidence_interval(r6.occupancy_NR_coords_json_6),           confidence_interval(r15.occupancy_NR_coords_json_15)],
    [confidence_interval(r3.occupancy_NR_coords_tokenized_txt_3),  confidence_interval(r6.occupancy_NR_coords_tokenized_txt_6),  confidence_interval(r15.occupancy_NR_coords_tokenized_txt_15)],
    [ confidence_interval(r3.occupancy_NR_coords_ascii_txt_3),     confidence_interval(r6.occupancy_NR_coords_ascii_txt_6),      confidence_interval(r15.occupancy_NR_coords_ascii_txt_15)]
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
# Averages and std deviation 3x3
avg_line_NR_allo_adj_json = np.mean(r3.line_NR_allo_adj_json_3)
avg_line_NR_allo_adj_txt = np.mean(r3.line_NR_allo_adj_txt_3)
avg_line_NR_allo_jpg = np.mean(r3.line_NR_allo_jpg_3)
avg_line_NR_allo_json = np.mean(r3.line_NR_allo_json_3)
avg_line_NR_allo_tokenized_txt = np.mean(r3.line_NR_allo_tokenized_txt_3)
avg_occupancy_NR_allo_adj_json = np.mean(r3.occupancy_NR_allo_adj_json_3)
avg_occupancy_NR_allo_adj_txt = np.mean(r3.occupancy_NR_allo_adj_txt_3)
avg_occupancy_NR_allo_ascii_txt = np.mean(r3.occupancy_NR_allo_ascii_txt_3)  
avg_occupancy_NR_allo_jpg = np.mean(r3.occupancy_NR_allo_jpg_3)
avg_occupancy_NR_allo_json = np.mean(r3.occupancy_NR_allo_json_3)
avg_occupancy_NR_allo_tokenized_txt = np.mean(r3.occupancy_NR_allo_tokenized_txt_3)
sd_line_NR_allo_adj_json = np.std(r3.line_NR_allo_adj_json_3)
sd_line_NR_allo_adj_txt = np.std(r3.line_NR_allo_adj_txt_3)
sd_line_NR_allo_jpg = np.std(r3.line_NR_allo_jpg_3)
sd_line_NR_allo_json = np.std(r3.line_NR_allo_json_3)
sd_line_NR_allo_tokenized_txt = np.std(r3.line_NR_allo_tokenized_txt_3)
sd_occupancy_NR_allo_adj_json = np.std(r3.occupancy_NR_allo_adj_json_3)
sd_occupancy_NR_allo_adj_txt = np.std(r3.occupancy_NR_allo_adj_txt_3)
sd_occupancy_NR_allo_ascii_txt = np.std(r3.occupancy_NR_allo_ascii_txt_3)  
sd_occupancy_NR_allo_jpg = np.std(r3.occupancy_NR_allo_jpg_3)
sd_occupancy_NR_allo_json = np.std(r3.occupancy_NR_allo_json_3)
sd_occupancy_NR_allo_tokenized_txt = np.std(r3.occupancy_NR_allo_tokenized_txt_3)
# Averages and std deviation 6x6
avg_line_NR_allo_adj_json_6 = np.mean(r6.line_NR_allo_adj_json_6)
avg_line_NR_allo_adj_txt_6 = np.mean(r6.line_NR_allo_adj_txt_6)
avg_line_NR_allo_jpg_6 = np.mean(r6.line_NR_allo_jpg_6)
avg_line_NR_allo_json_6 = np.mean(r6.line_NR_allo_json_6)
avg_line_NR_allo_tokenized_txt_6 = np.mean(r6.line_NR_allo_tokenized_txt_6)
avg_occupancy_NR_allo_adj_json_6 = np.mean(r6.occupancy_NR_allo_adj_json_6)
avg_occupancy_NR_allo_adj_txt_6 = np.mean(r6.occupancy_NR_allo_adj_txt_6)
avg_occupancy_NR_allo_ascii_txt_6 = np.mean(r6.occupancy_NR_allo_ascii_txt_6)  
avg_occupancy_NR_allo_jpg_6 = np.mean(r6.occupancy_NR_allo_jpg_6)
avg_occupancy_NR_allo_json_6 = np.mean(r6.occupancy_NR_allo_json_6)
avg_occupancy_NR_allo_tokenized_txt_6 = np.mean(r6.occupancy_NR_allo_tokenized_txt_6)
sd_line_NR_allo_adj_json_6 = np.std(r6.line_NR_allo_adj_json_6)
sd_line_NR_allo_adj_txt_6 = np.std(r6.line_NR_allo_adj_txt_6)
sd_line_NR_allo_jpg_6 = np.std(r6.line_NR_allo_jpg_6)
sd_line_NR_allo_json_6 = np.std(r6.line_NR_allo_json_6)
sd_line_NR_allo_tokenized_txt_6 = np.std(r6.line_NR_allo_tokenized_txt_6)
sd_occupancy_NR_allo_adj_json_6 = np.std(r6.occupancy_NR_allo_adj_json_6)
sd_occupancy_NR_allo_adj_txt_6 = np.std(r6.occupancy_NR_allo_adj_txt_6)
sd_occupancy_NR_allo_ascii_txt_6 = np.std(r6.occupancy_NR_allo_ascii_txt_6)  
sd_occupancy_NR_allo_jpg_6 = np.std(r6.occupancy_NR_allo_jpg_6)
sd_occupancy_NR_allo_json_6 = np.std(r6.occupancy_NR_allo_json_6)
sd_occupancy_NR_allo_tokenized_txt_6 = np.std(r6.occupancy_NR_allo_tokenized_txt_6)
# Averages and std deviation 15x15
avg_line_NR_allo_adj_json_15 = np.mean(r15.line_NR_allo_adj_json_15)
avg_line_NR_allo_adj_txt_15 = np.mean(r15.line_NR_allo_adj_txt_15)
avg_line_NR_allo_jpg_15 = np.nanmean(r15.line_NR_allo_jpg_15)
avg_line_NR_allo_json_15 = np.mean(r15.line_NR_allo_json_15)
avg_line_NR_allo_tokenized_txt_15 = np.mean(r15.line_NR_allo_tokenized_txt_15)
avg_occupancy_NR_allo_adj_json_15 = np.mean(r15.occupancy_NR_allo_adj_json_15)
avg_occupancy_NR_allo_adj_txt_15 = np.mean(r15.occupancy_NR_allo_adj_txt_15)
avg_occupancy_NR_allo_ascii_txt_15 = np.mean(r15.occupancy_NR_allo_ascii_txt_15)  
avg_occupancy_NR_allo_jpg_15 = np.nanmean(r15.occupancy_NR_allo_jpg_15)
avg_occupancy_NR_allo_json_15 = np.mean(r15.occupancy_NR_allo_json_15)
avg_occupancy_NR_allo_tokenized_txt_15 = np.mean(r15.occupancy_NR_allo_tokenized_txt_15)
sd_line_NR_allo_adj_json_15 = np.std(r15.line_NR_allo_adj_json_15)
sd_line_NR_allo_adj_txt_15 = np.std(r15.line_NR_allo_adj_txt_15)
sd_line_NR_allo_jpg_15 = np.std(r15.line_NR_allo_jpg_15)
sd_line_NR_allo_json_15 = np.std(r15.line_NR_allo_json_15)
sd_line_NR_allo_tokenized_txt_15 = np.std(r15.line_NR_allo_tokenized_txt_15)
sd_occupancy_NR_allo_adj_json_15 = np.std(r15.occupancy_NR_allo_adj_json_15)
sd_occupancy_NR_allo_adj_txt_15 = np.std(r15.occupancy_NR_allo_adj_txt_15)
sd_occupancy_NR_allo_ascii_txt_15 = np.std(r15.occupancy_NR_allo_ascii_txt_15)  
sd_occupancy_NR_allo_jpg_15 = np.std(r15.occupancy_NR_allo_jpg_15)
sd_occupancy_NR_allo_json_15 = np.std(r15.occupancy_NR_allo_json_15)
sd_occupancy_NR_allo_tokenized_txt_15 = np.std(r15.occupancy_NR_allo_tokenized_txt_15)


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
    [confidence_interval(r3.line_NR_allo_adj_json_3),       confidence_interval(r6.line_NR_allo_adj_json_6),       confidence_interval(r15.line_NR_allo_adj_json_15)],
    [confidence_interval(r3.line_NR_allo_adj_txt_3),        confidence_interval(r6.line_NR_allo_adj_txt_6),        confidence_interval(r15.line_NR_allo_adj_txt_15)],
    [confidence_interval(r3.line_NR_allo_jpg_3),            confidence_interval(r6.line_NR_allo_jpg_6),            confidence_interval(r15.line_NR_allo_jpg_15)],
    [confidence_interval(r3.line_NR_allo_json_3),           confidence_interval(r6.line_NR_allo_json_6),           confidence_interval(r15.line_NR_allo_json_15)],
    [confidence_interval(r3.line_NR_allo_tokenized_txt_3),  confidence_interval(r6.line_NR_allo_tokenized_txt_6),  confidence_interval(r15.line_NR_allo_tokenized_txt_15)]
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
    [avg_occupancy_NR_allo_jpg,            avg_occupancy_NR_allo_jpg_6,            avg_occupancy_NR_allo_jpg_15],
    [avg_occupancy_NR_allo_json,           avg_occupancy_NR_allo_json_6,           avg_occupancy_NR_allo_json_15],
    [avg_occupancy_NR_allo_tokenized_txt,  avg_occupancy_NR_allo_tokenized_txt_6,  avg_occupancy_NR_allo_tokenized_txt_15],
    [avg_occupancy_NR_allo_ascii_txt,      avg_occupancy_NR_allo_ascii_txt_6,      avg_occupancy_NR_allo_ascii_txt_15]
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
    [confidence_interval(r3.occupancy_NR_allo_adj_json_3),       confidence_interval(r6.occupancy_NR_allo_adj_json_6),       confidence_interval(r15.occupancy_NR_allo_adj_json_15)],
    [confidence_interval(r3.occupancy_NR_allo_adj_txt_3),        confidence_interval(r6.occupancy_NR_allo_adj_txt_6),        confidence_interval(r15.occupancy_NR_allo_adj_txt_15)],
    [confidence_interval(r3.occupancy_NR_allo_jpg_3),            confidence_interval(r6.occupancy_NR_allo_jpg_6),            confidence_interval(r15.occupancy_NR_allo_jpg_15)],
    [confidence_interval(r3.occupancy_NR_allo_json_3),           confidence_interval(r6.occupancy_NR_allo_json_6),           confidence_interval(r15.occupancy_NR_allo_json_15)],
    [confidence_interval(r3.occupancy_NR_allo_tokenized_txt_3),  confidence_interval(r6.occupancy_NR_allo_tokenized_txt_6),  confidence_interval(r15.occupancy_NR_allo_tokenized_txt_15)],
    [ confidence_interval(r3.occupancy_NR_allo_ascii_txt_3),     confidence_interval(r6.occupancy_NR_allo_ascii_txt_6),      confidence_interval(r15.occupancy_NR_allo_ascii_txt_15)]
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
# Averages and std deviation 3x3
avg_line_NR_ego_adj_json = np.mean(r3.line_NR_ego_adj_json_3)
avg_line_NR_ego_adj_txt = np.mean(r3.line_NR_ego_adj_txt_3)
avg_line_NR_ego_jpg = np.mean(r3.line_NR_ego_jpg_3)
avg_line_NR_ego_json = np.mean(r3.line_NR_ego_json_3)
avg_line_NR_ego_tokenized_txt = np.mean(r3.line_NR_ego_tokenized_txt_3)
avg_occupancy_NR_ego_adj_json = np.mean(r3.occupancy_NR_ego_adj_json_3)
avg_occupancy_NR_ego_adj_txt = np.mean(r3.occupancy_NR_ego_adj_txt_3)
avg_occupancy_NR_ego_ascii_txt = np.mean(r3.occupancy_NR_ego_ascii_txt_3)  
avg_occupancy_NR_ego_jpg = np.mean(r3.occupancy_NR_ego_jpg_3)
avg_occupancy_NR_ego_json = np.mean(r3.occupancy_NR_ego_json_3)
avg_occupancy_NR_ego_tokenized_txt = np.mean(r3.occupancy_NR_ego_tokenized_txt_3)
sd_line_NR_ego_adj_json = np.std(r3.line_NR_ego_adj_json_3)
sd_line_NR_ego_adj_txt = np.std(r3.line_NR_ego_adj_txt_3)
sd_line_NR_ego_jpg = np.std(r3.line_NR_ego_jpg_3)
sd_line_NR_ego_json = np.std(r3.line_NR_ego_json_3)
sd_line_NR_ego_tokenized_txt = np.std(r3.line_NR_ego_tokenized_txt_3)
sd_occupancy_NR_ego_adj_json = np.std(r3.occupancy_NR_ego_adj_json_3)
sd_occupancy_NR_ego_adj_txt = np.std(r3.occupancy_NR_ego_adj_txt_3)
sd_occupancy_NR_ego_ascii_txt = np.std(r3.occupancy_NR_ego_ascii_txt_3)  
sd_occupancy_NR_ego_jpg = np.std(r3.occupancy_NR_ego_jpg_3)
sd_occupancy_NR_ego_json = np.std(r3.occupancy_NR_ego_json_3)
sd_occupancy_NR_ego_tokenized_txt = np.std(r3.occupancy_NR_ego_tokenized_txt_3)
# Averages and std deviation 6x6
avg_line_NR_ego_adj_json_6 = np.mean(r6.line_NR_ego_adj_json_6)
avg_line_NR_ego_adj_txt_6 = np.mean(r6.line_NR_ego_adj_txt_6)
avg_line_NR_ego_jpg_6 = np.mean(r6.line_NR_ego_jpg_6)
avg_line_NR_ego_json_6 = np.mean(r6.line_NR_ego_json_6)
avg_line_NR_ego_tokenized_txt_6 = np.mean(r6.line_NR_ego_tokenized_txt_6)
avg_occupancy_NR_ego_adj_json_6 = np.mean(r6.occupancy_NR_ego_adj_json_6)
avg_occupancy_NR_ego_adj_txt_6 = np.mean(r6.occupancy_NR_ego_adj_txt_6)
avg_occupancy_NR_ego_ascii_txt_6 = np.mean(r6.occupancy_NR_ego_ascii_txt_6)  
avg_occupancy_NR_ego_jpg_6 = np.mean(r6.occupancy_NR_ego_jpg_6)
avg_occupancy_NR_ego_json_6 = np.mean(r6.occupancy_NR_ego_json_6)
avg_occupancy_NR_ego_tokenized_txt_6 = np.mean(r6.occupancy_NR_ego_tokenized_txt_6)
sd_line_NR_ego_adj_json_6 = np.std(r6.line_NR_ego_adj_json_6)
sd_line_NR_ego_adj_txt_6 = np.std(r6.line_NR_ego_adj_txt_6)
sd_line_NR_ego_jpg_6 = np.std(r6.line_NR_ego_jpg_6)
sd_line_NR_ego_json_6 = np.std(r6.line_NR_ego_json_6)
sd_line_NR_ego_tokenized_txt_6 = np.std(r6.line_NR_ego_tokenized_txt_6)
sd_occupancy_NR_ego_adj_json_6 = np.std(r6.occupancy_NR_ego_adj_json_6)
sd_occupancy_NR_ego_adj_txt_6 = np.std(r6.occupancy_NR_ego_adj_txt_6)
sd_occupancy_NR_ego_ascii_txt_6 = np.std(r6.occupancy_NR_ego_ascii_txt_6)  
sd_occupancy_NR_ego_jpg_6 = np.std(r6.occupancy_NR_ego_jpg_6)
sd_occupancy_NR_ego_json_6 = np.std(r6.occupancy_NR_ego_json_6)
sd_occupancy_NR_ego_tokenized_txt_6 = np.std(r6.occupancy_NR_ego_tokenized_txt_6)
# Averages and std deviation 15x15
avg_line_NR_ego_adj_json_15 = np.mean(r15.line_NR_ego_adj_json_15)
avg_line_NR_ego_adj_txt_15 = np.mean(r15.line_NR_ego_adj_txt_15)
avg_line_NR_ego_jpg_15 = np.mean(r15.line_NR_ego_jpg_15)
avg_line_NR_ego_json_15 = np.mean(r15.line_NR_ego_json_15)
avg_line_NR_ego_tokenized_txt_15 = np.mean(r15.line_NR_ego_tokenized_txt_15)
avg_occupancy_NR_ego_adj_json_15 = np.mean(r15.occupancy_NR_ego_adj_json_15)
avg_occupancy_NR_ego_adj_txt_15 = np.mean(r15.occupancy_NR_ego_adj_txt_15)
avg_occupancy_NR_ego_ascii_txt_15 = np.mean(r15.occupancy_NR_ego_ascii_txt_15)  
avg_occupancy_NR_ego_jpg_15 = np.mean(r15.occupancy_NR_ego_jpg_15)
avg_occupancy_NR_ego_json_15 = np.mean(r15.occupancy_NR_ego_json_15)
avg_occupancy_NR_ego_tokenized_txt_15 = np.mean(r15.occupancy_NR_ego_tokenized_txt_15)
sd_line_NR_ego_adj_json_15 = np.std(r15.line_NR_ego_adj_json_15)
sd_line_NR_ego_adj_txt_15 = np.std(r15.line_NR_ego_adj_txt_15)
sd_line_NR_ego_jpg_15 = np.std(r15.line_NR_ego_jpg_15)
sd_line_NR_ego_json_15 = np.std(r15.line_NR_ego_json_15)
sd_line_NR_ego_tokenized_txt_15 = np.std(r15.line_NR_ego_tokenized_txt_15)
sd_occupancy_NR_ego_adj_json_15 = np.std(r15.occupancy_NR_ego_adj_json_15)
sd_occupancy_NR_ego_adj_txt_15 = np.std(r15.occupancy_NR_ego_adj_txt_15)
sd_occupancy_NR_ego_ascii_txt_15 = np.std(r15.occupancy_NR_ego_ascii_txt_15)  
sd_occupancy_NR_ego_jpg_15 = np.std(r15.occupancy_NR_ego_jpg_15)
sd_occupancy_NR_ego_json_15 = np.std(r15.occupancy_NR_ego_json_15)
sd_occupancy_NR_ego_tokenized_txt_15 = np.std(r15.occupancy_NR_ego_tokenized_txt_15)


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
    [confidence_interval(r3.line_NR_ego_adj_json_3),       confidence_interval(r6.line_NR_ego_adj_json_6),       confidence_interval(r15.line_NR_ego_adj_json_15)],
    [confidence_interval(r3.line_NR_ego_adj_txt_3),        confidence_interval(r6.line_NR_ego_adj_txt_6),        confidence_interval(r15.line_NR_ego_adj_txt_15)],
    [confidence_interval(r3.line_NR_ego_jpg_3),            confidence_interval(r6.line_NR_ego_jpg_6),            confidence_interval(r15.line_NR_ego_jpg_15)],
    [confidence_interval(r3.line_NR_ego_json_3),           confidence_interval(r6.line_NR_ego_json_6),           confidence_interval(r15.line_NR_ego_json_15)],
    [confidence_interval(r3.line_NR_ego_tokenized_txt_3),  confidence_interval(r6.line_NR_ego_tokenized_txt_6),  confidence_interval(r15.line_NR_ego_tokenized_txt_15)]
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
    [avg_occupancy_NR_ego_jpg,            avg_occupancy_NR_ego_jpg_6,            avg_occupancy_NR_ego_jpg_15],
    [avg_occupancy_NR_ego_json,           avg_occupancy_NR_ego_json_6,           avg_occupancy_NR_ego_json_15],
    [avg_occupancy_NR_ego_tokenized_txt,  avg_occupancy_NR_ego_tokenized_txt_6,  avg_occupancy_NR_ego_tokenized_txt_15],
    [avg_occupancy_NR_ego_ascii_txt,      avg_occupancy_NR_ego_ascii_txt_6,      avg_occupancy_NR_ego_ascii_txt_15]
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
    [confidence_interval(r3.occupancy_NR_ego_adj_json_3),       confidence_interval(r6.occupancy_NR_ego_adj_json_6),       confidence_interval(r15.occupancy_NR_ego_adj_json_15)],
    [confidence_interval(r3.occupancy_NR_ego_adj_txt_3),        confidence_interval(r6.occupancy_NR_ego_adj_txt_6),        confidence_interval(r15.occupancy_NR_ego_adj_txt_15)],
    [confidence_interval(r3.occupancy_NR_ego_jpg_3),            confidence_interval(r6.occupancy_NR_ego_jpg_6),            confidence_interval(r15.occupancy_NR_ego_jpg_15)],
    [confidence_interval(r3.occupancy_NR_ego_json_3),           confidence_interval(r6.occupancy_NR_ego_json_6),           confidence_interval(r15.occupancy_NR_ego_json_15)],
    [confidence_interval(r3.occupancy_NR_ego_tokenized_txt_3),  confidence_interval(r6.occupancy_NR_ego_tokenized_txt_6),  confidence_interval(r15.occupancy_NR_ego_tokenized_txt_15)],
    [ confidence_interval(r3.occupancy_NR_ego_ascii_txt_3),     confidence_interval(r6.occupancy_NR_ego_ascii_txt_6),      confidence_interval(r15.occupancy_NR_ego_ascii_txt_15)]
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
# Averages and std deviation 3x3
avg_line_R_coords_adj_json = np.mean(r3.line_R_coords_adj_json_3)
avg_line_R_coords_adj_txt = np.mean(r3.line_R_coords_adj_txt_3)
avg_line_R_coords_jpg = np.mean(r3.line_R_coords_jpg_3)
avg_line_R_coords_json = np.mean(r3.line_R_coords_json_3)
avg_line_R_coords_tokenized_txt = np.mean(r3.line_R_coords_tokenized_txt_3)
avg_occupancy_R_coords_adj_json = np.mean(r3.occupancy_R_coords_adj_json_3)
avg_occupancy_R_coords_adj_txt = np.mean(r3.occupancy_R_coords_adj_txt_3)
avg_occupancy_R_coords_ascii_txt = np.mean(r3.occupancy_R_coords_ascii_txt_3)  
avg_occupancy_R_coords_jpg = np.mean(r3.occupancy_R_coords_jpg_3)
avg_occupancy_R_coords_json = np.mean(r3.occupancy_R_coords_json_3)
avg_occupancy_R_coords_tokenized_txt = np.mean(r3.occupancy_R_coords_tokenized_txt_3)
sd_line_R_coords_adj_json = np.std(r3.line_R_coords_adj_json_3)
sd_line_R_coords_adj_txt = np.std(r3.line_R_coords_adj_txt_3)
sd_line_R_coords_jpg = np.std(r3.line_R_coords_jpg_3)
sd_line_R_coords_json = np.std(r3.line_R_coords_json_3)
sd_line_R_coords_tokenized_txt = np.std(r3.line_R_coords_tokenized_txt_3)
sd_occupancy_R_coords_adj_json = np.std(r3.occupancy_R_coords_adj_json_3)
sd_occupancy_R_coords_adj_txt = np.std(r3.occupancy_R_coords_adj_txt_3)
sd_occupancy_R_coords_ascii_txt = np.std(r3.occupancy_R_coords_ascii_txt_3)  
sd_occupancy_R_coords_jpg = np.std(r3.occupancy_R_coords_jpg_3)
sd_occupancy_R_coords_json = np.std(r3.occupancy_R_coords_json_3)
sd_occupancy_R_coords_tokenized_txt = np.std(r3.occupancy_R_coords_tokenized_txt_3)
# Averages and std deviation 6x6
avg_line_R_coords_adj_json_6 = np.mean(r6.line_R_coords_adj_json_6)
avg_line_R_coords_adj_txt_6 = np.mean(r6.line_R_coords_adj_txt_6)
avg_line_R_coords_jpg_6 = np.mean(r6.line_R_coords_jpg_6)
avg_line_R_coords_json_6 = np.mean(r6.line_R_coords_json_6)
avg_line_R_coords_tokenized_txt_6 = np.mean(r6.line_R_coords_tokenized_txt_6)
avg_occupancy_R_coords_adj_json_6 = np.mean(r6.occupancy_R_coords_adj_json_6)
avg_occupancy_R_coords_adj_txt_6 = np.mean(r6.occupancy_R_coords_adj_txt_6)
avg_occupancy_R_coords_ascii_txt_6 = np.mean(r6.occupancy_R_coords_ascii_txt_6)  
avg_occupancy_R_coords_jpg_6 = np.mean(r6.occupancy_R_coords_jpg_6)
avg_occupancy_R_coords_json_6 = np.mean(r6.occupancy_R_coords_json_6)
avg_occupancy_R_coords_tokenized_txt_6 = np.mean(r6.occupancy_R_coords_tokenized_txt_6)
sd_line_R_coords_adj_json_6 = np.std(r6.line_R_coords_adj_json_6)
sd_line_R_coords_adj_txt_6 = np.std(r6.line_R_coords_adj_txt_6)
sd_line_R_coords_jpg_6 = np.std(r6.line_R_coords_jpg_6)
sd_line_R_coords_json_6 = np.std(r6.line_R_coords_json_6)
sd_line_R_coords_tokenized_txt_6 = np.std(r6.line_R_coords_tokenized_txt_6)
sd_occupancy_R_coords_adj_json_6 = np.std(r6.occupancy_R_coords_adj_json_6)
sd_occupancy_R_coords_adj_txt_6 = np.std(r6.occupancy_R_coords_adj_txt_6)
sd_occupancy_R_coords_ascii_txt_6 = np.std(r6.occupancy_R_coords_ascii_txt_6)  
sd_occupancy_R_coords_jpg_6 = np.std(r6.occupancy_R_coords_jpg_6)
sd_occupancy_R_coords_json_6 = np.std(r6.occupancy_R_coords_json_6)
sd_occupancy_R_coords_tokenized_txt_6 = np.std(r6.occupancy_R_coords_tokenized_txt_6)
# Averages and std deviation 15x15
avg_line_R_coords_adj_json_15 = np.mean(r15.line_R_coords_adj_json_15)
avg_line_R_coords_adj_txt_15 = np.mean(r15.line_R_coords_adj_txt_15)
avg_line_R_coords_jpg_15 = np.mean(r15.line_R_coords_jpg_15)
avg_line_R_coords_json_15 = np.mean(r15.line_R_coords_json_15)
avg_line_R_coords_tokenized_txt_15 = np.mean(r15.line_R_coords_tokenized_txt_15)
avg_occupancy_R_coords_adj_json_15 = np.mean(r15.occupancy_R_coords_adj_json_15)
avg_occupancy_R_coords_adj_txt_15 = np.mean(r15.occupancy_R_coords_adj_txt_15)
avg_occupancy_R_coords_ascii_txt_15 = np.mean(r15.occupancy_R_coords_ascii_txt_15)  
avg_occupancy_R_coords_jpg_15 = np.mean(r15.occupancy_R_coords_jpg_15)
avg_occupancy_R_coords_json_15 = np.mean(r15.occupancy_R_coords_json_15)
avg_occupancy_R_coords_tokenized_txt_15 = np.mean(r15.occupancy_R_coords_tokenized_txt_15)
sd_line_R_coords_adj_json_15 = np.std(r15.line_R_coords_adj_json_15)
sd_line_R_coords_adj_txt_15 = np.std(r15.line_R_coords_adj_txt_15)
sd_line_R_coords_jpg_15 = np.std(r15.line_R_coords_jpg_15)
sd_line_R_coords_json_15 = np.std(r15.line_R_coords_json_15)
sd_line_R_coords_tokenized_txt_15 = np.std(r15.line_R_coords_tokenized_txt_15)
sd_occupancy_R_coords_adj_json_15 = np.std(r15.occupancy_R_coords_adj_json_15)
sd_occupancy_R_coords_adj_txt_15 = np.std(r15.occupancy_R_coords_adj_txt_15)
sd_occupancy_R_coords_ascii_txt_15 = np.std(r15.occupancy_R_coords_ascii_txt_15)  
sd_occupancy_R_coords_jpg_15 = np.std(r15.occupancy_R_coords_jpg_15)
sd_occupancy_R_coords_json_15 = np.std(r15.occupancy_R_coords_json_15)
sd_occupancy_R_coords_tokenized_txt_15 = np.std(r15.occupancy_R_coords_tokenized_txt_15)

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
    [confidence_interval(r3.line_R_coords_adj_json_3),       confidence_interval(r6.line_R_coords_adj_json_6),       confidence_interval(r15.line_R_coords_adj_json_15)],
    [confidence_interval(r3.line_R_coords_adj_txt_3),        confidence_interval(r6.line_R_coords_adj_txt_6),        confidence_interval(r15.line_R_coords_adj_txt_15)],
    [confidence_interval(r3.line_R_coords_jpg_3),            confidence_interval(r6.line_R_coords_jpg_6),            confidence_interval(r15.line_R_coords_jpg_15)],
    [confidence_interval(r3.line_R_coords_json_3),           confidence_interval(r6.line_R_coords_json_6),           confidence_interval(r15.line_R_coords_json_15)],
    [confidence_interval(r3.line_R_coords_tokenized_txt_3),  confidence_interval(r6.line_R_coords_tokenized_txt_6),  confidence_interval(r15.line_R_coords_tokenized_txt_15)]
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
    [avg_occupancy_R_coords_jpg,            avg_occupancy_R_coords_jpg_6,            avg_occupancy_R_coords_jpg_15],
    [avg_occupancy_R_coords_json,           avg_occupancy_R_coords_json_6,           avg_occupancy_R_coords_json_15],
    [avg_occupancy_R_coords_tokenized_txt,  avg_occupancy_R_coords_tokenized_txt_6,  avg_occupancy_R_coords_tokenized_txt_15],
    [avg_occupancy_R_coords_ascii_txt,      avg_occupancy_R_coords_ascii_txt_6,      avg_occupancy_R_coords_ascii_txt_15]
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
    [confidence_interval(r3.occupancy_R_coords_adj_json_3),       confidence_interval(r6.occupancy_R_coords_adj_json_6),       confidence_interval(r15.occupancy_R_coords_adj_json_15)],
    [confidence_interval(r3.occupancy_R_coords_adj_txt_3),        confidence_interval(r6.occupancy_R_coords_adj_txt_6),        confidence_interval(r15.occupancy_R_coords_adj_txt_15)],
    [confidence_interval(r3.occupancy_R_coords_jpg_3),            confidence_interval(r6.occupancy_R_coords_jpg_6),            confidence_interval(r15.occupancy_R_coords_jpg_15)],
    [confidence_interval(r3.occupancy_R_coords_json_3),           confidence_interval(r6.occupancy_R_coords_json_6),           confidence_interval(r15.occupancy_R_coords_json_15)],
    [confidence_interval(r3.occupancy_R_coords_tokenized_txt_3),  confidence_interval(r6.occupancy_R_coords_tokenized_txt_6),  confidence_interval(r15.occupancy_R_coords_tokenized_txt_15)],
    [ confidence_interval(r3.occupancy_R_coords_ascii_txt_3),     confidence_interval(r6.occupancy_R_coords_ascii_txt_6),      confidence_interval(r15.occupancy_R_coords_ascii_txt_15)]
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
# Averages and std deviation 3x3
avg_line_R_allo_adj_json = np.mean(r3.line_R_allo_adj_json_3)
avg_line_R_allo_adj_txt = np.mean(r3.line_R_allo_adj_txt_3)
avg_line_R_allo_jpg = np.mean(r3.line_R_allo_jpg_3)
avg_line_R_allo_json = np.mean(r3.line_R_allo_json_3)
avg_line_R_allo_tokenized_txt = np.mean(r3.line_R_allo_tokenized_txt_3)
avg_occupancy_R_allo_adj_json = np.mean(r3.occupancy_R_allo_adj_json_3)
avg_occupancy_R_allo_adj_txt = np.mean(r3.occupancy_R_allo_adj_txt_3)
avg_occupancy_R_allo_ascii_txt = np.mean(r3.occupancy_R_allo_ascii_txt_3)  
avg_occupancy_R_allo_jpg = np.mean(r3.occupancy_R_allo_jpg_3)
avg_occupancy_R_allo_json = np.mean(r3.occupancy_R_allo_json_3)
avg_occupancy_R_allo_tokenized_txt = np.mean(r3.occupancy_R_allo_tokenized_txt_3)
sd_line_R_allo_adj_json = np.std(r3.line_R_allo_adj_json_3)
sd_line_R_allo_adj_txt = np.std(r3.line_R_allo_adj_txt_3)
sd_line_R_allo_jpg = np.std(r3.line_R_allo_jpg_3)
sd_line_R_allo_json = np.std(r3.line_R_allo_json_3)
sd_line_R_allo_tokenized_txt = np.std(r3.line_R_allo_tokenized_txt_3)
sd_occupancy_R_allo_adj_json = np.std(r3.occupancy_R_allo_adj_json_3)
sd_occupancy_R_allo_adj_txt = np.std(r3.occupancy_R_allo_adj_txt_3)
sd_occupancy_R_allo_ascii_txt = np.std(r3.occupancy_R_allo_ascii_txt_3)  
sd_occupancy_R_allo_jpg = np.std(r3.occupancy_R_allo_jpg_3)
sd_occupancy_R_allo_json = np.std(r3.occupancy_R_allo_json_3)
sd_occupancy_R_allo_tokenized_txt = np.std(r3.occupancy_R_allo_tokenized_txt_3)
# Averages and std deviation 6x6
avg_line_R_allo_adj_json_6 = np.mean(r6.line_R_allo_adj_json_6)
avg_line_R_allo_adj_txt_6 = np.mean(r6.line_R_allo_adj_txt_6)
avg_line_R_allo_jpg_6 = np.mean(r6.line_R_allo_jpg_6)
avg_line_R_allo_json_6 = np.mean(r6.line_R_allo_json_6)
avg_line_R_allo_tokenized_txt_6 = np.mean(r6.line_R_allo_tokenized_txt_6)
avg_occupancy_R_allo_adj_json_6 = np.mean(r6.occupancy_R_allo_adj_json_6)
avg_occupancy_R_allo_adj_txt_6 = np.mean(r6.occupancy_R_allo_adj_txt_6)
avg_occupancy_R_allo_ascii_txt_6 = np.mean(r6.occupancy_R_allo_ascii_txt_6)  
avg_occupancy_R_allo_jpg_6 = np.mean(r6.occupancy_R_allo_jpg_6)
avg_occupancy_R_allo_json_6 = np.mean(r6.occupancy_R_allo_json_6)
avg_occupancy_R_allo_tokenized_txt_6 = np.mean(r6.occupancy_R_allo_tokenized_txt_6)
sd_line_R_allo_adj_json_6 = np.std(r6.line_R_allo_adj_json_6)
sd_line_R_allo_adj_txt_6 = np.std(r6.line_R_allo_adj_txt_6)
sd_line_R_allo_jpg_6 = np.std(r6.line_R_allo_jpg_6)
sd_line_R_allo_json_6 = np.std(r6.line_R_allo_json_6)
sd_line_R_allo_tokenized_txt_6 = np.std(r6.line_R_allo_tokenized_txt_6)
sd_occupancy_R_allo_adj_json_6 = np.std(r6.occupancy_R_allo_adj_json_6)
sd_occupancy_R_allo_adj_txt_6 = np.std(r6.occupancy_R_allo_adj_txt_6)
sd_occupancy_R_allo_ascii_txt_6 = np.std(r6.occupancy_R_allo_ascii_txt_6)  
sd_occupancy_R_allo_jpg_6 = np.std(r6.occupancy_R_allo_jpg_6)
sd_occupancy_R_allo_json_6 = np.std(r6.occupancy_R_allo_json_6)
sd_occupancy_R_allo_tokenized_txt_6 = np.std(r6.occupancy_R_allo_tokenized_txt_6)
# Averages and std deviation 15x15
avg_line_R_allo_adj_json_15 = np.mean(r15.line_R_allo_adj_json_15)
avg_line_R_allo_adj_txt_15 = np.mean(r15.line_R_allo_adj_txt_15)
avg_line_R_allo_jpg_15 = np.mean(r15.line_R_allo_jpg_15)
avg_line_R_allo_json_15 = np.mean(r15.line_R_allo_json_15)
avg_line_R_allo_tokenized_txt_15 = np.mean(r15.line_R_allo_tokenized_txt_15)
avg_occupancy_R_allo_adj_json_15 = np.mean(r15.occupancy_R_allo_adj_json_15)
avg_occupancy_R_allo_adj_txt_15 = np.mean(r15.occupancy_R_allo_adj_txt_15)
avg_occupancy_R_allo_ascii_txt_15 = np.mean(r15.occupancy_R_allo_ascii_txt_15)  
avg_occupancy_R_allo_jpg_15 = np.mean(r15.occupancy_R_allo_jpg_15)
avg_occupancy_R_allo_json_15 = np.mean(r15.occupancy_R_allo_json_15)
avg_occupancy_R_allo_tokenized_txt_15 = np.mean(r15.occupancy_R_allo_tokenized_txt_15)
sd_line_R_allo_adj_json_15 = np.std(r15.line_R_allo_adj_json_15)
sd_line_R_allo_adj_txt_15 = np.std(r15.line_R_allo_adj_txt_15)
sd_line_R_allo_jpg_15 = np.std(r15.line_R_allo_jpg_15)
sd_line_R_allo_json_15 = np.std(r15.line_R_allo_json_15)
sd_line_R_allo_tokenized_txt_15 = np.std(r15.line_R_allo_tokenized_txt_15)
sd_occupancy_R_allo_adj_json_15 = np.std(r15.occupancy_R_allo_adj_json_15)
sd_occupancy_R_allo_adj_txt_15 = np.std(r15.occupancy_R_allo_adj_txt_15)
sd_occupancy_R_allo_ascii_txt_15 = np.std(r15.occupancy_R_allo_ascii_txt_15)  
sd_occupancy_R_allo_jpg_15 = np.std(r15.occupancy_R_allo_jpg_15)
sd_occupancy_R_allo_json_15 = np.std(r15.occupancy_R_allo_json_15)
sd_occupancy_R_allo_tokenized_txt_15 = np.std(r15.occupancy_R_allo_tokenized_txt_15)

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
    [confidence_interval(r3.line_R_allo_adj_json_3),       confidence_interval(r6.line_R_allo_adj_json_6),       confidence_interval(r15.line_R_allo_adj_json_15)],
    [confidence_interval(r3.line_R_allo_adj_txt_3),        confidence_interval(r6.line_R_allo_adj_txt_6),        confidence_interval(r15.line_R_allo_adj_txt_15)],
    [confidence_interval(r3.line_R_allo_jpg_3),            confidence_interval(r6.line_R_allo_jpg_6),            confidence_interval(r15.line_R_allo_jpg_15)],
    [confidence_interval(r3.line_R_allo_json_3),           confidence_interval(r6.line_R_allo_json_6),           confidence_interval(r15.line_R_allo_json_15)],
    [confidence_interval(r3.line_R_allo_tokenized_txt_3),  confidence_interval(r6.line_R_allo_tokenized_txt_6),  confidence_interval(r15.line_R_allo_tokenized_txt_15)]
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
    [avg_occupancy_R_allo_jpg,            avg_occupancy_R_allo_jpg_6,            avg_occupancy_R_allo_jpg_15],
    [avg_occupancy_R_allo_json,           avg_occupancy_R_allo_json_6,           avg_occupancy_R_allo_json_15],
    [avg_occupancy_R_allo_tokenized_txt,  avg_occupancy_R_allo_tokenized_txt_6,  avg_occupancy_R_allo_tokenized_txt_15],
    [avg_occupancy_R_allo_ascii_txt,      avg_occupancy_R_allo_ascii_txt_6,      avg_occupancy_R_allo_ascii_txt_15]
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
    [confidence_interval(r3.occupancy_R_allo_adj_json_3),       confidence_interval(r6.occupancy_R_allo_adj_json_6),       confidence_interval(r15.occupancy_R_allo_adj_json_15)],
    [confidence_interval(r3.occupancy_R_allo_adj_txt_3),        confidence_interval(r6.occupancy_R_allo_adj_txt_6),        confidence_interval(r15.occupancy_R_allo_adj_txt_15)],
    [confidence_interval(r3.occupancy_R_allo_jpg_3),            confidence_interval(r6.occupancy_R_allo_jpg_6),            confidence_interval(r15.occupancy_R_allo_jpg_15)],
    [confidence_interval(r3.occupancy_R_allo_json_3),           confidence_interval(r6.occupancy_R_allo_json_6),           confidence_interval(r15.occupancy_R_allo_json_15)],
    [confidence_interval(r3.occupancy_R_allo_tokenized_txt_3),  confidence_interval(r6.occupancy_R_allo_tokenized_txt_6),  confidence_interval(r15.occupancy_R_allo_tokenized_txt_15)],
    [ confidence_interval(r3.occupancy_R_allo_ascii_txt_3),     confidence_interval(r6.occupancy_R_allo_ascii_txt_6),      confidence_interval(r15.occupancy_R_allo_ascii_txt_15)]
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
# Averages and std deviation 3x3
avg_line_R_ego_adj_json = np.mean(r3.line_R_ego_adj_json_3)
avg_line_R_ego_adj_txt = np.mean(r3.line_R_ego_adj_txt_3)
avg_line_R_ego_jpg = np.mean(r3.line_R_ego_jpg_3)
avg_line_R_ego_json = np.mean(r3.line_R_ego_json_3)
avg_line_R_ego_tokenized_txt = np.mean(r3.line_R_ego_tokenized_txt_3)
avg_occupancy_R_ego_adj_json = np.mean(r3.occupancy_R_ego_adj_json_3)
avg_occupancy_R_ego_adj_txt = np.mean(r3.occupancy_R_ego_adj_txt_3)
avg_occupancy_R_ego_ascii_txt = np.mean(r3.occupancy_R_ego_ascii_txt_3)  
avg_occupancy_R_ego_jpg = np.mean(r3.occupancy_R_ego_jpg_3)
avg_occupancy_R_ego_json = np.mean(r3.occupancy_R_ego_json_3)
avg_occupancy_R_ego_tokenized_txt = np.mean(r3.occupancy_R_ego_tokenized_txt_3)
sd_line_R_ego_adj_json = np.std(r3.line_R_ego_adj_json_3)
sd_line_R_ego_adj_txt = np.std(r3.line_R_ego_adj_txt_3)
sd_line_R_ego_jpg = np.std(r3.line_R_ego_jpg_3)
sd_line_R_ego_json = np.std(r3.line_R_ego_json_3)
sd_line_R_ego_tokenized_txt = np.std(r3.line_R_ego_tokenized_txt_3)
sd_occupancy_R_ego_adj_json = np.std(r3.occupancy_R_ego_adj_json_3)
sd_occupancy_R_ego_adj_txt = np.std(r3.occupancy_R_ego_adj_txt_3)
sd_occupancy_R_ego_ascii_txt = np.std(r3.occupancy_R_ego_ascii_txt_3)  
sd_occupancy_R_ego_jpg = np.std(r3.occupancy_R_ego_jpg_3)
sd_occupancy_R_ego_json = np.std(r3.occupancy_R_ego_json_3)
sd_occupancy_R_ego_tokenized_txt = np.std(r3.occupancy_R_ego_tokenized_txt_3)
# Averages and std deviation 6x6
avg_line_R_ego_adj_json_6 = np.mean(r6.line_R_ego_adj_json_6)
avg_line_R_ego_adj_txt_6 = np.mean(r6.line_R_ego_adj_txt_6)
avg_line_R_ego_jpg_6 = np.mean(r6.line_R_ego_jpg_6)
avg_line_R_ego_json_6 = np.mean(r6.line_R_ego_json_6)
avg_line_R_ego_tokenized_txt_6 = np.mean(r6.line_R_ego_tokenized_txt_6)
avg_occupancy_R_ego_adj_json_6 = np.mean(r6.occupancy_R_ego_adj_json_6)
avg_occupancy_R_ego_adj_txt_6 = np.mean(r6.occupancy_R_ego_adj_txt_6)
avg_occupancy_R_ego_ascii_txt_6 = np.mean(r6.occupancy_R_ego_ascii_txt_6)  
avg_occupancy_R_ego_jpg_6 = np.mean(r6.occupancy_R_ego_jpg_6)
avg_occupancy_R_ego_json_6 = np.mean(r6.occupancy_R_ego_json_6)
avg_occupancy_R_ego_tokenized_txt_6 = np.mean(r6.occupancy_R_ego_tokenized_txt_6)
sd_line_R_ego_adj_json_6 = np.std(r6.line_R_ego_adj_json_6)
sd_line_R_ego_adj_txt_6 = np.std(r6.line_R_ego_adj_txt_6)
sd_line_R_ego_jpg_6 = np.std(r6.line_R_ego_jpg_6)
sd_line_R_ego_json_6 = np.std(r6.line_R_ego_json_6)
sd_line_R_ego_tokenized_txt_6 = np.std(r6.line_R_ego_tokenized_txt_6)
sd_occupancy_R_ego_adj_json_6 = np.std(r6.occupancy_R_ego_adj_json_6)
sd_occupancy_R_ego_adj_txt_6 = np.std(r6.occupancy_R_ego_adj_txt_6)
sd_occupancy_R_ego_ascii_txt_6 = np.std(r6.occupancy_R_ego_ascii_txt_6)  
sd_occupancy_R_ego_jpg_6 = np.std(r6.occupancy_R_ego_jpg_6)
sd_occupancy_R_ego_json_6 = np.std(r6.occupancy_R_ego_json_6)
sd_occupancy_R_ego_tokenized_txt_6 = np.std(r6.occupancy_R_ego_tokenized_txt_6)
# Averages and std deviation 15x15
avg_line_R_ego_adj_json_15 = np.mean(r15.line_R_ego_adj_json_15)
avg_line_R_ego_adj_txt_15 = np.mean(r15.line_R_ego_adj_txt_15)
avg_line_R_ego_jpg_15 = np.mean(r15.line_R_ego_jpg_15)
avg_line_R_ego_json_15 = np.mean(r15.line_R_ego_json_15)
avg_line_R_ego_tokenized_txt_15 = np.mean(r15.line_R_ego_tokenized_txt_15)
avg_occupancy_R_ego_adj_json_15 = np.mean(r15.occupancy_R_ego_adj_json_15)
avg_occupancy_R_ego_adj_txt_15 = np.mean(r15.occupancy_R_ego_adj_txt_15)
avg_occupancy_R_ego_ascii_txt_15 = np.mean(r15.occupancy_R_ego_ascii_txt_15)  
avg_occupancy_R_ego_jpg_15 = np.mean(r15.occupancy_R_ego_jpg_15)
avg_occupancy_R_ego_json_15 = np.mean(r15.occupancy_R_ego_json_15)
avg_occupancy_R_ego_tokenized_txt_15 = np.mean(r15.occupancy_R_ego_tokenized_txt_15)
sd_line_R_ego_adj_json_15 = np.std(r15.line_R_ego_adj_json_15)
sd_line_R_ego_adj_txt_15 = np.std(r15.line_R_ego_adj_txt_15)
sd_line_R_ego_jpg_15 = np.std(r15.line_R_ego_jpg_15)
sd_line_R_ego_json_15 = np.std(r15.line_R_ego_json_15)
sd_line_R_ego_tokenized_txt_15 = np.std(r15.line_R_ego_tokenized_txt_15)
sd_occupancy_R_ego_adj_json_15 = np.std(r15.occupancy_R_ego_adj_json_15)
sd_occupancy_R_ego_adj_txt_15 = np.std(r15.occupancy_R_ego_adj_txt_15)
sd_occupancy_R_ego_ascii_txt_15 = np.std(r15.occupancy_R_ego_ascii_txt_15)  
sd_occupancy_R_ego_jpg_15 = np.std(r15.occupancy_R_ego_jpg_15)
sd_occupancy_R_ego_json_15 = np.std(r15.occupancy_R_ego_json_15)
sd_occupancy_R_ego_tokenized_txt_15 = np.std(r15.occupancy_R_ego_tokenized_txt_15)

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
    [confidence_interval(r3.line_R_ego_adj_json_3),       confidence_interval(r6.line_R_ego_adj_json_6),       confidence_interval(r15.line_R_ego_adj_json_15)],
    [confidence_interval(r3.line_R_ego_adj_txt_3),        confidence_interval(r6.line_R_ego_adj_txt_6),        confidence_interval(r15.line_R_ego_adj_txt_15)],
    [confidence_interval(r3.line_R_ego_jpg_3),            confidence_interval(r6.line_R_ego_jpg_6),            confidence_interval(r15.line_R_ego_jpg_15)],
    [confidence_interval(r3.line_R_ego_json_3),           confidence_interval(r6.line_R_ego_json_6),           confidence_interval(r15.line_R_ego_json_15)],
    [confidence_interval(r3.line_R_ego_tokenized_txt_3),  confidence_interval(r6.line_R_ego_tokenized_txt_6),  confidence_interval(r15.line_R_ego_tokenized_txt_15)]
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
    [avg_occupancy_R_ego_jpg,            avg_occupancy_R_ego_jpg_6,            avg_occupancy_R_ego_jpg_15],
    [avg_occupancy_R_ego_json,           avg_occupancy_R_ego_json_6,           avg_occupancy_R_ego_json_15],
    [avg_occupancy_R_ego_tokenized_txt,  avg_occupancy_R_ego_tokenized_txt_6,  avg_occupancy_R_ego_tokenized_txt_15],
    [avg_occupancy_R_ego_ascii_txt,      avg_occupancy_R_ego_ascii_txt_6,      avg_occupancy_R_ego_ascii_txt_15]
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
    [confidence_interval(r3.occupancy_R_ego_adj_json_3),       confidence_interval(r6.occupancy_R_ego_adj_json_6),       confidence_interval(r15.occupancy_R_ego_adj_json_15)],
    [confidence_interval(r3.occupancy_R_ego_adj_txt_3),        confidence_interval(r6.occupancy_R_ego_adj_txt_6),        confidence_interval(r15.occupancy_R_ego_adj_txt_15)],
    [confidence_interval(r3.occupancy_R_ego_jpg_3),            confidence_interval(r6.occupancy_R_ego_jpg_6),            confidence_interval(r15.occupancy_R_ego_jpg_15)],
    [confidence_interval(r3.occupancy_R_ego_json_3),           confidence_interval(r6.occupancy_R_ego_json_6),           confidence_interval(r15.occupancy_R_ego_json_15)],
    [confidence_interval(r3.occupancy_R_ego_tokenized_txt_3),  confidence_interval(r6.occupancy_R_ego_tokenized_txt_6),  confidence_interval(r15.occupancy_R_ego_tokenized_txt_15)],
    [ confidence_interval(r3.occupancy_R_ego_ascii_txt_3),     confidence_interval(r6.occupancy_R_ego_ascii_txt_6),      confidence_interval(r15.occupancy_R_ego_ascii_txt_15)]
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


# --- I dont remember what this does- i think it plots all 6 acc plots in 1 fig but with lots of legends ---------------------

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

# ----- use this for plotting accuracy: Plottoing all 6 accuracy plots in one figure ------------------

# 1. Define the Legend Labels
# single_legend = [
#     'Adjacency JSON - Gemini 2.5 Flash-Lite', 
#     'Adjacency Text - Gemini 2.5 Flash-Lite', 
#     'JPG - Gemini 2.5 Flash-Lite', 
#     'JSON - Gemini 2.5 Flash-Lite', 
#     'Tokenized - Gemini 2.5 Flash-Lite', 
#     'ASCII - Gemini 2.5 Flash-Lite', 
#     'Adjacency JSON - Gemini 2.5 Pro', 
#     'Adjacency Text - Gemini 2.5 Pro', 
#     'JPG - Gemini 2.5 Pro', 
#     'JSON - Gemini 2.5 Pro', 
#     'Tokenized - Gemini 2.5 Pro', 
#     'ASCII - Gemini 2.5 Pro'
# ]

# 2. Organize Data into Groups for the 6 Subplots
# Structure: (Means_NR, Means_R, Err_NR, Err_R, Title)
# NR = Non-Reasoning (Solid), R = Reasoning (Dotted)
plot_configs = [
    # Top-Left: line coords
    (means_line_NR_coords, means_line_R_coords, 
     error_line_NR_coords, error_line_R_coords, 
     "Line-Walled Maze, Coordinates Output"),
    
    # Top-Middle: line allo
    (means_line_NR_allo, means_line_R_allo, 
     error_line_NR_allo, error_line_R_allo, 
     "Line-Walled Maze, Allocentric Output"),
    
    # Top-Right: line ego
    (means_line_NR_ego, means_line_R_ego, 
     error_line_NR_ego, error_line_R_ego, 
     "Line-Walled Maze, Egocentric Output"),
    
    # Bottom-Left: occupancy coords
    (means_occ_NR_coords, means_occ_R_coords, 
     error_occupancy_NR_coords, error_occupancy_R_coords, 
     "Occupancy Grid Maze, Coordinates Output"),
    
    # Bottom-Middle: occupancy allo
    (means_occ_NR_allo, means_occ_R_allo, 
     error_occupancy_NR_allo, error_occupancy_R_allo, 
     "Occupancy Grid Maze, Allocentric Output"),
    
    # Bottom-Right: occupancy ego
    (means_occ_NR_ego, means_occ_R_ego, 
     error_occupancy_NR_ego, error_occupancy_R_ego, 
     "Occupancy Grid Maze, Egocentric Output"),
]

# 3. Setup Plotting Parameters
x_vals = np.arange(3)
x_tick_lbls_line = ["3x3", "6x6", "15x15"] # Complexity levels
x_tick_lbls_occupancy = ["7x7", "13x13", "31x31"] # Complexity levels
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
            # label=single_legend[i],
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
            # label=single_legend[leg_idx],
            color=colors[i],      # Same color as the NR counterpart
            alpha=0.9
        )


    # Formatting
    if idx < 3:
        x_tick_lbls = x_tick_lbls_line
    else:
        x_tick_lbls = x_tick_lbls_occupancy
        ax.set_xlabel("Maze Size")
    ax.set_title(title, fontsize=11)
    ax.set_xticks(x_vals)
    ax.set_xticklabels(x_tick_lbls)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    if idx % 3 == 0:
        ax.set_ylabel("Accuracy (%)")
    


    
    # Save handles from the last plot (Bottom-Right) because it contains all 12 lines
    # if idx == 5:
    #     handles_for_legend, labels_for_legend = ax.get_legend_handles_labels()



plt.suptitle("Accuracy", x=0.9*0.5, fontweight='bold')
# Position the legend within that white space
# legend=fig.legend(
#     handles_for_legend, 
#     labels_for_legend, 
#     loc='center left',           # Align the LEFT side of the legend...
#     bbox_to_anchor=(0.78, 0.5),  # ...to the point just after the plots (0.72)
#     title="Input Formats & Models",
#     borderaxespad=0.
# )
# Make the legend title bold
# legend.get_title().set_fontweight('bold')



# -----------------------
# try making a legend

# --- Legend Group Definitions ---
spacer_handle = (
Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
pro_handle = (
Line2D([], [], marker='none', color='grey', linestyle = ':'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
),
flashlite_handle = (
Line2D([], [], marker='none', color='grey', linestyle = '-'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
)


handles = [
spacer_handle,
pro_handle,
flashlite_handle,
spacer_handle,

Line2D([], [], marker='o', color=colors[0], linestyle='None', markersize = 10),  # Adjacency JSON
Line2D([], [], marker='o', color=colors[1], linestyle='None', markersize = 10),  # Adjacency Text
Line2D([], [], marker='o', color=colors[2], linestyle='None', markersize = 10),  # JPG
Line2D([], [], marker='o', color=colors[3], linestyle='None', markersize = 10),  # JSON
Line2D([], [], marker='o', color=colors[4], linestyle='None', markersize = 10),  # Tokenized
Line2D([], [], marker='o', color=colors[5], linestyle='None', markersize = 10),  # ASCII

]
labels = [
r"$\bf{Models}$",
"Gemini 2.5 Pro", "Gemini 2.5 Flash-Lite",
r"$\bf{Input\ Formats}$",
"Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"
]
axes[1,2].legend(
handles,
labels,
handler_map={tuple: HandlerTuple(ndivide=None)},
loc='center left',
bbox_to_anchor=(1.02, 0.5),
title="Legend"
)


plt.tight_layout()
# Adjust right margin to make room for the legend
plt.subplots_adjust(right=0.85) 
plt.show()








#------------- Plotting raw scores for all types and sizes ----------------------


# NR -- Coords -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# 3x3 averages
avg_line_NR_coords_adj_json_raw_score_3 = np.mean(r3.line_NR_coords_adj_json_raw_score_3)
avg_line_NR_coords_adj_txt_raw_score_3 = np.mean(r3.line_NR_coords_adj_txt_raw_score_3)
avg_line_NR_coords_jpg_raw_score_3 = np.mean(r3.line_NR_coords_jpg_raw_score_3)
avg_line_NR_coords_json_raw_score_3 = np.mean(r3.line_NR_coords_json_raw_score_3)
avg_line_NR_coords_tokenized_txt_raw_score_3 = np.mean(r3.line_NR_coords_tokenized_txt_raw_score_3)
avg_occupancy_NR_coords_adj_json_raw_score_3 = np.mean(r3.occupancy_NR_coords_adj_json_raw_score_3)
avg_occupancy_NR_coords_adj_txt_raw_score_3 = np.mean(r3.occupancy_NR_coords_adj_txt_raw_score_3)
avg_occupancy_NR_coords_ascii_txt_raw_score_3 = np.mean(r3.occupancy_NR_coords_ascii_txt_raw_score_3)  
avg_occupancy_NR_coords_jpg_raw_score_3 = np.mean(r3.occupancy_NR_coords_jpg_raw_score_3)
avg_occupancy_NR_coords_json_raw_score_3 = np.mean(r3.occupancy_NR_coords_json_raw_score_3)
avg_occupancy_NR_coords_tokenized_txt_raw_score_3 = np.mean(r3.occupancy_NR_coords_tokenized_txt_raw_score_3)
# 6x6 averages
avg_line_NR_coords_adj_json_raw_score_6 = np.mean(r6.line_NR_coords_adj_json_raw_score_6)
avg_line_NR_coords_adj_txt_raw_score_6 = np.mean(r6.line_NR_coords_adj_txt_raw_score_6)
avg_line_NR_coords_jpg_raw_score_6 = np.mean(r6.line_NR_coords_jpg_raw_score_6)
avg_line_NR_coords_json_raw_score_6 = np.mean(r6.line_NR_coords_json_raw_score_6)
avg_line_NR_coords_tokenized_txt_raw_score_6 = np.mean(r6.line_NR_coords_tokenized_txt_raw_score_6)
avg_occupancy_NR_coords_adj_json_raw_score_6 = np.mean(r6.occupancy_NR_coords_adj_json_raw_score_6)
avg_occupancy_NR_coords_adj_txt_raw_score_6 = np.mean(r6.occupancy_NR_coords_adj_txt_raw_score_6)
avg_occupancy_NR_coords_ascii_txt_raw_score_6 = np.mean(r6.occupancy_NR_coords_ascii_txt_raw_score_6)  
avg_occupancy_NR_coords_jpg_raw_score_6 = np.mean(r6.occupancy_NR_coords_jpg_raw_score_6)
avg_occupancy_NR_coords_json_raw_score_6 = np.mean(r6.occupancy_NR_coords_json_raw_score_6)
avg_occupancy_NR_coords_tokenized_txt_raw_score_6 = np.mean(r6.occupancy_NR_coords_tokenized_txt_raw_score_6)
# 15x15 averages
avg_line_NR_coords_adj_json_raw_score_15 = np.mean(r15.line_NR_coords_adj_json_raw_score_15)
avg_line_NR_coords_adj_txt_raw_score_15 = np.mean(r15.line_NR_coords_adj_txt_raw_score_15)
avg_line_NR_coords_jpg_raw_score_15 = np.mean(r15.line_NR_coords_jpg_raw_score_15)
avg_line_NR_coords_json_raw_score_15 = np.mean(r15.line_NR_coords_json_raw_score_15)
avg_line_NR_coords_tokenized_txt_raw_score_15 = np.mean(r15.line_NR_coords_tokenized_txt_raw_score_15)   
avg_occupancy_NR_coords_adj_json_raw_score_15 = np.mean(r15.occupancy_NR_coords_adj_json_raw_score_15)
avg_occupancy_NR_coords_adj_txt_raw_score_15 = np.mean(r15.occupancy_NR_coords_adj_txt_raw_score_15)
avg_occupancy_NR_coords_ascii_txt_raw_score_15 = np.mean(r15.occupancy_NR_coords_ascii_txt_raw_score_15)
avg_occupancy_NR_coords_jpg_raw_score_15 = np.mean(r15.occupancy_NR_coords_jpg_raw_score_15)
avg_occupancy_NR_coords_json_raw_score_15 = np.mean(r15.occupancy_NR_coords_json_raw_score_15)
avg_occupancy_NR_coords_tokenized_txt_raw_score_15 = np.mean(r15.occupancy_NR_coords_tokenized_txt_raw_score_15)

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




# NR -- Allo -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# 3x3 averages
avg_line_NR_allo_adj_json_raw_score_3 = np.mean(r3.line_NR_allo_adj_json_raw_score_3)
avg_line_NR_allo_adj_txt_raw_score_3 = np.mean(r3.line_NR_allo_adj_txt_raw_score_3)
avg_line_NR_allo_jpg_raw_score_3 = np.mean(r3.line_NR_allo_jpg_raw_score_3)
avg_line_NR_allo_json_raw_score_3 = np.mean(r3.line_NR_allo_json_raw_score_3)
avg_line_NR_allo_tokenized_txt_raw_score_3 = np.mean(r3.line_NR_allo_tokenized_txt_raw_score_3)
avg_occupancy_NR_allo_adj_json_raw_score_3 = np.mean(r3.occupancy_NR_allo_adj_json_raw_score_3)
avg_occupancy_NR_allo_adj_txt_raw_score_3 = np.mean(r3.occupancy_NR_allo_adj_txt_raw_score_3)
avg_occupancy_NR_allo_ascii_txt_raw_score_3 = np.mean(r3.occupancy_NR_allo_ascii_txt_raw_score_3)  
avg_occupancy_NR_allo_jpg_raw_score_3 = np.mean(r3.occupancy_NR_allo_jpg_raw_score_3)
avg_occupancy_NR_allo_json_raw_score_3 = np.mean(r3.occupancy_NR_allo_json_raw_score_3)
avg_occupancy_NR_allo_tokenized_txt_raw_score_3 = np.mean(r3.occupancy_NR_allo_tokenized_txt_raw_score_3)
#6x6 averages
avg_line_NR_allo_adj_json_raw_score_6 = np.mean(r6.line_NR_allo_adj_json_raw_score_6)
avg_line_NR_allo_adj_txt_raw_score_6 = np.mean(r6.line_NR_allo_adj_txt_raw_score_6)
avg_line_NR_allo_jpg_raw_score_6 = np.mean(r6.line_NR_allo_jpg_raw_score_6)
avg_line_NR_allo_json_raw_score_6 = np.mean(r6.line_NR_allo_json_raw_score_6)
avg_line_NR_allo_tokenized_txt_raw_score_6 = np.mean(r6.line_NR_allo_tokenized_txt_raw_score_6)
avg_occupancy_NR_allo_adj_json_raw_score_6 = np.mean(r6.occupancy_NR_allo_adj_json_raw_score_6)
avg_occupancy_NR_allo_adj_txt_raw_score_6 = np.mean(r6.occupancy_NR_allo_adj_txt_raw_score_6)
avg_occupancy_NR_allo_ascii_txt_raw_score_6 = np.mean(r6.occupancy_NR_allo_ascii_txt_raw_score_6)  
avg_occupancy_NR_allo_jpg_raw_score_6 = np.mean(r6.occupancy_NR_allo_jpg_raw_score_6)
avg_occupancy_NR_allo_json_raw_score_6 = np.mean(r6.occupancy_NR_allo_json_raw_score_6)
avg_occupancy_NR_allo_tokenized_txt_raw_score_6 = np.mean(r6.occupancy_NR_allo_tokenized_txt_raw_score_6)
# 15x15 averages
avg_line_NR_allo_adj_json_raw_score_15 = np.mean(r15.line_NR_allo_adj_json_raw_score_15)
avg_line_NR_allo_adj_txt_raw_score_15 = np.mean(r15.line_NR_allo_adj_txt_raw_score_15)
avg_line_NR_allo_jpg_raw_score_15 = np.mean(r15.line_NR_allo_jpg_raw_score_15)
avg_line_NR_allo_json_raw_score_15 = np.mean(r15.line_NR_allo_json_raw_score_15)
avg_line_NR_allo_tokenized_txt_raw_score_15 = np.mean(r15.line_NR_allo_tokenized_txt_raw_score_15)
avg_occupancy_NR_allo_adj_json_raw_score_15 = np.mean(r15.occupancy_NR_allo_adj_json_raw_score_15)
avg_occupancy_NR_allo_adj_txt_raw_score_15 = np.mean(r15.occupancy_NR_allo_adj_txt_raw_score_15)
avg_occupancy_NR_allo_ascii_txt_raw_score_15 = np.mean(r15.occupancy_NR_allo_ascii_txt_raw_score_15) 
avg_occupancy_NR_allo_jpg_raw_score_15 = np.mean(r15.occupancy_NR_allo_jpg_raw_score_15)
avg_occupancy_NR_allo_json_raw_score_15 = np.mean(r15.occupancy_NR_allo_json_raw_score_15)
avg_occupancy_NR_allo_tokenized_txt_raw_score_15 = np.mean(r15.occupancy_NR_allo_tokenized_txt_raw_score_15)

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


# NR -- Ego -- raw scores ----------- 3x3 & 15x15 -----------------------------------
# 3x3 averages
avg_line_NR_ego_adj_json_raw_score_3 = np.mean(r3.line_NR_ego_adj_json_raw_score_3)
avg_line_NR_ego_adj_txt_raw_score_3 = np.mean(r3.line_NR_ego_adj_txt_raw_score_3)
avg_line_NR_ego_jpg_raw_score_3 = np.mean(r3.line_NR_ego_jpg_raw_score_3)
avg_line_NR_ego_json_raw_score_3 = np.mean(r3.line_NR_ego_json_raw_score_3)
avg_line_NR_ego_tokenized_txt_raw_score_3 = np.mean(r3.line_NR_ego_tokenized_txt_raw_score_3)
avg_occupancy_NR_ego_adj_json_raw_score_3 = np.mean(r3.occupancy_NR_ego_adj_json_raw_score_3)
avg_occupancy_NR_ego_adj_txt_raw_score_3 = np.mean(r3.occupancy_NR_ego_adj_txt_raw_score_3)
avg_occupancy_NR_ego_ascii_txt_raw_score_3 = np.mean(r3.occupancy_NR_ego_ascii_txt_raw_score_3)  
avg_occupancy_NR_ego_jpg_raw_score_3 = np.mean(r3.occupancy_NR_ego_jpg_raw_score_3)
avg_occupancy_NR_ego_json_raw_score_3 = np.mean(r3.occupancy_NR_ego_json_raw_score_3)
avg_occupancy_NR_ego_tokenized_txt_raw_score_3 = np.mean(r3.occupancy_NR_ego_tokenized_txt_raw_score_3)
#6x6 averages
avg_line_NR_ego_adj_json_raw_score_6 = np.mean(r6.line_NR_ego_adj_json_raw_score_6)
avg_line_NR_ego_adj_txt_raw_score_6 = np.mean(r6.line_NR_ego_adj_txt_raw_score_6)
avg_line_NR_ego_jpg_raw_score_6 = np.mean(r6.line_NR_ego_jpg_raw_score_6)
avg_line_NR_ego_json_raw_score_6 = np.mean(r6.line_NR_ego_json_raw_score_6)
avg_line_NR_ego_tokenized_txt_raw_score_6 = np.mean(r6.line_NR_ego_tokenized_txt_raw_score_6)
avg_occupancy_NR_ego_adj_json_raw_score_6 = np.mean(r6.occupancy_NR_ego_adj_json_raw_score_6)
avg_occupancy_NR_ego_adj_txt_raw_score_6 = np.mean(r6.occupancy_NR_ego_adj_txt_raw_score_6)
avg_occupancy_NR_ego_ascii_txt_raw_score_6 = np.mean(r6.occupancy_NR_ego_ascii_txt_raw_score_6)  
avg_occupancy_NR_ego_jpg_raw_score_6 = np.mean(r6.occupancy_NR_ego_jpg_raw_score_6)
avg_occupancy_NR_ego_json_raw_score_6 = np.mean(r6.occupancy_NR_ego_json_raw_score_6)
avg_occupancy_NR_ego_tokenized_txt_raw_score_6 = np.mean(r6.occupancy_NR_ego_tokenized_txt_raw_score_6)
# 15x15 averages
avg_line_NR_ego_adj_json_raw_score_15 = np.mean(r15.line_NR_ego_adj_json_raw_score_15)
avg_line_NR_ego_adj_txt_raw_score_15 = np.mean(r15.line_NR_ego_adj_txt_raw_score_15)
avg_line_NR_ego_jpg_raw_score_15 = np.mean(r15.line_NR_ego_jpg_raw_score_15)
avg_line_NR_ego_json_raw_score_15 = np.mean(r15.line_NR_ego_json_raw_score_15)
avg_line_NR_ego_tokenized_txt_raw_score_15 = np.mean(r15.line_NR_ego_tokenized_txt_raw_score_15)
avg_occupancy_NR_ego_adj_json_raw_score_15 = np.mean(r15.occupancy_NR_ego_adj_json_raw_score_15)
avg_occupancy_NR_ego_adj_txt_raw_score_15 = np.mean(r15.occupancy_NR_ego_adj_txt_raw_score_15)
avg_occupancy_NR_ego_ascii_txt_raw_score_15 = np.mean(r15.occupancy_NR_ego_ascii_txt_raw_score_15)
avg_occupancy_NR_ego_jpg_raw_score_15 = np.mean(r15.occupancy_NR_ego_jpg_raw_score_15)
avg_occupancy_NR_ego_json_raw_score_15 = np.mean(r15.occupancy_NR_ego_json_raw_score_15)
avg_occupancy_NR_ego_tokenized_txt_raw_score_15 = np.mean(r15.occupancy_NR_ego_tokenized_txt_raw_score_15)


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


# R -- Coords -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# 3x3 averages
avg_line_R_coords_adj_json_raw_score_3 = np.mean(r3.line_R_coords_adj_json_raw_score_3)
avg_line_R_coords_adj_txt_raw_score_3 = np.mean(r3.line_R_coords_adj_txt_raw_score_3)
avg_line_R_coords_jpg_raw_score_3 = np.mean(r3.line_R_coords_jpg_raw_score_3)
avg_line_R_coords_json_raw_score_3 = np.mean(r3.line_R_coords_json_raw_score_3)
avg_line_R_coords_tokenized_txt_raw_score_3 = np.mean(r3.line_R_coords_tokenized_txt_raw_score_3)
avg_occupancy_R_coords_adj_json_raw_score_3 = np.mean(r3.occupancy_R_coords_adj_json_raw_score_3)
avg_occupancy_R_coords_adj_txt_raw_score_3 = np.mean(r3.occupancy_R_coords_adj_txt_raw_score_3)
avg_occupancy_R_coords_ascii_txt_raw_score_3 = np.mean(r3.occupancy_R_coords_ascii_txt_raw_score_3)  
avg_occupancy_R_coords_jpg_raw_score_3 = np.mean(r3.occupancy_R_coords_jpg_raw_score_3)
avg_occupancy_R_coords_json_raw_score_3 = np.mean(r3.occupancy_R_coords_json_raw_score_3)
avg_occupancy_R_coords_tokenized_txt_raw_score_3 = np.mean(r3.occupancy_R_coords_tokenized_txt_raw_score_3)
# 6x6 averages
avg_line_R_coords_adj_json_raw_score_6 = np.mean(r6.line_R_coords_adj_json_raw_score_6)
avg_line_R_coords_adj_txt_raw_score_6 = np.mean(r6.line_R_coords_adj_txt_raw_score_6)
avg_line_R_coords_jpg_raw_score_6 = np.mean(r6.line_R_coords_jpg_raw_score_6)
avg_line_R_coords_json_raw_score_6 = np.mean(r6.line_R_coords_json_raw_score_6)
avg_line_R_coords_tokenized_txt_raw_score_6 = np.mean(r6.line_R_coords_tokenized_txt_raw_score_6)
avg_occupancy_R_coords_adj_json_raw_score_6 = np.mean(r6.occupancy_R_coords_adj_json_raw_score_6)
avg_occupancy_R_coords_adj_txt_raw_score_6 = np.mean(r6.occupancy_R_coords_adj_txt_raw_score_6)
avg_occupancy_R_coords_ascii_txt_raw_score_6 = np.mean(r6.occupancy_R_coords_ascii_txt_raw_score_6)  
avg_occupancy_R_coords_jpg_raw_score_6 = np.mean(r6.occupancy_R_coords_jpg_raw_score_6)
avg_occupancy_R_coords_json_raw_score_6 = np.mean(r6.occupancy_R_coords_json_raw_score_6)
avg_occupancy_R_coords_tokenized_txt_raw_score_6 = np.mean(r6.occupancy_R_coords_tokenized_txt_raw_score_6)
# 15x15 averages
avg_line_R_coords_adj_json_raw_score_15 = np.mean(r15.line_R_coords_adj_json_raw_score_15)
avg_line_R_coords_adj_txt_raw_score_15 = np.mean(r15.line_R_coords_adj_txt_raw_score_15)
avg_line_R_coords_jpg_raw_score_15 = np.mean(r15.line_R_coords_jpg_raw_score_15)
avg_line_R_coords_json_raw_score_15 = np.mean(r15.line_R_coords_json_raw_score_15)
avg_line_R_coords_tokenized_txt_raw_score_15 = np.mean(r15.line_R_coords_tokenized_txt_raw_score_15)
avg_occupancy_R_coords_adj_json_raw_score_15 = np.mean(r15.occupancy_R_coords_adj_json_raw_score_15)
avg_occupancy_R_coords_adj_txt_raw_score_15 = np.mean(r15.occupancy_R_coords_adj_txt_raw_score_15)
avg_occupancy_R_coords_ascii_txt_raw_score_15 = np.mean(r15.occupancy_R_coords_ascii_txt_raw_score_15)
avg_occupancy_R_coords_jpg_raw_score_15 = np.mean(r15.occupancy_R_coords_jpg_raw_score_15)
avg_occupancy_R_coords_json_raw_score_15 = np.mean(r15.occupancy_R_coords_json_raw_score_15)
avg_occupancy_R_coords_tokenized_txt_raw_score_15 = np.mean(r15.occupancy_R_coords_tokenized_txt_raw_score_15)


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

# R -- Allo -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# 3x3 averages
avg_line_R_allo_adj_json_raw_score_3 = np.mean(r3.line_R_allo_adj_json_raw_score_3)
avg_line_R_allo_adj_txt_raw_score_3 = np.mean(r3.line_R_allo_adj_txt_raw_score_3)
avg_line_R_allo_jpg_raw_score_3 = np.mean(r3.line_R_allo_jpg_raw_score_3)
avg_line_R_allo_json_raw_score_3 = np.mean(r3.line_R_allo_json_raw_score_3)
avg_line_R_allo_tokenized_txt_raw_score_3 = np.mean(r3.line_R_allo_tokenized_txt_raw_score_3)
avg_occupancy_R_allo_adj_json_raw_score_3 = np.mean(r3.occupancy_R_allo_adj_json_raw_score_3)
avg_occupancy_R_allo_adj_txt_raw_score_3 = np.mean(r3.occupancy_R_allo_adj_txt_raw_score_3)
avg_occupancy_R_allo_ascii_txt_raw_score_3 = np.mean(r3.occupancy_R_allo_ascii_txt_raw_score_3)  
avg_occupancy_R_allo_jpg_raw_score_3 = np.mean(r3.occupancy_R_allo_jpg_raw_score_3)
avg_occupancy_R_allo_json_raw_score_3 = np.mean(r3.occupancy_R_allo_json_raw_score_3)
avg_occupancy_R_allo_tokenized_txt_raw_score_3 = np.mean(r3.occupancy_R_allo_tokenized_txt_raw_score_3)
# 6x6 averages
avg_line_R_allo_adj_json_raw_score_6 = np.mean(r6.line_R_allo_adj_json_raw_score_6)
avg_line_R_allo_adj_txt_raw_score_6 = np.mean(r6.line_R_allo_adj_txt_raw_score_6)
avg_line_R_allo_jpg_raw_score_6 = np.mean(r6.line_R_allo_jpg_raw_score_6)
avg_line_R_allo_json_raw_score_6 = np.mean(r6.line_R_allo_json_raw_score_6)
avg_line_R_allo_tokenized_txt_raw_score_6 = np.mean(r6.line_R_allo_tokenized_txt_raw_score_6)
avg_occupancy_R_allo_adj_json_raw_score_6 = np.mean(r6.occupancy_R_allo_adj_json_raw_score_6)
avg_occupancy_R_allo_adj_txt_raw_score_6 = np.mean(r6.occupancy_R_allo_adj_txt_raw_score_6)
avg_occupancy_R_allo_ascii_txt_raw_score_6 = np.mean(r6.occupancy_R_allo_ascii_txt_raw_score_6)  
avg_occupancy_R_allo_jpg_raw_score_6 = np.mean(r6.occupancy_R_allo_jpg_raw_score_6)
avg_occupancy_R_allo_json_raw_score_6 = np.mean(r6.occupancy_R_allo_json_raw_score_6)
avg_occupancy_R_allo_tokenized_txt_raw_score_6 = np.mean(r6.occupancy_R_allo_tokenized_txt_raw_score_6)
# 15x15 averages
avg_line_R_allo_adj_json_raw_score_15 = np.mean(r15.line_R_allo_adj_json_raw_score_15)
avg_line_R_allo_adj_txt_raw_score_15 = np.mean(r15.line_R_allo_adj_txt_raw_score_15)
avg_line_R_allo_jpg_raw_score_15 = np.mean(r15.line_R_allo_jpg_raw_score_15)
avg_line_R_allo_json_raw_score_15 = np.mean(r15.line_R_allo_json_raw_score_15)
avg_line_R_allo_tokenized_txt_raw_score_15 = np.mean(r15.line_R_allo_tokenized_txt_raw_score_15)
avg_occupancy_R_allo_adj_json_raw_score_15 = np.mean(r15.occupancy_R_allo_adj_json_raw_score_15)
avg_occupancy_R_allo_adj_txt_raw_score_15 = np.mean(r15.occupancy_R_allo_adj_txt_raw_score_15)
avg_occupancy_R_allo_ascii_txt_raw_score_15 = np.mean(r15.occupancy_R_allo_ascii_txt_raw_score_15)
avg_occupancy_R_allo_jpg_raw_score_15 = np.mean(r15.occupancy_R_allo_jpg_raw_score_15)
avg_occupancy_R_allo_json_raw_score_15 = np.mean(r15.occupancy_R_allo_json_raw_score_15)
avg_occupancy_R_allo_tokenized_txt_raw_score_15 = np.mean(r15.occupancy_R_allo_tokenized_txt_raw_score_15)


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





# R -- Ego -- raw scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# 3x3 averages
avg_line_R_ego_adj_json_raw_score_3 = np.mean(r3.line_R_ego_adj_json_raw_score_3)
avg_line_R_ego_adj_txt_raw_score_3 = np.mean(r3.line_R_ego_adj_txt_raw_score_3)
avg_line_R_ego_jpg_raw_score_3 = np.mean(r3.line_R_ego_jpg_raw_score_3)
avg_line_R_ego_json_raw_score_3 = np.mean(r3.line_R_ego_json_raw_score_3)
avg_line_R_ego_tokenized_txt_raw_score_3 = np.mean(r3.line_R_ego_tokenized_txt_raw_score_3)
avg_occupancy_R_ego_adj_json_raw_score_3 = np.mean(r3.occupancy_R_ego_adj_json_raw_score_3)
avg_occupancy_R_ego_adj_txt_raw_score_3 = np.mean(r3.occupancy_R_ego_adj_txt_raw_score_3)
avg_occupancy_R_ego_ascii_txt_raw_score_3 = np.mean(r3.occupancy_R_ego_ascii_txt_raw_score_3)  
avg_occupancy_R_ego_jpg_raw_score_3 = np.mean(r3.occupancy_R_ego_jpg_raw_score_3)
avg_occupancy_R_ego_json_raw_score_3 = np.mean(r3.occupancy_R_ego_json_raw_score_3)
avg_occupancy_R_ego_tokenized_txt_raw_score_3 = np.mean(r3.occupancy_R_ego_tokenized_txt_raw_score_3)
#6x6 averages
avg_line_R_ego_adj_json_raw_score_6 = np.mean(r6.line_R_ego_adj_json_raw_score_6)
avg_line_R_ego_adj_txt_raw_score_6 = np.mean(r6.line_R_ego_adj_txt_raw_score_6)
avg_line_R_ego_jpg_raw_score_6 = np.mean(r6.line_R_ego_jpg_raw_score_6)
avg_line_R_ego_json_raw_score_6 = np.mean(r6.line_R_ego_json_raw_score_6)
avg_line_R_ego_tokenized_txt_raw_score_6 = np.mean(r6.line_R_ego_tokenized_txt_raw_score_6)
avg_occupancy_R_ego_adj_json_raw_score_6 = np.mean(r6.occupancy_R_ego_adj_json_raw_score_6)
avg_occupancy_R_ego_adj_txt_raw_score_6 = np.mean(r6.occupancy_R_ego_adj_txt_raw_score_6)
avg_occupancy_R_ego_ascii_txt_raw_score_6 = np.mean(r6.occupancy_R_ego_ascii_txt_raw_score_6)  
avg_occupancy_R_ego_jpg_raw_score_6 = np.mean(r6.occupancy_R_ego_jpg_raw_score_6)
avg_occupancy_R_ego_json_raw_score_6 = np.mean(r6.occupancy_R_ego_json_raw_score_6)
avg_occupancy_R_ego_tokenized_txt_raw_score_6 = np.mean(r6.occupancy_R_ego_tokenized_txt_raw_score_6)
# 15x15 averages and std
avg_line_R_ego_adj_json_raw_score_15 = np.mean(r15.line_R_ego_adj_json_raw_score_15)
avg_line_R_ego_adj_txt_raw_score_15 = np.mean(r15.line_R_ego_adj_txt_raw_score_15)
avg_line_R_ego_jpg_raw_score_15 = np.mean(r15.line_R_ego_jpg_raw_score_15)
avg_line_R_ego_json_raw_score_15 = np.mean(r15.line_R_ego_json_raw_score_15)
avg_line_R_ego_tokenized_txt_raw_score_15 = np.mean(r15.line_R_ego_tokenized_txt_raw_score_15)
avg_occupancy_R_ego_adj_json_raw_score_15 = np.mean(r15.occupancy_R_ego_adj_json_raw_score_15)
avg_occupancy_R_ego_adj_txt_raw_score_15 = np.mean(r15.occupancy_R_ego_adj_txt_raw_score_15)
avg_occupancy_R_ego_ascii_txt_raw_score_15 = np.mean(r15.occupancy_R_ego_ascii_txt_raw_score_15)
avg_occupancy_R_ego_jpg_raw_score_15 = np.mean(r15.occupancy_R_ego_jpg_raw_score_15)
avg_occupancy_R_ego_json_raw_score_15 = np.mean(r15.occupancy_R_ego_json_raw_score_15)
avg_occupancy_R_ego_tokenized_txt_raw_score_15 = np.mean(r15.occupancy_R_ego_tokenized_txt_raw_score_15)



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


# ----- use this for plotting raw scores: Plottoing all 6 raw score plots in one figure ------------------

# Structure the data
# Top plot data: line-maze data vectors with the complexities as column entries and representations as row entries.
# Bottom plot data: occupancy-maze data vectors with the complexities as column entries and representations as row entries. 
labels_line = [
    "Line Adjacency JSON",
    "Line Adjacency txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized"
]

labels_occ = [
    "Occupancy Adjacency JSON",
    "Occupancy Adjacency txt",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized",
    "Occupancy ASCII"
]

# Line, NR, coords
means_line_NR_coords = [
    [avg_line_NR_coords_adj_json_raw_score_3,       avg_line_NR_coords_adj_json_raw_score_6,       avg_line_NR_coords_adj_json_raw_score_15],
    [avg_line_NR_coords_adj_txt_raw_score_3,        avg_line_NR_coords_adj_txt_raw_score_6,        avg_line_NR_coords_adj_txt_raw_score_15],
    [avg_line_NR_coords_jpg_raw_score_3,            avg_line_NR_coords_jpg_raw_score_6,            avg_line_NR_coords_jpg_raw_score_15],
    [avg_line_NR_coords_json_raw_score_3,           avg_line_NR_coords_json_raw_score_6,           avg_line_NR_coords_json_raw_score_15],
    [avg_line_NR_coords_tokenized_txt_raw_score_3,  avg_line_NR_coords_tokenized_txt_raw_score_6,  avg_line_NR_coords_tokenized_txt_raw_score_15]
]

error_line_NR_coords = [
    [confidence_interval(r3.line_NR_coords_adj_json_raw_score_3),       confidence_interval(r6.line_NR_coords_adj_json_raw_score_6),       confidence_interval(r15.line_NR_coords_adj_json_raw_score_15)],
    [confidence_interval(r3.line_NR_coords_adj_txt_raw_score_3),        confidence_interval(r6.line_NR_coords_adj_txt_raw_score_6),        confidence_interval(r15.line_NR_coords_adj_txt_raw_score_15)],
    [confidence_interval(r3.line_NR_coords_jpg_raw_score_3),            confidence_interval(r6.line_NR_coords_jpg_raw_score_6),            confidence_interval(r15.line_NR_coords_jpg_raw_score_15)],
    [confidence_interval(r3.line_NR_coords_json_raw_score_3),           confidence_interval(r6.line_NR_coords_json_raw_score_6),           confidence_interval(r15.line_NR_coords_json_raw_score_15)],
    [confidence_interval(r3.line_NR_coords_tokenized_txt_raw_score_3),  confidence_interval(r6.line_NR_coords_tokenized_txt_raw_score_6),  confidence_interval(r15.line_NR_coords_tokenized_txt_raw_score_15)]
]



# Occupancy, NR, coords
means_occ_NR_coords = [
    [avg_occupancy_NR_coords_adj_json_raw_score_3,       avg_occupancy_NR_coords_adj_json_raw_score_6,      avg_occupancy_NR_coords_adj_json_raw_score_15],
    [avg_occupancy_NR_coords_adj_txt_raw_score_3,        avg_occupancy_NR_coords_adj_txt_raw_score_6,        avg_occupancy_NR_coords_adj_txt_raw_score_15],
    [avg_occupancy_NR_coords_jpg_raw_score_3,            avg_occupancy_NR_coords_jpg_raw_score_6,            avg_occupancy_NR_coords_jpg_raw_score_15],
    [avg_occupancy_NR_coords_json_raw_score_3,           avg_occupancy_NR_coords_json_raw_score_6,           avg_occupancy_NR_coords_json_raw_score_15],
    [avg_occupancy_NR_coords_tokenized_txt_raw_score_3,  avg_occupancy_NR_coords_tokenized_txt_raw_score_6,  avg_occupancy_NR_coords_tokenized_txt_raw_score_15],
    [avg_occupancy_NR_coords_ascii_txt_raw_score_3,      avg_occupancy_NR_coords_ascii_txt_raw_score_6,      avg_occupancy_NR_coords_ascii_txt_raw_score_15],
]


error_occupancy_NR_coords = [
    [confidence_interval(r3.occupancy_NR_coords_adj_json_raw_score_3),       confidence_interval(r6.occupancy_NR_coords_adj_json_raw_score_6),       confidence_interval(r15.occupancy_NR_coords_adj_json_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_coords_adj_txt_raw_score_3),        confidence_interval(r6.occupancy_NR_coords_adj_txt_raw_score_6),        confidence_interval(r15.occupancy_NR_coords_adj_txt_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_coords_jpg_raw_score_3),            confidence_interval(r6.occupancy_NR_coords_jpg_raw_score_6),            confidence_interval(r15.occupancy_NR_coords_jpg_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_coords_json_raw_score_3),           confidence_interval(r6.occupancy_NR_coords_json_raw_score_6),           confidence_interval(r15.occupancy_NR_coords_json_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_coords_tokenized_txt_raw_score_3),  confidence_interval(r6.occupancy_NR_coords_tokenized_txt_raw_score_6),  confidence_interval(r15.occupancy_NR_coords_tokenized_txt_raw_score_15)],
    [ confidence_interval(r3.occupancy_NR_coords_ascii_txt_raw_score_3),     confidence_interval(r6.occupancy_NR_coords_ascii_txt_raw_score_6),      confidence_interval(r15.occupancy_NR_coords_ascii_txt_raw_score_15)]
]



# Line, NR, allo
means_line_NR_allo = [
    [avg_line_NR_allo_adj_json_raw_score_3,       avg_line_NR_allo_adj_json_raw_score_6,       avg_line_NR_allo_adj_json_raw_score_15],
    [avg_line_NR_allo_adj_txt_raw_score_3,        avg_line_NR_allo_adj_txt_raw_score_6,        avg_line_NR_allo_adj_txt_raw_score_15],
    [avg_line_NR_allo_jpg_raw_score_3,            avg_line_NR_allo_jpg_raw_score_6,            avg_line_NR_allo_jpg_raw_score_15],
    [avg_line_NR_allo_json_raw_score_3,           avg_line_NR_allo_json_raw_score_6,           avg_line_NR_allo_json_raw_score_15],
    [avg_line_NR_allo_tokenized_txt_raw_score_3,  avg_line_NR_allo_tokenized_txt_raw_score_6,  avg_line_NR_allo_tokenized_txt_raw_score_15]
]

error_line_NR_allo = [
    [confidence_interval(r3.line_NR_allo_adj_json_raw_score_3),       confidence_interval(r6.line_NR_allo_adj_json_raw_score_6),       confidence_interval(r15.line_NR_allo_adj_json_raw_score_15)],
    [confidence_interval(r3.line_NR_allo_adj_txt_raw_score_3),        confidence_interval(r6.line_NR_allo_adj_txt_raw_score_6),        confidence_interval(r15.line_NR_allo_adj_txt_raw_score_15)],
    [confidence_interval(r3.line_NR_allo_jpg_raw_score_3),            confidence_interval(r6.line_NR_allo_jpg_raw_score_6),            confidence_interval(r15.line_NR_allo_jpg_raw_score_15)],
    [confidence_interval(r3.line_NR_allo_json_raw_score_3),           confidence_interval(r6.line_NR_allo_json_raw_score_6),           confidence_interval(r15.line_NR_allo_json_raw_score_15)],
    [confidence_interval(r3.line_NR_allo_tokenized_txt_raw_score_3),  confidence_interval(r6.line_NR_allo_tokenized_txt_raw_score_6),  confidence_interval(r15.line_NR_allo_tokenized_txt_raw_score_15)]
]


# Occupancy, NR, allo
means_occ_NR_allo = [
    [avg_occupancy_NR_allo_adj_json_raw_score_3,       avg_occupancy_NR_allo_adj_json_raw_score_6,       avg_occupancy_NR_allo_adj_json_raw_score_15],
    [avg_occupancy_NR_allo_adj_txt_raw_score_3,        avg_occupancy_NR_allo_adj_txt_raw_score_6,        avg_occupancy_NR_allo_adj_txt_raw_score_15],
    [avg_occupancy_NR_allo_jpg_raw_score_3,            avg_occupancy_NR_allo_jpg_raw_score_6,            avg_occupancy_NR_allo_jpg_raw_score_15],
    [avg_occupancy_NR_allo_json_raw_score_3,           avg_occupancy_NR_allo_json_raw_score_6,           avg_occupancy_NR_allo_json_raw_score_15],
    [avg_occupancy_NR_allo_tokenized_txt_raw_score_3,  avg_occupancy_NR_allo_tokenized_txt_raw_score_6,  avg_occupancy_NR_allo_tokenized_txt_raw_score_15],
    [avg_occupancy_NR_allo_ascii_txt_raw_score_3,      avg_occupancy_NR_allo_ascii_txt_raw_score_6,      avg_occupancy_NR_allo_ascii_txt_raw_score_15],
]

error_occupancy_NR_allo = [
    [confidence_interval(r3.occupancy_NR_allo_adj_json_raw_score_3),       confidence_interval(r6.occupancy_NR_allo_adj_json_raw_score_6),       confidence_interval(r15.occupancy_NR_allo_adj_json_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_allo_adj_txt_raw_score_3),        confidence_interval(r6.occupancy_NR_allo_adj_txt_raw_score_6),        confidence_interval(r15.occupancy_NR_allo_adj_txt_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_allo_jpg_raw_score_3),            confidence_interval(r6.occupancy_NR_allo_jpg_raw_score_6),            confidence_interval(r15.occupancy_NR_allo_jpg_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_allo_json_raw_score_3),           confidence_interval(r6.occupancy_NR_allo_json_raw_score_6),           confidence_interval(r15.occupancy_NR_allo_json_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_allo_tokenized_txt_raw_score_3),  confidence_interval(r6.occupancy_NR_allo_tokenized_txt_raw_score_6),  confidence_interval(r15.occupancy_NR_allo_tokenized_txt_raw_score_15)],
    [ confidence_interval(r3.occupancy_NR_allo_ascii_txt_raw_score_3),     confidence_interval(r6.occupancy_NR_allo_ascii_txt_raw_score_6),      confidence_interval(r15.occupancy_NR_allo_ascii_txt_raw_score_15)]
]

# Line, NR, ego
means_line_NR_ego = [
    [avg_line_NR_ego_adj_json_raw_score_3,       avg_line_NR_ego_adj_json_raw_score_6,       avg_line_NR_ego_adj_json_raw_score_15],
    [avg_line_NR_ego_adj_txt_raw_score_3,        avg_line_NR_ego_adj_txt_raw_score_6,        avg_line_NR_ego_adj_txt_raw_score_15],
    [avg_line_NR_ego_jpg_raw_score_3,            avg_line_NR_ego_jpg_raw_score_6,            avg_line_NR_ego_jpg_raw_score_15],
    [avg_line_NR_ego_json_raw_score_3,           avg_line_NR_ego_json_raw_score_6,           avg_line_NR_ego_json_raw_score_15],
    [avg_line_NR_ego_tokenized_txt_raw_score_3,  avg_line_NR_ego_tokenized_txt_raw_score_6,  avg_line_NR_ego_tokenized_txt_raw_score_15]
]

error_line_NR_ego = [
    [confidence_interval(r3.line_NR_ego_adj_json_raw_score_3),       confidence_interval(r6.line_NR_ego_adj_json_raw_score_6),       confidence_interval(r15.line_NR_ego_adj_json_raw_score_15)],
    [confidence_interval(r3.line_NR_ego_adj_txt_raw_score_3),        confidence_interval(r6.line_NR_ego_adj_txt_raw_score_6),        confidence_interval(r15.line_NR_ego_adj_txt_raw_score_15)],
    [confidence_interval(r3.line_NR_ego_jpg_raw_score_3),            confidence_interval(r6.line_NR_ego_jpg_raw_score_6),            confidence_interval(r15.line_NR_ego_jpg_raw_score_15)],
    [confidence_interval(r3.line_NR_ego_json_raw_score_3),           confidence_interval(r6.line_NR_ego_json_raw_score_6),           confidence_interval(r15.line_NR_ego_json_raw_score_15)],
    [confidence_interval(r3.line_NR_ego_tokenized_txt_raw_score_3),  confidence_interval(r6.line_NR_ego_tokenized_txt_raw_score_6),  confidence_interval(r15.line_NR_ego_tokenized_txt_raw_score_15)]
]


# Occupancy, NR, ego
means_occ_NR_ego = [
    [avg_occupancy_NR_ego_adj_json_raw_score_3,       avg_occupancy_NR_ego_adj_json_raw_score_6,       avg_occupancy_NR_ego_adj_json_raw_score_15],
    [avg_occupancy_NR_ego_adj_txt_raw_score_3,        avg_occupancy_NR_ego_adj_txt_raw_score_6,        avg_occupancy_NR_ego_adj_txt_raw_score_15],
    [avg_occupancy_NR_ego_jpg_raw_score_3,            avg_occupancy_NR_ego_jpg_raw_score_6,            avg_occupancy_NR_ego_jpg_raw_score_15],
    [avg_occupancy_NR_ego_json_raw_score_3,           avg_occupancy_NR_ego_json_raw_score_6,           avg_occupancy_NR_ego_json_raw_score_15],
    [avg_occupancy_NR_ego_tokenized_txt_raw_score_3,  avg_occupancy_NR_ego_tokenized_txt_raw_score_6,  avg_occupancy_NR_ego_tokenized_txt_raw_score_15],
    [avg_occupancy_NR_ego_ascii_txt_raw_score_3,      avg_occupancy_NR_ego_ascii_txt_raw_score_6,      avg_occupancy_NR_ego_ascii_txt_raw_score_15]

]

error_occupancy_NR_ego = [
    [confidence_interval(r3.occupancy_NR_ego_adj_json_raw_score_3),       confidence_interval(r6.occupancy_NR_ego_adj_json_raw_score_6),       confidence_interval(r15.occupancy_NR_ego_adj_json_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_ego_adj_txt_raw_score_3),        confidence_interval(r6.occupancy_NR_ego_adj_txt_raw_score_6),        confidence_interval(r15.occupancy_NR_ego_adj_txt_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_ego_jpg_raw_score_3),            confidence_interval(r6.occupancy_NR_ego_jpg_raw_score_6),            confidence_interval(r15.occupancy_NR_ego_jpg_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_ego_json_raw_score_3),           confidence_interval(r6.occupancy_NR_ego_json_raw_score_6),           confidence_interval(r15.occupancy_NR_ego_json_raw_score_15)],
    [confidence_interval(r3.occupancy_NR_ego_tokenized_txt_raw_score_3),  confidence_interval(r6.occupancy_NR_ego_tokenized_txt_raw_score_6),  confidence_interval(r15.occupancy_NR_ego_tokenized_txt_raw_score_15)],
    [ confidence_interval(r3.occupancy_NR_ego_ascii_txt_raw_score_3),     confidence_interval(r6.occupancy_NR_ego_ascii_txt_raw_score_6),      confidence_interval(r15.occupancy_NR_ego_ascii_txt_raw_score_15)]
]




# Line, R, coords
means_line_R_coords = [
    [avg_line_R_coords_adj_json_raw_score_3,       avg_line_R_coords_adj_json_raw_score_6,       avg_line_R_coords_adj_json_raw_score_15],
    [avg_line_R_coords_adj_txt_raw_score_3,        avg_line_R_coords_adj_txt_raw_score_6,        avg_line_R_coords_adj_txt_raw_score_15],
    [avg_line_R_coords_jpg_raw_score_3,            avg_line_R_coords_jpg_raw_score_6,            avg_line_R_coords_jpg_raw_score_15],
    [avg_line_R_coords_json_raw_score_3,           avg_line_R_coords_json_raw_score_6,           avg_line_R_coords_json_raw_score_15],
    [avg_line_R_coords_tokenized_txt_raw_score_3,  avg_line_R_coords_tokenized_txt_raw_score_6,  avg_line_R_coords_tokenized_txt_raw_score_15]
]

error_line_R_coords = [
    [confidence_interval(r3.line_R_coords_adj_json_raw_score_3),       confidence_interval(r6.line_R_coords_adj_json_raw_score_6),       confidence_interval(r15.line_R_coords_adj_json_raw_score_15)],
    [confidence_interval(r3.line_R_coords_adj_txt_raw_score_3),        confidence_interval(r6.line_R_coords_adj_txt_raw_score_6),        confidence_interval(r15.line_R_coords_adj_txt_raw_score_15)],
    [confidence_interval(r3.line_R_coords_jpg_raw_score_3),            confidence_interval(r6.line_R_coords_jpg_raw_score_6),            confidence_interval(r15.line_R_coords_jpg_raw_score_15)],
    [confidence_interval(r3.line_R_coords_json_raw_score_3),           confidence_interval(r6.line_R_coords_json_raw_score_6),           confidence_interval(r15.line_R_coords_json_raw_score_15)],
    [confidence_interval(r3.line_R_coords_tokenized_txt_raw_score_3),  confidence_interval(r6.line_R_coords_tokenized_txt_raw_score_6),  confidence_interval(r15.line_R_coords_tokenized_txt_raw_score_15)]
]



# Occupancy, R, coords
means_occ_R_coords = [
    [avg_occupancy_R_coords_adj_json_raw_score_3,       avg_occupancy_R_coords_adj_json_raw_score_6,      avg_occupancy_R_coords_adj_json_raw_score_15],
    [avg_occupancy_R_coords_adj_txt_raw_score_3,        avg_occupancy_R_coords_adj_txt_raw_score_6,        avg_occupancy_R_coords_adj_txt_raw_score_15],
    [avg_occupancy_R_coords_jpg_raw_score_3,            avg_occupancy_R_coords_jpg_raw_score_6,            avg_occupancy_R_coords_jpg_raw_score_15],
    [avg_occupancy_R_coords_json_raw_score_3,           avg_occupancy_R_coords_json_raw_score_6,           avg_occupancy_R_coords_json_raw_score_15],
    [avg_occupancy_R_coords_tokenized_txt_raw_score_3,  avg_occupancy_R_coords_tokenized_txt_raw_score_6,  avg_occupancy_R_coords_tokenized_txt_raw_score_15],
    [avg_occupancy_R_coords_ascii_txt_raw_score_3,      avg_occupancy_R_coords_ascii_txt_raw_score_6,      avg_occupancy_R_coords_ascii_txt_raw_score_15]
]


error_occupancy_R_coords = [
    [confidence_interval(r3.occupancy_R_coords_adj_json_raw_score_3),       confidence_interval(r6.occupancy_R_coords_adj_json_raw_score_6),       confidence_interval(r15.occupancy_R_coords_adj_json_raw_score_15)],
    [confidence_interval(r3.occupancy_R_coords_adj_txt_raw_score_3),        confidence_interval(r6.occupancy_R_coords_adj_txt_raw_score_6),        confidence_interval(r15.occupancy_R_coords_adj_txt_raw_score_15)],
    [confidence_interval(r3.occupancy_R_coords_jpg_raw_score_3),            confidence_interval(r6.occupancy_R_coords_jpg_raw_score_6),            confidence_interval(r15.occupancy_R_coords_jpg_raw_score_15)],
    [confidence_interval(r3.occupancy_R_coords_json_raw_score_3),           confidence_interval(r6.occupancy_R_coords_json_raw_score_6),           confidence_interval(r15.occupancy_R_coords_json_raw_score_15)],
    [confidence_interval(r3.occupancy_R_coords_tokenized_txt_raw_score_3),  confidence_interval(r6.occupancy_R_coords_tokenized_txt_raw_score_6),  confidence_interval(r15.occupancy_R_coords_tokenized_txt_raw_score_15)],
    [confidence_interval(r3.occupancy_R_coords_ascii_txt_raw_score_3),     confidence_interval(r6.occupancy_R_coords_ascii_txt_raw_score_6),      confidence_interval(r15.occupancy_R_coords_ascii_txt_raw_score_15)]
]



# Line, R, allo
means_line_R_allo = [
    [avg_line_R_allo_adj_json_raw_score_3,       avg_line_R_allo_adj_json_raw_score_6,       avg_line_R_allo_adj_json_raw_score_15],
    [avg_line_R_allo_adj_txt_raw_score_3,        avg_line_R_allo_adj_txt_raw_score_6,        avg_line_R_allo_adj_txt_raw_score_15],
    [avg_line_R_allo_jpg_raw_score_3,            avg_line_R_allo_jpg_raw_score_6,            avg_line_R_allo_jpg_raw_score_15],
    [avg_line_R_allo_json_raw_score_3,           avg_line_R_allo_json_raw_score_6,           avg_line_R_allo_json_raw_score_15],
    [avg_line_R_allo_tokenized_txt_raw_score_3,  avg_line_R_allo_tokenized_txt_raw_score_6,  avg_line_R_allo_tokenized_txt_raw_score_15]
]

error_line_R_allo = [
    [confidence_interval(r3.line_R_allo_adj_json_raw_score_3),       confidence_interval(r6.line_R_allo_adj_json_raw_score_6),       confidence_interval(r15.line_R_allo_adj_json_raw_score_15)],
    [confidence_interval(r3.line_R_allo_adj_txt_raw_score_3),        confidence_interval(r6.line_R_allo_adj_txt_raw_score_6),        confidence_interval(r15.line_R_allo_adj_txt_raw_score_15)],
    [confidence_interval(r3.line_R_allo_jpg_raw_score_3),            confidence_interval(r6.line_R_allo_jpg_raw_score_6),            confidence_interval(r15.line_R_allo_jpg_raw_score_15)],
    [confidence_interval(r3.line_R_allo_json_raw_score_3),           confidence_interval(r6.line_R_allo_json_raw_score_6),           confidence_interval(r15.line_R_allo_json_raw_score_15)],
    [confidence_interval(r3.line_R_allo_tokenized_txt_raw_score_3),  confidence_interval(r6.line_R_allo_tokenized_txt_raw_score_6),  confidence_interval(r15.line_R_allo_tokenized_txt_raw_score_15)]
]


# Occupancy, R, allo
means_occ_R_allo = [
    [avg_occupancy_R_allo_adj_json_raw_score_3,       avg_occupancy_R_allo_adj_json_raw_score_6,       avg_occupancy_R_allo_adj_json_raw_score_15],
    [avg_occupancy_R_allo_adj_txt_raw_score_3,        avg_occupancy_R_allo_adj_txt_raw_score_6,        avg_occupancy_R_allo_adj_txt_raw_score_15],
    [avg_occupancy_R_allo_jpg_raw_score_3,            avg_occupancy_R_allo_jpg_raw_score_6,            avg_occupancy_R_allo_jpg_raw_score_15],
    [avg_occupancy_R_allo_json_raw_score_3,           avg_occupancy_R_allo_json_raw_score_6,           avg_occupancy_R_allo_json_raw_score_15],
    [avg_occupancy_R_allo_tokenized_txt_raw_score_3,  avg_occupancy_R_allo_tokenized_txt_raw_score_6,  avg_occupancy_R_allo_tokenized_txt_raw_score_15],
    [avg_occupancy_R_allo_ascii_txt_raw_score_3,      avg_occupancy_R_allo_ascii_txt_raw_score_6,      avg_occupancy_R_allo_ascii_txt_raw_score_15]
]

error_occupancy_R_allo = [
    [confidence_interval(r3.occupancy_R_allo_adj_json_raw_score_3),       confidence_interval(r6.occupancy_R_allo_adj_json_raw_score_6),       confidence_interval(r15.occupancy_R_allo_adj_json_raw_score_15)],
    [confidence_interval(r3.occupancy_R_allo_adj_txt_raw_score_3),        confidence_interval(r6.occupancy_R_allo_adj_txt_raw_score_6),        confidence_interval(r15.occupancy_R_allo_adj_txt_raw_score_15)],
    [confidence_interval(r3.occupancy_R_allo_jpg_raw_score_3),            confidence_interval(r6.occupancy_R_allo_jpg_raw_score_6),            confidence_interval(r15.occupancy_R_allo_jpg_raw_score_15)],
    [confidence_interval(r3.occupancy_R_allo_json_raw_score_3),           confidence_interval(r6.occupancy_R_allo_json_raw_score_6),           confidence_interval(r15.occupancy_R_allo_json_raw_score_15)],
    [confidence_interval(r3.occupancy_R_allo_tokenized_txt_raw_score_3),  confidence_interval(r6.occupancy_R_allo_tokenized_txt_raw_score_6),  confidence_interval(r15.occupancy_R_allo_tokenized_txt_raw_score_15)],
    [ confidence_interval(r3.occupancy_R_allo_ascii_txt_raw_score_3),     confidence_interval(r6.occupancy_R_allo_ascii_txt_raw_score_6),      confidence_interval(r15.occupancy_R_allo_ascii_txt_raw_score_15)]
]

# Line, R, ego
means_line_R_ego = [
    [avg_line_R_ego_adj_json_raw_score_3,       avg_line_R_ego_adj_json_raw_score_6,       avg_line_R_ego_adj_json_raw_score_15],
    [avg_line_R_ego_adj_txt_raw_score_3,        avg_line_R_ego_adj_txt_raw_score_6,        avg_line_R_ego_adj_txt_raw_score_15],
    [avg_line_R_ego_jpg_raw_score_3,            avg_line_R_ego_jpg_raw_score_6,            avg_line_R_ego_jpg_raw_score_15],
    [avg_line_R_ego_json_raw_score_3,           avg_line_R_ego_json_raw_score_6,           avg_line_R_ego_json_raw_score_15],
    [avg_line_R_ego_tokenized_txt_raw_score_3,  avg_line_R_ego_tokenized_txt_raw_score_6,  avg_line_R_ego_tokenized_txt_raw_score_15]
]

error_line_R_ego = [
    [confidence_interval(r3.line_R_ego_adj_json_raw_score_3),       confidence_interval(r6.line_R_ego_adj_json_raw_score_6),       confidence_interval(r15.line_R_ego_adj_json_raw_score_15)],
    [confidence_interval(r3.line_R_ego_adj_txt_raw_score_3),        confidence_interval(r6.line_R_ego_adj_txt_raw_score_6),        confidence_interval(r15.line_R_ego_adj_txt_raw_score_15)],
    [confidence_interval(r3.line_R_ego_jpg_raw_score_3),            confidence_interval(r6.line_R_ego_jpg_raw_score_6),            confidence_interval(r15.line_R_ego_jpg_raw_score_15)],
    [confidence_interval(r3.line_R_ego_json_raw_score_3),           confidence_interval(r6.line_R_ego_json_raw_score_6),           confidence_interval(r15.line_R_ego_json_raw_score_15)],
    [confidence_interval(r3.line_R_ego_tokenized_txt_raw_score_3),  confidence_interval(r6.line_R_ego_tokenized_txt_raw_score_6),  confidence_interval(r15.line_R_ego_tokenized_txt_raw_score_15)]
]


# Occupancy, R, ego
means_occ_R_ego = [
    [avg_occupancy_R_ego_adj_json_raw_score_3,       avg_occupancy_R_ego_adj_json_raw_score_6,       avg_occupancy_R_ego_adj_json_raw_score_15],
    [avg_occupancy_R_ego_adj_txt_raw_score_3,        avg_occupancy_R_ego_adj_txt_raw_score_6,        avg_occupancy_R_ego_adj_txt_raw_score_15],
    [avg_occupancy_R_ego_jpg_raw_score_3,            avg_occupancy_R_ego_jpg_raw_score_6,            avg_occupancy_R_ego_jpg_raw_score_15],
    [avg_occupancy_R_ego_json_raw_score_3,           avg_occupancy_R_ego_json_raw_score_6,           avg_occupancy_R_ego_json_raw_score_15],
    [avg_occupancy_R_ego_tokenized_txt_raw_score_3,  avg_occupancy_R_ego_tokenized_txt_raw_score_6,  avg_occupancy_R_ego_tokenized_txt_raw_score_15],
    [avg_occupancy_R_ego_ascii_txt_raw_score_3,      avg_occupancy_R_ego_ascii_txt_raw_score_6,      avg_occupancy_R_ego_ascii_txt_raw_score_15]
]

error_occupancy_R_ego = [
    [confidence_interval(r3.occupancy_R_ego_adj_json_raw_score_3),       confidence_interval(r6.occupancy_R_ego_adj_json_raw_score_6),       confidence_interval(r15.occupancy_R_ego_adj_json_raw_score_15)],
    [confidence_interval(r3.occupancy_R_ego_adj_txt_raw_score_3),        confidence_interval(r6.occupancy_R_ego_adj_txt_raw_score_6),        confidence_interval(r15.occupancy_R_ego_adj_txt_raw_score_15)],
    [confidence_interval(r3.occupancy_R_ego_jpg_raw_score_3),            confidence_interval(r6.occupancy_R_ego_jpg_raw_score_6),            confidence_interval(r15.occupancy_R_ego_jpg_raw_score_15)],
    [confidence_interval(r3.occupancy_R_ego_json_raw_score_3),           confidence_interval(r6.occupancy_R_ego_json_raw_score_6),           confidence_interval(r15.occupancy_R_ego_json_raw_score_15)],
    [confidence_interval(r3.occupancy_R_ego_tokenized_txt_raw_score_3),  confidence_interval(r6.occupancy_R_ego_tokenized_txt_raw_score_6),  confidence_interval(r15.occupancy_R_ego_tokenized_txt_raw_score_15)],
    [ confidence_interval(r3.occupancy_R_ego_ascii_txt_raw_score_3),     confidence_interval(r6.occupancy_R_ego_ascii_txt_raw_score_6),      confidence_interval(r15.occupancy_R_ego_ascii_txt_raw_score_15)]
]





# # Define the Legend Labels
# single_legend = [
#     'Adjacency JSON', 
#     'Adjacency Text', 
#     'JPG', 
#     'JSON', 
#     'Tokenized', 
#     'ASCII'
# ]

# Organize Data into Groups for the 6 Subplots
# Structure: (Means_NR, Means_R, Err_NR, Err_R, Title)
# NR = Non-Reasoning (Solid), R = Reasoning (Dotted)
plot_configs = [
    # Col 0: Left left
    (means_line_NR_coords, means_occ_NR_coords,
     error_line_NR_coords, error_occupancy_NR_coords),
    # Col 1: Middle left
    (means_line_NR_allo, means_occ_NR_allo,
     error_line_NR_allo, error_occupancy_NR_allo),
    # Col 2: Right left
    (means_line_NR_ego, means_occ_NR_ego, 
     error_line_NR_ego, error_occupancy_NR_ego),
    # Col 3: Right left
    (means_line_R_coords, means_occ_R_coords,
     error_line_R_coords, error_occupancy_R_coords),
    # Col 4: Right middle
    (means_line_R_allo, means_occ_R_allo,
     error_line_R_allo, error_occupancy_R_allo),
    # Col 5: Right right
    (means_line_R_ego, means_occ_R_ego,
     error_line_R_ego, error_occupancy_R_ego)
]

# 3. Setup Plotting Parameters
x_vals = np.arange(3)
x_tick_lbls_line = ["3x3", "6x6", "15x15"] # Complexity levels
x_tick_lbls_occupancy = ["7x7", "13x13", "31x31"] # Complexity levels
# Define a color palette for the 6 distinct methods (ignoring model version)
# We have 6 base methods (Adj Json, Adj Text, JPG, JSON, Tok, ASCII)
colors = plt.cm.tab10(np.linspace(0, 1, 10))[:6] 

fig, axes = plt.subplots(nrows=2, ncols=6, figsize=(18, 7), sharey=False, sharex=False)

# Set the different axes ranges for better viewing of the data.
# Left half
for row in [0, 1]:
    for col in [0, 1, 2]:
        axes[row, col].set_ylim(0, 60)

# Right half
for row in [0,1]:
    for col in [3,4,5]:
        axes[row, col].set_ylim(0, 200)

# Container to grab handles/labels for the global legend later
handles_for_legend = []
labels_for_legend = []

for col in range(6):
    means_line, means_occ, err_line, err_occ = plot_configs[col]

    # Convert to numpy arrays
    means_line = np.array(means_line)
    means_occ  = np.array(means_occ)
    err_line  = np.array(err_line)
    err_occ   = np.array(err_occ)

    # Number of methods
    n_rows_line = means_line.shape[0]
    n_rows_occ = means_occ.shape[0]


    # Jitter for NR + R
    total_lines = n_rows * 2
    jitter_arr = np.linspace(-0.1, 0.1, total_lines)

    # ------------------------
    # LEFT HALF → NR (cols 0–2)
    # ------------------------
    if col < 3: # cols 0,1,2 are the left half of the fig
        for row in range(2):
            ax = axes[row, col] # determining which subplot to use
            if row < 1:
                for i in range(n_rows_line): # looping through the representations
                    x_shifted = x_vals + jitter_arr[i]

                    ax.errorbar(
                        x_shifted,
                        means_line[i],
                        yerr=err_line[i],
                        fmt='o-',  # doorgetrokken lijn
                        linewidth=2,
                        capsize=4,
                        color=colors[i],
                        alpha=0.9,
                        
                    )
            else:
                for i in range(n_rows_occ):
                    x_shifted = x_vals + jitter_arr[i]

                    ax.errorbar(
                        x_shifted,
                        means_occ[i],
                        yerr=err_occ[i],
                        fmt='o-',  # doorgetrokken lijn
                        linewidth=2,
                        capsize=4,
                        color=colors[i],
                        alpha=0.9,
                        # label=single_legend[i] if (row == 1 and col == 2) else None
                    )

    # ------------------------
    # RIGHT HALF → R (cols 3–5)
    # ------------------------
    else:
        for row in range(2):
            ax = axes[row, col]

            if row <1:

                for i in range(n_rows_line):
                    x_shifted = x_vals + jitter_arr[i + n_rows]

                    ax.errorbar(
                        x_shifted,
                        means_line[i],
                        yerr=err_line[i],
                        fmt='o:',
                        linewidth=2,
                        capsize=4,
                        color=colors[i],
                        alpha=0.9,
                        
                    )
            else: 
                for i in range(n_rows_occ):
                    x_shifted = x_vals + jitter_arr[i]

                    ax.errorbar(
                        x_shifted,
                        means_occ[i],
                        yerr=err_occ[i],
                        fmt='o:',
                        linewidth=2,
                        capsize=4,
                        color=colors[i],
                        alpha=0.9,
                        # label=single_legend[i] if (row == 1 and col == 5) else None
                    )

axes[0,0].set_title("Line-Walled Maze, \nCoordinates Output")
axes[1,0].set_title("Occupancy Grid Maze, \nCoordinates Output")
axes[0,1].set_title("Line-Walled Maze, \nAllocentric Output")
axes[1,1].set_title("Occupancy Grid Maze, \nAllocentric Output")
axes[0,2].set_title("Line-Walled Maze, \nEgocentric Output")
axes[1,2].set_title("Occupancy Grid Maze, \nEgocentric Output")
axes[0,3].set_title("Line-Walled Maze, \nCoordinates Output")
axes[1,3].set_title("Occupancy Grid Maze, \nCoordinates Output")
axes[0,4].set_title("Line-Walled Maze, \nAllocentric Output")
axes[1,4].set_title("Occupancy Grid Maze, \nAllocentric Output")
axes[0,5].set_title("Line-Walled Maze, \nEgocentric Output")
axes[1,5].set_title("Occupancy Grid Maze, \nEgocentric Output")
# Formatting
for col in range(6):
    for row in range(2):
        ax = axes[row, col]

        # ax.set_title(plot_configs[col][4], fontsize=11)
        ax.grid(axis='y', linestyle='--', alpha=0.5)

        if col < 3 and row == 0:
            ax.set_xticks(x_vals)
            ax.set_xticklabels(x_tick_lbls_line)
        elif col < 3 and row == 1:
            ax.set_xticks(x_vals)
            ax.set_xticklabels(x_tick_lbls_occupancy)
        elif col >= 3 and row == 0:
            ax.set_xticks(x_vals)
            ax.set_xticklabels(x_tick_lbls_line)
        else:
            ax.set_xticks(x_vals)
            ax.set_xticklabels(x_tick_lbls_occupancy)

        if col == 0:
            ax.set_ylabel("Number of Correct Consecutive Steps")

        if row == 1:
            ax.set_xlabel("Maze Size")

    
    # # Save handles from the last plot (Bottom-Right) because it contains all 12 lines
    # if idx == 5:
    #     handles_for_legend, labels_for_legend = ax.get_legend_handles_labels()



plt.suptitle("Number of Correct Consecutive Steps", x=0.85*0.5, fontweight='bold')
# Position the legend within that white space
# legend=fig.legend(
#     handles_for_legend, 
#     labels_for_legend, 
#     loc='center right',           # Align the right side of the legend...
#     bbox_to_anchor=(0.99, 0.5),  # ...to the side of the figure
#     title="Input Formats & Models",
#     borderaxespad=0.
# )
# Make the legend title bold
# legend.get_title().set_fontweight('bold')


# -----------------------
# try making a legend

# --- Legend Group Definitions ---
spacer_handle = (
Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
pro_handle = (
Line2D([], [], marker='none', color='grey', linestyle = ':'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
),
flashlite_handle = (
Line2D([], [], marker='none', color='grey', linestyle = '-'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
)


handles = [
spacer_handle,
pro_handle,
flashlite_handle,
spacer_handle,

Line2D([], [], marker='o', color=colors[0], linestyle='None', markersize = 10),  # Adjacency JSON
Line2D([], [], marker='o', color=colors[1], linestyle='None', markersize = 10),  # Adjacency Text
Line2D([], [], marker='o', color=colors[2], linestyle='None', markersize = 10),  # JPG
Line2D([], [], marker='o', color=colors[3], linestyle='None', markersize = 10),  # JSON
Line2D([], [], marker='o', color=colors[4], linestyle='None', markersize = 10),  # Tokenized
Line2D([], [], marker='o', color=colors[5], linestyle='None', markersize = 10),  # ASCII

]
labels = [
r"$\bf{Models}$",
"Gemini 2.5 Pro", "Gemini 2.5 Flash-Lite",
r"$\bf{Input\ Formats}$",
"Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"
]
axes[1,5].legend(
handles,
labels,
handler_map={tuple: HandlerTuple(ndivide=None)},
loc='center left',
bbox_to_anchor=(1.02, 0.5),
title="Legend"
)





plt.tight_layout()
# Adjust right margin to make room for the legend
plt.subplots_adjust(right=0.85) 
plt.show()



























# THIS WORKS AS A WHOLE!!!! Makes 6 raw score figs. top: line, bottom: occ. R and NR in the same graph each time. L: coords, M: allo, R: ego

# # 1. Define the Legend Labels
# single_legend = [
#     'Adjacency Json - Gemini 2.5 Flash-Lite', 
#     'Adjacency Text - Gemini 2.5 Flash-Lite', 
#     'JPG - Gemini 2.5 Flash-Lite', 
#     'JSON - Gemini 2.5 Flash-Lite', 
#     'Tokenized - Gemini 2.5 Flash-Lite', 
#     'ASCII - Gemini 2.5 Flash-Lite', 
#     'Adjacency Json - Gemini 2.5 Pro', 
#     'Adjacency Text - Gemini 2.5 Pro', 
#     'JPG - Gemini 2.5 Pro', 
#     'JSON - Gemini 2.5 Pro', 
#     'Tokenized - Gemini 2.5 Pro', 
#     'ASCII - Gemini 2.5 Pro'
# ]

# # 2. Organize Data into Groups for the 6 Subplots
# # Structure: (Means_NR, Means_R, Err_NR, Err_R, Title)
# # NR = Non-Reasoning (Solid), R = Reasoning (Dotted)
# plot_configs = [
#     # Top-Left: line coords
#     (means_line_NR_coords, means_line_R_coords, 
#      error_line_NR_coords, error_line_R_coords, 
#      "Line-Walled Maze, Coordinates Output"),
    
#     # Top-Middle: line allo
#     (means_line_NR_allo, means_line_R_allo, 
#      error_line_NR_allo, error_line_R_allo, 
#      "Line-Walled Maze, Allocentric Output"),
    
#     # Top-Right: line ego
#     (means_line_NR_ego, means_line_R_ego, 
#      error_line_NR_ego, error_line_R_ego, 
#      "Line-Walled Maze, Egocentric Output"),
    
#     # Bottom-Left: occupancy coords
#     (means_occ_NR_coords, means_occ_R_coords, 
#      error_occupancy_NR_coords, error_occupancy_R_coords, 
#      "Occupancy Grid Maze, Coordinates Output"),
    
#     # Bottom-Middle: occupancy allo
#     (means_occ_NR_allo, means_occ_R_allo, 
#      error_occupancy_NR_allo, error_occupancy_R_allo, 
#      "Occupancy Grid Maze, Allocentric Output"),
    
#     # Bottom-Right: occupancy ego
#     (means_occ_NR_ego, means_occ_R_ego, 
#      error_occupancy_NR_ego, error_occupancy_R_ego, 
#      "Occupancy Grid Maze, Egocentric Output"),
# ]

# # 3. Setup Plotting Parameters
# x_vals = np.arange(3)
# x_tick_lbls_line = ["3x3", "6x6", "15x15"] # Complexity levels
# x_tick_lbls_occupancy = ["7x7", "13x13", "31x31"] # Complexity levels
# # Define a color palette for the 6 distinct methods (ignoring model version)
# # We have 6 base methods (Adj Json, Adj Text, JPG, JSON, Tok, ASCII)
# colors = plt.cm.tab10(np.linspace(0, 1, 10))[:6] 

# fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(9, 8), sharey=True, sharex=False)

# # Container to grab handles/labels for the global legend later
# handles_for_legend = []
# labels_for_legend = []

# # 4. Main Plotting Loop
# for idx, ax in enumerate(axes.flat):
#     print("idx: ", idx)
#     print("ax: ", ax)
#     means_nr, means_r, err_nr, err_r, title = plot_configs[idx]
    
#     # Convert to numpy arrays just in case
#     means_nr = np.array(means_nr)
#     means_r = np.array(means_r)
#     err_nr = np.array(err_nr)
#     err_r = np.array(err_r)

#     # Determine number of lines (5 for top row, 6 for bottom row)
#     n_rows = means_nr.shape[0] 
    
#     # Calculate jitter
#     # We have n_rows * 2 lines (NR + R). We spread them slightly around x.
#     total_lines = n_rows * 2
#     jitter_arr = np.linspace(-0.1, 0.1, total_lines)
    
#     # --- Plot NR Lines (Solid) ---
#     # These correspond to the first 'n_rows' of the single_legend
#     for i in range(n_rows):
#         # Specific jitter for this line
#         x_shifted = x_vals + jitter_arr[i]
        
#         ax.errorbar(
#             x_shifted,
#             means_nr[i],
#             yerr=err_nr[i],
#             fmt='o-',            # Solid line with markers
#             linewidth=2,
#             capsize=4,
#             label=single_legend[i],
#             color=colors[i],      # Assign color based on method type
#             alpha=0.9
#         )

#     # --- Plot R Lines (Dotted) ---
#     # These correspond to the second half of the single_legend, adjusted by offset
#     # Legend structure is [6 items FL] + [6 items Pro]. 
#     # Index for R corresponds to i + 6.
#     for i in range(n_rows):
#         # Specific jitter for this line (offset from NR lines)
#         x_shifted = x_vals + jitter_arr[i + n_rows]
        
#         # Calculate legend index (jump over the 6 FL items)
#         leg_idx = i + 6
        
#         ax.errorbar(
#             x_shifted,
#             means_r[i],
#             yerr=err_r[i],
#             fmt='o:',            # Dotted line (:) with markers
#             linewidth=2,
#             capsize=4,
#             label=single_legend[leg_idx],
#             color=colors[i],      # Same color as the NR counterpart
#             alpha=0.9
#         )


#     # Formatting
#     if idx < 3:
#         x_tick_lbls = x_tick_lbls_line
#     else:
#         x_tick_lbls = x_tick_lbls_occupancy
#         ax.set_xlabel("Maze Complexity")
#     ax.set_title(title, fontsize=11)
#     ax.set_xticks(x_vals)
#     ax.set_xticklabels(x_tick_lbls)
#     ax.grid(axis='y', linestyle='--', alpha=0.5)
    
#     if idx % 3 == 0:
#         ax.set_ylabel("Number of Correct Consecutive Steps")
    


    
#     # Save handles from the last plot (Bottom-Right) because it contains all 12 lines
#     if idx == 5:
#         handles_for_legend, labels_for_legend = ax.get_legend_handles_labels()



# plt.suptitle("Performance Scaling", x=0.82*0.5, fontweight='bold')
# # Position the legend within that white space
# legend=fig.legend(
#     handles_for_legend, 
#     labels_for_legend, 
#     loc='center left',           # Align the LEFT side of the legend...
#     bbox_to_anchor=(0.78, 0.5),  # ...to the point just after the plots (0.72)
#     title="Input Formats & Models",
#     borderaxespad=0.
# )
# # Make the legend title bold
# legend.get_title().set_fontweight('bold')

# plt.tight_layout()
# # Adjust right margin to make room for the legend
# plt.subplots_adjust(right=0.75) 
# plt.show()

