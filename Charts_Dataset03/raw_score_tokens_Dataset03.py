# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataframe_image as dfi
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple, HandlerBase
from matplotlib import rcParams
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15





# 3x3 NR - COORDS ----------------------------------------------------------------
# 3x3 raw score averages
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
# 3x3 token output averages
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


# 3x3 NR - ALLO ----------------------------------------------------------------
# 3x3 raw score averages
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

# 3x3 token output averages
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


# 3x3 NR - EGO ----------------------------------------------------------------
# 3x3 raw score averages
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
# 3x3 output token averages
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


# 3x3 R - COORDS ----------------------------------------------------------------
# 3x3 raw score averages
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
# 3x3 output tokens averages
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

# 3x3 R - ALLO ----------------------------------------------------------------
# 3x3 raw score averages
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
# 3x3 output token averages
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



# 3x3 R - EGO ----------------------------------------------------------------
# 3x3 raw score averages
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
# 3x3 output tokens averages
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


# -----------------------------------------------------------------------------------------------------------------------------------



# 6x6 NR - COORDS ----------------------------------------------------------------
# 6x6 raw score averages
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
# 6x6 output tokens averages
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


# 6x6 NR - ALLO ----------------------------------------------------------------
#6x6 raw score averages
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
# 6x6 output tokens averages
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

# 6x6 NR - EGO ----------------------------------------------------------------
#6x6 raw score averages
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
# 6x6 output tokens averages
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

# 6x6 R - COORDS ----------------------------------------------------------------
# 6x6 raw scores averages
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
# 6x6 Output Tokens averages
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

# 6x6 R - ALLO ----------------------------------------------------------------
# 6x6 raw scores averages
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
# 6x6 output tokens averages
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

# 6x6 - R EGO ----------------------------------------------------------------
#6x6 raw scores averages
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
# 6x6 output tokens averages
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


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 15x15 NR - COORDS ----------------------------------------------------------------
# 15x15 raw scores averages
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
# 15x15 output tokens averages
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




# 15x15 NR - ALLO ----------------------------------------------------------------
# 15x15 raw score averages
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
# 15x15 output tokens averages
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



# 15x15 NR - EGO ----------------------------------------------------------------
# 15x15 raw scores averages
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
# 15x15 output tokens averages
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


# 15x15 R - COORDS ----------------------------------------------------------------
# 15x15 raw scores averages
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
# 15x15 output tokens averages
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


# 15x15 R - ALLO ----------------------------------------------------------------
# 15x15 raw scores averages
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
# 15x15 output tokens averages
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


# 15x15 R - EGO ----------------------------------------------------------------
# 15x15 raw scores averages
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
# 15x15 output tokens averages
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





# Creating an acc vs token output plot ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Creating data for plotting
line_NR_coords_3 = [[avg_line_NR_coords_adj_json_output_3,      avg_line_NR_coords_adj_json_raw_score_3],
                   [avg_line_NR_coords_adj_txt_output_3,        avg_line_NR_coords_adj_txt_raw_score_3],
                   [avg_line_NR_coords_jpg_output_3,            avg_line_NR_coords_jpg_raw_score_3],
                   [avg_line_NR_coords_json_output_3,           avg_line_NR_coords_json_raw_score_3],
                   [avg_line_NR_coords_tokenized_txt_output_3,  avg_line_NR_coords_tokenized_txt_raw_score_3]
                   ]

occupancy_NR_coords_3 = [[avg_occupancy_NR_coords_adj_json_output_3,    avg_occupancy_NR_coords_adj_json_raw_score_3],
                         [avg_occupancy_NR_coords_adj_txt_output_3,           avg_occupancy_NR_coords_adj_txt_raw_score_3],
                         [avg_occupancy_NR_coords_jpg_output_3,               avg_occupancy_NR_coords_jpg_raw_score_3],
                         [avg_occupancy_NR_coords_json_output_3,              avg_occupancy_NR_coords_json_raw_score_3],
                         [avg_occupancy_NR_coords_tokenized_txt_output_3,     avg_occupancy_NR_coords_tokenized_txt_raw_score_3],
                         [avg_occupancy_NR_coords_ascii_txt_output_3,        avg_occupancy_NR_coords_ascii_txt_raw_score_3]
                         ]


line_R_coords_3 = [[avg_line_R_coords_adj_json_output_3,        avg_line_R_coords_adj_json_raw_score_3],
                   [avg_line_R_coords_adj_txt_output_3,         avg_line_R_coords_adj_txt_raw_score_3],
                   [avg_line_R_coords_jpg_output_3,             avg_line_R_coords_jpg_raw_score_3],
                   [avg_line_R_coords_json_output_3,            avg_line_R_coords_json_raw_score_3],
                   [avg_line_R_coords_tokenized_txt_output_3,   avg_line_R_coords_tokenized_txt_raw_score_3]
                   ]

occupancy_R_coords_3 = [[avg_occupancy_R_coords_adj_json_output_3,      avg_occupancy_R_coords_adj_json_raw_score_3],
                        [avg_occupancy_R_coords_adj_txt_output_3,            avg_occupancy_R_coords_adj_txt_raw_score_3],
                        [avg_occupancy_R_coords_jpg_output_3,                avg_occupancy_R_coords_jpg_raw_score_3],
                        [avg_occupancy_R_coords_json_output_3,               avg_occupancy_R_coords_json_raw_score_3],
                        [avg_occupancy_R_coords_tokenized_txt_output_3,      avg_occupancy_R_coords_tokenized_txt_raw_score_3],
                        [avg_occupancy_R_coords_ascii_txt_output_3,         avg_occupancy_R_coords_ascii_txt_raw_score_3]
                        ]
                    
line_NR_allo_3 = [[avg_line_NR_allo_adj_json_output_3,      avg_line_NR_allo_adj_json_raw_score_3],
                  [avg_line_NR_allo_adj_txt_output_3,        avg_line_NR_allo_adj_txt_raw_score_3],
                  [avg_line_NR_allo_jpg_output_3,            avg_line_NR_allo_jpg_raw_score_3],
                  [avg_line_NR_allo_json_output_3,           avg_line_NR_allo_json_raw_score_3],
                  [avg_line_NR_allo_tokenized_txt_output_3,  avg_line_NR_allo_tokenized_txt_raw_score_3]
                  ]

occupancy_NR_allo_3 = [[avg_occupancy_NR_allo_adj_json_output_3,    avg_occupancy_NR_allo_adj_json_raw_score_3],
                       [avg_occupancy_NR_allo_adj_txt_output_3,           avg_occupancy_NR_allo_adj_txt_raw_score_3],
                       [avg_occupancy_NR_allo_jpg_output_3,               avg_occupancy_NR_allo_jpg_raw_score_3],
                       [avg_occupancy_NR_allo_json_output_3,              avg_occupancy_NR_allo_json_raw_score_3],
                       [avg_occupancy_NR_allo_tokenized_txt_output_3,     avg_occupancy_NR_allo_tokenized_txt_raw_score_3],
                       [avg_occupancy_NR_allo_ascii_txt_output_3,        avg_occupancy_NR_allo_ascii_txt_raw_score_3]
                       ]


line_R_allo_3 = [[avg_line_R_allo_adj_json_output_3,        avg_line_R_allo_adj_json_raw_score_3],
                [avg_line_R_allo_adj_txt_output_3,         avg_line_R_allo_adj_txt_raw_score_3],
                [avg_line_R_allo_jpg_output_3,             avg_line_R_allo_jpg_raw_score_3],
                [avg_line_R_allo_json_output_3,            avg_line_R_allo_json_raw_score_3],
                [avg_line_R_allo_tokenized_txt_output_3,   avg_line_R_allo_tokenized_txt_raw_score_3]
                ]

occupancy_R_allo_3 = [[avg_occupancy_R_allo_adj_json_output_3,          avg_occupancy_R_allo_adj_json_raw_score_3],
                      [avg_occupancy_R_allo_adj_txt_output_3,           avg_occupancy_R_allo_adj_txt_raw_score_3],
                      [avg_occupancy_R_allo_jpg_output_3,               avg_occupancy_R_allo_jpg_raw_score_3],
                      [avg_occupancy_R_allo_json_output_3,              avg_occupancy_R_allo_json_raw_score_3],
                      [avg_occupancy_R_allo_tokenized_txt_output_3,     avg_occupancy_R_allo_tokenized_txt_raw_score_3],
                      [avg_occupancy_R_allo_ascii_txt_output_3,         avg_occupancy_R_allo_ascii_txt_raw_score_3]
                      ]
                    
line_NR_ego_3 = [[avg_line_NR_ego_adj_json_output_3,      avg_line_NR_ego_adj_json_raw_score_3],
                [avg_line_NR_ego_adj_txt_output_3,        avg_line_NR_ego_adj_txt_raw_score_3],
                [avg_line_NR_ego_jpg_output_3,            avg_line_NR_ego_jpg_raw_score_3],
                [avg_line_NR_ego_json_output_3,           avg_line_NR_ego_json_raw_score_3],
                [avg_line_NR_ego_tokenized_txt_output_3,  avg_line_NR_ego_tokenized_txt_raw_score_3]
                ]

occupancy_NR_ego_3 = [[avg_occupancy_NR_ego_adj_json_output_3,          avg_occupancy_NR_ego_adj_json_raw_score_3],
                      [avg_occupancy_NR_ego_adj_txt_output_3,           avg_occupancy_NR_ego_adj_txt_raw_score_3],
                      [avg_occupancy_NR_ego_jpg_output_3,               avg_occupancy_NR_ego_jpg_raw_score_3],
                      [avg_occupancy_NR_ego_json_output_3,              avg_occupancy_NR_ego_json_raw_score_3],
                      [avg_occupancy_NR_ego_tokenized_txt_output_3,     avg_occupancy_NR_ego_tokenized_txt_raw_score_3],
                      [avg_occupancy_NR_ego_ascii_txt_output_3,         avg_occupancy_NR_ego_ascii_txt_raw_score_3]
                      ]


line_R_ego_3 = [[avg_line_R_ego_adj_json_output_3,        avg_line_R_ego_adj_json_raw_score_3],
                [avg_line_R_ego_adj_txt_output_3,         avg_line_R_ego_adj_txt_raw_score_3],
                [avg_line_R_ego_jpg_output_3,             avg_line_R_ego_jpg_raw_score_3],
                [avg_line_R_ego_json_output_3,            avg_line_R_ego_json_raw_score_3],
                [avg_line_R_ego_tokenized_txt_output_3,   avg_line_R_ego_tokenized_txt_raw_score_3]
                ]

