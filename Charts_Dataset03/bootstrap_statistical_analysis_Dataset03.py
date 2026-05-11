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
from scipy.stats import bootstrap
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15

x_axis_line = ['3x3', '6x6', '15x15']
x_axis_occ = ['7x7', '13x13', '31x31']

# Bootstrap confidence interval for the mean
def bootstrap_CI(scores):
    #set manual value of half-width=0.0 for degenerate samples (all values the same) to avoid error
    if np.nanstd(scores) == 0:
        half_width = 0.0
    else:
        res = bootstrap(
        (scores,),
        np.nanmean,
        confidence_level=0.95,
        n_resamples=10000,
        method='BCa',   # good default for non-normal data
        random_state=42
        )

        # Extract full confidence interval
        ci_low = res.confidence_interval.low
        ci_high = res.confidence_interval.high

        # Half-width
        half_width = (ci_high - ci_low) / 2
    return round(half_width, 1)



# making tables with the bootstrapped half-widths of the confidence intervals for each condition



hw_3x3_NR_coords = [
     bootstrap_CI( r3.line_NR_coords_adj_json_3  ),
     bootstrap_CI( r3.line_NR_coords_adj_txt_3  ),
     bootstrap_CI( r3.line_NR_coords_jpg_3  ),
     bootstrap_CI( r3.line_NR_coords_json_3  ),
     bootstrap_CI( r3.line_NR_coords_tokenized_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_coords_adj_json_3  ),
     bootstrap_CI( r3.occupancy_NR_coords_adj_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_coords_ascii_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_coords_jpg_3  ),
     bootstrap_CI( r3.occupancy_NR_coords_json_3  ),
     bootstrap_CI( r3.occupancy_NR_coords_tokenized_txt_3 )]
hw_6x6_NR_coords=[
     bootstrap_CI( r6.line_NR_coords_adj_json_6  ),
     bootstrap_CI( r6.line_NR_coords_adj_txt_6  ),
     bootstrap_CI( r6.line_NR_coords_jpg_6  ),
     bootstrap_CI( r6.line_NR_coords_json_6  ),
     bootstrap_CI( r6.line_NR_coords_tokenized_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_coords_adj_json_6  ),
     bootstrap_CI( r6.occupancy_NR_coords_adj_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_coords_ascii_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_coords_jpg_6  ),
     bootstrap_CI( r6.occupancy_NR_coords_json_6  ),
     bootstrap_CI( r6.occupancy_NR_coords_tokenized_txt_6 )]
hw_15x15_NR_coords=[
     bootstrap_CI( r15.line_NR_coords_adj_json_15  ),
     bootstrap_CI( r15.line_NR_coords_adj_txt_15  ),
     bootstrap_CI( r15.line_NR_coords_jpg_15  ),
     bootstrap_CI( r15.line_NR_coords_json_15  ),
     bootstrap_CI( r15.line_NR_coords_tokenized_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_coords_adj_json_15  ),
     bootstrap_CI( r15.occupancy_NR_coords_adj_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_coords_ascii_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_coords_jpg_15  ),
     bootstrap_CI( r15.occupancy_NR_coords_json_15  ),
     bootstrap_CI( r15.occupancy_NR_coords_tokenized_txt_15 )]

# NR -- Allo -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Allo 3x3 averages

hw_3x3_NR_allo = [
     bootstrap_CI( r3.line_NR_allo_adj_json_3  ),
     bootstrap_CI( r3.line_NR_allo_adj_txt_3  ),
     bootstrap_CI( r3.line_NR_allo_jpg_3  ),
     bootstrap_CI( r3.line_NR_allo_json_3  ),
     bootstrap_CI( r3.line_NR_allo_tokenized_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_allo_adj_json_3  ),
     bootstrap_CI( r3.occupancy_NR_allo_adj_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_allo_ascii_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_allo_jpg_3  ),
     bootstrap_CI( r3.occupancy_NR_allo_json_3  ),
     bootstrap_CI( r3.occupancy_NR_allo_tokenized_txt_3 )]
hw_6x6_NR_allo=[
     bootstrap_CI( r6.line_NR_allo_adj_json_6  ),
     bootstrap_CI( r6.line_NR_allo_adj_txt_6  ),
     bootstrap_CI( r6.line_NR_allo_jpg_6  ),
     bootstrap_CI( r6.line_NR_allo_json_6  ),
     bootstrap_CI( r6.line_NR_allo_tokenized_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_allo_adj_json_6  ),
     bootstrap_CI( r6.occupancy_NR_allo_adj_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_allo_ascii_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_allo_jpg_6  ),
     bootstrap_CI( r6.occupancy_NR_allo_json_6  ),
     bootstrap_CI( r6.occupancy_NR_allo_tokenized_txt_6 )]
