import numpy as np
import pandas as pd
import dataframe_image as dfi

representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']


# NR - ALLO - only run 1 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([0.0])
line_adj_txt = np.array([0.0])
line_jpg = np.array([np.nan])
line_json = np.array([1.5384615384615385])
line_tokenized_txt = np.array([0.0])
occupancy_adj_json = np.array([0.7692307692307693])
occupancy_adj_txt = np.array([0.0])
occupancy_ascii_txt = np.array([0.0])
occupancy_jpg = np.array([np.nan])
occupancy_json = np.array([0.0])
occupancy_tokenized_txt = np.array([0.0])

# Raw Scores
line_adj_json_raw_score = np.array([0])
line_adj_txt_raw_score = np.array([0])
line_jpg_raw_score = np.array([np.nan])
line_json_raw_score = np.array([2])
line_tokenized_txt_raw_score = np.array([0])
occupancy_adj_json_raw_score = np.array([2])
occupancy_adj_txt_raw_score = np.array([0])
occupancy_ascii_txt_raw_score = np.array([0])
occupancy_jpg_raw_score = np.array([np.nan])
occupancy_json_raw_score = np.array([0])
occupancy_tokenized_txt_raw_score = np.array([0])

# Prompt tokens

# Output tokens

# Set up runs for table
# x_axis = [1]
# complexities = [f"Run {x_axis[i]}" for i in range(1)]

# data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt,  line_tokenized_txt,
#                           occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])

# table = pd.DataFrame(
#     data=data_stacked,
#     index=representations,        # row labels
#     columns=complexities          # column labels
# )
# print(table.round(3))
# table.plot(kind="bar", figsize=(15,10))

# # Create and save table image
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Flash Lite, Allocentric Output  ** nan = no answer given").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_NR_allo.png")



# NR - EGO - only run 1 ----------------------------------------------------------------

# Accuracy
# line_adj_json = np.array([0.0])
# line_adj_txt = np.array([1.5384615384615385])
# line_jpg = np.array([1.5384615384615385])
# line_json = np.array([1.5384615384615385])
# line_tokenized_txt = np.array([0.7692307692307693])
# occupancy_adj_json = np.array([0.0])
# occupancy_adj_txt = np.array([1.5384615384615385])
# occupancy_ascii_txt = np.array([0.0])
# occupancy_jpg = np.array([0.7692307692307693])
# occupancy_json = np.array([0.0])
# occupancy_tokenized_txt = np.array([0.38461538461538464])

# Raw Scores
line_adj_json_raw_score = np.array([0])
line_adj_txt_raw_score = np.array([2])
line_jpg_raw_score = np.array([2])
line_json_raw_score = np.array([2])
line_tokenized_txt_raw_score = np.array([1])
occupancy_adj_json_raw_score = np.array([0])
occupancy_adj_txt_raw_score = np.array([4])
occupancy_ascii_txt_raw_score = np.array([0])
occupancy_jpg_raw_score = np.array([2])
occupancy_json_raw_score = np.array([0])
occupancy_tokenized_txt_raw_score = np.array([1])

# Prompt tokens

# Output tokens

# # Set up runs for table
# x_axis = [1]
# complexities = [f"Run {x_axis[i]}" for i in range(1)]

# data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt,  line_tokenized_txt,
#                           occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])

# table = pd.DataFrame(
#     data=data_stacked,
#     index=representations,        # row labels
#     columns=complexities          # column labels
# )
# print(table.round(3))
# table.plot(kind="bar", figsize=(15,10))

# # Create and save table image
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Flash Lite, Egocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_NR_ego.png")

# NR - COORDS - only run 1 ----------------------------------------------------------------

# Accuracy
# line_adj_json = np.array([2.2900763358778624])
# line_adj_txt = np.array([8.396946564885496])
# line_jpg = np.array([3.0534351145038165])
# line_json = np.array([1.5267175572519083])
# line_tokenized_txt = np.array([0.7633587786259541])
# occupancy_adj_json = np.array([25.67049808429119])
# occupancy_adj_txt = np.array([5.747126436781609])
# occupancy_ascii_txt = np.array([0.0])
# occupancy_jpg = np.array([0.0])
# occupancy_json = np.array([0.38314176245210724])
# occupancy_tokenized_txt = np.array([0.38314176245210724])

