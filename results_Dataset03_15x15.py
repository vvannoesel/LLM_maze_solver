import numpy as np
import pandas as pd
import dataframe_image as dfi

representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']


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





# R - COORDS - only run 1 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([19.083969465648856, 14.492753623188406, 51.798561151079134, 100.0, 60.629921259842526, 92.07920792079209, 100.0, 62.02531646, 46.616541353383454, 100.0])
line_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json = np.array([23.66412213740458, 15.942028985507244, 7.194244604316546, 7.017543859649122, 12.598425196850393, 9.900990099009901, 56.71641791044776, 50.63291139240506, 1.5037593984962405, 42.5531914893617])
line_tokenized_txt = np.array([96.18320610687023, 100.0, 100.0, 100.0, 92.1259842519685, 22.772277227722775, 100.0, 62.0253164556962, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 68.95306859205776, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([34.099616858237546, 15.328467153284672, 24.90974729241877, 29.20353982300885, 12.25296442687747, 42.28855721393035, 3.7593984962406015, 57.961783439490446, 46.41509433962264, 95.6989247311828])
occupancy_ascii_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.301075268817205])
occupancy_jpg = np.array([1.9157088122605364, 4.37956204379562, 1.083032490974729, 0.8849557522123894, 0.3952569169960474, 0.0, 0.7518796992481203, 0.0, 0.0, 0.0])
occupancy_json = np.array([11.877394636015326, 35.03649635036496, 1.8050541516245486, 15.04424778761062, 3.557312252964427, 21.393034825870647, 30.075187969924812, 15.92356687898089, 7.169811320754717, 33.33333333333333])
occupancy_tokenized_txt = np.array([39.46360153256705, 100.0, 7.581227436823104, 100.0, 7.905138339920949, 7.462686567164178, 100.0, 13.375796178343949, 6.415094339622642, 11.827956989247312])


# Raw scores
line_adj_json_raw_score = np.array([131.0, 69.0, 139.0, 57.0, 127.0, 101.0, 67.0, 79.0, 133.0, 47.0])
line_adj_txt_raw_score = np.array([25.0, 10.0, 72.0, 57.0, 77.0, 93.0, 67.0, 49.0, 62.0, 47.0])
line_jpg_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_raw_score = np.array([31.0, 11.0, 10.0, 4.0, 16.0, 10.0, 38.0, 40.0, 2.0, 20.0])
line_tokenized_txt_raw_score = np.array([126.0, 69.0, 139.0, 57.0, 117.0, 23.0, 67.0, 49.0, 133.0, 47.0])
occupancy_adj_json_raw_score = np.array([261.0, 137.0, 191.0, 113.0, 253.0, 201.0, 133.0, 157.0, 265.0, 93.0])
occupancy_adj_txt_raw_score = np.array([89.0, 21.0, 69.0, 33.0, 31.0, 85.0, 5.0, 91.0, 123.0, 89.0])
occupancy_ascii_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0])
occupancy_jpg_raw_score = np.array([5.0, 6.0, 3.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0])
occupancy_json_raw_score = np.array([31.0, 48.0, 5.0, 17.0, 9.0, 43.0, 40.0, 25.0, 19.0, 31.0])
occupancy_tokenized_txt_raw_score = np.array([103.0, 137.0, 21.0, 113.0, 20, 15.0, 133.0, 21.0, 17.0, 11.0])


# Prompt tokens
line_adj_json_input_tokens = np.array([13491.0, 13493.0, 13492.0, 13497.0, 13491.0, 13495.0, 13493.0, 13493.0, 13494.0, 13498.0])
line_adj_txt_input_tokens = np.array([3683.0, 3685.0, 3684.0, 3689.0, 3683.0, 3687.0, 3685.0, 3290.0, 3686.0, 3690.0])
line_jpg_input_tokens = np.array([437.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0])
line_json_input_tokens = np.array([9808.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0])
line_tokenized_txt_input_tokens = np.array([3283.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0])
occupancy_adj_json_input_tokens = np.array([27636.0, 27635.0, 27643.0, 27640.0, 27647.0, 27648.0, 27648.0, 27647.0, 27641.0, 27638.0])
occupancy_adj_txt_input_tokens = np.array([7732.0, 7733.0, 7739.0, 7737.0, 7741.0, 7743.0, 7743.0, 7742.0, 7737.0, 7735.0])
occupancy_ascii_txt_input_tokens = np.array([548.0, 547.0, 553.0, 540.0, 534.0, 535.0, 542.0, 555.0, 550.0, 546.0])
occupancy_jpg_input_tokens = np.array([442.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0])
occupancy_json_input_tokens = np.array([4247.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0])
occupancy_tokenized_txt_input_tokens = np.array([12136.0, 12142.0, 12142.0, 12142.0, 12142, 12142.0, 12142.0, 12142.0, 12142.0, 12142.0])


# Output tokens
line_adj_json_output_tokens = np.array([24319.0, 16225.0, 24616.0, 8139.0, 19260.0, 12408.0, 7826.0, 15115.0, 20876.0, 5314.0])
line_adj_txt_output_tokens = np.array([33577.0, 24330.0, 25615.0, 20071.0, 19655.0, 28924.0, 10897.0, 24814.0, 7706.0, 14201.0])
line_jpg_output_tokens = np.array([4504.0, 3944.0, 10750.0, 16490.0, 5091.0, 4180.0, 6718.0, 7549.0, 14674.0, 6569.0])
line_json_output_tokens = np.array([14877.0, 21134.0, 24389.0, 22863.0, 26197.0, 20740.0, 29735.0, 15855.0, 23004.0, 19638.0])
line_tokenized_txt_output_tokens = np.array([27012.0, 8104.0, 16779.0, 5941.0, 17585.0, 22661.0, 10570.0, 24814.0, 14842.0, 7821.0])
occupancy_adj_json_output_tokens = np.array([38108.0, 12526.0, 44759.0, 8955.0, 18015.0, 11288.0, 13758.0, 17437.0, 30188.0, 9741.0])
occupancy_adj_txt_output_tokens = np.array([35979.0, 29317.0, 27858.0, 29722.0, 32951.0, 27173.0, 32997.0, 27944.0, 33251.0, 22642.0])
occupancy_ascii_txt_output_tokens = np.array([10674.0, 7006.0, 14414.0, 10515.0, 9263.0, 11732.0, 19721.0, 10736.0, 16575.0, 19719.0])
occupancy_jpg_output_tokens = np.array([10193.0, 12494.0, 13728.0, 8963.0, 9955.0, 5758.0, 8949.0, 16009.0, 6946.0, 17182.0])
occupancy_json_output_tokens = np.array([17287.0, 13432.0, 24426.0, 19069.0, 20997.0, 19289.0, 25754.0, 15716.0, 18421.0, 19336.0])
occupancy_tokenized_txt_output_tokens = np.array([27461.0, 12623.0, 26548.0, 17015.0, 24129, 26580.0, 19448.0, 25165.0, 27684.0, 22137.0])



# R - ALLO - only run 1 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([46.92307692307692])
line_adj_txt = np.array([7.6923076923076925])
line_jpg = np.array([0.7692307692307693])
line_json = np.array([27.692307692307693])
line_tokenized_txt = np.array([33.07692307692307])
occupancy_adj_json = np.array([46.15384615384615])
occupancy_adj_txt = np.array([27.692307692307693])
occupancy_ascii_txt = np.array([1.5384615384615385])
occupancy_jpg = np.array([1.153846153846154])
occupancy_json = np.array([0.38461538461538464])
occupancy_tokenized_txt = np.array([25.384615384615383])

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
