
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataframe_image as dfi

representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line ascii txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']






# x_axis = np.linspace(1,30,30) # a range from 1 to 30 with 30 points


# -------------------- Reasoning, steps output, dataset 01 ----------------
x_axis = ['2x2', '5x5', '10x10', '15x15', '20x20']
line_adj_json = np.array([100.0, 100.0,  100.0,  69.2982456140351,  22.63157894736842])
line_adj_txt = np.array([0.0,  100.0,  78.57142857142857,  53.50877192982456,  3.1578947368421053])
line_ascii_txt = np.array([100.0,  28.57142857142857,  4.761904761904762,  0.0,  0.0])
line_jpg = np.array([0.0,  28.57142857142857,  2.380952380952381,  0.0,  0.0])
line_json = np.array([100.0,  100.0,  11.904761904761903,  21.052631578947366,  17.36842105263158])
line_tokenized_txt = np.array([100.0,  100.0,  100.0,  32.45614035087719,  16.842105263157894])
occupancy_adj_json = np.array([100.0,  100.0,  100.0,  35.96491228070175,  35.78947368421053])
occupancy_adj_txt = np.array([100.0,  100.0,  100.0,  64.03508771929825,  12.631578947368421])
occupancy_ascii_txt = np.array([110.0,  14.285714285714285,  7.142857142857142,  3.9473684210526314,  3.1578947368421053])
occupancy_jpg = np.array([25.0,  0.0,  0.0,  0.8771929824561403, 0.2631578947368421])
occupancy_json = np.array([0.0,  100.0,  19.047619047619047,  5.263157894736842,  3.684210526315789])
occupancy_tokenized_txt = np.array([100.0,  100.0,  100.0,  31.57894736842105,  5.7894736842105265])

# normalization_vector = np.array([4, 25, 100, 225, 400])


# normalized_line_adj_json = line_adj_json/normalization_vector
# normalized_line_adj_txt = line_adj_txt/normalization_vector
# normalized_line_ascii_txt = line_ascii_txt/normalization_vector
# normalized_line_jpg = line_jpg/normalization_vector
# normalized_line_json = line_json/normalization_vector
# normalized_line_tokenized_txt = line_tokenized_txt/normalization_vector
# normalized_occupancy_adj_json = occupancy_adj_json/normalization_vector
# normalized_occupancy_adj_txt = occupancy_adj_txt/normalization_vector
# normalized_occupancy_ascii_txt = occupancy_ascii_txt/normalization_vector
# normalized_occupancy_jpg = occupancy_jpg/normalization_vector
# normalized_occupancy_json = occupancy_json/normalization_vector
# normalized_occupancy_tokenized_txt = occupancy_tokenized_txt/normalization_vector

# #  Create a plot
# # Comment out when you want only final accuracy plot 
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

# plt.title('Accuracy Normalized for Complexity of Gemini 2.5 Pro, Steps Output')
# plt.xlabel('Maze Complexity')
# plt.ylabel('Normalized Accuracy (%/cell)')

# plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# plt.grid(linestyle = ':', linewidth = '0.5')
# plt.show()




# # -------------------- non-reasoning, steps output, dataset 01. ----------------
x_axis = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12']




line_adj_json = np.array([0.0, 100.0, 37.5, 7.142857142857142, 0.0, 0.0, 20.0, 0.0, 4.761904761904762, 0.0, np.nan])
line_adj_txt = np.array([0.0, 100.0, 37.5, 21.428571428571427, 0.0, 0.0, 20.0, 0.0, 11.904761904761903, 0.0, 0.0])
line_ascii_txt = np.array([0.0, 50.0, 25.0, 7.142857142857142, 0.0, 0.0, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])
line_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json = np.array([100.0, 25.0, 12.5, 28.57142857142857, 25.0, 16.666666666666664, 10.0, 2.0, 7.142857142857142, 1.6129032258064515, 3.3333333333333335])
line_tokenized_txt = np.array([0.0, 100.0, 37.5, 7.142857142857142, 0.0, 0.0, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])
occupancy_adj_json = np.array([0.0, 110.00000000000001, 31.25, 7.142857142857142, 0.0, np.nan, 15.0, 0.0, 9.523809523809524, 0.0, 0.8333333333333334])
occupancy_adj_txt = np.array([0.0, 110.00000000000001, 37.5, 10.714285714285714, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 25.0, 14.285714285714285, 0.0, 0.0, 20.0, 0.0, 5.952380952380952, 0.8064516129032258, 0.0])
occupancy_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json = np.array([0.0, 75.0, 37.5, 14.285714285714285, 0.0, 0.0, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])
occupancy_tokenized_txt = np.array([0.0, 0.0, 25.0, 7.142857142857142, 16.666666666666664, 11.11111111111111, 15.0, 0.0, 4.761904761904762, 0.0, 0.0])


normalization_vector = np.array([4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144])

normalized_line_adj_json = line_adj_json/normalization_vector
normalized_line_adj_txt = line_adj_txt/normalization_vector
normalized_line_ascii_txt = line_ascii_txt/normalization_vector
normalized_line_jpg = line_jpg/normalization_vector
normalized_line_json = line_json/normalization_vector
normalized_line_tokenized_txt = line_tokenized_txt/normalization_vector
normalized_occupancy_adj_json = occupancy_adj_json/normalization_vector
normalized_occupancy_adj_txt = occupancy_adj_txt/normalization_vector
normalized_occupancy_ascii_txt = occupancy_ascii_txt/normalization_vector
normalized_occupancy_jpg = occupancy_jpg/normalization_vector
normalized_occupancy_json = occupancy_json/normalization_vector
normalized_occupancy_tokenized_txt = occupancy_tokenized_txt/normalization_vector


# Set up complexities for table
complexities = [f"Complexity {x_axis[i]}" for i in range(11)]

data_stacked = np.vstack([line_jpg, line_json, line_adj_json, line_adj_txt, line_ascii_txt, line_tokenized_txt,
                          occupancy_jpg, occupancy_json, occupancy_adj_json, occupancy_adj_txt, occupancy_ascii_txt, occupancy_tokenized_txt])

table = pd.DataFrame(
    data=data_stacked,
    index=representations,        # row labels
    columns=complexities          # column labels
)
# print(table.round(3))
# table.plot(kind="bar", figsize=(10,6))

# Create and save table image
table_img = table.style.set_caption("Accuracy of Representations at Each Complexity").format(precision=3)
dfi.export(table_img, "table_accuracy_NR_Dataset01.png")


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

# plt.title('Accuracy Normalized for Complexity of Gemini 2.5 Flash-Lite, Steps Output')
# plt.xlabel('Maze Complexity')
# plt.ylabel('Normalized Accuracy (%/cell)')

# plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# plt.grid(linestyle = ':', linewidth = '0.5')
# plt.show()