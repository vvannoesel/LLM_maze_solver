import numpy as np
import pandas as pd
import dataframe_image as dfi
representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']


# NR - COORDS - 1-4 ----------------------------------------------------------------

# Accuracy
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0])
line_jpg = np.array([40.0, 20.0, 40.0, 60.0])
line_json = np.array([100.0, 20.0, 60.0, 20.0])
line_tokenized_txt = np.array([20.0, 0.0, 0.0, 60.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 110.00000000000001])
occupancy_jpg = np.array([0.0, 0.0, 55.55555555555556, 0.0])
occupancy_json = np.array([100.0, 110.00000000000001, 100.0, 110.00000000000001])
occupancy_tokenized_txt = np.array([11.11111111111111, 110.00000000000001, 100.0, 100.0])

# Raw scores
line_adj_json = np.array([5.0, 5.0, 5.0, 5.0])
line_adj_txt = np.array([5.0, 5.0, 5.0, 5.0])
line_jpg = np.array([2.0, 1.0, 2.0, 3.0])
line_json = np.array([5.0, 1.0, 3.0, 1.0])
line_tokenized_txt = np.array([1.0, 0.0, 0.0, 3.0])
occupancy_adj_json = np.array([9.0, 9.0, 9.0, 9.0])
occupancy_adj_txt = np.array([9.0, 9.0, 9.0, 9.0])
occupancy_ascii_txt = np.array([0.0, 9.0, 0.0, 9.0])  
occupancy_jpg = np.array([0.0, 0.0, 5.0, 0.0])
occupancy_json = np.array([9.0, 9.0, 9.0, 9.0])
occupancy_tokenized_txt = np.array([1.0, 9.0, 9.0, 9])

# Prompt tokens
line_adj_json_input_tokens = np.array([nan, nan, nan, 720.0])
line_adj_txt_input_tokens = np.array([nan, nan, nan, 352.0])
line_jpg_input_tokens = np.array([nan, nan, nan, 435.0])
line_json_input_tokens = np.array([nan, nan, nan, 658.0])
line_tokenized_txt_input_tokens = np.array([nan, nan, nan, 323.0])
occupancy_adj_json_input_tokens = np.array([nan, nan, nan, 1182.0])
occupancy_adj_txt_input_tokens = np.array([nan, nan, nan, 464.0])
occupancy_ascii_txt_input_tokens = np.array([nan, nan, nan, 201.0])
occupancy_jpg_input_tokens = np.array([nan, nan, nan, 430.0])
occupancy_json_input_tokens = np.array([nan, nan, nan, 473.0])
occupancy_tokenized_txt_input_tokens = np.array([nan, nan, nan, 752])


# Output tokens
line_adj_json_output_tokens = np.array([nan, nan, nan, 21.0])
line_adj_txt_output_tokens = np.array([nan, nan, nan, 21.0])
line_jpg_output_tokens = np.array([nan, nan, nan, 21.0])
line_json_output_tokens = np.array([nan, nan, nan, 17.0])
line_tokenized_txt_output_tokens = np.array([nan, nan, nan, 29.0])
occupancy_adj_json_output_tokens = np.array([nan, nan, nan, 37.0])
occupancy_adj_txt_output_tokens = np.array([nan, nan, nan, 37.0])
occupancy_ascii_txt_output_tokens = np.array([nan, nan, nan, 53.0])
occupancy_jpg_output_tokens = np.array([nan, nan, nan, 49.0])
occupancy_json_output_tokens = np.array([nan, nan, nan, 53.0])
occupancy_tokenized_txt_output_tokens = np.array([nan, nan, nan, 37])


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
line_adj_json = np.array([0.0, 0.0, 4.0, 4.0])
line_adj_txt = np.array([0.0, 4.0, 0.0, 4.0])
line_jpg = np.array([2.0, 0.0, 2.0, 4.0])
line_json = np.array([4.0, 0.0, 4.0, 0.0])
line_tokenized_txt = np.array([0.0, 4.0, 0.0, 1.0])
occupancy_adj_json = np.array([4.0, 2.0, 6.0, 8.0])
occupancy_adj_txt = np.array([5.0, 2.0, 0.0, 3.0])
occupancy_ascii_txt = np.array([0.0, 8.0, 0.0, 0.0])
occupancy_jpg = np.array([1.0, 0.0, 1.0, 0.0])
occupancy_json = np.array([5.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 4])