occupancy_R_ego_3 = [[avg_occupancy_R_ego_adj_json_output_3,      avg_occupancy_R_ego_adj_json_raw_score_3],
                     [avg_occupancy_R_ego_adj_txt_output_3,            avg_occupancy_R_ego_adj_txt_raw_score_3],
                     [avg_occupancy_R_ego_jpg_output_3,                avg_occupancy_R_ego_jpg_raw_score_3],
                     [avg_occupancy_R_ego_json_output_3,               avg_occupancy_R_ego_json_raw_score_3],
                     [avg_occupancy_R_ego_tokenized_txt_output_3,      avg_occupancy_R_ego_tokenized_txt_raw_score_3],
                     [avg_occupancy_R_ego_ascii_txt_output_3,          avg_occupancy_R_ego_ascii_txt_raw_score_3]
                     ]
                    


line_NR_coords_6 = [[avg_line_NR_coords_adj_json_output_6,      avg_line_NR_coords_adj_json_raw_score_6],
                   [avg_line_NR_coords_adj_txt_output_6,        avg_line_NR_coords_adj_txt_raw_score_6],
                   [avg_line_NR_coords_jpg_output_6,            avg_line_NR_coords_jpg_raw_score_6],
                   [avg_line_NR_coords_json_output_6,           avg_line_NR_coords_json_raw_score_6],
                   [avg_line_NR_coords_tokenized_txt_output_6,  avg_line_NR_coords_tokenized_txt_raw_score_6]
                   ]

occupancy_NR_coords_6 = [[avg_occupancy_NR_coords_adj_json_output_6,    avg_occupancy_NR_coords_adj_json_raw_score_6],
                         [avg_occupancy_NR_coords_adj_txt_output_6,           avg_occupancy_NR_coords_adj_txt_raw_score_6],
                         [avg_occupancy_NR_coords_jpg_output_6,               avg_occupancy_NR_coords_jpg_raw_score_6],
                         [avg_occupancy_NR_coords_json_output_6,              avg_occupancy_NR_coords_json_raw_score_6],
                         [avg_occupancy_NR_coords_tokenized_txt_output_6,     avg_occupancy_NR_coords_tokenized_txt_raw_score_6],
                         [avg_occupancy_NR_coords_ascii_txt_output_6,         avg_occupancy_NR_coords_ascii_txt_raw_score_6]
                         ]


line_R_coords_6 = [[avg_line_R_coords_adj_json_output_6,        avg_line_R_coords_adj_json_raw_score_6],
                   [avg_line_R_coords_adj_txt_output_6,         avg_line_R_coords_adj_txt_raw_score_6],
                   [avg_line_R_coords_jpg_output_6,             avg_line_R_coords_jpg_raw_score_6],
                   [avg_line_R_coords_json_output_6,            avg_line_R_coords_json_raw_score_6],
                   [avg_line_R_coords_tokenized_txt_output_6,   avg_line_R_coords_tokenized_txt_raw_score_6]
                   ]

occupancy_R_coords_6 = [[avg_occupancy_R_coords_adj_json_output_6,      avg_occupancy_R_coords_adj_json_raw_score_6],
                        [avg_occupancy_R_coords_adj_txt_output_6,            avg_occupancy_R_coords_adj_txt_raw_score_6],
                        [avg_occupancy_R_coords_jpg_output_6,                avg_occupancy_R_coords_jpg_raw_score_6],
                        [avg_occupancy_R_coords_json_output_6,               avg_occupancy_R_coords_json_raw_score_6],
                        [avg_occupancy_R_coords_tokenized_txt_output_6,      avg_occupancy_R_coords_tokenized_txt_raw_score_6],
                        [avg_occupancy_R_coords_ascii_txt_output_6,         avg_occupancy_R_coords_ascii_txt_raw_score_6]
                        ]
                    
line_NR_allo_6 = [[avg_line_NR_allo_adj_json_output_6,      avg_line_NR_allo_adj_json_raw_score_6],
                  [avg_line_NR_allo_adj_txt_output_6,        avg_line_NR_allo_adj_txt_raw_score_6],
                  [avg_line_NR_allo_jpg_output_6,            avg_line_NR_allo_jpg_raw_score_6],
                  [avg_line_NR_allo_json_output_6,           avg_line_NR_allo_json_raw_score_6],
                  [avg_line_NR_allo_tokenized_txt_output_6,  avg_line_NR_allo_tokenized_txt_raw_score_6]
                  ]

occupancy_NR_allo_6 = [[avg_occupancy_NR_allo_adj_json_output_6,    avg_occupancy_NR_allo_adj_json_raw_score_6],
                       [avg_occupancy_NR_allo_adj_txt_output_6,           avg_occupancy_NR_allo_adj_txt_raw_score_6],
                       [avg_occupancy_NR_allo_jpg_output_6,               avg_occupancy_NR_allo_jpg_raw_score_6],
                       [avg_occupancy_NR_allo_json_output_6,              avg_occupancy_NR_allo_json_raw_score_6],
                       [avg_occupancy_NR_allo_tokenized_txt_output_6,     avg_occupancy_NR_allo_tokenized_txt_raw_score_6],
                       [avg_occupancy_NR_allo_ascii_txt_output_6,        avg_occupancy_NR_allo_ascii_txt_raw_score_6]   
                       ]


line_R_allo_6 = [[avg_line_R_allo_adj_json_output_6,        avg_line_R_allo_adj_json_raw_score_6],
                [avg_line_R_allo_adj_txt_output_6,         avg_line_R_allo_adj_txt_raw_score_6],
                [avg_line_R_allo_jpg_output_6,             avg_line_R_allo_jpg_raw_score_6],
                [avg_line_R_allo_json_output_6,            avg_line_R_allo_json_raw_score_6],
                [avg_line_R_allo_tokenized_txt_output_6,   avg_line_R_allo_tokenized_txt_raw_score_6]
                ]

occupancy_R_allo_6 = [[avg_occupancy_R_allo_adj_json_output_6,      avg_occupancy_R_allo_adj_json_raw_score_6],
                      [avg_occupancy_R_allo_adj_txt_output_6,            avg_occupancy_R_allo_adj_txt_raw_score_6],
                      [avg_occupancy_R_allo_jpg_output_6,                avg_occupancy_R_allo_jpg_raw_score_6],
                      [avg_occupancy_R_allo_json_output_6,               avg_occupancy_R_allo_json_raw_score_6],
                      [avg_occupancy_R_allo_tokenized_txt_output_6,      avg_occupancy_R_allo_tokenized_txt_raw_score_6],
                      [avg_occupancy_R_allo_ascii_txt_output_6,          avg_occupancy_R_allo_ascii_txt_raw_score_6]
                      ]
                    
line_NR_ego_6 = [[avg_line_NR_ego_adj_json_output_6,      avg_line_NR_ego_adj_json_raw_score_6],
                [avg_line_NR_ego_adj_txt_output_6,        avg_line_NR_ego_adj_txt_raw_score_6],
                [avg_line_NR_ego_jpg_output_6,            avg_line_NR_ego_jpg_raw_score_6],
                [avg_line_NR_ego_json_output_6,           avg_line_NR_ego_json_raw_score_6],
                [avg_line_NR_ego_tokenized_txt_output_6,  avg_line_NR_ego_tokenized_txt_raw_score_6]
                ]

occupancy_NR_ego_6 = [[avg_occupancy_NR_ego_adj_json_output_6,    avg_occupancy_NR_ego_adj_json_raw_score_6],
                      [avg_occupancy_NR_ego_adj_txt_output_6,           avg_occupancy_NR_ego_adj_txt_raw_score_6],
                      [avg_occupancy_NR_ego_jpg_output_6,               avg_occupancy_NR_ego_jpg_raw_score_6],
                      [avg_occupancy_NR_ego_json_output_6,              avg_occupancy_NR_ego_json_raw_score_6],
                      [avg_occupancy_NR_ego_tokenized_txt_output_6,     avg_occupancy_NR_ego_tokenized_txt_raw_score_6],
                        [avg_occupancy_NR_ego_ascii_txt_output_6,         avg_occupancy_NR_ego_ascii_txt_raw_score_6]
                      ]


line_R_ego_6 = [[avg_line_R_ego_adj_json_output_6,        avg_line_R_ego_adj_json_raw_score_6],
                [avg_line_R_ego_adj_txt_output_6,         avg_line_R_ego_adj_txt_raw_score_6],
                [avg_line_R_ego_jpg_output_6,             avg_line_R_ego_jpg_raw_score_6],
                [avg_line_R_ego_json_output_6,            avg_line_R_ego_json_raw_score_6],
                [avg_line_R_ego_tokenized_txt_output_6,   avg_line_R_ego_tokenized_txt_raw_score_6]
                ]

occupancy_R_ego_6 = [[avg_occupancy_R_ego_adj_json_output_6,      avg_occupancy_R_ego_adj_json_raw_score_6],
                     [avg_occupancy_R_ego_adj_txt_output_6,            avg_occupancy_R_ego_adj_txt_raw_score_6],
                     [avg_occupancy_R_ego_jpg_output_6,                avg_occupancy_R_ego_jpg_raw_score_6],
                     [avg_occupancy_R_ego_json_output_6,               avg_occupancy_R_ego_json_raw_score_6],
                     [avg_occupancy_R_ego_tokenized_txt_output_6,      avg_occupancy_R_ego_tokenized_txt_raw_score_6],
                    [avg_occupancy_R_ego_ascii_txt_output_6,          avg_occupancy_R_ego_ascii_txt_raw_score_6]
                     ]
                    



line_NR_coords_15 = [[avg_line_NR_coords_adj_json_output_15,      avg_line_NR_coords_adj_json_raw_score_15],
                   [avg_line_NR_coords_adj_txt_output_15,        avg_line_NR_coords_adj_txt_raw_score_15],
                   [avg_line_NR_coords_jpg_output_15,            avg_line_NR_coords_jpg_raw_score_15],
                   [avg_line_NR_coords_json_output_15,           avg_line_NR_coords_json_raw_score_15],
                   [avg_line_NR_coords_tokenized_txt_output_15,  avg_line_NR_coords_tokenized_txt_raw_score_15]
                   ]

occupancy_NR_coords_15 = [[avg_occupancy_NR_coords_adj_json_output_15,    avg_occupancy_NR_coords_adj_json_raw_score_15],
                         [avg_occupancy_NR_coords_adj_txt_output_15,           avg_occupancy_NR_coords_adj_txt_raw_score_15],
                         [avg_occupancy_NR_coords_jpg_output_15,               avg_occupancy_NR_coords_jpg_raw_score_15],
                         [avg_occupancy_NR_coords_json_output_15,              avg_occupancy_NR_coords_json_raw_score_15],
                         [avg_occupancy_NR_coords_tokenized_txt_output_15,     avg_occupancy_NR_coords_tokenized_txt_raw_score_15],
                        [avg_occupancy_NR_coords_ascii_txt_output_15,         avg_occupancy_NR_coords_ascii_txt_raw_score_15]
                         ]


