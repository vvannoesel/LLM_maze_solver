# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import numpy as np
import matplotlib.pyplot as plt
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple

def binary_occurrence(category_list):
    ''' Function that converts the occurrence count of a category into
    a binary presence (1) or absence (0) for each run.
    
    input: list of occurrence count
    output: np array of binary presence
    takes the input list, converts to np array and then applies
    condition that converts all >0 values to a 1. '''
    category_array = np.array(category_list)
    return (category_array>0).astype(int)

# Only algorithm naming, all representations of 15

# Category counts excluding words such as DFS and BFS. 

line_R_coords_adj_json_algorithm_15 = [50, 2, 1, 0, 1, 0, 0, 3, 0, 0, 2, 2, 0, 3, 2, 1, 1, 0, 1, 0, 0, 0, 0, 2, 1, 1, 4, 5, 2, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 3, 2, 1, 1, 3, 0, 1]
line_R_coords_adj_json_backtracking_15 = [0, 3, 1, 1, 6, 5, 4, 12, 4, 1, 9, 3, 5, 6, 2, 3, 2, 4, 4, 1, 2, 2, 2, 4, 3, 1, 2, 6, 3, 3, 3, 5, 2, 5, 3, 5, 6, 1, 2, 7, 3, 2, 2, 2, 0, 1, 3, 5, 7, 5]
line_R_coords_adj_json_false_confidence_15 = [1, 0, 5, 0, 3, 0, 0, 0, 2, 2, 1, 3, 1, 0, 4, 1, 1, 2, 1, 2, 5, 1, 2, 0, 0, 1, 0, 1, 0, 2, 1, 3, 0, 1, 0, 2, 2, 0, 7, 0, 2, 0, 1, 0, 1, 0, 1, 1, 0, 4]
line_R_coords_adj_json_frustration_15 = [1, 2, 4, 1, 6, 2, 2, 5, 3, 0, 1, 1, 2, 0, 1, 0, 1, 2, 0, 0, 4, 0, 2, 1, 0, 0, 0, 2, 1, 7, 2, 1, 1, 1, 1, 0, 0, 0, 2, 1, 2, 0, 1, 0, 2, 0, 0, 2, 7, 2]
line_R_coords_adj_json_heuristic_15 = [0, 1, 0, 0, 2, 3, 0, 0, 2, 1, 2, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0, 0, 4, 1, 0, 1, 0, 0, 5, 0, 1, 0, 3, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 3, 2, 0, 1, 0]
line_R_coords_adj_json_restart_15 = [0, 0, 1, 0, 3, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 1]
line_R_coords_adj_json_reverse_search_15 = [0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
line_R_coords_adj_json_step_by_step_15 = [14, 0, 0, 4, 1, 0, 0, 3, 0, 54, 0, 86, 2, 0, 83, 1, 0, 0, 49, 126, 0, 2, 1, 111, 1, 51, 0, 0, 1, 0, 2, 2, 5, 0, 80, 0, 0, 44, 8, 6, 0, 0, 0, 0, 49, 0, 0, 0, 0, 0]
line_R_coords_adj_json_verification_15 = [1, 2, 4, 1, 6, 6, 6, 6, 1, 4, 3, 4, 2, 4, 3, 4, 4, 10, 5, 1, 4, 9, 2, 3, 4, 7, 5, 6, 1, 5, 6, 3, 0, 4, 1, 3, 6, 5, 3, 3, 4, 6, 8, 1, 2, 1, 2, 3, 5, 9]
line_R_coords_adj_txt_algorithm_15 = [10, 0, 1, 1, 5, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 4, 0, 1, 0, 2, 0, 1, 2, 0, 0, 0, 1, 0, 0, 3, 2, 0, 1, 4, 0, 16, 0, 2, 0, 0, 0, 3, 0, 1, 0, 1]
line_R_coords_adj_txt_backtracking_15 = [7, 4, 7, 1, 2, 5, 4, 1, 5, 4, 2, 4, 4, 3, 1, 5, 4, 3, 2, 6, 3, 2, 5, 7, 4, 2, 2, 5, 4, 4, 1, 1, 3, 14, 4, 3, 1, 2, 2, 10, 4, 5, 1, 2, 1, 7, 2, 2, 0, 3]
line_R_coords_adj_txt_false_confidence_15 = [0, 2, 4, 0, 1, 5, 1, 3, 1, 4, 0, 3, 1, 6, 1, 0, 1, 4, 1, 0, 2, 2, 2, 1, 1, 2, 1, 1, 0, 2, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 2, 1, 1, 2, 0, 1, 2, 2, 1, 1]
line_R_coords_adj_txt_frustration_15 = [7, 1, 3, 0, 3, 5, 0, 8, 2, 10, 1, 0, 0, 3, 0, 2, 6, 4, 1, 7, 1, 2, 1, 0, 3, 2, 2, 2, 3, 2, 5, 1, 0, 4, 5, 2, 4, 1, 3, 3, 9, 5, 1, 4, 3, 5, 1, 3, 1, 4]
line_R_coords_adj_txt_heuristic_15 = [2, 0, 2, 1, 0, 0, 0, 1, 0, 5, 0, 0, 1, 1, 0, 1, 2, 0, 0, 3, 2, 1, 1, 2, 1, 1, 1, 4, 0, 1, 1, 3, 0, 2, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 5, 3, 1, 2, 2, 1]
line_R_coords_adj_txt_restart_15 = [5, 0, 6, 0, 4, 5, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 1, 1, 2, 6, 0, 1, 0, 1, 1, 0, 0, 0, 0, 3, 1, 2, 2, 0, 4, 0, 0, 4, 1, 2, 2, 3, 1, 2, 0, 1]
line_R_coords_adj_txt_reverse_search_15 = [3, 0, 1, 0, 3, 5, 0, 3, 0, 4, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1]
line_R_coords_adj_txt_step_by_step_15 = [0, 0, 8, 79, 0, 2, 2, 0, 69, 0, 63, 0, 61, 3, 0, 1, 1, 0, 18, 0, 20, 2, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 62, 0, 0, 0, 49, 13, 0, 1, 18, 4, 6, 12, 0, 0, 0, 65, 0]
line_R_coords_adj_txt_verification_15 = [7, 5, 3, 1, 2, 3, 12, 3, 15, 6, 1, 7, 3, 8, 6, 3, 3, 1, 7, 5, 2, 10, 8, 5, 8, 4, 2, 9, 6, 3, 9, 4, 8, 9, 1, 4, 3, 1, 2, 2, 10, 11, 7, 10, 7, 7, 4, 2, 8, 8]
line_R_coords_jpg_algorithm_15 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
line_R_coords_jpg_backtracking_15 = [12, 1, 3, 5, 2, 1, 6, 3, 5, 0, 4, 5, 3, 5, 1, 2, 4, 3, 3, 5, 3, 6, 7, 2, 3, 2, 9, 7, 3, 1, 8, 1, 8, 3, 3, 3, 2, 8, 5, 8, 4, 8, 2, 5, 9, 8, 4, 4, 4, 2]
line_R_coords_jpg_false_confidence_15 = [2, 4, 1, 1, 1, 0, 4, 3, 4, 0, 2, 1, 3, 2, 1, 1, 1, 2, 1, 4, 2, 1, 2, 0, 1, 2, 1, 0, 1, 1, 1, 0, 0, 7, 1, 1, 1, 1, 2, 2, 4, 0, 4, 3, 0, 2, 6, 2, 2, 1]
line_R_coords_jpg_frustration_15 = [2, 2, 2, 5, 1, 0, 1, 1, 2, 2, 3, 0, 2, 1, 0, 4, 4, 1, 5, 3, 2, 0, 0, 0, 1, 0, 4, 4, 3, 1, 0, 2, 4, 1, 1, 1, 3, 1, 1, 0, 0, 1, 0, 3, 4, 2, 1, 0, 3, 0]
line_R_coords_jpg_heuristic_15 = [3, 2, 3, 1, 1, 1, 1, 2, 3, 1, 3, 6, 2, 4, 0, 0, 1, 6, 4, 4, 0, 1, 0, 1, 2, 3, 6, 3, 5, 3, 3, 1, 2, 3, 2, 4, 4, 4, 5, 2, 2, 2, 3, 3, 1, 2, 4, 6, 1, 2]
line_R_coords_jpg_restart_15 = [4, 0, 0, 3, 0, 1, 1, 2, 0, 0, 2, 0, 3, 3, 0, 1, 3, 1, 0, 1, 0, 0, 1, 0, 0, 0, 3, 0, 1, 1, 1, 0, 2, 2, 1, 1, 1, 1, 0, 3, 0, 1, 1, 2, 3, 1, 0, 0, 2, 3]
line_R_coords_jpg_reverse_search_15 = [0, 0, 0, 5, 3, 0, 1, 0, 3, 1, 0, 0, 1, 0, 2, 1, 1, 0, 0, 6, 4, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 0, 4, 0, 0, 1, 0, 0, 3, 0, 5, 1, 0, 0, 0, 1, 1]
line_R_coords_jpg_step_by_step_15 = [0, 0, 0, 1, 0, 0, 1, 0, 46, 0, 0, 0, 53, 1, 13, 48, 0, 0, 0, 3, 1, 20, 0, 0, 3, 53, 43, 58, 0, 16, 46, 68, 46, 47, 0, 0, 0, 1, 0, 36, 38, 1, 79, 1, 26, 43, 0, 42, 0, 55]
line_R_coords_jpg_verification_15 = [5, 6, 3, 3, 3, 1, 3, 4, 5, 3, 2, 6, 2, 1, 0, 5, 3, 3, 4, 4, 5, 0, 5, 2, 3, 5, 3, 3, 4, 3, 0, 1, 6, 6, 3, 5, 2, 4, 5, 11, 3, 2, 2, 3, 3, 9, 3, 3, 2, 4]
line_R_coords_json_algorithm_15 = [9, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 1, 0, 0, 3, 0, 0, 2, 0]
line_R_coords_json_backtracking_15 = [2, 3, 0, 7, 2, 4, 1, 8, 5, 1, 5, 2, 4, 10, 5, 4, 6, 4, 4, 8, 2, 2, 2, 3, 1, 4, 5, 6, 1, 2, 3, 3, 4, 1, 5, 6, 3, 6, 4, 2, 2, 3, 4, 2, 6, 9, 5, 4, 5, 3]
line_R_coords_json_false_confidence_15 = [1, 3, 0, 1, 1, 4, 2, 0, 0, 1, 2, 4, 0, 3, 0, 0, 2, 0, 2, 1, 4, 1, 2, 1, 2, 1, 3, 0, 0, 1, 3, 0, 1, 3, 0, 2, 1, 1, 2, 4, 2, 0, 5, 2, 1, 1, 3, 2, 1, 3]
line_R_coords_json_frustration_15 = [2, 0, 0, 2, 5, 6, 2, 4, 2, 1, 9, 1, 4, 7, 2, 2, 5, 3, 3, 5, 4, 2, 0, 2, 1, 2, 3, 4, 2, 4, 7, 3, 3, 4, 5, 6, 2, 4, 3, 2, 1, 2, 2, 0, 2, 4, 3, 2, 3, 2]
line_R_coords_json_heuristic_15 = [0, 4, 0, 4, 2, 3, 0, 8, 1, 2, 1, 1, 1, 2, 1, 0, 3, 1, 5, 3, 3, 0, 0, 2, 1, 1, 2, 0, 1, 1, 2, 1, 0, 4, 1, 2, 2, 1, 3, 0, 3, 2, 2, 1, 1, 2, 1, 0, 1, 1]
line_R_coords_json_restart_15 = [0, 0, 0, 0, 0, 4, 0, 2, 2, 1, 0, 0, 2, 6, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 3, 0, 1, 0, 0, 2, 1, 3, 2, 1, 0, 1, 1, 2, 0, 1, 2, 0, 2, 0, 0, 3, 1, 2, 1, 0]
line_R_coords_json_reverse_search_15 = [0, 0, 0, 0, 1, 2, 1, 0, 1, 0, 1, 0, 0, 0, 4, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 4, 1, 0, 3, 0, 0, 0, 1, 3, 2, 2, 0, 4, 0, 3, 0, 0, 0, 2, 0, 1, 0, 2]
line_R_coords_json_step_by_step_15 = [8, 0, 61, 3, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 9, 6, 51, 0, 1, 0, 0, 0, 44, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 1, 9, 1, 0, 0, 36, 5, 0]
line_R_coords_json_verification_15 = [8, 8, 0, 1, 7, 7, 6, 5, 3, 2, 7, 3, 11, 10, 1, 3, 8, 3, 8, 6, 4, 2, 3, 1, 0, 2, 2, 7, 1, 6, 2, 6, 10, 7, 1, 6, 6, 8, 6, 13, 3, 1, 7, 1, 4, 5, 2, 6, 3, 11]
line_R_coords_tokenized_txt_algorithm_15 = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 1, 1, 1, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
line_R_coords_tokenized_txt_backtracking_15 = [4, 2, 8, 1, 3, 8, 4, 4, 6, 1, 4, 4, 1, 2, 11, 6, 0, 4, 0, 1, 5, 1, 6, 3, 0, 4, 6, 0, 2, 2, 5, 0, 5, 1, 3, 3, 1, 0, 1, 3, 6, 8, 3, 2, 7, 2, 3, 4, 1, 7]
line_R_coords_tokenized_txt_false_confidence_15 = [2, 2, 3, 0, 3, 6, 2, 1, 2, 2, 1, 2, 3, 2, 2, 0, 0, 1, 2, 1, 1, 0, 2, 0, 4, 0, 2, 1, 0, 1, 0, 0, 3, 0, 1, 1, 5, 1, 1, 0, 1, 3, 2, 1, 2, 1, 1, 1, 4, 4]
line_R_coords_tokenized_txt_frustration_15 = [5, 1, 4, 2, 1, 5, 2, 2, 2, 1, 1, 4, 2, 1, 5, 4, 2, 4, 1, 1, 1, 1, 2, 4, 1, 2, 3, 1, 0, 0, 0, 0, 3, 6, 0, 0, 7, 1, 3, 1, 4, 2, 4, 1, 4, 2, 1, 0, 2, 6]
line_R_coords_tokenized_txt_heuristic_15 = [1, 2, 3, 0, 1, 3, 0, 1, 1, 3, 0, 3, 0, 0, 4, 0, 1, 1, 0, 1, 1, 2, 0, 0, 0, 1, 2, 2, 0, 0, 1, 2, 0, 3, 0, 2, 4, 2, 0, 2, 1, 2, 0, 3, 1, 0, 0, 0, 0, 2]
line_R_coords_tokenized_txt_restart_15 = [2, 0, 1, 0, 2, 0, 1, 1, 2, 0, 1, 0, 2, 1, 2, 1, 2, 3, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 1, 0, 0, 0, 3, 1, 2, 0, 1, 3, 0, 0, 1, 6]
line_R_coords_tokenized_txt_reverse_search_15 = [1, 0, 0, 0, 0, 5, 0, 3, 0, 0, 2, 3, 1, 0, 3, 3, 3, 0, 0, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
line_R_coords_tokenized_txt_step_by_step_15 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 91, 83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 78, 0, 1, 0, 1, 0, 1, 2, 0, 0, 10, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 73, 0]
line_R_coords_tokenized_txt_verification_15 = [2, 3, 4, 0, 2, 7, 3, 1, 3, 7, 2, 3, 4, 5, 2, 3, 7, 3, 12, 4, 6, 9, 3, 2, 6, 7, 3, 0, 4, 4, 1, 2, 7, 3, 5, 5, 3, 2, 1, 1, 8, 4, 4, 6, 5, 5, 6, 5, 1, 2]
occupancy_R_coords_adj_json_algorithm_15 = [0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 2, 0, 1, 0, 0, 4, 2, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 2, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
occupancy_R_coords_adj_json_backtracking_15 = [0, 4, 0, 3, 2, 1, 2, 4, 6, 2, 5, 2, 2, 7, 4, 3, 6, 3, 3, 3, 5, 1, 4, 3, 2, 4, 4, 6, 0, 2, 3, 1, 0, 3, 6, 4, 1, 4, 5, 2, 0, 2, 2, 1, 4, 2, 0, 5, 1, 2]
occupancy_R_coords_adj_json_false_confidence_15 = [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 3, 1, 2, 0, 5, 0, 0, 0, 4, 0, 1, 1, 0, 0, 0, 4, 1, 0, 3, 3, 1, 0, 4, 0, 0, 0, 1, 0, 1, 3, 0, 4, 1, 1]
occupancy_R_coords_adj_json_frustration_15 = [0, 4, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 3, 1, 2, 3, 0, 4, 0, 3, 0, 1, 1, 0, 3, 0, 4, 0, 0, 1, 4, 1, 2, 1, 3, 0, 1, 1, 0, 0, 5, 1, 4, 2, 1, 0, 1, 0, 0]
occupancy_R_coords_adj_json_heuristic_15 = [0, 2, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 2, 0, 2, 1, 0, 1, 2, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2, 0, 0, 0, 1, 1]
occupancy_R_coords_adj_json_restart_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
occupancy_R_coords_adj_json_reverse_search_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
occupancy_R_coords_adj_json_step_by_step_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 54, 0, 0, 1, 0, 0, 101, 0, 0, 0, 0, 102, 0, 83, 5, 0, 13, 1, 15, 1, 2, 121, 5, 1, 0, 0, 108, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
occupancy_R_coords_adj_json_verification_15 = [0, 3, 0, 5, 3, 4, 0, 2, 4, 1, 2, 0, 5, 3, 4, 3, 4, 4, 7, 1, 2, 1, 1, 2, 8, 8, 4, 3, 1, 0, 4, 3, 3, 2, 7, 3, 2, 3, 3, 3, 0, 10, 1, 4, 1, 3, 1, 4, 1, 1]
occupancy_R_coords_adj_txt_algorithm_15 = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 4, 0, 0, 0, 1, 7, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2]
occupancy_R_coords_adj_txt_backtracking_15 = [0, 0, 1, 2, 3, 3, 2, 1, 3, 3, 3, 2, 1, 5, 1, 3, 3, 1, 0, 4, 4, 1, 0, 2, 2, 2, 4, 1, 1, 2, 1, 2, 1, 0, 4, 4, 2, 0, 0, 3, 2, 3, 3, 2, 2, 0, 2, 3, 0, 4]
occupancy_R_coords_adj_txt_false_confidence_15 = [0, 1, 1, 4, 3, 4, 2, 0, 1, 0, 1, 3, 2, 1, 3, 2, 0, 2, 1, 0, 1, 4, 2, 1, 3, 1, 0, 1, 1, 1, 1, 3, 1, 3, 0, 1, 1, 1, 2, 3, 2, 3, 2, 4, 2, 0, 0, 2, 0, 2]
occupancy_R_coords_adj_txt_frustration_15 = [0, 2, 0, 0, 3, 3, 5, 2, 4, 5, 2, 7, 0, 1, 1, 4, 2, 1, 0, 7, 1, 0, 1, 1, 2, 1, 2, 1, 0, 4, 1, 3, 1, 4, 3, 3, 0, 1, 1, 4, 2, 4, 2, 2, 0, 1, 3, 2, 0, 3]
occupancy_R_coords_adj_txt_heuristic_15 = [0, 0, 1, 0, 0, 3, 0, 4, 0, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 2, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5, 1, 2, 0, 0, 3, 0, 3, 1, 1, 0, 0, 1, 0, 1]
occupancy_R_coords_adj_txt_restart_15 = [0, 1, 0, 2, 1, 2, 2, 2, 0, 0, 0, 1, 0, 1, 1, 1, 2, 2, 0, 2, 2, 0, 0, 0, 3, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 4, 0, 2, 0, 1, 2, 0, 0, 3, 0, 0]
occupancy_R_coords_adj_txt_reverse_search_15 = [0, 0, 0, 0, 2, 1, 0, 4, 0, 2, 1, 0, 0, 0, 2, 2, 2, 5, 0, 3, 6, 0, 0, 1, 3, 0, 2, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 1, 2, 0, 3, 1, 0, 1, 0, 0, 0]
occupancy_R_coords_adj_txt_step_by_step_15 = [0, 0, 0, 0, 4, 0, 0, 2, 1, 0, 2, 1, 5, 0, 2, 4, 0, 8, 2, 4, 3, 0, 2, 0, 54, 0, 6, 76, 7, 2, 11, 1, 0, 0, 1, 0, 1, 99, 0, 1, 2, 2, 4, 0, 1, 33, 20, 0, 0, 0]
occupancy_R_coords_adj_txt_verification_15 = [0, 1, 5, 4, 8, 3, 2, 3, 3, 1, 2, 2, 2, 6, 2, 7, 3, 4, 7, 2, 3, 7, 1, 0, 11, 5, 0, 1, 6, 1, 1, 3, 7, 6, 5, 0, 7, 2, 3, 3, 1, 7, 3, 3, 8, 3, 6, 5, 1, 4]
occupancy_R_coords_ascii_txt_algorithm_15 = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
occupancy_R_coords_ascii_txt_backtracking_15 = [1, 9, 1, 3, 0, 3, 2, 3, 7, 2, 2, 10, 2, 4, 2, 5, 5, 9, 7, 4, 1, 1, 1, 3, 2, 3, 9, 3, 3, 3, 4, 1, 5, 6, 2, 2, 2, 0, 2, 2, 3, 5, 3, 0, 1, 3, 9, 4, 3, 1]
occupancy_R_coords_ascii_txt_false_confidence_15 = [6, 5, 0, 1, 1, 3, 3, 5, 3, 0, 1, 5, 0, 1, 1, 2, 1, 5, 1, 1, 1, 0, 1, 0, 1, 2, 0, 3, 2, 2, 1, 1, 3, 1, 1, 0, 4, 0, 0, 3, 0, 0, 3, 1, 0, 2, 3, 3, 2, 1]
occupancy_R_coords_ascii_txt_frustration_15 = [1, 5, 1, 2, 3, 4, 5, 6, 6, 4, 0, 4, 6, 3, 4, 1, 5, 3, 0, 2, 4, 1, 2, 4, 6, 5, 3, 5, 3, 10, 0, 0, 3, 4, 7, 0, 2, 1, 2, 2, 7, 1, 3, 2, 0, 2, 7, 1, 6, 4]
occupancy_R_coords_ascii_txt_heuristic_15 = [1, 0, 1, 1, 2, 4, 2, 2, 2, 0, 3, 1, 0, 0, 2, 4, 2, 7, 4, 0, 2, 0, 1, 1, 4, 0, 1, 1, 2, 3, 4, 1, 2, 0, 4, 2, 1, 0, 2, 4, 0, 1, 0, 0, 2, 3, 1, 2, 0, 6]
occupancy_R_coords_ascii_txt_restart_15 = [0, 0, 1, 1, 2, 0, 0, 0, 4, 0, 0, 2, 1, 2, 1, 3, 4, 3, 3, 1, 1, 0, 0, 1, 1, 0, 2, 3, 1, 2, 0, 0, 2, 1, 3, 2, 3, 0, 1, 1, 2, 0, 1, 0, 0, 3, 2, 0, 1, 1]
occupancy_R_coords_ascii_txt_reverse_search_15 = [0, 1, 0, 4, 0, 0, 0, 0, 2, 2, 0, 1, 1, 0, 3, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 4, 2, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
occupancy_R_coords_ascii_txt_step_by_step_15 = [8, 0, 0, 0, 79, 0, 3, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 5, 0, 18, 0, 0, 52, 1, 0, 0, 0, 75, 7, 1, 1, 118, 3, 0, 0, 0, 0, 39, 0, 0, 18, 0, 0, 116, 0, 0, 2, 2, 4, 1]
occupancy_R_coords_ascii_txt_verification_15 = [0, 3, 4, 2, 1, 2, 1, 7, 4, 0, 6, 6, 3, 7, 4, 0, 13, 3, 3, 2, 1, 0, 7, 5, 7, 6, 4, 6, 7, 5, 4, 3, 3, 4, 4, 2, 5, 0, 1, 2, 3, 5, 3, 0, 0, 2, 8, 1, 7, 0]
occupancy_R_coords_jpg_algorithm_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
occupancy_R_coords_jpg_backtracking_15 = [7, 0, 4, 2, 6, 0, 3, 11, 1, 3, 2, 5, 2, 13, 4, 1, 1, 6, 3, 2, 3, 3, 1, 5, 3, 4, 9, 10, 3, 2, 0, 10, 5, 6, 7, 0, 0, 6, 7, 3, 6, 4, 8, 2, 3, 0, 1, 3, 3, 3]
occupancy_R_coords_jpg_false_confidence_15 = [3, 0, 2, 4, 2, 0, 1, 3, 2, 1, 0, 4, 1, 3, 1, 2, 0, 1, 3, 0, 2, 2, 0, 2, 2, 2, 3, 0, 0, 0, 2, 5, 2, 2, 1, 1, 0, 0, 4, 2, 0, 0, 4, 5, 1, 0, 0, 0, 2, 1]
occupancy_R_coords_jpg_frustration_15 = [5, 2, 1, 2, 5, 0, 1, 4, 1, 1, 0, 2, 3, 3, 1, 2, 0, 2, 2, 0, 1, 0, 3, 2, 3, 7, 8, 0, 7, 1, 4, 5, 3, 2, 0, 2, 0, 2, 4, 1, 2, 2, 7, 4, 6, 0, 0, 3, 1, 5]
occupancy_R_coords_jpg_heuristic_15 = [4, 4, 3, 7, 4, 1, 2, 2, 1, 2, 3, 1, 6, 4, 3, 3, 3, 5, 4, 3, 5, 3, 6, 1, 2, 1, 6, 0, 6, 4, 2, 4, 5, 3, 2, 3, 1, 5, 2, 2, 4, 1, 2, 2, 6, 0, 3, 4, 3, 3]
occupancy_R_coords_jpg_restart_15 = [0, 1, 0, 1, 3, 0, 0, 2, 0, 1, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 1, 5, 0, 3, 1, 0, 4, 2, 0, 0, 0, 0, 1, 3, 1, 1, 1, 2, 1, 0, 0, 0, 1, 1, 2]
occupancy_R_coords_jpg_reverse_search_15 = [0, 0, 2, 0, 3, 0, 1, 0, 0, 3, 0, 1, 1, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 4, 3, 3, 0, 0, 1, 0, 0, 5, 1, 3]
occupancy_R_coords_jpg_step_by_step_15 = [0, 74, 0, 1, 0, 0, 1, 0, 0, 1, 10, 0, 0, 0, 5, 0, 115, 0, 2, 0, 2, 6, 90, 0, 0, 1, 1, 38, 2, 3, 4, 0, 0, 0, 43, 0, 0, 16, 0, 0, 78, 2, 0, 1, 54, 0, 20, 0, 0, 77]
occupancy_R_coords_jpg_verification_15 = [2, 1, 2, 8, 3, 6, 2, 3, 5, 2, 0, 7, 1, 8, 2, 8, 3, 6, 3, 5, 1, 2, 0, 2, 2, 1, 8, 1, 2, 1, 6, 2, 4, 1, 2, 2, 1, 1, 1, 0, 4, 3, 11, 6, 4, 0, 0, 4, 5, 2]
occupancy_R_coords_json_algorithm_15 = [9, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
occupancy_R_coords_json_backtracking_15 = [0, 1, 5, 3, 3, 0, 2, 0, 2, 2, 2, 3, 2, 2, 5, 1, 5, 6, 5, 0, 1, 4, 4, 4, 4, 7, 5, 2, 5, 0, 1, 0, 0, 2, 4, 0, 3, 8, 4, 3, 4, 1, 4, 4, 2, 1, 0, 3, 2, 3]
occupancy_R_coords_json_false_confidence_15 = [1, 1, 1, 1, 0, 2, 3, 2, 1, 4, 0, 3, 1, 0, 4, 4, 4, 3, 0, 1, 0, 0, 1, 0, 2, 7, 3, 1, 2, 0, 2, 0, 1, 1, 1, 1, 0, 4, 1, 2, 0, 1, 3, 0, 2, 0, 1, 0, 0, 0]
occupancy_R_coords_json_frustration_15 = [2, 1, 4, 5, 1, 2, 2, 3, 0, 4, 2, 8, 0, 4, 2, 0, 3, 1, 4, 1, 2, 3, 1, 3, 1, 9, 4, 3, 1, 1, 2, 0, 9, 0, 5, 0, 5, 7, 1, 2, 0, 3, 4, 3, 2, 1, 2, 5, 9, 1]
occupancy_R_coords_json_heuristic_15 = [0, 0, 1, 1, 0, 1, 1, 2, 0, 0, 3, 5, 0, 2, 3, 3, 1, 1, 2, 3, 2, 3, 3, 0, 0, 2, 1, 1, 0, 3, 2, 0, 0, 0, 5, 1, 1, 4, 4, 1, 2, 1, 1, 0, 0, 2, 1, 0, 1, 1]
occupancy_R_coords_json_restart_15 = [0, 0, 3, 0, 1, 0, 4, 0, 1, 0, 0, 1, 2, 1, 2, 0, 1, 2, 2, 1, 1, 2, 0, 2, 1, 0, 2, 1, 3, 0, 0, 0, 2, 1, 2, 0, 0, 2, 1, 1, 1, 0, 1, 0, 2, 1, 1, 0, 1, 1]
occupancy_R_coords_json_reverse_search_15 = [0, 0, 2, 1, 0, 3, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 1, 3, 2, 1, 0, 2, 1, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1, 2, 0, 0, 1, 0, 1, 1, 0, 2, 3]
occupancy_R_coords_json_step_by_step_15 = [0, 0, 0, 7, 0, 3, 1, 0, 0, 0, 0, 0, 0, 18, 1, 0, 1, 15, 2, 2, 0, 0, 8, 31, 5, 3, 0, 0, 60, 91, 9, 0, 0, 6, 0, 0, 0, 0, 56, 0, 1, 1, 0, 0, 8, 0, 0, 11, 3, 1]
occupancy_R_coords_json_verification_15 = [3, 2, 3, 2, 2, 4, 4, 8, 3, 7, 3, 5, 3, 0, 1, 7, 8, 1, 4, 6, 7, 2, 2, 10, 8, 7, 10, 2, 9, 2, 2, 2, 9, 0, 4, 2, 3, 3, 3, 2, 7, 3, 5, 5, 4, 5, 4, 2, 8, 7]
occupancy_R_coords_tokenized_txt_algorithm_15 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2]
occupancy_R_coords_tokenized_txt_backtracking_15 = [4, 4, 6, 4, 2, 1, 1, 1, 9, 4, 7, 3, 9, 2, 2, 0, 1, 1, 2, 1, 3, 4, 7, 4, 5, 2, 2, 1, 1, 6, 3, 7, 5, 5, 6, 2, 2, 2, 12, 5, 7, 3, 4, 3, 4, 3, 2, 3, 4, 8]
occupancy_R_coords_tokenized_txt_false_confidence_15 = [1, 0, 1, 5, 4, 0, 0, 2, 3, 1, 0, 2, 1, 1, 6, 0, 0, 2, 5, 0, 1, 0, 1, 2, 3, 0, 0, 2, 2, 5, 5, 3, 1, 2, 1, 1, 2, 1, 0, 1, 1, 0, 3, 1, 0, 2, 1, 2, 4, 2]
occupancy_R_coords_tokenized_txt_frustration_15 = [3, 4, 2, 6, 1, 2, 5, 3, 8, 5, 5, 0, 13, 4, 1, 0, 0, 1, 1, 4, 1, 3, 1, 3, 2, 3, 0, 3, 2, 12, 5, 8, 2, 6, 3, 5, 3, 4, 11, 4, 1, 5, 0, 5, 2, 2, 3, 1, 1, 5]
occupancy_R_coords_tokenized_txt_heuristic_15 = [0, 1, 2, 0, 0, 1, 1, 2, 1, 0, 0, 2, 0, 2, 1, 0, 2, 0, 1, 1, 0, 1, 1, 2, 1, 2, 1, 1, 0, 0, 2, 2, 1, 0, 2, 3, 0, 1, 1, 1, 5, 3, 0, 1, 1, 0, 0, 1, 0, 2]
occupancy_R_coords_tokenized_txt_restart_15 = [0, 1, 1, 2, 1, 0, 1, 1, 1, 0, 1, 1, 4, 1, 1, 0, 2, 1, 1, 1, 1, 3, 3, 0, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 0, 3, 2, 1, 5, 4, 0, 1, 1, 3, 1, 2, 1, 2]
occupancy_R_coords_tokenized_txt_reverse_search_15 = [2, 0, 0, 0, 0, 0, 3, 0, 2, 3, 1, 0, 5, 2, 5, 0, 1, 3, 1, 1, 1, 2, 2, 4, 3, 0, 0, 0, 3, 3, 2, 6, 1, 7, 2, 1, 1, 2, 2, 3, 2, 0, 1, 3, 2, 3, 0, 2, 7, 0]
occupancy_R_coords_tokenized_txt_step_by_step_15 = [2, 1, 13, 0, 0, 23, 0, 1, 0, 1, 0, 0, 2, 101, 59, 0, 91, 2, 0, 0, 34, 0, 29, 4, 1, 99, 5, 0, 0, 2, 1, 1, 1, 1, 11, 1, 67, 43, 2, 1, 42, 42, 90, 1, 5, 2, 6, 0, 2, 0]
occupancy_R_coords_tokenized_txt_verification_15 = [3, 3, 4, 6, 3, 0, 3, 3, 6, 0, 4, 7, 3, 3, 3, 0, 2, 5, 2, 1, 3, 2, 3, 3, 5, 1, 5, 2, 4, 2, 4, 4, 0, 3, 6, 1, 2, 5, 2, 9, 7, 4, 2, 1, 0, 5, 7, 8, 5, 8]


occurrences_binary_line_tokenized_algorithm_15 = binary_occurrence(line_R_coords_tokenized_txt_algorithm_15)
occurrences_binary_line_tokenized_heuristic_15 = binary_occurrence(line_R_coords_tokenized_txt_heuristic_15)
occurrences_binary_line_tokenized_backtracking_15 = binary_occurrence(line_R_coords_tokenized_txt_backtracking_15)
occurrences_binary_line_tokenized_false_confidence_15 = binary_occurrence(line_R_coords_tokenized_txt_false_confidence_15)
occurrences_binary_line_tokenized_frustration_15 = binary_occurrence(line_R_coords_tokenized_txt_frustration_15)
occurrences_binary_line_tokenized_restart_15 = binary_occurrence(line_R_coords_tokenized_txt_restart_15)
occurrences_binary_line_tokenized_reverse_search_15 = binary_occurrence(line_R_coords_tokenized_txt_reverse_search_15)
occurrences_binary_line_tokenized_step_by_step_15 = binary_occurrence(line_R_coords_tokenized_txt_step_by_step_15)
occurrences_binary_line_tokenized_verification_15 = binary_occurrence(line_R_coords_tokenized_txt_verification_15)

occurrences_binary_line_adj_json_algorithm_15 = binary_occurrence(line_R_coords_adj_json_algorithm_15)
occurrences_binary_line_adj_json_heuristic_15 = binary_occurrence(line_R_coords_adj_json_heuristic_15)
occurrences_binary_line_adj_json_backtracking_15 = binary_occurrence(line_R_coords_adj_json_backtracking_15)
occurrences_binary_line_adj_json_false_confidence_15 = binary_occurrence(line_R_coords_adj_json_false_confidence_15)
occurrences_binary_line_adj_json_frustration_15 = binary_occurrence(line_R_coords_adj_json_frustration_15)
occurrences_binary_line_adj_json_restart_15 = binary_occurrence(line_R_coords_adj_json_restart_15)
occurrences_binary_line_adj_json_reverse_search_15 = binary_occurrence(line_R_coords_adj_json_reverse_search_15)
occurrences_binary_line_adj_json_step_by_step_15 = binary_occurrence(line_R_coords_adj_json_step_by_step_15)
occurrences_binary_line_adj_json_verification_15 = binary_occurrence(line_R_coords_adj_json_verification_15)

occurrences_binary_line_adj_txt_algorithm_15 = binary_occurrence(line_R_coords_adj_txt_algorithm_15)
occurrences_binary_line_adj_txt_heuristic_15 = binary_occurrence(line_R_coords_adj_txt_heuristic_15)
occurrences_binary_line_adj_txt_backtracking_15 = binary_occurrence(line_R_coords_adj_txt_backtracking_15)
occurrences_binary_line_adj_txt_false_confidence_15 = binary_occurrence(line_R_coords_adj_txt_false_confidence_15)
occurrences_binary_line_adj_txt_frustration_15 = binary_occurrence(line_R_coords_adj_txt_frustration_15)
occurrences_binary_line_adj_txt_restart_15 = binary_occurrence(line_R_coords_adj_txt_restart_15)
occurrences_binary_line_adj_txt_reverse_search_15 = binary_occurrence(line_R_coords_adj_txt_reverse_search_15)
occurrences_binary_line_adj_txt_step_by_step_15 = binary_occurrence(line_R_coords_adj_txt_step_by_step_15)
occurrences_binary_line_adj_txt_verification_15 = binary_occurrence(line_R_coords_adj_txt_verification_15)

occurrences_binary_line_jpg_algorithm_15 = binary_occurrence(line_R_coords_jpg_algorithm_15)
occurrences_binary_line_jpg_heuristic_15 = binary_occurrence(line_R_coords_jpg_heuristic_15)
occurrences_binary_line_jpg_backtracking_15 = binary_occurrence(line_R_coords_jpg_backtracking_15)
occurrences_binary_line_jpg_false_confidence_15 = binary_occurrence(line_R_coords_jpg_false_confidence_15)
occurrences_binary_line_jpg_frustration_15 = binary_occurrence(line_R_coords_jpg_frustration_15)
occurrences_binary_line_jpg_restart_15 = binary_occurrence(line_R_coords_jpg_restart_15)
occurrences_binary_line_jpg_reverse_search_15 = binary_occurrence(line_R_coords_jpg_reverse_search_15)
occurrences_binary_line_jpg_step_by_step_15 = binary_occurrence(line_R_coords_jpg_step_by_step_15)
occurrences_binary_line_jpg_verification_15 = binary_occurrence(line_R_coords_jpg_verification_15)

occurrences_binary_line_json_algorithm_15 = binary_occurrence(line_R_coords_json_algorithm_15)
occurrences_binary_line_json_heuristic_15 = binary_occurrence(line_R_coords_json_heuristic_15)
occurrences_binary_line_json_backtracking_15 = binary_occurrence(line_R_coords_json_backtracking_15)
occurrences_binary_line_json_false_confidence_15 = binary_occurrence(line_R_coords_json_false_confidence_15)
occurrences_binary_line_json_frustration_15 = binary_occurrence(line_R_coords_json_frustration_15)
occurrences_binary_line_json_restart_15 = binary_occurrence(line_R_coords_json_restart_15)
occurrences_binary_line_json_reverse_search_15 = binary_occurrence(line_R_coords_json_reverse_search_15)
occurrences_binary_line_json_step_by_step_15 = binary_occurrence(line_R_coords_json_step_by_step_15)
occurrences_binary_line_json_verification_15 = binary_occurrence(line_R_coords_json_verification_15)

occurrences_binary_occupancy_adj_json_algorithm_15 = binary_occurrence(occupancy_R_coords_adj_json_algorithm_15)
occurrences_binary_occupancy_adj_json_heuristic_15 = binary_occurrence(occupancy_R_coords_adj_json_heuristic_15)
occurrences_binary_occupancy_adj_json_backtracking_15 = binary_occurrence(occupancy_R_coords_adj_json_backtracking_15)
occurrences_binary_occupancy_adj_json_false_confidence_15 = binary_occurrence(occupancy_R_coords_adj_json_false_confidence_15)
occurrences_binary_occupancy_adj_json_frustration_15 = binary_occurrence(occupancy_R_coords_adj_json_frustration_15)
occurrences_binary_occupancy_adj_json_restart_15 = binary_occurrence(occupancy_R_coords_adj_json_restart_15)
occurrences_binary_occupancy_adj_json_reverse_search_15 = binary_occurrence(occupancy_R_coords_adj_json_reverse_search_15)
occurrences_binary_occupancy_adj_json_step_by_step_15 = binary_occurrence(occupancy_R_coords_adj_json_step_by_step_15)
occurrences_binary_occupancy_adj_json_verification_15 = binary_occurrence(occupancy_R_coords_adj_json_verification_15)

occurrences_binary_occupancy_adj_txt_algorithm_15 = binary_occurrence(occupancy_R_coords_adj_txt_algorithm_15)
occurrences_binary_occupancy_adj_txt_heuristic_15 = binary_occurrence(occupancy_R_coords_adj_txt_heuristic_15)
occurrences_binary_occupancy_adj_txt_backtracking_15 = binary_occurrence(occupancy_R_coords_adj_txt_backtracking_15)
occurrences_binary_occupancy_adj_txt_false_confidence_15 = binary_occurrence(occupancy_R_coords_adj_txt_false_confidence_15)
occurrences_binary_occupancy_adj_txt_frustration_15 = binary_occurrence(occupancy_R_coords_adj_txt_frustration_15)
occurrences_binary_occupancy_adj_txt_restart_15 = binary_occurrence(occupancy_R_coords_adj_txt_restart_15)
occurrences_binary_occupancy_adj_txt_reverse_search_15 = binary_occurrence(occupancy_R_coords_adj_txt_reverse_search_15)
occurrences_binary_occupancy_adj_txt_step_by_step_15 = binary_occurrence(occupancy_R_coords_adj_txt_step_by_step_15)
occurrences_binary_occupancy_adj_txt_verification_15 = binary_occurrence(occupancy_R_coords_adj_txt_verification_15)

occurrences_binary_occupancy_json_algorithm_15 = binary_occurrence(occupancy_R_coords_json_algorithm_15)
occurrences_binary_occupancy_json_heuristic_15 = binary_occurrence(occupancy_R_coords_json_heuristic_15)
occurrences_binary_occupancy_json_backtracking_15 = binary_occurrence(occupancy_R_coords_json_backtracking_15)
occurrences_binary_occupancy_json_false_confidence_15 = binary_occurrence(occupancy_R_coords_json_false_confidence_15)
occurrences_binary_occupancy_json_frustration_15 = binary_occurrence(occupancy_R_coords_json_frustration_15)
occurrences_binary_occupancy_json_restart_15 = binary_occurrence(occupancy_R_coords_json_restart_15)
occurrences_binary_occupancy_json_reverse_search_15 = binary_occurrence(occupancy_R_coords_json_reverse_search_15)
occurrences_binary_occupancy_json_step_by_step_15 = binary_occurrence(occupancy_R_coords_json_step_by_step_15)
occurrences_binary_occupancy_json_verification_15 = binary_occurrence(occupancy_R_coords_json_verification_15)

occurrences_binary_occupancy_tokenized_algorithm_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_algorithm_15)
occurrences_binary_occupancy_tokenized_heuristic_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_heuristic_15)
occurrences_binary_occupancy_tokenized_backtracking_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_backtracking_15)
occurrences_binary_occupancy_tokenized_false_confidence_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_false_confidence_15)
occurrences_binary_occupancy_tokenized_frustration_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_frustration_15)
occurrences_binary_occupancy_tokenized_restart_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_restart_15)
occurrences_binary_occupancy_tokenized_reverse_search_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_reverse_search_15)
occurrences_binary_occupancy_tokenized_step_by_step_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_step_by_step_15)
occurrences_binary_occupancy_tokenized_verification_15 = binary_occurrence(occupancy_R_coords_tokenized_txt_verification_15)

