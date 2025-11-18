import numpy as np
import pandas as pd
import dataframe_image as dfi
representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']


# NR - COORDS - 1-4 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 42.857142857142854, 100.0, 100.0])
line_jpg = np.array([40.0, 20.0, 40.0, 60.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_json = np.array([100.0, 20.0, 60.0, 20.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_tokenized_txt = np.array([20.0, 0.0, 0.0, 60.0, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 20.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 110.00000000000001])
occupancy_jpg = np.array([0.0, 0.0, 55.55555555555556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json = np.array([100.0, 110.00000000000001, 100.0, 110.00000000000001, 7.6923076923076925, 100.0, 110.00000000000001, 100.0, 100.0, 110.00000000000001])
occupancy_tokenized_txt = np.array([11.11111111111111, 110.00000000000001, 100.0, 100.0, 7.6923076923076925, 11.11111111111111, 100.0, 100.0, 7.6923076923076925, 110.00000000000001])

# Raw scores
line_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 3.0, 7.0, 5.0])
line_jpg_raw_score = np.array([2.0, 1.0, 2.0, 3.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_json_raw_score = np.array([5.0, 1.0, 3.0, 1.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_tokenized_txt_raw_score = np.array([1.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0])
occupancy_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_ascii_txt_raw_score = np.array([0.0, 9.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.0])  
occupancy_jpg_raw_score = np.array([0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 1.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_tokenized_txt_raw_score = np.array([1.0, 9.0, 9.0, 9.0, 1.0, 1.0, 9.0, 13.0, 1.0, 9])

# Prompt tokens
line_adj_json_input_tokens = np.array([714, 714, 714, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0])
line_adj_txt_input_tokens = np.array([346, 346, 346, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0])
line_jpg_input_tokens = np.array([429, 429, 429, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0])
line_json_input_tokens = np.array([652, 652, 652, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0])
line_tokenized_txt_input_tokens = np.array([317, 317, 317, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0])
occupancy_adj_json_input_tokens = np.array([1176, 1176, 1176, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0])
occupancy_adj_txt_input_tokens = np.array([458, 458, 458, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0])
occupancy_ascii_txt_input_tokens = np.array([195, 195, 193, 201.0, 201.0, 201.0, 201.0, 201.0, 201.0, 199.0])
occupancy_jpg_input_tokens = np.array([424, 424, 424, 430.0, 430.0, 430.0, 430.0, 430.0, 430.0, 430.0])
occupancy_json_input_tokens = np.array([467, 467, 467, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0])
occupancy_tokenized_txt_input_tokens = np.array([746, 746, 746, 752, 752.0, 752.0, 752.0, 752.0, 752.0, 752])


# Output tokens
line_adj_json_output_tokens = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 29.0, 29.0, 21.0])
line_adj_txt_output_tokens = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 21.0, 29.0, 21.0])
line_jpg_output_tokens = np.array([21, 21, 33, 21.0, 21.0, 21.0, 29.0, 21.0, 21.0, 21.0])
line_json_output_tokens = np.array([21, 21, 21, 17.0, 21.0, 21.0, 17.0, 29.0, 21.0, 21.0])
line_tokenized_txt_output_tokens = np.array([21, 25, 13, 29.0, 17.0, 17.0, 25.0, 21.0, 17.0, 29.0])
occupancy_adj_json_output_tokens = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_adj_txt_output_tokens = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_ascii_txt_output_tokens = np.array([57, 57, 125, 53.0, 41.0, 45.0, 57.0, 41.0, 57.0, 53.0])
occupancy_jpg_output_tokens = np.array([45, 49, 41, 49.0, 73.0, 45.0, 65.0, 41.0, 53.0, 57.0])
occupancy_json_output_tokens = np.array([37, 53, 37, 53.0, 69.0, 37.0, 53.0, 53.0, 53.0, 101.0])
occupancy_tokenized_txt_output_tokens = np.array([41, 53, 37, 37, 49.0, 65.0, 37.0, 53.0, 53.0, 53])



# # Set up runs for table
# x_axis = [1, 2, 3]
# complexities = [f"Run {x_axis[i]}" for i in range(3)]

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Flash Lite, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_NR_coords.png")


# NR - ALLO - 1-4 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([0.0, 0.0, 100.0, 100.0])
line_adj_txt = np.array([0.0, 100.0, 0.0, 100.0])
line_jpg = np.array([50.0, 0.0, 50.0, 100.0])
line_json = np.array([100.0, 0.0, 100.0, 0.0])
line_tokenized_txt = np.array([0.0, 100.0, 0.0, 25.0])
occupancy_adj_json = np.array([50.0, 25.0, 75.0, 110.00000000000001])
occupancy_adj_txt = np.array([62.5, 25.0, 0.0, 37.5])
occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 0.0])
occupancy_jpg = np.array([12.5, 0.0, 12.5, 0.0])
occupancy_json = np.array([62.5, 0.0, 0.0, 0.0])
occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 50.0])

# Raw Scores
line_adj_json_raw_score = np.array([0.0, 0.0, 4.0, 4.0])
line_adj_txt_raw_score = np.array([0.0, 4.0, 0.0, 4.0])
line_jpg_raw_score = np.array([2.0, 0.0, 2.0, 4.0])
line_json_raw_score = np.array([4.0, 0.0, 4.0, 0.0])
line_tokenized_txt_raw_score = np.array([0.0, 4.0, 0.0, 1.0])
occupancy_adj_json_raw_score = np.array([4.0, 2.0, 6.0, 8.0])
occupancy_adj_txt_raw_score = np.array([5.0, 2.0, 0.0, 3.0])
occupancy_ascii_txt_raw_score = np.array([0.0, 8.0, 0.0, 0.0])
occupancy_jpg_raw_score = np.array([1.0, 0.0, 1.0, 0.0])
occupancy_json_raw_score = np.array([5.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 4])

# Prompt tokens
line_adj_json_input_tokens = np.array([706, 706, 706, 712.0])
line_adj_txt_input_tokens = np.array([338, 338, 338, 344.0])
line_jpg_input_tokens = np.array([421, 421, 421, 427.0])
line_json_input_tokens = np.array([644, 644, 644, 650.0])
line_tokenized_txt_input_tokens = np.array([309, 309, 309, 315.0])
occupancy_adj_json_input_tokens = np.array([1168, 1168, 1168, 1174.0])
occupancy_adj_txt_input_tokens = np.array([450, 450, 450, 456.0])
occupancy_ascii_txt_input_tokens = np.array([187, 187, 185, 193.0])
occupancy_jpg_input_tokens = np.array([416, 416, 416, 422.0])
occupancy_json_input_tokens = np.array([459, 459, 459, 465.0])
occupancy_tokenized_txt_input_tokens = np.array([738, 738, 738, 744])

# Output tokens
line_adj_json_output_tokens = np.array([7, 7, 7, 7.0])
line_adj_txt_output_tokens = np.array([7, 7, 7, 7.0])
line_jpg_output_tokens = np.array([7, 218, 7, 7.0])
line_json_output_tokens = np.array([7, 7, 7, 7.0])
line_tokenized_txt_output_tokens = np.array([5, 7, 5, 7.0])
occupancy_adj_json_output_tokens = np.array([17, 15, 21, 19.0])
occupancy_adj_txt_output_tokens = np.array([21, 17, 1734, 15.0])
occupancy_ascii_txt_output_tokens = np.array([43, 29, 43, 23.0])
occupancy_jpg_output_tokens = np.array([21, 15, 15, 49.0])
occupancy_json_output_tokens = np.array([17, 21, 45, 21.0])
occupancy_tokenized_txt_output_tokens = np.array([33, 59, 4000, 650])

# # Set up complexities for table
# x_axis = [1, 2, 3]
# complexities = [f"Run {x_axis[i]}" for i in range(3)]

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Flash Lite, Allocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_NR_allo.png")

# NR - EGO - 1-4 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([25.0, 0.0, 25.0, 0.0])
line_adj_txt = np.array([0.0, 0.0, 0.0, 0.0])
line_jpg = np.array([0.0, 0.0, 0.0, 0.0])
line_json = np.array([25.0, 0.0, 0.0, 0.0])
line_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_adj_json = np.array([0.0, 0.0, 12.5, 0.0])
occupancy_adj_txt = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_jpg = np.array([0.0, 0.0, 12.5, 0.0])
occupancy_json = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0])