line_R_coords_15 = [[avg_line_R_coords_adj_json_output_15,        avg_line_R_coords_adj_json_raw_score_15],
                   [avg_line_R_coords_adj_txt_output_15,         avg_line_R_coords_adj_txt_raw_score_15],
                   [avg_line_R_coords_jpg_output_15,             avg_line_R_coords_jpg_raw_score_15],
                   [avg_line_R_coords_json_output_15,            avg_line_R_coords_json_raw_score_15],
                   [avg_line_R_coords_tokenized_txt_output_15,   avg_line_R_coords_tokenized_txt_raw_score_15]
                   ]

occupancy_R_coords_15 = [[avg_occupancy_R_coords_adj_json_output_15,      avg_occupancy_R_coords_adj_json_raw_score_15],
                        [avg_occupancy_R_coords_adj_txt_output_15,            avg_occupancy_R_coords_adj_txt_raw_score_15],
                        [avg_occupancy_R_coords_jpg_output_15,                avg_occupancy_R_coords_jpg_raw_score_15],
                        [avg_occupancy_R_coords_json_output_15,               avg_occupancy_R_coords_json_raw_score_15],
                        [avg_occupancy_R_coords_tokenized_txt_output_15,      avg_occupancy_R_coords_tokenized_txt_raw_score_15],
                        [avg_occupancy_R_coords_ascii_txt_output_15,         avg_occupancy_R_coords_ascii_txt_raw_score_15]
                        ]
                    
line_NR_allo_15 = [[avg_line_NR_allo_adj_json_output_15,      avg_line_NR_allo_adj_json_raw_score_15],
                  [avg_line_NR_allo_adj_txt_output_15,        avg_line_NR_allo_adj_txt_raw_score_15],
                  [avg_line_NR_allo_jpg_output_15,            avg_line_NR_allo_jpg_raw_score_15],
                  [avg_line_NR_allo_json_output_15,           avg_line_NR_allo_json_raw_score_15],
                  [avg_line_NR_allo_tokenized_txt_output_15,  avg_line_NR_allo_tokenized_txt_raw_score_15]
                  ]

occupancy_NR_allo_15 = [[avg_occupancy_NR_allo_adj_json_output_15,    avg_occupancy_NR_allo_adj_json_raw_score_15],
                       [avg_occupancy_NR_allo_adj_txt_output_15,           avg_occupancy_NR_allo_adj_txt_raw_score_15],
                       [avg_occupancy_NR_allo_jpg_output_15,               avg_occupancy_NR_allo_jpg_raw_score_15],
                       [avg_occupancy_NR_allo_json_output_15,              avg_occupancy_NR_allo_json_raw_score_15],
                       [avg_occupancy_NR_allo_tokenized_txt_output_15,     avg_occupancy_NR_allo_tokenized_txt_raw_score_15],
                        [avg_occupancy_NR_allo_ascii_txt_output_15,        avg_occupancy_NR_allo_ascii_txt_raw_score_15]
                       ]


line_R_allo_15 = [[avg_line_R_allo_adj_json_output_15,        avg_line_R_allo_adj_json_raw_score_15],
                [avg_line_R_allo_adj_txt_output_15,         avg_line_R_allo_adj_txt_raw_score_15],
                [avg_line_R_allo_jpg_output_15,             avg_line_R_allo_jpg_raw_score_15],
                [avg_line_R_allo_json_output_15,            avg_line_R_allo_json_raw_score_15],
                [avg_line_R_allo_tokenized_txt_output_15,   avg_line_R_allo_tokenized_txt_raw_score_15]
                ]

occupancy_R_allo_15 = [[avg_occupancy_R_allo_adj_json_output_15,      avg_occupancy_R_allo_adj_json_raw_score_15],
                      [avg_occupancy_R_allo_adj_txt_output_15,            avg_occupancy_R_allo_adj_txt_raw_score_15],
                      [avg_occupancy_R_allo_jpg_output_15,                avg_occupancy_R_allo_jpg_raw_score_15],
                      [avg_occupancy_R_allo_json_output_15,               avg_occupancy_R_allo_json_raw_score_15],
                      [avg_occupancy_R_allo_tokenized_txt_output_15,      avg_occupancy_R_allo_tokenized_txt_raw_score_15],
                    [avg_occupancy_R_allo_ascii_txt_output_15,          avg_occupancy_R_allo_ascii_txt_raw_score_15]
                      ]
                    
line_NR_ego_15 = [[avg_line_NR_ego_adj_json_output_15,      avg_line_NR_ego_adj_json_raw_score_15],
                [avg_line_NR_ego_adj_txt_output_15,        avg_line_NR_ego_adj_txt_raw_score_15],
                [avg_line_NR_ego_jpg_output_15,            avg_line_NR_ego_jpg_raw_score_15],
                [avg_line_NR_ego_json_output_15,           avg_line_NR_ego_json_raw_score_15],
                [avg_line_NR_ego_tokenized_txt_output_15,  avg_line_NR_ego_tokenized_txt_raw_score_15]
                ]

occupancy_NR_ego_15 = [[avg_occupancy_NR_ego_adj_json_output_15,    avg_occupancy_NR_ego_adj_json_raw_score_15],
                      [avg_occupancy_NR_ego_adj_txt_output_15,           avg_occupancy_NR_ego_adj_txt_raw_score_15],
                      [avg_occupancy_NR_ego_jpg_output_15,               avg_occupancy_NR_ego_jpg_raw_score_15],
                      [avg_occupancy_NR_ego_json_output_15,              avg_occupancy_NR_ego_json_raw_score_15],
                      [avg_occupancy_NR_ego_tokenized_txt_output_15,     avg_occupancy_NR_ego_tokenized_txt_raw_score_15],
                    [avg_occupancy_NR_ego_ascii_txt_output_15,         avg_occupancy_NR_ego_ascii_txt_raw_score_15]
                      ]


line_R_ego_15 = [[avg_line_R_ego_adj_json_output_15,        avg_line_R_ego_adj_json_raw_score_15],
                [avg_line_R_ego_adj_txt_output_15,         avg_line_R_ego_adj_txt_raw_score_15],
                [avg_line_R_ego_jpg_output_15,             avg_line_R_ego_jpg_raw_score_15],
                [avg_line_R_ego_json_output_15,            avg_line_R_ego_json_raw_score_15],
                [avg_line_R_ego_tokenized_txt_output_15,   avg_line_R_ego_tokenized_txt_raw_score_15]
                ]

occupancy_R_ego_15 = [[avg_occupancy_R_ego_adj_json_output_15,      avg_occupancy_R_ego_adj_json_raw_score_15],
                     [avg_occupancy_R_ego_adj_txt_output_15,            avg_occupancy_R_ego_adj_txt_raw_score_15],
                     [avg_occupancy_R_ego_jpg_output_15,                avg_occupancy_R_ego_jpg_raw_score_15],
                     [avg_occupancy_R_ego_json_output_15,               avg_occupancy_R_ego_json_raw_score_15],
                     [avg_occupancy_R_ego_tokenized_txt_output_15,      avg_occupancy_R_ego_tokenized_txt_raw_score_15],
                    [avg_occupancy_R_ego_ascii_txt_output_15,          avg_occupancy_R_ego_ascii_txt_raw_score_15]
                     ]





line_NR_coords_adj_json_output_tokens = [avg_line_NR_coords_adj_json_output_3, avg_line_NR_coords_adj_json_output_6, avg_line_NR_coords_adj_json_output_15]
line_NR_coords_adj_txt_output_tokens = [avg_line_NR_coords_adj_txt_output_3, avg_line_NR_coords_adj_txt_output_6, avg_line_NR_coords_adj_txt_output_15]
line_NR_coords_jpg_output_tokens = [avg_line_NR_coords_jpg_output_3, avg_line_NR_coords_jpg_output_6, avg_line_NR_coords_jpg_output_15]
line_NR_coords_json_output_tokens = [avg_line_NR_coords_json_output_3, avg_line_NR_coords_json_output_6, avg_line_NR_coords_json_output_15]
line_NR_coords_tokenized_txt_output_tokens = [avg_line_NR_coords_tokenized_txt_output_3, avg_line_NR_coords_tokenized_txt_output_6, avg_line_NR_coords_tokenized_txt_output_15]
occupancy_NR_coords_adj_json_output_tokens = [avg_occupancy_NR_coords_adj_json_output_3, avg_occupancy_NR_coords_adj_json_output_6, avg_occupancy_NR_coords_adj_json_output_15]
occupancy_NR_coords_adj_txt_output_tokens = [avg_occupancy_NR_coords_adj_txt_output_3, avg_occupancy_NR_coords_adj_txt_output_6, avg_occupancy_NR_coords_adj_txt_output_15]
occupancy_NR_coords_jpg_output_tokens = [avg_occupancy_NR_coords_jpg_output_3, avg_occupancy_NR_coords_jpg_output_6, avg_occupancy_NR_coords_jpg_output_15]
occupancy_NR_coords_json_output_tokens = [avg_occupancy_NR_coords_json_output_3, avg_occupancy_NR_coords_json_output_6, avg_occupancy_NR_coords_json_output_15]
occupancy_NR_coords_tokenized_txt_output_tokens = [avg_occupancy_NR_coords_tokenized_txt_output_3, avg_occupancy_NR_coords_tokenized_txt_output_6, avg_occupancy_NR_coords_tokenized_txt_output_15]
occupancy_NR_coords_ascii_txt_output_tokens = [avg_occupancy_NR_coords_ascii_txt_output_3, avg_occupancy_NR_coords_ascii_txt_output_6, avg_occupancy_NR_coords_ascii_txt_output_15]