occurrences_binary_occupancy_ascii_algorithm_15 = binary_occurrence(occupancy_R_coords_ascii_txt_algorithm_15)
occurrences_binary_occupancy_ascii_heuristic_15 = binary_occurrence(occupancy_R_coords_ascii_txt_heuristic_15)
occurrences_binary_occupancy_ascii_backtracking_15 = binary_occurrence(occupancy_R_coords_ascii_txt_backtracking_15)
occurrences_binary_occupancy_ascii_false_confidence_15 = binary_occurrence(occupancy_R_coords_ascii_txt_false_confidence_15)
occurrences_binary_occupancy_ascii_frustration_15 = binary_occurrence(occupancy_R_coords_ascii_txt_frustration_15)
occurrences_binary_occupancy_ascii_restart_15 = binary_occurrence(occupancy_R_coords_ascii_txt_restart_15)
occurrences_binary_occupancy_ascii_reverse_search_15 = binary_occurrence(occupancy_R_coords_ascii_txt_reverse_search_15)
occurrences_binary_occupancy_ascii_step_by_step_15 = binary_occurrence(occupancy_R_coords_ascii_txt_step_by_step_15)
occurrences_binary_occupancy_ascii_verification_15 = binary_occurrence(occupancy_R_coords_ascii_txt_verification_15)

