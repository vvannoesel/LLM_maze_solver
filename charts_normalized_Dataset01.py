
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataframe_image as dfi

representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line ascii txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']



# # # -------------------- Reasoning, steps output, dataset 01 ----------------
# x_axis = ['2x2', '5x5', '10x10', '15x15', '20x20']
# line_adj_json = np.array([100.0, 100.0,  100.0,  69.2982456140351,  22.63157894736842])
# line_adj_txt = np.array([0.0,  100.0,  78.57142857142857,  53.50877192982456,  3.1578947368421053])
# line_ascii_txt = np.array([100.0,  28.57142857142857,  4.761904761904762,  0.0,  0.0])
# line_jpg = np.array([0.0,  28.57142857142857,  2.380952380952381,  0.0,  0.0])
# line_json = np.array([100.0,  100.0,  11.904761904761903,  21.052631578947366,  17.36842105263158])
# line_tokenized_txt = np.array([100.0,  100.0,  100.0,  32.45614035087719,  16.842105263157894])
# occupancy_adj_json = np.array([100.0,  100.0,  100.0,  35.96491228070175,  35.78947368421053])
# occupancy_adj_txt = np.array([100.0,  100.0,  100.0,  64.03508771929825,  12.631578947368421])
# occupancy_ascii_txt = np.array([110.0,  14.285714285714285,  7.142857142857142,  3.9473684210526314,  3.1578947368421053])
# occupancy_jpg = np.array([25.0,  0.0,  0.0,  0.8771929824561403, 0.2631578947368421])
# occupancy_json = np.array([0.0,  100.0,  19.047619047619047,  5.263157894736842,  3.684210526315789])
# occupancy_tokenized_txt = np.array([100.0,  100.0,  100.0,  31.57894736842105,  5.7894736842105265])

# normalization_vector = np.array([4, 25, 100, 225, 400])
# normalization_vector_line = np.array([2, 14, 42,  114, 190]) # number of steps in ground truth solution per complexity
# normalization_vector_occ = np.array([4, 28, 84, 228, 380]) # number of steps in ground truth solution per complexity


# normalized_line_adj_json = line_adj_json*normalization_vector_line/100
# normalized_line_adj_txt = line_adj_txt*normalization_vector_line/100
# normalized_line_ascii_txt = line_ascii_txt*normalization_vector_line/100
# normalized_line_jpg = line_jpg*normalization_vector_line/100
# normalized_line_json = line_json*normalization_vector_line/100
# normalized_line_tokenized_txt = line_tokenized_txt*normalization_vector_line/100
# normalized_occupancy_adj_json = occupancy_adj_json*normalization_vector_occ/100
# normalized_occupancy_adj_txt = occupancy_adj_txt*normalization_vector_occ/100
# normalized_occupancy_ascii_txt = occupancy_ascii_txt*normalization_vector_occ/100
# normalized_occupancy_jpg = occupancy_jpg*normalization_vector_occ/100
# normalized_occupancy_json = occupancy_json*normalization_vector_occ/100
# normalized_occupancy_tokenized_txt = occupancy_tokenized_txt*normalization_vector_occ/100

# print('raw line ascii:', normalized_line_ascii_txt)
# print('raw occ ascii:', normalized_occupancy_ascii_txt)

# # Set up complexities for table
# complexities = [f"Complexity {x_axis[i]}" for i in range(5)]

# data_stacked = np.vstack([normalized_line_jpg, normalized_line_json, normalized_line_adj_json, normalized_line_adj_txt, normalized_line_ascii_txt, normalized_line_tokenized_txt,
#                           normalized_occupancy_jpg, normalized_occupancy_json, normalized_occupancy_adj_json, normalized_occupancy_adj_txt, normalized_occupancy_ascii_txt, normalized_occupancy_tokenized_txt])

# table = pd.DataFrame(
#     data=data_stacked,
#     index=representations,        # row labels
#     columns=complexities          # column labels
# )
# print(table.round(3))
# table.plot(kind="bar", figsize=(10,6))