hw_15x15_NR_allo=[
     bootstrap_CI( r15.line_NR_allo_adj_json_15  ),
     bootstrap_CI( r15.line_NR_allo_adj_txt_15  ),
     bootstrap_CI( r15.line_NR_allo_jpg_15  ),
     bootstrap_CI( r15.line_NR_allo_json_15),
     bootstrap_CI( r15.line_NR_allo_tokenized_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_allo_adj_json_15  ),
     bootstrap_CI( r15.occupancy_NR_allo_adj_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_allo_ascii_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_allo_jpg_15  ),
     bootstrap_CI( r15.occupancy_NR_allo_json_15  ),
     bootstrap_CI( r15.occupancy_NR_allo_tokenized_txt_15 )]

# NR -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Ego 3x3 averages

hw_3x3_NR_ego = [
     bootstrap_CI( r3.line_NR_ego_adj_json_3  ),
     bootstrap_CI( r3.line_NR_ego_adj_txt_3  ),
     bootstrap_CI( r3.line_NR_ego_jpg_3  ),
     bootstrap_CI( r3.line_NR_ego_json_3  ),
     bootstrap_CI( r3.line_NR_ego_tokenized_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_ego_adj_json_3  ),
     bootstrap_CI( r3.occupancy_NR_ego_adj_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_ego_ascii_txt_3  ),
     bootstrap_CI( r3.occupancy_NR_ego_jpg_3  ),
     bootstrap_CI( r3.occupancy_NR_ego_json_3  ),
     bootstrap_CI( r3.occupancy_NR_ego_tokenized_txt_3 )]
hw_6x6_NR_ego=[
     bootstrap_CI( r6.line_NR_ego_adj_json_6  ),
     bootstrap_CI( r6.line_NR_ego_adj_txt_6  ),
     bootstrap_CI( r6.line_NR_ego_jpg_6  ),
     bootstrap_CI( r6.line_NR_ego_json_6  ),
     bootstrap_CI( r6.line_NR_ego_tokenized_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_ego_adj_json_6  ),
     bootstrap_CI( r6.occupancy_NR_ego_adj_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_ego_ascii_txt_6  ),
     bootstrap_CI( r6.occupancy_NR_ego_jpg_6  ),
     bootstrap_CI( r6.occupancy_NR_ego_json_6  ),
     bootstrap_CI( r6.occupancy_NR_ego_tokenized_txt_6 )]
hw_15x15_NR_ego=[
     bootstrap_CI( r15.line_NR_ego_adj_json_15  ),
     bootstrap_CI( r15.line_NR_ego_adj_txt_15  ),
     bootstrap_CI( r15.line_NR_ego_jpg_15  ),
     bootstrap_CI( r15.line_NR_ego_json_15  ),
     bootstrap_CI( r15.line_NR_ego_tokenized_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_ego_adj_json_15  ),
     bootstrap_CI( r15.occupancy_NR_ego_adj_txt_15  ),
     bootstrap_CI( r15.occupancy_NR_ego_ascii_txt_15  ),
      bootstrap_CI( r15.occupancy_NR_ego_jpg_15  ),
     bootstrap_CI( r15.occupancy_NR_ego_json_15  ),
     bootstrap_CI( r15.occupancy_NR_ego_tokenized_txt_15 )]

# R -- Coords -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Coords 3x3 averages

hw_3x3_R_coords = [
     bootstrap_CI( r3.line_R_coords_adj_json_3  ),
     bootstrap_CI( r3.line_R_coords_adj_txt_3  ),
     bootstrap_CI( r3.line_R_coords_jpg_3  ),
     bootstrap_CI( r3.line_R_coords_json_3  ),
     bootstrap_CI( r3.line_R_coords_tokenized_txt_3  ),
     bootstrap_CI( r3.occupancy_R_coords_adj_json_3  ),
     bootstrap_CI( r3.occupancy_R_coords_adj_txt_3  ),
     bootstrap_CI( r3.occupancy_R_coords_ascii_txt_3  ),
     bootstrap_CI( r3.occupancy_R_coords_jpg_3  ),
     bootstrap_CI( r3.occupancy_R_coords_json_3  ),
     bootstrap_CI( r3.occupancy_R_coords_tokenized_txt_3 )]
