"""
Created on Wed Nov 26 19:14:00 2025
@author: valer
This code calculates the average accuracy and average output token count for each representation and condition in the Dataset03 experiment, 
for the 3x3, 6x6, and 15x15 grid sizes. The results are imported from separate files for each grid size.
The output of this file is a chart that shows model performance as a function of test compute for both LLMs.
By deselecting and selecting some sections, you can include or exclude reasoning and/or final answer tokens from the output token count.
"""



# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple, HandlerBase
from matplotlib import figure, rcParams
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15



representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']
# X-axis labels
x_labels = ['Coordinates', 'Allocentric', 'Egocentric']
x_vals = np.arange(len(x_labels))

# 3x3 NR - COORDS - 1-10 ----------------------------------------------------------------
avg_line_NR_coords_jpg_3 = np.mean(r3.line_NR_coords_jpg_3)
avg_line_NR_coords_json_3 = np.mean(r3.line_NR_coords_json_3)
avg_occupancy_NR_coords_jpg_3 = np.mean(r3.occupancy_NR_coords_jpg_3)
avg_occupancy_NR_coords_json_3 = np.mean(r3.occupancy_NR_coords_json_3)
avg_line_NR_coords_adj_json_3 = np.mean(r3.line_NR_coords_adj_json_3)
avg_line_NR_coords_adj_txt_3 = np.mean(r3.line_NR_coords_adj_txt_3)
avg_line_NR_coords_tokenized_txt_3 = np.mean(r3.line_NR_coords_tokenized_txt_3)
avg_occupancy_NR_coords_adj_json_3 = np.mean(r3.occupancy_NR_coords_adj_json_3)
avg_occupancy_NR_coords_adj_txt_3 = np.mean(r3.occupancy_NR_coords_adj_txt_3)
avg_occupancy_NR_coords_ascii_txt_3 = np.mean(r3.occupancy_NR_coords_ascii_txt_3)
avg_occupancy_NR_coords_tokenized_txt_3 = np.mean(r3.occupancy_NR_coords_tokenized_txt_3)

avg_line_NR_coords_jpg_output_3 = np.mean(r3.line_NR_coords_jpg_output_tokens_3)
avg_line_NR_coords_json_output_3 = np.mean(r3.line_NR_coords_json_output_tokens_3)
avg_occupancy_NR_coords_jpg_output_3 = np.mean(r3.occupancy_NR_coords_jpg_output_tokens_3)
avg_occupancy_NR_coords_json_output_3 = np.mean(r3.occupancy_NR_coords_json_output_tokens_3)
avg_line_NR_coords_adj_json_output_3 = np.mean(r3.line_NR_coords_adj_json_output_tokens_3)
avg_line_NR_coords_adj_txt_output_3 = np.mean(r3.line_NR_coords_adj_txt_output_tokens_3)
avg_line_NR_coords_tokenized_txt_output_3 = np.mean(r3.line_NR_coords_tokenized_txt_output_tokens_3)
avg_occupancy_NR_coords_adj_json_output_3 = np.mean(r3.occupancy_NR_coords_adj_json_output_tokens_3)
avg_occupancy_NR_coords_adj_txt_output_3 = np.mean(r3.occupancy_NR_coords_adj_txt_output_tokens_3)
avg_occupancy_NR_coords_ascii_txt_output_3 = np.mean(r3.occupancy_NR_coords_ascii_txt_output_tokens_3)
avg_occupancy_NR_coords_tokenized_txt_output_3 = np.mean(r3.occupancy_NR_coords_tokenized_txt_output_tokens_3)

# 3x3NR - ALLO - 1-10 ----------------------------------------------------------------

avg_line_NR_allo_jpg_3 = np.mean(r3.line_NR_allo_jpg_3)
avg_line_NR_allo_json_3 = np.mean(r3.line_NR_allo_json_3)
avg_occupancy_NR_allo_jpg_3 = np.mean(r3.occupancy_NR_allo_jpg_3)
avg_occupancy_NR_allo_json_3 = np.mean(r3.occupancy_NR_allo_json_3)
avg_line_NR_allo_adj_json_3 = np.mean(r3.line_NR_allo_adj_json_3)
avg_line_NR_allo_adj_txt_3 = np.mean(r3.line_NR_allo_adj_txt_3)
avg_line_NR_allo_tokenized_txt_3 = np.mean(r3.line_NR_allo_tokenized_txt_3)
avg_occupancy_NR_allo_adj_json_3 = np.mean(r3.occupancy_NR_allo_adj_json_3)
avg_occupancy_NR_allo_adj_txt_3 = np.mean(r3.occupancy_NR_allo_adj_txt_3)
avg_occupancy_NR_allo_ascii_txt_3 = np.mean(r3.occupancy_NR_allo_ascii_txt_3)
avg_occupancy_NR_allo_tokenized_txt_3 = np.mean(r3.occupancy_NR_allo_tokenized_txt_3)

avg_line_NR_allo_jpg_output_3 = np.mean(r3.line_NR_allo_jpg_output_tokens_3)
avg_line_NR_allo_json_output_3 = np.mean(r3.line_NR_allo_json_output_tokens_3)
avg_occupancy_NR_allo_jpg_output_3 = np.mean(r3.occupancy_NR_allo_jpg_output_tokens_3)
avg_occupancy_NR_allo_json_output_3 = np.mean(r3.occupancy_NR_allo_json_output_tokens_3)
avg_line_NR_allo_adj_json_output_3 = np.mean(r3.line_NR_allo_adj_json_output_tokens_3)
avg_line_NR_allo_adj_txt_output_3 = np.mean(r3.line_NR_allo_adj_txt_output_tokens_3)
avg_line_NR_allo_tokenized_txt_output_3 = np.mean(r3.line_NR_allo_tokenized_txt_output_tokens_3)
avg_occupancy_NR_allo_adj_json_output_3 = np.mean(r3.occupancy_NR_allo_adj_json_output_tokens_3)
avg_occupancy_NR_allo_adj_txt_output_3 = np.mean(r3.occupancy_NR_allo_adj_txt_output_tokens_3)
avg_occupancy_NR_allo_ascii_txt_output_3 = np.mean(r3.occupancy_NR_allo_ascii_txt_output_tokens_3)
avg_occupancy_NR_allo_tokenized_txt_output_3 = np.mean(r3.occupancy_NR_allo_tokenized_txt_output_tokens_3)

# 3x3 NR - EGO - 1-10 ----------------------------------------------------------------
avg_line_NR_ego_jpg_3 = np.mean(r3.line_NR_ego_jpg_3)
avg_line_NR_ego_json_3 = np.mean(r3.line_NR_ego_json_3)
avg_occupancy_NR_ego_jpg_3 = np.mean(r3.occupancy_NR_ego_jpg_3)
avg_occupancy_NR_ego_json_3 = np.mean(r3.occupancy_NR_ego_json_3)
avg_line_NR_ego_adj_json_3 = np.mean(r3.line_NR_ego_adj_json_3)
avg_line_NR_ego_adj_txt_3 = np.mean(r3.line_NR_ego_adj_txt_3)
avg_line_NR_ego_tokenized_txt_3 = np.mean(r3.line_NR_ego_tokenized_txt_3)
avg_occupancy_NR_ego_adj_json_3 = np.mean(r3.occupancy_NR_ego_adj_json_3)
avg_occupancy_NR_ego_adj_txt_3 = np.mean(r3.occupancy_NR_ego_adj_txt_3)
avg_occupancy_NR_ego_ascii_txt_3 = np.mean(r3.occupancy_NR_ego_ascii_txt_3)
avg_occupancy_NR_ego_tokenized_txt_3 = np.mean(r3.occupancy_NR_ego_tokenized_txt_3)

avg_line_NR_ego_jpg_output_3 = np.mean(r3.line_NR_ego_jpg_output_tokens_3)
avg_line_NR_ego_json_output_3 = np.mean(r3.line_NR_ego_json_output_tokens_3)
avg_occupancy_NR_ego_jpg_output_3 = np.mean(r3.occupancy_NR_ego_jpg_output_tokens_3)
avg_occupancy_NR_ego_json_output_3 = np.mean(r3.occupancy_NR_ego_json_output_tokens_3)
avg_line_NR_ego_adj_json_output_3 = np.mean(r3.line_NR_ego_adj_json_output_tokens_3)
avg_line_NR_ego_adj_txt_output_3 = np.mean(r3.line_NR_ego_adj_txt_output_tokens_3)
avg_line_NR_ego_tokenized_txt_output_3 = np.mean(r3.line_NR_ego_tokenized_txt_output_tokens_3)
avg_occupancy_NR_ego_adj_json_output_3 = np.mean(r3.occupancy_NR_ego_adj_json_output_tokens_3)
avg_occupancy_NR_ego_adj_txt_output_3 = np.mean(r3.occupancy_NR_ego_adj_txt_output_tokens_3)
avg_occupancy_NR_ego_ascii_txt_output_3 = np.mean(r3.occupancy_NR_ego_ascii_txt_output_tokens_3)
avg_occupancy_NR_ego_tokenized_txt_output_3 = np.mean(r3.occupancy_NR_ego_tokenized_txt_output_tokens_3)


# 3x3 R - COORDS -  - 1-10 ----------------------------------------------------------------
avg_line_R_coords_jpg_3 = np.mean(r3.line_R_coords_jpg_3)
avg_line_R_coords_json_3 = np.mean(r3.line_R_coords_json_3)
avg_occupancy_R_coords_jpg_3 = np.mean(r3.occupancy_R_coords_jpg_3)
avg_occupancy_R_coords_json_3 = np.mean(r3.occupancy_R_coords_json_3)
avg_line_R_coords_adj_json_3 = np.mean(r3.line_R_coords_adj_json_3)
avg_line_R_coords_adj_txt_3 = np.mean(r3.line_R_coords_adj_txt_3)
avg_line_R_coords_tokenized_txt_3 = np.mean(r3.line_R_coords_tokenized_txt_3)
avg_occupancy_R_coords_adj_json_3 = np.mean(r3.occupancy_R_coords_adj_json_3)
avg_occupancy_R_coords_adj_txt_3 = np.mean(r3.occupancy_R_coords_adj_txt_3)
avg_occupancy_R_coords_ascii_txt_3 = np.mean(r3.occupancy_R_coords_ascii_txt_3)
avg_occupancy_R_coords_tokenized_txt_3 = np.mean(r3.occupancy_R_coords_tokenized_txt_3)

avg_line_R_coords_jpg_output_3 = np.mean(r3.line_R_coords_jpg_output_tokens_3)
avg_line_R_coords_json_output_3 = np.mean(r3.line_R_coords_json_output_tokens_3)
avg_occupancy_R_coords_jpg_output_3 = np.mean(r3.occupancy_R_coords_jpg_output_tokens_3)
avg_occupancy_R_coords_json_output_3 = np.mean(r3.occupancy_R_coords_json_output_tokens_3)
avg_line_R_coords_adj_json_output_3 = np.mean(r3.line_R_coords_adj_json_output_tokens_3)
avg_line_R_coords_adj_txt_output_3 = np.mean(r3.line_R_coords_adj_txt_output_tokens_3)
avg_line_R_coords_tokenized_txt_output_3 = np.mean(r3.line_R_coords_tokenized_txt_output_tokens_3)
avg_occupancy_R_coords_adj_json_output_3 = np.mean(r3.occupancy_R_coords_adj_json_output_tokens_3)
avg_occupancy_R_coords_adj_txt_output_3 = np.mean(r3.occupancy_R_coords_adj_txt_output_tokens_3)
avg_occupancy_R_coords_ascii_txt_output_3 = np.mean(r3.occupancy_R_coords_ascii_txt_output_tokens_3)
avg_occupancy_R_coords_tokenized_txt_output_3 = np.mean(r3.occupancy_R_coords_tokenized_txt_output_tokens_3)

avg_final_line_R_coords_jpg_3 = np.nanmean(r3.line_R_coords_jpg_final_answer_3)
avg_final_line_R_coords_json_3 = np.nanmean(r3.line_R_coords_json_final_answer_3)
avg_final_occupancy_R_coords_jpg_3 = np.nanmean(r3.occupancy_R_coords_jpg_final_answer_3)
avg_final_occupancy_R_coords_json_3 = np.nanmean(r3.occupancy_R_coords_json_final_answer_3)
avg_final_line_R_coords_adj_json_3 = np.nanmean(r3.line_R_coords_adj_json_final_answer_3)
avg_final_line_R_coords_adj_txt_3 = np.nanmean(r3.line_R_coords_adj_txt_final_answer_3)
avg_final_line_R_coords_tokenized_txt_3 = np.nanmean(r3.line_R_coords_tokenized_txt_final_answer_3)
avg_final_occupancy_R_coords_adj_json_3 = np.nanmean(r3.occupancy_R_coords_adj_json_final_answer_3)
avg_final_occupancy_R_coords_adj_txt_3 = np.nanmean(r3.occupancy_R_coords_adj_txt_final_answer_3)
avg_final_occupancy_R_coords_ascii_txt_3 = np.nanmean(r3.occupancy_R_coords_ascii_txt_final_answer_3)
avg_final_occupancy_R_coords_tokenized_txt_3 = np.nanmean(r3.occupancy_R_coords_tokenized_txt_final_answer_3)

# 3x3 R - ALLO -  - 1-10 ----------------------------------------------------------------
avg_line_R_allo_jpg_3 = np.mean(r3.line_R_allo_jpg_3)
avg_line_R_allo_json_3 = np.mean(r3.line_R_allo_json_3)
avg_occupancy_R_allo_jpg_3 = np.mean(r3.occupancy_R_allo_jpg_3)
avg_occupancy_R_allo_json_3 = np.mean(r3.occupancy_R_allo_json_3)
avg_line_R_allo_adj_json_3 = np.mean(r3.line_R_allo_adj_json_3)
avg_line_R_allo_adj_txt_3 = np.mean(r3.line_R_allo_adj_txt_3)
avg_line_R_allo_tokenized_txt_3 = np.mean(r3.line_R_allo_tokenized_txt_3)
avg_occupancy_R_allo_adj_json_3 = np.mean(r3.occupancy_R_allo_adj_json_3)
avg_occupancy_R_allo_adj_txt_3 = np.mean(r3.occupancy_R_allo_adj_txt_3)
avg_occupancy_R_allo_ascii_txt_3 = np.mean(r3.occupancy_R_allo_ascii_txt_3)
avg_occupancy_R_allo_tokenized_txt_3 = np.mean(r3.occupancy_R_allo_tokenized_txt_3)

avg_line_R_allo_jpg_output_3 = np.mean(r3.line_R_allo_jpg_output_tokens_3)
avg_line_R_allo_json_output_3 = np.mean(r3.line_R_allo_json_output_tokens_3)
avg_occupancy_R_allo_jpg_output_3 = np.mean(r3.occupancy_R_allo_jpg_output_tokens_3)
avg_occupancy_R_allo_json_output_3 = np.mean(r3.occupancy_R_allo_json_output_tokens_3)
avg_line_R_allo_adj_json_output_3 = np.mean(r3.line_R_allo_adj_json_output_tokens_3)
avg_line_R_allo_adj_txt_output_3 = np.mean(r3.line_R_allo_adj_txt_output_tokens_3)
avg_line_R_allo_tokenized_txt_output_3 = np.mean(r3.line_R_allo_tokenized_txt_output_tokens_3)
avg_occupancy_R_allo_adj_json_output_3 = np.mean(r3.occupancy_R_allo_adj_json_output_tokens_3)
avg_occupancy_R_allo_adj_txt_output_3 = np.mean(r3.occupancy_R_allo_adj_txt_output_tokens_3)
avg_occupancy_R_allo_ascii_txt_output_3 = np.mean(r3.occupancy_R_allo_ascii_txt_output_tokens_3)
avg_occupancy_R_allo_tokenized_txt_output_3 = np.mean(r3.occupancy_R_allo_tokenized_txt_output_tokens_3)

avg_final_line_R_allo_jpg_3 = np.nanmean(r3.line_R_allo_jpg_final_answer_3)
avg_final_line_R_allo_json_3 = np.nanmean(r3.line_R_allo_json_final_answer_3)
avg_final_occupancy_R_allo_jpg_3 = np.nanmean(r3.occupancy_R_allo_jpg_final_answer_3)
avg_final_occupancy_R_allo_json_3 = np.nanmean(r3.occupancy_R_allo_json_final_answer_3)
avg_final_line_R_allo_adj_json_3 = np.nanmean(r3.line_R_allo_adj_json_final_answer_3)
avg_final_line_R_allo_adj_txt_3 = np.nanmean(r3.line_R_allo_adj_txt_final_answer_3)
avg_final_line_R_allo_tokenized_txt_3 = np.nanmean(r3.line_R_allo_tokenized_txt_final_answer_3)
avg_final_occupancy_R_allo_adj_json_3 = np.nanmean(r3.occupancy_R_allo_adj_json_final_answer_3)
avg_final_occupancy_R_allo_adj_txt_3 = np.nanmean(r3.occupancy_R_allo_adj_txt_final_answer_3)
avg_final_occupancy_R_allo_ascii_txt_3 = np.nanmean(r3.occupancy_R_allo_ascii_txt_final_answer_3)
avg_final_occupancy_R_allo_tokenized_txt_3 = np.nanmean(r3.occupancy_R_allo_tokenized_txt_final_answer_3)

# 3x3 R - EGO -  - 1-10 ----------------------------------------------------------------
avg_line_R_ego_jpg_3 = np.mean(r3.line_R_ego_jpg_3)
avg_line_R_ego_json_3 = np.mean(r3.line_R_ego_json_3)
avg_occupancy_R_ego_jpg_3 = np.mean(r3.occupancy_R_ego_jpg_3)
avg_occupancy_R_ego_json_3 = np.mean(r3.occupancy_R_ego_json_3)
avg_line_R_ego_adj_json_3 = np.mean(r3.line_R_ego_adj_json_3)
avg_line_R_ego_adj_txt_3 = np.mean(r3.line_R_ego_adj_txt_3)
avg_line_R_ego_tokenized_txt_3 = np.mean(r3.line_R_ego_tokenized_txt_3)
avg_occupancy_R_ego_adj_json_3 = np.mean(r3.occupancy_R_ego_adj_json_3)
avg_occupancy_R_ego_adj_txt_3 = np.mean(r3.occupancy_R_ego_adj_txt_3)
avg_occupancy_R_ego_ascii_txt_3 = np.mean(r3.occupancy_R_ego_ascii_txt_3)
avg_occupancy_R_ego_tokenized_txt_3 = np.mean(r3.occupancy_R_ego_tokenized_txt_3)

avg_line_R_ego_jpg_output_3 = np.mean(r3.line_R_ego_jpg_output_tokens_3)
avg_line_R_ego_json_output_3 = np.mean(r3.line_R_ego_json_output_tokens_3)
avg_occupancy_R_ego_jpg_output_3 = np.mean(r3.occupancy_R_ego_jpg_output_tokens_3)
avg_occupancy_R_ego_json_output_3 = np.mean(r3.occupancy_R_ego_json_output_tokens_3)
avg_line_R_ego_adj_json_output_3 = np.mean(r3.line_R_ego_adj_json_output_tokens_3)
avg_line_R_ego_adj_txt_output_3 = np.mean(r3.line_R_ego_adj_txt_output_tokens_3)
avg_line_R_ego_tokenized_txt_output_3 = np.mean(r3.line_R_ego_tokenized_txt_output_tokens_3)
avg_occupancy_R_ego_adj_json_output_3 = np.mean(r3.occupancy_R_ego_adj_json_output_tokens_3)
avg_occupancy_R_ego_adj_txt_output_3 = np.mean(r3.occupancy_R_ego_adj_txt_output_tokens_3)
avg_occupancy_R_ego_ascii_txt_output_3 = np.mean(r3.occupancy_R_ego_ascii_txt_output_tokens_3)
avg_occupancy_R_ego_tokenized_txt_output_3 = np.mean(r3.occupancy_R_ego_tokenized_txt_output_tokens_3)

avg_final_line_R_ego_jpg_3 = np.nanmean(r3.line_R_ego_jpg_final_answer_3)
avg_final_line_R_ego_json_3 = np.nanmean(r3.line_R_ego_json_final_answer_3)
avg_final_occupancy_R_ego_jpg_3 = np.nanmean(r3.occupancy_R_ego_jpg_final_answer_3)
avg_final_occupancy_R_ego_json_3 = np.nanmean(r3.occupancy_R_ego_json_final_answer_3)
avg_final_line_R_ego_adj_json_3 = np.nanmean(r3.line_R_ego_adj_json_final_answer_3)
avg_final_line_R_ego_adj_txt_3 = np.nanmean(r3.line_R_ego_adj_txt_final_answer_3)
avg_final_line_R_ego_tokenized_txt_3 = np.nanmean(r3.line_R_ego_tokenized_txt_final_answer_3)
avg_final_occupancy_R_ego_adj_json_3 = np.nanmean(r3.occupancy_R_ego_adj_json_final_answer_3)
avg_final_occupancy_R_ego_adj_txt_3 = np.nanmean(r3.occupancy_R_ego_adj_txt_final_answer_3)
avg_final_occupancy_R_ego_ascii_txt_3 = np.nanmean(r3.occupancy_R_ego_ascii_txt_final_answer_3)
avg_final_occupancy_R_ego_tokenized_txt_3 = np.nanmean(r3.occupancy_R_ego_tokenized_txt_final_answer_3)
# -----------------------------------------------------------------------------------------------------------------------------------



# 6x6 NR - COORDS - 1-10 ----------------------------------------------------------------
avg_line_NR_coords_jpg_6 = np.mean(r6.line_NR_coords_jpg_6)
avg_line_NR_coords_json_6 = np.mean(r6.line_NR_coords_json_6)
avg_occupancy_NR_coords_jpg_6 = np.mean(r6.occupancy_NR_coords_jpg_6)
avg_occupancy_NR_coords_json_6 = np.mean(r6.occupancy_NR_coords_json_6)
avg_line_NR_coords_adj_json_6 = np.mean(r6.line_NR_coords_adj_json_6)
avg_line_NR_coords_adj_txt_6 = np.mean(r6.line_NR_coords_adj_txt_6)
avg_line_NR_coords_tokenized_txt_6 = np.mean(r6.line_NR_coords_tokenized_txt_6)
avg_occupancy_NR_coords_adj_json_6 = np.mean(r6.occupancy_NR_coords_adj_json_6)
avg_occupancy_NR_coords_adj_txt_6 = np.mean(r6.occupancy_NR_coords_adj_txt_6)
avg_occupancy_NR_coords_ascii_txt_6 = np.mean(r6.occupancy_NR_coords_ascii_txt_6)
avg_occupancy_NR_coords_tokenized_txt_6 = np.mean(r6.occupancy_NR_coords_tokenized_txt_6)

avg_line_NR_coords_jpg_output_6 = np.mean(r6.line_NR_coords_jpg_output_tokens_6)
avg_line_NR_coords_json_output_6 = np.mean(r6.line_NR_coords_json_output_tokens_6)
avg_occupancy_NR_coords_jpg_output_6 = np.mean(r6.occupancy_NR_coords_jpg_output_tokens_6)
avg_occupancy_NR_coords_json_output_6 = np.mean(r6.occupancy_NR_coords_json_output_tokens_6)
avg_line_NR_coords_adj_json_output_6 = np.mean(r6.line_NR_coords_adj_json_output_tokens_6)
avg_line_NR_coords_adj_txt_output_6 = np.mean(r6.line_NR_coords_adj_txt_output_tokens_6)
avg_line_NR_coords_tokenized_txt_output_6 = np.mean(r6.line_NR_coords_tokenized_txt_output_tokens_6)
avg_occupancy_NR_coords_adj_json_output_6 = np.mean(r6.occupancy_NR_coords_adj_json_output_tokens_6)
avg_occupancy_NR_coords_adj_txt_output_6 = np.mean(r6.occupancy_NR_coords_adj_txt_output_tokens_6)
avg_occupancy_NR_coords_ascii_txt_output_6 = np.mean(r6.occupancy_NR_coords_ascii_txt_output_tokens_6)
avg_occupancy_NR_coords_tokenized_txt_output_6 = np.mean(r6.occupancy_NR_coords_tokenized_txt_output_tokens_6)


# 6x6 NR - ALLO - 1-10 ----------------------------------------------------------------
avg_line_NR_allo_jpg_6 = np.mean(r6.line_NR_allo_jpg_6)
avg_line_NR_allo_json_6 = np.mean(r6.line_NR_allo_json_6)
avg_occupancy_NR_allo_jpg_6 = np.mean(r6.occupancy_NR_allo_jpg_6)
avg_occupancy_NR_allo_json_6 = np.mean(r6.occupancy_NR_allo_json_6)
avg_line_NR_allo_adj_json_6 = np.mean(r6.line_NR_allo_adj_json_6)
avg_line_NR_allo_adj_txt_6 = np.mean(r6.line_NR_allo_adj_txt_6)
avg_line_NR_allo_tokenized_txt_6 = np.mean(r6.line_NR_allo_tokenized_txt_6)
avg_occupancy_NR_allo_adj_json_6 = np.mean(r6.occupancy_NR_allo_adj_json_6)
avg_occupancy_NR_allo_adj_txt_6 = np.mean(r6.occupancy_NR_allo_adj_txt_6)
avg_occupancy_NR_allo_ascii_txt_6 = np.mean(r6.occupancy_NR_allo_ascii_txt_6)
avg_occupancy_NR_allo_tokenized_txt_6 = np.mean(r6.occupancy_NR_allo_tokenized_txt_6)