line_NR_coords_adj_json_raw_scores = [avg_line_NR_coords_adj_json_raw_score_3, avg_line_NR_coords_adj_json_raw_score_6, avg_line_NR_coords_adj_json_raw_score_15]
line_NR_coords_adj_txt_raw_scores = [avg_line_NR_coords_adj_txt_raw_score_3, avg_line_NR_coords_adj_txt_raw_score_6, avg_line_NR_coords_adj_txt_raw_score_15]
line_NR_coords_jpg_raw_scores = [avg_line_NR_coords_jpg_raw_score_3, avg_line_NR_coords_jpg_raw_score_6, avg_line_NR_coords_jpg_raw_score_15]
line_NR_coords_json_raw_scores = [avg_line_NR_coords_json_raw_score_3, avg_line_NR_coords_json_raw_score_6, avg_line_NR_coords_json_raw_score_15]
line_NR_coords_tokenized_txt_raw_scores = [avg_line_NR_coords_tokenized_txt_raw_score_3, avg_line_NR_coords_tokenized_txt_raw_score_6, avg_line_NR_coords_tokenized_txt_raw_score_15]
occupancy_NR_coords_adj_json_raw_scores = [avg_occupancy_NR_coords_adj_json_raw_score_3, avg_occupancy_NR_coords_adj_json_raw_score_6, avg_occupancy_NR_coords_adj_json_raw_score_15]
occupancy_NR_coords_adj_txt_raw_scores = [avg_occupancy_NR_coords_adj_txt_raw_score_3, avg_occupancy_NR_coords_adj_txt_raw_score_6, avg_occupancy_NR_coords_adj_txt_raw_score_15]
occupancy_NR_coords_jpg_raw_scores = [avg_occupancy_NR_coords_jpg_raw_score_3, avg_occupancy_NR_coords_jpg_raw_score_6, avg_occupancy_NR_coords_jpg_raw_score_15]
occupancy_NR_coords_json_raw_scores = [avg_occupancy_NR_coords_json_raw_score_3, avg_occupancy_NR_coords_json_raw_score_6, avg_occupancy_NR_coords_json_raw_score_15]
occupancy_NR_coords_tokenized_txt_raw_scores = [avg_occupancy_NR_coords_tokenized_txt_raw_score_3, avg_occupancy_NR_coords_tokenized_txt_raw_score_6, avg_occupancy_NR_coords_tokenized_txt_raw_score_15]
occupancy_NR_coords_ascii_txt_raw_scores = [avg_occupancy_NR_coords_ascii_txt_raw_score_3, avg_occupancy_NR_coords_ascii_txt_raw_score_6, avg_occupancy_NR_coords_ascii_txt_raw_score_15]

avg_line_NR_coords = [[np.mean(line_NR_coords_adj_json_output_tokens), np.mean(line_NR_coords_adj_json_raw_scores )],
                     [np.mean(line_NR_coords_adj_txt_output_tokens), np.mean(line_NR_coords_adj_txt_raw_scores)],
                     [np.mean(line_NR_coords_jpg_output_tokens), np.mean(line_NR_coords_jpg_raw_scores)],
                     [np.mean(line_NR_coords_json_output_tokens), np.mean(line_NR_coords_json_raw_scores )],
                     [np.mean(line_NR_coords_tokenized_txt_output_tokens), np.mean(line_NR_coords_tokenized_txt_raw_scores)]
                     ]
avg_occupancy_NR_coords = [[np.mean(occupancy_NR_coords_adj_json_output_tokens), np.mean(occupancy_NR_coords_adj_json_raw_scores )],
                     [np.mean(occupancy_NR_coords_adj_txt_output_tokens), np.mean(occupancy_NR_coords_adj_txt_raw_scores)],
                     [np.mean(occupancy_NR_coords_jpg_output_tokens), np.mean(occupancy_NR_coords_jpg_raw_scores)],
                     [np.mean(occupancy_NR_coords_json_output_tokens), np.mean(occupancy_NR_coords_json_raw_scores )],
                     [np.mean(occupancy_NR_coords_tokenized_txt_output_tokens), np.mean(occupancy_NR_coords_tokenized_txt_raw_scores)],
                     [np.mean(occupancy_NR_coords_ascii_txt_output_tokens), np.mean(occupancy_NR_coords_ascii_txt_raw_scores)]
                     ]



line_R_coords_adj_json_output_tokens = [avg_line_R_coords_adj_json_output_3, avg_line_R_coords_adj_json_output_6, avg_line_R_coords_adj_json_output_15]
line_R_coords_adj_txt_output_tokens = [avg_line_R_coords_adj_txt_output_3, avg_line_R_coords_adj_txt_output_6, avg_line_R_coords_adj_txt_output_15]
line_R_coords_jpg_output_tokens = [avg_line_R_coords_jpg_output_3, avg_line_R_coords_jpg_output_6, avg_line_R_coords_jpg_output_15]
line_R_coords_json_output_tokens = [avg_line_R_coords_json_output_3, avg_line_R_coords_json_output_6, avg_line_R_coords_json_output_15]
line_R_coords_tokenized_txt_output_tokens = [avg_line_R_coords_tokenized_txt_output_3, avg_line_R_coords_tokenized_txt_output_6, avg_line_R_coords_tokenized_txt_output_15]
occupancy_R_coords_adj_json_output_tokens = [avg_occupancy_R_coords_adj_json_output_3, avg_occupancy_R_coords_adj_json_output_6, avg_occupancy_R_coords_adj_json_output_15]
occupancy_R_coords_adj_txt_output_tokens = [avg_occupancy_R_coords_adj_txt_output_3, avg_occupancy_R_coords_adj_txt_output_6, avg_occupancy_R_coords_adj_txt_output_15]
occupancy_R_coords_jpg_output_tokens = [avg_occupancy_R_coords_jpg_output_3, avg_occupancy_R_coords_jpg_output_6, avg_occupancy_R_coords_jpg_output_15]
occupancy_R_coords_json_output_tokens = [avg_occupancy_R_coords_json_output_3, avg_occupancy_R_coords_json_output_6, avg_occupancy_R_coords_json_output_15]
occupancy_R_coords_tokenized_txt_output_tokens = [avg_occupancy_R_coords_tokenized_txt_output_3, avg_occupancy_R_coords_tokenized_txt_output_6, avg_occupancy_R_coords_tokenized_txt_output_15]
occupancy_R_coords_ascii_txt_output_tokens = [avg_occupancy_R_coords_ascii_txt_output_3, avg_occupancy_R_coords_ascii_txt_output_6, avg_occupancy_R_coords_ascii_txt_output_15]

line_R_coords_adj_json_raw_scores = [avg_line_R_coords_adj_json_raw_score_3, avg_line_R_coords_adj_json_raw_score_6, avg_line_R_coords_adj_json_raw_score_15]
line_R_coords_adj_txt_raw_scores = [avg_line_R_coords_adj_txt_raw_score_3, avg_line_R_coords_adj_txt_raw_score_6, avg_line_R_coords_adj_txt_raw_score_15]
line_R_coords_jpg_raw_scores = [avg_line_R_coords_jpg_raw_score_3, avg_line_R_coords_jpg_raw_score_6, avg_line_R_coords_jpg_raw_score_15]
line_R_coords_json_raw_scores = [avg_line_R_coords_json_raw_score_3, avg_line_R_coords_json_raw_score_6, avg_line_R_coords_json_raw_score_15]
line_R_coords_tokenized_txt_raw_scores = [avg_line_R_coords_tokenized_txt_raw_score_3, avg_line_R_coords_tokenized_txt_raw_score_6, avg_line_R_coords_tokenized_txt_raw_score_15]
occupancy_R_coords_adj_json_raw_scores = [avg_occupancy_R_coords_adj_json_raw_score_3, avg_occupancy_R_coords_adj_json_raw_score_6, avg_occupancy_R_coords_adj_json_raw_score_15]
occupancy_R_coords_adj_txt_raw_scores = [avg_occupancy_R_coords_adj_txt_raw_score_3, avg_occupancy_R_coords_adj_txt_raw_score_6, avg_occupancy_R_coords_adj_txt_raw_score_15]
occupancy_R_coords_jpg_raw_scores = [avg_occupancy_R_coords_jpg_raw_score_3, avg_occupancy_R_coords_jpg_raw_score_6, avg_occupancy_R_coords_jpg_raw_score_15]
occupancy_R_coords_json_raw_scores = [avg_occupancy_R_coords_json_raw_score_3, avg_occupancy_R_coords_json_raw_score_6, avg_occupancy_R_coords_json_raw_score_15]
occupancy_R_coords_tokenized_txt_raw_scores = [avg_occupancy_R_coords_tokenized_txt_raw_score_3, avg_occupancy_R_coords_tokenized_txt_raw_score_6, avg_occupancy_R_coords_tokenized_txt_raw_score_15]
occupancy_R_coords_ascii_txt_raw_scores = [avg_occupancy_R_coords_ascii_txt_raw_score_3, avg_occupancy_R_coords_ascii_txt_raw_score_6, avg_occupancy_R_coords_ascii_txt_raw_score_15]

avg_line_R_coords = [[np.mean(line_R_coords_adj_json_output_tokens), np.mean(line_R_coords_adj_json_raw_scores)],
                     [np.mean(line_R_coords_adj_txt_output_tokens), np.mean(line_R_coords_adj_txt_raw_scores)],
                     [np.mean(line_R_coords_jpg_output_tokens), np.mean(line_R_coords_jpg_raw_scores)],
                     [np.mean(line_R_coords_json_output_tokens), np.mean(line_R_coords_json_raw_scores )],
                     [np.mean(line_R_coords_tokenized_txt_output_tokens), np.mean(line_R_coords_tokenized_txt_raw_scores)]
                     ]
avg_occupancy_R_coords = [[np.mean(occupancy_R_coords_adj_json_output_tokens), np.mean(occupancy_R_coords_adj_json_raw_scores )],
                     [np.mean(occupancy_R_coords_adj_txt_output_tokens), np.mean(occupancy_R_coords_adj_txt_raw_scores)],
                     [np.mean(occupancy_R_coords_jpg_output_tokens), np.mean(occupancy_R_coords_jpg_raw_scores)],
                     [np.mean(occupancy_R_coords_json_output_tokens), np.mean(occupancy_R_coords_json_raw_scores )],
                     [np.mean(occupancy_R_coords_tokenized_txt_output_tokens), np.mean(occupancy_R_coords_tokenized_txt_raw_scores)],
                     [np.mean(occupancy_R_coords_ascii_txt_output_tokens), np.mean(occupancy_R_coords_ascii_txt_raw_scores)]
                     ]