# Raw Scores
line_adj_json_raw_score = np.array([1.0, 0.0, 1.0, 0.0])
line_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0])
line_jpg_raw_score = np.array([0.0, 0.0, 0.0, 0.0])
line_json_raw_score = np.array([1.0, 0.0, 0.0, 0.0])
line_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_adj_json_raw_score = np.array([0.0, 0.0, 1.0, 0.0])
occupancy_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_jpg_raw_score = np.array([0.0, 0.0, 1.0, 0.0])
occupancy_json_raw_score = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0])

# Prompt tokens
line_adj_json_input_tokens = np.array([816, 816, 816, 836.0])
line_adj_txt_input_tokens = np.array([448, 448, 448, 468.0])
line_jpg_input_tokens = np.array([531, 531, 531, 551.0])
line_json_input_tokens = np.array([754, 754, 754, 774.0])
line_tokenized_txt_input_tokens = np.array([419, 419, 419, 439.0])
occupancy_adj_json_input_tokens = np.array([1278, 1278, 1278, 1298.0])
occupancy_adj_txt_input_tokens = np.array([560, 560, 560, 580.0])
occupancy_ascii_txt_input_tokens = np.array([297, 297, 295, 317.0])
occupancy_jpg_input_tokens = np.array([526, 526, 526, 546.0])
occupancy_json_input_tokens = np.array([569, 569, 569, 589.0])
occupancy_tokenized_txt_input_tokens = np.array([848, 848, 848, 868])