# # Create and save table image
# table_img = table.style.set_caption("Accuracy of Representations at Each Complexity, steps output").format(precision=3)
# dfi.export(table_img, "table_accuracy_R_Dataset01.png")

# # Create separate graphs for line and occ with aliged x-axes
# x_axis_line = ['2x2', '5x5', '10x10', '15x15', '20x20']
# x_axis_occ = ['5x5', '11x11','21x21', '31x31', '41x41']

# line_graph = [('Line Adjacency Json', normalized_line_adj_json), 
#               ('Line Adjacency Txt', normalized_line_adj_txt), 
#               ('Line ASCII', normalized_line_ascii_txt), 
#               ('Line JPG', normalized_line_jpg), 
#               ('Line JSON', normalized_line_json), 
#               ('Line Tokenized', normalized_line_tokenized_txt)]
# occ_graph = [('Occupancy Adjacency Json', normalized_occupancy_adj_json), 
#              ('Occupancy Adjacency Txt', normalized_occupancy_adj_txt), 
#              ('Occupancy ASCII', normalized_occupancy_ascii_txt), 
#              ('Occupancy JPG', normalized_occupancy_jpg), 
#              ('Occupancy JSON', normalized_occupancy_json), 
#              ('Occupancy Tokenized', normalized_occupancy_tokenized_txt)]

# # Create stacked subplots wiht vertical alignment of x-axis
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1,
#     figsize=(10, 8),
#     sharex=False  # align the x-axes perfectly
# )

# # Define the complexities (shared x positions)
# x = np.arange(5)

# # top plot
# for label, data in line_graph:
#     ax1.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)

# ax1.set_ylabel('Number of correct steps')
# ax1.set_title('Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Pro, Steps Output')
# ax1.set_xticks(x)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel('Maze Complexity')
# ax1.legend(loc='upper left', fontsize=8)
# ax1.grid(True, linestyle='--', alpha=0.4)

# # bottom plot
# for label, data in occ_graph:
#     ax2.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)
# ax2.set_title('Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Pro, Steps Output')
# ax2.set_ylabel('Number of correct steps')
# ax2.set_xlabel('Maze Complexity')
# ax2.set_xticks(x)
# ax2.set_xticklabels(x_axis_occ)
# ax2.legend(loc='upper left', fontsize=8)
# ax2.grid(True, linestyle='--', alpha=0.4)

# plt.tight_layout(h_pad=2.0)
# plt.show()


#  Create a plot
# Comment out when you want only final accuracy plot 
# plt.plot(x_axis, normalized_line_jpg, 'g:', label = 'line jpg')
# plt.plot(x_axis, normalized_line_json, 'b:o', label = 'line json')
# plt.plot(x_axis, normalized_line_adj_json, 'c:o', label = 'line adjacency json')
# plt.plot(x_axis, normalized_line_adj_txt, 'm:o', label = 'line adjacency txt')
# plt.plot(x_axis, normalized_line_ascii_txt, 'y:o', label = 'line ASCII')
# plt.plot(x_axis, normalized_line_tokenized_txt, 'k:o', label = 'line tokenized')
# plt.plot(x_axis, normalized_occupancy_jpg, 'g-->', label = 'occupancy jpg')
# plt.plot(x_axis, normalized_occupancy_json, 'b-->', label = 'occupancy json')
# plt.plot(x_axis, normalized_occupancy_adj_json, 'c-->', label = 'occupancy adjacency json')
# plt.plot(x_axis, normalized_occupancy_adj_txt, 'm-->', label = 'occupancy adjacency txt')
# plt.plot(x_axis, normalized_occupancy_ascii_txt, 'y-->', label = 'occupancy ASCII')
# plt.plot(x_axis, normalized_occupancy_tokenized_txt, 'k-->', label = 'occupancy tokenized')

# plt.title('Number of Correct Steps per Complexity,  Gemini 2.5 Pro, Steps Output')
# plt.xlabel('Maze Complexity')
# plt.ylabel('Number of Correct Steps')

# plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# plt.grid(linestyle = ':', linewidth = '0.5')
# plt.show()




# # -------------------- non-reasoning, steps output, dataset 01. ----------------
# x_axis = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12']

# line_adj_json = np.array([0.0, 100.0, 37.5, 7.142857142857142, 0.0, 0.0, 20.0, 0.0, 4.761904761904762, 0.0, np.nan])
# line_adj_txt = np.array([0.0, 100.0, 37.5, 21.428571428571427, 0.0, 0.0, 20.0, 0.0, 11.904761904761903, 0.0, 0.0])
# line_ascii_txt = np.array([0.0, 50.0, 25.0, 7.142857142857142, 0.0, 0.0, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])
# line_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# line_json = np.array([100.0, 25.0, 12.5, 28.57142857142857, 25.0, 16.666666666666664, 10.0, 2.0, 7.142857142857142, 1.6129032258064515, 3.3333333333333335])
# line_tokenized_txt = np.array([0.0, 100.0, 37.5, 7.142857142857142, 0.0, 0.0, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])
# occupancy_adj_json = np.array([0.0, 110.00000000000001, 31.25, 7.142857142857142, 0.0, np.nan, 15.0, 0.0, 9.523809523809524, 0.0, 0.8333333333333334])
# occupancy_adj_txt = np.array([0.0, 110.00000000000001, 37.5, 10.714285714285714, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0])
# occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 25.0, 14.285714285714285, 0.0, 0.0, 20.0, 0.0, 5.952380952380952, 0.8064516129032258, 0.0])
# occupancy_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# occupancy_json = np.array([0.0, 75.0, 37.5, 14.285714285714285, 0.0, 0.0, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])
# occupancy_tokenized_txt = np.array([0.0, 0.0, 25.0, 7.142857142857142, 16.666666666666664, 11.11111111111111, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])


# # # normalization_vector = np.array([4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) # number of cells per complexity
# normalization_vector_line = np.array([2, 4, 8, 14, 12, 18, 20, 50, 42, 62, 60 ]) # number of steps in ground truth solution per complexity
# normalization_vector_occ = np.array([4, 8, 16, 28, 24, 36, 40, 100, 84, 124, 120]) # number of steps in ground truth solution per complexity


# normalized_line_adj_json = line_adj_json*normalization_vector_line/100
# normalized_line_adj_txt = line_adj_txt*normalization_vector_line/100
# normalized_line_ascii_txt = line_ascii_txt*normalization_vector_line/100
# normalized_line_jpg = line_jpg*normalization_vector_line/100
# normalized_line_json = line_json*normalization_vector_line/100
# normalized_line_tokenized_txt = line_tokenized_txt*normalization_vector_line/100
# normalized_occupancy_adj_json = occupancy_adj_json*normalization_vector_occ/100
# normalized_occupancy_adj_txt = occupancy_adj_txt*normalization_vector_occ/100
# normalized_occupancy_ascii_txt = occupancy_ascii_txt*normalization_vector_occ/100
# normalized_occupancy_jpg = occupancy_jpg*normalization_vector_occ/100
# normalized_occupancy_json = occupancy_json*normalization_vector_occ/100
# normalized_occupancy_tokenized_txt = occupancy_tokenized_txt*normalization_vector_occ/100

# print('json line', normalized_line_json)

# # Set up complexities for table
# # complexities = [f"Complexity {x_axis[i]}" for i in range(11)]

# # data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt, line_ascii_txt, line_tokenized_txt,
#                         #   occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])


# # data_stacked = np.vstack([normalized_line_jpg, normalized_line_json, normalized_line_adj_json, normalized_line_adj_txt, normalized_line_ascii_txt, normalized_line_tokenized_txt,
# #                           normalized_occupancy_jpg, normalized_occupancy_json, normalized_occupancy_adj_json, normalized_occupancy_adj_txt, normalized_occupancy_ascii_txt, normalized_occupancy_tokenized_txt])