line_NR_allo_adj_json_output_tokens = [avg_line_NR_allo_adj_json_output_3, avg_line_NR_allo_adj_json_output_6, avg_line_NR_allo_adj_json_output_15]
line_NR_allo_adj_txt_output_tokens = [avg_line_NR_allo_adj_txt_output_3, avg_line_NR_allo_adj_txt_output_6, avg_line_NR_allo_adj_txt_output_15]
line_NR_allo_jpg_output_tokens = [avg_line_NR_allo_jpg_output_3, avg_line_NR_allo_jpg_output_6, avg_line_NR_allo_jpg_output_15]
line_NR_allo_json_output_tokens = [avg_line_NR_allo_json_output_3, avg_line_NR_allo_json_output_6, avg_line_NR_allo_json_output_15]
line_NR_allo_tokenized_txt_output_tokens = [avg_line_NR_allo_tokenized_txt_output_3, avg_line_NR_allo_tokenized_txt_output_6, avg_line_NR_allo_tokenized_txt_output_15]
occupancy_NR_allo_adj_json_output_tokens = [avg_occupancy_NR_allo_adj_json_output_3, avg_occupancy_NR_allo_adj_json_output_6, avg_occupancy_NR_allo_adj_json_output_15]
occupancy_NR_allo_adj_txt_output_tokens = [avg_occupancy_NR_allo_adj_txt_output_3, avg_occupancy_NR_allo_adj_txt_output_6, avg_occupancy_NR_allo_adj_txt_output_15]
occupancy_NR_allo_jpg_output_tokens = [avg_occupancy_NR_allo_jpg_output_3, avg_occupancy_NR_allo_jpg_output_6, avg_occupancy_NR_allo_jpg_output_15]
occupancy_NR_allo_json_output_tokens = [avg_occupancy_NR_allo_json_output_3, avg_occupancy_NR_allo_json_output_6, avg_occupancy_NR_allo_json_output_15]
occupancy_NR_allo_tokenized_txt_output_tokens = [avg_occupancy_NR_allo_tokenized_txt_output_3, avg_occupancy_NR_allo_tokenized_txt_output_6, avg_occupancy_NR_allo_tokenized_txt_output_15]
occupancy_NR_allo_ascii_txt_output_tokens = [avg_occupancy_NR_allo_ascii_txt_output_3, avg_occupancy_NR_allo_ascii_txt_output_6, avg_occupancy_NR_allo_ascii_txt_output_15]

line_NR_allo_adj_json_raw_scores = [avg_line_NR_allo_adj_json_raw_score_3, avg_line_NR_allo_adj_json_raw_score_6, avg_line_NR_allo_adj_json_raw_score_15]
line_NR_allo_adj_txt_raw_scores = [avg_line_NR_allo_adj_txt_raw_score_3, avg_line_NR_allo_adj_txt_raw_score_6, avg_line_NR_allo_adj_txt_raw_score_15]
line_NR_allo_jpg_raw_scores = [avg_line_NR_allo_jpg_raw_score_3, avg_line_NR_allo_jpg_raw_score_6, avg_line_NR_allo_jpg_raw_score_15]
line_NR_allo_json_raw_scores = [avg_line_NR_allo_json_raw_score_3, avg_line_NR_allo_json_raw_score_6, avg_line_NR_allo_json_raw_score_15]
line_NR_allo_tokenized_txt_raw_scores = [avg_line_NR_allo_tokenized_txt_raw_score_3, avg_line_NR_allo_tokenized_txt_raw_score_6, avg_line_NR_allo_tokenized_txt_raw_score_15]
occupancy_NR_allo_adj_json_raw_scores = [avg_occupancy_NR_allo_adj_json_raw_score_3, avg_occupancy_NR_allo_adj_json_raw_score_6, avg_occupancy_NR_allo_adj_json_raw_score_15]
occupancy_NR_allo_adj_txt_raw_scores = [avg_occupancy_NR_allo_adj_txt_raw_score_3, avg_occupancy_NR_allo_adj_txt_raw_score_6, avg_occupancy_NR_allo_adj_txt_raw_score_15]
occupancy_NR_allo_jpg_raw_scores = [avg_occupancy_NR_allo_jpg_raw_score_3, avg_occupancy_NR_allo_jpg_raw_score_6, avg_occupancy_NR_allo_jpg_raw_score_15]
occupancy_NR_allo_json_raw_scores = [avg_occupancy_NR_allo_json_raw_score_3, avg_occupancy_NR_allo_json_raw_score_6, avg_occupancy_NR_allo_json_raw_score_15]
occupancy_NR_allo_tokenized_txt_raw_scores = [avg_occupancy_NR_allo_tokenized_txt_raw_score_3, avg_occupancy_NR_allo_tokenized_txt_raw_score_6, avg_occupancy_NR_allo_tokenized_txt_raw_score_15]
occupancy_NR_allo_ascii_txt_raw_scores = [avg_occupancy_NR_allo_ascii_txt_raw_score_3, avg_occupancy_NR_allo_ascii_txt_raw_score_6, avg_occupancy_NR_allo_ascii_txt_raw_score_15]


avg_line_NR_allo = [[np.mean(line_NR_allo_adj_json_output_tokens), np.mean(line_NR_allo_adj_json_raw_scores)],
                     [np.mean(line_NR_allo_adj_txt_output_tokens), np.mean(line_NR_allo_adj_txt_raw_scores)],
                     [np.mean(line_NR_allo_jpg_output_tokens), np.mean(line_NR_allo_jpg_raw_scores)],
                     [np.mean(line_NR_allo_json_output_tokens), np.mean(line_NR_allo_json_raw_scores )],
                     [np.mean(line_NR_allo_tokenized_txt_output_tokens), np.mean(line_NR_allo_tokenized_txt_raw_scores)]
                     ]
avg_occupancy_NR_allo = [[np.mean(occupancy_NR_allo_adj_json_output_tokens), np.mean(occupancy_NR_allo_adj_json_raw_scores)],
                     [np.mean(occupancy_NR_allo_adj_txt_output_tokens), np.mean(occupancy_NR_allo_adj_txt_raw_scores)],
                     [np.mean(occupancy_NR_allo_jpg_output_tokens), np.mean(occupancy_NR_allo_jpg_raw_scores)],
                     [np.mean(occupancy_NR_allo_json_output_tokens), np.mean(occupancy_NR_allo_json_raw_scores )],
                     [np.mean(occupancy_NR_allo_tokenized_txt_output_tokens), np.mean(occupancy_NR_allo_tokenized_txt_raw_scores)],
                     [np.mean(occupancy_NR_allo_ascii_txt_output_tokens), np.mean(occupancy_NR_allo_ascii_txt_raw_scores)]
                     ]

line_R_allo_adj_json_output_tokens = [avg_line_R_allo_adj_json_output_3, avg_line_R_allo_adj_json_output_6, avg_line_R_allo_adj_json_output_15]
line_R_allo_adj_txt_output_tokens = [avg_line_R_allo_adj_txt_output_3, avg_line_R_allo_adj_txt_output_6, avg_line_R_allo_adj_txt_output_15]
line_R_allo_jpg_output_tokens = [avg_line_R_allo_jpg_output_3, avg_line_R_allo_jpg_output_6, avg_line_R_allo_jpg_output_15]
line_R_allo_json_output_tokens = [avg_line_R_allo_json_output_3, avg_line_R_allo_json_output_6, avg_line_R_allo_json_output_15]
line_R_allo_tokenized_txt_output_tokens = [avg_line_R_allo_tokenized_txt_output_3, avg_line_R_allo_tokenized_txt_output_6, avg_line_R_allo_tokenized_txt_output_15]
occupancy_R_allo_adj_json_output_tokens = [avg_occupancy_R_allo_adj_json_output_3, avg_occupancy_R_allo_adj_json_output_6, avg_occupancy_R_allo_adj_json_output_15]
occupancy_R_allo_adj_txt_output_tokens = [avg_occupancy_R_allo_adj_txt_output_3, avg_occupancy_R_allo_adj_txt_output_6, avg_occupancy_R_allo_adj_txt_output_15]
occupancy_R_allo_jpg_output_tokens = [avg_occupancy_R_allo_jpg_output_3, avg_occupancy_R_allo_jpg_output_6, avg_occupancy_R_allo_jpg_output_15]
occupancy_R_allo_json_output_tokens = [avg_occupancy_R_allo_json_output_3, avg_occupancy_R_allo_json_output_6, avg_occupancy_R_allo_json_output_15]
occupancy_R_allo_tokenized_txt_output_tokens = [avg_occupancy_R_allo_tokenized_txt_output_3, avg_occupancy_R_allo_tokenized_txt_output_6, avg_occupancy_R_allo_tokenized_txt_output_15]
occupancy_R_allo_ascii_txt_output_tokens = [avg_occupancy_R_allo_ascii_txt_output_3, avg_occupancy_R_allo_ascii_txt_output_6, avg_occupancy_R_allo_ascii_txt_output_15]

line_R_allo_adj_json_raw_scores = [avg_line_R_allo_adj_json_raw_score_3, avg_line_R_allo_adj_json_raw_score_6, avg_line_R_allo_adj_json_raw_score_15]
line_R_allo_adj_txt_raw_scores = [avg_line_R_allo_adj_txt_raw_score_3, avg_line_R_allo_adj_txt_raw_score_6, avg_line_R_allo_adj_txt_raw_score_15]
line_R_allo_jpg_raw_scores = [avg_line_R_allo_jpg_raw_score_3, avg_line_R_allo_jpg_raw_score_6, avg_line_R_allo_jpg_raw_score_15]
line_R_allo_json_raw_scores = [avg_line_R_allo_json_raw_score_3, avg_line_R_allo_json_raw_score_6, avg_line_R_allo_json_raw_score_15]
line_R_allo_tokenized_txt_raw_scores = [avg_line_R_allo_tokenized_txt_raw_score_3, avg_line_R_allo_tokenized_txt_raw_score_6, avg_line_R_allo_tokenized_txt_raw_score_15]
occupancy_R_allo_adj_json_raw_scores = [avg_occupancy_R_allo_adj_json_raw_score_3, avg_occupancy_R_allo_adj_json_raw_score_6, avg_occupancy_R_allo_adj_json_raw_score_15]
occupancy_R_allo_adj_txt_raw_scores = [avg_occupancy_R_allo_adj_txt_raw_score_3, avg_occupancy_R_allo_adj_txt_raw_score_6, avg_occupancy_R_allo_adj_txt_raw_score_15]
occupancy_R_allo_jpg_raw_scores = [avg_occupancy_R_allo_jpg_raw_score_3, avg_occupancy_R_allo_jpg_raw_score_6, avg_occupancy_R_allo_jpg_raw_score_15]
occupancy_R_allo_json_raw_scores = [avg_occupancy_R_allo_json_raw_score_3, avg_occupancy_R_allo_json_raw_score_6, avg_occupancy_R_allo_json_raw_score_15]
occupancy_R_allo_tokenized_txt_raw_scores = [avg_occupancy_R_allo_tokenized_txt_raw_score_3, avg_occupancy_R_allo_tokenized_txt_raw_score_6, avg_occupancy_R_allo_tokenized_txt_raw_score_15]
occupancy_R_allo_ascii_txt_raw_scores = [avg_occupancy_R_allo_ascii_txt_raw_score_3, avg_occupancy_R_allo_ascii_txt_raw_score_6, avg_occupancy_R_allo_ascii_txt_raw_score_15]

avg_line_R_allo = [[np.mean(line_R_allo_adj_json_output_tokens), np.mean(line_R_allo_adj_json_raw_scores )],
                     [np.mean(line_R_allo_adj_txt_output_tokens), np.mean(line_R_allo_adj_txt_raw_scores)],
                     [np.mean(line_R_allo_jpg_output_tokens), np.mean(line_R_allo_jpg_raw_scores)],
                     [np.mean(line_R_allo_json_output_tokens), np.mean(line_R_allo_json_raw_scores )],
                     [np.mean(line_R_allo_tokenized_txt_output_tokens), np.mean(line_R_allo_tokenized_txt_raw_scores)]
                     ]