# Output tokens
line_adj_json_output_tokens = np.array([13, 4000, 11, 15.0])
line_adj_txt_output_tokens = np.array([15, 17, 13, 11.0])
line_jpg_output_tokens = np.array([23, 17, 15, 15.0])
line_json_output_tokens = np.array([11, 11, 13, 19.0])
line_tokenized_txt_output_tokens = np.array([17, 4000, 17, 649.0])
occupancy_adj_json_output_tokens = np.array([33, 4000, 31, 99.0])
occupancy_adj_txt_output_tokens = np.array([4000, 49, 4000, 49.0])
occupancy_ascii_txt_output_tokens = np.array([133, 4000, 4000, 35.0])
occupancy_jpg_output_tokens = np.array([25, 27, 33, 23.0])
occupancy_json_output_tokens = np.array([4000, 4000, 79, 55.0])
occupancy_tokenized_txt_output_tokens = np.array([4000, 1561, 1029, 49])

# # Set up complexities for table
# x_axis = [1, 2, 3]
# complexities = [f"Run {x_axis[i]}" for i in range(3)]

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Flash Lite, Egocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_NR_ego.png")

# # R - COORDS -  - 1-4 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0])
line_jpg = np.array([40.0, 100.0, 100.0, 100.0])
line_json = np.array([100.0, 100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([22.22222222222222, 100.0, 100.0, 100.0])
occupancy_jpg = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556, 0.0])
occupancy_json = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0])
line_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0])
line_jpg_raw_score = np.array([2.0, 5.0, 5.0, 5.0])
line_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0])
line_tokenized_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0])
occupancy_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0])
occupancy_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0])
occupancy_ascii_txt_raw_score = np.array([2.0, 9.0, 9.0, 9.0])
occupancy_jpg_raw_score = np.array([1.0, 2.0, 5.0, 0.0])
occupancy_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0])
occupancy_tokenized_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0])