# # table = pd.DataFrame(
# #     data=data_stacked,
# #     index=representations,        # row labels
# #     columns=complexities          # column labels
# # )
# # print(table.round(3))
# # table.plot(kind="bar", figsize=(10,6))

# # # # # Create and save table image
# # # # table_img = table.style.set_caption("Accuracy of Representations at Each Complexity, steps output").format(precision=3)
# # # # dfi.export(table_img, "table_accuracy_NR_Dataset01.png")

# # Create separate graphs for line and occ with aliged x-axes
# x_axis_line = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12']
# x_axis_occ = ['5x5', '7x7', '9x9', '11x11', '13x13', '15x15', '17x17', '19x19', '21x21', '23x23', '25x25']

# line_graph = [('Line Adjacency Json', normalized_line_adj_json), 
#               ('Line Adjacency Txt', normalized_line_adj_txt), 
#               ('Line ASCII', normalized_line_ascii_txt), 
#               ('Line JPG', normalized_line_jpg),
#               ('Line JSON', normalized_line_json),
#               ('Line Tokenized', normalized_line_tokenized_txt)]
# occ_graph = [('Occupancy Adjacency Json', normalized_occupancy_adj_json), 
#              ('Occupancy Adjacency Txt', normalized_occupancy_adj_txt), 
#              ('Occupancy ASCII', normalized_occupancy_ascii_txt), 
#             ('Occupancy JPG', normalized_occupancy_jpg),
#              ('Occupancy JSON', normalized_occupancy_json), 
#              ('Occupancy Tokenized', normalized_occupancy_tokenized_txt)]

# # line_graph = [('Line JSON', normalized_line_json)]
# # occ_graph = [
# #              ('Occupancy JSON', normalized_occupancy_json)]

# # Create stacked subplots wiht vertical alignment of x-axis
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1,
#     figsize=(10, 8),
#     sharex=False  # align the x-axes perfectly
# )

# # Define the complexities (shared x positions)
# x = np.arange(11)

# # top plot
# for label, data in line_graph:
#     ax1.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)

# ax1.set_ylabel('Number of correct steps')
# ax1.set_title('Number of Correct Steps per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Steps Output')
# ax1.set_xticks(x)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel('Maze Complexity')
# ax1.legend(loc='upper right', fontsize=8)
# ax1.grid(True, linestyle='--', alpha=0.4)

# # bottom plot
# for label, data in occ_graph:
#     ax2.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)
# ax2.set_title('Number of Correct Steps per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Steps Output')
# ax2.set_ylabel('Number of correct steps')
# ax2.set_xlabel('Maze Complexity')
# ax2.set_xticks(x)
# ax2.set_xticklabels(x_axis_occ)
# ax2.legend(loc='upper right', fontsize=8)
# ax2.grid(True, linestyle='--', alpha=0.4)

# plt.tight_layout(h_pad=2.0)
# plt.show()

# #  Create a single plot
# # Comment out when you want only final accuracy plot 
# # plt.plot(x_axis, normalized_line_jpg, 'g:', label = 'line jpg')
# # plt.plot(x_axis, normalized_line_json, 'b:o', label = 'line json')
# # plt.plot(x_axis, normalized_line_adj_json, 'c:o', label = 'line adjacency json')
# # plt.plot(x_axis, normalized_line_adj_txt, 'm:o', label = 'line adjacency txt')
# # plt.plot(x_axis, normalized_line_ascii_txt, 'y:o', label = 'line ASCII')
# # plt.plot(x_axis, normalized_line_tokenized_txt, 'k:o', label = 'line tokenized')
# # plt.plot(x_axis, normalized_occupancy_jpg, 'g-->', label = 'occupancy jpg')
# # plt.plot(x_axis, normalized_occupancy_json, 'b-->', label = 'occupancy json')
# # plt.plot(x_axis, normalized_occupancy_adj_json, 'c-->', label = 'occupancy adjacency json')
# # plt.plot(x_axis, normalized_occupancy_adj_txt, 'm-->', label = 'occupancy adjacency txt')
# # plt.plot(x_axis, normalized_occupancy_ascii_txt, 'y-->', label = 'occupancy ASCII')
# # plt.plot(x_axis, normalized_occupancy_tokenized_txt, 'k-->', label = 'occupancy tokenized')