hw_6x6_R_coords=[
     bootstrap_CI( r6.line_R_coords_adj_json_6  ),
     bootstrap_CI( r6.line_R_coords_adj_txt_6  ),
     bootstrap_CI( r6.line_R_coords_jpg_6  ),
     bootstrap_CI( r6.line_R_coords_json_6  ),
     bootstrap_CI( r6.line_R_coords_tokenized_txt_6  ),
     bootstrap_CI( r6.occupancy_R_coords_adj_json_6  ),
     bootstrap_CI( r6.occupancy_R_coords_adj_txt_6  ),
     bootstrap_CI( r6.occupancy_R_coords_ascii_txt_6  ),
     bootstrap_CI( r6.occupancy_R_coords_jpg_6  ),
     bootstrap_CI( r6.occupancy_R_coords_json_6  ),
     bootstrap_CI( r6.occupancy_R_coords_tokenized_txt_6 )]
hw_15x15_R_coords=[
     bootstrap_CI( r15.line_R_coords_adj_json_15  ),
     bootstrap_CI( r15.line_R_coords_adj_txt_15  ),
     bootstrap_CI( r15.line_R_coords_jpg_15  ),
     bootstrap_CI( r15.line_R_coords_json_15  ),
     bootstrap_CI( r15.line_R_coords_tokenized_txt_15  ),
     bootstrap_CI( r15.occupancy_R_coords_adj_json_15  ),
     bootstrap_CI( r15.occupancy_R_coords_adj_txt_15  ),
     bootstrap_CI( r15.occupancy_R_coords_ascii_txt_15  ),
      bootstrap_CI( r15.occupancy_R_coords_jpg_15  ),
     bootstrap_CI( r15.occupancy_R_coords_json_15  ),
     bootstrap_CI( r15.occupancy_R_coords_tokenized_txt_15 )]


# # R -- Allo -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Allo 3x3 averages
hw_3x3_R_allo = [
     bootstrap_CI( r3.line_R_allo_adj_json_3  ),
     bootstrap_CI( r3.line_R_allo_adj_txt_3  ),
     bootstrap_CI( r3.line_R_allo_jpg_3  ),
     bootstrap_CI( r3.line_R_allo_json_3  ),
     bootstrap_CI( r3.line_R_allo_tokenized_txt_3  ),
     bootstrap_CI( r3.occupancy_R_allo_adj_json_3  ),
     bootstrap_CI( r3.occupancy_R_allo_adj_txt_3  ),
     bootstrap_CI( r3.occupancy_R_allo_ascii_txt_3  ),
     bootstrap_CI( r3.occupancy_R_allo_jpg_3  ),
     bootstrap_CI( r3.occupancy_R_allo_json_3  ),
     bootstrap_CI( r3.occupancy_R_allo_tokenized_txt_3 )]
hw_6x6_R_allo=[
     bootstrap_CI( r6.line_R_allo_adj_json_6  ),
     bootstrap_CI( r6.line_R_allo_adj_txt_6  ),
     bootstrap_CI( r6.line_R_allo_jpg_6  ),
     bootstrap_CI( r6.line_R_allo_json_6  ),
     bootstrap_CI( r6.line_R_allo_tokenized_txt_6  ),
     bootstrap_CI( r6.occupancy_R_allo_adj_json_6  ),
     bootstrap_CI( r6.occupancy_R_allo_adj_txt_6  ),
     bootstrap_CI( r6.occupancy_R_allo_ascii_txt_6  ),
     bootstrap_CI( r6.occupancy_R_allo_jpg_6  ),
     bootstrap_CI( r6.occupancy_R_allo_json_6  ),
     bootstrap_CI( r6.occupancy_R_allo_tokenized_txt_6 )]
hw_15x15_R_allo=[
     bootstrap_CI( r15.line_R_allo_adj_json_15  ),
     bootstrap_CI( r15.line_R_allo_adj_txt_15  ),
     bootstrap_CI( r15.line_R_allo_jpg_15  ),
     bootstrap_CI( r15.line_R_allo_json_15  ),
     bootstrap_CI( r15.line_R_allo_tokenized_txt_15  ),
     bootstrap_CI( r15.occupancy_R_allo_adj_json_15  ),
     bootstrap_CI( r15.occupancy_R_allo_adj_txt_15  ),
     bootstrap_CI( r15.occupancy_R_allo_ascii_txt_15  ),
     bootstrap_CI( r15.occupancy_R_allo_jpg_15  ),
     bootstrap_CI( r15.occupancy_R_allo_json_15  ),
     bootstrap_CI( r15.occupancy_R_allo_tokenized_txt_15 )]