# Raw Scores
line_adj_json_raw_score = np.array([3])
line_adj_txt_raw_score = np.array([11])
line_jpg_raw_score = np.array([4])
line_json_raw_score = np.array([2])
line_tokenized_txt_raw_score = np.array([1])
occupancy_adj_json_raw_score = np.array([67])
occupancy_adj_txt_raw_score = np.array([15])
occupancy_ascii_txt_raw_score = np.array([0])
occupancy_jpg_raw_score = np.array([0])
occupancy_json_raw_score = np.array([1])
occupancy_tokenized_txt_raw_score = np.array([1])

# Prompt tokens

# Output tokens

# # Set up runs for table
# x_axis = [1]
# complexities = [f"Run {x_axis[i]}" for i in range(1)]

# data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt,  line_tokenized_txt,
#                           occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])

# table = pd.DataFrame(
#     data=data_stacked,
#     index=representations,        # row labels
#     columns=complexities          # column labels
# )
# print(table.round(3))
# table.plot(kind="bar", figsize=(15,10))

# # Create and save table image
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Flash Lite, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_NR_coords.png")


# R - ALLO - only run 1 ----------------------------------------------------------------

# Accuracy
# line_adj_json = np.array([46.92307692307692])
# line_adj_txt = np.array([7.6923076923076925])
# line_jpg = np.array([0.7692307692307693])
# line_json = np.array([27.692307692307693])
# line_tokenized_txt = np.array([33.07692307692307])
# occupancy_adj_json = np.array([46.15384615384615])
# occupancy_adj_txt = np.array([27.692307692307693])
# occupancy_ascii_txt = np.array([1.5384615384615385])
# occupancy_jpg = np.array([1.153846153846154])
# occupancy_json = np.array([0.38461538461538464])
# occupancy_tokenized_txt = np.array([25.384615384615383])

# Raw Scores
line_adj_json_raw_score = np.array([61])
line_adj_txt_raw_score = np.array([10])
line_jpg_raw_score = np.array([1])
line_json_raw_score = np.array([36])
line_tokenized_txt_raw_score = np.array([43])
occupancy_adj_json_raw_score = np.array([120])
occupancy_adj_txt_raw_score = np.array([72])
occupancy_ascii_txt_raw_score = np.array([4])
occupancy_jpg_raw_score = np.array([3])
occupancy_json_raw_score = np.array([1])
occupancy_tokenized_txt_raw_score = np.array([66])

# Prompt tokens

# Output tokens

# # Set up runs for table
# x_axis = [1]
# complexities = [f"Run {x_axis[i]}" for i in range(1)]

# data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt,  line_tokenized_txt,
#                           occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])

# table = pd.DataFrame(
#     data=data_stacked,
#     index=representations,        # row labels
#     columns=complexities          # column labels
# )
# print(table.round(3))
# table.plot(kind="bar", figsize=(15,10))

# # Create and save table image
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Pro, Allocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_R_allo.png")

# R - EGO - only run 1 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([3.076923076923077])
line_adj_txt = np.array([2.307692307692308])
line_jpg = np.array([0.7692307692307693])
line_json = np.array([3.076923076923077])
line_tokenized_txt = np.array([1.5384615384615385])
occupancy_jpg = np.array([1.5384615384615385])
occupancy_json = np.array([3.8461538461538463])
occupancy_adj_json = np.array([34.23076923076923])
occupancy_adj_txt = np.array([1.5384615384615385])
occupancy_ascii_txt = np.array([0.7692307692307693])
occupancy_tokenized_txt = np.array([27.307692307692307])

