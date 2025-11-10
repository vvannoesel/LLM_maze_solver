"""
@author: valer, 7 October 21:22:04 2025
This script generates a maze, prompts a large language model (LLM) to solve it
using various maze representations, compares the LLM's solutions to the
correct solution, and saves the results in a markdown file.
DOES NOT INCLUDE INTERNAL THOUGHTS. USE ONLY FOR NON-REASONING LLMS.
Updated to new SDK call structure of call_llm. 
"""
import matplotlib.pyplot as plt
import numpy as np
# list = np.array([(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11), (2, 11), (1, 11), (1, 12), (1, 13), (2, 13), (3, 13), (3, 14), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (7, 16), (7, 17), (6, 17), (5, 17), (4, 17), (3, 17), (2, 17), (1, 17), (1, 18), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (5, 20), (5, 21), (5, 22), (5, 23), (6, 23), (7, 23), (8, 23), (9, 23), (9, 24), (9, 25), (8, 25), (7, 25), (7, 26), (7, 27), (7, 28), (7, 29), (8, 29), (9, 29), (10, 29), (11, 29), (11, 28), (11, 27), (11, 26), (11, 25), (11, 24), (11, 23), (11, 22), (11, 21), (12, 21), (13, 21), (13, 20), (13, 19), (13, 18), (13, 17), (14, 17), (15, 17), (16, 17), (17, 17), (17, 16), (17, 15), (18, 15), (19, 15), (19, 14), (19, 13), (19, 12), (19, 11), (18, 11), (17, 11), (17, 10), (17, 9), (16, 9), (15, 9), (15, 10), (15, 11), (14, 11), (13, 11), (12, 11), (11, 11), (11, 10), (11, 9), (12, 9), (13, 9), (13, 8), (13, 7), (14, 7), (15, 7), (15, 6), (15, 5), (15, 4), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (19, 4), (19, 5), (20, 5), (21, 5), (21, 4), (21, 3), (21, 2), (21, 1), (22, 1), (23, 1), (23, 2), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (24, 7), (25, 7), (25, 6), (25, 5), (25, 4), (25, 3), (26, 3), (27, 3), (27, 4), (27, 5), (28, 5), (29, 5), (29, 6), (29, 7), (28, 7), (27, 7), (27, 8), (27, 9), (26, 9), (25, 9), (25, 10), (25, 11), (24, 11), (23, 11), (23, 12), (23, 13), (22, 13), (21, 13), (21, 14), (21, 15), (22, 15), (23, 15), (23, 16), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17), (19, 18), (19, 19), (19, 20), (19, 21), (19, 22), (19, 23), (19, 24), (19, 25), (18, 25), (17, 25), (17, 24), (17, 23), (17, 22), (17, 21), (16, 21), (15, 21), (15, 22), (15, 23), (14, 23), (13, 23), (13, 24), (13, 25), (13, 26), (13, 27), (14, 27), (15, 27), (16, 27), (17, 27), (17, 28), (17, 29), (18, 29), (19, 29), (19, 28), (19, 27), (20, 27), (21, 27), (21, 26), (21, 25), (21, 24), (21, 23), (22, 23), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (24, 27), (25, 27), (25, 26), (25, 25), (26, 25), (27, 25), (27, 26), (27, 27), (27, 28), (27, 29), (28, 29), (29, 29)]
#                 )
# print(f'length = {len(list)}')
# x_axis = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12','13x13', '14x14', '15x15', '16x16', '17x17', '18x18', '19x19', '20x20']


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

# Change every value that is not 100 to 0 to get final answer accuracy
# line_jpg[line_jpg != 100.0] = 0
# line_json[line_json != 100.0] = 0
# line_adj_json[line_adj_json != 100.0] = 0
# line_adj_txt[line_adj_txt != 100.0] = 0
# line_ascii_txt[line_ascii_txt != 100.0] = 0
# line_tokenized_txt[line_tokenized_txt != 100.0] = 0
# occupancy_jpg[occupancy_jpg != 100.0] = 0
# occupancy_json[occupancy_json != 100.0] = 0
# occupancy_adj_json[occupancy_adj_json != 100.0] = 0
# occupancy_adj_txt[occupancy_adj_txt != 100.0] = 0
# occupancy_ascii_txt[occupancy_ascii_txt != 100.0] = 0
# occupancy_tokenized_txt[occupancy_tokenized_txt != 100.0] = 0


