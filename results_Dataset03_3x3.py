import numpy as np
import pandas as pd
import dataframe_image as dfi
representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']


# NR - COORDS - 1-3 ----------------------------------------------------------------

# line_adj_json = np.array([100.0, 100.0, 100.0])
# line_adj_txt = np.array([100.0, 100.0, 100.0])
# line_jpg = np.array([40.0, 20.0, 40.0])
# line_json = np.array([100.0, 20.0, 60.0])
# line_tokenized_txt = np.array([20.0, 0.0, 0.0])
# occupancy_adj_json = np.array([100.0, 100.0, 100.0])
# occupancy_adj_txt = np.array([100.0, 100.0, 100.0])
# occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0])
# occupancy_jpg = np.array([0.0, 0.0, 55.55555555555556])
# occupancy_json = np.array([100.0, 110.00000000000001, 100.0])
# occupancy_tokenized_txt = np.array([11.11111111111111, 110.00000000000001, 100.0])

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Flash Lite, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_NR_coords.png")


# NR - ALLO - 1-3 ----------------------------------------------------------------

# line_adj_json = np.array([0.0, 0.0, 100.0])
# line_adj_txt = np.array([0.0, 100.0, 0.0])
# line_jpg = np.array([50.0, 0.0, 50.0])
# line_json = np.array([100.0, 0.0, 100.0])
# line_tokenized_txt = np.array([0.0, 100.0, 0.0])
# occupancy_adj_json = np.array([50, 25.0, 75.0])
# occupancy_adj_txt = np.array([62.5, 25.0, 0.0])
# occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0])
# occupancy_jpg = np.array([12.5, 0.0, 12.5])
# occupancy_json = np.array([62.5, 0.0, 0.0])
# occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0])

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

# NR - EGO - 1-3 ----------------------------------------------------------------
# line_adj_json = np.array([25.0, 0.0, 25.0])
# line_adj_txt = np.array([0.0, 0.0, 0.0])
# line_jpg = np.array([0.0, 0.0, 0.0])
# line_json = np.array([25.0, 0.0, 0.0])
# line_tokenized_txt = np.array([0.0, 0.0, 0.0])
# occupancy_adj_json = np.array([0.0, 0.0, 12.5])
# occupancy_adj_txt = np.array([0.0, 0.0, 0.0])
# occupancy_ascii_txt = np.array([0.0, 0.0, 0.0])
# occupancy_jpg = np.array([0.0, 0.0, 12.5])
# occupancy_json = np.array([0.0, 0.0, 0.0])
# occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0])

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