avg_line_NR_allo_jpg_output_6 = np.mean(r6.line_NR_allo_jpg_output_tokens_6)
avg_line_NR_allo_json_output_6 = np.mean(r6.line_NR_allo_json_output_tokens_6)
avg_occupancy_NR_allo_jpg_output_6 = np.mean(r6.occupancy_NR_allo_jpg_output_tokens_6)
avg_occupancy_NR_allo_json_output_6 = np.mean(r6.occupancy_NR_allo_json_output_tokens_6)
avg_line_NR_allo_adj_json_output_6 = np.mean(r6.line_NR_allo_adj_json_output_tokens_6)
avg_line_NR_allo_adj_txt_output_6 = np.mean(r6.line_NR_allo_adj_txt_output_tokens_6)
avg_line_NR_allo_tokenized_txt_output_6 = np.mean(r6.line_NR_allo_tokenized_txt_output_tokens_6)
avg_occupancy_NR_allo_adj_json_output_6 = np.mean(r6.occupancy_NR_allo_adj_json_output_tokens_6)
avg_occupancy_NR_allo_adj_txt_output_6 = np.mean(r6.occupancy_NR_allo_adj_txt_output_tokens_6)
avg_occupancy_NR_allo_ascii_txt_output_6 = np.mean(r6.occupancy_NR_allo_ascii_txt_output_tokens_6)
avg_occupancy_NR_allo_tokenized_txt_output_6 = np.mean(r6.occupancy_NR_allo_tokenized_txt_output_tokens_6)

# 6x6 NR - EGO - 1-10 ----------------------------------------------------------------
avg_line_NR_ego_jpg_6 = np.mean(r6.line_NR_ego_jpg_6)
avg_line_NR_ego_json_6 = np.mean(r6.line_NR_ego_json_6)
avg_occupancy_NR_ego_jpg_6 = np.mean(r6.occupancy_NR_ego_jpg_6)
avg_occupancy_NR_ego_json_6 = np.mean(r6.occupancy_NR_ego_json_6)
avg_line_NR_ego_adj_json_6 = np.mean(r6.line_NR_ego_adj_json_6)
avg_line_NR_ego_adj_txt_6 = np.mean(r6.line_NR_ego_adj_txt_6)
avg_line_NR_ego_tokenized_txt_6 = np.mean(r6.line_NR_ego_tokenized_txt_6)
avg_occupancy_NR_ego_adj_json_6 = np.mean(r6.occupancy_NR_ego_adj_json_6)
avg_occupancy_NR_ego_adj_txt_6 = np.mean(r6.occupancy_NR_ego_adj_txt_6)
avg_occupancy_NR_ego_ascii_txt_6 = np.mean(r6.occupancy_NR_ego_ascii_txt_6)
avg_occupancy_NR_ego_tokenized_txt_6 = np.mean(r6.occupancy_NR_ego_tokenized_txt_6)

avg_line_NR_ego_jpg_output_6 = np.mean(r6.line_NR_ego_jpg_output_tokens_6)
avg_line_NR_ego_json_output_6 = np.mean(r6.line_NR_ego_json_output_tokens_6)
avg_occupancy_NR_ego_jpg_output_6 = np.mean(r6.occupancy_NR_ego_jpg_output_tokens_6)
avg_occupancy_NR_ego_json_output_6 = np.mean(r6.occupancy_NR_ego_json_output_tokens_6)
avg_line_NR_ego_adj_json_output_6 = np.mean(r6.line_NR_ego_adj_json_output_tokens_6)
avg_line_NR_ego_adj_txt_output_6 = np.mean(r6.line_NR_ego_adj_txt_output_tokens_6)
avg_line_NR_ego_tokenized_txt_output_6 = np.mean(r6.line_NR_ego_tokenized_txt_output_tokens_6)
avg_occupancy_NR_ego_adj_json_output_6 = np.mean(r6.occupancy_NR_ego_adj_json_output_tokens_6)
avg_occupancy_NR_ego_adj_txt_output_6 = np.mean(r6.occupancy_NR_ego_adj_txt_output_tokens_6)
avg_occupancy_NR_ego_ascii_txt_output_6 = np.mean(r6.occupancy_NR_ego_ascii_txt_output_tokens_6)
avg_occupancy_NR_ego_tokenized_txt_output_6 = np.mean(r6.occupancy_NR_ego_tokenized_txt_output_tokens_6)

# 6x6 R - COORDS - 1-10 ----------------------------------------------------------------
avg_line_R_coords_jpg_6 = np.mean(r6.line_R_coords_jpg_6)
avg_line_R_coords_json_6 = np.mean(r6.line_R_coords_json_6)
avg_occupancy_R_coords_jpg_6 = np.mean(r6.occupancy_R_coords_jpg_6)
avg_occupancy_R_coords_json_6 = np.mean(r6.occupancy_R_coords_json_6)
avg_line_R_coords_adj_json_6 = np.mean(r6.line_R_coords_adj_json_6)
avg_line_R_coords_adj_txt_6 = np.mean(r6.line_R_coords_adj_txt_6)
avg_line_R_coords_tokenized_txt_6 = np.mean(r6.line_R_coords_tokenized_txt_6)
avg_occupancy_R_coords_adj_json_6 = np.mean(r6.occupancy_R_coords_adj_json_6)
avg_occupancy_R_coords_adj_txt_6 = np.mean(r6.occupancy_R_coords_adj_txt_6)
avg_occupancy_R_coords_ascii_txt_6 = np.mean(r6.occupancy_R_coords_ascii_txt_6)
avg_occupancy_R_coords_tokenized_txt_6 = np.mean(r6.occupancy_R_coords_tokenized_txt_6)

avg_line_R_coords_jpg_output_6 = np.mean(r6.line_R_coords_jpg_output_tokens_6)
avg_line_R_coords_json_output_6 = np.mean(r6.line_R_coords_json_output_tokens_6)
avg_occupancy_R_coords_jpg_output_6 = np.mean(r6.occupancy_R_coords_jpg_output_tokens_6)
avg_occupancy_R_coords_json_output_6 = np.mean(r6.occupancy_R_coords_json_output_tokens_6)
avg_line_R_coords_adj_json_output_6 = np.mean(r6.line_R_coords_adj_json_output_tokens_6)
avg_line_R_coords_adj_txt_output_6 = np.mean(r6.line_R_coords_adj_txt_output_tokens_6)
avg_line_R_coords_tokenized_txt_output_6 = np.mean(r6.line_R_coords_tokenized_txt_output_tokens_6)
avg_occupancy_R_coords_adj_json_output_6 = np.mean(r6.occupancy_R_coords_adj_json_output_tokens_6)
avg_occupancy_R_coords_adj_txt_output_6 = np.mean(r6.occupancy_R_coords_adj_txt_output_tokens_6)
avg_occupancy_R_coords_ascii_txt_output_6 = np.mean(r6.occupancy_R_coords_ascii_txt_output_tokens_6)
avg_occupancy_R_coords_tokenized_txt_output_6 = np.mean(r6.occupancy_R_coords_tokenized_txt_output_tokens_6)


avg_final_line_R_coords_jpg_6 = np.mean(r6.line_R_coords_jpg_final_answer_6)
avg_final_line_R_coords_json_6 = np.mean(r6.line_R_coords_json_final_answer_6)
avg_final_occupancy_R_coords_jpg_6 = np.mean(r6.occupancy_R_coords_jpg_final_answer_6)
avg_final_occupancy_R_coords_json_6 = np.mean(r6.occupancy_R_coords_json_final_answer_6)
avg_final_line_R_coords_adj_json_6 = np.mean(r6.line_R_coords_adj_json_final_answer_6)
avg_final_line_R_coords_adj_txt_6 = np.mean(r6.line_R_coords_adj_txt_final_answer_6)
avg_final_line_R_coords_tokenized_txt_6 = np.mean(r6.line_R_coords_tokenized_txt_final_answer_6)
avg_final_occupancy_R_coords_adj_json_6 = np.mean(r6.occupancy_R_coords_adj_json_final_answer_6)
avg_final_occupancy_R_coords_adj_txt_6 = np.mean(r6.occupancy_R_coords_adj_txt_final_answer_6)
avg_final_occupancy_R_coords_ascii_txt_6 = np.mean(r6.occupancy_R_coords_ascii_txt_final_answer_6)
avg_final_occupancy_R_coords_tokenized_txt_6 = np.mean(r6.occupancy_R_coords_tokenized_txt_final_answer_6)

# 6x6 R - ALLO - 1-10 ----------------------------------------------------------------
avg_line_R_allo_jpg_6 = np.mean(r6.line_R_allo_jpg_6)
avg_line_R_allo_json_6 = np.mean(r6.line_R_allo_json_6)
avg_occupancy_R_allo_jpg_6 = np.mean(r6.occupancy_R_allo_jpg_6)
avg_occupancy_R_allo_json_6 = np.mean(r6.occupancy_R_allo_json_6)
avg_line_R_allo_adj_json_6 = np.mean(r6.line_R_allo_adj_json_6)
avg_line_R_allo_adj_txt_6 = np.mean(r6.line_R_allo_adj_txt_6)
avg_line_R_allo_tokenized_txt_6 = np.mean(r6.line_R_allo_tokenized_txt_6)
avg_occupancy_R_allo_adj_json_6 = np.mean(r6.occupancy_R_allo_adj_json_6)
avg_occupancy_R_allo_adj_txt_6 = np.mean(r6.occupancy_R_allo_adj_txt_6)
avg_occupancy_R_allo_ascii_txt_6 = np.mean(r6.occupancy_R_allo_ascii_txt_6)
avg_occupancy_R_allo_tokenized_txt_6 = np.mean(r6.occupancy_R_allo_tokenized_txt_6)

avg_line_R_allo_jpg_output_6 = np.mean(r6.line_R_allo_jpg_output_tokens_6)
avg_line_R_allo_json_output_6 = np.mean(r6.line_R_allo_json_output_tokens_6)
avg_occupancy_R_allo_jpg_output_6 = np.mean(r6.occupancy_R_allo_jpg_output_tokens_6)
avg_occupancy_R_allo_json_output_6 = np.mean(r6.occupancy_R_allo_json_output_tokens_6)
avg_line_R_allo_adj_json_output_6 = np.mean(r6.line_R_allo_adj_json_output_tokens_6)
avg_line_R_allo_adj_txt_output_6 = np.mean(r6.line_R_allo_adj_txt_output_tokens_6)
avg_line_R_allo_tokenized_txt_output_6 = np.mean(r6.line_R_allo_tokenized_txt_output_tokens_6)
avg_occupancy_R_allo_adj_json_output_6 = np.mean(r6.occupancy_R_allo_adj_json_output_tokens_6)
avg_occupancy_R_allo_adj_txt_output_6 = np.mean(r6.occupancy_R_allo_adj_txt_output_tokens_6)
avg_occupancy_R_allo_ascii_txt_output_6 = np.mean(r6.occupancy_R_allo_ascii_txt_output_tokens_6)
avg_occupancy_R_allo_tokenized_txt_output_6 = np.mean(r6.occupancy_R_allo_tokenized_txt_output_tokens_6)


avg_final_line_R_allo_jpg_6 = np.mean(r6.line_R_allo_jpg_final_answer_6)
avg_final_line_R_allo_json_6 = np.mean(r6.line_R_allo_json_final_answer_6)
avg_final_occupancy_R_allo_jpg_6 = np.mean(r6.occupancy_R_allo_jpg_final_answer_6)
avg_final_occupancy_R_allo_json_6 = np.mean(r6.occupancy_R_allo_json_final_answer_6)
avg_final_line_R_allo_adj_json_6 = np.mean(r6.line_R_allo_adj_json_final_answer_6)
avg_final_line_R_allo_adj_txt_6 = np.mean(r6.line_R_allo_adj_txt_final_answer_6)
avg_final_line_R_allo_tokenized_txt_6 = np.mean(r6.line_R_allo_tokenized_txt_final_answer_6)
avg_final_occupancy_R_allo_adj_json_6 = np.mean(r6.occupancy_R_allo_adj_json_final_answer_6)
avg_final_occupancy_R_allo_adj_txt_6 = np.mean(r6.occupancy_R_allo_adj_txt_final_answer_6)
avg_final_occupancy_R_allo_ascii_txt_6 = np.mean(r6.occupancy_R_allo_ascii_txt_final_answer_6)
avg_final_occupancy_R_allo_tokenized_txt_6 = np.mean(r6.occupancy_R_allo_tokenized_txt_final_answer_6)


# 6x6 - EGO - 1-10 ----------------------------------------------------------------
avg_line_R_ego_jpg_6 = np.mean(r6.line_R_ego_jpg_6)
avg_line_R_ego_json_6 = np.mean(r6.line_R_ego_json_6)
avg_occupancy_R_ego_jpg_6 = np.mean(r6.occupancy_R_ego_jpg_6)
avg_occupancy_R_ego_json_6 = np.mean(r6.occupancy_R_ego_json_6)
avg_line_R_ego_adj_json_6 = np.mean(r6.line_R_ego_adj_json_6)
avg_line_R_ego_adj_txt_6 = np.mean(r6.line_R_ego_adj_txt_6)
avg_line_R_ego_tokenized_txt_6 = np.mean(r6.line_R_ego_tokenized_txt_6)
avg_occupancy_R_ego_adj_json_6 = np.mean(r6.occupancy_R_ego_adj_json_6)
avg_occupancy_R_ego_adj_txt_6 = np.mean(r6.occupancy_R_ego_adj_txt_6)
avg_occupancy_R_ego_ascii_txt_6 = np.mean(r6.occupancy_R_ego_ascii_txt_6)
avg_occupancy_R_ego_tokenized_txt_6 = np.mean(r6.occupancy_R_ego_tokenized_txt_6)

avg_line_R_ego_jpg_output_6 = np.mean(r6.line_R_ego_jpg_output_tokens_6)
avg_line_R_ego_json_output_6 = np.mean(r6.line_R_ego_json_output_tokens_6)
avg_occupancy_R_ego_jpg_output_6 = np.mean(r6.occupancy_R_ego_jpg_output_tokens_6)
avg_occupancy_R_ego_json_output_6 = np.mean(r6.occupancy_R_ego_json_output_tokens_6)
avg_line_R_ego_adj_json_output_6 = np.mean(r6.line_R_ego_adj_json_output_tokens_6)
avg_line_R_ego_adj_txt_output_6 = np.mean(r6.line_R_ego_adj_txt_output_tokens_6)
avg_line_R_ego_tokenized_txt_output_6 = np.mean(r6.line_R_ego_tokenized_txt_output_tokens_6)
avg_occupancy_R_ego_adj_json_output_6 = np.mean(r6.occupancy_R_ego_adj_json_output_tokens_6)
avg_occupancy_R_ego_adj_txt_output_6 = np.mean(r6.occupancy_R_ego_adj_txt_output_tokens_6)
avg_occupancy_R_ego_ascii_txt_output_6 = np.mean(r6.occupancy_R_ego_ascii_txt_output_tokens_6)
avg_occupancy_R_ego_tokenized_txt_output_6 = np.mean(r6.occupancy_R_ego_tokenized_txt_output_tokens_6)


avg_final_line_R_ego_jpg_6 = np.mean(r6.line_R_ego_jpg_final_answer_6)
avg_final_line_R_ego_json_6 = np.mean(r6.line_R_ego_json_final_answer_6)
avg_final_occupancy_R_ego_jpg_6 = np.mean(r6.occupancy_R_ego_jpg_final_answer_6)
avg_final_occupancy_R_ego_json_6 = np.mean(r6.occupancy_R_ego_json_final_answer_6)
avg_final_line_R_ego_adj_json_6 = np.mean(r6.line_R_ego_adj_json_final_answer_6)
avg_final_line_R_ego_adj_txt_6 = np.mean(r6.line_R_ego_adj_txt_final_answer_6)
avg_final_line_R_ego_tokenized_txt_6 = np.mean(r6.line_R_ego_tokenized_txt_final_answer_6)
avg_final_occupancy_R_ego_adj_json_6 = np.mean(r6.occupancy_R_ego_adj_json_final_answer_6)
avg_final_occupancy_R_ego_adj_txt_6 = np.mean(r6.occupancy_R_ego_adj_txt_final_answer_6)
avg_final_occupancy_R_ego_ascii_txt_6 = np.mean(r6.occupancy_R_ego_ascii_txt_final_answer_6)
avg_final_occupancy_R_ego_tokenized_txt_6 = np.mean(r6.occupancy_R_ego_tokenized_txt_final_answer_6)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 15x15 NR - COORDS - 1-10 ----------------------------------------------------------------
avg_line_NR_coords_jpg_15 = np.mean(r15.line_NR_coords_jpg_15)
avg_line_NR_coords_json_15 = np.mean(r15.line_NR_coords_json_15)
avg_occupancy_NR_coords_jpg_15 = np.mean(r15.occupancy_NR_coords_jpg_15)
avg_occupancy_NR_coords_json_15 = np.mean(r15.occupancy_NR_coords_json_15)
avg_line_NR_coords_adj_json_15 = np.mean(r15.line_NR_coords_adj_json_15)
avg_line_NR_coords_adj_txt_15 = np.mean(r15.line_NR_coords_adj_txt_15)
avg_line_NR_coords_tokenized_txt_15 = np.mean(r15.line_NR_coords_tokenized_txt_15)
avg_occupancy_NR_coords_adj_json_15 = np.mean(r15.occupancy_NR_coords_adj_json_15)
avg_occupancy_NR_coords_adj_txt_15 = np.mean(r15.occupancy_NR_coords_adj_txt_15)
avg_occupancy_NR_coords_ascii_txt_15 = np.mean(r15.occupancy_NR_coords_ascii_txt_15)
avg_occupancy_NR_coords_tokenized_txt_15 = np.mean(r15.occupancy_NR_coords_tokenized_txt_15)

avg_line_NR_coords_jpg_output_15 = np.mean(r15.line_NR_coords_jpg_output_tokens_15)
avg_line_NR_coords_json_output_15 = np.mean(r15.line_NR_coords_json_output_tokens_15)
avg_occupancy_NR_coords_jpg_output_15 = np.mean(r15.occupancy_NR_coords_jpg_output_tokens_15)
avg_occupancy_NR_coords_json_output_15 = np.mean(r15.occupancy_NR_coords_json_output_tokens_15)
avg_line_NR_coords_adj_json_output_15 = np.mean(r15.line_NR_coords_adj_json_output_tokens_15)
avg_line_NR_coords_adj_txt_output_15 = np.mean(r15.line_NR_coords_adj_txt_output_tokens_15)
avg_line_NR_coords_tokenized_txt_output_15 = np.mean(r15.line_NR_coords_tokenized_txt_output_tokens_15)
avg_occupancy_NR_coords_adj_json_output_15 = np.mean(r15.occupancy_NR_coords_adj_json_output_tokens_15)
avg_occupancy_NR_coords_adj_txt_output_15 = np.mean(r15.occupancy_NR_coords_adj_txt_output_tokens_15)
avg_occupancy_NR_coords_ascii_txt_output_15 = np.mean(r15.occupancy_NR_coords_ascii_txt_output_tokens_15)
avg_occupancy_NR_coords_tokenized_txt_output_15 = np.mean(r15.occupancy_NR_coords_tokenized_txt_output_tokens_15)




# 15x15 NR - ALLO - 1-10 ----------------------------------------------------------------
avg_line_NR_allo_jpg_15 = np.mean(r15.line_NR_allo_jpg_15)
avg_line_NR_allo_json_15 = np.mean(r15.line_NR_allo_json_15)
avg_occupancy_NR_allo_jpg_15 = np.mean(r15.occupancy_NR_allo_jpg_15)
avg_occupancy_NR_allo_json_15 = np.mean(r15.occupancy_NR_allo_json_15)
avg_line_NR_allo_adj_json_15 = np.mean(r15.line_NR_allo_adj_json_15)
avg_line_NR_allo_adj_txt_15 = np.mean(r15.line_NR_allo_adj_txt_15)
avg_line_NR_allo_tokenized_txt_15 = np.mean(r15.line_NR_allo_tokenized_txt_15)
avg_occupancy_NR_allo_adj_json_15 = np.mean(r15.occupancy_NR_allo_adj_json_15)
avg_occupancy_NR_allo_adj_txt_15 = np.mean(r15.occupancy_NR_allo_adj_txt_15)
avg_occupancy_NR_allo_ascii_txt_15 = np.mean(r15.occupancy_NR_allo_ascii_txt_15)
avg_occupancy_NR_allo_tokenized_txt_15 = np.mean(r15.occupancy_NR_allo_tokenized_txt_15)

avg_line_NR_allo_jpg_output_15 = np.mean(r15.line_NR_allo_jpg_output_tokens_15)
avg_line_NR_allo_json_output_15 = np.mean(r15.line_NR_allo_json_output_tokens_15)
avg_occupancy_NR_allo_jpg_output_15 = np.mean(r15.occupancy_NR_allo_jpg_output_tokens_15)
avg_occupancy_NR_allo_json_output_15 = np.mean(r15.occupancy_NR_allo_json_output_tokens_15)
avg_line_NR_allo_adj_json_output_15 = np.mean(r15.line_NR_allo_adj_json_output_tokens_15)
avg_line_NR_allo_adj_txt_output_15 = np.mean(r15.line_NR_allo_adj_txt_output_tokens_15)
avg_line_NR_allo_tokenized_txt_output_15 = np.mean(r15.line_NR_allo_tokenized_txt_output_tokens_15)
avg_occupancy_NR_allo_adj_json_output_15 = np.mean(r15.occupancy_NR_allo_adj_json_output_tokens_15)
avg_occupancy_NR_allo_adj_txt_output_15 = np.mean(r15.occupancy_NR_allo_adj_txt_output_tokens_15)
avg_occupancy_NR_allo_ascii_txt_output_15 = np.mean(r15.occupancy_NR_allo_ascii_txt_output_tokens_15)
avg_occupancy_NR_allo_tokenized_txt_output_15 = np.mean(r15.occupancy_NR_allo_tokenized_txt_output_tokens_15)



# 15x15 NR - EGO - 1-10 ----------------------------------------------------------------
avg_line_NR_ego_jpg_15 = np.mean(r15.line_NR_ego_jpg_15)
avg_line_NR_ego_json_15 = np.mean(r15.line_NR_ego_json_15)
avg_occupancy_NR_ego_jpg_15 = np.mean(r15.occupancy_NR_ego_jpg_15)
avg_occupancy_NR_ego_json_15 = np.mean(r15.occupancy_NR_ego_json_15)
avg_line_NR_ego_adj_json_15 = np.mean(r15.line_NR_ego_adj_json_15)
avg_line_NR_ego_adj_txt_15 = np.mean(r15.line_NR_ego_adj_txt_15)
avg_line_NR_ego_tokenized_txt_15 = np.mean(r15.line_NR_ego_tokenized_txt_15)
avg_occupancy_NR_ego_adj_json_15 = np.mean(r15.occupancy_NR_ego_adj_json_15)
avg_occupancy_NR_ego_adj_txt_15 = np.mean(r15.occupancy_NR_ego_adj_txt_15)
avg_occupancy_NR_ego_ascii_txt_15 = np.mean(r15.occupancy_NR_ego_ascii_txt_15)
avg_occupancy_NR_ego_tokenized_txt_15 = np.mean(r15.occupancy_NR_ego_tokenized_txt_15)

avg_line_NR_ego_jpg_output_15 = np.mean(r15.line_NR_ego_jpg_output_tokens_15)
avg_line_NR_ego_json_output_15 = np.mean(r15.line_NR_ego_json_output_tokens_15)
avg_occupancy_NR_ego_jpg_output_15 = np.mean(r15.occupancy_NR_ego_jpg_output_tokens_15)
avg_occupancy_NR_ego_json_output_15 = np.mean(r15.occupancy_NR_ego_json_output_tokens_15)
avg_line_NR_ego_adj_json_output_15 = np.mean(r15.line_NR_ego_adj_json_output_tokens_15)
avg_line_NR_ego_adj_txt_output_15 = np.mean(r15.line_NR_ego_adj_txt_output_tokens_15)
avg_line_NR_ego_tokenized_txt_output_15 = np.mean(r15.line_NR_ego_tokenized_txt_output_tokens_15)
avg_occupancy_NR_ego_adj_json_output_15 = np.mean(r15.occupancy_NR_ego_adj_json_output_tokens_15)
avg_occupancy_NR_ego_adj_txt_output_15 = np.mean(r15.occupancy_NR_ego_adj_txt_output_tokens_15)
avg_occupancy_NR_ego_ascii_txt_output_15 = np.mean(r15.occupancy_NR_ego_ascii_txt_output_tokens_15)
avg_occupancy_NR_ego_tokenized_txt_output_15 = np.mean(r15.occupancy_NR_ego_tokenized_txt_output_tokens_15)


# 15x15 R - COORDS - 1-10  ----------------------------------------------------------------
avg_line_R_coords_jpg_15 = np.mean(r15.line_R_coords_jpg_15)
avg_line_R_coords_json_15 = np.mean(r15.line_R_coords_json_15)
avg_occupancy_R_coords_jpg_15 = np.mean(r15.occupancy_R_coords_jpg_15)
avg_occupancy_R_coords_json_15 = np.mean(r15.occupancy_R_coords_json_15)
avg_line_R_coords_adj_json_15 = np.mean(r15.line_R_coords_adj_json_15)
avg_line_R_coords_adj_txt_15 = np.mean(r15.line_R_coords_adj_txt_15)
avg_line_R_coords_tokenized_txt_15 = np.mean(r15.line_R_coords_tokenized_txt_15)
avg_occupancy_R_coords_adj_json_15 = np.mean(r15.occupancy_R_coords_adj_json_15)
avg_occupancy_R_coords_adj_txt_15 = np.mean(r15.occupancy_R_coords_adj_txt_15)
avg_occupancy_R_coords_ascii_txt_15 = np.mean(r15.occupancy_R_coords_ascii_txt_15)
avg_occupancy_R_coords_tokenized_txt_15 = np.mean(r15.occupancy_R_coords_tokenized_txt_15)

