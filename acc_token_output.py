
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataframe_image as dfi
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple, HandlerBase
from matplotlib import rcParams
representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']
# X-axis labels
x_labels = ['Coordinates', 'Allocentric', 'Egocentric']
x_vals = np.arange(len(x_labels))

# 3x3 NR - COORDS - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_NR_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 42.857142857142854, 100.0, 100.0])
line_NR_coords_jpg_3 = np.array([40.0, 20.0, 40.0, 60.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_json_3 = np.array([100.0, 20.0, 60.0, 20.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_tokenized_txt_3 = np.array([20.0, 0.0, 0.0, 60.0, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 20.0])
occupancy_NR_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_ascii_txt_3 = np.array([0.0, 110.00000000000001, 0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 110.00000000000001])
occupancy_NR_coords_jpg_3 = np.array([0.0, 0.0, 55.55555555555556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_3 = np.array([100.0, 110.00000000000001, 100.0, 110.00000000000001, 7.6923076923076925, 100.0, 110.00000000000001, 100.0, 100.0, 110.00000000000001])
occupancy_NR_coords_tokenized_txt_3 = np.array([11.11111111111111, 110.00000000000001, 100.0, 100.0, 7.6923076923076925, 11.11111111111111, 100.0, 100.0, 7.6923076923076925, 110.00000000000001])
# Output tokens
line_NR_coords_adj_json_output_tokens_3 = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 29.0, 29.0, 21.0])
line_NR_coords_adj_txt_output_tokens_3 = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 21.0, 29.0, 21.0])
line_NR_coords_jpg_output_tokens_3 = np.array([21, 21, 33, 21.0, 21.0, 21.0, 29.0, 21.0, 21.0, 21.0])
line_NR_coords_json_output_tokens_3 = np.array([21, 21, 21, 17.0, 21.0, 21.0, 17.0, 29.0, 21.0, 21.0])
line_NR_coords_tokenized_txt_output_tokens_3 = np.array([21, 25, 13, 29.0, 17.0, 17.0, 25.0, 21.0, 17.0, 29.0])
occupancy_NR_coords_adj_json_output_tokens_3 = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_NR_coords_adj_txt_output_tokens_3 = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_NR_coords_ascii_txt_output_tokens_3 = np.array([57, 57, 125, 53.0, 41.0, 45.0, 57.0, 41.0, 57.0, 53.0])
occupancy_NR_coords_jpg_output_tokens_3 = np.array([45, 49, 41, 49.0, 73.0, 45.0, 65.0, 41.0, 53.0, 57.0])
occupancy_NR_coords_json_output_tokens_3 = np.array([37, 53, 37, 53.0, 69.0, 37.0, 53.0, 53.0, 53.0, 101.0])
occupancy_NR_coords_tokenized_txt_output_tokens_3 = np.array([41, 53, 37, 37, 49.0, 65.0, 37.0, 53.0, 53.0, 53])

avg_line_NR_coords_jpg_3 = np.mean(line_NR_coords_jpg_3)
avg_line_NR_coords_json_3 = np.mean(line_NR_coords_json_3)
avg_occupancy_NR_coords_jpg_3 = np.mean(occupancy_NR_coords_jpg_3)
avg_occupancy_NR_coords_json_3 = np.mean(occupancy_NR_coords_json_3)
avg_line_NR_coords_adj_json_3 = np.mean(line_NR_coords_adj_json_3)
avg_line_NR_coords_adj_txt_3 = np.mean(line_NR_coords_adj_txt_3)
avg_line_NR_coords_tokenized_txt_3 = np.mean(line_NR_coords_tokenized_txt_3)
avg_occupancy_NR_coords_adj_json_3 = np.mean(occupancy_NR_coords_adj_json_3)
avg_occupancy_NR_coords_adj_txt_3 = np.mean(occupancy_NR_coords_adj_txt_3)
avg_occupancy_NR_coords_ascii_txt_3 = np.mean(occupancy_NR_coords_ascii_txt_3)
avg_occupancy_NR_coords_tokenized_txt_3 = np.mean(occupancy_NR_coords_tokenized_txt_3)
avg_line_NR_coords_jpg_output_3 = np.mean(line_NR_coords_jpg_output_tokens_3)
avg_line_NR_coords_json_output_3 = np.mean(line_NR_coords_json_output_tokens_3)
avg_occupancy_NR_coords_jpg_output_3 = np.mean(occupancy_NR_coords_jpg_output_tokens_3)
avg_occupancy_NR_coords_json_output_3 = np.mean(occupancy_NR_coords_json_output_tokens_3)
avg_line_NR_coords_adj_json_output_3 = np.mean(line_NR_coords_adj_json_output_tokens_3)
avg_line_NR_coords_adj_txt_output_3 = np.mean(line_NR_coords_adj_txt_output_tokens_3)
avg_line_NR_coords_tokenized_txt_output_3 = np.mean(line_NR_coords_tokenized_txt_output_tokens_3)
avg_occupancy_NR_coords_adj_json_output_3 = np.mean(occupancy_NR_coords_adj_json_output_tokens_3)
avg_occupancy_NR_coords_adj_txt_output_3 = np.mean(occupancy_NR_coords_adj_txt_output_tokens_3)
avg_occupancy_NR_coords_ascii_txt_output_3 = np.mean(occupancy_NR_coords_ascii_txt_output_tokens_3)
avg_occupancy_NR_coords_tokenized_txt_output_3 = np.mean(occupancy_NR_coords_tokenized_txt_output_tokens_3)


# 3x3NR - ALLO - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_allo_adj_json_3 = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 100.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_adj_txt_3 = np.array([0.0, 100.0, 0.0, 100.0, 0.0, 0.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_jpg_3 = np.array([50.0, 0.0, 50.0, 100.0, 33.33333333333333, 50.0, 100.0, 0.0, 0.0, 0.0])
line_NR_allo_json_3 = np.array([100.0, 0.0, 100.0, 0.0, 33.33333333333333, 100.0, 0.0, 0.0, 33.33333333333333, 0.0])
line_NR_allo_tokenized_txt_3 = np.array([0.0, 100.0, 0.0, 25.0, 0.0, 0.0, 25.0, 33.33333333333333, 0.0, 25.0])
occupancy_NR_allo_adj_json_3 = np.array([50.0, 25.0, 75.0, 110.00000000000001, 0.0, 50.0, 110.00000000000001, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_NR_allo_adj_txt_3 = np.array([62.5, 25.0, 0.0, 37.5, 33.33333333333333, 25.0, 37.5, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_NR_allo_ascii_txt_3 = np.array([0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 62.5, 33.33333333333333, 33.33333333333333, 0.0])
occupancy_NR_allo_jpg_3 = np.array([12.5, 0.0, 12.5, 0.0, 8.333333333333332, 12.5, 12.5, 8.333333333333332, 8.333333333333332, 0.0])
occupancy_NR_allo_json_3 = np.array([62.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 33.33333333333333, 0.0, 87.5])
occupancy_NR_allo_tokenized_txt_3 = np.array([0.0, 0.0, 0.0, 50.0, 8.333333333333332, 12.5, 0.0, 8.333333333333332, 0.0, 110.00000000000001])

# Output tokens
line_NR_allo_adj_json_output_tokens_3 = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 5.0, 7.0])
line_NR_allo_adj_txt_output_tokens_3 = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_jpg_output_tokens_3 = np.array([7.0, 218.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_json_output_tokens_3 = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_tokenized_txt_output_tokens_3 = np.array([5.0, 7.0, 5.0, 7.0, 7.0, 7.0, 7.0, 7.0, 5.0, 7.0])
occupancy_NR_allo_adj_json_output_tokens_3 = np.array([17.0, 15.0, 21.0, 19.0, 21.0, 17.0, 19.0, 19.0, 650.0, 19.0])
occupancy_NR_allo_adj_txt_output_tokens_3 = np.array([21.0, 17.0, 1734.0, 15.0, 13.0, 17.0, 15.0, 15.0, 650.0, 19.0])
occupancy_NR_allo_ascii_txt_output_tokens_3 = np.array([43.0, 29.0, 43.0, 23.0, 39.0, 31.0, 25.0, 31.0, 21.0, 29.0])
occupancy_NR_allo_jpg_output_tokens_3 = np.array([21.0, 15.0, 15.0, 49.0, 21.0, 43.0, 19.0, 17.0, 21.0, 198.0])
occupancy_NR_allo_json_output_tokens_3 = np.array([17.0, 21.0, 45.0, 21.0, 29.0, 31.0, 21.0, 21.0, 650.0, 35.0])
occupancy_NR_allo_tokenized_txt_output_tokens_3 = np.array([33.0, 59.0, 4000.0, 650.0, 31.0, 650.0, 31.0, 25.0, 650.0, 650])

avg_line_NR_allo_jpg_3 = np.mean(line_NR_allo_jpg_3)
avg_line_NR_allo_json_3 = np.mean(line_NR_allo_json_3)
avg_occupancy_NR_allo_jpg_3 = np.mean(occupancy_NR_allo_jpg_3)
avg_occupancy_NR_allo_json_3 = np.mean(occupancy_NR_allo_json_3)
avg_line_NR_allo_adj_json_3 = np.mean(line_NR_allo_adj_json_3)
avg_line_NR_allo_adj_txt_3 = np.mean(line_NR_allo_adj_txt_3)
avg_line_NR_allo_tokenized_txt_3 = np.mean(line_NR_allo_tokenized_txt_3)
avg_occupancy_NR_allo_adj_json_3 = np.mean(occupancy_NR_allo_adj_json_3)
avg_occupancy_NR_allo_adj_txt_3 = np.mean(occupancy_NR_allo_adj_txt_3)
avg_occupancy_NR_allo_ascii_txt_3 = np.mean(occupancy_NR_allo_ascii_txt_3)
avg_occupancy_NR_allo_tokenized_txt_3 = np.mean(occupancy_NR_allo_tokenized_txt_3)

avg_line_NR_allo_jpg_output_3 = np.mean(line_NR_allo_jpg_output_tokens_3)
avg_line_NR_allo_json_output_3 = np.mean(line_NR_allo_json_output_tokens_3)
avg_occupancy_NR_allo_jpg_output_3 = np.mean(occupancy_NR_allo_jpg_output_tokens_3)
avg_occupancy_NR_allo_json_output_3 = np.mean(occupancy_NR_allo_json_output_tokens_3)
avg_line_NR_allo_adj_json_output_3 = np.mean(line_NR_allo_adj_json_output_tokens_3)
avg_line_NR_allo_adj_txt_output_3 = np.mean(line_NR_allo_adj_txt_output_tokens_3)
avg_line_NR_allo_tokenized_txt_output_3 = np.mean(line_NR_allo_tokenized_txt_output_tokens_3)
avg_occupancy_NR_allo_adj_json_output_3 = np.mean(occupancy_NR_allo_adj_json_output_tokens_3)
avg_occupancy_NR_allo_adj_txt_output_3 = np.mean(occupancy_NR_allo_adj_txt_output_tokens_3)
avg_occupancy_NR_allo_ascii_txt_output_3 = np.mean(occupancy_NR_allo_ascii_txt_output_tokens_3)
avg_occupancy_NR_allo_tokenized_txt_output_3 = np.mean(occupancy_NR_allo_tokenized_txt_output_tokens_3)


# 3x3 NR - EGO - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_ego_adj_json_3 = np.array([25.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json_3 = np.array([25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json_3 = np.array([0.0, 0.0, 12.5, 0.0, 8.333333333333332, 0.0, 0.0, 0.0, 8.333333333333332, 0.0])
occupancy_NR_ego_adj_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_3 = np.array([0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_json_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# Output tokens
line_NR_ego_adj_json_output_tokens_3 = np.array([13.0, 4000.0, 11.0, 15.0, 15.0, 13.0, 15.0, 13.0, 15.0, 15.0])
line_NR_ego_adj_txt_output_tokens_3 = np.array([15.0, 17.0, 13.0, 11.0, 13.0, 13.0, 15.0, 13.0, 13.0, 13.0])
line_NR_ego_jpg_output_tokens_3 = np.array([23.0, 17.0, 15.0, 15.0, 261.0, 15.0, 15.0, 650.0, 19.0, 19.0])
line_NR_ego_json_output_tokens_3 = np.array([11.0, 11.0, 13.0, 19.0, 13.0, 21.0, 17.0, 11.0, 11.0, 11.0])
line_NR_ego_tokenized_txt_output_tokens_3 = np.array([17.0, 4000.0, 17.0, 649.0, 650.0, 517.0, 650.0, 47.0, 650.0, 650.0])
occupancy_NR_ego_adj_json_output_tokens_3 = np.array([33.0, 4000.0, 31.0, 99.0, 49.0, 35.0, 41.0, 39.0, 47.0, 29.0])
occupancy_NR_ego_adj_txt_output_tokens_3 = np.array([4000.0, 49.0, 4000.0, 49.0, 650.0, 436.0, 49.0, 45.0, 650.0, 49.0])
occupancy_NR_ego_ascii_txt_output_tokens_3 = np.array([133.0, 4000.0, 4000.0, 35.0, 650.0, 51.0, 650.0, 51.0, 650.0, 47.0])
occupancy_NR_ego_jpg_output_tokens_3 = np.array([25.0, 27.0, 33.0, 23.0, 27.0, 650.0, 35.0, 27.0, 35.0, 43.0])
occupancy_NR_ego_json_output_tokens_3 = np.array([4000.0, 4000.0, 79.0, 55.0, 650.0, 650.0, 650.0, 650.0, 41.0, 650.0])
occupancy_NR_ego_tokenized_txt_output_tokens_3 = np.array([4000.0, 1561.0, 1029.0, 49.0, 650.0, 650.0, 650.0, 650.0, 45.0, 650])


avg_line_NR_ego_jpg_3 = np.mean(line_NR_ego_jpg_3)
avg_line_NR_ego_json_3 = np.mean(line_NR_ego_json_3)
avg_occupancy_NR_ego_jpg_3 = np.mean(occupancy_NR_ego_jpg_3)
avg_occupancy_NR_ego_json_3 = np.mean(occupancy_NR_ego_json_3)
avg_line_NR_ego_adj_json_3 = np.mean(line_NR_ego_adj_json_3)
avg_line_NR_ego_adj_txt_3 = np.mean(line_NR_ego_adj_txt_3)
avg_line_NR_ego_tokenized_txt_3 = np.mean(line_NR_ego_tokenized_txt_3)
avg_occupancy_NR_ego_adj_json_3 = np.mean(occupancy_NR_ego_adj_json_3)
avg_occupancy_NR_ego_adj_txt_3 = np.mean(occupancy_NR_ego_adj_txt_3)
avg_occupancy_NR_ego_ascii_txt_3 = np.mean(occupancy_NR_ego_ascii_txt_3)
avg_occupancy_NR_ego_tokenized_txt_3 = np.mean(occupancy_NR_ego_tokenized_txt_3)
avg_line_NR_ego_jpg_output_3 = np.mean(line_NR_ego_jpg_output_tokens_3)
avg_line_NR_ego_json_output_3 = np.mean(line_NR_ego_json_output_tokens_3)
avg_occupancy_NR_ego_jpg_output_3 = np.mean(occupancy_NR_ego_jpg_output_tokens_3)
avg_occupancy_NR_ego_json_output_3 = np.mean(occupancy_NR_ego_json_output_tokens_3)
avg_line_NR_ego_adj_json_output_3 = np.mean(line_NR_ego_adj_json_output_tokens_3)
avg_line_NR_ego_adj_txt_output_3 = np.mean(line_NR_ego_adj_txt_output_tokens_3)
avg_line_NR_ego_tokenized_txt_output_3 = np.mean(line_NR_ego_tokenized_txt_output_tokens_3)
avg_occupancy_NR_ego_adj_json_output_3 = np.mean(occupancy_NR_ego_adj_json_output_tokens_3)
avg_occupancy_NR_ego_adj_txt_output_3 = np.mean(occupancy_NR_ego_adj_txt_output_tokens_3)
avg_occupancy_NR_ego_ascii_txt_output_3 = np.mean(occupancy_NR_ego_ascii_txt_output_tokens_3)
avg_occupancy_NR_ego_tokenized_txt_output_3 = np.mean(occupancy_NR_ego_tokenized_txt_output_tokens_3)


# 3x3 R - COORDS -  - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_jpg_3 = np.array([40.0, 100.0, 100.0, 100.0, 28.57142857142857, 40.0, 40.0, 100.0, 100.0, 100.0])
line_R_coords_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_ascii_txt_3 = np.array([22.22222222222222, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 46.15384615384615, 77.77777777777779])
occupancy_R_coords_jpg_3 = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556, 0.0, 7.6923076923076925, 11.11111111111111, 33.33333333333333, 0.0, 7.6923076923076925, 100.0])
occupancy_R_coords_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Output tokens
line_R_coords_adj_json_output_tokens_3 = np.array([1625.0, 1289.0, 898.0, 1267.0, 1428.0, 1180.0, 890.0, 1952.0, 4861.0, 1630.0])
line_R_coords_adj_txt_output_tokens_3 = np.array([2264.0, 2798.0, 2034.0, 1651.0, 2376.0, 2688.0, 1336.0, 2837.0, 3894.0, 2971.0])
line_R_coords_jpg_output_tokens_3 = np.array([16131.0, 5588.0, 3890.0, 10788.0, 4661.0, 11346.0, 3181.0, 1811.0, 1099.0, 4869.0])
line_R_coords_json_output_tokens_3 = np.array([1475.0, 1115.0, 1274.0, 1052.0, 2496.0, 1404.0, 1518.0, 1683.0, 1329.0, 2682.0])
line_R_coords_tokenized_txt_output_tokens_3 = np.array([1408.0, 1207.0, 1637.0, 1361.0, 2974.0, 1260.0, 1333.0, 1614.0, 1760.0, 1755.0])
occupancy_R_coords_adj_json_output_tokens_3 = np.array([2077.0, 2469.0, 3461.0, 3086.0, 3367.0, 1825.0, 4614.0, 3247.0, 5275.0, 2957.0])
occupancy_R_coords_adj_txt_output_tokens_3 = np.array([3621.0, 4114.0, 3696.0, 3970.0, 6715.0, 3728.0, 3978.0, 2455.0, 6534.0, 1944.0])
occupancy_R_coords_ascii_txt_output_tokens_3 = np.array([9407.0, 8884.0, 1926.0, 6484.0, 2357.0, 3312.0, 2518.0, 2395.0, 2447.0, 2544.0])
occupancy_R_coords_jpg_output_tokens_3 = np.array([1713.0, 1428.0, 7030.0, 3242.0, 1008.0, 1835.0, 832.0, 2965.0, 1402.0, 3035.0])
occupancy_R_coords_json_output_tokens_3 = np.array([3193.0, 2760.0, 4692.0, 5823.0, 2167.0, 3396.0, 4635.0, 2380.0, 4836.0, 3947.0])
occupancy_R_coords_tokenized_txt_output_tokens_3 = np.array([4248.0, 2453.0, 2759.0, 3372.0, 5675.0, 4171.0, 2481.0, 4070.0, 1732.0, 5926])

avg_line_R_coords_jpg_3 = np.mean(line_R_coords_jpg_3)
avg_line_R_coords_json_3 = np.mean(line_R_coords_json_3)
avg_occupancy_R_coords_jpg_3 = np.mean(occupancy_R_coords_jpg_3)
avg_occupancy_R_coords_json_3 = np.mean(occupancy_R_coords_json_3)
avg_line_R_coords_adj_json_3 = np.mean(line_R_coords_adj_json_3)
avg_line_R_coords_adj_txt_3 = np.mean(line_R_coords_adj_txt_3)
avg_line_R_coords_tokenized_txt_3 = np.mean(line_R_coords_tokenized_txt_3)
avg_occupancy_R_coords_adj_json_3 = np.mean(occupancy_R_coords_adj_json_3)
avg_occupancy_R_coords_adj_txt_3 = np.mean(occupancy_R_coords_adj_txt_3)
avg_occupancy_R_coords_ascii_txt_3 = np.mean(occupancy_R_coords_ascii_txt_3)
avg_occupancy_R_coords_tokenized_txt_3 = np.mean(occupancy_R_coords_tokenized_txt_3)

avg_line_R_coords_jpg_output_3 = np.mean(line_R_coords_jpg_output_tokens_3)
avg_line_R_coords_json_output_3 = np.mean(line_R_coords_json_output_tokens_3)
avg_occupancy_R_coords_jpg_output_3 = np.mean(occupancy_R_coords_jpg_output_tokens_3)
avg_occupancy_R_coords_json_output_3 = np.mean(occupancy_R_coords_json_output_tokens_3)
avg_line_R_coords_adj_json_output_3 = np.mean(line_R_coords_adj_json_output_tokens_3)
avg_line_R_coords_adj_txt_output_3 = np.mean(line_R_coords_adj_txt_output_tokens_3)
avg_line_R_coords_tokenized_txt_output_3 = np.mean(line_R_coords_tokenized_txt_output_tokens_3)
avg_occupancy_R_coords_adj_json_output_3 = np.mean(occupancy_R_coords_adj_json_output_tokens_3)
avg_occupancy_R_coords_adj_txt_output_3 = np.mean(occupancy_R_coords_adj_txt_output_tokens_3)
avg_occupancy_R_coords_ascii_txt_output_3 = np.mean(occupancy_R_coords_ascii_txt_output_tokens_3)
avg_occupancy_R_coords_tokenized_txt_output_3 = np.mean(occupancy_R_coords_tokenized_txt_output_tokens_3)

# 3x3 R - ALLO -  - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_allo_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_jpg_3 = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 25.0, 100.0, 16.666666666666664, 100.0, 0.0])
line_R_allo_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_ascii_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 41.66666666666667, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_jpg_3 = np.array([0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 25.0, 16.666666666666664, 0.0, 37.5])
occupancy_R_allo_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Output tokens
line_R_allo_adj_json_output_tokens_3 = np.array([1729.0, 1338.0, 1698.0, 1356.0, 2081.0, 1839.0, 1446.0, 3182.0, 2031.0, 1978.0])
line_R_allo_adj_txt_output_tokens_3 = np.array([2080.0, 4596.0, 2232.0, 1912.0, 3297.0, 1257.0, 2799.0, 1641.0, 2194.0, 2137.0])
line_R_allo_jpg_output_tokens_3 = np.array([14536.0, 2225.0, 1313.0, 1583.0, 565.0, 743.0, 1530.0, 7230.0, 6033.0, 1339.0])
line_R_allo_json_output_tokens_3 = np.array([1366.0, 1420.0, 1475.0, 1144.0, 1807.0, 1492.0, 1762.0, 1599.0, 1682.0, 2604.0])
line_R_allo_tokenized_txt_output_tokens_3 = np.array([1403.0, 1250.0, 1290.0, 933.0, 2456.0, 2327.0, 1276.0, 3675.0, 2060.0, 1521.0])
occupancy_R_allo_adj_json_output_tokens_3 = np.array([4853.0, 3989.0, 3209.0, 3350.0, 7269.0, 3599.0, 5583.0, 5676.0, 3584.0, 3374.0])
occupancy_R_allo_adj_txt_output_tokens_3 = np.array([7175.0, 7839.0, 4911.0, 8476.0, 7901.0, 4069.0, 6469.0, 5701.0, 6608.0, 4476.0])
occupancy_R_allo_ascii_txt_output_tokens_3 = np.array([3455.0, 3764.0, 4552.0, 3401.0, 1849.0, 6728.0, 2600.0, 4200.0, 3523.0, 3007.0])
occupancy_R_allo_jpg_output_tokens_3 = np.array([9275.0, 2057.0, 17922.0, 2315.0, 1158.0, 3392.0, 5907.0, 7009.0, 8449.0, 991.0])
occupancy_R_allo_json_output_tokens_3 = np.array([4247.0, 3624.0, 3078.0, 3722.0, 7561.0, 3847.0, 2845.0, 2169.0, 10791.0, 3687.0])
occupancy_R_allo_tokenized_txt_output_tokens_3 = np.array([2474.0, 2171.0, 1444.0, 3519.0, 3134.0, 4225.0, 3933.0, 3277.0, 3956.0, 2010])

avg_line_R_allo_jpg_3 = np.mean(line_R_allo_jpg_3)
avg_line_R_allo_json_3 = np.mean(line_R_allo_json_3)
avg_occupancy_R_allo_jpg_3 = np.mean(occupancy_R_allo_jpg_3)
avg_occupancy_R_allo_json_3 = np.mean(occupancy_R_allo_json_3)
avg_line_R_allo_adj_json_3 = np.mean(line_R_allo_adj_json_3)
avg_line_R_allo_adj_txt_3 = np.mean(line_R_allo_adj_txt_3)
avg_line_R_allo_tokenized_txt_3 = np.mean(line_R_allo_tokenized_txt_3)
avg_occupancy_R_allo_adj_json_3 = np.mean(occupancy_R_allo_adj_json_3)
avg_occupancy_R_allo_adj_txt_3 = np.mean(occupancy_R_allo_adj_txt_3)
avg_occupancy_R_allo_ascii_txt_3 = np.mean(occupancy_R_allo_ascii_txt_3)
avg_occupancy_R_allo_tokenized_txt_3 = np.mean(occupancy_R_allo_tokenized_txt_3)

avg_line_R_allo_jpg_output_3 = np.mean(line_R_allo_jpg_output_tokens_3)
avg_line_R_allo_json_output_3 = np.mean(line_R_allo_json_output_tokens_3)
avg_occupancy_R_allo_jpg_output_3 = np.mean(occupancy_R_allo_jpg_output_tokens_3)
avg_occupancy_R_allo_json_output_3 = np.mean(occupancy_R_allo_json_output_tokens_3)
avg_line_R_allo_adj_json_output_3 = np.mean(line_R_allo_adj_json_output_tokens_3)
avg_line_R_allo_adj_txt_output_3 = np.mean(line_R_allo_adj_txt_output_tokens_3)
avg_line_R_allo_tokenized_txt_output_3 = np.mean(line_R_allo_tokenized_txt_output_tokens_3)
avg_occupancy_R_allo_adj_json_output_3 = np.mean(occupancy_R_allo_adj_json_output_tokens_3)
avg_occupancy_R_allo_adj_txt_output_3 = np.mean(occupancy_R_allo_adj_txt_output_tokens_3)
avg_occupancy_R_allo_ascii_txt_output_3 = np.mean(occupancy_R_allo_ascii_txt_output_tokens_3)
avg_occupancy_R_allo_tokenized_txt_output_3 = np.mean(occupancy_R_allo_tokenized_txt_output_tokens_3)



# 3x3 R - EGO -  - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_ego_adj_json_3 = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_adj_txt_3 = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_jpg_3 = np.array([25.0, 0.0, 50.0, 50.0, 33.33333333333333, 0.0, 0.0, 100.0, 16.666666666666664, 110.00000000000001])
line_R_ego_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_ascii_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 100.0, 100.0, 75.0])
occupancy_R_ego_jpg_3 = np.array([12.5, 0.0, 0.0, 50.0, 33.33333333333333, 0.0, 12.5, 91.66666666666666, 8.333333333333332, 37.5])
occupancy_R_ego_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])


# Output tokens
line_R_ego_adj_txt_output_tokens_3 = np.array([2930.0, 3587.0, 1933.0, 2641.0, 3112.0, 4863.0, 2100.0, 3512.0, 4410.0, 4022.0])
line_R_ego_jpg_output_tokens_3 = np.array([8539.0, 4203.0, 1105.0, 6439.0, 2083.0, 1169.0, 2926.0, 6573.0, 956.0, 3620.0])
line_R_ego_adj_json_output_tokens_3 = np.array([3560.0, 2534.0, 2248.0, 5136.0, 2161.0, 1990.0, 2845.0, 3926.0, 3096.0, 2119.0])
line_R_ego_json_output_tokens_3 = np.array([2401.0, 3116.0, 2388.0, 2223.0, 1786.0, 2653.0, 2229.0, 2922.0, 2328.0, 1745.0])
line_R_ego_tokenized_txt_output_tokens_3 = np.array([3418.0, 3481.0, 2694.0, 2831.0, 5562.0, 1329.0, 3137.0, 4427.0, 4192.0, 4997.0])
occupancy_R_ego_adj_json_output_tokens_3 = np.array([2912.0, 2264.0, 2449.0, 5428.0, 3254.0, 5593.0, 4609.0, 9388.0, 2930.0, 3499.0])
occupancy_R_ego_adj_txt_output_tokens_3 = np.array([5534.0, 2162.0, 5607.0, 3270.0, 3786.0, 5441.0, 6224.0, 8755.0, 7211.0, 3472.0])
occupancy_R_ego_ascii_txt_output_tokens_3 = np.array([7469.0, 3371.0, 3412.0, 9243.0, 4083.0, 2292.0, 3412.0, 8108.0, 6947.0, 3962.0])
occupancy_R_ego_jpg_output_tokens_3 = np.array([4816.0, 9362.0, 2226.0, 1635.0, 2873.0, 10455.0, 10761.0, 2276.0, 3848.0, 3554.0])
occupancy_R_ego_json_output_tokens_3 = np.array([4612.0, 5353.0, 4658.0, 4597.0, 4898.0, 3064.0, 3409.0, 4365.0, 4804.0, 4792.0])
occupancy_R_ego_tokenized_txt_output_tokens_3 = np.array([3530.0, 4654.0, 2890.0, 4121.0, 5383.0, 4001.0, 7766.0, 3142.0, 3579.0, 3581])

avg_line_R_ego_jpg_3 = np.mean(line_R_ego_jpg_3)
avg_line_R_ego_json_3 = np.mean(line_R_ego_json_3)
avg_occupancy_R_ego_jpg_3 = np.mean(occupancy_R_ego_jpg_3)
avg_occupancy_R_ego_json_3 = np.mean(occupancy_R_ego_json_3)
avg_line_R_ego_adj_json_3 = np.mean(line_R_ego_adj_json_3)
avg_line_R_ego_adj_txt_3 = np.mean(line_R_ego_adj_txt_3)
avg_line_R_ego_tokenized_txt_3 = np.mean(line_R_ego_tokenized_txt_3)
avg_occupancy_R_ego_adj_json_3 = np.mean(occupancy_R_ego_adj_json_3)
avg_occupancy_R_ego_adj_txt_3 = np.mean(occupancy_R_ego_adj_txt_3)
avg_occupancy_R_ego_ascii_txt_3 = np.mean(occupancy_R_ego_ascii_txt_3)
avg_occupancy_R_ego_tokenized_txt_3 = np.mean(occupancy_R_ego_tokenized_txt_3)

avg_line_R_ego_jpg_output_3 = np.mean(line_R_ego_jpg_output_tokens_3)
avg_line_R_ego_json_output_3 = np.mean(line_R_ego_json_output_tokens_3)
avg_occupancy_R_ego_jpg_output_3 = np.mean(occupancy_R_ego_jpg_output_tokens_3)
avg_occupancy_R_ego_json_output_3 = np.mean(occupancy_R_ego_json_output_tokens_3)
avg_line_R_ego_adj_json_output_3 = np.mean(line_R_ego_adj_json_output_tokens_3)
avg_line_R_ego_adj_txt_output_3 = np.mean(line_R_ego_adj_txt_output_tokens_3)
avg_line_R_ego_tokenized_txt_output_3 = np.mean(line_R_ego_tokenized_txt_output_tokens_3)
avg_occupancy_R_ego_adj_json_output_3 = np.mean(occupancy_R_ego_adj_json_output_tokens_3)
avg_occupancy_R_ego_adj_txt_output_3 = np.mean(occupancy_R_ego_adj_txt_output_tokens_3)
avg_occupancy_R_ego_ascii_txt_output_3 = np.mean(occupancy_R_ego_ascii_txt_output_tokens_3)
avg_occupancy_R_ego_tokenized_txt_output_3 = np.mean(occupancy_R_ego_tokenized_txt_output_tokens_3)


# -----------------------------------------------------------------------------------------------------------------------------------



# 6x6 NR - COORDS - 1-10 ----------------------------------------------------------------
# Accuracy
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

# Output Tokens
line_NR_coords_adj_json_output_tokens_6 = np.array([45.0, 77.0, 69.0, 93.0, 61.0, 101.0, 141.0, 45.0, 53.0, 69.0])
line_NR_coords_adj_txt_output_tokens_6 = np.array([45.0, 45.0, 69.0, 61.0, 61.0, 85.0, 149.0, 45.0, 53.0, 650.0])
line_NR_coords_jpg_output_tokens_6 = np.array([41.0, 45.0, 45.0, 45.0, 45.0, 45.0, 53.0, 45.0, 45.0, 45.0])
line_NR_coords_json_output_tokens_6 = np.array([45.0, 45.0, 49.0, 45.0, 45.0, 45.0, 45.0, 53.0, 53.0, 45.0])
line_NR_coords_tokenized_txt_output_tokens_6 = np.array([45.0, 53.0, 45.0, 53.0, 45.0, 53.0, 61.0, 45.0, 89.0, 45.0])
occupancy_NR_coords_adj_json_output_tokens_6 = np.array([150.0, 184.0, 302.0, 236.0, 123.0, 181.0, 214.0, 91.0, 216.0, 267.0])
occupancy_NR_coords_adj_txt_output_tokens_6 = np.array([87.0, 163.0, 115.0, 244.0, 123.0, 115.0, 246.0, 91.0, 107.0, 284.0])
occupancy_NR_coords_ascii_txt_output_tokens_6 = np.array([119.0, 281.0, 157.0, 139.0, 120.0, 165.0, 117.0, 235.0, 182.0, 150.0])
occupancy_NR_coords_jpg_output_tokens_6 = np.array([152.0, 108.0, 192.0, 125.0, 107.0, 151.0, 296.0, 219.0, 283.0, 171.0])
occupancy_NR_coords_json_output_tokens_6 = np.array([99.0, 187.0, 162.0, 154.0, 136.0, 166.0, 172.0, 139.0, 149.0, 147.0])
occupancy_NR_coords_tokenized_txt_output_tokens_6 = np.array([269.0, 244.0, 171.0, 650.0, 229.0, 284.0, 232.0, 179.0, 269.0, 196])

avg_line_NR_coords_jpg_6 = np.mean(line_NR_coords_jpg_6)
avg_line_NR_coords_json_6 = np.mean(line_NR_coords_json_6)
avg_occupancy_NR_coords_jpg_6 = np.mean(occupancy_NR_coords_jpg_6)
avg_occupancy_NR_coords_json_6 = np.mean(occupancy_NR_coords_json_6)
avg_line_NR_coords_adj_json_6 = np.mean(line_NR_coords_adj_json_6)
avg_line_NR_coords_adj_txt_6 = np.mean(line_NR_coords_adj_txt_6)
avg_line_NR_coords_tokenized_txt_6 = np.mean(line_NR_coords_tokenized_txt_6)
avg_occupancy_NR_coords_adj_json_6 = np.mean(occupancy_NR_coords_adj_json_6)
avg_occupancy_NR_coords_adj_txt_6 = np.mean(occupancy_NR_coords_adj_txt_6)
avg_occupancy_NR_coords_ascii_txt_6 = np.mean(occupancy_NR_coords_ascii_txt_6)
avg_occupancy_NR_coords_tokenized_txt_6 = np.mean(occupancy_NR_coords_tokenized_txt_6)

avg_line_NR_coords_jpg_output_6 = np.mean(line_NR_coords_jpg_output_tokens_6)
avg_line_NR_coords_json_output_6 = np.mean(line_NR_coords_json_output_tokens_6)
avg_occupancy_NR_coords_jpg_output_6 = np.mean(occupancy_NR_coords_jpg_output_tokens_6)
avg_occupancy_NR_coords_json_output_6 = np.mean(occupancy_NR_coords_json_output_tokens_6)
avg_line_NR_coords_adj_json_output_6 = np.mean(line_NR_coords_adj_json_output_tokens_6)
avg_line_NR_coords_adj_txt_output_6 = np.mean(line_NR_coords_adj_txt_output_tokens_6)
avg_line_NR_coords_tokenized_txt_output_6 = np.mean(line_NR_coords_tokenized_txt_output_tokens_6)
avg_occupancy_NR_coords_adj_json_output_6 = np.mean(occupancy_NR_coords_adj_json_output_tokens_6)
avg_occupancy_NR_coords_adj_txt_output_6 = np.mean(occupancy_NR_coords_adj_txt_output_tokens_6)
avg_occupancy_NR_coords_ascii_txt_output_6 = np.mean(occupancy_NR_coords_ascii_txt_output_tokens_6)
avg_occupancy_NR_coords_tokenized_txt_output_6 = np.mean(occupancy_NR_coords_tokenized_txt_output_tokens_6)

# 6x6 NR - ALLO - 1-10 ----------------------------------------------------------------
# Accuracy
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



# Output Tokens
line_NR_allo_adj_json_output_tokens_6 = np.array([19.0, 19.0, 23.0, 29.0, 29.0, 21.0, 19.0, 27.0, 31.0, 19.0])
line_NR_allo_adj_txt_output_tokens_6 = np.array([25.0, 19.0, 21.0, 29.0, 23.0, 23.0, 27.0, 27.0, 29.0, 23.0])
line_NR_allo_jpg_output_tokens_6 = np.array([31.0, 23.0, 21.0, 23.0, 31.0, 25.0, 45.0, 15.0, 27.0, 51.0])
line_NR_allo_json_output_tokens_6 = np.array([21.0, 49.0, 19.0, 29.0, 23.0, 23.0, 21.0, 21.0, 21.0, 21.0])
line_NR_allo_tokenized_txt_output_tokens_6 = np.array([43.0, 29.0, 117.0, 21.0, 650.0, 59.0, 27.0, 33.0, 650.0, 57.0])
occupancy_NR_allo_adj_json_output_tokens_6 = np.array([65.0, 53.0, 51.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_adj_txt_output_tokens_6 = np.array([650.0, 650.0, 189.0, 650.0, 53.0, 650.0, 650.0, 47.0, 650.0, 43.0])
occupancy_NR_allo_ascii_txt_output_tokens_6 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 0.0, 137.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_jpg_output_tokens_6 = np.array([61.0, 41.0, 65.0, 650.0, 650.0, 31.0, 41.0, 650.0, 41.0, 37.0])
occupancy_NR_allo_json_output_tokens_6 = np.array([650.0, 650.0, 650.0, 51.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_tokenized_txt_output_tokens_6 = np.array([650.0, 650.0, 85.0, 650.0, 0.0, 650.0, 650.0, 650.0, 650.0, 650])

avg_line_NR_allo_jpg_6 = np.mean(line_NR_allo_jpg_6)
avg_line_NR_allo_json_6 = np.mean(line_NR_allo_json_6)
avg_occupancy_NR_allo_jpg_6 = np.mean(occupancy_NR_allo_jpg_6)
avg_occupancy_NR_allo_json_6 = np.mean(occupancy_NR_allo_json_6)
avg_line_NR_allo_adj_json_6 = np.mean(line_NR_allo_adj_json_6)
avg_line_NR_allo_adj_txt_6 = np.mean(line_NR_allo_adj_txt_6)
avg_line_NR_allo_tokenized_txt_6 = np.mean(line_NR_allo_tokenized_txt_6)
avg_occupancy_NR_allo_adj_json_6 = np.mean(occupancy_NR_allo_adj_json_6)
avg_occupancy_NR_allo_adj_txt_6 = np.mean(occupancy_NR_allo_adj_txt_6)
avg_occupancy_NR_allo_ascii_txt_6 = np.mean(occupancy_NR_allo_ascii_txt_6)
avg_occupancy_NR_allo_tokenized_txt_6 = np.mean(occupancy_NR_allo_tokenized_txt_6)

avg_line_NR_allo_jpg_output_6 = np.mean(line_NR_allo_jpg_output_tokens_6)
avg_line_NR_allo_json_output_6 = np.mean(line_NR_allo_json_output_tokens_6)
avg_occupancy_NR_allo_jpg_output_6 = np.mean(occupancy_NR_allo_jpg_output_tokens_6)
avg_occupancy_NR_allo_json_output_6 = np.mean(occupancy_NR_allo_json_output_tokens_6)
avg_line_NR_allo_adj_json_output_6 = np.mean(line_NR_allo_adj_json_output_tokens_6)
avg_line_NR_allo_adj_txt_output_6 = np.mean(line_NR_allo_adj_txt_output_tokens_6)
avg_line_NR_allo_tokenized_txt_output_6 = np.mean(line_NR_allo_tokenized_txt_output_tokens_6)
avg_occupancy_NR_allo_adj_json_output_6 = np.mean(occupancy_NR_allo_adj_json_output_tokens_6)
avg_occupancy_NR_allo_adj_txt_output_6 = np.mean(occupancy_NR_allo_adj_txt_output_tokens_6)
avg_occupancy_NR_allo_ascii_txt_output_6 = np.mean(occupancy_NR_allo_ascii_txt_output_tokens_6)
avg_occupancy_NR_allo_tokenized_txt_output_6 = np.mean(occupancy_NR_allo_tokenized_txt_output_tokens_6)

# 6x6 NR - EGO - 1-10 ----------------------------------------------------------------
# Accuracy
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


# Output Tokens
line_NR_ego_adj_json_output_tokens_6 = np.array([57.0, 43.0, 47.0, 59.0, 43.0, 650.0, 111.0, 111.0, 59.0, 97.0])
line_NR_ego_adj_txt_output_tokens_6 = np.array([43.0, 650.0, 650.0, 105.0, 39.0, 53.0, 35.0, 81.0, 650.0, 650.0])
line_NR_ego_jpg_output_tokens_6 = np.array([51.0, 42.0, 80.0, 57.0, 650.0, 37.0, 411.0, 74.0, 31.0, 33.0])
line_NR_ego_json_output_tokens_6 = np.array([83.0, 51.0, 51.0, 47.0, 650.0, 49.0, 49.0, 35.0, 129.0, 47.0])
line_NR_ego_tokenized_txt_output_tokens_6 = np.array([296.0, 650.0, 650.0, 650.0, 650.0, 41.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_json_output_tokens_6 = np.array([650.0, 221.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_txt_output_tokens_6 = np.array([650.0, 650.0, 650.0, 417.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_ascii_txt_output_tokens_6 = np.array([650.0, 211.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_jpg_output_tokens_6 = np.array([71.0, 650.0, 93.0, 650.0, 650.0, 650.0, 79.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_json_output_tokens_6 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_tokenized_txt_output_tokens_6 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650])

avg_line_NR_ego_jpg_6 = np.mean(line_NR_ego_jpg_6)
avg_line_NR_ego_json_6 = np.mean(line_NR_ego_json_6)
avg_occupancy_NR_ego_jpg_6 = np.mean(occupancy_NR_ego_jpg_6)
avg_occupancy_NR_ego_json_6 = np.mean(occupancy_NR_ego_json_6)
avg_line_NR_ego_adj_json_6 = np.mean(line_NR_ego_adj_json_6)
avg_line_NR_ego_adj_txt_6 = np.mean(line_NR_ego_adj_txt_6)
avg_line_NR_ego_tokenized_txt_6 = np.mean(line_NR_ego_tokenized_txt_6)
avg_occupancy_NR_ego_adj_json_6 = np.mean(occupancy_NR_ego_adj_json_6)
avg_occupancy_NR_ego_adj_txt_6 = np.mean(occupancy_NR_ego_adj_txt_6)
avg_occupancy_NR_ego_ascii_txt_6 = np.mean(occupancy_NR_ego_ascii_txt_6)
avg_occupancy_NR_ego_tokenized_txt_6 = np.mean(occupancy_NR_ego_tokenized_txt_6)

avg_line_NR_ego_jpg_output_6 = np.mean(line_NR_ego_jpg_output_tokens_6)
avg_line_NR_ego_json_output_6 = np.mean(line_NR_ego_json_output_tokens_6)
avg_occupancy_NR_ego_jpg_output_6 = np.mean(occupancy_NR_ego_jpg_output_tokens_6)
avg_occupancy_NR_ego_json_output_6 = np.mean(occupancy_NR_ego_json_output_tokens_6)
avg_line_NR_ego_adj_json_output_6 = np.mean(line_NR_ego_adj_json_output_tokens_6)
avg_line_NR_ego_adj_txt_output_6 = np.mean(line_NR_ego_adj_txt_output_tokens_6)
avg_line_NR_ego_tokenized_txt_output_6 = np.mean(line_NR_ego_tokenized_txt_output_tokens_6)
avg_occupancy_NR_ego_adj_json_output_6 = np.mean(occupancy_NR_ego_adj_json_output_tokens_6)
avg_occupancy_NR_ego_adj_txt_output_6 = np.mean(occupancy_NR_ego_adj_txt_output_tokens_6)
avg_occupancy_NR_ego_ascii_txt_output_6 = np.mean(occupancy_NR_ego_ascii_txt_output_tokens_6)
avg_occupancy_NR_ego_tokenized_txt_output_6 = np.mean(occupancy_NR_ego_tokenized_txt_output_tokens_6)

# 6x6 R - COORDS - 1-10 ----------------------------------------------------------------
# Accuracy
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

# Output Tokens
line_R_coords_adj_json_output_tokens_6 = np.array([8118.0, 7536.0, 8051.0, 10359.0, 7050.0, 7165.0, 8363.0, 5188.0, 8328.0, 8680.0])
line_R_coords_adj_txt_output_tokens_6 = np.array([9010.0, 6917.0, 8107.0, 12580.0, 8466.0, 11368.0, 8631.0, 6225.0, 7009.0, 6776.0])
line_R_coords_jpg_output_tokens_6 = np.array([2481.0, 1957.0, 3621.0, 2795.0, 3635.0, 2330.0, 1944.0, 2540.0, 2893.0, 1487.0])
line_R_coords_json_output_tokens_6 = np.array([7887.0, 10892.0, 12599.0, 11490.0, 4499.0, 12090.0, 8009.0, 5811.0, 7880.0, 7781.0])
line_R_coords_tokenized_txt_output_tokens_6 = np.array([7478.0, 5124.0, 7192.0, 6404.0, 7403.0, 5634.0, 6509.0, 4192.0, 5771.0, 8980.0])
occupancy_R_coords_adj_json_output_tokens_6 = np.array([15384.0, 9125.0, 16476.0, 7410.0, 8446.0, 6965.0, 8409.0, 6349.0, 7760.0, 6097.0])
occupancy_R_coords_adj_txt_output_tokens_6 = np.array([13139.0, 9709.0, 8620.0, 19753.0, 9188.0, 5554.0, 10526.0, 9994.0, 7690.0, 10978.0])
occupancy_R_coords_ascii_txt_output_tokens_6 = np.array([9580.0, 13563.0, 18661.0, 6554.0, 5994.0, 18625.0, 11382.0, 2098.0, 16252.0, 3579.0])
occupancy_R_coords_jpg_output_tokens_6 = np.array([3205.0, 12404.0, 4649.0, 23554.0, 2155.0, 5385.0, 10584.0, 9918.0, 3286.0, 2238.0])
occupancy_R_coords_json_output_tokens_6 = np.array([7036.0, 9541.0, 11979.0, 12481.0, 17432.0, 6230.0, 7207.0, 4910.0, 8837.0, 7369.0])
occupancy_R_coords_tokenized_txt_output_tokens_6 = np.array([6473.0, 6508.0, 16281.0, 8357.0, 4132.0, 5736.0, 7801.0, 6271.0, 6880.0, 7046])

avg_line_R_coords_jpg_6 = np.mean(line_R_coords_jpg_6)
avg_line_R_coords_json_6 = np.mean(line_R_coords_json_6)
avg_occupancy_R_coords_jpg_6 = np.mean(occupancy_R_coords_jpg_6)
avg_occupancy_R_coords_json_6 = np.mean(occupancy_R_coords_json_6)
avg_line_R_coords_adj_json_6 = np.mean(line_R_coords_adj_json_6)
avg_line_R_coords_adj_txt_6 = np.mean(line_R_coords_adj_txt_6)
avg_line_R_coords_tokenized_txt_6 = np.mean(line_R_coords_tokenized_txt_6)
avg_occupancy_R_coords_adj_json_6 = np.mean(occupancy_R_coords_adj_json_6)
avg_occupancy_R_coords_adj_txt_6 = np.mean(occupancy_R_coords_adj_txt_6)
avg_occupancy_R_coords_ascii_txt_6 = np.mean(occupancy_R_coords_ascii_txt_6)
avg_occupancy_R_coords_tokenized_txt_6 = np.mean(occupancy_R_coords_tokenized_txt_6)

avg_line_R_coords_jpg_output_6 = np.mean(line_R_coords_jpg_output_tokens_6)
avg_line_R_coords_json_output_6 = np.mean(line_R_coords_json_output_tokens_6)
avg_occupancy_R_coords_jpg_output_6 = np.mean(occupancy_R_coords_jpg_output_tokens_6)
avg_occupancy_R_coords_json_output_6 = np.mean(occupancy_R_coords_json_output_tokens_6)
avg_line_R_coords_adj_json_output_6 = np.mean(line_R_coords_adj_json_output_tokens_6)
avg_line_R_coords_adj_txt_output_6 = np.mean(line_R_coords_adj_txt_output_tokens_6)
avg_line_R_coords_tokenized_txt_output_6 = np.mean(line_R_coords_tokenized_txt_output_tokens_6)
avg_occupancy_R_coords_adj_json_output_6 = np.mean(occupancy_R_coords_adj_json_output_tokens_6)
avg_occupancy_R_coords_adj_txt_output_6 = np.mean(occupancy_R_coords_adj_txt_output_tokens_6)
avg_occupancy_R_coords_ascii_txt_output_6 = np.mean(occupancy_R_coords_ascii_txt_output_tokens_6)
avg_occupancy_R_coords_tokenized_txt_output_6 = np.mean(occupancy_R_coords_tokenized_txt_output_tokens_6)


# 6x6 R - ALLO - 1-10 ----------------------------------------------------------------
# Accuracy
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

# Output Tokens
line_R_allo_adj_json_output_tokens_6 = np.array([10641.0, 14090.0, 10868.0, 8676.0, 9407.0, 8748.0, 9268.0, 6268.0, 7776.0, 10410.0])
line_R_allo_adj_txt_output_tokens_6 = np.array([9343.0, 10961.0, 14119.0, 7126.0, 8186.0, 8730.0, 16201.0, 7605.0, 9852.0, 9724.0])
line_R_allo_jpg_output_tokens_6 = np.array([1839.0, 2913.0, 1991.0, 1423.0, 1177.0, 1452.0, 9757.0, 1935.0, 2147.0, 1590.0])
line_R_allo_json_output_tokens_6 = np.array([5597.0, 11044.0, 9192.0, 9277.0, 3700.0, 9559.0, 7836.0, 7537.0, 7277.0, 6526.0])
line_R_allo_tokenized_txt_output_tokens_6 = np.array([5793.0, 5608.0, 7936.0, 6865.0, 5683.0, 5279.0, 4705.0, 5013.0, 8851.0, 4439.0])
occupancy_R_allo_adj_json_output_tokens_6 = np.array([7474.0, 9524.0, 6529.0, 11801.0, 11052.0, 6205.0, 7602.0, 5525.0, 12079.0, 5873.0])
occupancy_R_allo_adj_txt_output_tokens_6 = np.array([13306.0, 13157.0, 13986.0, 16671.0, 11294.0, 8513.0, 7497.0, 11042.0, 9924.0, 11305.0])
occupancy_R_allo_ascii_txt_output_tokens_6 = np.array([4481.0, 3359.0, 20039.0, 22024.0, 18930.0, 15800.0, 14766.0, 14579.0, 12277.0, 22136.0])
occupancy_R_allo_jpg_output_tokens_6 = np.array([5419.0, 2450.0, 1883.0, 2165.0, 2629.0, 2649.0, 1955.0, 2538.0, 1897.0, 2900.0])
occupancy_R_allo_json_output_tokens_6 = np.array([12925.0, 8580.0, 17443.0, 27933.0, 8077.0, 14011.0, 12393.0, 4414.0, 10960.0, 15358.0])
occupancy_R_allo_tokenized_txt_output_tokens_6 = np.array([6708.0, 6990.0, 7499.0, 11540.0, 3074.0, 4217.0, 14502.0, 6598.0, 6265.0, 8402])

avg_line_R_allo_jpg_6 = np.mean(line_R_allo_jpg_6)
avg_line_R_allo_json_6 = np.mean(line_R_allo_json_6)
avg_occupancy_R_allo_jpg_6 = np.mean(occupancy_R_allo_jpg_6)
avg_occupancy_R_allo_json_6 = np.mean(occupancy_R_allo_json_6)
avg_line_R_allo_adj_json_6 = np.mean(line_R_allo_adj_json_6)
avg_line_R_allo_adj_txt_6 = np.mean(line_R_allo_adj_txt_6)
avg_line_R_allo_tokenized_txt_6 = np.mean(line_R_allo_tokenized_txt_6)
avg_occupancy_R_allo_adj_json_6 = np.mean(occupancy_R_allo_adj_json_6)
avg_occupancy_R_allo_adj_txt_6 = np.mean(occupancy_R_allo_adj_txt_6)
avg_occupancy_R_allo_ascii_txt_6 = np.mean(occupancy_R_allo_ascii_txt_6)
avg_occupancy_R_allo_tokenized_txt_6 = np.mean(occupancy_R_allo_tokenized_txt_6)


avg_line_R_allo_jpg_output_6 = np.mean(line_R_allo_jpg_output_tokens_6)
avg_line_R_allo_json_output_6 = np.mean(line_R_allo_json_output_tokens_6)
avg_occupancy_R_allo_jpg_output_6 = np.mean(occupancy_R_allo_jpg_output_tokens_6)
avg_occupancy_R_allo_json_output_6 = np.mean(occupancy_R_allo_json_output_tokens_6)
avg_line_R_allo_adj_json_output_6 = np.mean(line_R_allo_adj_json_output_tokens_6)
avg_line_R_allo_adj_txt_output_6 = np.mean(line_R_allo_adj_txt_output_tokens_6)
avg_line_R_allo_tokenized_txt_output_6 = np.mean(line_R_allo_tokenized_txt_output_tokens_6)
avg_occupancy_R_allo_adj_json_output_6 = np.mean(occupancy_R_allo_adj_json_output_tokens_6)
avg_occupancy_R_allo_adj_txt_output_6 = np.mean(occupancy_R_allo_adj_txt_output_tokens_6)
avg_occupancy_R_allo_ascii_txt_output_6 = np.mean(occupancy_R_allo_ascii_txt_output_tokens_6)
avg_occupancy_R_allo_tokenized_txt_output_6 = np.mean(occupancy_R_allo_tokenized_txt_output_tokens_6)


# 6x6 - EGO - 1-10 ----------------------------------------------------------------
# # Accuracy
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

# Output Tokens
line_R_ego_adj_json_output_tokens_6 = np.array([6390.0, 10668.0, 12437.0, 12920.0, 6567.0, 8281.0, 10218.0, 5101.0, 10020.0, 7362.0])
line_R_ego_adj_txt_output_tokens_6 = np.array([6467.0, 6319.0, 6035.0, 9648.0, 7523.0, 10133.0, 12011.0, 5569.0, 8592.0, 7937.0])
line_R_ego_jpg_output_tokens_6 = np.array([2398.0, 3132.0, 3318.0, 3813.0, 2187.0, 1674.0, 2857.0, 1577.0, 2172.0, 2070.0])
line_R_ego_json_output_tokens_6 = np.array([3994.0, 5758.0, 13995.0, 9986.0, 8931.0, 12105.0, 8791.0, 3930.0, 15025.0, 15241.0])
line_R_ego_tokenized_txt_output_tokens_6 = np.array([8429.0, 6664.0, 10667.0, 9767.0, 5029.0, 10211.0, 13849.0, 5052.0, 6737.0, 12532.0])
occupancy_R_ego_adj_json_output_tokens_6 = np.array([11970.0, 13702.0, 17330.0, 19841.0, 12415.0, 8618.0, 10500.0, 9725.0, 10587.0, 8333.0])
occupancy_R_ego_adj_txt_output_tokens_6 = np.array([9861.0, 19222.0, 14460.0, 23064.0, 15292.0, 17620.0, 9997.0, 6948.0, 17158.0, 11736.0])
occupancy_R_ego_ascii_txt_output_tokens_6 = np.array([22762.0, 9003.0, 2806.0, 16200.0, 17916.0, 7652.0, 16613.0, 8111.0, 6627.0, 7386.0])
occupancy_R_ego_jpg_output_tokens_6 = np.array([5468.0, 3335.0, 6321.0, 7905.0, 8185.0, 7207.0, 5149.0, 5087.0, 10110.0, 5163.0])
occupancy_R_ego_json_output_tokens_6 = np.array([12945.0, 10590.0, 14452.0, 26708.0, 10656.0, 7456.0, 8722.0, 8159.0, 22047.0, 12086.0])
occupancy_R_ego_tokenized_txt_output_tokens_6 = np.array([8801.0, 9813.0, 12147.0, 7806.0, 8871.0, 14289.0, 4835.0, 4969.0, 8420.0, 7251])

avg_line_R_ego_jpg_6 = np.mean(line_R_ego_jpg_6)
avg_line_R_ego_json_6 = np.mean(line_R_ego_json_6)
avg_occupancy_R_ego_jpg_6 = np.mean(occupancy_R_ego_jpg_6)
avg_occupancy_R_ego_json_6 = np.mean(occupancy_R_ego_json_6)
avg_line_R_ego_adj_json_6 = np.mean(line_R_ego_adj_json_6)
avg_line_R_ego_adj_txt_6 = np.mean(line_R_ego_adj_txt_6)
avg_line_R_ego_tokenized_txt_6 = np.mean(line_R_ego_tokenized_txt_6)
avg_occupancy_R_ego_adj_json_6 = np.mean(occupancy_R_ego_adj_json_6)
avg_occupancy_R_ego_adj_txt_6 = np.mean(occupancy_R_ego_adj_txt_6)
avg_occupancy_R_ego_ascii_txt_6 = np.mean(occupancy_R_ego_ascii_txt_6)
avg_occupancy_R_ego_tokenized_txt_6 = np.mean(occupancy_R_ego_tokenized_txt_6)

avg_line_R_ego_jpg_output_6 = np.mean(line_R_ego_jpg_output_tokens_6)
avg_line_R_ego_json_output_6 = np.mean(line_R_ego_json_output_tokens_6)
avg_occupancy_R_ego_jpg_output_6 = np.mean(occupancy_R_ego_jpg_output_tokens_6)
avg_occupancy_R_ego_json_output_6 = np.mean(occupancy_R_ego_json_output_tokens_6)
avg_line_R_ego_adj_json_output_6 = np.mean(line_R_ego_adj_json_output_tokens_6)
avg_line_R_ego_adj_txt_output_6 = np.mean(line_R_ego_adj_txt_output_tokens_6)
avg_line_R_ego_tokenized_txt_output_6 = np.mean(line_R_ego_tokenized_txt_output_tokens_6)
avg_occupancy_R_ego_adj_json_output_6 = np.mean(occupancy_R_ego_adj_json_output_tokens_6)
avg_occupancy_R_ego_adj_txt_output_6 = np.mean(occupancy_R_ego_adj_txt_output_tokens_6)
avg_occupancy_R_ego_ascii_txt_output_6 = np.mean(occupancy_R_ego_ascii_txt_output_tokens_6)
avg_occupancy_R_ego_tokenized_txt_output_6 = np.mean(occupancy_R_ego_tokenized_txt_output_tokens_6)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 15x15 NR - COORDS - 1-10 ----------------------------------------------------------------

# Accuracy
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



# Output tokens
line_NR_coords_adj_json_output_tokens_15 = np.array([256.0, 606.0, 648.0, 202.0, 637.0, 204.0, 650.0, 650.0, 650.0, 165.0])
line_NR_coords_adj_txt_output_tokens_15 = np.array([557.0, 418.0, 650.0, 387.0, 188.0, 310.0, 568.0, 603.0, 650.0, 254.0])
line_NR_coords_jpg_output_tokens_15 = np.array([147.0, 182.0, 153.0, 164.0, 219.0, 335.0, 174.0, 257.0, 174.0, 132.0])
line_NR_coords_json_output_tokens_15 = np.array([152.0, 141.0, 650.0, 213.0, 211.0, 300.0, 136.0, 260.0, 444.0, 220.0])
line_NR_coords_tokenized_txt_output_tokens_15 = np.array([172.0, 146.0, 350.0, 237.0, 149.0, 141.0, 230.0, 208.0, 130.0, 141.0])
occupancy_NR_coords_adj_json_output_tokens_15 = np.array([650.0, 515.0, 92.0, 615.0, 650.0, 650.0, 650.0, 650.0, 650.0, 429.0])
occupancy_NR_coords_adj_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 621.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_coords_ascii_txt_output_tokens_15 = np.array([329.0, 650.0, 649.0, 592.0, 339.0, 650.0, 582.0, 416.0, 321.0, 650.0])
occupancy_NR_coords_jpg_output_tokens_15 = np.array([583.0, 469.0, 472.0, 409.0, 457.0, 495.0, 419.0, 465.0, 310.0, 335.0])
occupancy_NR_coords_json_output_tokens_15 = np.array([297.0, 298.0, 302.0, 587.0, 339.0, 650.0, 410.0, 295.0, 313.0, 650.0])
occupancy_NR_coords_tokenized_txt_output_tokens_15 = np.array([302.0, 297.0, 650.0, 650, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])

avg_line_NR_coords_jpg_15 = np.mean(line_NR_coords_jpg_15)
avg_line_NR_coords_json_15 = np.mean(line_NR_coords_json_15)
avg_occupancy_NR_coords_jpg_15 = np.mean(occupancy_NR_coords_jpg_15)
avg_occupancy_NR_coords_json_15 = np.mean(occupancy_NR_coords_json_15)
avg_line_NR_coords_adj_json_15 = np.mean(line_NR_coords_adj_json_15)
avg_line_NR_coords_adj_txt_15 = np.mean(line_NR_coords_adj_txt_15)
avg_line_NR_coords_tokenized_txt_15 = np.mean(line_NR_coords_tokenized_txt_15)
avg_occupancy_NR_coords_adj_json_15 = np.mean(occupancy_NR_coords_adj_json_15)
avg_occupancy_NR_coords_adj_txt_15 = np.mean(occupancy_NR_coords_adj_txt_15)
avg_occupancy_NR_coords_ascii_txt_15 = np.mean(occupancy_NR_coords_ascii_txt_15)
avg_occupancy_NR_coords_tokenized_txt_15 = np.mean(occupancy_NR_coords_tokenized_txt_15)

avg_line_NR_coords_jpg_output_15 = np.mean(line_NR_coords_jpg_output_tokens_15)
avg_line_NR_coords_json_output_15 = np.mean(line_NR_coords_json_output_tokens_15)
avg_occupancy_NR_coords_jpg_output_15 = np.mean(occupancy_NR_coords_jpg_output_tokens_15)
avg_occupancy_NR_coords_json_output_15 = np.mean(occupancy_NR_coords_json_output_tokens_15)
avg_line_NR_coords_adj_json_output_15 = np.mean(line_NR_coords_adj_json_output_tokens_15)
avg_line_NR_coords_adj_txt_output_15 = np.mean(line_NR_coords_adj_txt_output_tokens_15)
avg_line_NR_coords_tokenized_txt_output_15 = np.mean(line_NR_coords_tokenized_txt_output_tokens_15)
avg_occupancy_NR_coords_adj_json_output_15 = np.mean(occupancy_NR_coords_adj_json_output_tokens_15)
avg_occupancy_NR_coords_adj_txt_output_15 = np.mean(occupancy_NR_coords_adj_txt_output_tokens_15)
avg_occupancy_NR_coords_ascii_txt_output_15 = np.mean(occupancy_NR_coords_ascii_txt_output_tokens_15)
avg_occupancy_NR_coords_tokenized_txt_output_15 = np.mean(occupancy_NR_coords_tokenized_txt_output_tokens_15)




# 15x15 NR - ALLO - 1-10 ----------------------------------------------------------------

# Accuracy
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


# output tokens
line_NR_allo_adj_json_output_tokens_15 = np.array([650.0, 99.0, 57.0, 55.0, 57.0, 650.0, 57.0, 57.0, 57.0, 85.0])
line_NR_allo_adj_txt_output_tokens_15 = np.array([57.0, 650.0, 650.0, 533.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_allo_jpg_output_tokens_15 = np.array([0.0, 113.0, 650.0, 81.0, 650.0, 0.0, 0.0, 0.0, 103.0, 650.0])
line_NR_allo_json_output_tokens_15 = np.array([55.0, 53.0, 55.0, 650.0, 650.0, 650.0, 650.0, 0.0, 55.0, 0.0])
line_NR_allo_tokenized_txt_output_tokens_15 = np.array([650.0, 0.0, 650.0, 650.0, 650.0, 0.0, 650.0, 650.0, 650.0, 0.0])
occupancy_NR_allo_adj_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 0.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_adj_txt_output_tokens_15 = np.array([650.0, 0.0, 115.0, 117.0, 650.0, 650.0, 59.0, 0.0, 113.0, 650.0])
occupancy_NR_allo_ascii_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 0.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_jpg_output_tokens_15 = np.array([650, 650.0, 650.0, 650.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_allo_json_output_tokens_15 = np.array([650.0, 57.0, 650.0, 650.0, 650.0, 119.0, 650.0, 650.0, 57.0, 650.0])
occupancy_NR_allo_tokenized_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])

avg_line_NR_allo_jpg_15 = np.mean(line_NR_allo_jpg_15)
avg_line_NR_allo_json_15 = np.mean(line_NR_allo_json_15)
avg_occupancy_NR_allo_jpg_15 = np.mean(occupancy_NR_allo_jpg_15)
avg_occupancy_NR_allo_json_15 = np.mean(occupancy_NR_allo_json_15)
avg_line_NR_allo_adj_json_15 = np.mean(line_NR_allo_adj_json_15)
avg_line_NR_allo_adj_txt_15 = np.mean(line_NR_allo_adj_txt_15)
avg_line_NR_allo_tokenized_txt_15 = np.mean(line_NR_allo_tokenized_txt_15)
avg_occupancy_NR_allo_adj_json_15 = np.mean(occupancy_NR_allo_adj_json_15)
avg_occupancy_NR_allo_adj_txt_15 = np.mean(occupancy_NR_allo_adj_txt_15)
avg_occupancy_NR_allo_ascii_txt_15 = np.mean(occupancy_NR_allo_ascii_txt_15)
avg_occupancy_NR_allo_tokenized_txt_15 = np.mean(occupancy_NR_allo_tokenized_txt_15)

avg_line_NR_allo_jpg_output_15 = np.mean(line_NR_allo_jpg_output_tokens_15)
avg_line_NR_allo_json_output_15 = np.mean(line_NR_allo_json_output_tokens_15)
avg_occupancy_NR_allo_jpg_output_15 = np.mean(occupancy_NR_allo_jpg_output_tokens_15)
avg_occupancy_NR_allo_json_output_15 = np.mean(occupancy_NR_allo_json_output_tokens_15)
avg_line_NR_allo_adj_json_output_15 = np.mean(line_NR_allo_adj_json_output_tokens_15)
avg_line_NR_allo_adj_txt_output_15 = np.mean(line_NR_allo_adj_txt_output_tokens_15)
avg_line_NR_allo_tokenized_txt_output_15 = np.mean(line_NR_allo_tokenized_txt_output_tokens_15)
avg_occupancy_NR_allo_adj_json_output_15 = np.mean(occupancy_NR_allo_adj_json_output_tokens_15)
avg_occupancy_NR_allo_adj_txt_output_15 = np.mean(occupancy_NR_allo_adj_txt_output_tokens_15)
avg_occupancy_NR_allo_ascii_txt_output_15 = np.mean(occupancy_NR_allo_ascii_txt_output_tokens_15)
avg_occupancy_NR_allo_tokenized_txt_output_15 = np.mean(occupancy_NR_allo_tokenized_txt_output_tokens_15)



# 15x15 NR - EGO - 1-10 ----------------------------------------------------------------

# Accuracy

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


# output tokens
line_NR_ego_adj_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_adj_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_jpg_output_tokens_15 = np.array([133.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_tokenized_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_ascii_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_jpg_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_tokenized_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650, 650.0, 650.0, 650.0, 650.0])

avg_line_NR_ego_jpg_15 = np.mean(line_NR_ego_jpg_15)
avg_line_NR_ego_json_15 = np.mean(line_NR_ego_json_15)
avg_occupancy_NR_ego_jpg_15 = np.mean(occupancy_NR_ego_jpg_15)
avg_occupancy_NR_ego_json_15 = np.mean(occupancy_NR_ego_json_15)
avg_line_NR_ego_adj_json_15 = np.mean(line_NR_ego_adj_json_15)
avg_line_NR_ego_adj_txt_15 = np.mean(line_NR_ego_adj_txt_15)
avg_line_NR_ego_tokenized_txt_15 = np.mean(line_NR_ego_tokenized_txt_15)
avg_occupancy_NR_ego_adj_json_15 = np.mean(occupancy_NR_ego_adj_json_15)
avg_occupancy_NR_ego_adj_txt_15 = np.mean(occupancy_NR_ego_adj_txt_15)
avg_occupancy_NR_ego_ascii_txt_15 = np.mean(occupancy_NR_ego_ascii_txt_15)
avg_occupancy_NR_ego_tokenized_txt_15 = np.mean(occupancy_NR_ego_tokenized_txt_15)

avg_line_NR_ego_jpg_output_15 = np.mean(line_NR_ego_jpg_output_tokens_15)
avg_line_NR_ego_json_output_15 = np.mean(line_NR_ego_json_output_tokens_15)
avg_occupancy_NR_ego_jpg_output_15 = np.mean(occupancy_NR_ego_jpg_output_tokens_15)
avg_occupancy_NR_ego_json_output_15 = np.mean(occupancy_NR_ego_json_output_tokens_15)
avg_line_NR_ego_adj_json_output_15 = np.mean(line_NR_ego_adj_json_output_tokens_15)
avg_line_NR_ego_adj_txt_output_15 = np.mean(line_NR_ego_adj_txt_output_tokens_15)
avg_line_NR_ego_tokenized_txt_output_15 = np.mean(line_NR_ego_tokenized_txt_output_tokens_15)
avg_occupancy_NR_ego_adj_json_output_15 = np.mean(occupancy_NR_ego_adj_json_output_tokens_15)
avg_occupancy_NR_ego_adj_txt_output_15 = np.mean(occupancy_NR_ego_adj_txt_output_tokens_15)
avg_occupancy_NR_ego_ascii_txt_output_15 = np.mean(occupancy_NR_ego_ascii_txt_output_tokens_15)
avg_occupancy_NR_ego_tokenized_txt_output_15 = np.mean(occupancy_NR_ego_tokenized_txt_output_tokens_15)


# 15x15 R - COORDS - 1-10  ----------------------------------------------------------------

# Accuracy
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

# Output tokens
line_R_coords_adj_json_output_tokens_15 = np.array([24319.0, 16225.0, 24616.0, 8139.0, 19260.0, 12408.0, 7826.0, 15115.0, 20876.0, 5314.0])
line_R_coords_adj_txt_output_tokens_15 = np.array([33577.0, 24330.0, 25615.0, 20071.0, 19655.0, 28924.0, 10897.0, 23268.0, 7706.0, 14201.0])
line_R_coords_jpg_output_tokens_15 = np.array([4504.0, 3944.0, 10750.0, 16490.0, 5091.0, 4180.0, 6718.0, 7549.0, 14674.0, 6569.0])
line_R_coords_json_output_tokens_15 = np.array([14877.0, 21134.0, 24389.0, 22863.0, 26197.0, 20740.0, 29735.0, 15855.0, 23004.0, 19638.0])
line_R_coords_tokenized_txt_output_tokens_15 = np.array([27012.0, 8104.0, 16779.0, 5941.0, 17585.0, 22661.0, 10570.0, 24814.0, 14842.0, 7821.0])
occupancy_R_coords_adj_json_output_tokens_15 = np.array([38108.0, 12526.0, 44759.0, 8955.0, 18015.0, 11288.0, 13758.0, 17437.0, 30188.0, 9741.0])
occupancy_R_coords_adj_txt_output_tokens_15 = np.array([35979.0, 29317.0, 27858.0, 29722.0, 32951.0, 27173.0, 32997.0, 27944.0, 33251.0, 22642.0])
occupancy_R_coords_ascii_txt_output_tokens_15 = np.array([10674.0, 7006.0, 14414.0, 10515.0, 9263.0, 11732.0, 19721.0, 10736.0, 16575.0, 19719.0])
occupancy_R_coords_jpg_output_tokens_15 = np.array([10193.0, 12494.0, 13728.0, 8963.0, 9955.0, 5758.0, 8949.0, 16009.0, 6946.0, 17182.0])
occupancy_R_coords_json_output_tokens_15 = np.array([17287.0, 13432.0, 24426.0, 19069.0, 20997.0, 19289.0, 25754.0, 15716.0, 18421.0, 19336.0])
occupancy_R_coords_tokenized_txt_output_tokens_15 = np.array([27461.0, 12623.0, 26548.0, 17015.0, 24129, 26580.0, 19448.0, 25165.0, 27684.0, 22137.0])

avg_line_R_coords_jpg_15 = np.mean(line_R_coords_jpg_15)
avg_line_R_coords_json_15 = np.mean(line_R_coords_json_15)
avg_occupancy_R_coords_jpg_15 = np.mean(occupancy_R_coords_jpg_15)
avg_occupancy_R_coords_json_15 = np.mean(occupancy_R_coords_json_15)
avg_line_R_coords_adj_json_15 = np.mean(line_R_coords_adj_json_15)
avg_line_R_coords_adj_txt_15 = np.mean(line_R_coords_adj_txt_15)
avg_line_R_coords_tokenized_txt_15 = np.mean(line_R_coords_tokenized_txt_15)
avg_occupancy_R_coords_adj_json_15 = np.mean(occupancy_R_coords_adj_json_15)
avg_occupancy_R_coords_adj_txt_15 = np.mean(occupancy_R_coords_adj_txt_15)
avg_occupancy_R_coords_ascii_txt_15 = np.mean(occupancy_R_coords_ascii_txt_15)
avg_occupancy_R_coords_tokenized_txt_15 = np.mean(occupancy_R_coords_tokenized_txt_15)

avg_line_R_coords_jpg_output_15 = np.mean(line_R_coords_jpg_output_tokens_15)
avg_line_R_coords_json_output_15 = np.mean(line_R_coords_json_output_tokens_15)
avg_occupancy_R_coords_jpg_output_15 = np.mean(occupancy_R_coords_jpg_output_tokens_15)
avg_occupancy_R_coords_json_output_15 = np.mean(occupancy_R_coords_json_output_tokens_15)
avg_line_R_coords_adj_json_output_15 = np.mean(line_R_coords_adj_json_output_tokens_15)
avg_line_R_coords_adj_txt_output_15 = np.mean(line_R_coords_adj_txt_output_tokens_15)
avg_line_R_coords_tokenized_txt_output_15 = np.mean(line_R_coords_tokenized_txt_output_tokens_15)
avg_occupancy_R_coords_adj_json_output_15 = np.mean(occupancy_R_coords_adj_json_output_tokens_15)
avg_occupancy_R_coords_adj_txt_output_15 = np.mean(occupancy_R_coords_adj_txt_output_tokens_15)
avg_occupancy_R_coords_ascii_txt_output_15 = np.mean(occupancy_R_coords_ascii_txt_output_tokens_15)
avg_occupancy_R_coords_tokenized_txt_output_15 = np.mean(occupancy_R_coords_tokenized_txt_output_tokens_15)

# 15x15 R - ALLO - 1-10 ----------------------------------------------------------------

# Accuracy
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


# Output tokens
line_R_allo_adj_json_output_tokens_15 = np.array([22587.0, 10727.0, 22842.0, 9131.0, 11767.0, 19558.0, 9256.0, 16737.0, 20988.0, 11533.0])
line_R_allo_adj_txt_output_tokens_15 = np.array([31007.0, 23644.0, 9234.0, 11180.0, 22655.0, 17180.0, 10782.0, 21815.0, 19407.0, 19985.0])
line_R_allo_jpg_output_tokens_15 = np.array([6803.0, 4423.0, 6075.0, 2966.0, 4505.0, 8598.0, 8694.0, 4345.0, 9458.0, 4858.0])
line_R_allo_json_output_tokens_15 = np.array([23638.0, 6698.0, 18380.0, 4923.0, 20808.0, 20562.0, 21221.0, 12816.0, 22590.0, 13677.0])
line_R_allo_tokenized_txt_output_tokens_15 = np.array([24874.0, 5662.0, 29110.0, 19105.0, 16818.0, 14950.0, 6263.0, 20016.0, 21413.0, 7500.0])
occupancy_R_allo_adj_json_output_tokens_15 = np.array([21385.0, 13601.0, 25273.0, 12155.0, 24470.0, 15482.0, 18116.0, 26090.0, 29201.0, 11509.0])
occupancy_R_allo_adj_txt_output_tokens_15 = np.array([26432.0, 17327.0, 27365.0, 33199.0, 27635.0, 34064.0, 27374.0, 28281.0, 26462.0, 10218.0])
occupancy_R_allo_ascii_txt_output_tokens_15 = np.array([6953.0, 5720.0, 3744.0, 11475.0, 7697.0, 4759.0, 9551.0, 18615.0, 11527.0, 4246.0])
occupancy_R_allo_jpg_output_tokens_15 = np.array([14420.0, 16069.0, 7911.0, 10028.0, 9050.0, 6771.0, 8747.0, 11031.0, 17497.0, 14351.0])
occupancy_R_allo_json_output_tokens_15 = np.array([18136.0, 20884.0, 15988.0, 24608.0, 18119.0, 7607.0, 12994.0, 18491.0, 22347.0, 20437.0])
occupancy_R_allo_tokenized_txt_output_tokens_15 = np.array([25641.0, 12698.0, 22502.0, 19036.0, 24018.0, 23182.0, 25434.0, 23742.0, 20451.0, 10015])

avg_line_R_allo_jpg_15 = np.mean(line_R_allo_jpg_15)
avg_line_R_allo_json_15 = np.mean(line_R_allo_json_15)
avg_occupancy_R_allo_jpg_15 = np.mean(occupancy_R_allo_jpg_15)
avg_occupancy_R_allo_json_15 = np.mean(occupancy_R_allo_json_15)
avg_line_R_allo_adj_json_15 = np.mean(line_R_allo_adj_json_15)
avg_line_R_allo_adj_txt_15 = np.mean(line_R_allo_adj_txt_15)
avg_line_R_allo_tokenized_txt_15 = np.mean(line_R_allo_tokenized_txt_15)
avg_occupancy_R_allo_adj_json_15 = np.mean(occupancy_R_allo_adj_json_15)
avg_occupancy_R_allo_adj_txt_15 = np.mean(occupancy_R_allo_adj_txt_15)
avg_occupancy_R_allo_ascii_txt_15 = np.mean(occupancy_R_allo_ascii_txt_15)
avg_occupancy_R_allo_tokenized_txt_15 = np.mean(occupancy_R_allo_tokenized_txt_15)


avg_line_R_allo_jpg_output_15 = np.mean(line_R_allo_jpg_output_tokens_15)
avg_line_R_allo_json_output_15 = np.mean(line_R_allo_json_output_tokens_15)
avg_occupancy_R_allo_jpg_output_15 = np.mean(occupancy_R_allo_jpg_output_tokens_15)
avg_occupancy_R_allo_json_output_15 = np.mean(occupancy_R_allo_json_output_tokens_15)
avg_line_R_allo_adj_json_output_15 = np.mean(line_R_allo_adj_json_output_tokens_15)
avg_line_R_allo_adj_txt_output_15 = np.mean(line_R_allo_adj_txt_output_tokens_15)
avg_line_R_allo_tokenized_txt_output_15 = np.mean(line_R_allo_tokenized_txt_output_tokens_15)
avg_occupancy_R_allo_adj_json_output_15 = np.mean(occupancy_R_allo_adj_json_output_tokens_15)
avg_occupancy_R_allo_adj_txt_output_15 = np.mean(occupancy_R_allo_adj_txt_output_tokens_15)
avg_occupancy_R_allo_ascii_txt_output_15 = np.mean(occupancy_R_allo_ascii_txt_output_tokens_15)
avg_occupancy_R_allo_tokenized_txt_output_15 = np.mean(occupancy_R_allo_tokenized_txt_output_tokens_15)

# 15x15 R - EGO - 1-10 ----------------------------------------------------------------

# Accuracy
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

# Output tokens
line_R_ego_adj_json_output_tokens_15 = np.array([23590.0, 12603.0, 22603.0, 10547.0, 23935.0, 17924.0, 18562.0, 17955.0, 29135.0, 7887.0])
line_R_ego_adj_txt_output_tokens_15 = np.array([31340.0, 13936.0, 22702.0, 10531.0, 21926.0, 27592.0, 10754.0, 21051.0, 13892.0, 13337.0])
line_R_ego_jpg_output_tokens_15 = np.array([5694.0, 10838.0, 8056.0, 7726.0, 8044.0, 4165.0, 6490.0, 7053.0, 6032.0, 5382.0])
line_R_ego_json_output_tokens_15 = np.array([22185.0, 22400.0, 10695.0, 12779.0, 26711.0, 22117.0, 22326.0, 18744.0, 19329.0, 26979.0])
line_R_ego_tokenized_txt_output_tokens_15 = np.array([26034.0, 23176.0, 30332.0, 14776.0, 26266.0, 19001.0, 9542.0, 12020.0, 17727.0, 6311.0])
occupancy_R_ego_adj_json_output_tokens_15 = np.array([18870.0, 19262.0, 33481.0, 14313.0, 37418.0, 22595.0, 25233.0, 23782.0, 35780.0, 17694.0])
occupancy_R_ego_adj_txt_output_tokens_15 = np.array([38830.0, 24530.0, 29628.0, 30868.0, 24143.0, 25473.0, 24312.0, 24105.0, 31731.0, 23472.0])
occupancy_R_ego_ascii_txt_output_tokens_15 = np.array([18233.0, 21823.0, 12927.0, 20916.0, 9998.0, 12138.0, 12549.0, 13949.0, 17702.0, 17755.0])
occupancy_R_ego_jpg_output_tokens_15 = np.array([18405.0, 15913.0, 23382.0, 8448.0, 12519.0, 12638.0, 12785.0, 10682.0, 10414.0, 12349.0])
occupancy_R_ego_json_output_tokens_15 = np.array([10282.0, 17161.0, 29684.0, 21330.0, 13550.0, 26301.0, 15134.0, 8967.0, 18473.0, 8937.0])
occupancy_R_ego_tokenized_txt_output_tokens_15 = np.array([31644.0, 23772.0, 23668.0, 29242.0, 27743.0, 21539.0, 9479.0, 29551.0, 26594.0, 18002])

avg_line_R_ego_jpg_15 = np.mean(line_R_ego_jpg_15)
avg_line_R_ego_json_15 = np.mean(line_R_ego_json_15)
avg_occupancy_R_ego_jpg_15 = np.mean(occupancy_R_ego_jpg_15)
avg_occupancy_R_ego_json_15 = np.mean(occupancy_R_ego_json_15)
avg_line_R_ego_adj_json_15 = np.mean(line_R_ego_adj_json_15)
avg_line_R_ego_adj_txt_15 = np.mean(line_R_ego_adj_txt_15)
avg_line_R_ego_tokenized_txt_15 = np.mean(line_R_ego_tokenized_txt_15)
avg_occupancy_R_ego_adj_json_15 = np.mean(occupancy_R_ego_adj_json_15)
avg_occupancy_R_ego_adj_txt_15 = np.mean(occupancy_R_ego_adj_txt_15)
avg_occupancy_R_ego_ascii_txt_15 = np.mean(occupancy_R_ego_ascii_txt_15)
avg_occupancy_R_ego_tokenized_txt_15 = np.mean(occupancy_R_ego_tokenized_txt_15)

avg_line_R_ego_jpg_output_15 = np.mean(line_R_ego_jpg_output_tokens_15)
avg_line_R_ego_json_output_15 = np.mean(line_R_ego_json_output_tokens_15)
avg_occupancy_R_ego_jpg_output_15 = np.mean(occupancy_R_ego_jpg_output_tokens_15)
avg_occupancy_R_ego_json_output_15 = np.mean(occupancy_R_ego_json_output_tokens_15)
avg_line_R_ego_adj_json_output_15 = np.mean(line_R_ego_adj_json_output_tokens_15)
avg_line_R_ego_adj_txt_output_15 = np.mean(line_R_ego_adj_txt_output_tokens_15)
avg_line_R_ego_tokenized_txt_output_15 = np.mean(line_R_ego_tokenized_txt_output_tokens_15)
avg_occupancy_R_ego_adj_json_output_15 = np.mean(occupancy_R_ego_adj_json_output_tokens_15)
avg_occupancy_R_ego_adj_txt_output_15 = np.mean(occupancy_R_ego_adj_txt_output_tokens_15)
avg_occupancy_R_ego_ascii_txt_output_15 = np.mean(occupancy_R_ego_ascii_txt_output_tokens_15)
avg_occupancy_R_ego_tokenized_txt_output_15 = np.mean(occupancy_R_ego_tokenized_txt_output_tokens_15)



# Creating an acc vs token output plot ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Creating data for plotting
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




# Labels for legend
labels_base = ["Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"]
markers = ['o', 'v', 's', '*', 'D', 'P']
red = ['lightcoral', 'red'] #light, dark
blue = ['cornflowerblue', 'blue'] #light, dark
green = ['limegreen', 'green'] #light, dark
marker_edge = ['none', 'black'] #line, occupancy
marker_size = [10,10,10]

# Create multiple plots in the same figure
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(9, 8), sharex=True)

# # Create figure
# fig, ax = plt.subplots(figsize=(8, 6))

# Plot 3x3 data with corresponding labels
for i, point in enumerate(line_NR_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Flash Lite")

for i, point in enumerate(line_NR_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i],  color = green[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(line_NR_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(line_R_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(line_R_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i],  color = green[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(line_R_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[0], linestyle='None', label=label+", 3x3, Egocentric, Gemini 2.5 Pro")


# Plot 7x7 data with corresponding labels
for i, point in enumerate(occupancy_NR_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = red[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_NR_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_NR_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_R_coords_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_allo_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_ego_3):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax1.plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[0], linestyle='None', label=label+", 7x7, Egocentric, Gemini 2.5 Pro")

# Plot 6x6 data with corresponding labels
for i, point in enumerate(line_NR_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Coordinates, Gemini 2.5 Flash Lite")
for i, point in enumerate(line_NR_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Allocentric, Gemini 2.5 Flash Lite")
for i, point in enumerate(line_NR_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Egocentric, Gemini 2.5 Flash Lite")
for i, point in enumerate(line_R_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Coordinates, Gemini 2.5 Pro")
for i, point in enumerate(line_R_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Allocentric, Gemini 2.5 Pro")
for i, point in enumerate(line_R_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[1], linestyle='None', label=label+", 6x6, Egocentric, Gemini 2.5 Pro")

# Plot 13x13 data with corresponding labels
for i, point in enumerate(occupancy_NR_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Coordinates, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_NR_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Allocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_NR_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Egocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_R_coords_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_allo_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_ego_6):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax2.plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[1], linestyle='None', label=label+", 13x13, Egocentric, Gemini 2.5 Pro")


    # Plot 15x15 data with corresponding labels
for i, point in enumerate(line_NR_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Coordinates, Gemini 2.5 Flash Lite")

for i, point in enumerate(line_NR_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Allocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(line_NR_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Egocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(line_R_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(line_R_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(line_R_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[0], ms = marker_size[2], linestyle='None', label=label+", 15x15, Egocentric, Gemini 2.5 Pro")


# Plot 31x31 data with corresponding labels
for i, point in enumerate(occupancy_NR_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i],  color = red[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Coordinates, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_NR_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = green[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Allocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_NR_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = blue[0], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Egocentric, Gemini 2.5 Flash Lite")

for i, point in enumerate(occupancy_R_coords_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i],  color = red[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Coordinates, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_allo_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = green[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Allocentric, Gemini 2.5 Pro")

for i, point in enumerate(occupancy_R_ego_15):
    x, y = point
    label = labels_base[i]  # get label corresponding to the row
    ax3.plot(x, y, marker=markers[i], color = blue[1], mec=marker_edge[1], ms = marker_size[2], linestyle='None', label=label+", 31x31, Egocentric, Gemini 2.5 Pro")


# Axis labels
ax3.set_xlabel("Average Cost Per Task (Tokens)")
ax1.set_ylabel("Accuracy (%)")
ax2.set_ylabel("Accuracy (%)")
ax3.set_ylabel("Accuracy (%)")

ax1.set_xscale('log')  # Set x-axis to logarithmic scale
ax2.set_xscale('log')  # Set x-axis to logarithmic scale
ax3.set_xscale('log')  # Set x-axis to logarithmic scale
# Grid for readability
ax1.grid(True, linestyle='--', alpha=0.6)
ax2.grid(True, linestyle='--', alpha=0.6)
ax3.grid(True, linestyle='--', alpha=0.6)


# Custom combined legend handles:
coord_handle = [
    Line2D([], [], marker='o',  markerfacecolor='lightcoral', markersize=10),
    Line2D([], [], marker='o',  markerfacecolor='firebrick', markersize=10)
]
allo_handle = [
    Line2D([], [], marker='o', color='none', markerfacecolor='lightgreen', markersize=10),
    Line2D([], [], marker='o', color='none', markerfacecolor='green', markersize=10)
]
ego_handle = [
    Line2D([], [], marker='o', color='none', markerfacecolor='cyan', markersize=10),
    Line2D([], [], marker='o', color='none', markerfacecolor='blue', markersize=10)
]



# 1. Define the Custom Legend Elements
legend_elements = [


    # --- Section: Output Type (Colors) ---
    Line2D([0], [0], color='none', label=r'$\bf{Output\ Type}$'), # Bold Header
    Line2D([0], [0], marker='o', color='w', markerfacecolor=red[1], label='Coordinates (Red)', markersize=10),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=green[1], label='Allocentric (Green)', markersize=10),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=blue[1], label='Egocentric (Blue)', markersize=10),
    
    # --- Spacer ---
    Line2D([0], [0], color='none', label=''), 

    # --- Section: Input Format (Shapes) ---
    Line2D([0], [0], color='none', label=r'$\bf{Input\ Format}$'), # Bold Header
    Line2D([0], [0], marker='s', color='lightgrey', label='JPG', linestyle='None'),
    Line2D([0], [0], marker='*', color='lightgrey', label='JSON', linestyle='None'),
    Line2D([0], [0], marker='o', color='lightgrey', label='Adjacency JSON', linestyle='None'),
    Line2D([0], [0], marker='v', color='lightgrey', label='Adjacency Text', linestyle='None'),
    Line2D([0], [0], marker='D', color='lightgrey', label='Tokenized', linestyle='None'),
    Line2D([0], [0], marker='P', color='lightgrey', label='ASCII', linestyle='None'),

    # --- Spacer ---
    Line2D([0], [0], color='none', label=''), 

    # --- Section: Model (Hues) ---
    Line2D([0], [0], color='none', label=r'$\bf{Model\ (Marker\ Hue)}$'), # Bold Header
    Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', label='Gemini 2.5 Pro', markersize=10),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgray', label='Gemini 2.5 Flash Lite', markersize=10),

    # --- Spacer ---
    Line2D([0], [0], color='none', label=''), 

    # --- Maze Style ---
    Line2D([0], [0], color='none', label=r'$\bf{Maze\ Style}$' ), # Bold Header
    Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgrey', mec='black', ms = marker_size[0], label = 'Occupancy Grid Maze, 7x7, 13x13, 31x31' ),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgrey', ms = marker_size[1], label = 'Line Walled Maze, 3x3, 6x6, 15x15' ),
]


# 2. Add the custom legend to the axis
ax2.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))


# Place legend outside the plot on the right
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Representation, Complexity, Output Type, Model")
# plt.title("Performance vs. Cost Per Task")
ax1.set_title("Performance vs. Cost Per Task, Low Complexity")
ax2.set_title("Performance vs. Cost Per Task, Medium Complexity")
ax3.set_title("Performance vs. Cost Per Task, High Complexity")
# Adjust layout to make room for legend
plt.tight_layout(rect=[0, 0, 0.85, 1])  # leave 15% of width for legend


plt.show()











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