# # plt.title('Number of Correct Steps per Complexity, Gemini 2.5 Flash-Lite, Steps Output')
# # plt.xlabel('Maze Complexity')
# # plt.ylabel('Number of Correct Steps')

# # plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# # plt.grid(linestyle = ':', linewidth = '0.5')
# # plt.show()





# # -------------------- non-reasoning, coordinate output, dataset 01. ----------------
x_axis = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12','13x13', '14x14', '15x15']

line_jpg = np.array([66.67, 0, 0, 0, 7.69, 0, 4.76, 3.92, 2.33, 0, 8.2, 3.37, 0, 0.87 ])
line_json = np.array([100, 20, 11.11, 6.67, 15.38, 10.53, 4.76, 3.92, 2.33, 3.17, 3.28, 3.37, 0.9, 5.22])
line_adj_json = np.array([100, 100, 100, 100, 100, 78.95, 76.19, 11.76, 46.51, 15.87, 9.84, 24.72, 18.92, 26.09])
line_adj_txt = np.array([100, 100, 100, 100, 100, 78.95, 66.67, 11.76, 2.33, 19.05, 44.26, 7.87, 10.81, 8.7])
line_ascii = np.array([33.33, 80, 11.11, 13.33, 15.38, 10.53, 14.29, 3.92, 6.98, 1.59, 4.92, 1.12, 0.9, 0.87])
line_tokenized = np.array([100, 20, 11.11, 0, 30.77, 21.05, 23.81, 1.96, 2.33, 3.17, 6.56, 3.37, 0.9, 1.74])
occupancy_jpg = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
occupancy_json = np.array([20, 100, 100, 51.72, 4, 2.7, 21.95, 0.99, 8.24, 2.4, 0.83, 0.56, 4.07, 0.44])
occupancy_adj_json = np.array([100, 100, 100, 93.1, 100, 100, 90.24, 70.3, 12.94, 15.2, 23.97, 63.84, 12.22, 7.86])
occupancy_adj_txt = np.array([100, 100, 100, 100, 100, 94.59, 100, 70.3, 22.35, 7.2, 23.97, 5.08, 10.41, 8.3])
occupancy_ascii = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
occupancy_tokenized = np.array([80, 77.78, 52.94, 17.24, 4, 2.7, 17.07, 0.99, 10.59, 0.8, 0.83, 0.56, 1.36, 0.44])



# # normalization_vector = np.array([4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) # number of cells per complexity
normalization_vector_line = np.array([3, 5, 9, 15, 13, 19, 21, 51, 43, 63, 61, 89, 111, 115]) # number of steps in ground truth solution per complexity
normalization_vector_occ = np.array([5, 9, 17, 29, 25, 37, 41, 101, 85, 125, 121, 177, 121, 229]) # number of steps in ground truth solution per complexity


normalized_line_adj_json = line_adj_json*normalization_vector_line/100
normalized_line_adj_txt = line_adj_txt*normalization_vector_line/100
normalized_line_ascii_txt = line_ascii*normalization_vector_line/100
normalized_line_jpg = line_jpg*normalization_vector_line/100
normalized_line_json = line_json*normalization_vector_line/100
normalized_line_tokenized_txt = line_tokenized*normalization_vector_line/100
normalized_occupancy_adj_json = occupancy_adj_json*normalization_vector_occ/100
normalized_occupancy_adj_txt = occupancy_adj_txt*normalization_vector_occ/100
normalized_occupancy_ascii_txt = occupancy_ascii*normalization_vector_occ/100
normalized_occupancy_jpg = occupancy_jpg*normalization_vector_occ/100
normalized_occupancy_json = occupancy_json*normalization_vector_occ/100
normalized_occupancy_tokenized_txt = occupancy_tokenized*normalization_vector_occ/100


# Set up complexities for table
# complexities = [f"Complexity {x_axis[i]}" for i in range(11)]