avg_line_R_coords_jpg_output_15 = np.mean(r15.line_R_coords_jpg_output_tokens_15)
avg_line_R_coords_json_output_15 = np.mean(r15.line_R_coords_json_output_tokens_15)
avg_occupancy_R_coords_jpg_output_15 = np.mean(r15.occupancy_R_coords_jpg_output_tokens_15)
avg_occupancy_R_coords_json_output_15 = np.mean(r15.occupancy_R_coords_json_output_tokens_15)
avg_line_R_coords_adj_json_output_15 = np.mean(r15.line_R_coords_adj_json_output_tokens_15)
avg_line_R_coords_adj_txt_output_15 = np.mean(r15.line_R_coords_adj_txt_output_tokens_15)
avg_line_R_coords_tokenized_txt_output_15 = np.mean(r15.line_R_coords_tokenized_txt_output_tokens_15)
avg_occupancy_R_coords_adj_json_output_15 = np.mean(r15.occupancy_R_coords_adj_json_output_tokens_15)
avg_occupancy_R_coords_adj_txt_output_15 = np.mean(r15.occupancy_R_coords_adj_txt_output_tokens_15)
avg_occupancy_R_coords_ascii_txt_output_15 = np.mean(r15.occupancy_R_coords_ascii_txt_output_tokens_15)
avg_occupancy_R_coords_tokenized_txt_output_15 = np.mean(r15.occupancy_R_coords_tokenized_txt_output_tokens_15)


avg_final_line_R_coords_jpg_15 = np.mean(r15.line_R_coords_jpg_final_answer_15)
avg_final_line_R_coords_json_15 = np.mean(r15.line_R_coords_json_final_answer_15)
avg_final_occupancy_R_coords_jpg_15 = np.mean(r15.occupancy_R_coords_jpg_final_answer_15)
avg_final_occupancy_R_coords_json_15 = np.mean(r15.occupancy_R_coords_json_final_answer_15)
avg_final_line_R_coords_adj_json_15 = np.mean(r15.line_R_coords_adj_json_final_answer_15)
avg_final_line_R_coords_adj_txt_15 = np.mean(r15.line_R_coords_adj_txt_final_answer_15)
avg_final_line_R_coords_tokenized_txt_15 = np.mean(r15.line_R_coords_tokenized_txt_final_answer_15)
avg_final_occupancy_R_coords_adj_json_15 = np.mean(r15.occupancy_R_coords_adj_json_final_answer_15)
avg_final_occupancy_R_coords_adj_txt_15 = np.mean(r15.occupancy_R_coords_adj_txt_final_answer_15)
avg_final_occupancy_R_coords_ascii_txt_15 = np.mean(r15.occupancy_R_coords_ascii_txt_final_answer_15)
avg_final_occupancy_R_coords_tokenized_txt_15 = np.mean(r15.occupancy_R_coords_tokenized_txt_final_answer_15)

# 15x15 R - ALLO - 1-10 ----------------------------------------------------------------
avg_line_R_allo_jpg_15 = np.mean(r15.line_R_allo_jpg_15)
avg_line_R_allo_json_15 = np.mean(r15.line_R_allo_json_15)
avg_occupancy_R_allo_jpg_15 = np.mean(r15.occupancy_R_allo_jpg_15)
avg_occupancy_R_allo_json_15 = np.mean(r15.occupancy_R_allo_json_15)
avg_line_R_allo_adj_json_15 = np.mean(r15.line_R_allo_adj_json_15)
avg_line_R_allo_adj_txt_15 = np.mean(r15.line_R_allo_adj_txt_15)
avg_line_R_allo_tokenized_txt_15 = np.mean(r15.line_R_allo_tokenized_txt_15)
avg_occupancy_R_allo_adj_json_15 = np.mean(r15.occupancy_R_allo_adj_json_15)
avg_occupancy_R_allo_adj_txt_15 = np.mean(r15.occupancy_R_allo_adj_txt_15)
avg_occupancy_R_allo_ascii_txt_15 = np.mean(r15.occupancy_R_allo_ascii_txt_15)
avg_occupancy_R_allo_tokenized_txt_15 = np.mean(r15.occupancy_R_allo_tokenized_txt_15)

avg_line_R_allo_jpg_output_15 = np.mean(r15.line_R_allo_jpg_output_tokens_15)
avg_line_R_allo_json_output_15 = np.mean(r15.line_R_allo_json_output_tokens_15)
avg_occupancy_R_allo_jpg_output_15 = np.mean(r15.occupancy_R_allo_jpg_output_tokens_15)
avg_occupancy_R_allo_json_output_15 = np.mean(r15.occupancy_R_allo_json_output_tokens_15)
avg_line_R_allo_adj_json_output_15 = np.mean(r15.line_R_allo_adj_json_output_tokens_15)
avg_line_R_allo_adj_txt_output_15 = np.mean(r15.line_R_allo_adj_txt_output_tokens_15)
avg_line_R_allo_tokenized_txt_output_15 = np.mean(r15.line_R_allo_tokenized_txt_output_tokens_15)
avg_occupancy_R_allo_adj_json_output_15 = np.mean(r15.occupancy_R_allo_adj_json_output_tokens_15)
avg_occupancy_R_allo_adj_txt_output_15 = np.mean(r15.occupancy_R_allo_adj_txt_output_tokens_15)
avg_occupancy_R_allo_ascii_txt_output_15 = np.mean(r15.occupancy_R_allo_ascii_txt_output_tokens_15)
avg_occupancy_R_allo_tokenized_txt_output_15 = np.mean(r15.occupancy_R_allo_tokenized_txt_output_tokens_15)


avg_final_line_R_allo_jpg_15 = np.mean(r15.line_R_allo_jpg_final_answer_15)
avg_final_line_R_allo_json_15 = np.mean(r15.line_R_allo_json_final_answer_15)
avg_final_occupancy_R_allo_jpg_15 = np.mean(r15.occupancy_R_allo_jpg_final_answer_15)
avg_final_occupancy_R_allo_json_15 = np.mean(r15.occupancy_R_allo_json_final_answer_15)
avg_final_line_R_allo_adj_json_15 = np.mean(r15.line_R_allo_adj_json_final_answer_15)
avg_final_line_R_allo_adj_txt_15 = np.mean(r15.line_R_allo_adj_txt_final_answer_15)
avg_final_line_R_allo_tokenized_txt_15 = np.mean(r15.line_R_allo_tokenized_txt_final_answer_15)
avg_final_occupancy_R_allo_adj_json_15 = np.mean(r15.occupancy_R_allo_adj_json_final_answer_15)
avg_final_occupancy_R_allo_adj_txt_15 = np.mean(r15.occupancy_R_allo_adj_txt_final_answer_15)
avg_final_occupancy_R_allo_ascii_txt_15 = np.mean(r15.occupancy_R_allo_ascii_txt_final_answer_15)
avg_final_occupancy_R_allo_tokenized_txt_15 = np.mean(r15.occupancy_R_allo_tokenized_txt_final_answer_15)

# 15x15 R - EGO - 1-10 ----------------------------------------------------------------
avg_line_R_ego_jpg_15 = np.mean(r15.line_R_ego_jpg_15)
avg_line_R_ego_json_15 = np.mean(r15.line_R_ego_json_15)
avg_occupancy_R_ego_jpg_15 = np.mean(r15.occupancy_R_ego_jpg_15)
avg_occupancy_R_ego_json_15 = np.mean(r15.occupancy_R_ego_json_15)
avg_line_R_ego_adj_json_15 = np.mean(r15.line_R_ego_adj_json_15)
avg_line_R_ego_adj_txt_15 = np.mean(r15.line_R_ego_adj_txt_15)
avg_line_R_ego_tokenized_txt_15 = np.mean(r15.line_R_ego_tokenized_txt_15)
avg_occupancy_R_ego_adj_json_15 = np.mean(r15.occupancy_R_ego_adj_json_15)
avg_occupancy_R_ego_adj_txt_15 = np.mean(r15.occupancy_R_ego_adj_txt_15)
avg_occupancy_R_ego_ascii_txt_15 = np.mean(r15.occupancy_R_ego_ascii_txt_15)
avg_occupancy_R_ego_tokenized_txt_15 = np.mean(r15.occupancy_R_ego_tokenized_txt_15)

avg_line_R_ego_jpg_output_15 = np.mean(r15.line_R_ego_jpg_output_tokens_15)
avg_line_R_ego_json_output_15 = np.mean(r15.line_R_ego_json_output_tokens_15)
avg_occupancy_R_ego_jpg_output_15 = np.mean(r15.occupancy_R_ego_jpg_output_tokens_15)
avg_occupancy_R_ego_json_output_15 = np.mean(r15.occupancy_R_ego_json_output_tokens_15)
avg_line_R_ego_adj_json_output_15 = np.mean(r15.line_R_ego_adj_json_output_tokens_15)
avg_line_R_ego_adj_txt_output_15 = np.mean(r15.line_R_ego_adj_txt_output_tokens_15)
avg_line_R_ego_tokenized_txt_output_15 = np.mean(r15.line_R_ego_tokenized_txt_output_tokens_15)
avg_occupancy_R_ego_adj_json_output_15 = np.mean(r15.occupancy_R_ego_adj_json_output_tokens_15)
avg_occupancy_R_ego_adj_txt_output_15 = np.mean(r15.occupancy_R_ego_adj_txt_output_tokens_15)
avg_occupancy_R_ego_ascii_txt_output_15 = np.mean(r15.occupancy_R_ego_ascii_txt_output_tokens_15)
avg_occupancy_R_ego_tokenized_txt_output_15 = np.mean(r15.occupancy_R_ego_tokenized_txt_output_tokens_15)


avg_final_line_R_ego_jpg_15 = np.mean(r15.line_R_ego_jpg_final_answer_15)
avg_final_line_R_ego_json_15 = np.mean(r15.line_R_ego_json_final_answer_15)
avg_final_occupancy_R_ego_jpg_15 = np.mean(r15.occupancy_R_ego_jpg_final_answer_15)
avg_final_occupancy_R_ego_json_15 = np.mean(r15.occupancy_R_ego_json_final_answer_15)
avg_final_line_R_ego_adj_json_15 = np.mean(r15.line_R_ego_adj_json_final_answer_15)
avg_final_line_R_ego_adj_txt_15 = np.mean(r15.line_R_ego_adj_txt_final_answer_15)
avg_final_line_R_ego_tokenized_txt_15 = np.mean(r15.line_R_ego_tokenized_txt_final_answer_15)
avg_final_occupancy_R_ego_adj_json_15 = np.mean(r15.occupancy_R_ego_adj_json_final_answer_15)
avg_final_occupancy_R_ego_adj_txt_15 = np.mean(r15.occupancy_R_ego_adj_txt_final_answer_15)
avg_final_occupancy_R_ego_ascii_txt_15 = np.mean(r15.occupancy_R_ego_ascii_txt_final_answer_15)
avg_final_occupancy_R_ego_tokenized_txt_15 = np.mean(r15.occupancy_R_ego_tokenized_txt_final_answer_15)

# Creating an acc vs token output plot ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Creating data for plotting - using  ALL OUTPUT TOKENS (INCL. THINKING)
figure = 'all_tokens'  # this is for setting the correct title and axis labels
line_NR_coords_3 = [[avg_line_NR_coords_adj_json_output_3,      avg_line_NR_coords_adj_json_3],
                   [avg_line_NR_coords_adj_txt_output_3,        avg_line_NR_coords_adj_txt_3],
                   [avg_line_NR_coords_jpg_output_3,            avg_line_NR_coords_jpg_3],
                   [avg_line_NR_coords_json_output_3,           avg_line_NR_coords_json_3],
                   [avg_line_NR_coords_tokenized_txt_output_3,  avg_line_NR_coords_tokenized_txt_3]
                   ]

occupancy_NR_coords_3 = [[avg_occupancy_NR_coords_adj_json_output_3,    avg_occupancy_NR_coords_adj_json_3],
                         [avg_occupancy_NR_coords_adj_txt_output_3,           avg_occupancy_NR_coords_adj_txt_3],
                         [avg_occupancy_NR_coords_jpg_output_3,               avg_occupancy_NR_coords_jpg_3],
                         [avg_occupancy_NR_coords_json_output_3,              avg_occupancy_NR_coords_json_3],
                         [avg_occupancy_NR_coords_tokenized_txt_output_3,     avg_occupancy_NR_coords_tokenized_txt_3],
                         [avg_occupancy_NR_coords_ascii_txt_output_3,        avg_occupancy_NR_coords_ascii_txt_3]
                         ]


line_R_coords_3 = [[avg_line_R_coords_adj_json_output_3,        avg_line_R_coords_adj_json_3],
                   [avg_line_R_coords_adj_txt_output_3,         avg_line_R_coords_adj_txt_3],
                   [avg_line_R_coords_jpg_output_3,             avg_line_R_coords_jpg_3],
                   [avg_line_R_coords_json_output_3,            avg_line_R_coords_json_3],
                   [avg_line_R_coords_tokenized_txt_output_3,   avg_line_R_coords_tokenized_txt_3]
                   ]

occupancy_R_coords_3 = [[avg_occupancy_R_coords_adj_json_output_3,      avg_occupancy_R_coords_adj_json_3],
                        [avg_occupancy_R_coords_adj_txt_output_3,            avg_occupancy_R_coords_adj_txt_3],
                        [avg_occupancy_R_coords_jpg_output_3,                avg_occupancy_R_coords_jpg_3],
                        [avg_occupancy_R_coords_json_output_3,               avg_occupancy_R_coords_json_3],
                        [avg_occupancy_R_coords_tokenized_txt_output_3,      avg_occupancy_R_coords_tokenized_txt_3],
                        [avg_occupancy_R_coords_ascii_txt_output_3,         avg_occupancy_R_coords_ascii_txt_3]
                        ]
                    
line_NR_allo_3 = [[avg_line_NR_allo_adj_json_output_3,      avg_line_NR_allo_adj_json_3],
                  [avg_line_NR_allo_adj_txt_output_3,        avg_line_NR_allo_adj_txt_3],
                  [avg_line_NR_allo_jpg_output_3,            avg_line_NR_allo_jpg_3],
                  [avg_line_NR_allo_json_output_3,           avg_line_NR_allo_json_3],
                  [avg_line_NR_allo_tokenized_txt_output_3,  avg_line_NR_allo_tokenized_txt_3]
                  ]

occupancy_NR_allo_3 = [[avg_occupancy_NR_allo_adj_json_output_3,    avg_occupancy_NR_allo_adj_json_3],
                       [avg_occupancy_NR_allo_adj_txt_output_3,           avg_occupancy_NR_allo_adj_txt_3],
                       [avg_occupancy_NR_allo_jpg_output_3,               avg_occupancy_NR_allo_jpg_3],
                       [avg_occupancy_NR_allo_json_output_3,              avg_occupancy_NR_allo_json_3],
                       [avg_occupancy_NR_allo_tokenized_txt_output_3,     avg_occupancy_NR_allo_tokenized_txt_3],
                       [avg_occupancy_NR_allo_ascii_txt_output_3,        avg_occupancy_NR_allo_ascii_txt_3]
                       ]


line_R_allo_3 = [[avg_line_R_allo_adj_json_output_3,        avg_line_R_allo_adj_json_3],
                [avg_line_R_allo_adj_txt_output_3,         avg_line_R_allo_adj_txt_3],
                [avg_line_R_allo_jpg_output_3,             avg_line_R_allo_jpg_3],
                [avg_line_R_allo_json_output_3,            avg_line_R_allo_json_3],
                [avg_line_R_allo_tokenized_txt_output_3,   avg_line_R_allo_tokenized_txt_3]
                ]

occupancy_R_allo_3 = [[avg_occupancy_R_allo_adj_json_output_3,          avg_occupancy_R_allo_adj_json_3],
                      [avg_occupancy_R_allo_adj_txt_output_3,           avg_occupancy_R_allo_adj_txt_3],
                      [avg_occupancy_R_allo_jpg_output_3,               avg_occupancy_R_allo_jpg_3],
                      [avg_occupancy_R_allo_json_output_3,              avg_occupancy_R_allo_json_3],
                      [avg_occupancy_R_allo_tokenized_txt_output_3,     avg_occupancy_R_allo_tokenized_txt_3],
                      [avg_occupancy_R_allo_ascii_txt_output_3,         avg_occupancy_R_allo_ascii_txt_3]
                      ]
                    
line_NR_ego_3 = [[avg_line_NR_ego_adj_json_output_3,      avg_line_NR_ego_adj_json_3],
                [avg_line_NR_ego_adj_txt_output_3,        avg_line_NR_ego_adj_txt_3],
                [avg_line_NR_ego_jpg_output_3,            avg_line_NR_ego_jpg_3],
                [avg_line_NR_ego_json_output_3,           avg_line_NR_ego_json_3],
                [avg_line_NR_ego_tokenized_txt_output_3,  avg_line_NR_ego_tokenized_txt_3]
                ]

occupancy_NR_ego_3 = [[avg_occupancy_NR_ego_adj_json_output_3,          avg_occupancy_NR_ego_adj_json_3],
                      [avg_occupancy_NR_ego_adj_txt_output_3,           avg_occupancy_NR_ego_adj_txt_3],
                      [avg_occupancy_NR_ego_jpg_output_3,               avg_occupancy_NR_ego_jpg_3],
                      [avg_occupancy_NR_ego_json_output_3,              avg_occupancy_NR_ego_json_3],
                      [avg_occupancy_NR_ego_tokenized_txt_output_3,     avg_occupancy_NR_ego_tokenized_txt_3],
                      [avg_occupancy_NR_ego_ascii_txt_output_3,         avg_occupancy_NR_ego_ascii_txt_3]
                      ]


line_R_ego_3 = [[avg_line_R_ego_adj_json_output_3,        avg_line_R_ego_adj_json_3],
                [avg_line_R_ego_adj_txt_output_3,         avg_line_R_ego_adj_txt_3],
                [avg_line_R_ego_jpg_output_3,             avg_line_R_ego_jpg_3],
                [avg_line_R_ego_json_output_3,            avg_line_R_ego_json_3],
                [avg_line_R_ego_tokenized_txt_output_3,   avg_line_R_ego_tokenized_txt_3]
                ]

occupancy_R_ego_3 = [[avg_occupancy_R_ego_adj_json_output_3,      avg_occupancy_R_ego_adj_json_3],
                     [avg_occupancy_R_ego_adj_txt_output_3,            avg_occupancy_R_ego_adj_txt_3],
                     [avg_occupancy_R_ego_jpg_output_3,                avg_occupancy_R_ego_jpg_3],
                     [avg_occupancy_R_ego_json_output_3,               avg_occupancy_R_ego_json_3],
                     [avg_occupancy_R_ego_tokenized_txt_output_3,      avg_occupancy_R_ego_tokenized_txt_3],
                     [avg_occupancy_R_ego_ascii_txt_output_3,          avg_occupancy_R_ego_ascii_txt_3]
                     ]
                    


line_NR_coords_6 = [[avg_line_NR_coords_adj_json_output_6,      avg_line_NR_coords_adj_json_6],
                   [avg_line_NR_coords_adj_txt_output_6,        avg_line_NR_coords_adj_txt_6],
                   [avg_line_NR_coords_jpg_output_6,            avg_line_NR_coords_jpg_6],
                   [avg_line_NR_coords_json_output_6,           avg_line_NR_coords_json_6],
                   [avg_line_NR_coords_tokenized_txt_output_6,  avg_line_NR_coords_tokenized_txt_6]
                   ]

occupancy_NR_coords_6 = [[avg_occupancy_NR_coords_adj_json_output_6,    avg_occupancy_NR_coords_adj_json_6],
                         [avg_occupancy_NR_coords_adj_txt_output_6,           avg_occupancy_NR_coords_adj_txt_6],
                         [avg_occupancy_NR_coords_jpg_output_6,               avg_occupancy_NR_coords_jpg_6],
                         [avg_occupancy_NR_coords_json_output_6,              avg_occupancy_NR_coords_json_6],
                         [avg_occupancy_NR_coords_tokenized_txt_output_6,     avg_occupancy_NR_coords_tokenized_txt_6],
                         [avg_occupancy_NR_coords_ascii_txt_output_6,         avg_occupancy_NR_coords_ascii_txt_6]
                         ]


line_R_coords_6 = [[avg_line_R_coords_adj_json_output_6,        avg_line_R_coords_adj_json_6],
                   [avg_line_R_coords_adj_txt_output_6,         avg_line_R_coords_adj_txt_6],
                   [avg_line_R_coords_jpg_output_6,             avg_line_R_coords_jpg_6],
                   [avg_line_R_coords_json_output_6,            avg_line_R_coords_json_6],
                   [avg_line_R_coords_tokenized_txt_output_6,   avg_line_R_coords_tokenized_txt_6]
                   ]

occupancy_R_coords_6 = [[avg_occupancy_R_coords_adj_json_output_6,      avg_occupancy_R_coords_adj_json_6],
                        [avg_occupancy_R_coords_adj_txt_output_6,            avg_occupancy_R_coords_adj_txt_6],
                        [avg_occupancy_R_coords_jpg_output_6,                avg_occupancy_R_coords_jpg_6],
                        [avg_occupancy_R_coords_json_output_6,               avg_occupancy_R_coords_json_6],
                        [avg_occupancy_R_coords_tokenized_txt_output_6,      avg_occupancy_R_coords_tokenized_txt_6],
                        [avg_occupancy_R_coords_ascii_txt_output_6,         avg_occupancy_R_coords_ascii_txt_6]
                        ]
                    
line_NR_allo_6 = [[avg_line_NR_allo_adj_json_output_6,      avg_line_NR_allo_adj_json_6],
                  [avg_line_NR_allo_adj_txt_output_6,        avg_line_NR_allo_adj_txt_6],
                  [avg_line_NR_allo_jpg_output_6,            avg_line_NR_allo_jpg_6],
                  [avg_line_NR_allo_json_output_6,           avg_line_NR_allo_json_6],
                  [avg_line_NR_allo_tokenized_txt_output_6,  avg_line_NR_allo_tokenized_txt_6]
                  ]

occupancy_NR_allo_6 = [[avg_occupancy_NR_allo_adj_json_output_6,    avg_occupancy_NR_allo_adj_json_6],
                       [avg_occupancy_NR_allo_adj_txt_output_6,           avg_occupancy_NR_allo_adj_txt_6],
                       [avg_occupancy_NR_allo_jpg_output_6,               avg_occupancy_NR_allo_jpg_6],
                       [avg_occupancy_NR_allo_json_output_6,              avg_occupancy_NR_allo_json_6],
                       [avg_occupancy_NR_allo_tokenized_txt_output_6,     avg_occupancy_NR_allo_tokenized_txt_6],
                       [avg_occupancy_NR_allo_ascii_txt_output_6,        avg_occupancy_NR_allo_ascii_txt_6]   
                       ]


line_R_allo_6 = [[avg_line_R_allo_adj_json_output_6,        avg_line_R_allo_adj_json_6],
                [avg_line_R_allo_adj_txt_output_6,         avg_line_R_allo_adj_txt_6],
                [avg_line_R_allo_jpg_output_6,             avg_line_R_allo_jpg_6],
                [avg_line_R_allo_json_output_6,            avg_line_R_allo_json_6],
                [avg_line_R_allo_tokenized_txt_output_6,   avg_line_R_allo_tokenized_txt_6]
                ]

occupancy_R_allo_6 = [[avg_occupancy_R_allo_adj_json_output_6,      avg_occupancy_R_allo_adj_json_6],
                      [avg_occupancy_R_allo_adj_txt_output_6,            avg_occupancy_R_allo_adj_txt_6],
                      [avg_occupancy_R_allo_jpg_output_6,                avg_occupancy_R_allo_jpg_6],
                      [avg_occupancy_R_allo_json_output_6,               avg_occupancy_R_allo_json_6],
                      [avg_occupancy_R_allo_tokenized_txt_output_6,      avg_occupancy_R_allo_tokenized_txt_6],
                      [avg_occupancy_R_allo_ascii_txt_output_6,          avg_occupancy_R_allo_ascii_txt_6]
                      ]
                    
line_NR_ego_6 = [[avg_line_NR_ego_adj_json_output_6,      avg_line_NR_ego_adj_json_6],
                [avg_line_NR_ego_adj_txt_output_6,        avg_line_NR_ego_adj_txt_6],
                [avg_line_NR_ego_jpg_output_6,            avg_line_NR_ego_jpg_6],
                [avg_line_NR_ego_json_output_6,           avg_line_NR_ego_json_6],
                [avg_line_NR_ego_tokenized_txt_output_6,  avg_line_NR_ego_tokenized_txt_6]
                ]

occupancy_NR_ego_6 = [[avg_occupancy_NR_ego_adj_json_output_6,    avg_occupancy_NR_ego_adj_json_6],
                      [avg_occupancy_NR_ego_adj_txt_output_6,           avg_occupancy_NR_ego_adj_txt_6],
                      [avg_occupancy_NR_ego_jpg_output_6,               avg_occupancy_NR_ego_jpg_6],
                      [avg_occupancy_NR_ego_json_output_6,              avg_occupancy_NR_ego_json_6],
                      [avg_occupancy_NR_ego_tokenized_txt_output_6,     avg_occupancy_NR_ego_tokenized_txt_6],
                        [avg_occupancy_NR_ego_ascii_txt_output_6,         avg_occupancy_NR_ego_ascii_txt_6]
                      ]


line_R_ego_6 = [[avg_line_R_ego_adj_json_output_6,        avg_line_R_ego_adj_json_6],
                [avg_line_R_ego_adj_txt_output_6,         avg_line_R_ego_adj_txt_6],
                [avg_line_R_ego_jpg_output_6,             avg_line_R_ego_jpg_6],
                [avg_line_R_ego_json_output_6,            avg_line_R_ego_json_6],
                [avg_line_R_ego_tokenized_txt_output_6,   avg_line_R_ego_tokenized_txt_6]
                ]