occurrences_binary_occupancy_jpg_algorithm_15 = binary_occurrence(occupancy_R_coords_jpg_algorithm_15)
occurrences_binary_occupancy_jpg_heuristic_15 = binary_occurrence(occupancy_R_coords_jpg_heuristic_15)
occurrences_binary_occupancy_jpg_backtracking_15 = binary_occurrence(occupancy_R_coords_jpg_backtracking_15)
occurrences_binary_occupancy_jpg_false_confidence_15 = binary_occurrence(occupancy_R_coords_jpg_false_confidence_15)
occurrences_binary_occupancy_jpg_frustration_15 = binary_occurrence(occupancy_R_coords_jpg_frustration_15)
occurrences_binary_occupancy_jpg_restart_15 = binary_occurrence(occupancy_R_coords_jpg_restart_15)
occurrences_binary_occupancy_jpg_reverse_search_15 = binary_occurrence(occupancy_R_coords_jpg_reverse_search_15)
occurrences_binary_occupancy_jpg_step_by_step_15 = binary_occurrence(occupancy_R_coords_jpg_step_by_step_15)
occurrences_binary_occupancy_jpg_verification_15 = binary_occurrence(occupancy_R_coords_jpg_verification_15)



# creating heatmap: presence vs score for all inputs

score_vectors = [
    r15.line_R_coords_adj_json_15,
    r15.line_R_coords_adj_txt_15,
    r15.line_R_coords_jpg_15,
    r15.line_R_coords_json_15,
    r15.line_R_coords_tokenized_txt_15,
    r15.occupancy_R_coords_adj_json_15,
    r15.occupancy_R_coords_adj_txt_15,
    r15.occupancy_R_coords_jpg_15,
    r15.occupancy_R_coords_json_15,
    r15.occupancy_R_coords_tokenized_txt_15,
    r15.occupancy_R_coords_ascii_txt_15
]