# data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt, line_ascii_txt, line_tokenized_txt,
                        #   occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])


# data_stacked = np.vstack([normalized_line_jpg, normalized_line_json, normalized_line_adj_json, normalized_line_adj_txt, normalized_line_ascii_txt, normalized_line_tokenized_txt,
#                           normalized_occupancy_jpg, normalized_occupancy_json, normalized_occupancy_adj_json, normalized_occupancy_adj_txt, normalized_occupancy_ascii_txt, normalized_occupancy_tokenized_txt])

# table = pd.DataFrame(
#     data=data_stacked,
#     index=representations,        # row labels
#     columns=complexities          # column labels
# )
# print(table.round(3))
# table.plot(kind="bar", figsize=(10,6))

# # # # Create and save table image
# # # table_img = table.style.set_caption("Accuracy of Representations at Each Complexity, steps output").format(precision=3)
# # # dfi.export(table_img, "table_accuracy_NR_Dataset01.png")

# # Create separate graphs for line and occ with aliged x-axes
# x_axis_line = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12','13x13', '14x14', '15x15']
# x_axis_occ = ['5x5', '7x7', '9x9', '11x11', '13x13', '15x15', '17x17', '19x19', '21x21', '23x23', '25x25', '27x27', '29x29', '31x31']

# line_graph = [('Line Adjacency Json', normalized_line_adj_json), 
#               ('Line Adjacency Txt', normalized_line_adj_txt), 
#               ('Line ASCII', normalized_line_ascii_txt), 
#               ('Line JPG', normalized_line_jpg),
#               ('Line JSON', normalized_line_json),
#               ('Line Tokenized', normalized_line_tokenized_txt), 
#               ('100%', normalization_vector_line)]
# occ_graph = [('Occupancy Adjacency Json', normalized_occupancy_adj_json), 
#              ('Occupancy Adjacency Txt', normalized_occupancy_adj_txt), 
#              ('Occupancy ASCII', normalized_occupancy_ascii_txt), 
#             ('Occupancy JPG', normalized_occupancy_jpg),
#              ('Occupancy JSON', normalized_occupancy_json), 
#              ('Occupancy Tokenized', normalized_occupancy_tokenized_txt), 
#              ('100%', normalization_vector_occ)]


# # Create stacked subplots wiht vertical alignment of x-axis
# fig, (ax1, ax2) = plt.subplots(
#     nrows=2, ncols=1,
#     figsize=(10, 8),
#     sharex=False  # align the x-axes perfectly
# )

# # Define the complexities (shared x positions)
# x = np.arange(14)

# # top plot
# for label, data in line_graph:
#     ax1.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)

# ax1.set_ylabel('Number of correct coordinates')
# ax1.set_title('Number of Correct Coordinates per Complexity, Line Maze, Gemini 2.5 Flash-Lite, Coordinates Output')
# ax1.set_xticks(x)
# ax1.set_xticklabels(x_axis_line)
# ax1.set_xlabel('Maze Complexity')
# ax1.legend(loc='upper left', fontsize=8)
# ax1.grid(True, linestyle='--', alpha=0.4)

# # bottom plot
# for label, data in occ_graph:
#     ax2.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)
# ax2.set_title('Number of Correct Coordinates per Complexity, Occupancy Maze, Gemini 2.5 Flash-Lite, Coordinates Output')
# ax2.set_ylabel('Number of correct coordinates')
# ax2.set_xlabel('Maze Complexity')
# ax2.set_xticks(x)
# ax2.set_xticklabels(x_axis_occ)
# ax2.legend(loc='upper left', fontsize=8)
# ax2.grid(True, linestyle='--', alpha=0.4)

# plt.tight_layout(h_pad=2.0)
# plt.show()