occupancy_R_ego_6 = [[avg_occupancy_R_ego_adj_json_output_6,      avg_occupancy_R_ego_adj_json_6],
                     [avg_occupancy_R_ego_adj_txt_output_6,            avg_occupancy_R_ego_adj_txt_6],
                     [avg_occupancy_R_ego_jpg_output_6,                avg_occupancy_R_ego_jpg_6],
                     [avg_occupancy_R_ego_json_output_6,               avg_occupancy_R_ego_json_6],
                     [avg_occupancy_R_ego_tokenized_txt_output_6,      avg_occupancy_R_ego_tokenized_txt_6],
                    [avg_occupancy_R_ego_ascii_txt_output_6,          avg_occupancy_R_ego_ascii_txt_6]
                     ]
                    



line_NR_coords_15 = [[avg_line_NR_coords_adj_json_output_15,      avg_line_NR_coords_adj_json_15],
                   [avg_line_NR_coords_adj_txt_output_15,        avg_line_NR_coords_adj_txt_15],
                   [avg_line_NR_coords_jpg_output_15,            avg_line_NR_coords_jpg_15],
                   [avg_line_NR_coords_json_output_15,           avg_line_NR_coords_json_15],
                   [avg_line_NR_coords_tokenized_txt_output_15,  avg_line_NR_coords_tokenized_txt_15]
                   ]

occupancy_NR_coords_15 = [[avg_occupancy_NR_coords_adj_json_output_15,    avg_occupancy_NR_coords_adj_json_15],
                         [avg_occupancy_NR_coords_adj_txt_output_15,           avg_occupancy_NR_coords_adj_txt_15],
                         [avg_occupancy_NR_coords_jpg_output_15,               avg_occupancy_NR_coords_jpg_15],
                         [avg_occupancy_NR_coords_json_output_15,              avg_occupancy_NR_coords_json_15],
                         [avg_occupancy_NR_coords_tokenized_txt_output_15,     avg_occupancy_NR_coords_tokenized_txt_15],
                        [avg_occupancy_NR_coords_ascii_txt_output_15,         avg_occupancy_NR_coords_ascii_txt_15]
                         ]


line_R_coords_15 = [[avg_line_R_coords_adj_json_output_15,        avg_line_R_coords_adj_json_15],
                   [avg_line_R_coords_adj_txt_output_15,         avg_line_R_coords_adj_txt_15],
                   [avg_line_R_coords_jpg_output_15,             avg_line_R_coords_jpg_15],
                   [avg_line_R_coords_json_output_15,            avg_line_R_coords_json_15],
                   [avg_line_R_coords_tokenized_txt_output_15,   avg_line_R_coords_tokenized_txt_15]
                   ]

occupancy_R_coords_15 = [[avg_occupancy_R_coords_adj_json_output_15,      avg_occupancy_R_coords_adj_json_15],
                        [avg_occupancy_R_coords_adj_txt_output_15,            avg_occupancy_R_coords_adj_txt_15],
                        [avg_occupancy_R_coords_jpg_output_15,                avg_occupancy_R_coords_jpg_15],
                        [avg_occupancy_R_coords_json_output_15,               avg_occupancy_R_coords_json_15],
                        [avg_occupancy_R_coords_tokenized_txt_output_15,      avg_occupancy_R_coords_tokenized_txt_15],
                        [avg_occupancy_R_coords_ascii_txt_output_15,         avg_occupancy_R_coords_ascii_txt_15]
                        ]
                    
line_NR_allo_15 = [[avg_line_NR_allo_adj_json_output_15,      avg_line_NR_allo_adj_json_15],
                  [avg_line_NR_allo_adj_txt_output_15,        avg_line_NR_allo_adj_txt_15],
                  [avg_line_NR_allo_jpg_output_15,            avg_line_NR_allo_jpg_15],
                  [avg_line_NR_allo_json_output_15,           avg_line_NR_allo_json_15],
                  [avg_line_NR_allo_tokenized_txt_output_15,  avg_line_NR_allo_tokenized_txt_15]
                  ]

occupancy_NR_allo_15 = [[avg_occupancy_NR_allo_adj_json_output_15,    avg_occupancy_NR_allo_adj_json_15],
                       [avg_occupancy_NR_allo_adj_txt_output_15,           avg_occupancy_NR_allo_adj_txt_15],
                       [avg_occupancy_NR_allo_jpg_output_15,               avg_occupancy_NR_allo_jpg_15],
                       [avg_occupancy_NR_allo_json_output_15,              avg_occupancy_NR_allo_json_15],
                       [avg_occupancy_NR_allo_tokenized_txt_output_15,     avg_occupancy_NR_allo_tokenized_txt_15],
                        [avg_occupancy_NR_allo_ascii_txt_output_15,        avg_occupancy_NR_allo_ascii_txt_15]
                       ]


line_R_allo_15 = [[avg_line_R_allo_adj_json_output_15,        avg_line_R_allo_adj_json_15],
                [avg_line_R_allo_adj_txt_output_15,         avg_line_R_allo_adj_txt_15],
                [avg_line_R_allo_jpg_output_15,             avg_line_R_allo_jpg_15],
                [avg_line_R_allo_json_output_15,            avg_line_R_allo_json_15],
                [avg_line_R_allo_tokenized_txt_output_15,   avg_line_R_allo_tokenized_txt_15]
                ]

occupancy_R_allo_15 = [[avg_occupancy_R_allo_adj_json_output_15,      avg_occupancy_R_allo_adj_json_15],
                      [avg_occupancy_R_allo_adj_txt_output_15,            avg_occupancy_R_allo_adj_txt_15],
                      [avg_occupancy_R_allo_jpg_output_15,                avg_occupancy_R_allo_jpg_15],
                      [avg_occupancy_R_allo_json_output_15,               avg_occupancy_R_allo_json_15],
                      [avg_occupancy_R_allo_tokenized_txt_output_15,      avg_occupancy_R_allo_tokenized_txt_15],
                    [avg_occupancy_R_allo_ascii_txt_output_15,          avg_occupancy_R_allo_ascii_txt_15]
                      ]
                    
line_NR_ego_15 = [[avg_line_NR_ego_adj_json_output_15,      avg_line_NR_ego_adj_json_15],
                [avg_line_NR_ego_adj_txt_output_15,        avg_line_NR_ego_adj_txt_15],
                [avg_line_NR_ego_jpg_output_15,            avg_line_NR_ego_jpg_15],
                [avg_line_NR_ego_json_output_15,           avg_line_NR_ego_json_15],
                [avg_line_NR_ego_tokenized_txt_output_15,  avg_line_NR_ego_tokenized_txt_15]
                ]

occupancy_NR_ego_15 = [[avg_occupancy_NR_ego_adj_json_output_15,    avg_occupancy_NR_ego_adj_json_15],
                      [avg_occupancy_NR_ego_adj_txt_output_15,           avg_occupancy_NR_ego_adj_txt_15],
                      [avg_occupancy_NR_ego_jpg_output_15,               avg_occupancy_NR_ego_jpg_15],
                      [avg_occupancy_NR_ego_json_output_15,              avg_occupancy_NR_ego_json_15],
                      [avg_occupancy_NR_ego_tokenized_txt_output_15,     avg_occupancy_NR_ego_tokenized_txt_15],
                    [avg_occupancy_NR_ego_ascii_txt_output_15,         avg_occupancy_NR_ego_ascii_txt_15]
                      ]


line_R_ego_15 = [[avg_line_R_ego_adj_json_output_15,        avg_line_R_ego_adj_json_15],
                [avg_line_R_ego_adj_txt_output_15,         avg_line_R_ego_adj_txt_15],
                [avg_line_R_ego_jpg_output_15,             avg_line_R_ego_jpg_15],
                [avg_line_R_ego_json_output_15,            avg_line_R_ego_json_15],
                [avg_line_R_ego_tokenized_txt_output_15,   avg_line_R_ego_tokenized_txt_15]
                ]

occupancy_R_ego_15 = [[avg_occupancy_R_ego_adj_json_output_15,      avg_occupancy_R_ego_adj_json_15],
                     [avg_occupancy_R_ego_adj_txt_output_15,            avg_occupancy_R_ego_adj_txt_15],
                     [avg_occupancy_R_ego_jpg_output_15,                avg_occupancy_R_ego_jpg_15],
                     [avg_occupancy_R_ego_json_output_15,               avg_occupancy_R_ego_json_15],
                     [avg_occupancy_R_ego_tokenized_txt_output_15,      avg_occupancy_R_ego_tokenized_txt_15],
                    [avg_occupancy_R_ego_ascii_txt_output_15,          avg_occupancy_R_ego_ascii_txt_15]
                     ]


# Creating data for plotting - using FINAL ANSWER TOKENS (EXCL. THINKING)
# figure = 'final_answer_tokens' # this is for choosing the correct title and axis labels
# line_NR_coords_3 = [[avg_line_NR_coords_adj_json_output_3,      avg_line_NR_coords_adj_json_3],
#                    [avg_line_NR_coords_adj_txt_output_3,        avg_line_NR_coords_adj_txt_3],
#                    [avg_line_NR_coords_jpg_output_3,            avg_line_NR_coords_jpg_3],
#                    [avg_line_NR_coords_json_output_3,           avg_line_NR_coords_json_3],
#                    [avg_line_NR_coords_tokenized_txt_output_3,  avg_line_NR_coords_tokenized_txt_3]
#                    ]

# occupancy_NR_coords_3 = [[avg_occupancy_NR_coords_adj_json_output_3,    avg_occupancy_NR_coords_adj_json_3],
#                          [avg_occupancy_NR_coords_adj_txt_output_3,           avg_occupancy_NR_coords_adj_txt_3],
#                          [avg_occupancy_NR_coords_jpg_output_3,               avg_occupancy_NR_coords_jpg_3],
#                          [avg_occupancy_NR_coords_json_output_3,              avg_occupancy_NR_coords_json_3],
#                          [avg_occupancy_NR_coords_tokenized_txt_output_3,     avg_occupancy_NR_coords_tokenized_txt_3],
#                          [avg_occupancy_NR_coords_ascii_txt_output_3,        avg_occupancy_NR_coords_ascii_txt_3]
#                          ]


# line_R_coords_3 = [[avg_final_line_R_coords_adj_json_3,        avg_line_R_coords_adj_json_3],
#                    [avg_final_line_R_coords_adj_txt_3,         avg_line_R_coords_adj_txt_3],
#                    [avg_final_line_R_coords_jpg_3,             avg_line_R_coords_jpg_3],
#                    [avg_final_line_R_coords_json_3,            avg_line_R_coords_json_3],
#                    [avg_final_line_R_coords_tokenized_txt_3,   avg_line_R_coords_tokenized_txt_3]
#                    ]

# occupancy_R_coords_3 = [[avg_final_occupancy_R_coords_adj_json_3,      avg_occupancy_R_coords_adj_json_3],
#                         [avg_final_occupancy_R_coords_adj_txt_3,            avg_occupancy_R_coords_adj_txt_3],
#                         [avg_final_occupancy_R_coords_jpg_3,                avg_occupancy_R_coords_jpg_3],
#                         [avg_final_occupancy_R_coords_json_3,               avg_occupancy_R_coords_json_3],
#                         [avg_final_occupancy_R_coords_tokenized_txt_3,      avg_occupancy_R_coords_tokenized_txt_3],
#                         [avg_final_occupancy_R_coords_ascii_txt_3,         avg_occupancy_R_coords_ascii_txt_3]
#                         ]
                    
# line_NR_allo_3 = [[avg_line_NR_allo_adj_json_output_3,      avg_line_NR_allo_adj_json_3],
#                   [avg_line_NR_allo_adj_txt_output_3,        avg_line_NR_allo_adj_txt_3],
#                   [avg_line_NR_allo_jpg_output_3,            avg_line_NR_allo_jpg_3],
#                   [avg_line_NR_allo_json_output_3,           avg_line_NR_allo_json_3],
#                   [avg_line_NR_allo_tokenized_txt_output_3,  avg_line_NR_allo_tokenized_txt_3]
#                   ]

# occupancy_NR_allo_3 = [[avg_occupancy_NR_allo_adj_json_output_3,    avg_occupancy_NR_allo_adj_json_3],
#                        [avg_occupancy_NR_allo_adj_txt_output_3,           avg_occupancy_NR_allo_adj_txt_3],
#                        [avg_occupancy_NR_allo_jpg_output_3,               avg_occupancy_NR_allo_jpg_3],
#                        [avg_occupancy_NR_allo_json_output_3,              avg_occupancy_NR_allo_json_3],
#                        [avg_occupancy_NR_allo_tokenized_txt_output_3,     avg_occupancy_NR_allo_tokenized_txt_3],
#                        [avg_occupancy_NR_allo_ascii_txt_output_3,        avg_occupancy_NR_allo_ascii_txt_3]
#                        ]


# line_R_allo_3 = [[avg_final_line_R_allo_adj_json_3,        avg_line_R_allo_adj_json_3],
#                 [avg_final_line_R_allo_adj_txt_3,         avg_line_R_allo_adj_txt_3],
#                 [avg_final_line_R_allo_jpg_3,             avg_line_R_allo_jpg_3],
#                 [avg_final_line_R_allo_json_3,            avg_line_R_allo_json_3],
#                 [avg_final_line_R_allo_tokenized_txt_3,   avg_line_R_allo_tokenized_txt_3]
#                 ]

# occupancy_R_allo_3 = [[avg_final_occupancy_R_allo_adj_json_3,          avg_occupancy_R_allo_adj_json_3],
#                       [avg_final_occupancy_R_allo_adj_txt_3,           avg_occupancy_R_allo_adj_txt_3],
#                       [avg_final_occupancy_R_allo_jpg_3,               avg_occupancy_R_allo_jpg_3],
#                       [avg_final_occupancy_R_allo_json_3,              avg_occupancy_R_allo_json_3],
#                       [avg_final_occupancy_R_allo_tokenized_txt_3,     avg_occupancy_R_allo_tokenized_txt_3],
#                       [avg_final_occupancy_R_allo_ascii_txt_3,         avg_occupancy_R_allo_ascii_txt_3]
#                       ]
                    
# line_NR_ego_3 = [[avg_line_NR_ego_adj_json_output_3,      avg_line_NR_ego_adj_json_3],
#                 [avg_line_NR_ego_adj_txt_output_3,        avg_line_NR_ego_adj_txt_3],
#                 [avg_line_NR_ego_jpg_output_3,            avg_line_NR_ego_jpg_3],
#                 [avg_line_NR_ego_json_output_3,           avg_line_NR_ego_json_3],
#                 [avg_line_NR_ego_tokenized_txt_output_3,  avg_line_NR_ego_tokenized_txt_3]
#                 ]

# occupancy_NR_ego_3 = [[avg_occupancy_NR_ego_adj_json_output_3,          avg_occupancy_NR_ego_adj_json_3],
#                       [avg_occupancy_NR_ego_adj_txt_output_3,           avg_occupancy_NR_ego_adj_txt_3],
#                       [avg_occupancy_NR_ego_jpg_output_3,               avg_occupancy_NR_ego_jpg_3],
#                       [avg_occupancy_NR_ego_json_output_3,              avg_occupancy_NR_ego_json_3],
#                       [avg_occupancy_NR_ego_tokenized_txt_output_3,     avg_occupancy_NR_ego_tokenized_txt_3],
#                       [avg_occupancy_NR_ego_ascii_txt_output_3,         avg_occupancy_NR_ego_ascii_txt_3]
#                       ]


# line_R_ego_3 = [[avg_final_line_R_ego_adj_json_3,        avg_line_R_ego_adj_json_3],
#                 [avg_final_line_R_ego_adj_txt_3,         avg_line_R_ego_adj_txt_3],
#                 [avg_final_line_R_ego_jpg_3,             avg_line_R_ego_jpg_3],
#                 [avg_final_line_R_ego_json_3,            avg_line_R_ego_json_3],
#                 [avg_final_line_R_ego_tokenized_txt_3,   avg_line_R_ego_tokenized_txt_3]
#                 ]

# occupancy_R_ego_3 = [[avg_final_occupancy_R_ego_adj_json_3,      avg_occupancy_R_ego_adj_json_3],
#                      [avg_final_occupancy_R_ego_adj_txt_3,            avg_occupancy_R_ego_adj_txt_3],
#                      [avg_final_occupancy_R_ego_jpg_3,                avg_occupancy_R_ego_jpg_3],
#                      [avg_final_occupancy_R_ego_json_3,               avg_occupancy_R_ego_json_3],
#                      [avg_final_occupancy_R_ego_tokenized_txt_3,      avg_occupancy_R_ego_tokenized_txt_3],
#                      [avg_final_occupancy_R_ego_ascii_txt_3,          avg_occupancy_R_ego_ascii_txt_3]
#                      ]
                    


# line_NR_coords_6 = [[avg_line_NR_coords_adj_json_output_6,      avg_line_NR_coords_adj_json_6],
#                    [avg_line_NR_coords_adj_txt_output_6,        avg_line_NR_coords_adj_txt_6],
#                    [avg_line_NR_coords_jpg_output_6,            avg_line_NR_coords_jpg_6],
#                    [avg_line_NR_coords_json_output_6,           avg_line_NR_coords_json_6],
#                    [avg_line_NR_coords_tokenized_txt_output_6,  avg_line_NR_coords_tokenized_txt_6]
#                    ]

# occupancy_NR_coords_6 = [[avg_occupancy_NR_coords_adj_json_output_6,    avg_occupancy_NR_coords_adj_json_6],
#                          [avg_occupancy_NR_coords_adj_txt_output_6,           avg_occupancy_NR_coords_adj_txt_6],
#                          [avg_occupancy_NR_coords_jpg_output_6,               avg_occupancy_NR_coords_jpg_6],
#                          [avg_occupancy_NR_coords_json_output_6,              avg_occupancy_NR_coords_json_6],
#                          [avg_occupancy_NR_coords_tokenized_txt_output_6,     avg_occupancy_NR_coords_tokenized_txt_6],
#                          [avg_occupancy_NR_coords_ascii_txt_output_6,         avg_occupancy_NR_coords_ascii_txt_6]
#                          ]


# line_R_coords_6 = [[avg_final_line_R_coords_adj_json_6,        avg_line_R_coords_adj_json_6],
#                    [avg_final_line_R_coords_adj_txt_6,         avg_line_R_coords_adj_txt_6],
#                    [avg_final_line_R_coords_jpg_6,             avg_line_R_coords_jpg_6],
#                    [avg_final_line_R_coords_json_6,            avg_line_R_coords_json_6],
#                    [avg_final_line_R_coords_tokenized_txt_6,   avg_line_R_coords_tokenized_txt_6]
#                    ]

# occupancy_R_coords_6 = [[avg_final_occupancy_R_coords_adj_json_6,      avg_occupancy_R_coords_adj_json_6],
#                         [avg_final_occupancy_R_coords_adj_txt_6,            avg_occupancy_R_coords_adj_txt_6],
#                         [avg_final_occupancy_R_coords_jpg_6,                avg_occupancy_R_coords_jpg_6],
#                         [avg_final_occupancy_R_coords_json_6,               avg_occupancy_R_coords_json_6],
#                         [avg_final_occupancy_R_coords_tokenized_txt_6,      avg_occupancy_R_coords_tokenized_txt_6],
#                         [avg_final_occupancy_R_coords_ascii_txt_6,         avg_occupancy_R_coords_ascii_txt_6]
#                         ]
                    
# line_NR_allo_6 = [[avg_line_NR_allo_adj_json_output_6,      avg_line_NR_allo_adj_json_6],
#                   [avg_line_NR_allo_adj_txt_output_6,        avg_line_NR_allo_adj_txt_6],
#                   [avg_line_NR_allo_jpg_output_6,            avg_line_NR_allo_jpg_6],
#                   [avg_line_NR_allo_json_output_6,           avg_line_NR_allo_json_6],
#                   [avg_line_NR_allo_tokenized_txt_output_6,  avg_line_NR_allo_tokenized_txt_6]
#                   ]

# occupancy_NR_allo_6 = [[avg_occupancy_NR_allo_adj_json_output_6,    avg_occupancy_NR_allo_adj_json_6],
#                        [avg_occupancy_NR_allo_adj_txt_output_6,           avg_occupancy_NR_allo_adj_txt_6],
#                        [avg_occupancy_NR_allo_jpg_output_6,               avg_occupancy_NR_allo_jpg_6],
#                        [avg_occupancy_NR_allo_json_output_6,              avg_occupancy_NR_allo_json_6],
#                        [avg_occupancy_NR_allo_tokenized_txt_output_6,     avg_occupancy_NR_allo_tokenized_txt_6],
#                        [avg_occupancy_NR_allo_ascii_txt_output_6,        avg_occupancy_NR_allo_ascii_txt_6]   
#                        ]


# line_R_allo_6 = [[avg_final_line_R_allo_adj_json_6,        avg_line_R_allo_adj_json_6],
#                 [avg_final_line_R_allo_adj_txt_6,         avg_line_R_allo_adj_txt_6],
#                 [avg_final_line_R_allo_jpg_6,             avg_line_R_allo_jpg_6],
#                 [avg_final_line_R_allo_json_6,            avg_line_R_allo_json_6],
#                 [avg_final_line_R_allo_tokenized_txt_6,   avg_line_R_allo_tokenized_txt_6]
#                 ]

# occupancy_R_allo_6 = [[avg_final_occupancy_R_allo_adj_json_6,      avg_occupancy_R_allo_adj_json_6],
#                       [avg_final_occupancy_R_allo_adj_txt_6,            avg_occupancy_R_allo_adj_txt_6],
#                       [avg_final_occupancy_R_allo_jpg_6,                avg_occupancy_R_allo_jpg_6],
#                       [avg_final_occupancy_R_allo_json_6,               avg_occupancy_R_allo_json_6],
#                       [avg_final_occupancy_R_allo_tokenized_txt_6,      avg_occupancy_R_allo_tokenized_txt_6],
#                       [avg_final_occupancy_R_allo_ascii_txt_6,          avg_occupancy_R_allo_ascii_txt_6]
#                       ]
                    
# line_NR_ego_6 = [[avg_line_NR_ego_adj_json_output_6,      avg_line_NR_ego_adj_json_6],
#                 [avg_line_NR_ego_adj_txt_output_6,        avg_line_NR_ego_adj_txt_6],
#                 [avg_line_NR_ego_jpg_output_6,            avg_line_NR_ego_jpg_6],
#                 [avg_line_NR_ego_json_output_6,           avg_line_NR_ego_json_6],
#                 [avg_line_NR_ego_tokenized_txt_output_6,  avg_line_NR_ego_tokenized_txt_6]
#                 ]

# occupancy_NR_ego_6 = [[avg_occupancy_NR_ego_adj_json_output_6,    avg_occupancy_NR_ego_adj_json_6],
#                       [avg_occupancy_NR_ego_adj_txt_output_6,           avg_occupancy_NR_ego_adj_txt_6],
#                       [avg_occupancy_NR_ego_jpg_output_6,               avg_occupancy_NR_ego_jpg_6],
#                       [avg_occupancy_NR_ego_json_output_6,              avg_occupancy_NR_ego_json_6],
#                       [avg_occupancy_NR_ego_tokenized_txt_output_6,     avg_occupancy_NR_ego_tokenized_txt_6],
#                         [avg_occupancy_NR_ego_ascii_txt_output_6,         avg_occupancy_NR_ego_ascii_txt_6]
#                       ]


# line_R_ego_6 = [[avg_final_line_R_ego_adj_json_6,        avg_line_R_ego_adj_json_6],
#                 [avg_final_line_R_ego_adj_txt_6,         avg_line_R_ego_adj_txt_6],
#                 [avg_final_line_R_ego_jpg_6,             avg_line_R_ego_jpg_6],
#                 [avg_final_line_R_ego_json_6,            avg_line_R_ego_json_6],
#                 [avg_final_line_R_ego_tokenized_txt_6,   avg_line_R_ego_tokenized_txt_6]
#                 ]

# occupancy_R_ego_6 = [[avg_final_occupancy_R_ego_adj_json_6,      avg_occupancy_R_ego_adj_json_6],
#                      [avg_final_occupancy_R_ego_adj_txt_6,            avg_occupancy_R_ego_adj_txt_6],
#                      [avg_final_occupancy_R_ego_jpg_6,                avg_occupancy_R_ego_jpg_6],
#                      [avg_final_occupancy_R_ego_json_6,               avg_occupancy_R_ego_json_6],
#                      [avg_final_occupancy_R_ego_tokenized_txt_6,      avg_occupancy_R_ego_tokenized_txt_6],
#                     [avg_final_occupancy_R_ego_ascii_txt_6,          avg_occupancy_R_ego_ascii_txt_6]
#                      ]
                    



# line_NR_coords_15 = [[avg_line_NR_coords_adj_json_output_15,      avg_line_NR_coords_adj_json_15],
#                    [avg_line_NR_coords_adj_txt_output_15,        avg_line_NR_coords_adj_txt_15],
#                    [avg_line_NR_coords_jpg_output_15,            avg_line_NR_coords_jpg_15],
#                    [avg_line_NR_coords_json_output_15,           avg_line_NR_coords_json_15],
#                    [avg_line_NR_coords_tokenized_txt_output_15,  avg_line_NR_coords_tokenized_txt_15]
#                    ]

