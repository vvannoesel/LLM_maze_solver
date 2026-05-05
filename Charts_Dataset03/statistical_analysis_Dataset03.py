"""
Created on Wed Nov 26 12:41:15 2025
@author: valer
This code calculates the necessary sample size to achieve a desired statistical power (α=0.05, error margin = 5%) 
for each representation and condition in the Dataset03 experiment.
"""


# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

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
avg_line_adj_json = np.nanmean(r3.line_NR_allo_adj_json_3)
avg_line_adj_txt = np.nanmean(r3.line_NR_allo_adj_txt_3)
avg_line_jpg = np.nanmean(r3.line_NR_allo_jpg_3)
avg_line_json = np.nanmean(r3.line_NR_allo_json_3)
avg_line_tokenized_txt = np.nanmean(r3.line_NR_allo_tokenized_txt_3)
avg_occupancy_adj_json = np.nanmean(r3.occupancy_NR_allo_adj_json_3)
avg_occupancy_adj_txt = np.nanmean(r3.occupancy_NR_allo_adj_txt_3)
avg_occupancy_ascii_txt = np.nanmean(r3.occupancy_NR_allo_ascii_txt_3)  
avg_occupancy_jpg = np.nanmean(r3.occupancy_NR_allo_jpg_3)
avg_occupancy_json = np.nanmean(r3.occupancy_NR_allo_json_3)
avg_occupancy_tokenized_txt = np.nanmean(r3.occupancy_NR_allo_tokenized_txt_3)

# Accuracy NR Allo 6x6 averages