# Raw Scores
line_adj_json_raw_score = np.array([4.0])
line_adj_txt_raw_score = np.array([3.0])
line_jpg_raw_score = np.array([1.0])
line_json_raw_score = np.array([4.0])
line_tokenized_txt_raw_score = np.array([2.0])
occupancy_jpg_raw_score = np.array([4.0])
occupancy_json_raw_score = np.array([10.0])
occupancy_adj_json_raw_score = np.array([89.0])
occupancy_adj_txt_raw_score = np.array([4.0])
occupancy_ascii_txt_raw_score = np.array([2.0])
occupancy_tokenized_txt_raw_score = np.array([71])


# Prompt tokens
occupancy_adj_json_input_tokens = np.array([27745])
occupancy_adj_txt_input_tokens = np.array([7841.0])
occupancy_ascii_txt_input_tokens = np.array([657])
occupancy_tokenized_txt_input_tokens = np.array([12245])

# Output tokens
occupancy_adj_json_output_tokens = np.array([18870])
occupancy_adj_txt_output_tokens = np.array([38830.0])
occupancy_ascii_txt_output_tokens = np.array([18233])
occupancy_tokenized_txt_output_tokens = np.array([31644])

# # Set up runs for table
# x_axis = [1]
# complexities = [f"Run {x_axis[i]}" for i in range(1)]

# data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt,  line_tokenized_txt,
#                           occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])

# table = pd.DataFrame(
#     data=data_stacked,
#     index=representations,        # row labels
#     columns=complexities          # column labels
# )
# print(table.round(3))
# table.plot(kind="bar", figsize=(15,10))

# # Create and save table image
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Pro, Egocentric Outputn   ** nan = run not yet complete").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_R_ego.png")

# R - COORDS - only run 1 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([100.0])
line_adj_txt = np.array([19.083969465648856])
line_jpg = np.array([0.0])
line_json = np.array([23.66412213740458])
line_tokenized_txt = np.array([96.18320610687023])
occupancy_adj_json = np.array([100.0])
occupancy_adj_txt = np.array([34.099616858237546])
occupancy_ascii_txt = np.array([0.0])
occupancy_jpg = np.array([1.9157088122605364])
occupancy_json = np.array([11.877394636015326])
occupancy_tokenized_txt = np.array([39.46360153256705])

# Raw scores
line_adj_json_raw_score = np.array([131.0])
line_adj_txt_raw_score = np.array([25.0])
line_jpg_raw_score = np.array([0.0])
line_json_raw_score = np.array([31.0])
line_tokenized_txt_raw_score = np.array([126.0])
occupancy_adj_json_raw_score = np.array([261.0])
occupancy_adj_txt_raw_score = np.array([89.0])
occupancy_ascii_txt_raw_score = np.array([0.0])
occupancy_jpg_raw_score = np.array([5.0])
occupancy_json_raw_score = np.array([31.0])
occupancy_tokenized_txt_raw_score = np.array([103])

# Prompt tokens
line_adj_json_input_tokens = np.array([13491.0])
line_adj_txt_input_tokens = np.array([3683.0])
line_jpg_input_tokens = np.array([437.0])
line_json_input_tokens = np.array([9808.0])
line_tokenized_txt_input_tokens = np.array([3283.0])
occupancy_adj_json_input_tokens = np.array([27636.0])
occupancy_adj_txt_input_tokens = np.array([7732.0])
occupancy_ascii_txt_input_tokens = np.array([548.0])
occupancy_jpg_input_tokens = np.array([442.0])
occupancy_json_input_tokens = np.array([4247.0])
occupancy_tokenized_txt_input_tokens = np.array([12136])

# Output tokens
line_adj_json_output_tokens = np.array([24319.0])
line_adj_txt_output_tokens = np.array([33577.0])
line_jpg_output_tokens = np.array([4504.0])
line_json_output_tokens = np.array([14877.0])
line_tokenized_txt_output_tokens = np.array([27012.0])
occupancy_adj_json_output_tokens = np.array([38108.0])
occupancy_adj_txt_output_tokens = np.array([35979.0])
occupancy_ascii_txt_output_tokens = np.array([10674.0])
occupancy_jpg_output_tokens = np.array([10193.0])
occupancy_json_output_tokens = np.array([17287.0])
occupancy_tokenized_txt_output_tokens = np.array([27461])