# occupancy_NR_coords_15 = [[avg_occupancy_NR_coords_adj_json_output_15,    avg_occupancy_NR_coords_adj_json_15],
#                          [avg_occupancy_NR_coords_adj_txt_output_15,           avg_occupancy_NR_coords_adj_txt_15],
#                          [avg_occupancy_NR_coords_jpg_output_15,               avg_occupancy_NR_coords_jpg_15],
#                          [avg_occupancy_NR_coords_json_output_15,              avg_occupancy_NR_coords_json_15],
#                          [avg_occupancy_NR_coords_tokenized_txt_output_15,     avg_occupancy_NR_coords_tokenized_txt_15],
#                         [avg_occupancy_NR_coords_ascii_txt_output_15,         avg_occupancy_NR_coords_ascii_txt_15]
#                          ]


# line_R_coords_15 = [[avg_final_line_R_coords_adj_json_15,        avg_line_R_coords_adj_json_15],
#                    [avg_final_line_R_coords_adj_txt_15,         avg_line_R_coords_adj_txt_15],
#                    [avg_final_line_R_coords_jpg_15,             avg_line_R_coords_jpg_15],
#                    [avg_final_line_R_coords_json_15,            avg_line_R_coords_json_15],
#                    [avg_final_line_R_coords_tokenized_txt_15,   avg_line_R_coords_tokenized_txt_15]
#                    ]

# occupancy_R_coords_15 = [[avg_final_occupancy_R_coords_adj_json_15,      avg_occupancy_R_coords_adj_json_15],
#                         [avg_final_occupancy_R_coords_adj_txt_15,            avg_occupancy_R_coords_adj_txt_15],
#                         [avg_final_occupancy_R_coords_jpg_15,                avg_occupancy_R_coords_jpg_15],
#                         [avg_final_occupancy_R_coords_json_15,               avg_occupancy_R_coords_json_15],
#                         [avg_final_occupancy_R_coords_tokenized_txt_15,      avg_occupancy_R_coords_tokenized_txt_15],
#                         [avg_final_occupancy_R_coords_ascii_txt_15,         avg_occupancy_R_coords_ascii_txt_15]
#                         ]
                    
# line_NR_allo_15 = [[avg_line_NR_allo_adj_json_output_15,      avg_line_NR_allo_adj_json_15],
#                   [avg_line_NR_allo_adj_txt_output_15,        avg_line_NR_allo_adj_txt_15],
#                   [avg_line_NR_allo_jpg_output_15,            avg_line_NR_allo_jpg_15],
#                   [avg_line_NR_allo_json_output_15,           avg_line_NR_allo_json_15],
#                   [avg_line_NR_allo_tokenized_txt_output_15,  avg_line_NR_allo_tokenized_txt_15]
#                   ]

# occupancy_NR_allo_15 = [[avg_occupancy_NR_allo_adj_json_output_15,    avg_occupancy_NR_allo_adj_json_15],
#                        [avg_occupancy_NR_allo_adj_txt_output_15,           avg_occupancy_NR_allo_adj_txt_15],
#                        [avg_occupancy_NR_allo_jpg_output_15,               avg_occupancy_NR_allo_jpg_15],
#                        [avg_occupancy_NR_allo_json_output_15,              avg_occupancy_NR_allo_json_15],
#                        [avg_occupancy_NR_allo_tokenized_txt_output_15,     avg_occupancy_NR_allo_tokenized_txt_15],
#                         [avg_occupancy_NR_allo_ascii_txt_output_15,        avg_occupancy_NR_allo_ascii_txt_15]
#                        ]


# line_R_allo_15 = [[avg_final_line_R_allo_adj_json_15,        avg_line_R_allo_adj_json_15],
#                 [avg_final_line_R_allo_adj_txt_15,         avg_line_R_allo_adj_txt_15],
#                 [avg_final_line_R_allo_jpg_15,             avg_line_R_allo_jpg_15],
#                 [avg_final_line_R_allo_json_15,            avg_line_R_allo_json_15],
#                 [avg_final_line_R_allo_tokenized_txt_15,   avg_line_R_allo_tokenized_txt_15]
#                 ]

# occupancy_R_allo_15 = [[avg_final_occupancy_R_allo_adj_json_15,      avg_occupancy_R_allo_adj_json_15],
#                       [avg_final_occupancy_R_allo_adj_txt_15,            avg_occupancy_R_allo_adj_txt_15],
#                       [avg_final_occupancy_R_allo_jpg_15,                avg_occupancy_R_allo_jpg_15],
#                       [avg_final_occupancy_R_allo_json_15,               avg_occupancy_R_allo_json_15],
#                       [avg_final_occupancy_R_allo_tokenized_txt_15,      avg_occupancy_R_allo_tokenized_txt_15],
#                     [avg_final_occupancy_R_allo_ascii_txt_15,          avg_occupancy_R_allo_ascii_txt_15]
#                       ]
                    
# line_NR_ego_15 = [[avg_line_NR_ego_adj_json_output_15,      avg_line_NR_ego_adj_json_15],
#                 [avg_line_NR_ego_adj_txt_output_15,        avg_line_NR_ego_adj_txt_15],
#                 [avg_line_NR_ego_jpg_output_15,            avg_line_NR_ego_jpg_15],
#                 [avg_line_NR_ego_json_output_15,           avg_line_NR_ego_json_15],
#                 [avg_line_NR_ego_tokenized_txt_output_15,  avg_line_NR_ego_tokenized_txt_15]
#                 ]

# occupancy_NR_ego_15 = [[avg_occupancy_NR_ego_adj_json_output_15,    avg_occupancy_NR_ego_adj_json_15],
#                       [avg_occupancy_NR_ego_adj_txt_output_15,           avg_occupancy_NR_ego_adj_txt_15],
#                       [avg_occupancy_NR_ego_jpg_output_15,               avg_occupancy_NR_ego_jpg_15],
#                       [avg_occupancy_NR_ego_json_output_15,              avg_occupancy_NR_ego_json_15],
#                       [avg_occupancy_NR_ego_tokenized_txt_output_15,     avg_occupancy_NR_ego_tokenized_txt_15],
#                     [avg_occupancy_NR_ego_ascii_txt_output_15,         avg_occupancy_NR_ego_ascii_txt_15]
#                       ]


# line_R_ego_15 = [[avg_final_line_R_ego_adj_json_15,        avg_line_R_ego_adj_json_15],
#                 [avg_final_line_R_ego_adj_txt_15,         avg_line_R_ego_adj_txt_15],
#                 [avg_final_line_R_ego_jpg_15,             avg_line_R_ego_jpg_15],
#                 [avg_final_line_R_ego_json_15,            avg_line_R_ego_json_15],
#                 [avg_final_line_R_ego_tokenized_txt_15,   avg_line_R_ego_tokenized_txt_15]
#                 ]

# occupancy_R_ego_15 = [[avg_final_occupancy_R_ego_adj_json_15,      avg_occupancy_R_ego_adj_json_15],
#                      [avg_final_occupancy_R_ego_adj_txt_15,            avg_occupancy_R_ego_adj_txt_15],
#                      [avg_final_occupancy_R_ego_jpg_15,                avg_occupancy_R_ego_jpg_15],
#                      [avg_final_occupancy_R_ego_json_15,               avg_occupancy_R_ego_json_15],
#                      [avg_final_occupancy_R_ego_tokenized_txt_15,      avg_occupancy_R_ego_tokenized_txt_15],
#                     [avg_final_occupancy_R_ego_ascii_txt_15,          avg_occupancy_R_ego_ascii_txt_15]
#                      ]



# For plotting exclusively thinking tokens, without final answer tokens.

# figure = 'thinking_tokens' # this is for choosing the correct title and axis labels
# line_NR_coords_3 = [[avg_line_NR_coords_adj_json_output_3,      avg_line_NR_coords_adj_json_3],
#                    [avg_line_NR_coords_adj_txt_output_3,        avg_line_NR_coords_adj_txt_3],
#                    [avg_line_NR_coords_jpg_output_3,            avg_line_NR_coords_jpg_3],
#                    [avg_line_NR_coords_json_output_3,           avg_line_NR_coords_json_3],
#                    [avg_line_NR_coords_tokenized_txt_output_3,  avg_line_NR_coords_tokenized_txt_3]
#                    ]

# occupancy_NR_coords_3 = [[avg_occupancy_NR_coords_adj_json_output_3,    avg_occupancy_NR_coords_adj_json_3],
#                          [avg_occupancy_NR_coords_adj_txt_output_3,           avg_occupancy_NR_coords_adj_txt_3],
#                          [avg_occupancy_NR_coords_jpg_output_3,               avg_occupancy_NR_coords_jpg_3],
#                          [avg_occupancy_NR_coords_json_output_3,              avg_occupancy_NR_coords_json_3],
#                          [avg_occupancy_NR_coords_tokenized_txt_output_3,     avg_occupancy_NR_coords_tokenized_txt_3],
#                          [avg_occupancy_NR_coords_ascii_txt_output_3,        avg_occupancy_NR_coords_ascii_txt_3]
#                          ]
# print('shape:', avg_occupancy_R_coords_adj_txt_output_15.shape)
# print('output:', avg_occupancy_R_coords_adj_txt_output_15)
# print('final:' , avg_final_occupancy_R_coords_adj_txt_15)
# sub = avg_occupancy_R_coords_adj_txt_output_15- avg_final_occupancy_R_coords_adj_txt_15
# print('subtraction:', sub)


# line_R_coords_3 = [[avg_line_R_coords_adj_json_output_3 - avg_final_line_R_coords_adj_json_3,             avg_line_R_coords_adj_json_3],
#                 [avg_line_R_coords_adj_txt_output_3 - avg_final_line_R_coords_adj_txt_3,                avg_line_R_coords_adj_txt_3],
#                 [avg_line_R_coords_jpg_output_3 - avg_final_line_R_coords_jpg_3,                        avg_line_R_coords_jpg_3],
#                 [avg_line_R_coords_json_output_3 - avg_final_line_R_coords_json_3,                      avg_line_R_coords_json_3],
#                 [avg_line_R_coords_tokenized_txt_output_3 - avg_final_line_R_coords_tokenized_txt_3,    avg_line_R_coords_tokenized_txt_3]
#                 ]

# occupancy_R_coords_3 = [[avg_occupancy_R_coords_adj_json_output_3 - avg_final_occupancy_R_coords_adj_json_3,      avg_occupancy_R_coords_adj_json_3],
#                      [avg_occupancy_R_coords_adj_txt_output_3 - avg_final_occupancy_R_coords_adj_txt_3,            avg_occupancy_R_coords_adj_txt_3],
#                      [avg_occupancy_R_coords_jpg_output_3 - avg_final_occupancy_R_coords_jpg_3,                avg_occupancy_R_coords_jpg_3],
#                      [avg_occupancy_R_coords_json_output_3 - avg_final_occupancy_R_coords_json_3,               avg_occupancy_R_coords_json_3],
#                      [avg_occupancy_R_coords_tokenized_txt_output_3 - avg_final_occupancy_R_coords_tokenized_txt_3,      avg_occupancy_R_coords_tokenized_txt_3],
#                     [avg_occupancy_R_coords_ascii_txt_output_3 - avg_final_occupancy_R_coords_ascii_txt_3,          avg_occupancy_R_coords_ascii_txt_3]
#                      ]
                    
# line_NR_allo_3 = [[avg_line_NR_allo_adj_json_output_3,      avg_line_NR_allo_adj_json_3],
#                   [avg_line_NR_allo_adj_txt_output_3,        avg_line_NR_allo_adj_txt_3],
#                   [avg_line_NR_allo_jpg_output_3,            avg_line_NR_allo_jpg_3],
#                   [avg_line_NR_allo_json_output_3,           avg_line_NR_allo_json_3],
#                   [avg_line_NR_allo_tokenized_txt_output_3,  avg_line_NR_allo_tokenized_txt_3]
#                   ]

# occupancy_NR_allo_3 = [[avg_occupancy_NR_allo_adj_json_output_3,    avg_occupancy_NR_allo_adj_json_3],
#                        [avg_occupancy_NR_allo_adj_txt_output_3,           avg_occupancy_NR_allo_adj_txt_3],
#                        [avg_occupancy_NR_allo_jpg_output_3,               avg_occupancy_NR_allo_jpg_3],
#                        [avg_occupancy_NR_allo_json_output_3,              avg_occupancy_NR_allo_json_3],
#                        [avg_occupancy_NR_allo_tokenized_txt_output_3,     avg_occupancy_NR_allo_tokenized_txt_3],
#                        [avg_occupancy_NR_allo_ascii_txt_output_3,        avg_occupancy_NR_allo_ascii_txt_3]
#                        ]


# line_R_allo_3 = [[avg_line_R_allo_adj_json_output_3 - avg_final_line_R_allo_adj_json_3,             avg_line_R_allo_adj_json_3],
#                 [avg_line_R_allo_adj_txt_output_3 - avg_final_line_R_allo_adj_txt_3,                avg_line_R_allo_adj_txt_3],
#                 [avg_line_R_allo_jpg_output_3 - avg_final_line_R_allo_jpg_3,                        avg_line_R_allo_jpg_3],
#                 [avg_line_R_allo_json_output_3 - avg_final_line_R_allo_json_3,                      avg_line_R_allo_json_3],
#                 [avg_line_R_allo_tokenized_txt_output_3 - avg_final_line_R_allo_tokenized_txt_3,    avg_line_R_allo_tokenized_txt_3]
#                 ]

# occupancy_R_allo_3 = [[avg_occupancy_R_allo_adj_json_output_3 - avg_final_occupancy_R_allo_adj_json_3,      avg_occupancy_R_allo_adj_json_3],
#                      [avg_occupancy_R_allo_adj_txt_output_3 - avg_final_occupancy_R_allo_adj_txt_3,            avg_occupancy_R_allo_adj_txt_3],
#                      [avg_occupancy_R_allo_jpg_output_3 - avg_final_occupancy_R_allo_jpg_3,                avg_occupancy_R_allo_jpg_3],
#                      [avg_occupancy_R_allo_json_output_3 - avg_final_occupancy_R_allo_json_3,               avg_occupancy_R_allo_json_3],
#                      [avg_occupancy_R_allo_tokenized_txt_output_3 - avg_final_occupancy_R_allo_tokenized_txt_3,      avg_occupancy_R_allo_tokenized_txt_3],
#                     [avg_occupancy_R_allo_ascii_txt_output_3 - avg_final_occupancy_R_allo_ascii_txt_3,          avg_occupancy_R_allo_ascii_txt_3]
#                      ]
                    
# line_NR_ego_3 = [[avg_line_NR_ego_adj_json_output_3,      avg_line_NR_ego_adj_json_3],
#                 [avg_line_NR_ego_adj_txt_output_3,        avg_line_NR_ego_adj_txt_3],
#                 [avg_line_NR_ego_jpg_output_3,            avg_line_NR_ego_jpg_3],
#                 [avg_line_NR_ego_json_output_3,           avg_line_NR_ego_json_3],
#                 [avg_line_NR_ego_tokenized_txt_output_3,  avg_line_NR_ego_tokenized_txt_3]
#                 ]

# occupancy_NR_ego_3 = [[avg_occupancy_NR_ego_adj_json_output_3,          avg_occupancy_NR_ego_adj_json_3],
#                       [avg_occupancy_NR_ego_adj_txt_output_3,           avg_occupancy_NR_ego_adj_txt_3],
#                       [avg_occupancy_NR_ego_jpg_output_3,               avg_occupancy_NR_ego_jpg_3],
#                       [avg_occupancy_NR_ego_json_output_3,              avg_occupancy_NR_ego_json_3],
#                       [avg_occupancy_NR_ego_tokenized_txt_output_3,     avg_occupancy_NR_ego_tokenized_txt_3],
#                       [avg_occupancy_NR_ego_ascii_txt_output_3,         avg_occupancy_NR_ego_ascii_txt_3]
#                       ]



# line_R_ego_3 = [[avg_line_R_ego_adj_json_output_3 - avg_final_line_R_ego_adj_json_3,             avg_line_R_ego_adj_json_3],
#                 [avg_line_R_ego_adj_txt_output_3 - avg_final_line_R_ego_adj_txt_3,                avg_line_R_ego_adj_txt_3],
#                 [avg_line_R_ego_jpg_output_3 - avg_final_line_R_ego_jpg_3,                        avg_line_R_ego_jpg_3],
#                 [avg_line_R_ego_json_output_3 - avg_final_line_R_ego_json_3,                      avg_line_R_ego_json_3],
#                 [avg_line_R_ego_tokenized_txt_output_3 - avg_final_line_R_ego_tokenized_txt_3,    avg_line_R_ego_tokenized_txt_3]
#                 ]

# occupancy_R_ego_3 = [[avg_occupancy_R_ego_adj_json_output_3 - avg_final_occupancy_R_ego_adj_json_3,      avg_occupancy_R_ego_adj_json_3],
#                      [avg_occupancy_R_ego_adj_txt_output_3 - avg_final_occupancy_R_ego_adj_txt_3,            avg_occupancy_R_ego_adj_txt_3],
#                      [avg_occupancy_R_ego_jpg_output_3 - avg_final_occupancy_R_ego_jpg_3,                avg_occupancy_R_ego_jpg_3],
#                      [avg_occupancy_R_ego_json_output_3 - avg_final_occupancy_R_ego_json_3,               avg_occupancy_R_ego_json_3],
#                      [avg_occupancy_R_ego_tokenized_txt_output_3 - avg_final_occupancy_R_ego_tokenized_txt_3,      avg_occupancy_R_ego_tokenized_txt_3],
#                     [avg_occupancy_R_ego_ascii_txt_output_3 - avg_final_occupancy_R_ego_ascii_txt_3,          avg_occupancy_R_ego_ascii_txt_3]
#                      ]

                    


# line_NR_coords_6 = [[avg_line_NR_coords_adj_json_output_6,      avg_line_NR_coords_adj_json_6],
#                    [avg_line_NR_coords_adj_txt_output_6,        avg_line_NR_coords_adj_txt_6],
#                    [avg_line_NR_coords_jpg_output_6,            avg_line_NR_coords_jpg_6],
#                    [avg_line_NR_coords_json_output_6,           avg_line_NR_coords_json_6],
#                    [avg_line_NR_coords_tokenized_txt_output_6,  avg_line_NR_coords_tokenized_txt_6]
#                    ]

# occupancy_NR_coords_6 = [[avg_occupancy_NR_coords_adj_json_output_6,    avg_occupancy_NR_coords_adj_json_6],
#                          [avg_occupancy_NR_coords_adj_txt_output_6,           avg_occupancy_NR_coords_adj_txt_6],
#                          [avg_occupancy_NR_coords_jpg_output_6,               avg_occupancy_NR_coords_jpg_6],
#                          [avg_occupancy_NR_coords_json_output_6,              avg_occupancy_NR_coords_json_6],
#                          [avg_occupancy_NR_coords_tokenized_txt_output_6,     avg_occupancy_NR_coords_tokenized_txt_6],
#                          [avg_occupancy_NR_coords_ascii_txt_output_6,         avg_occupancy_NR_coords_ascii_txt_6]
#                          ]



# line_R_coords_6 = [[avg_line_R_coords_adj_json_output_6 - avg_final_line_R_coords_adj_json_6,             avg_line_R_coords_adj_json_6],
#                 [avg_line_R_coords_adj_txt_output_6 - avg_final_line_R_coords_adj_txt_6,                avg_line_R_coords_adj_txt_6],
#                 [avg_line_R_coords_jpg_output_6 - avg_final_line_R_coords_jpg_6,                        avg_line_R_coords_jpg_6],
#                 [avg_line_R_coords_json_output_6 - avg_final_line_R_coords_json_6,                      avg_line_R_coords_json_6],
#                 [avg_line_R_coords_tokenized_txt_output_6 - avg_final_line_R_coords_tokenized_txt_6,    avg_line_R_coords_tokenized_txt_6]
#                 ]

# occupancy_R_coords_6 = [[avg_occupancy_R_coords_adj_json_output_6 - avg_final_occupancy_R_coords_adj_json_6,      avg_occupancy_R_coords_adj_json_6],
#                      [avg_occupancy_R_coords_adj_txt_output_6 - avg_final_occupancy_R_coords_adj_txt_6,            avg_occupancy_R_coords_adj_txt_6],
#                      [avg_occupancy_R_coords_jpg_output_6 - avg_final_occupancy_R_coords_jpg_6,                avg_occupancy_R_coords_jpg_6],
#                      [avg_occupancy_R_coords_json_output_6 - avg_final_occupancy_R_coords_json_6,               avg_occupancy_R_coords_json_6],
#                      [avg_occupancy_R_coords_tokenized_txt_output_6 - avg_final_occupancy_R_coords_tokenized_txt_6,      avg_occupancy_R_coords_tokenized_txt_6],
#                     [avg_occupancy_R_coords_ascii_txt_output_6 - avg_final_occupancy_R_coords_ascii_txt_6,          avg_occupancy_R_coords_ascii_txt_6]
#                      ]
                    
# line_NR_allo_6 = [[avg_line_NR_allo_adj_json_output_6,      avg_line_NR_allo_adj_json_6],
#                   [avg_line_NR_allo_adj_txt_output_6,        avg_line_NR_allo_adj_txt_6],
#                   [avg_line_NR_allo_jpg_output_6,            avg_line_NR_allo_jpg_6],
#                   [avg_line_NR_allo_json_output_6,           avg_line_NR_allo_json_6],
#                   [avg_line_NR_allo_tokenized_txt_output_6,  avg_line_NR_allo_tokenized_txt_6]
#                   ]

# occupancy_NR_allo_6 = [[avg_occupancy_NR_allo_adj_json_output_6,    avg_occupancy_NR_allo_adj_json_6],
#                        [avg_occupancy_NR_allo_adj_txt_output_6,           avg_occupancy_NR_allo_adj_txt_6],
#                        [avg_occupancy_NR_allo_jpg_output_6,               avg_occupancy_NR_allo_jpg_6],
#                        [avg_occupancy_NR_allo_json_output_6,              avg_occupancy_NR_allo_json_6],
#                        [avg_occupancy_NR_allo_tokenized_txt_output_6,     avg_occupancy_NR_allo_tokenized_txt_6],
#                        [avg_occupancy_NR_allo_ascii_txt_output_6,        avg_occupancy_NR_allo_ascii_txt_6]   
#                        ]

# line_R_allo_6 = [[avg_line_R_allo_adj_json_output_6 - avg_final_line_R_allo_adj_json_6,             avg_line_R_allo_adj_json_6],
#                 [avg_line_R_allo_adj_txt_output_6 - avg_final_line_R_allo_adj_txt_6,                avg_line_R_allo_adj_txt_6],
#                 [avg_line_R_allo_jpg_output_6 - avg_final_line_R_allo_jpg_6,                        avg_line_R_allo_jpg_6],
#                 [avg_line_R_allo_json_output_6 - avg_final_line_R_allo_json_6,                      avg_line_R_allo_json_6],
#                 [avg_line_R_allo_tokenized_txt_output_6 - avg_final_line_R_allo_tokenized_txt_6,    avg_line_R_allo_tokenized_txt_6]
#                 ]

# occupancy_R_allo_6 = [[avg_occupancy_R_allo_adj_json_output_6 - avg_final_occupancy_R_allo_adj_json_6,      avg_occupancy_R_allo_adj_json_6],
#                      [avg_occupancy_R_allo_adj_txt_output_6 - avg_final_occupancy_R_allo_adj_txt_6,            avg_occupancy_R_allo_adj_txt_6],
#                      [avg_occupancy_R_allo_jpg_output_6 - avg_final_occupancy_R_allo_jpg_6,                avg_occupancy_R_allo_jpg_6],
#                      [avg_occupancy_R_allo_json_output_6 - avg_final_occupancy_R_allo_json_6,               avg_occupancy_R_allo_json_6],
#                      [avg_occupancy_R_allo_tokenized_txt_output_6 - avg_final_occupancy_R_allo_tokenized_txt_6,      avg_occupancy_R_allo_tokenized_txt_6],
#                     [avg_occupancy_R_allo_ascii_txt_output_6 - avg_final_occupancy_R_allo_ascii_txt_6,          avg_occupancy_R_allo_ascii_txt_6]
#                      ]
                    
# line_NR_ego_6 = [[avg_line_NR_ego_adj_json_output_6,      avg_line_NR_ego_adj_json_6],
#                 [avg_line_NR_ego_adj_txt_output_6,        avg_line_NR_ego_adj_txt_6],
#                 [avg_line_NR_ego_jpg_output_6,            avg_line_NR_ego_jpg_6],
#                 [avg_line_NR_ego_json_output_6,           avg_line_NR_ego_json_6],
#                 [avg_line_NR_ego_tokenized_txt_output_6,  avg_line_NR_ego_tokenized_txt_6]
#                 ]

# occupancy_NR_ego_6 = [[avg_occupancy_NR_ego_adj_json_output_6,    avg_occupancy_NR_ego_adj_json_6],
#                       [avg_occupancy_NR_ego_adj_txt_output_6,           avg_occupancy_NR_ego_adj_txt_6],
#                       [avg_occupancy_NR_ego_jpg_output_6,               avg_occupancy_NR_ego_jpg_6],
#                       [avg_occupancy_NR_ego_json_output_6,              avg_occupancy_NR_ego_json_6],
#                       [avg_occupancy_NR_ego_tokenized_txt_output_6,     avg_occupancy_NR_ego_tokenized_txt_6],
#                         [avg_occupancy_NR_ego_ascii_txt_output_6,         avg_occupancy_NR_ego_ascii_txt_6]
#                       ]



# line_R_ego_6 = [[avg_line_R_ego_adj_json_output_6 - avg_final_line_R_ego_adj_json_6,             avg_line_R_ego_adj_json_6],
#                 [avg_line_R_ego_adj_txt_output_6 - avg_final_line_R_ego_adj_txt_6,                avg_line_R_ego_adj_txt_6],
#                 [avg_line_R_ego_jpg_output_6 - avg_final_line_R_ego_jpg_6,                        avg_line_R_ego_jpg_6],
#                 [avg_line_R_ego_json_output_6 - avg_final_line_R_ego_json_6,                      avg_line_R_ego_json_6],
#                 [avg_line_R_ego_tokenized_txt_output_6 - avg_final_line_R_ego_tokenized_txt_6,    avg_line_R_ego_tokenized_txt_6]
#                 ]