avg_line_adj_json_6 = np.nanmean(r6.line_NR_allo_adj_json_6)
avg_line_adj_txt_6 = np.nanmean(r6.line_NR_allo_adj_txt_6)
avg_line_jpg_6 = np.nanmean(r6.line_NR_allo_jpg_6)
avg_line_json_6 = np.nanmean(r6.line_NR_allo_json_6)
avg_line_tokenized_txt_6 = np.nanmean(r6.line_NR_allo_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.nanmean(r6.occupancy_NR_allo_adj_json_6)
avg_occupancy_adj_txt_6 = np.nanmean(r6.occupancy_NR_allo_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.nanmean(r6.occupancy_NR_allo_ascii_txt_6)  
avg_occupancy_jpg_6 = np.nanmean(r6.occupancy_NR_allo_jpg_6)
avg_occupancy_json_6 = np.nanmean(r6.occupancy_NR_allo_json_6)
avg_occupancy_tokenized_txt_6 = np.nanmean(r6.occupancy_NR_allo_tokenized_txt_6)


# Accuracy NR Allo 15x15 averages
avg_line_adj_json_15 = np.nanmean(r15.line_NR_allo_adj_json_15)
avg_line_adj_txt_15 = np.nanmean(r15.line_NR_allo_adj_txt_15)
avg_line_jpg_15 = np.nanmean(r15.line_NR_allo_jpg_15)
avg_line_json_15 = np.nanmean(r15.line_NR_allo_json_15)
avg_line_tokenized_txt_15 = np.nanmean(r15.line_NR_allo_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.nanmean(r15.occupancy_NR_allo_adj_json_15)
avg_occupancy_adj_txt_15 = np.nanmean(r15.occupancy_NR_allo_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.nanmean(r15.occupancy_NR_allo_ascii_txt_15)  
avg_occupancy_jpg_15 = np.nanmean(r15.occupancy_NR_allo_jpg_15)
avg_occupancy_json_15 = np.nanmean(r15.occupancy_NR_allo_json_15)
avg_occupancy_tokenized_txt_15 = np.nanmean(r15.occupancy_NR_allo_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Flash-Lite, Allocentric Output", fontsize=16, pad=20)

sample_sizes_3x3_NR_allo = [
    sample_size(np.nanstd(r3.line_NR_allo_adj_json_3)),
    sample_size(np.nanstd(r3.line_NR_allo_adj_txt_3)),
    sample_size(np.nanstd(r3.line_NR_allo_jpg_3)),
    sample_size(np.nanstd(r3.line_NR_allo_json_3)),
    sample_size(np.nanstd(r3.line_NR_allo_tokenized_txt_3)),
    sample_size(np.nanstd(r3.occupancy_NR_allo_adj_json_3)),
    sample_size(np.nanstd(r3.occupancy_NR_allo_adj_txt_3)),
    sample_size(np.nanstd(r3.occupancy_NR_allo_ascii_txt_3)),
    sample_size(np.nanstd(r3.occupancy_NR_allo_jpg_3)),
    sample_size(np.nanstd(r3.occupancy_NR_allo_json_3)),
    sample_size(np.nanstd(r3.occupancy_NR_allo_tokenized_txt_3))
    ]
sample_sizes_6x6_NR_allo=[
    sample_size(np.nanstd(r6.line_NR_allo_adj_json_6)),
    sample_size(np.nanstd(r6.line_NR_allo_adj_txt_6)),
    sample_size(np.nanstd(r6.line_NR_allo_jpg_6)),
    sample_size(np.nanstd(r6.line_NR_allo_json_6)),
    sample_size(np.nanstd(r6.line_NR_allo_tokenized_txt_6)),
    sample_size(np.nanstd(r6.occupancy_NR_allo_adj_json_6)),
    sample_size(np.nanstd(r6.occupancy_NR_allo_adj_txt_6)),
    sample_size(np.nanstd(r6.occupancy_NR_allo_ascii_txt_6)),
    sample_size(np.nanstd(r6.occupancy_NR_allo_jpg_6)),
    sample_size(np.nanstd(r6.occupancy_NR_allo_json_6)),
    sample_size(np.nanstd(r6.occupancy_NR_allo_tokenized_txt_6)) ]
sample_sizes_15x15_NR_allo=[
    sample_size(np.nanstd(r15.line_NR_allo_adj_json_15)),
    sample_size(np.nanstd(r15.line_NR_allo_adj_txt_15)),
    sample_size(np.nanstd(r15.line_NR_allo_jpg_15)),
    sample_size(np.nanstd(r15.line_NR_allo_json_15)),
    sample_size(np.nanstd(r15.line_NR_allo_tokenized_txt_15)),
    sample_size(np.nanstd(r15.occupancy_NR_allo_adj_json_15)),
    sample_size(np.nanstd(r15.occupancy_NR_allo_adj_txt_15)),
    sample_size(np.nanstd(r15.occupancy_NR_allo_ascii_txt_15)),
    sample_size(np.nanstd(r15.occupancy_NR_allo_jpg_15)),
    sample_size(np.nanstd(r15.occupancy_NR_allo_json_15)),
    sample_size(np.nanstd(r15.occupancy_NR_allo_tokenized_txt_15)) ]

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


# --------- Plot a table showing required sample sizes   ----------------------


representations = [
    "Line-wall AL-JSON",
    "Line-wall AL-TXT",
    "Line-wall JPG",
    "Line-wall JSON",
    "Line-wall Tagged",
    "Occupancy AL-JSON",
    "Occupancy AL-TXT",
    "Occupancy ASCII",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tagged"
]


df = pd.DataFrame({
    "Representation": representations,
    "Sample Size Coordinates Output, \n Gemini 2.5 Pro": sample_sizes_3x3_R_coords,
    "Sample Size Abs. Directions Output, \n Gemini 2.5 Pro": sample_sizes_3x3_R_allo,
    "Sample Size Egocentric Output, \n Gemini 2.5 Pro": sample_sizes_3x3_R_ego,
    "Sample Size Coordinates Output, \n Gemini 2.5 Flash-Lite": sample_sizes_3x3_NR_coords,
    "Sample Size Abs. Directions Output, \n Gemini 2.5 Flash-Lite": sample_sizes_3x3_NR_allo,
    "Sample Size Egocentric Output, \n Gemini 2.5 Flash-Lite": sample_sizes_3x3_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 3x3/7x7 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Sample Sizes, Determined so that the 95% Confidence Interval for the Mean Completion Score Would Have a Half-Width No Greater Than 5 Percentage Points,\nComputed Separately for Each Combination of Input Representation, Output Frame of Reference, Maze Size, and LLM", fontsize=14)
plt.title("3x3/7x7 Mazes", fontsize=12)


table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2,2.5)

# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

plt.tight_layout()
# plt.show()


df = pd.DataFrame({
    "Representation": representations,

    "Sample Size Coordinates Output, \n Gemini 2.5 Pro": sample_sizes_6x6_R_coords,
    "Sample Size Abs. Directions Output, \n Gemini 2.5 Pro": sample_sizes_6x6_R_allo,
    "Sample Size Egocentric Output, \n Gemini 2.5 Pro": sample_sizes_6x6_R_ego,
    "Sample Size Coordinates Output, \n Gemini 2.5 Flash-Lite": sample_sizes_6x6_NR_coords,
    "Sample Size Abs. Directions Output, \n Gemini 2.5 Flash-Lite": sample_sizes_6x6_NR_allo,
    "Sample Size Egocentric Output, \n Gemini 2.5 Flash-Lite": sample_sizes_6x6_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 6x6/13x13 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Sample Sizes, Determined so that the 95% Confidence Interval for the Mean Completion Score Would Have a Half-Width No Greater Than 5 Percentage Points,\nComputed Separately for Each Combination of Input Representation, Output Frame of Reference, Maze Size, and LLM", fontsize=14)
plt.title("6x6/13x13 Mazes", fontsize=12)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.5)


# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

plt.tight_layout()
# plt.show()


df = pd.DataFrame({
    "Representation": representations,
    "Sample Size Coordinates Output, \n Gemini 2.5 Pro": sample_sizes_15x15_R_coords,
    "Sample Size Abs. Directions Output, \n Gemini 2.5 Pro": sample_sizes_15x15_R_allo,
    "Sample Size Egocentric Output, \n Gemini 2.5 Pro": sample_sizes_15x15_R_ego,
    "Sample Size Coordinates Output, \n Gemini 2.5 Flash-Lite": sample_sizes_15x15_NR_coords,
    "Sample Size Abs. Directions Output, \n Gemini 2.5 Flash-Lite": sample_sizes_15x15_NR_allo,
    "Sample Size Egocentric Output, \n Gemini 2.5 Flash-Lite": sample_sizes_15x15_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 15x15/31x31 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Sample Sizes, Determined so that the 95% Confidence Interval for the Mean Completion Score Would Have a Half-Width No Greater Than 5 Percentage Points,\nComputed Separately for Each Combination of Input Representation, Output Frame of Reference, Maze Size, and LLM", fontsize=14)
plt.title("15x15/31x31 Mazes", fontsize=12)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)


table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.5)


# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

plt.tight_layout()
# plt.show()





# ------------------------------------------------------------------------------------------------------------------
# Making tables with the SDs for each condition





sd_3x3_NR_coords = [
     np.std(r3.line_NR_coords_adj_json_3 ),
     np.std(r3.line_NR_coords_adj_txt_3 ),
     np.std(r3.line_NR_coords_jpg_3 ),
     np.std(r3.line_NR_coords_json_3 ),
     np.std(r3.line_NR_coords_tokenized_txt_3 ),
     np.std(r3.occupancy_NR_coords_adj_json_3 ),
     np.std(r3.occupancy_NR_coords_adj_txt_3 ),
     np.std(r3.occupancy_NR_coords_ascii_txt_3 ),
     np.std(r3.occupancy_NR_coords_jpg_3 ),
     np.std(r3.occupancy_NR_coords_json_3 ),
     np.std(r3.occupancy_NR_coords_tokenized_txt_3 )
]
sd_6x6_NR_coords=[
     np.std(r6.line_NR_coords_adj_json_6 ),
     np.std(r6.line_NR_coords_adj_txt_6 ),
     np.std(r6.line_NR_coords_jpg_6 ),
     np.std(r6.line_NR_coords_json_6 ),
     np.std(r6.line_NR_coords_tokenized_txt_6 ),
     np.std(r6.occupancy_NR_coords_adj_json_6 ),
     np.std(r6.occupancy_NR_coords_adj_txt_6 ),
     np.std(r6.occupancy_NR_coords_ascii_txt_6 ),
     np.std(r6.occupancy_NR_coords_jpg_6 ),
     np.std(r6.occupancy_NR_coords_json_6 ),
     np.std(r6.occupancy_NR_coords_tokenized_txt_6 ) ]
sd_15x15_NR_coords=[
     np.std(r15.line_NR_coords_adj_json_15 ),
     np.std(r15.line_NR_coords_adj_txt_15 ),
     np.std(r15.line_NR_coords_jpg_15 ),
     np.std(r15.line_NR_coords_json_15 ),
     np.std(r15.line_NR_coords_tokenized_txt_15 ),
     np.std(r15.occupancy_NR_coords_adj_json_15 ),
     np.std(r15.occupancy_NR_coords_adj_txt_15 ),
     np.std(r15.occupancy_NR_coords_ascii_txt_15 ),
     np.std(r15.occupancy_NR_coords_jpg_15 ),
     np.std(r15.occupancy_NR_coords_json_15 ),
     np.std(r15.occupancy_NR_coords_tokenized_txt_15 ) ]

# NR -- Allo -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Allo 3x3 averages

sd_3x3_NR_allo = [
     np.nanstd(r3.line_NR_allo_adj_json_3 ),
     np.nanstd(r3.line_NR_allo_adj_txt_3 ),
     np.nanstd(r3.line_NR_allo_jpg_3 ),
     np.nanstd(r3.line_NR_allo_json_3 ),
     np.nanstd(r3.line_NR_allo_tokenized_txt_3 ),
     np.nanstd(r3.occupancy_NR_allo_adj_json_3 ),
     np.nanstd(r3.occupancy_NR_allo_adj_txt_3 ),
     np.nanstd(r3.occupancy_NR_allo_ascii_txt_3 ),
     np.nanstd(r3.occupancy_NR_allo_jpg_3 ),
     np.nanstd(r3.occupancy_NR_allo_json_3 ),
     np.nanstd(r3.occupancy_NR_allo_tokenized_txt_3 )
    ]
sd_6x6_NR_allo=[
     np.nanstd(r6.line_NR_allo_adj_json_6 ),
     np.nanstd(r6.line_NR_allo_adj_txt_6 ),
     np.nanstd(r6.line_NR_allo_jpg_6 ),
     np.nanstd(r6.line_NR_allo_json_6 ),
     np.nanstd(r6.line_NR_allo_tokenized_txt_6 ),
     np.nanstd(r6.occupancy_NR_allo_adj_json_6 ),
     np.nanstd(r6.occupancy_NR_allo_adj_txt_6 ),
     np.nanstd(r6.occupancy_NR_allo_ascii_txt_6 ),
     np.nanstd(r6.occupancy_NR_allo_jpg_6 ),
     np.nanstd(r6.occupancy_NR_allo_json_6 ),
     np.nanstd(r6.occupancy_NR_allo_tokenized_txt_6 ) ]
sd_15x15_NR_allo=[
     np.nanstd(r15.line_NR_allo_adj_json_15 ),
     np.nanstd(r15.line_NR_allo_adj_txt_15 ),
     np.nanstd(r15.line_NR_allo_jpg_15 ),
     np.nanstd(r15.line_NR_allo_json_15 ),
     np.nanstd(r15.line_NR_allo_tokenized_txt_15 ),
     np.nanstd(r15.occupancy_NR_allo_adj_json_15 ),
     np.nanstd(r15.occupancy_NR_allo_adj_txt_15 ),
     np.nanstd(r15.occupancy_NR_allo_ascii_txt_15 ),
     np.nanstd(r15.occupancy_NR_allo_jpg_15 ),
     np.nanstd(r15.occupancy_NR_allo_json_15 ),
     np.nanstd(r15.occupancy_NR_allo_tokenized_txt_15 ) ]

# NR -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Ego 3x3 averages

sd_3x3_NR_ego = [
     np.std(r3.line_NR_ego_adj_json_3 ),
     np.std(r3.line_NR_ego_adj_txt_3 ),
     np.std(r3.line_NR_ego_jpg_3 ),
     np.std(r3.line_NR_ego_json_3 ),
     np.std(r3.line_NR_ego_tokenized_txt_3 ),
     np.std(r3.occupancy_NR_ego_adj_json_3 ),
     np.std(r3.occupancy_NR_ego_adj_txt_3 ),
     np.std(r3.occupancy_NR_ego_ascii_txt_3 ),
     np.std(r3.occupancy_NR_ego_jpg_3 ),
     np.std(r3.occupancy_NR_ego_json_3 ),
     np.std(r3.occupancy_NR_ego_tokenized_txt_3 )
    ]
sd_6x6_NR_ego=[
     np.std(r6.line_NR_ego_adj_json_6 ),
     np.std(r6.line_NR_ego_adj_txt_6 ),
     np.std(r6.line_NR_ego_jpg_6 ),
     np.std(r6.line_NR_ego_json_6 ),
     np.std(r6.line_NR_ego_tokenized_txt_6 ),
     np.std(r6.occupancy_NR_ego_adj_json_6 ),
     np.std(r6.occupancy_NR_ego_adj_txt_6 ),
     np.std(r6.occupancy_NR_ego_ascii_txt_6 ),
     np.std(r6.occupancy_NR_ego_jpg_6 ),
     np.std(r6.occupancy_NR_ego_json_6 ),
     np.std(r6.occupancy_NR_ego_tokenized_txt_6 ) ]
sd_15x15_NR_ego=[
     np.std(r15.line_NR_ego_adj_json_15 ),
     np.std(r15.line_NR_ego_adj_txt_15 ),
     np.std(r15.line_NR_ego_jpg_15 ),
     np.std(r15.line_NR_ego_json_15 ),
     np.std(r15.line_NR_ego_tokenized_txt_15 ),
     np.std(r15.occupancy_NR_ego_adj_json_15 ),
     np.std(r15.occupancy_NR_ego_adj_txt_15 ),
     np.std(r15.occupancy_NR_ego_ascii_txt_15 ),
      np.std(r15.occupancy_NR_ego_jpg_15 ),
     np.std(r15.occupancy_NR_ego_json_15 ),
     np.std(r15.occupancy_NR_ego_tokenized_txt_15 )]

# R -- Coords -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Coords 3x3 averages

sd_3x3_R_coords = [
     np.std(r3.line_R_coords_adj_json_3 ),
     np.std(r3.line_R_coords_adj_txt_3 ),
     np.std(r3.line_R_coords_jpg_3 ),
     np.std(r3.line_R_coords_json_3 ),
     np.std(r3.line_R_coords_tokenized_txt_3 ),
     np.std(r3.occupancy_R_coords_adj_json_3 ),
     np.std(r3.occupancy_R_coords_adj_txt_3 ),
     np.std(r3.occupancy_R_coords_ascii_txt_3 ),
     np.std(r3.occupancy_R_coords_jpg_3 ),
     np.std(r3.occupancy_R_coords_json_3 ),
     np.std(r3.occupancy_R_coords_tokenized_txt_3 )
    ]
sd_6x6_R_coords=[
     np.std(r6.line_R_coords_adj_json_6 ),
     np.std(r6.line_R_coords_adj_txt_6 ),
     np.std(r6.line_R_coords_jpg_6 ),
     np.std(r6.line_R_coords_json_6 ),
     np.std(r6.line_R_coords_tokenized_txt_6 ),
     np.std(r6.occupancy_R_coords_adj_json_6 ),
     np.std(r6.occupancy_R_coords_adj_txt_6 ),
     np.std(r6.occupancy_R_coords_ascii_txt_6 ),
     np.std(r6.occupancy_R_coords_jpg_6 ),
     np.std(r6.occupancy_R_coords_json_6 ),
     np.std(r6.occupancy_R_coords_tokenized_txt_6 ) ]
sd_15x15_R_coords=[
     np.std(r15.line_R_coords_adj_json_15 ),
     np.std(r15.line_R_coords_adj_txt_15 ),
     np.std(r15.line_R_coords_jpg_15 ),
     np.std(r15.line_R_coords_json_15 ),
     np.std(r15.line_R_coords_tokenized_txt_15 ),
     np.std(r15.occupancy_R_coords_adj_json_15 ),
     np.std(r15.occupancy_R_coords_adj_txt_15 ),
     np.std(r15.occupancy_R_coords_ascii_txt_15 ),
      np.std(r15.occupancy_R_coords_jpg_15 ),
     np.std(r15.occupancy_R_coords_json_15 ),
     np.std(r15.occupancy_R_coords_tokenized_txt_15 ) ]


# # R -- Allo -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Allo 3x3 averages
sd_3x3_R_allo = [
     np.std(r3.line_R_allo_adj_json_3 ),
     np.std(r3.line_R_allo_adj_txt_3 ),
     np.std(r3.line_R_allo_jpg_3 ),
     np.std(r3.line_R_allo_json_3 ),
     np.std(r3.line_R_allo_tokenized_txt_3 ),
     np.std(r3.occupancy_R_allo_adj_json_3 ),
     np.std(r3.occupancy_R_allo_adj_txt_3 ),
     np.std(r3.occupancy_R_allo_ascii_txt_3 ),
     np.std(r3.occupancy_R_allo_jpg_3 ),
     np.std(r3.occupancy_R_allo_json_3 ),
     np.std(r3.occupancy_R_allo_tokenized_txt_3 )
    ]
sd_6x6_R_allo=[
     np.std(r6.line_R_allo_adj_json_6 ),
     np.std(r6.line_R_allo_adj_txt_6 ),
     np.std(r6.line_R_allo_jpg_6 ),
     np.std(r6.line_R_allo_json_6 ),
     np.std(r6.line_R_allo_tokenized_txt_6 ),
     np.std(r6.occupancy_R_allo_adj_json_6 ),
     np.std(r6.occupancy_R_allo_adj_txt_6 ),
     np.std(r6.occupancy_R_allo_ascii_txt_6 ),
     np.std(r6.occupancy_R_allo_jpg_6 ),
     np.std(r6.occupancy_R_allo_json_6 ),
     np.std(r6.occupancy_R_allo_tokenized_txt_6 ) ]
sd_15x15_R_allo=[
     np.std(r15.line_R_allo_adj_json_15 ),
     np.std(r15.line_R_allo_adj_txt_15 ),
     np.std(r15.line_R_allo_jpg_15 ),
     np.std(r15.line_R_allo_json_15 ),
     np.std(r15.line_R_allo_tokenized_txt_15 ),
     np.std(r15.occupancy_R_allo_adj_json_15 ),
     np.std(r15.occupancy_R_allo_adj_txt_15 ),
     np.std(r15.occupancy_R_allo_ascii_txt_15 ),
     np.std(r15.occupancy_R_allo_jpg_15 ),
     np.std(r15.occupancy_R_allo_json_15 ),
     np.std(r15.occupancy_R_allo_tokenized_txt_15 ) ]

# # R -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
sd_3x3_R_ego = [
     np.std(r3.line_R_ego_adj_json_3 ),
     np.std(r3.line_R_ego_adj_txt_3 ),
     np.std(r3.line_R_ego_jpg_3 ),
     np.std(r3.line_R_ego_json_3 ),
     np.std(r3.line_R_ego_tokenized_txt_3 ),
     np.std(r3.occupancy_R_ego_adj_json_3 ),
     np.std(r3.occupancy_R_ego_adj_txt_3 ),
     np.std(r3.occupancy_R_ego_ascii_txt_3 ),
     np.std(r3.occupancy_R_ego_jpg_3 ),
     np.std(r3.occupancy_R_ego_json_3 ),
     np.std(r3.occupancy_R_ego_tokenized_txt_3 )
    ]
sd_6x6_R_ego=[
     np.std(r6.line_R_ego_adj_json_6 ),
     np.std(r6.line_R_ego_adj_txt_6 ),
     np.std(r6.line_R_ego_jpg_6 ),
     np.std(r6.line_R_ego_json_6 ),
     np.std(r6.line_R_ego_tokenized_txt_6 ),
     np.std(r6.occupancy_R_ego_adj_json_6 ),
     np.std(r6.occupancy_R_ego_adj_txt_6 ),
     np.std(r6.occupancy_R_ego_ascii_txt_6 ),
     np.std(r6.occupancy_R_ego_jpg_6 ),
     np.std(r6.occupancy_R_ego_json_6 ),
     np.std(r6.occupancy_R_ego_tokenized_txt_6 ) ]
sd_15x15_R_ego=[
     np.std(r15.line_R_ego_adj_json_15 ),
     np.std(r15.line_R_ego_adj_txt_15 ),
     np.std(r15.line_R_ego_jpg_15 ),
     np.std(r15.line_R_ego_json_15 ),
     np.std(r15.line_R_ego_tokenized_txt_15 ),
     np.std(r15.occupancy_R_ego_adj_json_15 ),
     np.std(r15.occupancy_R_ego_adj_txt_15 ),
     np.std(r15.occupancy_R_ego_ascii_txt_15 ),
     np.std(r15.occupancy_R_ego_jpg_15 ),
     np.std(r15.occupancy_R_ego_json_15 ),
     np.std(r15.occupancy_R_ego_tokenized_txt_15 ) ]




representations = [
    "Line-wall AL-JSON",
    "Line-wall AL-TXT",
    "Line-wall JPG",
    "Line-wall JSON",
    "Line-wall Tagged",
    "Occupancy AL-JSON",
    "Occupancy AL-TXT",
    "Occupancy ASCII",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tagged"
]


df = pd.DataFrame({
    "Representation": representations,
    "Standard dev. Coordinates Output, \n Gemini 2.5 Pro": sd_3x3_R_coords,
    "Standard dev. Abs. Directions Output, \n Gemini 2.5 Pro": sd_3x3_R_allo,
    "Standard dev. Egocentric Output, \n Gemini 2.5 Pro": sd_3x3_R_ego,
    "Standard dev. Coordinates Output, \n Gemini 2.5 Flash-Lite": sd_3x3_NR_coords,
    "Standard dev. Abs. Directions Output, \n Gemini 2.5 Flash-Lite": sd_3x3_NR_allo,
    "Standard dev. Egocentric Output, \n Gemini 2.5 Flash-Lite": sd_3x3_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required Standard dev.s for Desired Statistical Power (α=0.05, error margin = 5%), \n 3x3/7x7 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Standard deviations for each combination of input representation, output FoR, and LLM", fontsize=14)
plt.title("3x3/7x7 Mazes", fontsize=12)
# '''Sample sizes were determined so that the 95% confidence interval for the mean completion score 
# would have a half-width no greater than 5 percentage points, computed separately for each combination of 
# input representation, output frame of reference, maze size, and LLM'''

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2,2.5)

# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

plt.tight_layout()
# plt.show()


df = pd.DataFrame({
    "Representation": representations,

    "Standard dev. Coordinates Output, \n Gemini 2.5 Pro": sd_6x6_R_coords,
    "Standard dev. Abs. Directions Output, \n Gemini 2.5 Pro": sd_6x6_R_allo,
    "Standard dev. Egocentric Output, \n Gemini 2.5 Pro": sd_6x6_R_ego,
    "Standard dev. Coordinates Output, \n Gemini 2.5 Flash-Lite": sd_6x6_NR_coords,
    "Standard dev. Abs. Directions Output, \n Gemini 2.5 Flash-Lite": sd_6x6_NR_allo,
    "Standard dev. Egocentric Output, \n Gemini 2.5 Flash-Lite": sd_6x6_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required Standard dev.s for Desired Statistical Power (α=0.05, error margin = 5%), \n 6x6/13x13 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Standard deviations for each combination of input representation, output FoR, and LLM", fontsize=14)
plt.title("6x6/13x13 Mazes", fontsize=12)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.5)


# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

plt.tight_layout()
# plt.show()


df = pd.DataFrame({
    "Representation": representations,
    "Standard dev. Coordinates Output, \n Gemini 2.5 Pro": sd_15x15_R_coords,
    "Standard dev. Abs. Directions Output, \n Gemini 2.5 Pro": sd_15x15_R_allo,
    "Standard dev. Egocentric Output, \n Gemini 2.5 Pro": sd_15x15_R_ego,
    "Standard dev. Coordinates Output, \n Gemini 2.5 Flash-Lite": sd_15x15_NR_coords,
    "Standard dev. Abs. Directions Output, \n Gemini 2.5 Flash-Lite": sd_15x15_NR_allo,
    "Standard dev. Egocentric Output, \n Gemini 2.5 Flash-Lite": sd_15x15_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 15x15/31x31 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Standard deviations for each combination of input representation, output FoR, and LLM", fontsize=14)
plt.title("15x15/31x31 Mazes", fontsize=12)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)


table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.5)


# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

plt.tight_layout()
# plt.show()


# ----------------------------------------------------------------------------------------------------------------------------
# making tables with the half-widths of the confidence intervals for each condition

def half(sigma):
    half= 0.284*sigma
    return round(half, 1)







hw_3x3_NR_coords = [
     half(np.std(r3.line_NR_coords_adj_json_3 )),
     half(np.std(r3.line_NR_coords_adj_txt_3 )),
     half(np.std(r3.line_NR_coords_jpg_3 )),
     half(np.std(r3.line_NR_coords_json_3 )),
     half(np.std(r3.line_NR_coords_tokenized_txt_3 )),
     half(np.std(r3.occupancy_NR_coords_adj_json_3 )),
     half(np.std(r3.occupancy_NR_coords_adj_txt_3 )),
     half(np.std(r3.occupancy_NR_coords_ascii_txt_3 )),
     half(np.std(r3.occupancy_NR_coords_jpg_3 )),
     half(np.std(r3.occupancy_NR_coords_json_3 )),
     half(np.std(r3.occupancy_NR_coords_tokenized_txt_3 ))]
hw_6x6_NR_coords=[
     half(np.std(r6.line_NR_coords_adj_json_6 )),
     half(np.std(r6.line_NR_coords_adj_txt_6 )),
     half(np.std(r6.line_NR_coords_jpg_6 )),
     half(np.std(r6.line_NR_coords_json_6 )),
     half(np.std(r6.line_NR_coords_tokenized_txt_6 )),
     half(np.std(r6.occupancy_NR_coords_adj_json_6 )),
     half(np.std(r6.occupancy_NR_coords_adj_txt_6 )),
     half(np.std(r6.occupancy_NR_coords_ascii_txt_6 )),
     half(np.std(r6.occupancy_NR_coords_jpg_6 )),
     half(np.std(r6.occupancy_NR_coords_json_6 )),
     half(np.std(r6.occupancy_NR_coords_tokenized_txt_6 )) ]
hw_15x15_NR_coords=[
     half(np.std(r15.line_NR_coords_adj_json_15 )),
     half(np.std(r15.line_NR_coords_adj_txt_15 )),
     half(np.std(r15.line_NR_coords_jpg_15 )),
     half(np.std(r15.line_NR_coords_json_15 )),
     half(np.std(r15.line_NR_coords_tokenized_txt_15 )),
     half(np.std(r15.occupancy_NR_coords_adj_json_15 )),
     half(np.std(r15.occupancy_NR_coords_adj_txt_15 )),
     half(np.std(r15.occupancy_NR_coords_ascii_txt_15 )),
     half(np.std(r15.occupancy_NR_coords_jpg_15 )),
     half(np.std(r15.occupancy_NR_coords_json_15 )),
     half(np.std(r15.occupancy_NR_coords_tokenized_txt_15 )) ]

# NR -- Allo -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Allo 3x3 averages

hw_3x3_NR_allo = [
     half(np.nanstd(r3.line_NR_allo_adj_json_3 )),
     half(np.nanstd(r3.line_NR_allo_adj_txt_3 )),
     half(np.nanstd(r3.line_NR_allo_jpg_3 )),
     half(np.nanstd(r3.line_NR_allo_json_3 )),
     half(np.nanstd(r3.line_NR_allo_tokenized_txt_3 )),
     half(np.nanstd(r3.occupancy_NR_allo_adj_json_3 )),
     half(np.nanstd(r3.occupancy_NR_allo_adj_txt_3 )),
     half(np.nanstd(r3.occupancy_NR_allo_ascii_txt_3 )),
     half(np.nanstd(r3.occupancy_NR_allo_jpg_3 )),
     half(np.nanstd(r3.occupancy_NR_allo_json_3 )),
     half(np.nanstd(r3.occupancy_NR_allo_tokenized_txt_3 ))    ]
hw_6x6_NR_allo=[
     half(np.nanstd(r6.line_NR_allo_adj_json_6 )),
     half(np.nanstd(r6.line_NR_allo_adj_txt_6 )),
     half(np.nanstd(r6.line_NR_allo_jpg_6 )),
     half(np.nanstd(r6.line_NR_allo_json_6 )),
     half(np.nanstd(r6.line_NR_allo_tokenized_txt_6 )),
     half(np.nanstd(r6.occupancy_NR_allo_adj_json_6 )),
     half(np.nanstd(r6.occupancy_NR_allo_adj_txt_6 )),
     half(np.nanstd(r6.occupancy_NR_allo_ascii_txt_6 )),
     half(np.nanstd(r6.occupancy_NR_allo_jpg_6 )),
     half(np.nanstd(r6.occupancy_NR_allo_json_6 )),
     half(np.nanstd(r6.occupancy_NR_allo_tokenized_txt_6 )) ]
hw_15x15_NR_allo=[
     half(np.nanstd(r15.line_NR_allo_adj_json_15 )),
     half(np.nanstd(r15.line_NR_allo_adj_txt_15 )),
     half(np.nanstd(r15.line_NR_allo_jpg_15 )),
     half(np.nanstd(r15.line_NR_allo_json_15 )),
     half(np.nanstd(r15.line_NR_allo_tokenized_txt_15 )),
     half(np.nanstd(r15.occupancy_NR_allo_adj_json_15 )),
     half(np.nanstd(r15.occupancy_NR_allo_adj_txt_15 )),
     half(np.nanstd(r15.occupancy_NR_allo_ascii_txt_15 )),
     half(np.nanstd(r15.occupancy_NR_allo_jpg_15 )),
     half(np.nanstd(r15.occupancy_NR_allo_json_15 )),
     half(np.nanstd(r15.occupancy_NR_allo_tokenized_txt_15 )) ]

# NR -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Ego 3x3 averages

hw_3x3_NR_ego = [
     half(np.std(r3.line_NR_ego_adj_json_3 )),
     half(np.std(r3.line_NR_ego_adj_txt_3 )),
     half(np.std(r3.line_NR_ego_jpg_3 )),
     half(np.std(r3.line_NR_ego_json_3 )),
     half(np.std(r3.line_NR_ego_tokenized_txt_3 )),
     half(np.std(r3.occupancy_NR_ego_adj_json_3 )),
     half(np.std(r3.occupancy_NR_ego_adj_txt_3 )),
     half(np.std(r3.occupancy_NR_ego_ascii_txt_3 )),
     half(np.std(r3.occupancy_NR_ego_jpg_3 )),
     half(np.std(r3.occupancy_NR_ego_json_3 )),
     half(np.std(r3.occupancy_NR_ego_tokenized_txt_3 ))
    ]
hw_6x6_NR_ego=[
     half(np.std(r6.line_NR_ego_adj_json_6 )),
     half(np.std(r6.line_NR_ego_adj_txt_6 )),
     half(np.std(r6.line_NR_ego_jpg_6 )),
     half(np.std(r6.line_NR_ego_json_6 )),
     half(np.std(r6.line_NR_ego_tokenized_txt_6 )),
     half(np.std(r6.occupancy_NR_ego_adj_json_6 )),
     half(np.std(r6.occupancy_NR_ego_adj_txt_6 )),
     half(np.std(r6.occupancy_NR_ego_ascii_txt_6 )),
     half(np.std(r6.occupancy_NR_ego_jpg_6 )),
     half(np.std(r6.occupancy_NR_ego_json_6 )),
     half(np.std(r6.occupancy_NR_ego_tokenized_txt_6 )) ]
hw_15x15_NR_ego=[
     half(np.std(r15.line_NR_ego_adj_json_15 )),
     half(np.std(r15.line_NR_ego_adj_txt_15 )),
     half(np.std(r15.line_NR_ego_jpg_15 )),
     half(np.std(r15.line_NR_ego_json_15 )),
     half(np.std(r15.line_NR_ego_tokenized_txt_15 )),
     half(np.std(r15.occupancy_NR_ego_adj_json_15 )),
     half(np.std(r15.occupancy_NR_ego_adj_txt_15 )),
     half(np.std(r15.occupancy_NR_ego_ascii_txt_15 )),
      half(np.std(r15.occupancy_NR_ego_jpg_15 )),
     half(np.std(r15.occupancy_NR_ego_json_15 )),
     half(np.std(r15.occupancy_NR_ego_tokenized_txt_15 ))]

# R -- Coords -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Coords 3x3 averages

hw_3x3_R_coords = [
     half(np.std(r3.line_R_coords_adj_json_3 )),
     half(np.std(r3.line_R_coords_adj_txt_3 )),
     half(np.std(r3.line_R_coords_jpg_3 )),
     half(np.std(r3.line_R_coords_json_3 )),
     half(np.std(r3.line_R_coords_tokenized_txt_3 )),
     half(np.std(r3.occupancy_R_coords_adj_json_3 )),
     half(np.std(r3.occupancy_R_coords_adj_txt_3 )),
     half(np.std(r3.occupancy_R_coords_ascii_txt_3 )),
     half(np.std(r3.occupancy_R_coords_jpg_3 )),
     half(np.std(r3.occupancy_R_coords_json_3 )),
     half(np.std(r3.occupancy_R_coords_tokenized_txt_3 ))
    ]
hw_6x6_R_coords=[
     half(np.std(r6.line_R_coords_adj_json_6 )),
     half(np.std(r6.line_R_coords_adj_txt_6 )),
     half(np.std(r6.line_R_coords_jpg_6 )),
     half(np.std(r6.line_R_coords_json_6 )),
     half(np.std(r6.line_R_coords_tokenized_txt_6 )),
     half(np.std(r6.occupancy_R_coords_adj_json_6 )),
     half(np.std(r6.occupancy_R_coords_adj_txt_6 )),
     half(np.std(r6.occupancy_R_coords_ascii_txt_6 )),
     half(np.std(r6.occupancy_R_coords_jpg_6 )),
     half(np.std(r6.occupancy_R_coords_json_6 )),
     half(np.std(r6.occupancy_R_coords_tokenized_txt_6 )) ]
hw_15x15_R_coords=[
     half(np.std(r15.line_R_coords_adj_json_15 )),
     half(np.std(r15.line_R_coords_adj_txt_15 )),
     half(np.std(r15.line_R_coords_jpg_15 )),
     half(np.std(r15.line_R_coords_json_15 )),
     half(np.std(r15.line_R_coords_tokenized_txt_15 )),
     half(np.std(r15.occupancy_R_coords_adj_json_15 )),
     half(np.std(r15.occupancy_R_coords_adj_txt_15 )),
     half(np.std(r15.occupancy_R_coords_ascii_txt_15 )),
      half(np.std(r15.occupancy_R_coords_jpg_15 )),
     half(np.std(r15.occupancy_R_coords_json_15 )),
     half(np.std(r15.occupancy_R_coords_tokenized_txt_15 )) ]


# # R -- Allo -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Allo 3x3 averages
hw_3x3_R_allo = [
     half(np.std(r3.line_R_allo_adj_json_3 )),
     half(np.std(r3.line_R_allo_adj_txt_3 )),
     half(np.std(r3.line_R_allo_jpg_3 )),
     half(np.std(r3.line_R_allo_json_3 )),
     half(np.std(r3.line_R_allo_tokenized_txt_3 )),
     half(np.std(r3.occupancy_R_allo_adj_json_3 )),
     half(np.std(r3.occupancy_R_allo_adj_txt_3 )),
     half(np.std(r3.occupancy_R_allo_ascii_txt_3 )),
     half(np.std(r3.occupancy_R_allo_jpg_3 )),
     half(np.std(r3.occupancy_R_allo_json_3 )),
     half(np.std(r3.occupancy_R_allo_tokenized_txt_3 ))
    ]
hw_6x6_R_allo=[
     half(np.std(r6.line_R_allo_adj_json_6 )),
     half(np.std(r6.line_R_allo_adj_txt_6 )),
     half(np.std(r6.line_R_allo_jpg_6 )),
     half(np.std(r6.line_R_allo_json_6 )),
     half(np.std(r6.line_R_allo_tokenized_txt_6 )),
     half(np.std(r6.occupancy_R_allo_adj_json_6 )),
     half(np.std(r6.occupancy_R_allo_adj_txt_6 )),
     half(np.std(r6.occupancy_R_allo_ascii_txt_6 )),
     half(np.std(r6.occupancy_R_allo_jpg_6 )),
     half(np.std(r6.occupancy_R_allo_json_6 )),
     half(np.std(r6.occupancy_R_allo_tokenized_txt_6 )) ]
hw_15x15_R_allo=[
     half(np.std(r15.line_R_allo_adj_json_15 )),
     half(np.std(r15.line_R_allo_adj_txt_15 )),
     half(np.std(r15.line_R_allo_jpg_15 )),
     half(np.std(r15.line_R_allo_json_15 )),
     half(np.std(r15.line_R_allo_tokenized_txt_15 )),
     half(np.std(r15.occupancy_R_allo_adj_json_15 )),
     half(np.std(r15.occupancy_R_allo_adj_txt_15 )),
     half(np.std(r15.occupancy_R_allo_ascii_txt_15 )),
     half(np.std(r15.occupancy_R_allo_jpg_15 )),
     half(np.std(r15.occupancy_R_allo_json_15 )),
     half(np.std(r15.occupancy_R_allo_tokenized_txt_15 )) ]

# # R -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
hw_3x3_R_ego = [
     half(np.std(r3.line_R_ego_adj_json_3 )),
     half(np.std(r3.line_R_ego_adj_txt_3 )),
     half(np.std(r3.line_R_ego_jpg_3 )),
     half(np.std(r3.line_R_ego_json_3 )),
     half(np.std(r3.line_R_ego_tokenized_txt_3 )),
     half(np.std(r3.occupancy_R_ego_adj_json_3 )),
     half(np.std(r3.occupancy_R_ego_adj_txt_3 )),
     half(np.std(r3.occupancy_R_ego_ascii_txt_3 )),
     half(np.std(r3.occupancy_R_ego_jpg_3 )),
     half(np.std(r3.occupancy_R_ego_json_3 )),
     half(np.std(r3.occupancy_R_ego_tokenized_txt_3 ))
    ]
hw_6x6_R_ego=[
     half(np.std(r6.line_R_ego_adj_json_6 )),
     half(np.std(r6.line_R_ego_adj_txt_6 )),
     half(np.std(r6.line_R_ego_jpg_6 )),
     half(np.std(r6.line_R_ego_json_6 )),
     half(np.std(r6.line_R_ego_tokenized_txt_6 )),
     half(np.std(r6.occupancy_R_ego_adj_json_6 )),
     half(np.std(r6.occupancy_R_ego_adj_txt_6 )),
     half(np.std(r6.occupancy_R_ego_ascii_txt_6 )),
     half(np.std(r6.occupancy_R_ego_jpg_6 )),
     half(np.std(r6.occupancy_R_ego_json_6 )),
     half(np.std(r6.occupancy_R_ego_tokenized_txt_6 )) ]
hw_15x15_R_ego=[
     half(np.std(r15.line_R_ego_adj_json_15 )),
     half(np.std(r15.line_R_ego_adj_txt_15 )),
     half(np.std(r15.line_R_ego_jpg_15 )),
     half(np.std(r15.line_R_ego_json_15 )),
     half(np.std(r15.line_R_ego_tokenized_txt_15 )),
     half(np.std(r15.occupancy_R_ego_adj_json_15 )),
     half(np.std(r15.occupancy_R_ego_adj_txt_15 )),
     half(np.std(r15.occupancy_R_ego_ascii_txt_15 )),
     half(np.std(r15.occupancy_R_ego_jpg_15 )),
     half(np.std(r15.occupancy_R_ego_json_15 )),
     half(np.std(r15.occupancy_R_ego_tokenized_txt_15 )) ]




representations = [
    "Line-wall AL-JSON",
    "Line-wall AL-TXT",
    "Line-wall JPG",
    "Line-wall JSON",
    "Line-wall Tagged",
    "Occupancy AL-JSON",
    "Occupancy AL-TXT",
    "Occupancy ASCII",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tagged"
]


df = pd.DataFrame({
    "Representation": representations,
    "CI half-width\nCoordinates Output,\nGemini 2.5 Pro": hw_3x3_R_coords,
    "CI half-width\nAbs. Directions Output,\nGemini 2.5 Pro": hw_3x3_R_allo,
    "CI half-width\nEgocentric Output,\nGemini 2.5 Pro": hw_3x3_R_ego,
    "CI half-width\nCoordinates Output,\nGemini 2.5 Flash-Lite": hw_3x3_NR_coords,
    "CI half-width\nAbs. Directions Output,\nGemini 2.5 Flash-Lite": hw_3x3_NR_allo,
    "CI half-width\nEgocentric Output,\nGemini 2.5 Flash-Lite": hw_3x3_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required CI half-widths for Desired Statistical Power (α=0.05, error margin = 5%), \n 3x3/7x7 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Half-Widths of the 95% Confidence Interval for the Mean Completion Scores, Given in Percentage Points,\nComputed separately for Each Combination of Input Representation, Output FoR, Maze Size, and LLM", fontsize=14)
plt.title("3x3/7x7 Mazes", fontsize=12)
# '''Sample sizes were determined so that the 95% confidence interval for the mean completion score 
# would have a half-width no greater than 5 percentage points, computed separately for each combination of 
# input representation, output frame of reference, maze size, and LLM'''

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(2.2, 3.0)

# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

# plt.tight_layout()
# plt.show()


df = pd.DataFrame({
    "Representation": representations,

    "CI half-width\nCoordinates Output,\nGemini 2.5 Pro": hw_6x6_R_coords,
    "CI half-width\nAbs. Directions Output,\nGemini 2.5 Pro": hw_6x6_R_allo,
    "CI half-width\nEgocentric Output,\nGemini 2.5 Pro": hw_6x6_R_ego,
    "CI half-width\nCoordinates Output,\nGemini 2.5 Flash-Lite": hw_6x6_NR_coords,
    "CI half-width\nAbs. Directions Output,\nGemini 2.5 Flash-Lite": hw_6x6_NR_allo,
    "CI half-width\nEgocentric Output,\nGemini 2.5 Flash-Lite": hw_6x6_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required CI half-widths for Desired Statistical Power (α=0.05, error margin = 5%), \n 6x6/13x13 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Half-Widths of the 95% Confidence Interval for the Mean Completion Scores, Given in Percentage Points,\nComputed separately for Each Combination of Input Representation, Output FoR, Maze Size, and LLM", fontsize=14)
plt.title("6x6/13x13 Mazes", fontsize=12)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(2.2, 3.0)


# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

# plt.tight_layout()
# plt.show()


df = pd.DataFrame({
    "Representation": representations,
    "CI half-width\nCoordinates Output,\nGemini 2.5 Pro": hw_15x15_R_coords,
    "CI half-width\nAbs. Directions Output,\nGemini 2.5 Pro": hw_15x15_R_allo,
    "CI half-width\nEgocentric Output,\nGemini 2.5 Pro": hw_15x15_R_ego,
    "CI half-width\nCoordinates Output,\nGemini 2.5 Flash-Lite": hw_15x15_NR_coords,
    "CI half-width\nAbs. Directions Output,\nGemini 2.5 Flash-Lite": hw_15x15_NR_allo,
    "CI half-width\nEgocentric Output,\nGemini 2.5 Flash-Lite": hw_15x15_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 15x15/31x31 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Frames of Reference", fontsize=16, pad=20)

plt.suptitle("Half-Widths of the 95% Confidence Interval for the Mean Completion Scores, Given in Percentage Points,\nComputed separately for Each Combination of Input Representation, Output FoR, Maze Size, and LLM", fontsize=14)
plt.title("15x15/31x31 Mazes", fontsize=12)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)


table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(2.2, 3.0)


# Make header row bold
for col in range(len(df.columns)):
    table[(0, col)].set_text_props(weight='bold')

# Make first column bold
for row in range(1, len(df) + 1):
    table[(row, 0)].set_text_props(weight='bold')
    # Shade header row
for col in range(len(df.columns)):
    table[(0, col)].set_facecolor("#f0f0f0")

# plt.tight_layout()
# plt.show()





list_half = [
             hw_15x15_NR_allo, 
             hw_15x15_NR_ego, 
             hw_15x15_NR_coords,
             hw_15x15_R_coords,
             hw_15x15_R_allo, 
             hw_15x15_R_ego,
            #  hw_6x6_NR_allo,
            #  hw_6x6_NR_ego,
            #  hw_6x6_NR_coords, 
            #  hw_6x6_R_coords,
            #  hw_6x6_R_allo,
            #  hw_6x6_R_ego,
            #  hw_3x3_NR_ego,
            #  hw_3x3_NR_coords,
            #  hw_3x3_NR_allo,
            #  hw_3x3_R_coords,
            #  hw_3x3_R_allo,
            #  hw_3x3_R_ego
            ]

def sort(lst):
    
    empty0 = 0
    empty1 = 0
    empty2 = 0
    empty3 = 0
    empty4 = 0
    for j,bla in enumerate(lst):

        for i,val in enumerate(bla):
            if 0.0<= val < 2.5:
                empty0 +=1
            elif 2.5 <= val < 5:
                empty1 +=1
            elif 5 <= val < 7.5:
                empty2 +=1
            elif 7.5 <= val < 10:
                empty3 +=1
            elif 10<=val <12.5:
                empty4 +=1
            else:
                print("Value out of range:", val)
    print("0-2.5:", empty0, '\n')
    print("2.5-5:", empty1, '\n')
    print("5-7.5:", empty2, '\n')
    print("7.5-10:", empty3, '\n')
    print("10+:", empty4, '\n') 
    return empty0, empty1, empty2, empty3, empty4

sort(list_half)






# Checking if the data is normally distributed, using the shapiro-wilk test

from scipy.stats import shapiro


def z_score_standardization(data):
    mean = np.nanmean(data)
    std = np.nanstd(data)
    z_scores = (data - mean) / std
    return z_scores

# dummy = [0,1,2, 1]
# print(np.std(dummy))
z_scores = z_score_standardization(r15.line_R_allo_tokenized_txt_15)
print(z_scores)


fig, ax = plt.subplots(figsize=(30, 8))

plt.hist(z_scores, bins=10)
plt.title("Histogram of Z-scores, 15x15 line r allo tokenized")
plt.show()


def frequency(data):
    bin0=0
    bin1=0
    for a in range(len(data)):
        if data[a] == 0.0 or (0.0 < data[a] < 2.5):
            bin0 +=1
        if 2.5 <= data[a] < 5:
            bin1 +=1    
        if 5 <= data[a] < 7.5:
            bin2 +=1
        if 7.5 <= data[a] < 10:
            bin3 +=1
        if 10 <= data[a] < 12.5:
            bin4 +=1
        if 12.5 <= data[a] < 15:
            bin5 +=1
        if 15 <= data[a] < 17.5:
            bin6 +=1
        if 17.5 <= data[a] < 20:
            bin7 +=1
        if 20 <= data[a] < 22.5:
            bin8 +=1
        if 22.5 <= data[a] < 25:
            bin9 +=1
        if 25 <= data[a] < 27.5:
            bin10 +=1
        if 27.5 <= data[a] < 30:
            bin11 +=1
        if 30 <= data[a] < 32.5:
            bin12 +=1
        if 32.5 <= data[a] < 35:
            bin13 +=1
        if 35 <= data[a] < 37.5:
            bin14 +=1
        if 37.5 <= data[a] < 40:
            bin15 +=1
        if 40 <= data[a] < 42.5:
            bin16 +=1
        if 42.5 <= data[a] < 45:
            bin17 +=1
        if 45 <= data[a] < 47.5:
            bin18 +=1
        if 47.5 <= data[a] < 50:
            bin19 +=1
        if 50 <= data[a] < 52.5:
            bin20 +=1
        if 52.5 <= data[a] < 55:
            bin21 +=1
        if 55 <= data[a] < 57.5:
            bin22 +=1
        if 57.5 <= data[a] < 60:
            bin23 +=1
        if 60 <= data[a] < 62.5:
            bin24 +=1
        if 62.5 <= data[a] < 65:
            bin25 +=1
        if 65 <= data[a] < 67.5:
            bin26 +=1
        if 67.5 <= data[a] < 70:
            bin27 +=1
        if 70 <= data[a] < 72.5:
            bin28 +=1
        if 72.5 <= data[a] < 75:
            bin29 +=1
        if 75 <= data[a] < 77.5:
            bin30 +=1
        if 77.5 <= data[a] < 80:
            bin31 +=1
        if 80 <= data[a] < 82.5:
            bin32 +=1
        if 82.5 <= data[a] < 85:
            bin33 +=1
        if 85 <= data[a] < 87.5:
            bin34 +=1
        if 87.5 <= data[a] < 90:
            bin35 +=1
        