# Prompt tokens
line_adj_json_input_tokens = np.array([714, 720, 720, 720.0])
line_adj_txt_input_tokens = np.array([346, 352, 352, 352.0])
line_jpg_input_tokens = np.array([429, 435, 435, 435.0])
line_json_input_tokens = np.array([652, 658, 658, 658.0])
line_tokenized_txt_input_tokens = np.array([317, 323, 323, 323.0])
occupancy_adj_json_input_tokens = np.array([1176, 1182, 1182, 1182.0])
occupancy_adj_txt_input_tokens = np.array([458, 464, 464, 464.0])
occupancy_ascii_txt_input_tokens = np.array([194, 200, 198, 200.0])
occupancy_jpg_input_tokens = np.array([434, 440, 440, 440.0])
occupancy_json_input_tokens = np.array([467, 473, 473, 473.0])
occupancy_tokenized_txt_input_tokens = np.array([746, 752, 752, 752.0])

# Output tokens
line_adj_json_output_tokens = np.array([1625, 1289, 898, 1267.0])
line_adj_txt_output_tokens = np.array([2264, 2798, 2034, 1651.0])
line_jpg_output_tokens = np.array([16131, 5588, 3890, 10788.0])
line_json_output_tokens = np.array([1475, 1115, 1274, 1052.0])
line_tokenized_txt_output_tokens = np.array([1408, 1207, 1637, 1361.0])
occupancy_adj_json_output_tokens = np.array([2077, 2469, 3461, 3086.0])
occupancy_adj_txt_output_tokens = np.array([3621, 4114, 3696, 3970.0])
occupancy_ascii_txt_output_tokens = np.array([9407, 8884, 1926, 6484.0])
occupancy_jpg_output_tokens = np.array([1713, 1428, 7030, 3242.0])
occupancy_json_output_tokens = np.array([3193, 2760, 4692, 5823.0])
occupancy_tokenized_txt_output_tokens = np.array([4248, 2453, 2759, 3372])


# # Set up complexities for table
# x_axis = [1, 2, 3]
# complexities = [f"Run {x_axis[i]}" for i in range(3)]

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Pro, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_R_coords.png")

# # R - EGO -  - 1-4 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([25.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([25.0, 100.0, 100.0, 100.0])
line_jpg = np.array([25.0, 0.0, 50.0, 50.0])
line_json = np.array([100.0, 100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_jpg = np.array([12.5, 0.0, 0.0, 50.0])
occupancy_json = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([0.0, 100.0, 100.0, 100.0])

# Raw Scores
line_adj_json_raw_score = np.array([1.0, 4.0, 4.0, 4.0])
line_adj_txt_raw_score = np.array([1.0, 4.0, 4.0, 4.0])
line_jpg_raw_score = np.array([1.0, 0.0, 2.0, 2.0])
line_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0])
line_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0])
occupancy_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_jpg_raw_score = np.array([1.0, 0.0, 0.0, 4.0])
occupancy_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_tokenized_txt_raw_score = np.array([0.0, 8.0, 8.0, 8])

# Prompt tokens
line_adj_json_input_tokens = np.array([822, 822, 829, 829.0])
line_adj_txt_input_tokens = np.array([454, 454, 461, 461.0])
line_jpg_input_tokens = np.array([537, 537, 544, 544.0])
line_json_input_tokens = np.array([760, 760, 767, 767.0])
line_tokenized_txt_input_tokens = np.array([425, 425, 432, 432.0])
occupancy_adj_json_input_tokens = np.array([1284, 1284, 1291, 1291.0])
occupancy_adj_txt_input_tokens = np.array([566, 566, 573, 573.0])
occupancy_ascii_txt_input_tokens = np.array([302, 302, 307, 309.0])
occupancy_jpg_input_tokens = np.array([542, 542, 549, 549.0])
occupancy_json_input_tokens = np.array([575, 575, 582, 582.0])
occupancy_tokenized_txt_input_tokens = np.array([854, 854, 861, 861.0])