# Create separate graphs for line and occ with aliged x-axes
x_axis_line = ['2x2', '5x5', '10x10','15x15','20x20']
x_axis_occ = ['5x5', '11x11', '21x21', '31x31', '41x41']

line_graph = [('Line Adjacency Json',line_adj_json), 
              ('Line Adjacency Txt', line_adj_txt), 
            #   ('Line ASCII', line_ascii_txt), 
            #   ('Line JPG', line_jpg),
              ('Line JSON', line_json),
              ('Line Tokenized', line_tokenized_txt)]
occ_graph = [('Occupancy Adjacency Json', occupancy_adj_json), 
             ('Occupancy Adjacency Txt', occupancy_adj_txt), 
            #  ('Occupancy ASCII', occupancy_ascii_txt), 
            # ('Occupancy JPG', occupancy_jpg),
             ('Occupancy JSON', occupancy_json), 
             ('Occupancy Tokenized', occupancy_tokenized_txt)]


# Create stacked subplots wiht vertical alignment of x-axis
fig, (ax1, ax2) = plt.subplots(
    nrows=2, ncols=1,
    figsize=(10, 8),
    sharex=False  # align the x-axes perfectly
)

# Define the complexities (shared x positions)
x = np.arange(5)

# top plot
for label, data in line_graph:
    ax1.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)

ax1.set_ylabel('Single Answer Accuracy (%)')
ax1.set_title('Single Answer Accuracy, Line Maze, Gemini 2.5 Pro, Steps Output')
ax1.set_xticks(x)
ax1.set_xticklabels(x_axis_line)
ax1.set_xlabel('Maze Complexity')
ax1.legend(loc='upper right', fontsize=8)
ax1.grid(True, linestyle='--', alpha=0.4)

# bottom plot
for label, data in occ_graph:
    ax2.plot(x, data, marker='o', ls='--', alpha=0.7, label=label)
ax2.set_title('Single Answer Accuracy, Occupancy Maze, Gemini 2.5 Pro, Steps Output')
ax2.set_ylabel('Single Answer Accuracy (%)')
ax2.set_xlabel('Maze Complexity')
ax2.set_xticks(x)
ax2.set_xticklabels(x_axis_occ)
ax2.legend(loc='upper right', fontsize=8)
ax2.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout(h_pad=2.0)
plt.show()





# Create a plot
# Comment out when you want only final accuracy plot 
# plt.plot(x_axis, line_jpg, 'g:', label = 'line jpg')
# plt.plot(x_axis, line_json, 'b:o', label = 'line json')
# plt.plot(x_axis, line_adj_json, 'c:o', label = 'line adjacency json')
# plt.plot(x_axis, line_adj_txt, 'm:o', label = 'line adjacency txt')
# plt.plot(x_axis, line_ascii_txt, 'y:o', label = 'line ASCII')
# plt.plot(x_axis, line_tokenized_txt, 'k:o', label = 'line tokenized')
# plt.plot(x_axis, occupancy_jpg, 'g-->', label = 'occupancy jpg')
# plt.plot(x_axis, occupancy_json, 'b-->', label = 'occupancy json')
# plt.plot(x_axis, occupancy_adj_json, 'c-->', label = 'occupancy adjacency json')
# plt.plot(x_axis, occupancy_adj_txt, 'm-->', label = 'occupancy adjacency txt')
# plt.plot(x_axis, occupancy_ascii_txt, 'y-->', label = 'occupancy ASCII')
# plt.plot(x_axis, occupancy_tokenized_txt, 'k-->', label = 'occupancy tokenized')