# # R -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
hw_3x3_R_ego = [
     bootstrap_CI( r3.line_R_ego_adj_json_3  ),
     bootstrap_CI( r3.line_R_ego_adj_txt_3  ),
     bootstrap_CI( r3.line_R_ego_jpg_3  ),
     bootstrap_CI( r3.line_R_ego_json_3  ),
     bootstrap_CI( r3.line_R_ego_tokenized_txt_3  ),
     bootstrap_CI( r3.occupancy_R_ego_adj_json_3  ),
     bootstrap_CI( r3.occupancy_R_ego_adj_txt_3  ),
     bootstrap_CI( r3.occupancy_R_ego_ascii_txt_3  ),
     bootstrap_CI( r3.occupancy_R_ego_jpg_3  ),
     bootstrap_CI( r3.occupancy_R_ego_json_3  ),
     bootstrap_CI( r3.occupancy_R_ego_tokenized_txt_3 )]
hw_6x6_R_ego=[
     bootstrap_CI( r6.line_R_ego_adj_json_6  ),
     bootstrap_CI( r6.line_R_ego_adj_txt_6  ),
     bootstrap_CI( r6.line_R_ego_jpg_6  ),
     bootstrap_CI( r6.line_R_ego_json_6  ),
     bootstrap_CI( r6.line_R_ego_tokenized_txt_6  ),
     bootstrap_CI( r6.occupancy_R_ego_adj_json_6  ),
     bootstrap_CI( r6.occupancy_R_ego_adj_txt_6  ),
     bootstrap_CI( r6.occupancy_R_ego_ascii_txt_6  ),
     bootstrap_CI( r6.occupancy_R_ego_jpg_6  ),
     bootstrap_CI( r6.occupancy_R_ego_json_6  ),
     bootstrap_CI( r6.occupancy_R_ego_tokenized_txt_6 )]
hw_15x15_R_ego=[
     bootstrap_CI( r15.line_R_ego_adj_json_15  ),
     bootstrap_CI( r15.line_R_ego_adj_txt_15  ),
     bootstrap_CI( r15.line_R_ego_jpg_15  ),
     bootstrap_CI( r15.line_R_ego_json_15  ),
     bootstrap_CI( r15.line_R_ego_tokenized_txt_15  ),
     bootstrap_CI( r15.occupancy_R_ego_adj_json_15  ),
     bootstrap_CI( r15.occupancy_R_ego_adj_txt_15  ),
     bootstrap_CI( r15.occupancy_R_ego_ascii_txt_15  ),
     bootstrap_CI( r15.occupancy_R_ego_jpg_15  ),
     bootstrap_CI( r15.occupancy_R_ego_json_15  ),
     bootstrap_CI( r15.occupancy_R_ego_tokenized_txt_15 )]




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

plt.suptitle("Half-Widths of the 95% Confidence Interval for the Mean Completion Scores, Given in Percentage Points,\nComputed separately for Each Combination of Spatial Representation, Output FoR, Maze Size, and LLM", fontsize=14)
plt.title("3x3/7x7 Mazes", fontsize=12)
# '''Sample sizes were determined so that the 95% confidence interval for the mean completion score 
# would have a half-width no greater than 5 percentage points, computed separately for each combination of 
# Spatial Representation, output frame of reference, maze size, and LLM'''

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

plt.suptitle("Half-Widths of the 95% Confidence Interval for the Mean Completion Scores, Given in Percentage Points,\nComputed separately for Each Combination of Spatial Representation, Output FoR, Maze Size, and LLM", fontsize=14)
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

plt.suptitle("Half-Widths of the 95% Confidence Interval for the Mean Completion Scores, Given in Percentage Points,\nComputed separately for Each Combination of Spatial Representation, Output FoR, Maze Size, and LLM", fontsize=14)
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
plt.show()





list_half = [
            #  hw_15x15_NR_allo, 
            #  hw_15x15_NR_ego, 
            #  hw_15x15_NR_coords,
            #  hw_15x15_R_coords,
            #  hw_15x15_R_allo, 
            #  hw_15x15_R_ego,
            #  hw_6x6_NR_allo,
            #  hw_6x6_NR_ego,
            #  hw_6x6_NR_coords, 
            #  hw_6x6_R_coords,
            #  hw_6x6_R_allo,
            #  hw_6x6_R_ego,
             hw_3x3_NR_ego,
             hw_3x3_NR_coords,
             hw_3x3_NR_allo,
             hw_3x3_R_coords,
             hw_3x3_R_allo,
             hw_3x3_R_ego
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
            elif 2.5 <= val < 5.0:
                empty1 +=1
            elif 5.0 <= val < 7.5:
                empty2 +=1
            elif 7.5 <= val < 10.0:
                empty3 +=1
            elif 10.0<=val <12.5:
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