binary_occurrence_vectors_false_confidence = [
    occurrences_binary_line_adj_json_false_confidence_15,
    occurrences_binary_line_adj_txt_false_confidence_15,
    occurrences_binary_line_jpg_false_confidence_15,
    occurrences_binary_line_json_false_confidence_15,
    occurrences_binary_line_tokenized_false_confidence_15,
    occurrences_binary_occupancy_adj_json_false_confidence_15,
    occurrences_binary_occupancy_adj_txt_false_confidence_15,
    occurrences_binary_occupancy_jpg_false_confidence_15,
    occurrences_binary_occupancy_json_false_confidence_15,
    occurrences_binary_occupancy_tokenized_false_confidence_15,
    occurrences_binary_occupancy_ascii_false_confidence_15
    ]

binary_occurrence_vectors_heuristic = [
    occurrences_binary_line_adj_json_heuristic_15,
    occurrences_binary_line_adj_txt_heuristic_15,
    occurrences_binary_line_jpg_heuristic_15,
    occurrences_binary_line_json_heuristic_15,
    occurrences_binary_line_tokenized_heuristic_15,
    occurrences_binary_occupancy_adj_json_heuristic_15,
    occurrences_binary_occupancy_adj_txt_heuristic_15,
    occurrences_binary_occupancy_jpg_heuristic_15,
    occurrences_binary_occupancy_json_heuristic_15,
    occurrences_binary_occupancy_tokenized_heuristic_15,
    occurrences_binary_occupancy_ascii_heuristic_15
    ]