# occupancy_R_ego_6 = [[avg_occupancy_R_ego_adj_json_output_6 - avg_final_occupancy_R_ego_adj_json_6,      avg_occupancy_R_ego_adj_json_6],
#                      [avg_occupancy_R_ego_adj_txt_output_6 - avg_final_occupancy_R_ego_adj_txt_6,            avg_occupancy_R_ego_adj_txt_6],
#                      [avg_occupancy_R_ego_jpg_output_6 - avg_final_occupancy_R_ego_jpg_6,                avg_occupancy_R_ego_jpg_6],
#                      [avg_occupancy_R_ego_json_output_6 - avg_final_occupancy_R_ego_json_6,               avg_occupancy_R_ego_json_6],
#                      [avg_occupancy_R_ego_tokenized_txt_output_6 - avg_final_occupancy_R_ego_tokenized_txt_6,      avg_occupancy_R_ego_tokenized_txt_6],
#                     [avg_occupancy_R_ego_ascii_txt_output_6 - avg_final_occupancy_R_ego_ascii_txt_6,          avg_occupancy_R_ego_ascii_txt_6]
#                      ]




# line_NR_coords_15 = [[avg_line_NR_coords_adj_json_output_15,      avg_line_NR_coords_adj_json_15],
#                    [avg_line_NR_coords_adj_txt_output_15,        avg_line_NR_coords_adj_txt_15],
#                    [avg_line_NR_coords_jpg_output_15,            avg_line_NR_coords_jpg_15],
#                    [avg_line_NR_coords_json_output_15,           avg_line_NR_coords_json_15],
#                    [avg_line_NR_coords_tokenized_txt_output_15,  avg_line_NR_coords_tokenized_txt_15]
#                    ]

# occupancy_NR_coords_15 = [[avg_occupancy_NR_coords_adj_json_output_15,    avg_occupancy_NR_coords_adj_json_15],
#                          [avg_occupancy_NR_coords_adj_txt_output_15,           avg_occupancy_NR_coords_adj_txt_15],
#                          [avg_occupancy_NR_coords_jpg_output_15,               avg_occupancy_NR_coords_jpg_15],
#                          [avg_occupancy_NR_coords_json_output_15,              avg_occupancy_NR_coords_json_15],
#                          [avg_occupancy_NR_coords_tokenized_txt_output_15,     avg_occupancy_NR_coords_tokenized_txt_15],
#                         [avg_occupancy_NR_coords_ascii_txt_output_15,         avg_occupancy_NR_coords_ascii_txt_15]
#                          ]


# line_R_coords_15 = [[avg_line_R_coords_adj_json_output_15 - avg_final_line_R_coords_adj_json_15,             avg_line_R_coords_adj_json_15],
#                 [avg_line_R_coords_adj_txt_output_15 - avg_final_line_R_coords_adj_txt_15,                avg_line_R_coords_adj_txt_15],
#                 [avg_line_R_coords_jpg_output_15 - avg_final_line_R_coords_jpg_15,                        avg_line_R_coords_jpg_15],
#                 [avg_line_R_coords_json_output_15 - avg_final_line_R_coords_json_15,                      avg_line_R_coords_json_15],
#                 [avg_line_R_coords_tokenized_txt_output_15 - avg_final_line_R_coords_tokenized_txt_15,    avg_line_R_coords_tokenized_txt_15]
#                 ]

# occupancy_R_coords_15 = [[avg_occupancy_R_coords_adj_json_output_15 - avg_final_occupancy_R_coords_adj_json_15,      avg_occupancy_R_coords_adj_json_15],
#                      [avg_occupancy_R_coords_adj_txt_output_15 - avg_final_occupancy_R_coords_adj_txt_15,            avg_occupancy_R_coords_adj_txt_15],
#                      [avg_occupancy_R_coords_jpg_output_15 - avg_final_occupancy_R_coords_jpg_15,                avg_occupancy_R_coords_jpg_15],
#                      [avg_occupancy_R_coords_json_output_15 - avg_final_occupancy_R_coords_json_15,               avg_occupancy_R_coords_json_15],
#                      [avg_occupancy_R_coords_tokenized_txt_output_15 - avg_final_occupancy_R_coords_tokenized_txt_15,      avg_occupancy_R_coords_tokenized_txt_15],
#                     [avg_occupancy_R_coords_ascii_txt_output_15 - avg_final_occupancy_R_coords_ascii_txt_15,          avg_occupancy_R_coords_ascii_txt_15]
#                      ]

                    
# line_NR_allo_15 = [[avg_line_NR_allo_adj_json_output_15,      avg_line_NR_allo_adj_json_15],
#                   [avg_line_NR_allo_adj_txt_output_15,        avg_line_NR_allo_adj_txt_15],
#                   [avg_line_NR_allo_jpg_output_15,            avg_line_NR_allo_jpg_15],
#                   [avg_line_NR_allo_json_output_15,           avg_line_NR_allo_json_15],
#                   [avg_line_NR_allo_tokenized_txt_output_15,  avg_line_NR_allo_tokenized_txt_15]
#                   ]

# occupancy_NR_allo_15 = [[avg_occupancy_NR_allo_adj_json_output_15,    avg_occupancy_NR_allo_adj_json_15],
#                        [avg_occupancy_NR_allo_adj_txt_output_15,           avg_occupancy_NR_allo_adj_txt_15],
#                        [avg_occupancy_NR_allo_jpg_output_15,               avg_occupancy_NR_allo_jpg_15],
#                        [avg_occupancy_NR_allo_json_output_15,              avg_occupancy_NR_allo_json_15],
#                        [avg_occupancy_NR_allo_tokenized_txt_output_15,     avg_occupancy_NR_allo_tokenized_txt_15],
#                         [avg_occupancy_NR_allo_ascii_txt_output_15,        avg_occupancy_NR_allo_ascii_txt_15]
#                        ]


# line_R_allo_15 = [[avg_line_R_allo_adj_json_output_15 - avg_final_line_R_allo_adj_json_15,             avg_line_R_allo_adj_json_15],
#                 [avg_line_R_allo_adj_txt_output_15 - avg_final_line_R_allo_adj_txt_15,                avg_line_R_allo_adj_txt_15],
#                 [avg_line_R_allo_jpg_output_15 - avg_final_line_R_allo_jpg_15,                        avg_line_R_allo_jpg_15],
#                 [avg_line_R_allo_json_output_15 - avg_final_line_R_allo_json_15,                      avg_line_R_allo_json_15],
#                 [avg_line_R_allo_tokenized_txt_output_15 - avg_final_line_R_allo_tokenized_txt_15,    avg_line_R_allo_tokenized_txt_15]
#                 ]

# occupancy_R_allo_15 = [[avg_occupancy_R_allo_adj_json_output_15 - avg_final_occupancy_R_allo_adj_json_15,      avg_occupancy_R_allo_adj_json_15],
#                      [avg_occupancy_R_allo_adj_txt_output_15 - avg_final_occupancy_R_allo_adj_txt_15,            avg_occupancy_R_allo_adj_txt_15],
#                      [avg_occupancy_R_allo_jpg_output_15 - avg_final_occupancy_R_allo_jpg_15,                avg_occupancy_R_allo_jpg_15],
#                      [avg_occupancy_R_allo_json_output_15 - avg_final_occupancy_R_allo_json_15,               avg_occupancy_R_allo_json_15],
#                      [avg_occupancy_R_allo_tokenized_txt_output_15 - avg_final_occupancy_R_allo_tokenized_txt_15,      avg_occupancy_R_allo_tokenized_txt_15],
#                     [avg_occupancy_R_allo_ascii_txt_output_15 - avg_final_occupancy_R_allo_ascii_txt_15,          avg_occupancy_R_allo_ascii_txt_15]
#                      ]


                    
# line_NR_ego_15 = [[avg_line_NR_ego_adj_json_output_15,      avg_line_NR_ego_adj_json_15],
#                 [avg_line_NR_ego_adj_txt_output_15,        avg_line_NR_ego_adj_txt_15],
#                 [avg_line_NR_ego_jpg_output_15,            avg_line_NR_ego_jpg_15],
#                 [avg_line_NR_ego_json_output_15,           avg_line_NR_ego_json_15],
#                 [avg_line_NR_ego_tokenized_txt_output_15,  avg_line_NR_ego_tokenized_txt_15]
#                 ]

# occupancy_NR_ego_15 = [[avg_occupancy_NR_ego_adj_json_output_15,    avg_occupancy_NR_ego_adj_json_15],
#                       [avg_occupancy_NR_ego_adj_txt_output_15,           avg_occupancy_NR_ego_adj_txt_15],
#                       [avg_occupancy_NR_ego_jpg_output_15,               avg_occupancy_NR_ego_jpg_15],
#                       [avg_occupancy_NR_ego_json_output_15,              avg_occupancy_NR_ego_json_15],
#                       [avg_occupancy_NR_ego_tokenized_txt_output_15,     avg_occupancy_NR_ego_tokenized_txt_15],
#                     [avg_occupancy_NR_ego_ascii_txt_output_15,         avg_occupancy_NR_ego_ascii_txt_15]
#                       ]


# line_R_ego_15 = [[avg_line_R_ego_adj_json_output_15 - avg_final_line_R_ego_adj_json_15,             avg_line_R_ego_adj_json_15],
#                 [avg_line_R_ego_adj_txt_output_15 - avg_final_line_R_ego_adj_txt_15,                avg_line_R_ego_adj_txt_15],
#                 [avg_line_R_ego_jpg_output_15 - avg_final_line_R_ego_jpg_15,                        avg_line_R_ego_jpg_15],
#                 [avg_line_R_ego_json_output_15 - avg_final_line_R_ego_json_15,                      avg_line_R_ego_json_15],
#                 [avg_line_R_ego_tokenized_txt_output_15 - avg_final_line_R_ego_tokenized_txt_15,   avg_line_R_ego_tokenized_txt_15]
#                 ]

# occupancy_R_ego_15 = [[avg_occupancy_R_ego_adj_json_output_15 - avg_final_occupancy_R_ego_adj_json_15,      avg_occupancy_R_ego_adj_json_15],
#                      [avg_occupancy_R_ego_adj_txt_output_15 - avg_final_occupancy_R_ego_adj_txt_15,            avg_occupancy_R_ego_adj_txt_15],
#                      [avg_occupancy_R_ego_jpg_output_15 - avg_final_occupancy_R_ego_jpg_15,                avg_occupancy_R_ego_jpg_15],
#                      [avg_occupancy_R_ego_json_output_15 - avg_final_occupancy_R_ego_json_15,               avg_occupancy_R_ego_json_15],
#                      [avg_occupancy_R_ego_tokenized_txt_output_15 - avg_final_occupancy_R_ego_tokenized_txt_15,      avg_occupancy_R_ego_tokenized_txt_15],
#                     [avg_occupancy_R_ego_ascii_txt_output_15 - avg_final_occupancy_R_ego_ascii_txt_15,          avg_occupancy_R_ego_ascii_txt_15]
#                      ]



# acc vs tokens: 6 figures ----------------------------------------------------------------------------





# Labels for legend
labels_base = ["Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"]
markers = ['o', 'v', 's', '*', 'D', 'P']
red = ['tomato', 'tomato'] #['red', 'red'] #light, dark
blue = ['dodgerblue', 'dodgerblue']#['blue', 'blue'] #light, dark
green = ['lightgreen', 'lightgreen']#['lime', 'lime'] #light, dark
marker_edge = ['none', 'black'] #line, occupancy
marker_size = [10,10,10]
testx = [1, 2, 3, 4, 5, 6]
testy = [1, 2, 3, 4, 5, 6]
# Create multiple plots in the same figure
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 6), sharex=True, sharey=True)
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 6), sharex=True, sharey=True)

# axes[0,0].plot(testx[0], testy[0], marker='o', color=red[0], label='test 1')
# axes[1,0].plot(testx[1], testy[1], marker='o', color=red[1], label='test 2')
# axes[2,0].plot(testx[2], testy[2], marker='o', color=blue[0], label='test 3')
# axes[0,1].plot(testx[3], testy[3], marker='o', color=blue[1], label='test 4')
# axes[1,1].plot(testx[4], testy[4], marker='o', color=green[0], label='test 5')
# axes[2,1].plot(testx[5], testy[5], marker='o', color=green[1], label=f'test 6')