#----------- Trying a new kind of plot ----------------------
delta_size_line = np.array([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) # number of cells increase from one size to the next
size_increments_percentage_line = np.array([125, 700/9, 900/16, 1100/25, 1300/36, 1500/49, 1700/64, 1900/81, 2100/100, 2300/121, 2500/144, 2700/169, 2900/196]) # percentage increase of cells from one size to the next 

delta_size_occ = np.array([24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]) # number of cells increase from one size to the next
size_increments_percentage_occ = np.array([2400/25, 3200/49, 4000/81, 4800/121, 5600/169, 6400/225, 7200/289, 8000/361, 8800/441, 9600/529, 10400/625, 11200/729, 12000/841]) # percentage increase of cells from one size to the next


delta_performance_line_adj_json = np.diff(line_adj_json)
delta_performance_line_adj_txt = np.diff(line_adj_txt)
delta_performance_line_json = np.diff(line_json)
delta_performance_line_jpg = np.diff(line_jpg)
delta_performance_line_ascii = np.diff(line_ascii)
delta_performance_line_tokenized = np.diff(line_tokenized)
delta_performance_occ_adj_json = np.diff(occupancy_adj_json)
delta_performance_occ_adj_txt = np.diff(occupancy_adj_txt)
delta_performance_occ_json = np.diff(occupancy_json)
delta_performance_occ_jpg = np.diff(occupancy_jpg)
delta_performance_occ_ascii = np.diff(occupancy_ascii)
delta_performance_occ_tokenized = np.diff(occupancy_tokenized)


line_graph = [('Line Adjacency Json', delta_performance_line_adj_json), 
              ('Line Adjacency Txt', delta_performance_line_adj_txt), 
              ('Line ASCII', delta_performance_line_ascii), 
              ('Line JPG', delta_performance_line_jpg),
              ('Line JSON', delta_performance_line_json),
              ('Line Tokenized', delta_performance_line_tokenized)]
occ_graph = [('Occupancy Adjacency Json', delta_performance_occ_adj_json), 
             ('Occupancy Adjacency Txt', delta_performance_occ_adj_txt), 
             ('Occupancy ASCII', delta_performance_occ_ascii), 
            ('Occupancy JPG', delta_performance_occ_jpg),
             ('Occupancy JSON', delta_performance_occ_json), 
             ('Occupancy Tokenized', delta_performance_occ_tokenized)]




# plt.title('Change of Performance for Each Complexity Increase of Gemini 2.5 Flash Lite, Coordinate Output')
# plt.xlabel('number of added cells per complexity')
# plt.ylabel('change in performance per complexity increase (%)')





# Create stacked subplots wiht vertical alignment of x-axis
fig, (ax1, ax2) = plt.subplots(
    nrows=2, ncols=1,
    figsize=(10, 8),
    sharex=False  # align the x-axes perfectly
)

# Define the complexities (shared x positions)
x = np.arange(13)

# top plot
for label, data in line_graph:
    ax1.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)

ax1.set_ylabel('change in performance per complexity increase (%)')
ax1.set_title('Change of Performance for Each Relative Complexity Increase, Line Maze, Gemini 2.5 Flash-Lite, Coordinates Output')
ax1.set_xticks(x)
ax1.set_xticklabels(delta_size_line)
ax1.set_xlabel('number of added cells per complexity')
ax1.legend(loc='upper left', fontsize=8)
ax1.grid(True, linestyle='--', alpha=0.4)

# bottom plot
for label, data in occ_graph:
    ax2.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)
ax2.set_title('Change of Performance for Each Relative Complexity Increase, Occupancy Maze, Gemini 2.5 Flash Lite, Coordinate Output')
ax2.set_ylabel('change in performance per complexity increase (%)')
ax2.set_xlabel('number of added cells per complexity')
ax2.set_xticks(x)
ax2.set_xticklabels(delta_size_occ)
ax2.legend(loc='upper left', fontsize=8)
ax2.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout(h_pad=2.0)
plt.show()



# plt.title('Change of Performance for Each Relative Complexity Increase of Gemini 2.5 Flash Lite, Coordinate Output')
# plt.xlabel('relative increase of cells per complexity (%)')
# plt.ylabel('change in performance per complexity increase (%)')

# plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# plt.grid(linestyle = ':', linewidth = '0.5')
# plt.show()