avg_occupancy_R_allo = [[np.mean(occupancy_R_allo_adj_json_output_tokens), np.mean(occupancy_R_allo_adj_json_raw_scores )],
                     [np.mean(occupancy_R_allo_adj_txt_output_tokens), np.mean(occupancy_R_allo_adj_txt_raw_scores)],
                     [np.mean(occupancy_R_allo_jpg_output_tokens), np.mean(occupancy_R_allo_jpg_raw_scores)],
                     [np.mean(occupancy_R_allo_json_output_tokens), np.mean(occupancy_R_allo_json_raw_scores )],
                     [np.mean(occupancy_R_allo_tokenized_txt_output_tokens), np.mean(occupancy_R_allo_tokenized_txt_raw_scores)],
                     [np.mean(occupancy_R_allo_ascii_txt_output_tokens), np.mean(occupancy_R_allo_ascii_txt_raw_scores)]
                     ]


line_NR_ego_adj_json_output_tokens = [avg_line_NR_ego_adj_json_output_3, avg_line_NR_ego_adj_json_output_6, avg_line_NR_ego_adj_json_output_15]
line_NR_ego_adj_txt_output_tokens = [avg_line_NR_ego_adj_txt_output_3, avg_line_NR_ego_adj_txt_output_6, avg_line_NR_ego_adj_txt_output_15]
line_NR_ego_jpg_output_tokens = [avg_line_NR_ego_jpg_output_3, avg_line_NR_ego_jpg_output_6, avg_line_NR_ego_jpg_output_15]
line_NR_ego_json_output_tokens = [avg_line_NR_ego_json_output_3, avg_line_NR_ego_json_output_6, avg_line_NR_ego_json_output_15]
line_NR_ego_tokenized_txt_output_tokens = [avg_line_NR_ego_tokenized_txt_output_3, avg_line_NR_ego_tokenized_txt_output_6, avg_line_NR_ego_tokenized_txt_output_15]
occupancy_NR_ego_adj_json_output_tokens = [avg_occupancy_NR_ego_adj_json_output_3, avg_occupancy_NR_ego_adj_json_output_6, avg_occupancy_NR_ego_adj_json_output_15]
occupancy_NR_ego_adj_txt_output_tokens = [avg_occupancy_NR_ego_adj_txt_output_3, avg_occupancy_NR_ego_adj_txt_output_6, avg_occupancy_NR_ego_adj_txt_output_15]
occupancy_NR_ego_jpg_output_tokens = [avg_occupancy_NR_ego_jpg_output_3, avg_occupancy_NR_ego_jpg_output_6, avg_occupancy_NR_ego_jpg_output_15]
occupancy_NR_ego_json_output_tokens = [avg_occupancy_NR_ego_json_output_3, avg_occupancy_NR_ego_json_output_6, avg_occupancy_NR_ego_json_output_15]
occupancy_NR_ego_tokenized_txt_output_tokens = [avg_occupancy_NR_ego_tokenized_txt_output_3, avg_occupancy_NR_ego_tokenized_txt_output_6, avg_occupancy_NR_ego_tokenized_txt_output_15]
occupancy_NR_ego_ascii_txt_output_tokens = [avg_occupancy_NR_ego_ascii_txt_output_3, avg_occupancy_NR_ego_ascii_txt_output_6, avg_occupancy_NR_ego_ascii_txt_output_15]

line_NR_ego_adj_json_raw_scores = [avg_line_NR_ego_adj_json_raw_score_3, avg_line_NR_ego_adj_json_raw_score_6, avg_line_NR_ego_adj_json_raw_score_15]
line_NR_ego_adj_txt_raw_scores = [avg_line_NR_ego_adj_txt_raw_score_3, avg_line_NR_ego_adj_txt_raw_score_6, avg_line_NR_ego_adj_txt_raw_score_15]
line_NR_ego_jpg_raw_scores = [avg_line_NR_ego_jpg_raw_score_3, avg_line_NR_ego_jpg_raw_score_6, avg_line_NR_ego_jpg_raw_score_15]
line_NR_ego_json_raw_scores = [avg_line_NR_ego_json_raw_score_3, avg_line_NR_ego_json_raw_score_6, avg_line_NR_ego_json_raw_score_15]
line_NR_ego_tokenized_txt_raw_scores = [avg_line_NR_ego_tokenized_txt_raw_score_3, avg_line_NR_ego_tokenized_txt_raw_score_6, avg_line_NR_ego_tokenized_txt_raw_score_15]
occupancy_NR_ego_adj_json_raw_scores = [avg_occupancy_NR_ego_adj_json_raw_score_3, avg_occupancy_NR_ego_adj_json_raw_score_6, avg_occupancy_NR_ego_adj_json_raw_score_15]
occupancy_NR_ego_adj_txt_raw_scores = [avg_occupancy_NR_ego_adj_txt_raw_score_3, avg_occupancy_NR_ego_adj_txt_raw_score_6, avg_occupancy_NR_ego_adj_txt_raw_score_15]
occupancy_NR_ego_jpg_raw_scores = [avg_occupancy_NR_ego_jpg_raw_score_3, avg_occupancy_NR_ego_jpg_raw_score_6, avg_occupancy_NR_ego_jpg_raw_score_15]
occupancy_NR_ego_json_raw_scores = [avg_occupancy_NR_ego_json_raw_score_3, avg_occupancy_NR_ego_json_raw_score_6, avg_occupancy_NR_ego_json_raw_score_15]
occupancy_NR_ego_tokenized_txt_raw_scores = [avg_occupancy_NR_ego_tokenized_txt_raw_score_3, avg_occupancy_NR_ego_tokenized_txt_raw_score_6, avg_occupancy_NR_ego_tokenized_txt_raw_score_15]
occupancy_NR_ego_ascii_txt_raw_scores = [avg_occupancy_NR_ego_ascii_txt_raw_score_3, avg_occupancy_NR_ego_ascii_txt_raw_score_6, avg_occupancy_NR_ego_ascii_txt_raw_score_15]


avg_line_NR_ego = [[np.mean(line_NR_ego_adj_json_output_tokens), np.mean(line_NR_ego_adj_json_raw_scores )],
                     [np.mean(line_NR_ego_adj_txt_output_tokens), np.mean(line_NR_ego_adj_txt_raw_scores)],
                     [np.mean(line_NR_ego_jpg_output_tokens), np.mean(line_NR_ego_jpg_raw_scores)],
                     [np.mean(line_NR_ego_json_output_tokens), np.mean(line_NR_ego_json_raw_scores )],
                     [np.mean(line_NR_ego_tokenized_txt_output_tokens), np.mean(line_NR_ego_tokenized_txt_raw_scores)]
                     ]
avg_occupancy_NR_ego = [[np.mean(occupancy_NR_ego_adj_json_output_tokens), np.mean(occupancy_NR_ego_adj_json_raw_scores )],
                     [np.mean(occupancy_NR_ego_adj_txt_output_tokens), np.mean(occupancy_NR_ego_adj_txt_raw_scores)],
                     [np.mean(occupancy_NR_ego_jpg_output_tokens), np.mean(occupancy_NR_ego_jpg_raw_scores)],
                     [np.mean(occupancy_NR_ego_json_output_tokens), np.mean(occupancy_NR_ego_json_raw_scores )],
                     [np.mean(occupancy_NR_ego_tokenized_txt_output_tokens), np.mean(occupancy_NR_ego_tokenized_txt_raw_scores)],
                     [np.mean(occupancy_NR_ego_ascii_txt_output_tokens), np.mean(occupancy_NR_ego_ascii_txt_raw_scores)]
                     ]



line_R_ego_adj_json_output_tokens = [avg_line_R_ego_adj_json_output_3, avg_line_R_ego_adj_json_output_6, avg_line_R_ego_adj_json_output_15]
line_R_ego_adj_txt_output_tokens = [avg_line_R_ego_adj_txt_output_3, avg_line_R_ego_adj_txt_output_6, avg_line_R_ego_adj_txt_output_15]
line_R_ego_jpg_output_tokens = [avg_line_R_ego_jpg_output_3, avg_line_R_ego_jpg_output_6, avg_line_R_ego_jpg_output_15]
line_R_ego_json_output_tokens = [avg_line_R_ego_json_output_3, avg_line_R_ego_json_output_6, avg_line_R_ego_json_output_15]
line_R_ego_tokenized_txt_output_tokens = [avg_line_R_ego_tokenized_txt_output_3, avg_line_R_ego_tokenized_txt_output_6, avg_line_R_ego_tokenized_txt_output_15]
occupancy_R_ego_adj_json_output_tokens = [avg_occupancy_R_ego_adj_json_output_3, avg_occupancy_R_ego_adj_json_output_6, avg_occupancy_R_ego_adj_json_output_15]
occupancy_R_ego_adj_txt_output_tokens = [avg_occupancy_R_ego_adj_txt_output_3, avg_occupancy_R_ego_adj_txt_output_6, avg_occupancy_R_ego_adj_txt_output_15]
occupancy_R_ego_jpg_output_tokens = [avg_occupancy_R_ego_jpg_output_3, avg_occupancy_R_ego_jpg_output_6, avg_occupancy_R_ego_jpg_output_15]
occupancy_R_ego_json_output_tokens = [avg_occupancy_R_ego_json_output_3, avg_occupancy_R_ego_json_output_6, avg_occupancy_R_ego_json_output_15]
occupancy_R_ego_tokenized_txt_output_tokens = [avg_occupancy_R_ego_tokenized_txt_output_3, avg_occupancy_R_ego_tokenized_txt_output_6, avg_occupancy_R_ego_tokenized_txt_output_15]
occupancy_R_ego_ascii_txt_output_tokens = [avg_occupancy_R_ego_ascii_txt_output_3, avg_occupancy_R_ego_ascii_txt_output_6, avg_occupancy_R_ego_ascii_txt_output_15]