# Plot 3x3 data with corresponding labels
for i, point in enumerate(line_NR_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Flash-Lite")

for i, point in enumerate(line_NR_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i],  color = green[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(line_NR_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(line_R_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(line_R_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i],  color = green[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(line_R_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Pro")


# Plot 7x7 data with corresponding labels
for i, point in enumerate(occupancy_NR_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_NR_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_NR_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_R_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Pro")

# Plot 6x6 data with corresponding labels
for i, point in enumerate(line_NR_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Coordinates, Gemini 2.5 Flash-Lite")
for i, point in enumerate(line_NR_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Allocentric, Gemini 2.5 Flash-Lite")
for i, point in enumerate(line_NR_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Egocentric, Gemini 2.5 Flash-Lite")
for i, point in enumerate(line_R_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Coordinates, Gemini 2.5 Pro")
for i, point in enumerate(line_R_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Allocentric, Gemini 2.5 Pro")
for i, point in enumerate(line_R_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Egocentric, Gemini 2.5 Pro")

# Plot 13x13 data with corresponding labels
for i, point in enumerate(occupancy_NR_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Coordinates, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_NR_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Allocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_NR_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Egocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_R_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Egocentric, Gemini 2.5 Pro")


    # Plot 15x15 data with corresponding labels
for i, point in enumerate(line_NR_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Coordinates, Gemini 2.5 Flash-Lite")

for i, point in enumerate(line_NR_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Allocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(line_NR_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Egocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(line_R_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(line_R_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(line_R_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Egocentric, Gemini 2.5 Pro")


# Plot 31x31 data with corresponding labels
for i, point in enumerate(occupancy_NR_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Coordinates, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_NR_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Allocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_NR_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Egocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(occupancy_R_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[2,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Egocentric, Gemini 2.5 Pro")


# # Axis labels
for i in range(0,3):
    for j in range(0,2):
        axes[i,j].set_xscale('log')  # Set x-axis to logarithmic scale
        axes[i,j].grid(True, linestyle='--', alpha=0.6)

        # # ylabel placed on all rows
        # axes[i,j].set_ylabel("Completion Score (%)")
        # ylabel placed only once in the figure
        fig.supylabel("Completion Score (%)")
        if figure == 'all_tokens':
            # # xlabel for the figure using ALL tokens, placed on all columns
            # axes[i,j].set_xlabel("Test Compute (Tokens)")
            # xlabel for the figure using ALL tokens, placed once
            fig.supxlabel("Test Compute (Tokens)")
        elif figure == 'final_answer_tokens':
            # # xlabel for the figure using EXCLUSIVELY final answer tokens, placed on all columns
            # axes[i,j].set_xlabel("Final Answer Test Compute (Tokens)")
            # xlabel for the figure using ALL tokens, placed once
            fig.supxlabel("Final Answer Test Compute (Tokens)")
        elif figure == 'thinking_tokens':
            #  # xlabel for the figure using EXCLUSIVELY thinking tokens, placed on all columns
            # axes[i,j].set_xlabel("Thinking Compute (Tokens)")
            # xlabel for the figure using ALL tokens, placed once
            fig.supxlabel("Thinking Compute (Tokens)")




# --- Legend Group Definitions ---
spacer_handle = (
    Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
coord_handle = (
    Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[0], markersize=10),
    # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
)
allo_handle = (
    Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=green[0], markersize=10),
    # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=green[1], markersize=10)
)
ego_handle = (
    Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=blue[0], markersize=10),
    # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=blue[1], markersize=10)
)

pro_handle = (
    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=red[1], markersize=10),
    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=green[1], markersize=10),
    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=blue[1], markersize=10)
)

flashlite_handle = (Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=red[0], markersize=10),
                    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=green[0], markersize=10),
                    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=blue[0], markersize=10)
)

handles = [
    spacer_handle,
    coord_handle,
    allo_handle,
    ego_handle,
    spacer_handle,

    Line2D([], [], marker='o', color='gray', linestyle='None', markersize = 10),  # Adjacency JSON
    Line2D([], [], marker='v', color='gray', linestyle='None', markersize = 10),  # Adjacency Text
    Line2D([], [], marker='s', color='gray', linestyle='None', markersize = 10),  # JPG
    Line2D([], [], marker='*', color='gray', linestyle='None', markersize = 10),  # JSON
    Line2D([], [], marker='D', color='gray', linestyle='None', markersize = 10),  # Tokenized
    Line2D([], [], marker='P', color='gray', linestyle='None', markersize = 10),  # ASCII
    
    # spacer_handle,
    # pro_handle,
    # flashlite_handle,
    # Line2D([], [], marker='o', color='none', markerfacecolor=red[1], markersize=10), # Gemini Pro
    # Line2D([], [], marker='o', color='none', markerfacecolor=red[0], markersize=10), # Gemini Flash Lite

    spacer_handle,  
    Line2D([], [], marker='o', color='none', markerfacecolor='lightgrey', mec=marker_edge[1], markersize = 10),   # Occupancy
    Line2D([], [], marker='o', color='none', markerfacecolor='lightgrey', mec=marker_edge[0], markersize = 10), # Line Wall
]

labels = [
    r"$\bf{Output\ FoRs}$",
    "Coordinates", "Allocentric", "Egocentric",
    r"$\bf{Input\ Formats}$",
    "Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII",
    # r"$\bf{Models}$",
    # "Gemini 2.5 Pro", "Gemini 2.5 Flash-Lite",
    # r"$\bf{Maze\ Styles\ and\ Complexities\ (Low -> High)}$",
    # "Occupancy Grid, 7x7, 13x13, 31x31", "Line Wall, 3x3, 6x6, 15x15"
        r"$\bf{Maze\ Styles}$",
    "Occupancy Grid", "Line Wall"
]

axes[1,1].legend(
    handles,
    labels,
    handler_map={tuple: HandlerTuple(ndivide=None)},
    loc='center left',
    bbox_to_anchor=(1.02, 0.5),
    title="Legend"
)

# Place legend outside the plot on the right
# axes[1,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Representation, Complexity, Output Type, Model")


axes[0,0].set_title("3x3 and 7x7, Gemini 2.5 Flash-Lite")
axes[0,1].set_title("3x3 and 7x7, Gemini 2.5 Pro")
axes[1,0].set_title("6x6 and 13x13, Gemini 2.5 Flash-Lite")
axes[1,1].set_title("6x6 and 13x13, Gemini 2.5 Pro")
axes[2,0].set_title("15x15 and 31x31, Gemini 2.5 Flash-Lite")
axes[2,1].set_title("15x15 and 31x31, Gemini 2.5 Pro")

if figure == 'all_tokens':
    # Title for the figure using ALL tokens
    plt.suptitle("Model Performance as a Function of Test Compute", x=0.48,  fontweight= 'bold')
elif figure == 'final_answer_tokens':
    # Title for the figure using EXCLUSIVELY final answer tokens
    plt.suptitle("Model Performance as a Function of Final Answer Test Compute", x=0.48,  fontweight= 'bold')
elif figure == 'thinking_tokens':
     # Title for the figure using EXCLUSIVELY thinking tokens
    plt.suptitle("Model Performance as a Function of Thinking Compute", x=0.48,  fontweight= 'bold')

plt.tight_layout(rect=[0, 0, 0.97, 1])  # leave 15% of width for legend





plt.show()







print('ratios: completion score / tokens \n')
print('allo adj json 6x6 line', avg_line_R_allo_adj_json_6/avg_line_R_allo_adj_json_output_6,'\n')
print('coords adj json 6x6 line', avg_line_R_coords_adj_json_6/avg_line_R_coords_adj_json_output_6,'\n')
print('coords tokenized 6x6 line', avg_line_R_coords_tokenized_txt_6/avg_line_R_coords_tokenized_txt_output_6,'\n')
print('allo json 6x6 line', avg_line_R_allo_json_6/avg_line_R_allo_json_output_6,'\n')





# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Creating acc/token vs. output type charts for each representation
# # jpg
# line_jpg_NR_3 = np.array([avg_nr_coords_line_jpg_3/avg_nr_coords_line_jpg_output_3, avg_nr_allo_line_jpg_3/avg_nr_allo_line_jpg_output_3, avg_nr_ego_line_jpg_3/avg_nr_ego_line_jpg_output_3])
# line_jpg_R_3 = np.array([avg_r_coords_line_jpg_3/avg_r_coords_line_jpg_output_3, avg_r_allo_line_jpg_3/avg_r_allo_line_jpg_output_3, avg_r_ego_line_jpg_3/avg_r_ego_line_jpg_output_3])

# line_jpg_NR_6 = np.array([avg_nr_coords_line_jpg_6/avg_nr_coords_line_jpg_output_6, avg_nr_allo_line_jpg_6/avg_nr_allo_line_jpg_output_6, avg_nr_ego_line_jpg_6/avg_nr_ego_line_jpg_output_6])
# line_jpg_R_6 = np.array([avg_r_coords_line_jpg_6/avg_r_coords_line_jpg_output_6, avg_r_allo_line_jpg_6/avg_r_allo_line_jpg_output_6, avg_r_ego_line_jpg_6/avg_r_ego_line_jpg_output_6])

# line_jpg_NR_15 = np.array([avg_nr_coords_line_jpg_15/avg_nr_coords_line_jpg_output_15, avg_nr_allo_line_jpg_15/avg_nr_allo_line_jpg_output_15, avg_nr_ego_line_jpg_15/avg_nr_ego_line_jpg_output_15])
# line_jpg_R_15 = np.array([avg_r_coords_line_jpg_15/avg_r_coords_line_jpg_output_15, avg_r_allo_line_jpg_15/avg_r_allo_line_jpg_output_15, avg_r_ego_line_jpg_15/avg_r_ego_line_jpg_output_15])

# occupancy_jpg_NR_3 = np.array([avg_nr_coords_occupancy_jpg_3/avg_nr_coords_occupancy_jpg_output_3, avg_nr_allo_occupancy_jpg_3/avg_nr_allo_occupancy_jpg_output_3, avg_nr_ego_occupancy_jpg_3/avg_nr_ego_occupancy_jpg_output_3])
# occupancy_jpg_R_3 = np.array([avg_r_coords_occupancy_jpg_3/avg_r_coords_occupancy_jpg_output_3, avg_r_allo_occupancy_jpg_3/avg_r_allo_occupancy_jpg_output_3, avg_r_ego_occupancy_jpg_3/avg_r_ego_occupancy_jpg_output_3])

# occupancy_jpg_NR_6 = np.array([avg_nr_coords_occupancy_jpg_6/avg_nr_coords_occupancy_jpg_output_6, avg_nr_allo_occupancy_jpg_6/avg_nr_allo_occupancy_jpg_output_6, avg_nr_ego_occupancy_jpg_6/avg_nr_ego_occupancy_jpg_output_6])
# occupancy_jpg_R_6 = np.array([avg_r_coords_occupancy_jpg_6/avg_r_coords_occupancy_jpg_output_6, avg_r_allo_occupancy_jpg_6/avg_r_allo_occupancy_jpg_output_6, avg_r_ego_occupancy_jpg_6/avg_r_ego_occupancy_jpg_output_6])

# occupancy_jpg_NR_15 = np.array([avg_nr_coords_occupancy_jpg_15/avg_nr_coords_occupancy_jpg_output_15, avg_nr_allo_occupancy_jpg_15/avg_nr_allo_occupancy_jpg_output_15, avg_nr_ego_occupancy_jpg_15/avg_nr_ego_occupancy_jpg_output_15])
# occupancy_jpg_R_15 = np.array([avg_r_coords_occupancy_jpg_15/avg_r_coords_occupancy_jpg_output_15, avg_r_allo_occupancy_jpg_15/avg_r_allo_occupancy_jpg_output_15, avg_r_ego_occupancy_jpg_15/avg_r_ego_occupancy_jpg_output_15])


# # json
# line_json_NR_3 = np.array([avg_nr_coords_line_json_3/avg_nr_coords_line_json_output_3, avg_nr_allo_line_json_3/avg_nr_allo_line_json_output_3, avg_nr_ego_line_json_3/avg_nr_ego_line_json_output_3])
# line_json_R_3 = np.array([avg_r_coords_line_json_3/avg_r_coords_line_json_output_3, avg_r_allo_line_json_3/avg_r_allo_line_json_output_3, avg_r_ego_line_json_3/avg_r_ego_line_json_output_3])

# line_json_NR_6 = np.array([avg_nr_coords_line_json_6/avg_nr_coords_line_json_output_6, avg_nr_allo_line_json_6/avg_nr_allo_line_json_output_6, avg_nr_ego_line_json_6/avg_nr_ego_line_json_output_6])
# line_json_R_6 = np.array([avg_r_coords_line_json_6/avg_r_coords_line_json_output_6, avg_r_allo_line_json_6/avg_r_allo_line_json_output_6, avg_r_ego_line_json_6/avg_r_ego_line_json_output_6])

# line_json_NR_15 = np.array([avg_nr_coords_line_json_15/avg_nr_coords_line_json_output_15, avg_nr_allo_line_json_15/avg_nr_allo_line_json_output_15, avg_nr_ego_line_json_15/avg_nr_ego_line_json_output_15])
# line_json_R_15 = np.array([avg_r_coords_line_json_15/avg_r_coords_line_json_output_15, avg_r_allo_line_json_15/avg_r_allo_line_json_output_15, avg_r_ego_line_json_15/avg_r_ego_line_json_output_15])

# occupancy_json_NR_3 = np.array([avg_nr_coords_occupancy_json_3/avg_nr_coords_occupancy_json_output_3, avg_nr_allo_occupancy_json_3/avg_nr_allo_occupancy_json_output_3, avg_nr_ego_occupancy_json_3/avg_nr_ego_occupancy_json_output_3])
# occupancy_json_R_3 = np.array([avg_r_coords_occupancy_json_3/avg_r_coords_occupancy_json_output_3, avg_r_allo_occupancy_json_3/avg_r_allo_occupancy_json_output_3, avg_r_ego_occupancy_json_3/avg_r_ego_occupancy_json_output_3])

# occupancy_json_NR_6 = np.array([avg_nr_coords_occupancy_json_6/avg_nr_coords_occupancy_json_output_6, avg_nr_allo_occupancy_json_6/avg_nr_allo_occupancy_json_output_6, avg_nr_ego_occupancy_json_6/avg_nr_ego_occupancy_json_output_6])
# occupancy_json_R_6 = np.array([avg_r_coords_occupancy_json_6/avg_r_coords_occupancy_json_output_6, avg_r_allo_occupancy_json_6/avg_r_allo_occupancy_json_output_6, avg_r_ego_occupancy_json_6/avg_r_ego_occupancy_json_output_6])

# occupancy_json_NR_15 = np.array([avg_nr_coords_occupancy_json_15/avg_nr_coords_occupancy_json_output_15, avg_nr_allo_occupancy_json_15/avg_nr_allo_occupancy_json_output_15, avg_nr_ego_occupancy_json_15/avg_nr_ego_occupancy_json_output_15])
# occupancy_json_R_15 = np.array([avg_r_coords_occupancy_json_15/avg_r_coords_occupancy_json_output_15, avg_r_allo_occupancy_json_15/avg_r_allo_occupancy_json_output_15, avg_r_ego_occupancy_json_15/avg_r_ego_occupancy_json_output_15])

# # Tokenized
# line_tokenized_txt_NR_3 = np.array([avg_nr_coords_line_tokenized_txt_3/avg_nr_coords_line_tokenized_txt_output_3, avg_nr_allo_line_tokenized_txt_3/avg_nr_allo_line_tokenized_txt_output_3, avg_nr_ego_line_tokenized_txt_3/avg_nr_ego_line_tokenized_txt_output_3])
# line_tokenized_txt_R_3 = np.array([avg_r_coords_line_tokenized_txt_3/avg_r_coords_line_tokenized_txt_output_3, avg_r_allo_line_tokenized_txt_3/avg_r_allo_line_tokenized_txt_output_3, avg_r_ego_line_tokenized_txt_3/avg_r_ego_line_tokenized_txt_output_3])

# line_tokenized_txt_NR_6 = np.array([avg_nr_coords_line_tokenized_txt_6/avg_nr_coords_line_tokenized_txt_output_6, avg_nr_allo_line_tokenized_txt_6/avg_nr_allo_line_tokenized_txt_output_6, avg_nr_ego_line_tokenized_txt_6/avg_nr_ego_line_tokenized_txt_output_6])
# line_tokenized_txt_R_6 = np.array([avg_r_coords_line_tokenized_txt_6/avg_r_coords_line_tokenized_txt_output_6, avg_r_allo_line_tokenized_txt_6/avg_r_allo_line_tokenized_txt_output_6, avg_r_ego_line_tokenized_txt_6/avg_r_ego_line_tokenized_txt_output_6])

# line_tokenized_txt_NR_15 = np.array([avg_nr_coords_line_tokenized_txt_15/avg_nr_coords_line_tokenized_txt_output_15, avg_nr_allo_line_tokenized_txt_15/avg_nr_allo_line_tokenized_txt_output_15, avg_nr_ego_line_tokenized_txt_15/avg_nr_ego_line_tokenized_txt_output_15])
# line_tokenized_txt_R_15 = np.array([avg_r_coords_line_tokenized_txt_15/avg_r_coords_line_tokenized_txt_output_15, avg_r_allo_line_tokenized_txt_15/avg_r_allo_line_tokenized_txt_output_15, avg_r_ego_line_tokenized_txt_15/avg_r_ego_line_tokenized_txt_output_15])

# occupancy_tokenized_txt_NR_3 = np.array([avg_nr_coords_occupancy_tokenized_txt_3/avg_nr_coords_occupancy_tokenized_txt_output_3, avg_nr_allo_occupancy_tokenized_txt_3/avg_nr_allo_occupancy_tokenized_txt_output_3, avg_nr_ego_occupancy_tokenized_txt_3/avg_nr_ego_occupancy_tokenized_txt_output_3])
# occupancy_tokenized_txt_R_3 = np.array([avg_r_coords_occupancy_tokenized_txt_3/avg_r_coords_occupancy_tokenized_txt_output_3, avg_r_allo_occupancy_tokenized_txt_3/avg_r_allo_occupancy_tokenized_txt_output_3, avg_r_ego_occupancy_tokenized_txt_3/avg_r_ego_occupancy_tokenized_txt_output_3])

# occupancy_tokenized_txt_NR_6 = np.array([avg_nr_coords_occupancy_tokenized_txt_6/avg_nr_coords_occupancy_tokenized_txt_output_6, avg_nr_allo_occupancy_tokenized_txt_6/avg_nr_allo_occupancy_tokenized_txt_output_6, avg_nr_ego_occupancy_tokenized_txt_6/avg_nr_ego_occupancy_tokenized_txt_output_6])
# occupancy_tokenized_txt_R_6 = np.array([avg_r_coords_occupancy_tokenized_txt_6/avg_r_coords_occupancy_tokenized_txt_output_6, avg_r_allo_occupancy_tokenized_txt_6/avg_r_allo_occupancy_tokenized_txt_output_6, avg_r_ego_occupancy_tokenized_txt_6/avg_r_ego_occupancy_tokenized_txt_output_6])

# occupancy_tokenized_txt_NR_15 = np.array([avg_nr_coords_occupancy_tokenized_txt_15/avg_nr_coords_occupancy_tokenized_txt_output_15, avg_nr_allo_occupancy_tokenized_txt_15/avg_nr_allo_occupancy_tokenized_txt_output_15, avg_nr_ego_occupancy_tokenized_txt_15/avg_nr_ego_occupancy_tokenized_txt_output_15])
# occupancy_tokenized_txt_R_15 = np.array([avg_r_coords_occupancy_tokenized_txt_15/avg_r_coords_occupancy_tokenized_txt_output_15, avg_r_allo_occupancy_tokenized_txt_15/avg_r_allo_occupancy_tokenized_txt_output_15, avg_r_ego_occupancy_tokenized_txt_15/avg_r_ego_occupancy_tokenized_txt_output_15])

# # adj json
# line_adj_json_NR_3 = np.array([avg_nr_coords_line_adj_json_3/avg_nr_coords_line_adj_json_output_3, avg_nr_allo_line_adj_json_3/avg_nr_allo_line_adj_json_output_3, avg_nr_ego_line_adj_json_3/avg_nr_ego_line_adj_json_output_3])
# line_adj_json_R_3 = np.array([avg_r_coords_line_adj_json_3/avg_r_coords_line_adj_json_output_3, avg_r_allo_line_adj_json_3/avg_r_allo_line_adj_json_output_3, avg_r_ego_line_adj_json_3/avg_r_ego_line_adj_json_output_3])

# line_adj_json_NR_6 = np.array([avg_nr_coords_line_adj_json_6/avg_nr_coords_line_adj_json_output_6, avg_nr_allo_line_adj_json_6/avg_nr_allo_line_adj_json_output_6, avg_nr_ego_line_adj_json_6/avg_nr_ego_line_adj_json_output_6])
# line_adj_json_R_6 = np.array([avg_r_coords_line_adj_json_6/avg_r_coords_line_adj_json_output_6, avg_r_allo_line_adj_json_6/avg_r_allo_line_adj_json_output_6, avg_r_ego_line_adj_json_6/avg_r_ego_line_adj_json_output_6])

# line_adj_json_NR_15 = np.array([avg_nr_coords_line_adj_json_15/avg_nr_coords_line_adj_json_output_15, avg_nr_allo_line_adj_json_15/avg_nr_allo_line_adj_json_output_15, avg_nr_ego_line_adj_json_15/avg_nr_ego_line_adj_json_output_15])
# line_adj_json_R_15 = np.array([avg_r_coords_line_adj_json_15/avg_r_coords_line_adj_json_output_15, avg_r_allo_line_adj_json_15/avg_r_allo_line_adj_json_output_15, avg_r_ego_line_adj_json_15/avg_r_ego_line_adj_json_output_15])

# occupancy_adj_json_NR_3 = np.array([avg_nr_coords_occupancy_adj_json_3/avg_nr_coords_occupancy_adj_json_output_3, avg_nr_allo_occupancy_adj_json_3/avg_nr_allo_occupancy_adj_json_output_3, avg_nr_ego_occupancy_adj_json_3/avg_nr_ego_occupancy_adj_json_output_3])
# occupancy_adj_json_R_3 = np.array([avg_r_coords_occupancy_adj_json_3/avg_r_coords_occupancy_adj_json_output_3, avg_r_allo_occupancy_adj_json_3/avg_r_allo_occupancy_adj_json_output_3, avg_r_ego_occupancy_adj_json_3/avg_r_ego_occupancy_adj_json_output_3])

# occupancy_adj_json_NR_6 = np.array([avg_nr_coords_occupancy_adj_json_6/avg_nr_coords_occupancy_adj_json_output_6, avg_nr_allo_occupancy_adj_json_6/avg_nr_allo_occupancy_adj_json_output_6, avg_nr_ego_occupancy_adj_json_6/avg_nr_ego_occupancy_adj_json_output_6])
# occupancy_adj_json_R_6 = np.array([avg_r_coords_occupancy_adj_json_6/avg_r_coords_occupancy_adj_json_output_6, avg_r_allo_occupancy_adj_json_6/avg_r_allo_occupancy_adj_json_output_6, avg_r_ego_occupancy_adj_json_6/avg_r_ego_occupancy_adj_json_output_6])

# occupancy_adj_json_NR_15 = np.array([avg_nr_coords_occupancy_adj_json_15/avg_nr_coords_occupancy_adj_json_output_15, avg_nr_allo_occupancy_adj_json_15/avg_nr_allo_occupancy_adj_json_output_15, avg_nr_ego_occupancy_adj_json_15/avg_nr_ego_occupancy_adj_json_output_15])
# occupancy_adj_json_R_15 = np.array([avg_r_coords_occupancy_adj_json_15/avg_r_coords_occupancy_adj_json_output_15, avg_r_allo_occupancy_adj_json_15/avg_r_allo_occupancy_adj_json_output_15, avg_r_ego_occupancy_adj_json_15/avg_r_ego_occupancy_adj_json_output_15])


# # ajd txt
# line_adj_txt_NR_3 = np.array([avg_nr_coords_line_adj_txt_3/avg_nr_coords_line_adj_txt_output_3, avg_nr_allo_line_adj_txt_3/avg_nr_allo_line_adj_txt_output_3, avg_nr_ego_line_adj_txt_3/avg_nr_ego_line_adj_txt_output_3])
# line_adj_txt_R_3 = np.array([avg_r_coords_line_adj_txt_3/avg_r_coords_line_adj_txt_output_3, avg_r_allo_line_adj_txt_3/avg_r_allo_line_adj_txt_output_3, avg_r_ego_line_adj_txt_3/avg_r_ego_line_adj_txt_output_3])

# line_adj_txt_NR_6 = np.array([avg_nr_coords_line_adj_txt_6/avg_nr_coords_line_adj_txt_output_6, avg_nr_allo_line_adj_txt_6/avg_nr_allo_line_adj_txt_output_6, avg_nr_ego_line_adj_txt_6/avg_nr_ego_line_adj_txt_output_6])
# line_adj_txt_R_6 = np.array([avg_r_coords_line_adj_txt_6/avg_r_coords_line_adj_txt_output_6, avg_r_allo_line_adj_txt_6/avg_r_allo_line_adj_txt_output_6, avg_r_ego_line_adj_txt_6/avg_r_ego_line_adj_txt_output_6])

# line_adj_txt_NR_15 = np.array([avg_nr_coords_line_adj_txt_15/avg_nr_coords_line_adj_txt_output_15, avg_nr_allo_line_adj_txt_15/avg_nr_allo_line_adj_txt_output_15, avg_nr_ego_line_adj_txt_15/avg_nr_ego_line_adj_txt_output_15])
# line_adj_txt_R_15 = np.array([avg_r_coords_line_adj_txt_15/avg_r_coords_line_adj_txt_output_15, avg_r_allo_line_adj_txt_15/avg_r_allo_line_adj_txt_output_15, avg_r_ego_line_adj_txt_15/avg_r_ego_line_adj_txt_output_15])

# occupancy_adj_txt_NR_3 = np.array([avg_nr_coords_occupancy_adj_txt_3/avg_nr_coords_occupancy_adj_txt_output_3, avg_nr_allo_occupancy_adj_txt_3/avg_nr_allo_occupancy_adj_txt_output_3, avg_nr_ego_occupancy_adj_txt_3/avg_nr_ego_occupancy_adj_txt_output_3])
# occupancy_adj_txt_R_3 = np.array([avg_r_coords_occupancy_adj_txt_3/avg_r_coords_occupancy_adj_txt_output_3, avg_r_allo_occupancy_adj_txt_3/avg_r_allo_occupancy_adj_txt_output_3, avg_r_ego_occupancy_adj_txt_3/avg_r_ego_occupancy_adj_txt_output_3])

# occupancy_adj_txt_NR_6 = np.array([avg_nr_coords_occupancy_adj_txt_6/avg_nr_coords_occupancy_adj_txt_output_6, avg_nr_allo_occupancy_adj_txt_6/avg_nr_allo_occupancy_adj_txt_output_6, avg_nr_ego_occupancy_adj_txt_6/avg_nr_ego_occupancy_adj_txt_output_6])
# occupancy_adj_txt_R_6 = np.array([avg_r_coords_occupancy_adj_txt_6/avg_r_coords_occupancy_adj_txt_output_6, avg_r_allo_occupancy_adj_txt_6/avg_r_allo_occupancy_adj_txt_output_6, avg_r_ego_occupancy_adj_txt_6/avg_r_ego_occupancy_adj_txt_output_6])

# occupancy_adj_txt_NR_15 = np.array([avg_nr_coords_occupancy_adj_txt_15/avg_nr_coords_occupancy_adj_txt_output_15, avg_nr_allo_occupancy_adj_txt_15/avg_nr_allo_occupancy_adj_txt_output_15, avg_nr_ego_occupancy_adj_txt_15/avg_nr_ego_occupancy_adj_txt_output_15])
# occupancy_adj_txt_R_15 = np.array([avg_r_coords_occupancy_adj_txt_15/avg_r_coords_occupancy_adj_txt_output_15, avg_r_allo_occupancy_adj_txt_15/avg_r_allo_occupancy_adj_txt_output_15, avg_r_ego_occupancy_adj_txt_15/avg_r_ego_occupancy_adj_txt_output_15])

# # Ascii
# occupancy_ascii_txt_NR_3 = np.array([avg_nr_coords_occupancy_ascii_txt_3/avg_nr_coords_occupancy_ascii_txt_output_3, avg_nr_allo_occupancy_ascii_txt_3/avg_nr_allo_occupancy_ascii_txt_output_3, avg_nr_ego_occupancy_ascii_txt_3/avg_nr_ego_occupancy_ascii_txt_output_3])
# occupancy_ascii_txt_R_3 = np.array([avg_r_coords_occupancy_ascii_txt_3/avg_r_coords_occupancy_ascii_txt_output_3, avg_r_allo_occupancy_ascii_txt_3/avg_r_allo_occupancy_ascii_txt_output_3, avg_r_ego_occupancy_ascii_txt_3/avg_r_ego_occupancy_ascii_txt_output_3])

# occupancy_ascii_txt_NR_6 = np.array([avg_nr_coords_occupancy_ascii_txt_6/avg_nr_coords_occupancy_ascii_txt_output_6, avg_nr_allo_occupancy_ascii_txt_6/avg_nr_allo_occupancy_ascii_txt_output_6, avg_nr_ego_occupancy_ascii_txt_6/avg_nr_ego_occupancy_ascii_txt_output_6])
# occupancy_ascii_txt_R_6 = np.array([avg_r_coords_occupancy_ascii_txt_6/avg_r_coords_occupancy_ascii_txt_output_6, avg_r_allo_occupancy_ascii_txt_6/avg_r_allo_occupancy_ascii_txt_output_6, avg_r_ego_occupancy_ascii_txt_6/avg_r_ego_occupancy_ascii_txt_output_6])

# occupancy_ascii_txt_NR_15 = np.array([avg_nr_coords_occupancy_ascii_txt_15/avg_nr_coords_occupancy_ascii_txt_output_15, avg_nr_allo_occupancy_ascii_txt_15/avg_nr_allo_occupancy_ascii_txt_output_15, avg_nr_ego_occupancy_ascii_txt_15/avg_nr_ego_occupancy_ascii_txt_output_15])
# occupancy_ascii_txt_R_15 = np.array([avg_r_coords_occupancy_ascii_txt_15/avg_r_coords_occupancy_ascii_txt_output_15, avg_r_allo_occupancy_ascii_txt_15/avg_r_allo_occupancy_ascii_txt_output_15, avg_r_ego_occupancy_ascii_txt_15/avg_r_ego_occupancy_ascii_txt_output_15])



# jitter_strength = 0.1
# jitter = np.random.uniform(-jitter_strength, jitter_strength, size=10)
# # Create figure with 2 vertical subplots
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(10, 10), sharex=True
# )


# # Top Plot 
# ax1.plot(x_vals+jitter[0], line_jpg_NR_6,  marker='o', color = 'lightcoral', linestyle = 'none', label='JPG, Gemini 2.5 Flash-Lite')
# ax1.plot(x_vals+jitter[1], line_jpg_R_6,   marker='o', color = 'indianred', linestyle = 'none', label='JPG, Gemini 2.5 Pro')
# ax1.plot(x_vals+jitter[2], line_json_NR_6,  marker='o', color = 'deepskyblue',linestyle = 'none', label='JSON Gemini 2.5 Flash-Lite')
# ax1.plot(x_vals+jitter[3], line_json_R_6,   marker='o', color = 'steelblue', linestyle = 'none', label='JSON Gemini 2.5 Pro')
# ax1.plot(x_vals+jitter[4], line_adj_json_NR_6,  marker='o', color = 'orange', linestyle = 'none', label='Adjacency JSON, Gemini 2.5 Flash-Lite')
# ax1.plot(x_vals+jitter[5], line_adj_json_R_6,   marker='o', color = 'darkorange', linestyle = 'none', label='Adjacency JSON, Gemini 2.5 Pro')
# ax1.plot(x_vals+jitter[6], line_adj_txt_NR_6,  marker='o', color = 'limegreen',linestyle = 'none', label='Adjacency Text, Gemini 2.5 Flash-Lite')
# ax1.plot(x_vals+jitter[7], line_adj_txt_R_6,   marker='o', color = 'forestgreen', linestyle = 'none', label='Adjacency Text, Gemini 2.5 Pro')
# ax1.plot(x_vals+jitter[8], line_tokenized_txt_NR_6,  marker='o', color = 'violet', linestyle = 'none', label='Tokenized, Gemini 2.5 Flash-Lite')
# ax1.plot(x_vals+jitter[9], line_tokenized_txt_R_6,   marker='o', color = 'darkviolet', linestyle = 'none', label='Tokenized, Gemini 2.5 Pro')

# ax1.set_ylabel("Average Accuracy /\n Average Output Tokens [%/tokens]")
# ax1.set_title("Contribution of Each Output Token To One Percent Point of Accuracy for Each Output Type\n 6x6 Line Maze")
# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_labels)
# ax1.grid(axis='y', linestyle='--', alpha=0.9)
# # ax1.legend(loc='best')

# bottom_lines = []
# bottom_labels = []

# def add_line(axis, x, y, color, label):
#     h = axis.plot(x, y, marker='o', color=color, linestyle='none', label=label)[0]
#     bottom_lines.append(h)
#     bottom_labels.append(label)


# # Bottom Plot
# ax2.plot(x_vals+jitter[0], occupancy_jpg_NR_6,  marker='o', color = 'lightcoral', linestyle = 'none', label='JPG, Gemini 2.5 Flash-Lite')
# ax2.plot(x_vals+jitter[1], occupancy_jpg_R_6,   marker='o', color = 'indianred', linestyle = 'none', label='JPG, Gemini 2.5 Pro')
# ax2.plot(x_vals+jitter[2], occupancy_json_NR_6,  marker='o', color = 'deepskyblue',linestyle = 'none', label='JSON Gemini 2.5 Flash-Lite')
# ax2.plot(x_vals+jitter[3], occupancy_json_R_6,   marker='o', color = 'steelblue', linestyle = 'none', label='JSON Gemini 2.5 Pro')
# ax2.plot(x_vals+jitter[4], occupancy_adj_json_NR_6,  marker='o', color = 'orange', linestyle = 'none', label='Adjacency JSON, Gemini 2.5 Flash-Lite')
# ax2.plot(x_vals+jitter[5], occupancy_adj_json_R_6,   marker='o', color = 'darkorange', linestyle = 'none', label='Adjacency JSON, Gemini 2.5 Pro')
# ax2.plot(x_vals+jitter[6], occupancy_adj_txt_NR_6,  marker='o', color = 'limegreen',linestyle = 'none', label='Adjacency Text, Gemini 2.5 Flash-Lite')
# ax2.plot(x_vals+jitter[7], occupancy_adj_txt_R_6,   marker='o', color = 'forestgreen', linestyle = 'none', label='Adjacency Text, Gemini 2.5 Pro')
# ax2.plot(x_vals+jitter[8], occupancy_tokenized_txt_NR_6,  marker='o', color = 'violet', linestyle = 'none', label='Tokenized, Gemini 2.5 Flash-Lite')
# ax2.plot(x_vals+jitter[9], occupancy_tokenized_txt_R_6,   marker='o', color = 'darkviolet', linestyle = 'none', label='Tokenized, Gemini 2.5 Pro')
# ax2.plot(x_vals+jitter[8], occupancy_ascii_txt_NR_6,  marker='o', color = 'darkgrey', linestyle = 'none', label='ASCII, Gemini 2.5 Flash-Lite')
# ax2.plot(x_vals+jitter[9], occupancy_ascii_txt_R_6,   marker='o', color = 'dimgrey', linestyle = 'none', label='ASCII, Gemini 2.5 Pro')

# add_line(ax2, x_vals+jitter[0], occupancy_jpg_NR_6, 'lightcoral', 'JPG, Gemini 2.5 Flash-Lite')
# add_line(ax2, x_vals+jitter[1], occupancy_jpg_R_6, 'indianred', 'JPG, Gemini 2.5 Pro')
# add_line(ax2, x_vals+jitter[2], occupancy_json_NR_6, 'deepskyblue', 'JSON Gemini 2.5 Flash-Lite')
# add_line(ax2, x_vals+jitter[3], occupancy_json_R_6, 'steelblue', 'JSON Gemini 2.5 Pro')
# add_line(ax2, x_vals+jitter[4], occupancy_adj_json_NR_6, 'orange', 'Adjacency JSON, Gemini 2.5 Flash-Lite')
# add_line(ax2, x_vals+jitter[5], occupancy_adj_json_R_6, 'darkorange', 'Adjacency JSON, Gemini 2.5 Pro')
# add_line(ax2, x_vals+jitter[6], occupancy_adj_txt_NR_6, 'limegreen', 'Adjacency Text, Gemini 2.5 Flash-Lite')
# add_line(ax2, x_vals+jitter[7], occupancy_adj_txt_R_6, 'forestgreen', 'Adjacency Text, Gemini 2.5 Pro')
# add_line(ax2, x_vals+jitter[8], occupancy_tokenized_txt_NR_6, 'violet', 'Tokenized, Gemini 2.5 Flash-Lite')
# add_line(ax2, x_vals+jitter[9], occupancy_tokenized_txt_R_6, 'darkviolet', 'Tokenized, Gemini 2.5 Pro')
# add_line(ax2, x_vals+jitter[8], occupancy_ascii_txt_NR_6, 'darkgrey', 'ASCII, Gemini 2.5 Flash-Lite')
# add_line(ax2, x_vals+jitter[9], occupancy_ascii_txt_R_6, 'dimgrey', 'ASCII, Gemini 2.5 Pro')



# ax2.set_ylabel("Average Accuracy /\n Average Output Tokens [%/tokens]")
# ax2.set_xlabel("Output Type")
# ax2.set_title("Contribution of Each Output Token To One Percent Point of Accuracy for Each Output Type \n 13x13 Occupancy Maze")
# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_labels)
# ax2.grid(axis='y', linestyle='--', alpha=0.9)
# # ax2.legend(loc='best')

# fig.legend(
#     handles=bottom_lines,
#     labels=bottom_labels,
#     loc='lower right',
#     bbox_to_anchor=(0.98, 0.02),   # adjust for nice spacing
# )

# plt.tight_layout()
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Creating acc vs. output type charts for each representation


# # Line maze accuracy (Pro & Flash-Lite)
# #jpg
# acc_line_jpg_nr_3 = np.array([avg_nr_coords_line_jpg_3, avg_nr_allo_line_jpg_3, avg_nr_ego_line_jpg_3])
# acc_line_jpg_r_3 = np.array([avg_r_coords_line_jpg_3, avg_r_allo_line_jpg_3, avg_r_ego_line_jpg_3])

# acc_line_jpg_nr_6 = np.array([avg_nr_coords_line_jpg_6, avg_nr_allo_line_jpg_6, avg_nr_ego_line_jpg_6])
# acc_line_jpg_r_6 = np.array([avg_r_coords_line_jpg_6, avg_r_allo_line_jpg_6, avg_r_ego_line_jpg_6])

# acc_line_jpg_nr_15 = np.array([avg_nr_coords_line_jpg_15, avg_nr_allo_line_jpg_15, avg_nr_ego_line_jpg_15])
# acc_line_jpg_r_15 = np.array([avg_r_coords_line_jpg_15, avg_r_allo_line_jpg_15, avg_r_ego_line_jpg_15])

# #json
# acc_line_json_nr_3 = np.array([avg_nr_coords_line_json_3, avg_nr_allo_line_json_3, avg_nr_ego_line_json_3])
# acc_line_json_r_3 = np.array([avg_r_coords_line_json_3, avg_r_allo_line_json_3, avg_r_ego_line_json_3])

# acc_line_json_nr_6 = np.array([avg_nr_coords_line_json_6, avg_nr_allo_line_json_6, avg_nr_ego_line_json_6])
# acc_line_json_r_6 = np.array([avg_r_coords_line_json_6, avg_r_allo_line_json_6, avg_r_ego_line_json_6])

# acc_line_json_nr_15 = np.array([avg_nr_coords_line_json_15, avg_nr_allo_line_json_15, avg_nr_ego_line_json_15])
# acc_line_json_r_15 = np.array([avg_r_coords_line_json_15, avg_r_allo_line_json_15, avg_r_ego_line_json_15])

# #tokenized
# acc_line_tokenized_txt_nr_3 = np.array([avg_nr_coords_line_tokenized_txt_3, avg_nr_allo_line_tokenized_txt_3, avg_nr_ego_line_tokenized_txt_3])
# acc_line_tokenized_txt_r_3 = np.array([avg_r_coords_line_tokenized_txt_3, avg_r_allo_line_tokenized_txt_3, avg_r_ego_line_tokenized_txt_3])

# acc_line_tokenized_txt_nr_6 = np.array([avg_nr_coords_line_tokenized_txt_6, avg_nr_allo_line_tokenized_txt_6, avg_nr_ego_line_tokenized_txt_6])
# acc_line_tokenized_txt_r_6 = np.array([avg_r_coords_line_tokenized_txt_6, avg_r_allo_line_tokenized_txt_6, avg_r_ego_line_tokenized_txt_6])

# acc_line_tokenized_txt_nr_15 = np.array([avg_nr_coords_line_tokenized_txt_15, avg_nr_allo_line_tokenized_txt_15, avg_nr_ego_line_tokenized_txt_15])
# acc_line_tokenized_txt_r_15 = np.array([avg_r_coords_line_tokenized_txt_15, avg_r_allo_line_tokenized_txt_15, avg_r_ego_line_tokenized_txt_15])


# #adj json
# acc_line_adj_json_nr_3 = np.array([avg_nr_coords_line_adj_json_3, avg_nr_allo_line_adj_json_3, avg_nr_ego_line_adj_json_3])
# acc_line_adj_json_r_3 = np.array([avg_r_coords_line_adj_json_3, avg_r_allo_line_adj_json_3, avg_r_ego_line_adj_json_3])

# acc_line_adj_json_nr_6 = np.array([avg_nr_coords_line_adj_json_6, avg_nr_allo_line_adj_json_6, avg_nr_ego_line_adj_json_6])
# acc_line_adj_json_r_6 = np.array([avg_r_coords_line_adj_json_6, avg_r_allo_line_adj_json_6, avg_r_ego_line_adj_json_6])

# acc_line_adj_json_nr_15 = np.array([avg_nr_coords_line_adj_json_15, avg_nr_allo_line_adj_json_15, avg_nr_ego_line_adj_json_15])
# acc_line_adj_json_r_15 = np.array([avg_r_coords_line_adj_json_15, avg_r_allo_line_adj_json_15, avg_r_ego_line_adj_json_15])

# #adj txt
# acc_line_adj_txt_nr_3 = np.array([avg_nr_coords_line_adj_txt_3, avg_nr_allo_line_adj_txt_3, avg_nr_ego_line_adj_txt_3])
# acc_line_adj_txt_r_3 = np.array([avg_r_coords_line_adj_txt_3, avg_r_allo_line_adj_txt_3, avg_r_ego_line_adj_txt_3])

# acc_line_adj_txt_nr_6 = np.array([avg_nr_coords_line_adj_txt_6, avg_nr_allo_line_adj_txt_6, avg_nr_ego_line_adj_txt_6])
# acc_line_adj_txt_r_6 = np.array([avg_r_coords_line_adj_txt_6, avg_r_allo_line_adj_txt_6, avg_r_ego_line_adj_txt_6])

# acc_line_adj_txt_nr_15 = np.array([avg_nr_coords_line_adj_txt_15, avg_nr_allo_line_adj_txt_15, avg_nr_ego_line_adj_txt_15])
# acc_line_adj_txt_r_15 = np.array([avg_r_coords_line_adj_txt_15, avg_r_allo_line_adj_txt_15, avg_r_ego_line_adj_txt_15])


# # Occupancy maze accuracy (Pro & Flash-Lite)
# #jpg
# acc_occupancy_jpg_nr_3 = np.array([avg_nr_coords_occupancy_jpg_3, avg_nr_allo_occupancy_jpg_3, avg_nr_ego_occupancy_jpg_3])
# acc_occupancy_jpg_r_3 = np.array([avg_r_coords_occupancy_jpg_3, avg_r_allo_occupancy_jpg_3, avg_r_ego_occupancy_jpg_3])

# acc_occupancy_jpg_nr_6 = np.array([avg_nr_coords_occupancy_jpg_6, avg_nr_allo_occupancy_jpg_6, avg_nr_ego_occupancy_jpg_6])
# acc_occupancy_jpg_r_6 = np.array([avg_r_coords_occupancy_jpg_6, avg_r_allo_occupancy_jpg_6, avg_r_ego_occupancy_jpg_6])

# acc_occupancy_jpg_nr_15 = np.array([avg_nr_coords_occupancy_jpg_15, avg_nr_allo_occupancy_jpg_15, avg_nr_ego_occupancy_jpg_15])
# acc_occupancy_jpg_r_15 = np.array([avg_r_coords_occupancy_jpg_15, avg_r_allo_occupancy_jpg_15, avg_r_ego_occupancy_jpg_15])

# #json
# acc_occupancy_json_nr_3 = np.array([avg_nr_coords_occupancy_json_3, avg_nr_allo_occupancy_json_3, avg_nr_ego_occupancy_json_3])
# acc_occupancy_json_r_3 = np.array([avg_r_coords_occupancy_json_3, avg_r_allo_occupancy_json_3, avg_r_ego_occupancy_json_3])

# acc_occupancy_json_nr_6 = np.array([avg_nr_coords_occupancy_json_6, avg_nr_allo_occupancy_json_6, avg_nr_ego_occupancy_json_6])
# acc_occupancy_json_r_6 = np.array([avg_r_coords_occupancy_json_6, avg_r_allo_occupancy_json_6, avg_r_ego_occupancy_json_6])

# acc_occupancy_json_nr_15 = np.array([avg_nr_coords_occupancy_json_15, avg_nr_allo_occupancy_json_15, avg_nr_ego_occupancy_json_15])
# acc_occupancy_json_r_15 = np.array([avg_r_coords_occupancy_json_15, avg_r_allo_occupancy_json_15, avg_r_ego_occupancy_json_15])

# #tokenized
# acc_occupancy_tokenized_txt_nr_3 = np.array([avg_nr_coords_occupancy_tokenized_txt_3, avg_nr_allo_occupancy_tokenized_txt_3, avg_nr_ego_occupancy_tokenized_txt_3])
# acc_occupancy_tokenized_txt_r_3 = np.array([avg_r_coords_occupancy_tokenized_txt_3, avg_r_allo_occupancy_tokenized_txt_3, avg_r_ego_occupancy_tokenized_txt_3])

# acc_occupancy_tokenized_txt_nr_6 = np.array([avg_nr_coords_occupancy_tokenized_txt_6, avg_nr_allo_occupancy_tokenized_txt_6, avg_nr_ego_occupancy_tokenized_txt_6])
# acc_occupancy_tokenized_txt_r_6 = np.array([avg_r_coords_occupancy_tokenized_txt_6, avg_r_allo_occupancy_tokenized_txt_6, avg_r_ego_occupancy_tokenized_txt_6])

# acc_occupancy_tokenized_txt_nr_15 = np.array([avg_nr_coords_occupancy_tokenized_txt_15, avg_nr_allo_occupancy_tokenized_txt_15, avg_nr_ego_occupancy_tokenized_txt_15])
# acc_occupancy_tokenized_txt_r_15 = np.array([avg_r_coords_occupancy_tokenized_txt_15, avg_r_allo_occupancy_tokenized_txt_15, avg_r_ego_occupancy_tokenized_txt_15])

# #adj json
# acc_occupancy_adj_json_nr_3 = np.array([avg_nr_coords_occupancy_adj_json_3, avg_nr_allo_occupancy_adj_json_3, avg_nr_ego_occupancy_adj_json_3])
# acc_occupancy_adj_json_r_3 = np.array([avg_r_coords_occupancy_adj_json_3, avg_r_allo_occupancy_adj_json_3, avg_r_ego_occupancy_adj_json_3])

# acc_occupancy_adj_json_nr_6 = np.array([avg_nr_coords_occupancy_adj_json_6, avg_nr_allo_occupancy_adj_json_6, avg_nr_ego_occupancy_adj_json_6])
# acc_occupancy_adj_json_r_6 = np.array([avg_r_coords_occupancy_adj_json_6, avg_r_allo_occupancy_adj_json_6, avg_r_ego_occupancy_adj_json_6])

# acc_occupancy_adj_json_nr_15 = np.array([avg_nr_coords_occupancy_adj_json_15, avg_nr_allo_occupancy_adj_json_15, avg_nr_ego_occupancy_adj_json_15])
# acc_occupancy_adj_json_r_15 = np.array([avg_r_coords_occupancy_adj_json_15, avg_r_allo_occupancy_adj_json_15, avg_r_ego_occupancy_adj_json_15])

# #adj txt
# acc_occupancy_adj_txt_nr_3 = np.array([avg_nr_coords_occupancy_adj_txt_3, avg_nr_allo_occupancy_adj_txt_3, avg_nr_ego_occupancy_adj_txt_3])
# acc_occupancy_adj_txt_r_3 = np.array([avg_r_coords_occupancy_adj_txt_3, avg_r_allo_occupancy_adj_txt_3, avg_r_ego_occupancy_adj_txt_3])

# acc_occupancy_adj_txt_nr_6 = np.array([avg_nr_coords_occupancy_adj_txt_6, avg_nr_allo_occupancy_adj_txt_6, avg_nr_ego_occupancy_adj_txt_6])
# acc_occupancy_adj_txt_r_6 = np.array([avg_r_coords_occupancy_adj_txt_6, avg_r_allo_occupancy_adj_txt_6, avg_r_ego_occupancy_adj_txt_6])

# acc_occupancy_adj_txt_nr_15 = np.array([avg_nr_coords_occupancy_adj_txt_15, avg_nr_allo_occupancy_adj_txt_15, avg_nr_ego_occupancy_adj_txt_15])
# acc_occupancy_adj_txt_r_15 = np.array([avg_r_coords_occupancy_adj_txt_15, avg_r_allo_occupancy_adj_txt_15, avg_r_ego_occupancy_adj_txt_15])

# #ascii
# acc_occupancy_ascii_txt_nr_3 = np.array([avg_nr_coords_occupancy_ascii_txt_3, avg_nr_allo_occupancy_ascii_txt_3, avg_nr_ego_occupancy_ascii_txt_3])
# acc_occupancy_ascii_txt_r_3 = np.array([avg_r_coords_occupancy_ascii_txt_3, avg_r_allo_occupancy_ascii_txt_3, avg_r_ego_occupancy_ascii_txt_3])

# acc_occupancy_ascii_txt_nr_6 = np.array([avg_nr_coords_occupancy_ascii_txt_6, avg_nr_allo_occupancy_ascii_txt_6, avg_nr_ego_occupancy_ascii_txt_6])
# acc_occupancy_ascii_txt_r_6 = np.array([avg_r_coords_occupancy_ascii_txt_6, avg_r_allo_occupancy_ascii_txt_6, avg_r_ego_occupancy_ascii_txt_6])

# acc_occupancy_ascii_txt_nr_15 = np.array([avg_nr_coords_occupancy_ascii_txt_15, avg_nr_allo_occupancy_ascii_txt_15, avg_nr_ego_occupancy_ascii_txt_15])
# acc_occupancy_ascii_txt_r_15 = np.array([avg_r_coords_occupancy_ascii_txt_15, avg_r_allo_occupancy_ascii_txt_15, avg_r_ego_occupancy_ascii_txt_15])

# # --------------------------------------------------------


# jitter_strength = 0.01
# jitter = np.random.uniform(-jitter_strength, jitter_strength, size=6)
# Create figure with 2 vertical subplots
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(10, 10), sharex=True
# )

# # Top Plot
# ax1.plot(x_vals+jitter[0], acc_line_jpg_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 3x3")
# ax1.plot(x_vals+jitter[1], acc_line_jpg_r_3,  linestyle = 'dashed',marker='o', color = 'indianred', label="Gemini 2.5 Pro, 3x3")
# ax1.plot(x_vals+jitter[2], acc_line_jpg_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 6x6")
# ax1.plot(x_vals+jitter[3], acc_line_jpg_r_6, linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 6x6")
# ax1.plot(x_vals+jitter[4], acc_line_jpg_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 15x15")
# ax1.plot(x_vals+jitter[5], acc_line_jpg_r_15, linestyle = 'dashed', marker='o', color ='mediumorchid', label="Gemini 2.5 Pro, 15x15")
# ax1.set_ylabel("Average Accuracy [%]")
# ax1.set_title("Accuracy of JPG Line Maze, All Complexities")
# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_labels)
# ax1.grid(axis='y', linestyle='--', alpha=0.9)
# ax1.legend(loc='best')

# # Bottom Plot
# ax2.plot(x_vals+jitter[0], acc_occupancy_jpg_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 7x7")
# ax2.plot(x_vals+jitter[1], acc_occupancy_jpg_r_3,  linestyle = 'dashed', marker='o', color = 'indianred', label="Gemini 2.5 Pro, 7x7")
# ax2.plot(x_vals+jitter[2], acc_occupancy_jpg_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 13x13")
# ax2.plot(x_vals+jitter[3], acc_occupancy_jpg_r_6,  linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 13x13")
# ax2.plot(x_vals+jitter[4], acc_occupancy_jpg_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 31x31")
# ax2.plot(x_vals+jitter[5], acc_occupancy_jpg_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 31x31")


# ax2.set_ylabel("Average Accuracy [%]")
# ax2.set_xlabel("Output Type")
# ax2.set_title("Accuracy of JPG Occupancy Maze, All Complexities")
# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_labels)
# ax2.grid(axis='y', linestyle='--', alpha=0.9)
# ax2.legend(loc='best')
# # ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Create figure with 2 vertical subplots
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(10, 10), sharex=True
# )

# # Top Plot
# ax1.plot(x_vals+jitter[0], acc_line_json_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 3x3")
# ax1.plot(x_vals+jitter[1], acc_line_json_r_3,  linestyle = 'dashed',marker='o', color = 'indianred', label="Gemini 2.5 Pro, 3x3")
# ax1.plot(x_vals+jitter[2], acc_line_json_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 6x6")
# ax1.plot(x_vals+jitter[3], acc_line_json_r_6,  linestyle = 'dashed',marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 6x6")
# ax1.plot(x_vals+jitter[4], acc_line_json_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 15x15")
# ax1.plot(x_vals+jitter[5], acc_line_json_r_15,  linestyle = 'dashed',marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 15x15")

# ax1.set_ylabel("Average Accuracy [%]")
# ax2.set_xlabel("Output Type")
# ax1.set_title("Accuracy of JSON Line Maze, All Complexities")
# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_labels)
# ax1.grid(axis='y', linestyle='--', alpha=0.9)
# ax1.legend(loc='best')

# # Bottom Plot
# ax2.plot(x_vals+jitter[0], acc_occupancy_json_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 7x7")
# ax2.plot(x_vals+jitter[1], acc_occupancy_json_r_3,  linestyle = 'dashed', marker='o', color = 'indianred', label="Gemini 2.5 Pro, 7x7")
# ax2.plot(x_vals+jitter[2], acc_occupancy_json_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 13x13")
# ax2.plot(x_vals+jitter[3], acc_occupancy_json_r_6, linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 13x13")
# ax2.plot(x_vals+jitter[4], acc_occupancy_json_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 31x31")
# ax2.plot(x_vals+jitter[5], acc_occupancy_json_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 31x31")


# ax2.set_ylabel("Average Accuracy [%]")
# ax2.set_xlabel("Output Type")
# ax2.set_title("Accuracy of JSON Occupancy Maze, All Complexities")
# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_labels)
# ax2.grid(axis='y', linestyle='--', alpha=0.9)
# ax2.legend(loc='best')

# # ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Create figure with 2 vertical subplots
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(10, 10), sharex=True
# )

# # Top Plot
# ax1.plot(x_vals+jitter[0], acc_line_tokenized_txt_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 3x3")
# ax1.plot(x_vals+jitter[1], acc_line_tokenized_txt_r_3, linestyle = 'dashed', marker='o', color = 'indianred', label="Gemini 2.5 Pro, 3x3")
# ax1.plot(x_vals+jitter[2], acc_line_tokenized_txt_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 6x6")
# ax1.plot(x_vals+jitter[3], acc_line_tokenized_txt_r_6, linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 6x6")
# ax1.plot(x_vals+jitter[4], acc_line_tokenized_txt_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 15x15")
# ax1.plot(x_vals+jitter[5], acc_line_tokenized_txt_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 15x15")

# ax1.set_ylabel("Average Accuracy [%]")
# ax1.set_title("Accuracy of Tokenized Line Maze, All Complexities")
# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_labels)
# ax1.grid(axis='y', linestyle='--', alpha=0.9)
# ax1.legend(loc='best')

# # Bottom Plot
# ax2.plot(x_vals+jitter[0], acc_occupancy_tokenized_txt_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 7x7")
# ax2.plot(x_vals+jitter[1], acc_occupancy_tokenized_txt_r_3, linestyle = 'dashed', marker='o', color = 'indianred', label="Gemini 2.5 Pro, 7x7")
# ax2.plot(x_vals+jitter[2], acc_occupancy_tokenized_txt_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 13x13")
# ax2.plot(x_vals+jitter[3], acc_occupancy_tokenized_txt_r_6, linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 13x13")
# ax2.plot(x_vals+jitter[4], acc_occupancy_tokenized_txt_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 31x31")
# ax2.plot(x_vals+jitter[5], acc_occupancy_tokenized_txt_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 31x31")


# ax2.set_ylabel("Average Accuracy [%]")
# ax2.set_xlabel("Output Type")
# ax2.set_title("Accuracy of Tokenized Occupancy Maze, All Complexities")
# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_labels)
# ax2.grid(axis='y', linestyle='--', alpha=0.9)
# ax2.legend(loc='best')

# # ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Create figure with 2 vertical subplots
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(10, 10), sharex=True
# )

# # Top Plot
# ax1.plot(x_vals+jitter[0], acc_line_adj_json_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 3x3")
# ax1.plot(x_vals+jitter[1], acc_line_adj_json_r_3, linestyle = 'dashed', marker='o', color = 'indianred', label="Gemini 2.5 Pro, 3x3")
# ax1.plot(x_vals+jitter[2], acc_line_adj_json_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 6x6")
# ax1.plot(x_vals+jitter[3], acc_line_adj_json_r_6, linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 6x6")
# ax1.plot(x_vals+jitter[4], acc_line_adj_json_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 15x15")
# ax1.plot(x_vals+jitter[5], acc_line_adj_json_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 15x15")

# ax1.set_ylabel("Average Accuracy [%]")
# ax1.set_title("Accuracy of Adjacency JSON Line Maze, All Complexities")
# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_labels)
# ax1.grid(axis='y', linestyle='--', alpha=0.9)
# ax1.legend(loc='best')

# # Bottom Plot
# ax2.plot(x_vals+jitter[0], acc_occupancy_adj_json_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 7x7")
# ax2.plot(x_vals+jitter[1], acc_occupancy_adj_json_r_3, linestyle = 'dashed', marker='o', color = 'indianred', label="Gemini 2.5 Pro, 7x7")
# ax2.plot(x_vals+jitter[2], acc_occupancy_adj_json_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 13x13")
# ax2.plot(x_vals+jitter[3], acc_occupancy_adj_json_r_6, linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 13x13")
# ax2.plot(x_vals+jitter[4], acc_occupancy_adj_json_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 31x31")
# ax2.plot(x_vals+jitter[5], acc_occupancy_adj_json_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 31x31")


# ax2.set_ylabel("Average Accuracy [%]")
# ax2.set_xlabel("Output Type")
# ax2.set_title("Accuracy of Adjacency JSON Occupancy Maze, All Complexities")
# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_labels)
# ax2.grid(axis='y', linestyle='--', alpha=0.9)
# ax2.legend(loc='best')


# # ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Create figure with 2 vertical subplots
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1, figsize=(10, 10), sharex=True
# )

# # Top Plot
# ax1.plot(x_vals+jitter[0], acc_line_adj_txt_nr_3,   marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 3x3")
# ax1.plot(x_vals+jitter[1], acc_line_adj_txt_r_3, linestyle = 'dashed', marker='o', color = 'indianred', label="Gemini 2.5 Pro, 3x3")
# ax1.plot(x_vals+jitter[2], acc_line_adj_txt_nr_6,   marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 6x6")
# ax1.plot(x_vals+jitter[3], acc_line_adj_txt_r_6, linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 6x6")
# ax1.plot(x_vals+jitter[4], acc_line_adj_txt_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 15x15")
# ax1.plot(x_vals+jitter[5], acc_line_adj_txt_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 15x15")

# ax1.set_ylabel("Average Accuracy [%]")
# ax1.set_title("Accuracy of Adjacency Text Line Maze, All Complexities")
# ax1.set_xticks(x_vals)
# ax1.set_xticklabels(x_labels)
# ax1.grid(axis='y', linestyle='--', alpha=0.9)
# ax1.legend(loc='best')

# # Bottom Plot
# ax2.plot(x_vals+jitter[0], acc_occupancy_adj_txt_nr_3,    marker='o', color = 'lightcoral', label="Gemini 2.5 Flash-Lite, 7x7")
# ax2.plot(x_vals+jitter[1], acc_occupancy_adj_txt_r_3,  linestyle = 'dashed',marker='o', color = 'indianred', label="Gemini 2.5 Pro, 7x7")
# ax2.plot(x_vals+jitter[2], acc_occupancy_adj_txt_nr_6,  marker='o', color = 'palegreen', label="Gemini 2.5 Flash-Lite, 13x13")
# ax2.plot(x_vals+jitter[3], acc_occupancy_adj_txt_r_6,  linestyle = 'dashed', marker='o', color = 'darkseagreen', label="Gemini 2.5 Pro, 13x13")
# ax2.plot(x_vals+jitter[4], acc_occupancy_adj_txt_nr_15,   marker='o', color = 'violet', label="Gemini 2.5 Flash-Lite, 31x31")
# ax2.plot(x_vals+jitter[5], acc_occupancy_adj_txt_r_15, linestyle = 'dashed', marker='o', color = 'mediumorchid', label="Gemini 2.5 Pro, 31x31")


# ax2.set_ylabel("Average Accuracy [%]")
# ax2.set_xlabel("Output Type")
# ax2.set_title("Average Accuracy of Adjacency Text Occupancy Maze, All Complexities")
# ax2.set_xticks(x_vals)
# ax2.set_xticklabels(x_labels)
# ax2.grid(axis='y', linestyle='--', alpha=0.9)
# ax2.legend(loc='best')



# plt.tight_layout()  # leave space on the right
# plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# plt.figure(figsize=(10, 6))

# # --- Occupancy Maze (asciii) ---
# plt.plot(x_vals+jitter[0], acc_occupancy_ascii_txt_nr_3,   marker='s', color = 'lightcoral', label="Occupancy, Flash-Lite, 7x7")
# plt.plot(x_vals+jitter[1], acc_occupancy_ascii_txt_r_3, linestyle = 'dashed',    marker='s', color = 'indianred', label="Occupancy, Pro, 7x7")
# plt.plot(x_vals+jitter[2], acc_occupancy_ascii_txt_nr_6,   marker='s', color = 'palegreen', label="Occupancy, Flash-Lite, 13x13")
# plt.plot(x_vals+jitter[3], acc_occupancy_ascii_txt_r_6,  linestyle = 'dashed',   marker='s', color = 'darkseagreen', label="Occupancy, Pro, 13x13")
# plt.plot(x_vals+jitter[4], acc_occupancy_ascii_txt_nr_15,  marker='s', color = 'violet', label="Occupancy, Flash-Lite, 31x31")
# plt.plot(x_vals+jitter[5], acc_occupancy_ascii_txt_r_15, linestyle = 'dashed',   marker='s', color = 'mediumorchid', label="Occupancy, Pro, 31x31")

# # --- Axes labels & ticks ---
# plt.ylabel("Average Accuracy [%]")
# plt.xlabel("Output Type")
# plt.xticks(x_vals, x_labels)

# # --- Title (combined) ---
# plt.title("Accuracy of Ascii Occupancy Maze,\nAll Complexities")

# # --- Aesthetics ---
# plt.grid(axis='y', linestyle='--', alpha=0.9)
# plt.legend(loc='best')

# plt.tight_layout()
# plt.show()

