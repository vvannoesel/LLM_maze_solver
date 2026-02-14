import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15

x_axis_line = ['3x3', '6x6', '15x15']
x_axis_occ = ['7x7', '13x13', '31x31']

def sample_size(sigma):
    """Calculates the required sample size for a given standard deviation and margin of error."""
    Z = 1.96  # Z-score for 95% confidence level
    E = 5.0   # Margin of error
    n = (Z * sigma / E) ** 2
    return np.ceil(n)


# # --- Statistical determination of sample size ----------

# NR -- Coords -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Averages 3x3
avg_line_adj_json = np.mean(r3.line_NR_coords_adj_json_3)
avg_line_adj_txt = np.mean(r3.line_NR_coords_adj_txt_3)
avg_line_jpg = np.mean(r3.line_NR_coords_jpg_3)
avg_line_json = np.mean(r3.line_NR_coords_json_3)
avg_line_tokenized_txt = np.mean(r3.line_NR_coords_tokenized_txt_3)
avg_occupancy_adj_json = np.mean(r3.occupancy_NR_coords_adj_json_3)
avg_occupancy_adj_txt = np.mean(r3.occupancy_NR_coords_adj_txt_3)
avg_occupancy_ascii_txt = np.mean(r3.occupancy_NR_coords_ascii_txt_3)  
avg_occupancy_jpg = np.mean(r3.occupancy_NR_coords_jpg_3)
avg_occupancy_json = np.mean(r3.occupancy_NR_coords_json_3)
avg_occupancy_tokenized_txt = np.mean(r3.occupancy_NR_coords_tokenized_txt_3)