binary_occurrence_vectors_verification = [
    occurrences_binary_line_adj_json_verification_15,
    occurrences_binary_line_adj_txt_verification_15,
    occurrences_binary_line_jpg_verification_15,
    occurrences_binary_line_json_verification_15,
    occurrences_binary_line_tokenized_verification_15,
    occurrences_binary_occupancy_adj_json_verification_15,
    occurrences_binary_occupancy_adj_txt_verification_15,
    occurrences_binary_occupancy_jpg_verification_15,
    occurrences_binary_occupancy_json_verification_15,
    occurrences_binary_occupancy_tokenized_verification_15,
    occurrences_binary_occupancy_ascii_verification_15
    ]

binary_occurrence_vectors_frustration = [
    occurrences_binary_line_adj_json_frustration_15,
    occurrences_binary_line_adj_txt_frustration_15,
    occurrences_binary_line_jpg_frustration_15,
    occurrences_binary_line_json_frustration_15,
    occurrences_binary_line_tokenized_frustration_15,
    occurrences_binary_occupancy_adj_json_frustration_15,
    occurrences_binary_occupancy_adj_txt_frustration_15,
    occurrences_binary_occupancy_jpg_frustration_15,
    occurrences_binary_occupancy_json_frustration_15,
    occurrences_binary_occupancy_tokenized_frustration_15,
    occurrences_binary_occupancy_ascii_frustration_15
    ]

binary_occurrence_vectors_step_by_step = [
    occurrences_binary_line_adj_json_step_by_step_15,
    occurrences_binary_line_adj_txt_step_by_step_15,
    occurrences_binary_line_jpg_step_by_step_15,
    occurrences_binary_line_json_step_by_step_15,
    occurrences_binary_line_tokenized_step_by_step_15,
    occurrences_binary_occupancy_adj_json_step_by_step_15,
    occurrences_binary_occupancy_adj_txt_step_by_step_15,
    occurrences_binary_occupancy_jpg_step_by_step_15,
    occurrences_binary_occupancy_json_step_by_step_15,
    occurrences_binary_occupancy_tokenized_step_by_step_15,
    occurrences_binary_occupancy_ascii_step_by_step_15
    ]

binary_occurrence_vectors_backtracking = [
    occurrences_binary_line_adj_json_backtracking_15,
    occurrences_binary_line_adj_txt_backtracking_15,
    occurrences_binary_line_jpg_backtracking_15,
    occurrences_binary_line_json_backtracking_15,
    occurrences_binary_line_tokenized_backtracking_15,
    occurrences_binary_occupancy_adj_json_backtracking_15,
    occurrences_binary_occupancy_adj_txt_backtracking_15,
    occurrences_binary_occupancy_jpg_backtracking_15,
    occurrences_binary_occupancy_json_backtracking_15,
    occurrences_binary_occupancy_tokenized_backtracking_15,
    occurrences_binary_occupancy_ascii_backtracking_15
    ]

binary_occurrence_vectors_algo = [
    occurrences_binary_line_adj_json_algorithm_15,
    occurrences_binary_line_adj_txt_algorithm_15,
    occurrences_binary_line_jpg_algorithm_15,
    occurrences_binary_line_json_algorithm_15,
    occurrences_binary_line_tokenized_algorithm_15,
    occurrences_binary_occupancy_adj_json_algorithm_15,
    occurrences_binary_occupancy_adj_txt_algorithm_15,
    occurrences_binary_occupancy_jpg_algorithm_15,
    occurrences_binary_occupancy_json_algorithm_15,
    occurrences_binary_occupancy_tokenized_algorithm_15,
    occurrences_binary_occupancy_ascii_algorithm_15
    ]

binary_occurrence_vectors_restart = [
    occurrences_binary_line_adj_json_restart_15,
    occurrences_binary_line_adj_txt_restart_15,
    occurrences_binary_line_jpg_restart_15,
    occurrences_binary_line_json_restart_15,
    occurrences_binary_line_tokenized_restart_15,
    occurrences_binary_occupancy_adj_json_restart_15,
    occurrences_binary_occupancy_adj_txt_restart_15,
    occurrences_binary_occupancy_jpg_restart_15,
    occurrences_binary_occupancy_json_restart_15,
    occurrences_binary_occupancy_tokenized_restart_15,
    occurrences_binary_occupancy_ascii_restart_15
    ]

binary_occurrence_vectors_reverse_search = [
    occurrences_binary_line_adj_json_reverse_search_15,
    occurrences_binary_line_adj_txt_reverse_search_15,
    occurrences_binary_line_jpg_reverse_search_15,
    occurrences_binary_line_json_reverse_search_15,
    occurrences_binary_line_tokenized_reverse_search_15,
    occurrences_binary_occupancy_adj_json_reverse_search_15,
    occurrences_binary_occupancy_adj_txt_reverse_search_15,
    occurrences_binary_occupancy_jpg_reverse_search_15,
    occurrences_binary_occupancy_json_reverse_search_15,
    occurrences_binary_occupancy_tokenized_reverse_search_15,
    occurrences_binary_occupancy_ascii_reverse_search_15
    ]

labels = [
    "Line Adj JSON",
    "Line Adj Txt",
    "Line JPG",
    "Line JSON",
    "Line Tokenized",
    "Occ Adj JSON",
    "Occ Adj Txt",
    "Occ JPG",
    "Occ JSON",
    "Occ Tokenized",
    "Occ ASCII"
]