# Prompt tokens
line_adj_json_input_tokens = np.array([nan, nan, nan, 712.0])
line_adj_txt_input_tokens = np.array([nan, nan, nan, 344.0])
line_jpg_input_tokens = np.array([nan, nan, nan, 427.0])
line_json_input_tokens = np.array([nan, nan, nan, 650.0])
line_tokenized_txt_input_tokens = np.array([nan, nan, nan, 315.0])
occupancy_adj_json_input_tokens = np.array([nan, nan, nan, 1174.0])
occupancy_adj_txt_input_tokens = np.array([nan, nan, nan, 456.0])
occupancy_ascii_txt_input_tokens = np.array([nan, nan, nan, 193.0])
occupancy_jpg_input_tokens = np.array([nan, nan, nan, 422.0])
occupancy_json_input_tokens = np.array([nan, nan, nan, 465.0])
occupancy_tokenized_txt_input_tokens = np.array([nan, nan, nan, 744])

# Output tokens
line_adj_json_output_tokens = np.array([nan, nan, nan, 7.0])
line_adj_txt_output_tokens = np.array([nan, nan, nan, 7.0])
line_jpg_output_tokens = np.array([nan, nan, nan, 7.0])
line_json_output_tokens = np.array([nan, nan, nan, 7.0])
line_tokenized_txt_output_tokens = np.array([nan, nan, nan, 7.0])
occupancy_adj_json_output_tokens = np.array([nan, nan, nan, 19.0])
occupancy_adj_txt_output_tokens = np.array([nan, nan, nan, 15.0])
occupancy_ascii_txt_output_tokens = np.array([nan, nan, nan, 23.0])
occupancy_jpg_output_tokens = np.array([nan, nan, nan, 49.0])
occupancy_json_output_tokens = np.array([nan, nan, nan, 21.0])
occupancy_tokenized_txt_output_tokens = np.array([nan, nan, nan, 650])

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
line_adj_json = np.array([1.0, 0.0, 1.0, 0.0])
line_adj_txt = np.array([0.0, 0.0, 0.0, 0.0])
line_jpg = np.array([0.0, 0.0, 0.0, 0.0])
line_json = np.array([1.0, 0.0, 0.0, 0.0])
line_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_adj_json = np.array([0.0, 0.0, 1.0, 0.0])
occupancy_adj_txt = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_jpg = np.array([0.0, 0.0, 1.0, 0.0])
occupancy_json = np.array([0.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 0])

# Prompt tokens
line_adj_json_input_tokens = np.array([nan, nan, nan, 836.0])
line_adj_txt_input_tokens = np.array([nan, nan, nan, 468.0])
line_jpg_input_tokens = np.array([nan, nan, nan, 551.0])
line_json_input_tokens = np.array([nan, nan, nan, 774.0])
line_tokenized_txt_input_tokens = np.array([nan, nan, nan, 439.0])
occupancy_adj_json_input_tokens = np.array([nan, nan, nan, 1298.0])
occupancy_adj_txt_input_tokens = np.array([nan, nan, nan, 580.0])
occupancy_ascii_txt_input_tokens = np.array([nan, nan, nan, 317.0])
occupancy_jpg_input_tokens = np.array([nan, nan, nan, 546.0])
occupancy_json_input_tokens = np.array([nan, nan, nan, 589.0])
occupancy_tokenized_txt_input_tokens = np.array([nan, nan, nan, 868])

# Output tokens
line_adj_json_output_tokens = np.array([nan, nan, nan, 15.0])
line_adj_txt_output_tokens = np.array([nan, nan, nan, 11.0])
line_jpg_output_tokens = np.array([nan, nan, nan, 15.0])
line_json_output_tokens = np.array([nan, nan, nan, 19.0])
line_tokenized_txt_output_tokens = np.array([nan, nan, nan, 649.0])
occupancy_adj_json_output_tokens = np.array([nan, nan, nan, 99.0])
occupancy_adj_txt_output_tokens = np.array([nan, nan, nan, 49.0])
occupancy_ascii_txt_output_tokens = np.array([nan, nan, nan, 35.0])
occupancy_jpg_output_tokens = np.array([nan, nan, nan, 23.0])
occupancy_json_output_tokens = np.array([nan, nan, nan, 55.0])
occupancy_tokenized_txt_output_tokens = np.array([nan, nan, nan, 49])

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