# plt.title('Single Answer Accuracy of Gemini 2.5 Pro, Steps Output')
# plt.xlabel('Maze Complexity')
# plt.ylabel('Single Answer Accuracy (%)')

# # plt.title('Final Answer Accuracy of Gemini 2.5 Pro, Steps Output')
# # plt.xlabel('Maze Complexity')
# # plt.ylabel('Final Answer Accuracy (%)')

# plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# plt.grid(linestyle = ':', linewidth = '0.5')
# plt.show()
# # -------------------------------------------------------------------------------------------------------------



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


# # Change every value that is not 100 to 0 to get final answer accuracy
# # Deze grafiek is onduidelijk omdat alle 100 lijnen op elkaar liggen.
# line_jpg[line_jpg != 100.0] = 0
# line_json[line_json != 100.0] = 0
# line_adj_json[line_adj_json != 100.0] = 0
# line_adj_txt[line_adj_txt != 100.0] = 0
# line_ascii_txt[line_ascii_txt != 100.0] = 0
# line_tokenized_txt[line_tokenized_txt != 100.0] = 0
# occupancy_jpg[occupancy_jpg != 100.0] = 0
# occupancy_json[occupancy_json != 100.0] = 0
# occupancy_adj_json[occupancy_adj_json != 100.0] = 0
# occupancy_adj_txt[occupancy_adj_txt != 100.0] = 0
# occupancy_ascii_txt[occupancy_ascii_txt != 100.0] = 0
# occupancy_tokenized_txt[occupancy_tokenized_txt != 100.0] = 0

# # Create a plot
# # Comment out when you want only final accuracy plot 
# plt.plot(x_axis, line_jpg, 'g:o', label = 'line jpg')
# plt.plot(x_axis, line_json, 'b:o', label = 'line json')
# plt.plot(x_axis, line_adj_json, 'c:o', label = 'line adjacency json')
# plt.plot(x_axis, line_adj_txt, 'm:o', label = 'line adjacency txt')
# plt.plot(x_axis, line_ascii_txt, 'y:o', label = 'line ASCII')
# plt.plot(x_axis, line_tokenized_txt, 'k:o', label = 'line tokenized')
# plt.plot(x_axis, occupancy_jpg, 'g-->', label = 'occupancy jpg')
# plt.plot(x_axis, occupancy_json, 'b-->', label = 'occupancy json')
# plt.plot(x_axis, occupancy_adj_json, 'c-->', label = 'occupancy adjacency json')
# plt.plot(x_axis, occupancy_adj_txt, 'm-->', label = 'occupancy adjacency txt')
# plt.plot(x_axis, occupancy_ascii_txt, 'y-->', label = 'occupancy ASCII')
# plt.plot(x_axis, occupancy_tokenized_txt, 'k-->', label = 'occupancy tokenized')

# plt.title('Single Answer Accuracy of Gemini 2.5 Flash Lite, Steps Output')
# plt.xlabel('Maze Complexity')
# plt.ylabel('Single Answer Accuracy (%)')

# plt.title('Final Answer Accuracy of Gemini 2.5 Flash Lite, Steps Output')
# plt.xlabel('Maze Complexity')
# plt.ylabel('Final Answer Accuracy (%)')

# plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# plt.grid(linestyle = ':', linewidth = '0.5')
# plt.show()
# # -------------------------------------------------------------------------------------------------------------



# # -------------------- non-reasoning, coordinate output, dataset 01. ----------------
# x_axis = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12','13x13', '14x14', '15x15']