line_R_ego_adj_json_raw_scores = [avg_line_R_ego_adj_json_raw_score_3, avg_line_R_ego_adj_json_raw_score_6, avg_line_R_ego_adj_json_raw_score_15]
line_R_ego_adj_txt_raw_scores = [avg_line_R_ego_adj_txt_raw_score_3, avg_line_R_ego_adj_txt_raw_score_6, avg_line_R_ego_adj_txt_raw_score_15]
line_R_ego_jpg_raw_scores = [avg_line_R_ego_jpg_raw_score_3, avg_line_R_ego_jpg_raw_score_6, avg_line_R_ego_jpg_raw_score_15]
line_R_ego_json_raw_scores = [avg_line_R_ego_json_raw_score_3, avg_line_R_ego_json_raw_score_6, avg_line_R_ego_json_raw_score_15]
line_R_ego_tokenized_txt_raw_scores = [avg_line_R_ego_tokenized_txt_raw_score_3, avg_line_R_ego_tokenized_txt_raw_score_6, avg_line_R_ego_tokenized_txt_raw_score_15]
occupancy_R_ego_adj_json_raw_scores = [avg_occupancy_R_ego_adj_json_raw_score_3, avg_occupancy_R_ego_adj_json_raw_score_6, avg_occupancy_R_ego_adj_json_raw_score_15]
occupancy_R_ego_adj_txt_raw_scores = [avg_occupancy_R_ego_adj_txt_raw_score_3, avg_occupancy_R_ego_adj_txt_raw_score_6, avg_occupancy_R_ego_adj_txt_raw_score_15]
occupancy_R_ego_jpg_raw_scores = [avg_occupancy_R_ego_jpg_raw_score_3, avg_occupancy_R_ego_jpg_raw_score_6, avg_occupancy_R_ego_jpg_raw_score_15]
occupancy_R_ego_json_raw_scores = [avg_occupancy_R_ego_json_raw_score_3, avg_occupancy_R_ego_json_raw_score_6, avg_occupancy_R_ego_json_raw_score_15]
occupancy_R_ego_tokenized_txt_raw_scores = [avg_occupancy_R_ego_tokenized_txt_raw_score_3, avg_occupancy_R_ego_tokenized_txt_raw_score_6, avg_occupancy_R_ego_tokenized_txt_raw_score_15]
occupancy_R_ego_ascii_txt_raw_scores = [avg_occupancy_R_ego_ascii_txt_raw_score_3, avg_occupancy_R_ego_ascii_txt_raw_score_6, avg_occupancy_R_ego_ascii_txt_raw_score_15]

avg_line_R_ego = [[np.mean(line_R_ego_adj_json_output_tokens), np.mean(line_R_ego_adj_json_raw_scores )],
                     [np.mean(line_R_ego_adj_txt_output_tokens), np.mean(line_R_ego_adj_txt_raw_scores)],
                     [np.mean(line_R_ego_jpg_output_tokens), np.mean(line_R_ego_jpg_raw_scores)],
                     [np.mean(line_R_ego_json_output_tokens), np.mean(line_R_ego_json_raw_scores )],
                     [np.mean(line_R_ego_tokenized_txt_output_tokens), np.mean(line_R_ego_tokenized_txt_raw_scores)]
                     ]
avg_occupancy_R_ego = [[np.mean(occupancy_R_ego_adj_json_output_tokens), np.mean(occupancy_R_ego_adj_json_raw_scores )],
                     [np.mean(occupancy_R_ego_adj_txt_output_tokens), np.mean(occupancy_R_ego_adj_txt_raw_scores)],
                     [np.mean(occupancy_R_ego_jpg_output_tokens), np.mean(occupancy_R_ego_jpg_raw_scores)],
                     [np.mean(occupancy_R_ego_json_output_tokens), np.mean(occupancy_R_ego_json_raw_scores )],
                     [np.mean(occupancy_R_ego_tokenized_txt_output_tokens), np.mean(occupancy_R_ego_tokenized_txt_raw_scores)],
                     [np.mean(occupancy_R_ego_ascii_txt_output_tokens), np.mean(occupancy_R_ego_ascii_txt_raw_scores)]
                     ]


# two plots with tokens and raw scores averaged over complexities


# Labels for legend
labels_base = ["Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"]
markers = ['o', 'v', 's', '*', 'D', 'P']
red = ['tomato', 'tomato']#['red', 'red'] #light, dark
blue = ['dodgerblue','dodgerblue']#['blue', 'blue'] #light, dark
green = ['lightgreen', 'lightgreen']#['lime', 'lime'] #light, dark
marker_edge = ['none', 'black'] #line, occupancy
marker_size = [10,10,10]
testx = [1, 2, 3, 4, 5, 6]
testy = [1, 2, 3, 4, 5, 6]
# Create multiple plots in the same figure
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 6), sharex=True, sharey=True)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 6), sharex=True, sharey=True)

# axes[0,0].plot(testx[0], testy[0], marker='o', color=red[0], label='test 1')
# axes[1,0].plot(testx[1], testy[1], marker='o', color=red[1], label='test 2')
# axes[2,0].plot(testx[2], testy[2], marker='o', color=blue[0], label='test 3')
# axes[0,1].plot(testx[3], testy[3], marker='o', color=blue[1], label='test 4')
# axes[1,1].plot(testx[4], testy[4], marker='o', color=green[0], label='test 5')
# axes[2,1].plot(testx[5], testy[5], marker='o', color=green[1], label=f'test 6')

# Non-reasoning plot
for i, point in enumerate(avg_line_NR_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_line_NR_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_line_NR_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_occupancy_NR_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_occupancy_NR_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_occupancy_NR_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None')



# Reasoning plot
for i, point in enumerate(avg_line_R_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_line_R_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_line_R_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_occupancy_R_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_occupancy_R_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None')

for i, point in enumerate(avg_occupancy_R_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None')


# Axis settings
ax1.set_xscale('log')  # Set x-axis to logarithmic scale
ax2.set_xscale('log')
ax1.grid(True, linestyle='--', alpha=0.6)
ax2.grid(True, linestyle='--', alpha=0.6)
ax1.set_ylabel("Number of Correct Steps")
ax1.set_xlabel("Average Test Compute (Tokens)")
ax2.set_ylabel("Number of Correct Steps")
ax2.set_xlabel("Average Test Compute (Tokens)")



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
    r"$\bf{Output\ Types}$",
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

ax2.legend(
    handles,
    labels,
    handler_map={tuple: HandlerTuple(ndivide=None)},
    loc='center left',
    bbox_to_anchor=(1.02, 0.5),
    title="Legend"
)

# Place legend outside the plot on the right
# axes[1,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Representation, Complexity, Output Type, Model")


ax1.set_title("Gemini 2.5 Flash-Lite")
ax2.set_title("Gemini 2.5 Pro")


plt.suptitle("Number of Correct Consecutive Steps as a Function of Test Compute", fontweight= 'bold')

plt.tight_layout(rect=[0, 0, 0.97, 1])  # leave 15% of width for legend





# plt.show()


# 4 plots raw score vs output tokens


# Labels for legend
labels_base = ["Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"]
markers = ['o', 'v', 's', '*', 'D', 'P']
red = ['tomato', 'tomato']#['red', 'red'] #light, dark
blue = ['dodgerblue','dodgerblue']#['blue', 'blue'] #light, dark
green = ['lightgreen', 'lightgreen']#['lime', 'lime'] #light, dark
marker_edge = ['dimgrey', 'dimgrey'] #line, occupancy
marker_size = [10,10,10]
testx = [1, 2, 3, 4, 5, 6]
testy = [1, 2, 3, 4, 5, 6]
# Create multiple plots in the same figure
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 6), sharex=True, sharey=True)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 6), sharex=True, sharey=True)

# axes[0,0].plot(testx[0], testy[0], marker='o', color=red[0], label='test 1')
# axes[1,0].plot(testx[1], testy[1], marker='o', color=red[1], label='test 2')
# axes[2,0].plot(testx[2], testy[2], marker='o', color=blue[0], label='test 3')
# axes[0,1].plot(testx[3], testy[3], marker='o', color=blue[1], label='test 4')
# axes[1,1].plot(testx[4], testy[4], marker='o', color=green[0], label='test 5')
# axes[2,1].plot(testx[5], testy[5], marker='o', color=green[1], label=f'test 6')