# Output tokens
line_adj_json_output_tokens = np.array([3560, 2534, 2248, 5136.0])
line_adj_txt_output_tokens = np.array([2930, 3587, 1933, 2641.0])
line_jpg_output_tokens = np.array([8539, 4203, 1105, 6439.0])
line_json_output_tokens = np.array([2401, 3116, 2388, 2223.0])
line_tokenized_txt_output_tokens = np.array([3418, 3481, 2694, 2831.0])
occupancy_adj_json_output_tokens = np.array([2912, 2264, 2449, 5428.0])
occupancy_adj_txt_output_tokens = np.array([5534, 2162, 5607, 3270.0])
occupancy_ascii_txt_output_tokens = np.array([7469, 3371, 3412, 9243.0])
occupancy_jpg_output_tokens = np.array([4816, 9362, 2226, 1635.0])
occupancy_json_output_tokens = np.array([4612, 5353, 4658, 4597.0])
occupancy_tokenized_txt_output_tokens = np.array([3530, 4654, 2890, 4121.0])

# # Set up complexities for table
# x_axis = [1, 2, 3]
# complexities = [f"Run {x_axis[i]}" for i in range(3)]

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Pro, Egocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_R_ego.png")


# # R - ALLO -  - 1-3 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0])
line_jpg = np.array([0.0, 0.0, 100.0, 100.0])
line_json = np.array([100.0, 100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_jpg = np.array([0.0, 0.0, 0.0, 50.0])
occupancy_json = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_adj_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0])
line_adj_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0])
line_jpg_raw_score = np.array([0.0, 0.0, 4.0, 4.0])
line_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0])
line_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0])
occupancy_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_jpg_raw_score = np.array([0.0, 0.0, 0.0, 4.0])
occupancy_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0])
occupancy_tokenized_txt_raw_score = np.array([8.0, 8.0, 8.0, 8])

# Prompt tokens
line_adj_json_input_tokens = np.array([712, 712, 712, 712.0])
line_adj_txt_input_tokens = np.array([344, 344, 344, 344.0])
line_jpg_input_tokens = np.array([427, 427, 427, 427.0])
line_json_input_tokens = np.array([650, 650, 650, 650.0])
line_tokenized_txt_input_tokens = np.array([315, 315, 315, 315.0])
occupancy_adj_json_input_tokens = np.array([1174, 1174, 1174, 1174.0])
occupancy_adj_txt_input_tokens = np.array([456, 456, 456, 456.0])
occupancy_ascii_txt_input_tokens = np.array([192, 192, 190, 192.0])
occupancy_jpg_input_tokens = np.array([432, 432, 432, 432.0])
occupancy_json_input_tokens = np.array([465, 465, 465, 465.0])
occupancy_tokenized_txt_input_tokens = np.array([744, 744, 744, 744])

# Output tokens
line_adj_json_output_tokens = np.array([1729, 1338, 1698, 1356.0])
line_adj_txt_output_tokens = np.array([2080, 4596, 2232, 1912.0])
line_jpg_output_tokens = np.array([14536, 2225, 1313, 1583.0])
line_json_output_tokens = np.array([1366, 1420, 1475, 1144.0])
line_tokenized_txt_output_tokens = np.array([1403, 1250, 1290, 933.0])
occupancy_adj_json_output_tokens = np.array([4853, 3989, 3209, 3350.0])
occupancy_adj_txt_output_tokens = np.array([7175, 7839, 4911, 8476.0])
occupancy_ascii_txt_output_tokens = np.array([3455, 3764, 4552, 3401.0])
occupancy_jpg_output_tokens = np.array([9275, 2057, 17922, 2315.0])
occupancy_json_output_tokens = np.array([4247, 3624, 3078, 3722.0])
occupancy_tokenized_txt_output_tokens = np.array([2474, 2171, 1444, 3519])

# Set up complexities for table
x_axis = [1, 2, 3]
complexities = [f"Run {x_axis[i]}" for i in range(3)]

data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt,  line_tokenized_txt,
                          occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])

table = pd.DataFrame(
    data=data_stacked,
    index=representations,        # row labels
    columns=complexities          # column labels
)
print(table.round(3))
table.plot(kind="bar", figsize=(15,10))

# Create and save table image
table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Pro, Allocentric Output").format(precision=3)
dfi.export(table_img, "table_accuracy_Dataset03_R_allo.png")