# line_jpg = np.array([66.67, 0, 0, 0, 7.69, 0, 4.76, 3.92, 2.33, 0, 8.2, 3.37, 0, 0.87 ])
# line_json = np.array([100, 20, 11.11, 6.67, 15.38, 10.53, 4.76, 3.92, 2.33, 3.17, 3.28, 3.37, 0.9, 5.22])
# line_adj_json = np.array([100, 100, 100, 100, 100, 78.95, 76.19, 11.76, 46.51, 15.87, 9.84, 24.72, 18.92, 26.09])
# line_adj_txt = np.array([100, 100, 100, 100, 100, 78.95, 66.67, 11.76, 2.33, 19.05, 44.26, 7.87, 10.81, 8.7])
# line_ascii = np.array([33.33, 80, 11.11, 13.33, 15.38, 10.53, 14.29, 3.92, 6.98, 1.59, 4.92, 1.12, 0.9, 0.87])
# line_tokenized = np.array([100, 20, 11.11, 0, 30.77, 21.05, 23.81, 1.96, 2.33, 3.17, 6.56, 3.37, 0.9, 1.74])
# occupancy_jpg = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# occupancy_json = np.array([20, 100, 100, 51.72, 4, 2.7, 21.95, 0.99, 8.24, 2.4, 0.83, 0.56, 4.07, 0.44])
# occupancy_adj_json = np.array([100, 100, 100, 93.1, 100, 100, 90.24, 70.3, 12.94, 15.2, 23.97, 63.84, 12.22, 7.86])
# occupancy_adj_txt = np.array([100, 100, 100, 100, 100, 94.59, 100, 70.3, 22.35, 7.2, 23.97, 5.08, 10.41, 8.3])
# occupancy_ascii = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# occupancy_tokenized = np.array([80, 77.78, 52.94, 17.24, 4, 2.7, 17.07, 0.99, 10.59, 0.8, 0.83, 0.56, 1.36, 0.44])

# Change every value that is not 100 to 0 to get final answer accuracy
# line_jpg[line_jpg != 100.0] = 0
# line_json[line_json != 100.0] = 0
# line_adj_json[line_adj_json != 100.0] = 0
# line_adj_txt[line_adj_txt != 100.0] = 0
# line_ascii[line_ascii != 100.0] = 0
# line_tokenized[line_tokenized != 100.0] = 0
# occupancy_jpg[occupancy_jpg != 100.0] = 0
# occupancy_json[occupancy_json != 100.0] = 0
# occupancy_adj_json[occupancy_adj_json != 100.0] = 0
# occupancy_adj_txt[occupancy_adj_txt != 100.0] = 0
# occupancy_ascii[occupancy_ascii != 100.0] = 0
# occupancy_tokenized[occupancy_tokenized != 100.0] = 0

# # Create a plot
# # Comment out when you want only final accuracy plot 
# plt.plot(x_axis, line_jpg, 'g:o', label = 'line jpg')
# plt.plot(x_axis, line_json, 'b:o', label = 'line json')
# plt.plot(x_axis, line_adj_json, 'c:o', label = 'line adjacency json')
# plt.plot(x_axis, line_adj_txt, 'm:o', label = 'line adjacency txt')
# plt.plot(x_axis, line_ascii, 'y:o', label = 'line ASCII')
# plt.plot(x_axis, line_tokenized, 'k:o', label = 'line tokenized')
# plt.plot(x_axis, occupancy_jpg, 'g-->', label = 'occupancy jpg')
# plt.plot(x_axis, occupancy_json, 'b-->', label = 'occupancy json')
# plt.plot(x_axis, occupancy_adj_json, 'c-->', label = 'occupancy adjacency json')
# plt.plot(x_axis, occupancy_adj_txt, 'm-->', label = 'occupancy adjacency txt')
# plt.plot(x_axis, occupancy_ascii, 'y-->', label = 'occupancy ASCII')
# plt.plot(x_axis, occupancy_tokenized, 'k-->', label = 'occupancy tokenized')

# plt.title('Single Answer Accuracy of Gemini 2.5 Flash Lite, Coordinate Output')
# plt.xlabel('Maze Complexity')
# plt.ylabel('Single Answer Accuracy (%)')

# # plt.title('Final Answer Accuracy of Gemini 2.5 Flash Lite, Coordinate Output')
# # plt.xlabel('Maze Complexity')
# # plt.ylabel('Final Answer Accuracy (%)')

# plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
# plt.grid(linestyle = ':', linewidth = '0.5')
# plt.show()
# # -------------------------------------------------------------------------------------------------------------