# Plot top row
for i, point in enumerate(avg_line_NR_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Flash-Lite")

for i, point in enumerate(avg_line_NR_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i],  color = green[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(avg_line_NR_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(avg_line_R_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(avg_line_R_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i],  color = green[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(avg_line_R_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[0,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Pro")


# Plot bottom row
for i, point in enumerate(avg_occupancy_NR_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Flash-Lite")

for i, point in enumerate(avg_occupancy_NR_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(avg_occupancy_NR_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Flash-Lite")

for i, point in enumerate(avg_occupancy_R_coords):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(avg_occupancy_R_allo):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(avg_occupancy_R_ego):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    axes[1,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Pro")

# Plot the summed average number of steps as a dotted line
coords_line = np.array([5.6, 21.0, 95.0])
coords_occupancy = np.array([10.2, 41.0, 189.0])
allo_ego_line = np.array([4.6, 20.0, 94.0])
allo_ego_occupancy = np.array([9.2, 40.0, 188.0])

# plot as a horizontal line
axes[0,0].axhline(y=np.mean(coords_line), color=red[0], linewidth = 1, linestyle='--', alpha = 0.8)
axes[0,0].axhline(y=np.mean(allo_ego_line), color=green[0], linewidth = 1, linestyle='--', alpha = 0.8)
axes[0,1].axhline(y=np.mean(coords_line), color=red[0], linewidth = 1, linestyle='--', alpha = 0.8)
axes[0,1].axhline(y=np.mean(allo_ego_line), color=green[0], linewidth = 1, linestyle='--', alpha = 0.8)
axes[1,0].axhline(y=np.mean(coords_occupancy), color=red[0], linewidth = 1, linestyle='--', alpha = 0.8)
axes[1,0].axhline(y=np.mean(allo_ego_occupancy), color=green[0], linewidth = 1, linestyle='--', alpha = 0.8)
axes[1,1].axhline(y=np.mean(coords_occupancy), color=red[0], linewidth = 1, linestyle='--', alpha = 0.8)
axes[1,1].axhline(y=np.mean(allo_ego_occupancy), color=green[0], linewidth = 1, linestyle='--', alpha = 0.8)
                  
# # Axis labels
for i in range(0,2):
    for j in range(0,2):
        axes[i,j].set_xscale('log')  # Set x-axis to logarithmic scale
        axes[i,j].grid(True, linestyle='--', alpha=0.6)
        axes[i,j].set_ylabel("Number of Correct Steps")
        axes[i,j].set_xlabel("Average Test Compute  (Tokens)")



# --- Legend Group Definitions ---
spacer_handle = (
    Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
coord_handle = (
    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=red[0], markersize=10),
    # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
)
allo_handle = (
    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=green[0], markersize=10),
    # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=green[1], markersize=10)
)
ego_handle = (
    Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=blue[0], markersize=10),
    # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=blue[1], markersize=10)
)
ground_truth_coords_line_handle = (
    Line2D([], [], color = red[0], linewidth = 1, linestyle = '--', marker = 'none')
)

ground_truth_allo_ego_line_handle = (
    Line2D([], [], color = green[0], linewidth = 1, linestyle = '--', marker = 'none')
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
    spacer_handle,
    ground_truth_coords_line_handle,
    ground_truth_allo_ego_line_handle
    
    # spacer_handle,
    # pro_handle,
    # flashlite_handle,
    # Line2D([], [], marker='o', color='none', markerfacecolor=red[1], markersize=10), # Gemini Pro
    # Line2D([], [], marker='o', color='none', markerfacecolor=red[0], markersize=10), # Gemini Flash Lite

#     spacer_handle,  
#     Line2D([], [], marker='o', color='none', markerfacecolor='lightgrey', mec=marker_edge[1], markersize = 10),   # Occupancy
#     Line2D([], [], marker='o', color='none', markerfacecolor='lightgrey', mec=marker_edge[0], markersize = 10), # Line Wall
]

labels = [
    r"$\bf{Output\ Types}$",
    "Coordinates", "Allocentric", "Egocentric",
    r"$\bf{Input\ Formats}$",
    "Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII",
    # r"$\bf{Models}$",
    # "Gemini 2.5 Pro", "Gemini 2.5 Flash-Lite",
    # r"$\bf{Maze\ Styles\ and\ Complexities\ (Low -> High)}$",
    # "Occupancy Grid, 7x7, 13x13, 31x31", "Line Wall, 3x3, 6x6, 15x15"
    #     r"$\bf{Maze\ Styles}$",
    # "Occupancy Grid", "Line Wall",
    r"$\bf{True\ Solution\ Length}$",
    "Coordinates", "Allocentric and Egocentric"
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


axes[0,0].set_title("Line-Walled Mazes, Gemini 2.5 Flash-Lite")
axes[0,1].set_title("Line-Walled Mazes, Gemini 2.5 Pro")
axes[1,0].set_title("Occupancy Grid Mazes, Gemini 2.5 Flash-Lite")
axes[1,1].set_title("Occupancy Grid Mazes, Gemini 2.5 Pro")


plt.suptitle("Number of Correct Consecutive Steps as a Function of Test Compute", fontweight= 'bold')

plt.tight_layout(rect=[0, 0, 0.97, 1])  # leave 15% of width for legend





plt.show()
















# 6 plots of raw score vs output tokens

# # Labels for legend
# labels_base = ["Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"]
# markers = ['o', 'v', 's', '*', 'D', 'P']
# red = ['red', 'red'] #light, dark
# blue = ['blue', 'blue'] #light, dark
# green = ['lime', 'lime'] #light, dark
# marker_edge = ['none', 'black'] #line, occupancy
# marker_size = [10,10,10]
# testx = [1, 2, 3, 4, 5, 6]
# testy = [1, 2, 3, 4, 5, 6]
# # Create multiple plots in the same figure
# # fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 6), sharex=True, sharey=True)
# fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 6), sharex=False, sharey=False)

# # axes[0,0].plot(testx[0], testy[0], marker='o', color=red[0], label='test 1')
# # axes[1,0].plot(testx[1], testy[1], marker='o', color=red[1], label='test 2')
# # axes[2,0].plot(testx[2], testy[2], marker='o', color=blue[0], label='test 3')
# # axes[0,1].plot(testx[3], testy[3], marker='o', color=blue[1], label='test 4')
# # axes[1,1].plot(testx[4], testy[4], marker='o', color=green[0], label='test 5')
# # axes[2,1].plot(testx[5], testy[5], marker='o', color=green[1], label=f'test 6')


# # Plot 3x3 data with corresponding labels
# for i, point in enumerate(line_NR_coords_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,0].plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(line_NR_allo_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,0].plot(x, y, marker=markers[i],  color = green[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(line_NR_ego_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(line_R_coords_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Pro")

# for i, point in enumerate(line_R_allo_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,1].plot(x, y, marker=markers[i],  color = green[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Pro")

# for i, point in enumerate(line_R_ego_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Pro")


# # Plot 7x7 data with corresponding labels
# for i, point in enumerate(occupancy_NR_coords_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,0].plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_NR_allo_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_NR_ego_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_R_coords_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Pro")

# for i, point in enumerate(occupancy_R_allo_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Pro")

# for i, point in enumerate(occupancy_R_ego_3):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[0,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Pro")

# # Plot 6x6 data with corresponding labels
# for i, point in enumerate(line_NR_coords_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Coordinates, Gemini 2.5 Flash-Lite")
# for i, point in enumerate(line_NR_allo_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Allocentric, Gemini 2.5 Flash-Lite")
# for i, point in enumerate(line_NR_ego_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Egocentric, Gemini 2.5 Flash-Lite")
# for i, point in enumerate(line_R_coords_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Coordinates, Gemini 2.5 Pro")
# for i, point in enumerate(line_R_allo_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Allocentric, Gemini 2.5 Pro")
# for i, point in enumerate(line_R_ego_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Egocentric, Gemini 2.5 Pro")

# # Plot 13x13 data with corresponding labels
# for i, point in enumerate(occupancy_NR_coords_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Coordinates, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_NR_allo_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Allocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_NR_ego_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Egocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_R_coords_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Coordinates, Gemini 2.5 Pro")

# for i, point in enumerate(occupancy_R_allo_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Allocentric, Gemini 2.5 Pro")

# for i, point in enumerate(occupancy_R_ego_6):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[1,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Egocentric, Gemini 2.5 Pro")


#     # Plot 15x15 data with corresponding labels
# for i, point in enumerate(line_NR_coords_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Coordinates, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(line_NR_allo_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Allocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(line_NR_ego_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Egocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(line_R_coords_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Coordinates, Gemini 2.5 Pro")

# for i, point in enumerate(line_R_allo_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Allocentric, Gemini 2.5 Pro")

# for i, point in enumerate(line_R_ego_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Egocentric, Gemini 2.5 Pro")


# # Plot 31x31 data with corresponding labels
# for i, point in enumerate(occupancy_NR_coords_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,0].plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Coordinates, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_NR_allo_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,0].plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Allocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_NR_ego_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,0].plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Egocentric, Gemini 2.5 Flash-Lite")

# for i, point in enumerate(occupancy_R_coords_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,1].plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Coordinates, Gemini 2.5 Pro")

# for i, point in enumerate(occupancy_R_allo_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,1].plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Allocentric, Gemini 2.5 Pro")

# for i, point in enumerate(occupancy_R_ego_15):
#     x, y = point
#     label = labels_base[i]  # get label corresponding to the row
#     axes[2,1].plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Egocentric, Gemini 2.5 Pro")


# # # Axis labels
# for i in range(0,3):
#     for j in range(0,2):
#         axes[i,j].set_xscale('log')  # Set x-axis to logarithmic scale
#         axes[i,j].grid(True, linestyle='--', alpha=0.6)
#         axes[i,j].set_ylabel("Number of Correct Steps")
#         axes[i,j].set_xlabel("Average Cost Per Task (Tokens)")



# # --- Legend Group Definitions ---
# spacer_handle = (
#     Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
# )
# coord_handle = (
#     Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[0], markersize=10),
#     # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
# )
# allo_handle = (
#     Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=green[0], markersize=10),
#     # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=green[1], markersize=10)
# )
# ego_handle = (
#     Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=blue[0], markersize=10),
#     # Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=blue[1], markersize=10)
# )

# pro_handle = (
#     Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=red[1], markersize=10),
#     Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=green[1], markersize=10),
#     Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=blue[1], markersize=10)
# )

# flashlite_handle = (Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=red[0], markersize=10),
#                     Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=green[0], markersize=10),
#                     Line2D([], [], marker='o', color='none', mec= marker_edge[0], markerfacecolor=blue[0], markersize=10)
# )

# handles = [
#     spacer_handle,
#     coord_handle,
#     allo_handle,
#     ego_handle,
#     spacer_handle,

#     Line2D([], [], marker='o', color='gray', linestyle='None', markersize = 10),  # Adjacency JSON
#     Line2D([], [], marker='v', color='gray', linestyle='None', markersize = 10),  # Adjacency Text
#     Line2D([], [], marker='s', color='gray', linestyle='None', markersize = 10),  # JPG
#     Line2D([], [], marker='*', color='gray', linestyle='None', markersize = 10),  # JSON
#     Line2D([], [], marker='D', color='gray', linestyle='None', markersize = 10),  # Tokenized
#     Line2D([], [], marker='P', color='gray', linestyle='None', markersize = 10),  # ASCII
    
#     # spacer_handle,
#     # pro_handle,
#     # flashlite_handle,
#     # Line2D([], [], marker='o', color='none', markerfacecolor=red[1], markersize=10), # Gemini Pro
#     # Line2D([], [], marker='o', color='none', markerfacecolor=red[0], markersize=10), # Gemini Flash Lite

#     spacer_handle,  
#     Line2D([], [], marker='o', color='none', markerfacecolor='lightgrey', mec=marker_edge[1], markersize = 10),   # Occupancy
#     Line2D([], [], marker='o', color='none', markerfacecolor='lightgrey', mec=marker_edge[0], markersize = 10), # Line Wall
# ]

# labels = [
#     r"$\bf{Output\ Types}$",
#     "Coordinates", "Allocentric", "Egocentric",
#     r"$\bf{Input\ Formats}$",
#     "Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII",
#     # r"$\bf{Models}$",
#     # "Gemini 2.5 Pro", "Gemini 2.5 Flash-Lite",
#     # r"$\bf{Maze\ Styles\ and\ Complexities\ (Low -> High)}$",
#     # "Occupancy Grid, 7x7, 13x13, 31x31", "Line Wall, 3x3, 6x6, 15x15"
#         r"$\bf{Maze\ Styles}$",
#     "Occupancy Grid", "Line Wall"
# ]

# axes[1,1].legend(
#     handles,
#     labels,
#     handler_map={tuple: HandlerTuple(ndivide=None)},
#     loc='center left',
#     bbox_to_anchor=(1.02, 0.5),
#     title="Legend"
# )

# # Place legend outside the plot on the right
# # axes[1,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Representation, Complexity, Output Type, Model")


# axes[0,0].set_title("3x3 and 7x7, Gemini 2.5 Flash-Lite")
# axes[0,1].set_title("3x3 and 7x7, Gemini 2.5 Pro")
# axes[1,0].set_title("6x6 and 13x13, Gemini 2.5 Flash-Lite")
# axes[1,1].set_title("6x6 and 13x13, Gemini 2.5 Pro")
# axes[2,0].set_title("15x15 and 31x31, Gemini 2.5 Flash-Lite")
# axes[2,1].set_title("15x15 and 31x31, Gemini 2.5 Pro")

# plt.suptitle("Absolute Number of Correct Steps vs. Cost Per Task", fontweight= 'bold')

# plt.tight_layout(rect=[0, 0, 0.97, 1])  # leave 15% of width for legend





# plt.show()