# # R - COORDS -  - 1-3 ----------------------------------------------------------------

# line_adj_json = np.array([100.0, 100.0, 100.0])
# line_adj_txt = np.array([100.0, 100.0, 100.0])
# line_jpg = np.array([40.0, 100.0, 100.0])
# line_json = np.array([100.0, 100.0, 100.0])
# line_tokenized_txt = np.array([100.0, 100.0, 100.0])
# occupancy_adj_json = np.array([100.0, 100.0, 100.0])
# occupancy_adj_txt = np.array([100.0, 100.0, 100.0])
# occupancy_ascii_txt = np.array([22.22222222222222, 100.0, 100.0])
# occupancy_jpg = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556])
# occupancy_json = np.array([100.0, 100.0, 100.0])
# occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0])

# Raw Scores
line_adj_json = np.array([5, 5, 5])
line_adj_txt = np.array([5, 5, 5])
line_jpg = np.array([2, 5, 5])
line_json = np.array([5, 5, 5])
line_tokenized_txt = np.array([5, 5, 5])
occupancy_adj_json = np.array([9, 9, 9])
occupancy_adj_txt = np.array([9, 9, 9])
occupancy_ascii_txt = np.array([2, 9, 9])
occupancy_jpg = np.array([1, 2, 5])
occupancy_json = np.array([9, 9, 9])
occupancy_tokenized_txt = np.array([9, 9, 9])

# Prompt tokens

# Output tokens

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

# # R - EGO -  - 1-3 ----------------------------------------------------------------

# line_adj_json = np.array([25.0, 100.0, 100.0])
# line_adj_txt = np.array([25.0, 100.0, 100.0])
# line_jpg = np.array([25.0, 0.0, 50.0])
# line_json = np.array([100.0, 100.0, 100.0])
# line_tokenized_txt = np.array([100.0, 100.0, 100.0])
# occupancy_adj_json = np.array([100.0, 100.0, 100.0])
# occupancy_adj_txt = np.array([100.0, 100.0, 100.0])
# occupancy_ascii_txt = np.array([100.0, 100.0, 100.0])
# occupancy_jpg = np.array([12.5, 0.0, 0.0])
# occupancy_json = np.array([100.0, 100.0, 100.0])
# occupancy_tokenized_txt = np.array([0.0, 100.0, 100.0])


# Raw Scores
line_adj_json = np.array([1, 4, 4])
line_adj_txt = np.array([1, 4, 4])
line_jpg = np.array([1, 0, 2])
line_json = np.array([4, 4, 4])
line_tokenized_txt = np.array([4, 4, 4])
occupancy_adj_json = np.array([8, 8, 8])
occupancy_adj_txt = np.array([8, 8, 8])
occupancy_ascii_txt = np.array([8, 8, 8])
occupancy_jpg = np.array([1, 0, 0])
occupancy_json = np.array([8, 8, 8])
occupancy_tokenized_txt = np.array([0, 8, 8])

# Prompt tokens

# Output tokens

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

line_adj_json = np.array([100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0])
line_jpg = np.array([0.0, 0.0, 100.0])
line_json = np.array([100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([100.0, 100.0, 100.0])
occupancy_jpg = np.array([0.0, 0.0, 0.0])
occupancy_json = np.array([100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0])

# Raw Scores
line_adj_json = np.array([4, 4, 4])
line_adj_txt = np.array([4, 4, 4])
line_jpg = np.array([0, 0, 4])
line_json = np.array([4, 4, 4])
line_tokenized_txt = np.array([4, 4, 4])
occupancy_adj_json = np.array([8, 8, 8])
occupancy_adj_txt = np.array([8, 8, 8])
occupancy_ascii_txt = np.array([8, 8, 8])
occupancy_jpg = np.array([0, 0, 0])
occupancy_json = np.array([8, 8, 8])
occupancy_tokenized_txt = np.array([8, 8, 8])

# Prompt tokens

# Output tokens

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