# Accuracy NR Coords 6x6 averages
avg_line_adj_json_6 = np.mean(r6.line_NR_coords_adj_json_6)
avg_line_adj_txt_6 = np.mean(r6.line_NR_coords_adj_txt_6)
avg_line_jpg_6 = np.mean(r6.line_NR_coords_jpg_6)
avg_line_json_6 = np.mean(r6.line_NR_coords_json_6)
avg_line_tokenized_txt_6 = np.mean(r6.line_NR_coords_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(r6.occupancy_NR_coords_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(r6.occupancy_NR_coords_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(r6.occupancy_NR_coords_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(r6.occupancy_NR_coords_jpg_6)
avg_occupancy_json_6 = np.mean(r6.occupancy_NR_coords_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(r6.occupancy_NR_coords_tokenized_txt_6)

# Accuracy NR Coords 15x15 averages
avg_line_adj_json_15 = np.mean(r15.line_NR_coords_adj_json_15)
avg_line_adj_txt_15 = np.mean(r15.line_NR_coords_adj_txt_15)
avg_line_jpg_15 = np.mean(r15.line_NR_coords_jpg_15)
avg_line_json_15 = np.mean(r15.line_NR_coords_json_15)
avg_line_tokenized_txt_15 = np.mean(r15.line_NR_coords_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(r15.occupancy_NR_coords_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(r15.occupancy_NR_coords_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(r15.occupancy_NR_coords_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(r15.occupancy_NR_coords_jpg_15)
avg_occupancy_json_15 = np.mean(r15.occupancy_NR_coords_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(r15.occupancy_NR_coords_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Flash-Lite, Coordinates Output", fontsize=16, pad=20)

sample_sizes_3x3_NR_coords = [
    sample_size(np.std(r3.line_NR_coords_adj_json_3)),
    sample_size(np.std(r3.line_NR_coords_adj_txt_3)),
    sample_size(np.std(r3.line_NR_coords_jpg_3)),
    sample_size(np.std(r3.line_NR_coords_json_3)),
    sample_size(np.std(r3.line_NR_coords_tokenized_txt_3)),
    sample_size(np.std(r3.occupancy_NR_coords_adj_json_3)),
    sample_size(np.std(r3.occupancy_NR_coords_adj_txt_3)),
    sample_size(np.std(r3.occupancy_NR_coords_ascii_txt_3)),
    sample_size(np.std(r3.occupancy_NR_coords_jpg_3)),
    sample_size(np.std(r3.occupancy_NR_coords_json_3)),
    sample_size(np.std(r3.occupancy_NR_coords_tokenized_txt_3))
    ]
sample_sizes_6x6_NR_coords=[
    sample_size(np.std(r6.line_NR_coords_adj_json_6)),
    sample_size(np.std(r6.line_NR_coords_adj_txt_6)),
    sample_size(np.std(r6.line_NR_coords_jpg_6)),
    sample_size(np.std(r6.line_NR_coords_json_6)),
    sample_size(np.std(r6.line_NR_coords_tokenized_txt_6)),
    sample_size(np.std(r6.occupancy_NR_coords_adj_json_6)),
    sample_size(np.std(r6.occupancy_NR_coords_adj_txt_6)),
    sample_size(np.std(r6.occupancy_NR_coords_ascii_txt_6)),
    sample_size(np.std(r6.occupancy_NR_coords_jpg_6)),
    sample_size(np.std(r6.occupancy_NR_coords_json_6)),
    sample_size(np.std(r6.occupancy_NR_coords_tokenized_txt_6)) ]
sample_sizes_15x15_NR_coords=[
    sample_size(np.std(r15.line_NR_coords_adj_json_15)),
    sample_size(np.std(r15.line_NR_coords_adj_txt_15)),
    sample_size(np.std(r15.line_NR_coords_jpg_15)),
    sample_size(np.std(r15.line_NR_coords_json_15)),
    sample_size(np.std(r15.line_NR_coords_tokenized_txt_15)),
    sample_size(np.std(r15.occupancy_NR_coords_adj_json_15)),
    sample_size(np.std(r15.occupancy_NR_coords_adj_txt_15)),
    sample_size(np.std(r15.occupancy_NR_coords_ascii_txt_15)),
    sample_size(np.std(r15.occupancy_NR_coords_jpg_15)),
    sample_size(np.std(r15.occupancy_NR_coords_json_15)),
    sample_size(np.std(r15.occupancy_NR_coords_tokenized_txt_15)) ]

# NR -- Allo -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Allo 3x3 averages
avg_line_adj_json = np.mean(r3.line_NR_allo_adj_json_3)
avg_line_adj_txt = np.mean(r3.line_NR_allo_adj_txt_3)
avg_line_jpg = np.mean(r3.line_NR_allo_jpg_3)
avg_line_json = np.mean(r3.line_NR_allo_json_3)
avg_line_tokenized_txt = np.mean(r3.line_NR_allo_tokenized_txt_3)
avg_occupancy_adj_json = np.mean(r3.occupancy_NR_allo_adj_json_3)
avg_occupancy_adj_txt = np.mean(r3.occupancy_NR_allo_adj_txt_3)
avg_occupancy_ascii_txt = np.mean(r3.occupancy_NR_allo_ascii_txt_3)  
avg_occupancy_jpg = np.mean(r3.occupancy_NR_allo_jpg_3)
avg_occupancy_json = np.mean(r3.occupancy_NR_allo_json_3)
avg_occupancy_tokenized_txt = np.mean(r3.occupancy_NR_allo_tokenized_txt_3)

# Accuracy NR Allo 6x6 averages

avg_line_adj_json_6 = np.mean(r6.line_NR_allo_adj_json_6)
avg_line_adj_txt_6 = np.mean(r6.line_NR_allo_adj_txt_6)
avg_line_jpg_6 = np.mean(r6.line_NR_allo_jpg_6)
avg_line_json_6 = np.mean(r6.line_NR_allo_json_6)
avg_line_tokenized_txt_6 = np.mean(r6.line_NR_allo_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(r6.occupancy_NR_allo_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(r6.occupancy_NR_allo_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(r6.occupancy_NR_allo_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(r6.occupancy_NR_allo_jpg_6)
avg_occupancy_json_6 = np.mean(r6.occupancy_NR_allo_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(r6.occupancy_NR_allo_tokenized_txt_6)


# Accuracy NR Allo 15x15 averages
avg_line_adj_json_15 = np.mean(r15.line_NR_allo_adj_json_15)
avg_line_adj_txt_15 = np.mean(r15.line_NR_allo_adj_txt_15)
avg_line_jpg_15 = np.mean(r15.line_NR_allo_jpg_15)
avg_line_json_15 = np.mean(r15.line_NR_allo_json_15)
avg_line_tokenized_txt_15 = np.mean(r15.line_NR_allo_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(r15.occupancy_NR_allo_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(r15.occupancy_NR_allo_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(r15.occupancy_NR_allo_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(r15.occupancy_NR_allo_jpg_15)
avg_occupancy_json_15 = np.mean(r15.occupancy_NR_allo_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(r15.occupancy_NR_allo_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Flash-Lite, Allocentric Output", fontsize=16, pad=20)

sample_sizes_3x3_NR_allo = [
    sample_size(np.std(r3.line_NR_allo_adj_json_3)),
    sample_size(np.std(r3.line_NR_allo_adj_txt_3)),
    sample_size(np.std(r3.line_NR_allo_jpg_3)),
    sample_size(np.std(r3.line_NR_allo_json_3)),
    sample_size(np.std(r3.line_NR_allo_tokenized_txt_3)),
    sample_size(np.std(r3.occupancy_NR_allo_adj_json_3)),
    sample_size(np.std(r3.occupancy_NR_allo_adj_txt_3)),
    sample_size(np.std(r3.occupancy_NR_allo_ascii_txt_3)),
    sample_size(np.std(r3.occupancy_NR_allo_jpg_3)),
    sample_size(np.std(r3.occupancy_NR_allo_json_3)),
    sample_size(np.std(r3.occupancy_NR_allo_tokenized_txt_3))
    ]
sample_sizes_6x6_NR_allo=[
    sample_size(np.std(r6.line_NR_allo_adj_json_6)),
    sample_size(np.std(r6.line_NR_allo_adj_txt_6)),
    sample_size(np.std(r6.line_NR_allo_jpg_6)),
    sample_size(np.std(r6.line_NR_allo_json_6)),
    sample_size(np.std(r6.line_NR_allo_tokenized_txt_6)),
    sample_size(np.std(r6.occupancy_NR_allo_adj_json_6)),
    sample_size(np.std(r6.occupancy_NR_allo_adj_txt_6)),
    sample_size(np.std(r6.occupancy_NR_allo_ascii_txt_6)),
    sample_size(np.std(r6.occupancy_NR_allo_jpg_6)),
    sample_size(np.std(r6.occupancy_NR_allo_json_6)),
    sample_size(np.std(r6.occupancy_NR_allo_tokenized_txt_6)) ]
sample_sizes_15x15_NR_allo=[
    sample_size(np.std(r15.line_NR_allo_adj_json_15)),
    sample_size(np.std(r15.line_NR_allo_adj_txt_15)),
    sample_size(np.std(r15.line_NR_allo_jpg_15)),
    sample_size(np.std(r15.line_NR_allo_json_15)),
    sample_size(np.std(r15.line_NR_allo_tokenized_txt_15)),
    sample_size(np.std(r15.occupancy_NR_allo_adj_json_15)),
    sample_size(np.std(r15.occupancy_NR_allo_adj_txt_15)),
    sample_size(np.std(r15.occupancy_NR_allo_ascii_txt_15)),
    sample_size(np.std(r15.occupancy_NR_allo_jpg_15)),
    sample_size(np.std(r15.occupancy_NR_allo_json_15)),
    sample_size(np.std(r15.occupancy_NR_allo_tokenized_txt_15)) ]

# NR -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Ego 3x3 averages
avg_line_adj_json = np.mean(r3.line_NR_ego_adj_json_3)
avg_line_adj_txt = np.mean(r3.line_NR_ego_adj_txt_3)
avg_line_jpg = np.mean(r3.line_NR_ego_jpg_3)
avg_line_json = np.mean(r3.line_NR_ego_json_3)
avg_line_tokenized_txt = np.mean(r3.line_NR_ego_tokenized_txt_3)
avg_occupancy_adj_json = np.mean(r3.occupancy_NR_ego_adj_json_3)
avg_occupancy_adj_txt = np.mean(r3.occupancy_NR_ego_adj_txt_3)
avg_occupancy_ascii_txt = np.mean(r3.occupancy_NR_ego_ascii_txt_3)  
avg_occupancy_jpg = np.mean(r3.occupancy_NR_ego_jpg_3)
avg_occupancy_json = np.mean(r3.occupancy_NR_ego_json_3)
avg_occupancy_tokenized_txt = np.mean(r3.occupancy_NR_ego_tokenized_txt_3)

# Accuracy NR Ego 6x6 averages
avg_line_adj_json_6 = np.mean(r6.line_NR_ego_adj_json_6)
avg_line_adj_txt_6 = np.mean(r6.line_NR_ego_adj_txt_6)
avg_line_jpg_6 = np.mean(r6.line_NR_ego_jpg_6)
avg_line_json_6 = np.mean(r6.line_NR_ego_json_6)
avg_line_tokenized_txt_6 = np.mean(r6.line_NR_ego_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(r6.occupancy_NR_ego_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(r6.occupancy_NR_ego_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(r6.occupancy_NR_ego_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(r6.occupancy_NR_ego_jpg_6)
avg_occupancy_json_6 = np.mean(r6.occupancy_NR_ego_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(r6.occupancy_NR_ego_tokenized_txt_6)

# Accuracy NR Ego 15x15 averages
avg_line_adj_json_15 = np.mean(r15.line_NR_ego_adj_json_15)
avg_line_adj_txt_15 = np.mean(r15.line_NR_ego_adj_txt_15)
avg_line_jpg_15 = np.mean(r15.line_NR_ego_jpg_15)
avg_line_json_15 = np.mean(r15.line_NR_ego_json_15)
avg_line_tokenized_txt_15 = np.mean(r15.line_NR_ego_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(r15.occupancy_NR_ego_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(r15.occupancy_NR_ego_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(r15.occupancy_NR_ego_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(r15.occupancy_NR_ego_jpg_15)
avg_occupancy_json_15 = np.mean(r15.occupancy_NR_ego_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(r15.occupancy_NR_ego_tokenized_txt_15)


# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Flash-Lite, Egocentric Output", fontsize=16, pad=20)

sample_sizes_3x3_NR_ego = [
    sample_size(np.std(r3.line_NR_ego_adj_json_3)),
    sample_size(np.std(r3.line_NR_ego_adj_txt_3)),
    sample_size(np.std(r3.line_NR_ego_jpg_3)),
    sample_size(np.std(r3.line_NR_ego_json_3)),
    sample_size(np.std(r3.line_NR_ego_tokenized_txt_3)),
    sample_size(np.std(r3.occupancy_NR_ego_adj_json_3)),
    sample_size(np.std(r3.occupancy_NR_ego_adj_txt_3)),
    sample_size(np.std(r3.occupancy_NR_ego_ascii_txt_3)),
    sample_size(np.std(r3.occupancy_NR_ego_jpg_3)),
    sample_size(np.std(r3.occupancy_NR_ego_json_3)),
    sample_size(np.std(r3.occupancy_NR_ego_tokenized_txt_3))
    ]
sample_sizes_6x6_NR_ego=[
    sample_size(np.std(r6.line_NR_ego_adj_json_6)),
    sample_size(np.std(r6.line_NR_ego_adj_txt_6)),
    sample_size(np.std(r6.line_NR_ego_jpg_6)),
    sample_size(np.std(r6.line_NR_ego_json_6)),
    sample_size(np.std(r6.line_NR_ego_tokenized_txt_6)),
    sample_size(np.std(r6.occupancy_NR_ego_adj_json_6)),
    sample_size(np.std(r6.occupancy_NR_ego_adj_txt_6)),
    sample_size(np.std(r6.occupancy_NR_ego_ascii_txt_6)),
    sample_size(np.std(r6.occupancy_NR_ego_jpg_6)),
    sample_size(np.std(r6.occupancy_NR_ego_json_6)),
    sample_size(np.std(r6.occupancy_NR_ego_tokenized_txt_6)) ]
sample_sizes_15x15_NR_ego=[
    sample_size(np.std(r15.line_NR_ego_adj_json_15)),
    sample_size(np.std(r15.line_NR_ego_adj_txt_15)),
    sample_size(np.std(r15.line_NR_ego_jpg_15)),
    sample_size(np.std(r15.line_NR_ego_json_15)),
    sample_size(np.std(r15.line_NR_ego_tokenized_txt_15)),
    sample_size(np.std(r15.occupancy_NR_ego_adj_json_15)),
    sample_size(np.std(r15.occupancy_NR_ego_adj_txt_15)),
    sample_size(np.std(r15.occupancy_NR_ego_ascii_txt_15)),
     sample_size(np.std(r15.occupancy_NR_ego_jpg_15)),
    sample_size(np.std(r15.occupancy_NR_ego_json_15)),
    sample_size(np.std(r15.occupancy_NR_ego_tokenized_txt_15))]

# R -- Coords -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Coords 3x3 averages
avg_line_adj_json = np.mean(r3.line_R_coords_adj_json_3)
avg_line_adj_txt = np.mean(r3.line_R_coords_adj_txt_3)
avg_line_jpg = np.mean(r3.line_R_coords_jpg_3)
avg_line_json = np.mean(r3.line_R_coords_json_3)
avg_line_tokenized_txt = np.mean(r3.line_R_coords_tokenized_txt_3)
avg_occupancy_adj_json = np.mean(r3.occupancy_R_coords_adj_json_3)
avg_occupancy_adj_txt = np.mean(r3.occupancy_R_coords_adj_txt_3)
avg_occupancy_ascii_txt = np.mean(r3.occupancy_R_coords_ascii_txt_3)  
avg_occupancy_jpg = np.mean(r3.occupancy_R_coords_jpg_3)
avg_occupancy_json = np.mean(r3.occupancy_R_coords_json_3)
avg_occupancy_tokenized_txt = np.mean(r3.occupancy_R_coords_tokenized_txt_3)

# Accuracy R Coords 6x6 averages
avg_line_adj_json_6 = np.mean(r6.line_R_coords_adj_json_6)
avg_line_adj_txt_6 = np.mean(r6.line_R_coords_adj_txt_6)
avg_line_jpg_6 = np.mean(r6.line_R_coords_jpg_6)
avg_line_json_6 = np.mean(r6.line_R_coords_json_6)
avg_line_tokenized_txt_6 = np.mean(r6.line_R_coords_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(r6.occupancy_R_coords_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(r6.occupancy_R_coords_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(r6.occupancy_R_coords_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(r6.occupancy_R_coords_jpg_6)
avg_occupancy_json_6 = np.mean(r6.occupancy_R_coords_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(r6.occupancy_R_coords_tokenized_txt_6)

# Accuracy R Coords 15x15 averages
avg_line_adj_json_15 = np.mean(r15.line_R_coords_adj_json_15)
avg_line_adj_txt_15 = np.mean(r15.line_R_coords_adj_txt_15)
avg_line_jpg_15 = np.mean(r15.line_R_coords_jpg_15)
avg_line_json_15 = np.mean(r15.line_R_coords_json_15)
avg_line_tokenized_txt_15 = np.mean(r15.line_R_coords_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(r15.occupancy_R_coords_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(r15.occupancy_R_coords_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(r15.occupancy_R_coords_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(r15.occupancy_R_coords_jpg_15)
avg_occupancy_json_15 = np.mean(r15.occupancy_R_coords_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(r15.occupancy_R_coords_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Pro, Coordinates Output", fontsize=16, pad=20)

sample_sizes_3x3_R_coords = [
    sample_size(np.std(r3.line_R_coords_adj_json_3)),
    sample_size(np.std(r3.line_R_coords_adj_txt_3)),
    sample_size(np.std(r3.line_R_coords_jpg_3)),
    sample_size(np.std(r3.line_R_coords_json_3)),
    sample_size(np.std(r3.line_R_coords_tokenized_txt_3)),
    sample_size(np.std(r3.occupancy_R_coords_adj_json_3)),
    sample_size(np.std(r3.occupancy_R_coords_adj_txt_3)),
    sample_size(np.std(r3.occupancy_R_coords_ascii_txt_3)),
    sample_size(np.std(r3.occupancy_R_coords_jpg_3)),
    sample_size(np.std(r3.occupancy_R_coords_json_3)),
    sample_size(np.std(r3.occupancy_R_coords_tokenized_txt_3))
    ]
sample_sizes_6x6_R_coords=[
    sample_size(np.std(r6.line_R_coords_adj_json_6)),
    sample_size(np.std(r6.line_R_coords_adj_txt_6)),
    sample_size(np.std(r6.line_R_coords_jpg_6)),
    sample_size(np.std(r6.line_R_coords_json_6)),
    sample_size(np.std(r6.line_R_coords_tokenized_txt_6)),
    sample_size(np.std(r6.occupancy_R_coords_adj_json_6)),
    sample_size(np.std(r6.occupancy_R_coords_adj_txt_6)),
    sample_size(np.std(r6.occupancy_R_coords_ascii_txt_6)),
    sample_size(np.std(r6.occupancy_R_coords_jpg_6)),
    sample_size(np.std(r6.occupancy_R_coords_json_6)),
    sample_size(np.std(r6.occupancy_R_coords_tokenized_txt_6)) ]
sample_sizes_15x15_R_coords=[
    sample_size(np.std(r15.line_R_coords_adj_json_15)),
    sample_size(np.std(r15.line_R_coords_adj_txt_15)),
    sample_size(np.std(r15.line_R_coords_jpg_15)),
    sample_size(np.std(r15.line_R_coords_json_15)),
    sample_size(np.std(r15.line_R_coords_tokenized_txt_15)),
    sample_size(np.std(r15.occupancy_R_coords_adj_json_15)),
    sample_size(np.std(r15.occupancy_R_coords_adj_txt_15)),
    sample_size(np.std(r15.occupancy_R_coords_ascii_txt_15)),
     sample_size(np.std(r15.occupancy_R_coords_jpg_15)),
    sample_size(np.std(r15.occupancy_R_coords_json_15)),
    sample_size(np.std(r15.occupancy_R_coords_tokenized_txt_15)) ]


# # R -- Allo -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Allo 3x3 averages
avg_line_adj_json = np.mean(r3.line_R_allo_adj_json_3)
avg_line_adj_txt = np.mean(r3.line_R_allo_adj_txt_3)
avg_line_jpg = np.mean(r3.line_R_allo_jpg_3)
avg_line_json = np.mean(r3.line_R_allo_json_3)
avg_line_tokenized_txt = np.mean(r3.line_R_allo_tokenized_txt_3)
avg_occupancy_adj_json = np.mean(r3.occupancy_R_allo_adj_json_3)
avg_occupancy_adj_txt = np.mean(r3.occupancy_R_allo_adj_txt_3)
avg_occupancy_ascii_txt = np.mean(r3.occupancy_R_allo_ascii_txt_3)  
avg_occupancy_jpg = np.mean(r3.occupancy_R_allo_jpg_3)
avg_occupancy_json = np.mean(r3.occupancy_R_allo_json_3)
avg_occupancy_tokenized_txt = np.mean(r3.occupancy_R_allo_tokenized_txt_3)

# Accuracy R Allo 6x6 averages
avg_line_adj_json_6 = np.mean(r6.line_R_allo_adj_json_6)
avg_line_adj_txt_6 = np.mean(r6.line_R_allo_adj_txt_6)
avg_line_jpg_6 = np.mean(r6.line_R_allo_jpg_6)
avg_line_json_6 = np.mean(r6.line_R_allo_json_6)
avg_line_tokenized_txt_6 = np.mean(r6.line_R_allo_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(r6.occupancy_R_allo_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(r6.occupancy_R_allo_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(r6.occupancy_R_allo_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(r6.occupancy_R_allo_jpg_6)
avg_occupancy_json_6 = np.mean(r6.occupancy_R_allo_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(r6.occupancy_R_allo_tokenized_txt_6)

# Accuracy R Allo 15x15 averages
avg_line_adj_json_15 = np.mean(r15.line_R_allo_adj_json_15)
avg_line_adj_txt_15 = np.mean(r15.line_R_allo_adj_txt_15)
avg_line_jpg_15 = np.mean(r15.line_R_allo_jpg_15)
avg_line_json_15 = np.mean(r15.line_R_allo_json_15)
avg_line_tokenized_txt_15 = np.mean(r15.line_R_allo_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(r15.occupancy_R_allo_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(r15.occupancy_R_allo_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(r15.occupancy_R_allo_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(r15.occupancy_R_allo_jpg_15)
avg_occupancy_json_15 = np.mean(r15.occupancy_R_allo_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(r15.occupancy_R_allo_tokenized_txt_15)


# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Pro, Allocentric Output", fontsize=16, pad=20)

sample_sizes_3x3_R_allo = [
    sample_size(np.std(r3.line_R_allo_adj_json_3)),
    sample_size(np.std(r3.line_R_allo_adj_txt_3)),
    sample_size(np.std(r3.line_R_allo_jpg_3)),
    sample_size(np.std(r3.line_R_allo_json_3)),
    sample_size(np.std(r3.line_R_allo_tokenized_txt_3)),
    sample_size(np.std(r3.occupancy_R_allo_adj_json_3)),
    sample_size(np.std(r3.occupancy_R_allo_adj_txt_3)),
    sample_size(np.std(r3.occupancy_R_allo_ascii_txt_3)),
    sample_size(np.std(r3.occupancy_R_allo_jpg_3)),
    sample_size(np.std(r3.occupancy_R_allo_json_3)),
    sample_size(np.std(r3.occupancy_R_allo_tokenized_txt_3))
    ]
sample_sizes_6x6_R_allo=[
    sample_size(np.std(r6.line_R_allo_adj_json_6)),
    sample_size(np.std(r6.line_R_allo_adj_txt_6)),
    sample_size(np.std(r6.line_R_allo_jpg_6)),
    sample_size(np.std(r6.line_R_allo_json_6)),
    sample_size(np.std(r6.line_R_allo_tokenized_txt_6)),
    sample_size(np.std(r6.occupancy_R_allo_adj_json_6)),
    sample_size(np.std(r6.occupancy_R_allo_adj_txt_6)),
    sample_size(np.std(r6.occupancy_R_allo_ascii_txt_6)),
    sample_size(np.std(r6.occupancy_R_allo_jpg_6)),
    sample_size(np.std(r6.occupancy_R_allo_json_6)),
    sample_size(np.std(r6.occupancy_R_allo_tokenized_txt_6)) ]
sample_sizes_15x15_R_allo=[
    sample_size(np.std(r15.line_R_allo_adj_json_15)),
    sample_size(np.std(r15.line_R_allo_adj_txt_15)),
    sample_size(np.std(r15.line_R_allo_jpg_15)),
    sample_size(np.std(r15.line_R_allo_json_15)),
    sample_size(np.std(r15.line_R_allo_tokenized_txt_15)),
    sample_size(np.std(r15.occupancy_R_allo_adj_json_15)),
    sample_size(np.std(r15.occupancy_R_allo_adj_txt_15)),
    sample_size(np.std(r15.occupancy_R_allo_ascii_txt_15)),
     sample_size(np.std(r15.occupancy_R_allo_jpg_15)),
    sample_size(np.std(r15.occupancy_R_allo_json_15)),
    sample_size(np.std(r15.occupancy_R_allo_tokenized_txt_15)) ]

# # R -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Ego 3x3 averages
avg_line_adj_json = np.mean(r3.line_R_ego_adj_json_3)
avg_line_adj_txt = np.mean(r3.line_R_ego_adj_txt_3)
avg_line_jpg = np.mean(r3.line_R_ego_jpg_3)
avg_line_json = np.mean(r3.line_R_ego_json_3)
avg_line_tokenized_txt = np.mean(r3.line_R_ego_tokenized_txt_3)
avg_occupancy_adj_json = np.mean(r3.occupancy_R_ego_adj_json_3)
avg_occupancy_adj_txt = np.mean(r3.occupancy_R_ego_adj_txt_3)
avg_occupancy_ascii_txt = np.mean(r3.occupancy_R_ego_ascii_txt_3)  
avg_occupancy_jpg = np.mean(r3.occupancy_R_ego_jpg_3)
avg_occupancy_json = np.mean(r3.occupancy_R_ego_json_3)
avg_occupancy_tokenized_txt = np.mean(r3.occupancy_R_ego_tokenized_txt_3)

# Accuracy R Ego 6x6 averages
avg_line_adj_json_6 = np.mean(r6.line_R_ego_adj_json_6)
avg_line_adj_txt_6 = np.mean(r6.line_R_ego_adj_txt_6)
avg_line_jpg_6 = np.mean(r6.line_R_ego_jpg_6)
avg_line_json_6 = np.mean(r6.line_R_ego_json_6)
avg_line_tokenized_txt_6 = np.mean(r6.line_R_ego_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(r6.occupancy_R_ego_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(r6.occupancy_R_ego_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(r6.occupancy_R_ego_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(r6.occupancy_R_ego_jpg_6)
avg_occupancy_json_6 = np.mean(r6.occupancy_R_ego_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(r6.occupancy_R_ego_tokenized_txt_6)

# Accuracy R Ego 15x15 averages
avg_line_adj_json_15 = np.mean(r15.line_R_ego_adj_json_15)
avg_line_adj_txt_15 = np.mean(r15.line_R_ego_adj_txt_15)
avg_line_jpg_15 = np.mean(r15.line_R_ego_jpg_15)
avg_line_json_15 = np.mean(r15.line_R_ego_json_15)
avg_line_tokenized_txt_15 = np.mean(r15.line_R_ego_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(r15.occupancy_R_ego_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(r15.occupancy_R_ego_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(r15.occupancy_R_ego_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(r15.occupancy_R_ego_jpg_15)
avg_occupancy_json_15 = np.mean(r15.occupancy_R_ego_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(r15.occupancy_R_ego_tokenized_txt_15)


sample_sizes_3x3_R_ego = [
    sample_size(np.std(r3.line_R_ego_adj_json_3)),
    sample_size(np.std(r3.line_R_ego_adj_txt_3)),
    sample_size(np.std(r3.line_R_ego_jpg_3)),
    sample_size(np.std(r3.line_R_ego_json_3)),
    sample_size(np.std(r3.line_R_ego_tokenized_txt_3)),
    sample_size(np.std(r3.occupancy_R_ego_adj_json_3)),
    sample_size(np.std(r3.occupancy_R_ego_adj_txt_3)),
    sample_size(np.std(r3.occupancy_R_ego_ascii_txt_3)),
    sample_size(np.std(r3.occupancy_R_ego_jpg_3)),
    sample_size(np.std(r3.occupancy_R_ego_json_3)),
    sample_size(np.std(r3.occupancy_R_ego_tokenized_txt_3))
    ]
sample_sizes_6x6_R_ego=[
    sample_size(np.std(r6.line_R_ego_adj_json_6)),
    sample_size(np.std(r6.line_R_ego_adj_txt_6)),
    sample_size(np.std(r6.line_R_ego_jpg_6)),
    sample_size(np.std(r6.line_R_ego_json_6)),
    sample_size(np.std(r6.line_R_ego_tokenized_txt_6)),
    sample_size(np.std(r6.occupancy_R_ego_adj_json_6)),
    sample_size(np.std(r6.occupancy_R_ego_adj_txt_6)),
    sample_size(np.std(r6.occupancy_R_ego_ascii_txt_6)),
    sample_size(np.std(r6.occupancy_R_ego_jpg_6)),
    sample_size(np.std(r6.occupancy_R_ego_json_6)),
    sample_size(np.std(r6.occupancy_R_ego_tokenized_txt_6)) ]
sample_sizes_15x15_R_ego=[
    sample_size(np.std(r15.line_R_ego_adj_json_15)),
    sample_size(np.std(r15.line_R_ego_adj_txt_15)),
    sample_size(np.std(r15.line_R_ego_jpg_15)),
    sample_size(np.std(r15.line_R_ego_json_15)),
    sample_size(np.std(r15.line_R_ego_tokenized_txt_15)),
    sample_size(np.std(r15.occupancy_R_ego_adj_json_15)),
    sample_size(np.std(r15.occupancy_R_ego_adj_txt_15)),
    sample_size(np.std(r15.occupancy_R_ego_ascii_txt_15)),
     sample_size(np.std(r15.occupancy_R_ego_jpg_15)),
    sample_size(np.std(r15.occupancy_R_ego_json_15)),
    sample_size(np.std(r15.occupancy_R_ego_tokenized_txt_15)) ]


# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Pro, Egocentric Output", fontsize=16, pad=20)


# --------- Plot a table showing required sample sizes and standard deviations for all complexities, output types and  ----------------------

# n_line_jpg_3 = sample_size(sd_line_jpg)
# n_occupancy_jpg_3 = sample_size(sd_occupancy_jpg)
# n_line_tokenized_txt_3 = sample_size(sd_line_tokenized_txt)
# n_occupancy_tokenized_txt_3 = sample_size(sd_occupancy_tokenized_txt)
# n_line_json_3 = sample_size(sd_line_json)
# n_occupancy_json_3 = sample_size(sd_occupancy_json)
# n_line_adj_txt_3 = sample_size(sd_line_adj_txt)
# n_occupancy_adj_txt_3 = sample_size(sd_occupancy_adj_txt)
# n_line_adj_json_3 = sample_size(sd_line_adj_json)
# n_occupancy_adj_json_3 = sample_size(sd_occupancy_adj_json)
# n_occupancy_ascii_txt_3 = sample_size(sd_occupancy_ascii_txt)
# n_line_jpg_6 = sample_size(sd_line_jpg_6)
# n_occupancy_jpg_6 = sample_size(sd_occupancy_jpg_6)
# n_line_tokenized_txt_6 = sample_size(sd_line_tokenized_txt_6)
# n_occupancy_tokenized_txt_6 = sample_size(sd_occupancy_tokenized_txt_6)
# n_line_json_6 = sample_size(sd_line_json_6)
# n_occupancy_json_6 = sample_size(sd_occupancy_json_6)
# n_line_adj_txt_6 = sample_size(sd_line_adj_txt_6)
# n_occupancy_adj_txt_6 = sample_size(sd_occupancy_adj_txt_6)
# n_line_adj_json_6 = sample_size(sd_line_adj_json_6)
# n_occupancy_adj_json_6 = sample_size(sd_occupancy_adj_json_6)
# n_occupancy_ascii_txt_6 = sample_size(sd_occupancy_ascii_txt_6) 
# n_line_jpg_15 = sample_size(sd_line_jpg_15)
# n_occupancy_jpg_15 = sample_size(sd_occupancy_jpg_15)
# n_line_tokenized_txt_15 = sample_size(sd_line_tokenized_txt_15)
# n_occupancy_tokenized_txt_15 = sample_size(sd_occupancy_tokenized_txt_15)
# n_line_json_15 = sample_size(sd_line_json_15)
# n_occupancy_json_15 = sample_size(sd_occupancy_json_15)
# n_line_adj_txt_15 = sample_size(sd_line_adj_txt_15)
# n_occupancy_adj_txt_15 = sample_size(sd_occupancy_adj_txt_15)
# n_line_adj_json_15 = sample_size(sd_line_adj_json_15)
# n_occupancy_adj_json_15 = sample_size(sd_occupancy_adj_json_15)
# n_occupancy_ascii_txt_15 = sample_size(sd_occupancy_ascii_txt_15) 

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

# sample_sizes_3x3 = [
#     n_line_jpg_3 ,
#     n_line_json_3,
#     n_line_adj_json_3,
#     n_line_adj_txt_3,
#     n_line_tokenized_txt_3,
#     n_occupancy_jpg_3,
#     n_occupancy_json_3,
#     n_occupancy_adj_json_3,
#     n_occupancy_adj_txt_3,
#     n_occupancy_ascii_txt_3,
#     n_occupancy_tokenized_txt_3 
#     ]
# sample_sizes_6x6=[
#     n_line_jpg_6 ,
#     n_line_json_6,
#     n_line_adj_json_6,
#     n_line_adj_txt_6,
#     n_line_tokenized_txt_6,
#     n_occupancy_jpg_6,
#     n_occupancy_json_6,
#     n_occupancy_adj_json_6,
#     n_occupancy_adj_txt_6,
#     n_occupancy_ascii_txt_6,
#     n_occupancy_tokenized_txt_6 ]
# sample_sizes_15x15=[
#     n_line_jpg_15,
#     n_line_json_15,
#     n_line_adj_json_15,
#     n_line_adj_txt_15,
#     n_line_tokenized_txt_15,
#     n_occupancy_jpg_15,
#     n_occupancy_json_15,
#     n_occupancy_adj_json_15,
#     n_occupancy_adj_txt_15,
#     n_occupancy_ascii_txt_15,
#     n_occupancy_tokenized_txt_15 ]


# std_3x3 = [
#     sd_line_jpg,
#     sd_line_json,        
#     sd_line_adj_json,
#     sd_line_adj_txt,
#     sd_line_tokenized_txt,
#     sd_occupancy_jpg,
#     sd_occupancy_json,
#     sd_occupancy_adj_json,
#     sd_occupancy_adj_txt,
#     sd_occupancy_ascii_txt,
#     sd_occupancy_tokenized_txt]

# std_6x6 = [
#     sd_line_jpg_6,
#     sd_line_json_6,        
#     sd_line_adj_json_6,
#     sd_line_adj_txt_6,
#     sd_line_tokenized_txt_6,
#     sd_occupancy_jpg_6,
#     sd_occupancy_json_6,
#     sd_occupancy_adj_json_6,
#     sd_occupancy_adj_txt_6,
#     sd_occupancy_ascii_txt_6,
#     sd_occupancy_tokenized_txt_6]
# std_15x15 = [
#     sd_line_jpg_15,
#     sd_line_json_15,        
#     sd_line_adj_json_15,
#     sd_line_adj_txt_15,
#     sd_line_tokenized_txt_15,
#     sd_occupancy_jpg_15,
#     sd_occupancy_json_15,
#     sd_occupancy_adj_json_15,
#     sd_occupancy_adj_txt_15,
#     sd_occupancy_ascii_txt_15,
#     sd_occupancy_tokenized_txt_15]

df = pd.DataFrame({
    "Representation": representations,
    "Sample Size Coordinates, \n Reasoning": sample_sizes_3x3_R_coords,
    "Sample Size Allocentric, \n Reasoning": sample_sizes_3x3_R_allo,
    "Sample Size Egocentric, \n Reasoning": sample_sizes_3x3_R_ego,
    "Sample Size Coordinates, \n Non-Reasoning": sample_sizes_3x3_NR_coords,
    "Sample Size Allocentric, \n Non-Reasoning": sample_sizes_3x3_NR_allo,
    "Sample Size Egocentric, \n Non-Reasoning": sample_sizes_3x3_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 3x3 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Types", fontsize=16, pad=20)


table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.0)

plt.tight_layout()
plt.show()


df = pd.DataFrame({
    "Representation": representations,

    "Sample Size Coordinates, \n Reasoning": sample_sizes_6x6_R_coords,
    "Sample Size Allocentric, \n Reasoning": sample_sizes_6x6_R_allo,
    "Sample Size Egocentric, \n Reasoning": sample_sizes_6x6_R_ego,
    "Sample Size Coordinates, \n Non-Reasoning": sample_sizes_6x6_NR_coords,
    "Sample Size Allocentric, \n Non-Reasoning": sample_sizes_6x6_NR_allo,
    "Sample Size Egocentric, \n Non-Reasoning": sample_sizes_6x6_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 6x6 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Types", fontsize=16, pad=20)


table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.0)

plt.tight_layout()
plt.show()


df = pd.DataFrame({
    "Representation": representations,
    "Sample Size Coordinates, \n Reasoning": sample_sizes_15x15_R_coords,
    "Sample Size Allocentric, \n Reasoning": sample_sizes_15x15_R_allo,
    "Sample Size Egocentric, \n Reasoning": sample_sizes_15x15_R_ego,
    "Sample Size Coordinates, \n Non-Reasoning": sample_sizes_15x15_NR_coords,
    "Sample Size Allocentric, \n Non-Reasoning": sample_sizes_15x15_NR_allo,
    "Sample Size Egocentric, \n Non-Reasoning": sample_sizes_15x15_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 15x15 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Types", fontsize=16, pad=20)


table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(True)
# table.set_fontsize(10)
table.scale(1.2, 2.0)

plt.tight_layout()
plt.show()