# plotting 1 fig with 8 subplots that show occurrence vs completion score - most useful graphic
# List of (occurrence_vector, score_vector, label)
datasets_algorithm = [
    (occurrences_binary_line_adj_json_algorithm_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_algorithm_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_algorithm_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_algorithm_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_algorithm_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_algorithm_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_algorithm_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_algorithm_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_algorithm_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_algorithm_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_algorithm_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]

# List of (occurrence_vector, score_vector, label)
datasets_heuristic = [
    (occurrences_binary_line_adj_json_heuristic_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_heuristic_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_heuristic_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_heuristic_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_heuristic_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_heuristic_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_heuristic_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_heuristic_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_heuristic_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_heuristic_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_heuristic_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]

# List of (occurrence_vector, score_vector, label)
datasets_backtracking = [
    (occurrences_binary_line_adj_json_backtracking_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_backtracking_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_backtracking_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_backtracking_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_backtracking_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_backtracking_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_backtracking_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_backtracking_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_backtracking_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_backtracking_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_backtracking_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]


# List of (occurrence_vector, score_vector, label)
datasets_false_confidence = [
    (occurrences_binary_line_adj_json_false_confidence_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_false_confidence_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_false_confidence_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_false_confidence_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_false_confidence_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_false_confidence_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_false_confidence_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_false_confidence_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_false_confidence_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_false_confidence_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_false_confidence_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]


# List of (occurrence_vector, score_vector, label)
datasets_frustration = [
    (occurrences_binary_line_adj_json_frustration_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_frustration_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_frustration_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_frustration_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_frustration_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_frustration_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_frustration_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_frustration_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_frustration_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_frustration_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_frustration_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]

# List of (occurrence_vector, score_vector, label)
datasets_restart = [
    (occurrences_binary_line_adj_json_restart_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_restart_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_restart_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_restart_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_restart_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_restart_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_restart_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_restart_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_restart_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_restart_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_restart_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]


# List of (occurrence_vector, score_vector, label)
datasets_reverse_search = [
    (occurrences_binary_line_adj_json_reverse_search_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_reverse_search_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_reverse_search_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_reverse_search_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_reverse_search_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_reverse_search_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_reverse_search_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_reverse_search_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_reverse_search_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_reverse_search_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_reverse_search_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]


# List of (occurrence_vector, score_vector, label)
datasets_step_by_step = [
    (occurrences_binary_line_adj_json_step_by_step_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_step_by_step_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_step_by_step_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_step_by_step_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_step_by_step_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_step_by_step_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_step_by_step_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_step_by_step_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_step_by_step_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_step_by_step_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple', 'v'),
    (occurrences_binary_occupancy_ascii_step_by_step_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]

# List of (occurrence_vector, score_vector, label)
datasets_verification = [
    (occurrences_binary_line_adj_json_verification_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', 'o'),
    (occurrences_binary_line_adj_txt_verification_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', 'o'),
    (occurrences_binary_line_json_verification_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', 'o'),
    (occurrences_binary_line_jpg_verification_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', 'o'),
    (occurrences_binary_line_tokenized_verification_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', 'o'),
    (occurrences_binary_occupancy_adj_json_verification_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'v'),
    (occurrences_binary_occupancy_adj_txt_verification_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'v'),
    (occurrences_binary_occupancy_json_verification_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'v'),
    (occurrences_binary_occupancy_jpg_verification_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'v'),
    (occurrences_binary_occupancy_tokenized_verification_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'v'),
    (occurrences_binary_occupancy_ascii_verification_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'v'),
]





def plot_keyword(ax, datasets, title, ylabel):

    x_vals = []
    y_vals = []

    for occurrence_vector, score_vector, label, color, marker in datasets:

        # Make sure they are np arrays
        occurrence_vector = np.array(occurrence_vector)
        score_vector = np.array(score_vector)
        
        # Calculate mean presence and mean score for this dataset
        y_sum = np.mean(occurrence_vector) * 100 # the mean of the number of times the keywords are present * 100 yields the percentage of presence across all runs
        x_mean = np.mean(score_vector)

        x_vals.append(x_mean)
        y_vals.append(y_sum)

        ax.scatter(
            x_mean,
            y_sum,
            color=color,
            marker=marker,
            s=60,
            label=label
        )

    x_vals = np.array(x_vals)
    y_vals = np.array(y_vals)

    # Trend line
    z = np.polyfit(x_vals, y_vals, 1)
    p = np.poly1d(z)

    sorted_idx = np.argsort(x_vals)

    ax.plot(
        x_vals[sorted_idx],
        p(x_vals[sorted_idx]),
        linestyle='--',
        color='black',
        alpha=0.7
    )

    # set subfigure titles and x-ylabels for each individual subplot
    ax.set_title(title, fontweight = 'bold', fontsize=10)
    # ax.set_xlabel('Mean Completion Score (%)')
    # ax.set_ylabel(ylabel)
    ax.grid(linestyle=':', alpha=0.6)


# Create 2x4 subplot grid (8 total)
fig, axes = plt.subplots(2, 5, figsize=(22, 8))
axes = axes.flatten()

# Set 1 common x-y label for the entire figure
fig.supxlabel('Mean Completion Score (%)', fontsize = 12)
fig.supylabel('Keyword Presence (%)', fontsize = 12)

plot_keyword(axes[0], datasets_algorithm, "Algorithm",  "Presence (%)")
plot_keyword(axes[1], datasets_heuristic, "Heuristics", "Presence (%)")
plot_keyword(axes[2], datasets_backtracking, "Backtracking", "Presence (%)")
plot_keyword(axes[3], datasets_false_confidence, "False Confidence", "Presence (%)")
plot_keyword(axes[4], datasets_frustration, "Frustration", "Presence (%)")
plot_keyword(axes[5], datasets_restart, "Restart", "Presence (%)")
plot_keyword(axes[6], datasets_reverse_search, "Reverse Search", "Presence (%)")
plot_keyword(axes[7], datasets_step_by_step, "Step-by-Step", "Presence (%)")
plot_keyword(axes[8], datasets_verification, "Verification", "Presence (%)")


# Make a legend
# specify colors
colors = ['tab:blue', 'tab:orange', 'tab:red', 'tab:green', 'tab:purple', 'tab:brown']

# --- Design Legend Group Markers ---
spacer_handle = (
Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
line_handle = (
Line2D([], [], marker='o', color='grey', linestyle = 'none'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
),
occupancy_handle = (
Line2D([], [], marker='v', color='grey', linestyle = 'none'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
)

# Create legend order with spacers for grouping
handles = [
spacer_handle,
line_handle,
occupancy_handle,
spacer_handle,

Line2D([], [], marker='s', color=colors[0], linestyle='None', markersize = 10),  # Adjacency JSON
Line2D([], [], marker='s', color=colors[1], linestyle='None', markersize = 10),  # Adjacency Text
Line2D([], [], marker='s', color=colors[3], linestyle='None', markersize = 10),  # JSON
Line2D([], [], marker='s', color=colors[2], linestyle='None', markersize = 10),  # JPG
Line2D([], [], marker='s', color=colors[4], linestyle='None', markersize = 10),  # Tokenized
Line2D([], [], marker='s', color=colors[5], linestyle='None', markersize = 10),  # ASCII

]

# Add labels to the markers
labels = [
r"$\bf{Input\ Maze\ Style}$",
"Line", "Occupancy",
r"$\bf{Input\ Formats}$",
"Adjacency JSON", "Adjacency Text", "JPG", "JSON", "Tokenized", "ASCII"
]
# axes[3].legend(
# handles,
# labels,
# handler_map={tuple: HandlerTuple(ndivide=None)},
# loc='center left',
# bbox_to_anchor=(1.02, 0.5),
# title="Legend"
# )

axes[9].axis("off")

axes[9].legend(
    handles,
    labels,
    handler_map={tuple: HandlerTuple(ndivide=None)},
    loc="center",
    title="Legend",
    frameon=True
)

plt.suptitle(' Presence of Each Keyword Category vs Completion Score \nGemini 2.5 Pro, Coordinates Output, 15x15/31x31', fontsize=14)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout(rect=[0.03, 0, 0.97, 0.95])
plt.show()








# ---------------------------- Charts about ground truth solution length ---------------------------------------

# solution lenghts of line coords 15x15 1-50
sol_lengths  = [131, 69, 139, 57, 127, 101, 67, 79, 133, 47, 91, 85, 129, 65, 81, 123, 91, 93, 49, 
                133, 115, 75, 53, 121, 39, 51, 105, 69, 67, 147, 85, 65, 95, 61, 83, 131,87, 81, 49,
                119, 143, 139, 71, 53, 101, 125, 143, 113, 75,73]
# completion scores 
scores  = np.array(r15.line_R_coords_adj_txt_15)
#raw scores
raw= r15.line_R_coords_adj_txt_raw_score_15

#empty lists
scores_high_sol = []
scores_mid_sol = []
scores_low_sol = []
rawscores_high_sol = []
rawscores_mid_sol = []
rawscores_low_sol = []


# Fill the lists according to low-medium-high number of ground truth steps
boundaries=[70,120] # these are the boundaries for low-med-high
for i in range(len(scores)):
    if sol_lengths[i] >= boundaries[1]:
        scores_high_sol.append(scores[i])
        rawscores_high_sol.append(raw[i])
    elif sol_lengths[i]<= boundaries[0]:
        scores_low_sol.append(scores[i])
        rawscores_low_sol.append(raw[i])
    else:
        scores_mid_sol.append(scores[i])
        rawscores_mid_sol.append(raw[i])

#make lists into arrays
scores_high_sol = np.array(scores_high_sol)
scores_mid_sol = np.array(scores_mid_sol)
scores_low_sol = np.array(scores_low_sol)
rawscores_high_sol = np.array(rawscores_high_sol)
rawscores_mid_sol = np.array(rawscores_mid_sol)
rawscores_low_sol = np.array(rawscores_low_sol)

#print values
print('high', scores_high_sol, '\n')
print('mid', scores_mid_sol, '\n')
print('low', scores_low_sol, '\n')
print('raw high', rawscores_high_sol, '\n')
print('raw mid', rawscores_mid_sol, '\n')
print('raw low', rawscores_low_sol, '\n')
print('mean high', np.mean(scores_high_sol), '\n')
print('mean mid', np.mean(scores_mid_sol), '\n')
print('mean low', np.mean(scores_low_sol), '\n')
print('raw mean high', np.mean(rawscores_high_sol), '\n')
print('raw mean mid', np.mean(rawscores_mid_sol), '\n')
print('raw mean low', np.mean(rawscores_low_sol), '\n')


# put the means and boundaries into lists so they can be plot
middle_of_low_area = (min(sol_lengths)+boundaries[0])/2
middle_of_high_area = (boundaries[1]+max(sol_lengths))/2
middle_of_mid_area = (boundaries[0]+boundaries[1])/2
complexity_mean_scores = [np.mean(scores_low_sol),np.mean(scores_mid_sol),np.mean(scores_high_sol)]
complexity_solution_categories = [middle_of_low_area, middle_of_mid_area, middle_of_high_area]
rawcomplexity_mean_scores = [np.mean(rawscores_low_sol),np.mean(rawscores_mid_sol),np.mean(rawscores_high_sol)]
rawcomplexity_solution_categories = [middle_of_low_area, middle_of_mid_area, middle_of_high_area]

# plotting completion score vs ground truth solution length
plt.figure(1)
plt.scatter(scores, sol_lengths)
plt.scatter(complexity_mean_scores, complexity_solution_categories)
# Fit linear trend line
z = np.polyfit(scores, sol_lengths, 2)   # 1 = linear
p = np.poly1d(z)

# Plot trend line
x_line = np.linspace(min(scores), max(scores), 100)
plt.plot(x_line, p(x_line), linestyle='--')
plt.xlabel('Score (%)')
plt.ylabel('Solution Length (cells)')
plt.title('Solution Length vs. Score')
plt.grid()
# plt.show()


#plotting raw steps vs ground truth solution length
plt.figure(2)
plt.scatter(sol_lengths, raw)
plt.scatter(rawcomplexity_solution_categories, rawcomplexity_mean_scores)

# Fit linear trend line to the mean scores, NOT all the data
z = np.polyfit(rawcomplexity_solution_categories,rawcomplexity_mean_scores,  2)   # 1 = linear
p = np.poly1d(z)

# Plot trend line
x_line = np.linspace(min(rawcomplexity_solution_categories), max(rawcomplexity_solution_categories), 400)
plt.plot(x_line, p(x_line), linestyle='--')

#shade regions
plt.axvspan(20, 70, color='green', alpha=0.2)
plt.axvspan(70, 120, color='orange', alpha=0.2)
plt.axvspan(120, max(sol_lengths)+20, color='red', alpha=0.2)
#plot category barriers
plt.axvline(x=70, linestyle='-', color='grey')
plt.axvline(x=120, linestyle='-', color='grey')



# --- Design Legend Group Markers ---
spacer_handle = (
Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
mean_handle = (
Line2D([], [], marker='o', color='tab:orange', linestyle = 'none'),
),
datapoint_handle = (
Line2D([], [], marker='o', color='tab:blue', linestyle = 'none'),
),


# Create legend order with spacers for grouping
handles = [
mean_handle,
datapoint_handle
]

# Add labels to the markers
labels = [
"Mean correct nr. of steps\n within maze difficulty", "datapoint",

]


plt.legend(
    handles,
    labels,
    handler_map={tuple: HandlerTuple(ndivide=None)},
    loc="lower right",
    title="Legend",
    frameon=True
)





plt.ylabel('Number of Correct Consecutive Steps')
plt.xlabel('Ground Truth Solution Length')
plt.suptitle('Maze Difficulty Based On Ground Truth Solution Length', fontweight='bold')
plt.title('15x15, Coordinates output, Line Adjacency Txt input, n=50')
plt.grid()


plt.show()














# Heatmap of score distribution in the case that keyword is present. 
# bins = np.arange(0, 105, 5)   # 0,5,10,...,100
# bin_labels = [f"{i}-{i+5}" for i in range(0, 100, 5)]


# heatmap_matrix = np.zeros((20, len(score_vectors)))

# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_algo)): # change input vectors here to decide which keyword heatmap to plot. 

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges"
# )

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When Algorithm Naming Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()
# # plt.show()




# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_restart)):

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges",

    
# )

# # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When Restart Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()
# # plt.show()





# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_false_confidence)):

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges",

    
# )

# # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When False Confidence Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()



# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_verification)):

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges",

    
# )

# # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When Verification Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()





# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_frustration)):

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges",

    
# )

# # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When Frustration Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()



# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_backtracking)):

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges",

    
# )

# # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When Backtracking Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()




# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_step_by_step)):

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges",

    
# )

# # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When Step by Step Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()


# for col, (scores, occurrences) in enumerate(zip(score_vectors, binary_occurrence_vectors_reverse_search)):

#     # Make sure the scores and occurrences are np arrays
#     scores = np.array(scores)
#     occurrences = np.array(occurrences)

#     # Only keep scores where keyword is present
#     present_scores = scores[occurrences == 1]

#     if len(present_scores) == 0:
#         continue  # column remains zero

#     # Histogram counts per bin
#     counts, _ = np.histogram(present_scores, bins=bins)

#     # Convert to percentage of keyword-present events
#     percentages = (counts / len(present_scores)) * 100

#     heatmap_matrix[:, col] = percentages

# plt.figure(figsize=(12, 8))

# im = plt.imshow(
#     heatmap_matrix,
#     aspect='auto',
#     origin='lower' ,
#     cmap="Oranges",

    
# )

# # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

# plt.colorbar(im, label='Percentage of Keyword-Present Events (%)')

# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45, ha='right')
# plt.yticks(ticks=np.arange(20), labels=bin_labels)

# plt.xlabel("Dataset")
# plt.ylabel("Completion Score (%)")
# plt.title("Distribution of Scores When Reverse Search Keywords Are Present, \nCoordinates Output, 15x15/31x31", fontweight='bold')

# # annotate the cells with the percentage values of keyword-present events (only non-zero)
# for i in range(heatmap_matrix.shape[0]):      # rows (bins)
#     for j in range(heatmap_matrix.shape[1]):  # columns (datasets)

#         value = heatmap_matrix[i, j]

#         if value > 0:   # only write non-zero cells (cleaner)
#             plt.text(
#                 j, i,
#                 f"{value:.0f}%",
#                 ha='center',
#                 va='center',
#                 color='white' if value > 50 else 'black',
#                 fontsize=8
#             )

# plt.tight_layout()
# plt.show()























# plotting 1 fig with 8 subplots that show occurrence normalized for number of reasoning tokens vs completion score  - Not so useful,
# results are a bit skewed by the fact that some inputs have more reasoning tokens and thus more chances for keywords. 
# List of (occurrence_vector, reasoning tokens, score_vector, label)
# datasets_algorithm = [
#     (occurrences_binary_line_adj_json_algorithm_15, r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_algorithm_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_algorithm_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_algorithm_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_algorithm_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_algorithm_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_algorithm_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_algorithm_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_algorithm_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_algorithm_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_algorithm_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]

# # List of (occurrence_vector, score_vector, label)
# datasets_backtracking = [
#     (occurrences_binary_line_adj_json_backtracking_15, r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_backtracking_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_backtracking_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_backtracking_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_backtracking_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_backtracking_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_backtracking_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_backtracking_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_backtracking_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_backtracking_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_backtracking_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]


# # List of (occurrence_vector, score_vector, label)
# datasets_false_confidence = [
#     (occurrences_binary_line_adj_json_false_confidence_15,  r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_false_confidence_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_false_confidence_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_false_confidence_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_false_confidence_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_false_confidence_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_false_confidence_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_false_confidence_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_false_confidence_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_false_confidence_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_false_confidence_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]


# # List of (occurrence_vector, score_vector, label)
# datasets_frustration = [
#     (occurrences_binary_line_adj_json_frustration_15, r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_frustration_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_frustration_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_frustration_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_frustration_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_frustration_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_frustration_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_frustration_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_frustration_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_frustration_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_frustration_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]

# # List of (occurrence_vector, score_vector, label)
# datasets_restart = [
#     (occurrences_binary_line_adj_json_restart_15, r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_restart_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_restart_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_restart_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_restart_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_restart_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_restart_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_restart_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_restart_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_restart_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_restart_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]


# # List of (occurrence_vector, score_vector, label)
# datasets_reverse_search = [
#     (occurrences_binary_line_adj_json_reverse_search_15, r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_reverse_search_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_reverse_search_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_reverse_search_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_reverse_search_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_reverse_search_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_reverse_search_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_reverse_search_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_reverse_search_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_reverse_search_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_reverse_search_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]


# # List of (occurrence_vector, score_vector, label)
# datasets_step_by_step = [
#     (occurrences_binary_line_adj_json_step_by_step_15, r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_step_by_step_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_step_by_step_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_step_by_step_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_step_by_step_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_step_by_step_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_step_by_step_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_step_by_step_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_step_by_step_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_step_by_step_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_step_by_step_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]

# # List of (occurrence_vector, score_vector, label)
# datasets_verification = [
#     (occurrences_binary_line_adj_json_verification_15, r15.line_R_coords_adj_json_reasoning_tokens_15, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None, 'o'),
#     (occurrences_binary_line_adj_txt_verification_15, r15.line_R_coords_adj_txt_reasoning_tokens_15, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange', None, 'o'),
#     (occurrences_binary_line_json_verification_15, r15.line_R_coords_json_reasoning_tokens_15, r15.line_R_coords_json_15, "Line JSON", 'tab:red', None, 'o'),
#     (occurrences_binary_line_jpg_verification_15, r15.line_R_coords_jpg_reasoning_tokens_15, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green', None, 'o'),
#     (occurrences_binary_line_tokenized_verification_15, r15.line_R_coords_tokenized_txt_reasoning_tokens_15, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple', None, 'o'),
#     (occurrences_binary_occupancy_adj_json_verification_15, r15.occupancy_R_coords_adj_json_reasoning_tokens_15, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black', 'v'),
#     (occurrences_binary_occupancy_adj_txt_verification_15, r15.occupancy_R_coords_adj_txt_reasoning_tokens_15, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black', 'v'),
#     (occurrences_binary_occupancy_json_verification_15, r15.occupancy_R_coords_json_reasoning_tokens_15, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black', 'v'),
#     (occurrences_binary_occupancy_jpg_verification_15, r15.occupancy_R_coords_jpg_reasoning_tokens_15, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black', 'v'),
#     (occurrences_binary_occupancy_tokenized_verification_15, r15.occupancy_R_coords_tokenized_txt_reasoning_tokens_15, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black', 'v'),
#     (occurrences_binary_occupancy_ascii_verification_15, r15.occupancy_R_coords_ascii_txt_reasoning_tokens_15, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black', 'v'),
# ]





# def plot_keyword(ax, datasets, title, ylabel):

#     x_vals = []
#     y_vals = []

#     for occurrence_vector, reasoning_token_count ,score_vector, label, color, mec, shape in datasets:

#         # Make sure they are np arrays
#         occurrence_vector = np.array(occurrence_vector)
#         score_vector = np.array(score_vector)
#         reasoning_vector = np.array(reasoning_token_count)
        
#         # Calculate mean presence and mean score for this dataset
#         reasoning_mean = np.mean(reasoning_vector) # the mean of the number of times the keywords are present yields the percentage of presence across all runs
#         occurrence_sum = np.sum(occurrence_vector)
#         y_ratio = (occurrence_sum / reasoning_mean)*1000 if reasoning_mean > 0 else 1 # avoid division by zero, multiply by 1000 for more interpretable scale
#         x_mean = np.mean(score_vector)

#         x_vals.append(x_mean)
#         y_vals.append(y_ratio)

#         ax.scatter(
#             x_mean,
#             y_ratio,
#             color=color,
#             # edgecolor=mec,
#             marker=shape,
#             s=60,
#             label=label
#         )

#     x_vals = np.array(x_vals)
#     y_vals = np.array(y_vals)

#     # Trend line
#     z = np.polyfit(x_vals, y_vals, 1)
#     p = np.poly1d(z)

#     sorted_idx = np.argsort(x_vals)

#     ax.plot(
#         x_vals[sorted_idx],
#         p(x_vals[sorted_idx]),
#         linestyle='--',
#         # marker=shape,
#         color='black',
#         alpha=0.7
#     )

#     ax.set_title(title, fontweight = 'bold', fontsize=10)
#     # ax.set_xlabel('Mean Completion Score (%)')
#     # ax.set_ylabel(ylabel)
#     ax.grid(linestyle=':', alpha=0.6)

# # Create 2x4 subplot grid (8 total)
# fig, axes = plt.subplots(2, 4, figsize=(18, 8), sharey = True)
# axes = axes.flatten()
# fig.supylabel(
#     "Presence Normalized by Mean Reasoning Length\n(presence per 1000 tokens)",
#     fontsize=13,
#     x=0.04
# )

# fig.supxlabel("Mean Completion Score (%)", fontsize=13)

# plot_keyword(axes[0], datasets_algorithm, "Algorithm",  "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")
# plot_keyword(axes[1], datasets_backtracking, "Backtracking", "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")
# plot_keyword(axes[2], datasets_false_confidence, "False Confidence", "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")
# plot_keyword(axes[3], datasets_frustration, "Frustration", "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")
# plot_keyword(axes[4], datasets_restart, "Restart", "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")
# plot_keyword(axes[5], datasets_reverse_search, "Reverse Search", "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")
# plot_keyword(axes[6], datasets_step_by_step, "Step-by-Step", "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")
# plot_keyword(axes[7], datasets_verification, "Verification", "Presence Normalized by Mean Reasoning Lenght (presence per 1000 tokens)")

# plt.suptitle('Keyword Categories Presence Normalized for Mean Reasoning Tokens vs Completion Score \nCoordinates Output, 15x15', fontsize=14)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()



# # ----- Creates Bar charts comparing avg completion score for present/absent keywords ---
# '''Does not show differences in scores achieved, regardless of keyword presence. 
# Does show that verification and backtracking always occur. '''
# representations = {
#     "Line Adjacency JSON": {
#         "scores": r15.line_R_coords_adj_json_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_line_adj_json_algorithm_15,
#             "Backtracking": occurrences_binary_line_adj_json_backtracking_15,
#             "False Confidence": occurrences_binary_line_adj_json_false_confidence_15,
#             "Frustration": occurrences_binary_line_adj_json_frustration_15,
#             "Restart": occurrences_binary_line_adj_json_restart_15,
#             "Reverse Search": occurrences_binary_line_adj_json_reverse_search_15,
#             "Step-by-Step": occurrences_binary_line_adj_json_step_by_step_15,
#             "Verification": occurrences_binary_line_adj_json_verification_15,
#         }
#     },
#     "Line Adjacency Text": {
#         "scores": r15.line_R_coords_adj_txt_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_line_adj_txt_algorithm_15,
#             "Backtracking": occurrences_binary_line_adj_txt_backtracking_15,
#             "False Confidence": occurrences_binary_line_adj_txt_false_confidence_15,
#             "Frustration": occurrences_binary_line_adj_txt_frustration_15,
#             "Restart": occurrences_binary_line_adj_txt_restart_15,
#             "Reverse Search": occurrences_binary_line_adj_txt_reverse_search_15,
#             "Step-by-Step": occurrences_binary_line_adj_txt_step_by_step_15,
#             "Verification": occurrences_binary_line_adj_txt_verification_15,
#         }
#     },
#     "Line JSON": {
#         "scores": r15.line_R_coords_json_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_line_json_algorithm_15,
#             "Backtracking": occurrences_binary_line_json_backtracking_15,
#             "False Confidence": occurrences_binary_line_json_false_confidence_15,
#             "Frustration": occurrences_binary_line_json_frustration_15,
#             "Restart": occurrences_binary_line_json_restart_15,
#             "Reverse Search": occurrences_binary_line_json_reverse_search_15,
#             "Step-by-Step": occurrences_binary_line_json_step_by_step_15,
#             "Verification": occurrences_binary_line_json_verification_15,
#         }
#     },
#     "Line JPG": {
#         "scores": r15.line_R_coords_jpg_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_line_jpg_algorithm_15,
#             "Backtracking": occurrences_binary_line_jpg_backtracking_15,
#             "False Confidence": occurrences_binary_line_jpg_false_confidence_15,
#             "Frustration": occurrences_binary_line_jpg_frustration_15,
#             "Restart": occurrences_binary_line_jpg_restart_15,
#             "Reverse Search": occurrences_binary_line_jpg_reverse_search_15,
#             "Step-by-Step": occurrences_binary_line_jpg_step_by_step_15,
#             "Verification": occurrences_binary_line_jpg_verification_15,
#         }
#     },
#     "Line Tokenized": {
#         "scores": r15.line_R_coords_tokenized_txt_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_line_tokenized_algorithm_15,
#             "Backtracking": occurrences_binary_line_tokenized_backtracking_15,
#             "False Confidence": occurrences_binary_line_tokenized_false_confidence_15,
#             "Frustration": occurrences_binary_line_tokenized_frustration_15,
#             "Restart": occurrences_binary_line_tokenized_restart_15,
#             "Reverse Search": occurrences_binary_line_tokenized_reverse_search_15,
#             "Step-by-Step": occurrences_binary_line_tokenized_step_by_step_15,
#             "Verification": occurrences_binary_line_tokenized_verification_15,
#         }
#     },
#     "Occupancy Adjacency JSON": {
#         "scores": r15.occupancy_R_coords_adj_json_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_occupancy_adj_json_algorithm_15,
#             "Backtracking": occurrences_binary_occupancy_adj_json_backtracking_15,
#             "False Confidence": occurrences_binary_occupancy_adj_json_false_confidence_15,
#             "Frustration": occurrences_binary_occupancy_adj_json_frustration_15,
#             "Restart": occurrences_binary_occupancy_adj_json_restart_15,
#             "Reverse Search": occurrences_binary_occupancy_adj_json_reverse_search_15,
#             "Step-by-Step": occurrences_binary_occupancy_adj_json_step_by_step_15,
#             "Verification": occurrences_binary_occupancy_adj_json_verification_15,
#         }
#     },
#     "Occupancy Adjacency Text": {
#         "scores": r15.occupancy_R_coords_adj_txt_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_occupancy_adj_txt_algorithm_15,
#             "Backtracking": occurrences_binary_occupancy_adj_txt_backtracking_15,
#             "False Confidence": occurrences_binary_occupancy_adj_txt_false_confidence_15,
#             "Frustration": occurrences_binary_occupancy_adj_txt_frustration_15,
#             "Restart": occurrences_binary_occupancy_adj_txt_restart_15,
#             "Reverse Search": occurrences_binary_occupancy_adj_txt_reverse_search_15,
#             "Step-by-Step": occurrences_binary_occupancy_adj_txt_step_by_step_15,
#             "Verification": occurrences_binary_occupancy_adj_txt_verification_15,
#         }
#     },
#     "Occupancy JSON": {
#         "scores": r15.occupancy_R_coords_json_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_occupancy_json_algorithm_15,
#             "Backtracking": occurrences_binary_occupancy_json_backtracking_15,
#             "False Confidence": occurrences_binary_occupancy_json_false_confidence_15,
#             "Frustration": occurrences_binary_occupancy_json_frustration_15,
#             "Restart": occurrences_binary_occupancy_json_restart_15,
#             "Reverse Search": occurrences_binary_occupancy_json_reverse_search_15,
#             "Step-by-Step": occurrences_binary_occupancy_json_step_by_step_15,
#             "Verification": occurrences_binary_occupancy_json_verification_15,
#         }
#     },
#     "Occupancy JPG": {
#         "scores": r15.occupancy_R_coords_jpg_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_occupancy_jpg_algorithm_15,
#             "Backtracking": occurrences_binary_occupancy_jpg_backtracking_15,
#             "False Confidence": occurrences_binary_occupancy_jpg_false_confidence_15,
#             "Frustration": occurrences_binary_occupancy_jpg_frustration_15,
#             "Restart": occurrences_binary_occupancy_jpg_restart_15,
#             "Reverse Search": occurrences_binary_occupancy_jpg_reverse_search_15,
#             "Step-by-Step": occurrences_binary_occupancy_jpg_step_by_step_15,
#             "Verification": occurrences_binary_occupancy_jpg_verification_15,
#         }
#     },
#     "Occupancy Tokenized": {
#         "scores": r15.occupancy_R_coords_tokenized_txt_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_occupancy_tokenized_algorithm_15,
#             "Backtracking": occurrences_binary_occupancy_tokenized_backtracking_15,
#             "False Confidence": occurrences_binary_occupancy_tokenized_false_confidence_15,
#             "Frustration": occurrences_binary_occupancy_tokenized_frustration_15,
#             "Restart": occurrences_binary_occupancy_tokenized_restart_15,
#             "Reverse Search": occurrences_binary_occupancy_tokenized_reverse_search_15,
#             "Step-by-Step": occurrences_binary_occupancy_tokenized_step_by_step_15,
#             "Verification": occurrences_binary_occupancy_tokenized_verification_15,
#         }
#     },
#     "Occupancy ASCII": {
#         "scores": r15.occupancy_R_coords_ascii_txt_15,
#         "keywords": {
#             "Algorithm Naming": occurrences_binary_occupancy_ascii_algorithm_15,
#             "Backtracking": occurrences_binary_occupancy_ascii_backtracking_15,
#             "False Confidence": occurrences_binary_occupancy_ascii_false_confidence_15,
#             "Frustration": occurrences_binary_occupancy_ascii_frustration_15,
#             "Restart": occurrences_binary_occupancy_ascii_restart_15,
#             "Reverse Search": occurrences_binary_occupancy_ascii_reverse_search_15,
#             "Step-by-Step": occurrences_binary_occupancy_ascii_step_by_step_15,
#             "Verification": occurrences_binary_occupancy_ascii_verification_15,
#         }
#     }

# }




# # plotting all representations for each keyword

# keywords = [
#     "Algorithm Naming",
#     "Backtracking",
#     "False Confidence",
#     "Frustration",
#     "Restart",
#     "Reverse Search",
#     "Step-by-Step",
#     "Verification",
# ]

# rep_names = list(representations.keys())

# fig, axes = plt.subplots(2, 4, figsize=(20, 10), sharex=True)
# axes = axes.flatten()

# for ax, keyword in zip(axes, keywords):

#     present_means = []
#     absent_means = []

#     for rep in rep_names:

#         scores = np.array(representations[rep]["scores"])
#         occurrence_vector = np.array(
#             representations[rep]["keywords"][keyword]
#         )

#         yes_scores = scores[occurrence_vector == 1]
#         no_scores  = scores[occurrence_vector == 0]

#         mean_yes = np.mean(yes_scores) if len(yes_scores) > 0 else 0
#         mean_no  = np.mean(no_scores) if len(no_scores) > 0 else 0

#         present_means.append(mean_yes)
#         absent_means.append(mean_no)

#     y_positions = np.arange(len(rep_names))
#     bar_height = 0.35


#     ax.barh(y_positions - bar_height/2,
#             present_means,
#             height=bar_height,
#             alpha=0.8,
#             label="Present")

#     ax.barh(y_positions + bar_height/2,
#             absent_means,
#             height=bar_height,
#             alpha=0.6,
#             label="Absent")

#     ax.set_yticks(y_positions)
#     ax.set_yticklabels(rep_names, fontsize=8)

#     ax.set_title(keyword, fontweight='bold')
#     ax.set_xlim(0, 100)
#     ax.grid(axis='x', linestyle=':', alpha=0.5)

# fig.supxlabel("Average Completion Score (%)", fontsize=14)
# fig.supylabel("Representation", fontsize=14)

# plt.suptitle(
#     "Average Completion Score When Keyword Is Present vs Absent\nAcross All Representations",
#     fontsize=16,
#     fontweight='bold'
# )

# # Single shared legend
# handles, labels = axes[0].get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper right', ncol=1, fontsize=12)

# plt.tight_layout(rect=[0, 0.05, 1, 0.95])
# # plt.show()














# # plot only the differences between performance for present and absent. Positive is mean_yes>mean_no, negative is mean_yes<mean_no

# keywords = [
#     "Algorithm Naming",
#     "Backtracking",
#     "False Confidence",
#     "Frustration",
#     "Restart",
#     "Reverse Search",
#     "Step-by-Step",
#     "Verification",
# ]

# rep_names = list(representations.keys())

# fig, axes = plt.subplots(2, 4, figsize=(20, 10), sharex=True)
# axes = axes.flatten()

# for ax, keyword in zip(axes, keywords):

#     differences = []

#     for rep in rep_names:

#         scores = np.array(representations[rep]["scores"])
#         occurrence_vector = np.array(
#             representations[rep]["keywords"][keyword]
#         )

#         yes_scores = scores[occurrence_vector == 1]
#         no_scores  = scores[occurrence_vector == 0]

#         mean_yes = np.mean(yes_scores) if len(yes_scores) > 0 else 0
#         mean_no  = np.mean(no_scores) if len(no_scores) > 0 else 0

#         diff = mean_yes - mean_no
#         differences.append(diff)
#         if rep == 'Occupancy JSON' and keyword == 'Reverse Search':
#             print('occ json present_score:', mean_yes, '\n')
#             print('occ json absent_score:', mean_no)


#     y_positions = np.arange(len(rep_names))

#     ax.barh(y_positions, differences)

#     ax.set_yticks(y_positions)
#     ax.set_yticklabels(rep_names, fontsize=8)

#     ax.axvline(0, linestyle='--')  # zero reference line

#     ax.set_title(keyword, fontweight='bold')
#     ax.set_xlim(-100, 80)  # adjust if needed
#     ax.grid(axis='x', linestyle=':', alpha=0.5)

# fig.supxlabel("Difference in Completion Score (Present − Absent) (%)", fontsize=14)
# fig.supylabel("Representation", fontsize=14)

# plt.suptitle(
#     "Effect of Keyword Presence on Completion Score\n(Mean Difference)",
#     fontsize=16,
#     fontweight='bold'
# )

# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.show()





# # # ----- Plotting number of used tokens vs number of output characters  - no interesting results. ---------

# # # Number of thinking tokens
# # # y= r15.line_R_coords_adj_txt_output_tokens_15 - r15.line_R_coords_adj_txt_final_answer_15 

# # # Number of final answer tokens
# # y=r15.line_R_coords_adj_txt_final_answer_15 

# # line_R_coords_adj_txt_thoughts_characters  = np.array([4193, 1312, 1990, 2316, 2283, 2513, 1644, 2192, 2814, 2892])
# # x = line_R_coords_adj_txt_thoughts_characters

# # # Linear fit
# # slope, intercept = np.polyfit(x, y, 1)

# # x_fit = np.linspace(x.min(), x.max(), 200)
# # y_fit = slope * x_fit + intercept

# # # Plot
# # plt.figure(figsize=(8, 6))
# # plt.scatter(x, y, edgecolor='black', label='data')
# # plt.plot(x_fit, y_fit, linestyle='--', linewidth=2, label='trend')

# # # Axis labels
# # plt.ylabel('number of tokens (-)')
# # plt.xlabel('number of characters (-)')

# # # Grid
# # plt.grid(alpha=0.3)

# # # In-figure slope label
# # plt.text(
# #     0.05, 0.95,
# #     f'slope = {slope:.2f} tokens/characters',
# #     transform=plt.gca().transAxes,
# #     fontsize=11,
# #     verticalalignment='top',
# #     bbox=dict(boxstyle='round', facecolor=None, alpha=0.8)
# # )

# # plt.tight_layout()
# # plt.show()





# # # -------------------------------------------------------------------------------
# # # thinking tokens
# # thinking_tokens = r15.line_R_coords_adj_txt_output_tokens_15 - r15.line_R_coords_adj_txt_final_answer_15

# # ratio = line_R_coords_adj_txt_thoughts_characters / thinking_tokens
# # print(ratio)
# # y= ratio

# # completion_score = r15.line_R_coords_adj_txt_15
# # x = completion_score
# # # Linear fit
# # slope, intercept = np.polyfit(x, y, 1)

# # x_fit = np.linspace(x.min(), x.max(), 200)
# # y_fit = slope * x_fit + intercept

# # # Plot
# # plt.figure(figsize=(8, 6))
# # plt.scatter(x, y, edgecolor='black', label='data')
# # plt.plot(x_fit, y_fit, linestyle='--', linewidth=2, label='trend')

# # # Axis labels
# # plt.ylabel('ratio characters/token (-)')
# # plt.xlabel('Completion score (%)')

# # # Grid
# # plt.grid(alpha=0.3)

# # # In-figure slope label
# # plt.text(
# #     0.05, 0.95,
# #     f'slope = {slope:.2f}',
# #     transform=plt.gca().transAxes,
# #     fontsize=11,
# #     verticalalignment='top',
# #     bbox=dict(boxstyle='round', facecolor=None, alpha=0.8)
# # )

# # plt.tight_layout()
# # plt.show()