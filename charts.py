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


x_axis = ['2x2', '3x3', '4x4', '5x5', '6x6','7x7','8x8','9x9', '10x10','11x11','12x12','13x13', '14x14', '15x15']


# -------------------- non-reasoning, coordinate output, dataset 01, single answer accuracy. ----------------
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

# Create a plot
# Comment out when you want only final accuracy plot 
plt.plot(x_axis, line_jpg, 'g:o', label = 'line jpg')
plt.plot(x_axis, line_json, 'b:o', label = 'line json')
plt.plot(x_axis, line_adj_json, 'c:o', label = 'line adjacency json')
plt.plot(x_axis, line_adj_txt, 'm:o', label = 'line adjacency txt')
plt.plot(x_axis, line_ascii, 'y:o', label = 'line ASCII')
plt.plot(x_axis, line_tokenized, 'k:o', label = 'line tokenized')
plt.plot(x_axis, occupancy_jpg, 'g-->', label = 'occupancyupancy jpg')
plt.plot(x_axis, occupancy_json, 'b-->', label = 'occupancyupancy json')
plt.plot(x_axis, occupancy_adj_json, 'c-->', label = 'occupancyupancy adjacency json')
plt.plot(x_axis, occupancy_adj_txt, 'm-->', label = 'occupancyupancy adjacency txt')
plt.plot(x_axis, occupancy_ascii, 'y-->', label = 'occupancyupancy ASCII')
plt.plot(x_axis, occupancy_tokenized, 'k-->', label = 'occupancyupancy tokenized')
plt.title('Single Answer Accuracy of Gemini 2.5 Flash Lite, Coordinate Output')
plt.xlabel('Maze Complexity')
plt.ylabel('Single Answer Accuracy (%)')
plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
plt.grid(linestyle = ':', linewidth = '0.5')
plt.show()
# -------------------------------------------------------------------------------------------------------------

# -------------------- non-reasoning, coordinate output, dataset 01, final accuracy. ----------------
# Change every value that is not 100 to 0 to get final answer accuracy
line_jpg[line_jpg != 100] = 0
line_json[line_json != 100] = 0
line_adj_json[line_adj_json != 100] = 0
line_adj_txt[line_adj_txt != 100] = 0
line_ascii[line_ascii != 100] = 0
line_tokenized[line_tokenized != 100] = 0
occupancy_jpg[occupancy_jpg != 100] = 0
occupancy_json[occupancy_json != 100] = 0
occupancy_adj_json[occupancy_adj_json != 100] = 0
occupancy_adj_txt[occupancy_adj_txt != 100] = 0
occupancy_ascii[occupancy_ascii != 100] = 0
occupancy_tokenized[occupancy_tokenized != 100] = 0

# Create plots
plt.plot(x_axis, line_jpg, 'g:o', label = 'line jpg')
plt.plot(x_axis, line_json, 'b:o', label = 'line json')
plt.plot(x_axis, line_adj_json, 'c:o', label = 'line adjacency json')
plt.plot(x_axis, line_adj_txt, 'm:o', label = 'line adjacency txt')
plt.plot(x_axis, line_ascii, 'y:o', label = 'line ASCII')
plt.plot(x_axis, line_tokenized, 'k:o', label = 'line tokenized')
plt.plot(x_axis, occupancy_jpg, 'g-->', label = 'occupancyupancy jpg')
plt.plot(x_axis, occupancy_json, 'b-->', label = 'occupancyupancy json')
plt.plot(x_axis, occupancy_adj_json, 'c-->', label = 'occupancyupancy adjacency json')
plt.plot(x_axis, occupancy_adj_txt, 'm-->', label = 'occupancyupancy adjacency txt')
plt.plot(x_axis, occupancy_ascii, 'y-->', label = 'occupancyupancy ASCII')
plt.plot(x_axis, occupancy_tokenized, 'k-->', label = 'occupancyupancy tokenized')
plt.title('Final Answer Accuracy of Gemini 2.5 Flash Lite, Coordinate Output')
plt.xlabel('Maze Complexity')
plt.ylabel('Final Answer Accuracy (%)')
plt.legend(loc=(1.04, 0)) # Place legend to top right of plot, next to plot. 
plt.grid(linestyle = ':', linewidth = '0.5')
plt.show()
