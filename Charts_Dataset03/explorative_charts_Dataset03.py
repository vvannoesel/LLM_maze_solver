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


# only adj txt 15, all categories
line_R_coords_adj_txt_algorithm_15 = [24, 4, 7, 2, 10, 10, 5, 10, 5, 0, 4, 10, 4, 4, 0, 5, 4, 2, 0, 11, 10, 5, 0, 15, 2, 9, 10, 13, 4, 0, 5, 8, 8, 13, 15, 1, 12, 14, 6, 39, 0, 7, 3, 0, 8, 16, 0, 7, 0, 5]
line_R_coords_adj_txt_backtracking_15 = [11, 6, 11, 2, 2, 6, 6, 3, 7, 7, 5, 6, 5, 5, 1, 6, 7, 4, 3, 7, 7, 2, 6, 16, 6, 3, 5, 7, 10, 7, 3, 1, 4, 16, 6, 6, 5, 3, 6, 11, 7, 11, 1, 4, 1, 9, 4, 7, 1, 4]
line_R_coords_adj_txt_false_confidence_15 = [0, 2, 4, 0, 1, 5, 1, 3, 1, 4, 0, 3, 1, 6, 1, 0, 1, 4, 1, 0, 2, 2, 2, 1, 1, 2, 1, 1, 0, 2, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 2, 1, 1, 2, 0, 1, 2, 2, 1, 1]
line_R_coords_adj_txt_frustration_15 = [7, 1, 3, 0, 3, 5, 0, 8, 2, 10, 1, 0, 0, 3, 0, 2, 6, 4, 1, 7, 1, 2, 1, 0, 3, 2, 2, 2, 3, 2, 5, 1, 0, 4, 5, 2, 4, 1, 3, 3, 9, 5, 1, 4, 3, 5, 1, 3, 1, 4]
line_R_coords_adj_txt_restart_15 = [5, 0, 6, 0, 4, 5, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 1, 1, 2, 6, 0, 1, 0, 1, 1, 0, 0, 0, 0, 3, 1, 2, 2, 0, 4, 0, 0, 4, 1, 2, 2, 3, 1, 2, 0, 1]
line_R_coords_adj_txt_reverse_search_15 = [3, 0, 1, 0, 3, 5, 0, 3, 0, 4, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1]
line_R_coords_adj_txt_step_by_step_15 = [0, 0, 8, 79, 0, 2, 2, 0, 69, 0, 63, 0, 61, 3, 0, 1, 1, 0, 18, 0, 20, 2, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 62, 0, 0, 0, 49, 13, 0, 1, 18, 4, 6, 12, 0, 0, 0, 65, 0]
line_R_coords_adj_txt_verification_15 = [7, 5, 3, 1, 2, 3, 12, 3, 15, 6, 1, 7, 3, 8, 6, 3, 3, 1, 7, 5, 2, 10, 8, 5, 8, 4, 2, 9, 6, 3, 9, 4, 8, 9, 1, 4, 3, 1, 2, 2, 10, 11, 7, 10, 7, 7, 4, 2, 8, 8]



occurrences_binary_algorithm_15 = binary_occurrence(line_R_coords_adj_txt_algorithm_15)
occurrences_binary_backtracking_15 = binary_occurrence(line_R_coords_adj_txt_backtracking_15)
occurrences_binary_false_confidence_15 = binary_occurrence(line_R_coords_adj_txt_false_confidence_15)
occurrences_binary_frustration_15 = binary_occurrence(line_R_coords_adj_txt_frustration_15)
occurrences_binary_restart_15 = binary_occurrence(line_R_coords_adj_txt_restart_15)
occurrences_binary_reverse_search_15 = binary_occurrence(line_R_coords_adj_txt_reverse_search_15)
occurrences_binary_step_by_step_15 = binary_occurrence(line_R_coords_adj_txt_step_by_step_15)
occurrences_binary_verification_15 = binary_occurrence(line_R_coords_adj_txt_verification_15)




# Only algorithm naming, all representations of 15

line_R_coords_adj_json_algorithm_15 = [62, 6, 1, 0, 10, 3, 4, 7, 10, 6, 7, 13, 9, 12, 5, 6, 5, 3, 8, 0, 3, 4, 8, 9, 11, 5, 12, 11, 10, 10, 10, 13, 1, 9, 1, 8, 9, 9, 6, 12, 0, 3, 12, 13, 2, 11, 2, 9, 2, 1]
line_R_coords_adj_json_backtracking_15 = [0, 5, 3, 2, 11, 7, 4, 12, 5, 2, 11, 5, 8, 7, 2, 6, 3, 7, 5, 1, 2, 3, 3, 6, 6, 1, 4, 10, 3, 3, 4, 8, 2, 7, 4, 7, 9, 2, 3, 12, 6, 5, 3, 3, 0, 1, 5, 7, 8, 8]
line_R_coords_adj_json_false_confidence_15 = [1, 0, 5, 0, 3, 0, 0, 0, 2, 2, 1, 3, 1, 0, 4, 1, 1, 2, 1, 2, 5, 1, 2, 0, 0, 1, 0, 1, 0, 2, 1, 3, 0, 1, 0, 2, 2, 0, 7, 0, 2, 0, 1, 0, 1, 0, 1, 1, 0, 4]
line_R_coords_adj_json_frustration_15 = [1, 2, 4, 1, 6, 2, 2, 5, 3, 0, 1, 1, 2, 0, 1, 0, 1, 2, 0, 0, 4, 0, 2, 1, 0, 0, 0, 2, 1, 7, 2, 1, 1, 1, 1, 0, 0, 0, 2, 1, 2, 0, 1, 0, 2, 0, 0, 2, 7, 2]
line_R_coords_adj_json_restart_15 = [0, 0, 0, 0, 3, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 1]
line_R_coords_adj_json_reverse_search_15 = [0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
line_R_coords_adj_json_step_by_step_15 = [14, 0, 0, 4, 1, 0, 0, 3, 0, 54, 0, 86, 2, 0, 83, 1, 0, 0, 49, 126, 0, 2, 1, 111, 1, 51, 0, 0, 1, 0, 2, 2, 5, 0, 80, 0, 0, 44, 8, 6, 0, 0, 0, 0, 49, 0, 0, 0, 0, 0]
line_R_coords_adj_json_verification_15 = [1, 2, 4, 1, 6, 6, 6, 6, 1, 4, 3, 4, 2, 4, 3, 4, 4, 10, 5, 1, 4, 9, 2, 3, 4, 7, 5, 6, 1, 5, 6, 3, 0, 4, 1, 3, 6, 5, 3, 3, 4, 6, 8, 1, 2, 1, 2, 3, 5, 9]
line_R_coords_adj_txt_algorithm_15 = [24, 4, 7, 2, 10, 10, 5, 10, 5, 0, 4, 10, 4, 4, 0, 5, 4, 2, 0, 11, 10, 5, 0, 15, 2, 9, 10, 13, 4, 0, 5, 8, 8, 13, 15, 1, 12, 14, 6, 39, 0, 7, 3, 0, 8, 16, 0, 7, 0, 5]
line_R_coords_adj_txt_backtracking_15 = [11, 6, 11, 2, 2, 6, 6, 3, 7, 7, 5, 6, 5, 5, 1, 6, 7, 4, 3, 7, 7, 2, 6, 16, 6, 3, 5, 7, 10, 7, 3, 1, 4, 16, 6, 6, 5, 3, 6, 11, 7, 11, 1, 4, 1, 9, 4, 7, 1, 4]
line_R_coords_adj_txt_false_confidence_15 = [0, 2, 4, 0, 1, 5, 1, 3, 1, 4, 0, 3, 1, 6, 1, 0, 1, 4, 1, 0, 2, 2, 2, 1, 1, 2, 1, 1, 0, 2, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 2, 1, 1, 2, 0, 1, 2, 2, 1, 1]
line_R_coords_adj_txt_frustration_15 = [7, 1, 3, 0, 3, 5, 0, 8, 2, 10, 1, 0, 0, 3, 0, 2, 6, 4, 1, 7, 1, 2, 1, 0, 3, 2, 2, 2, 3, 2, 5, 1, 0, 4, 5, 2, 4, 1, 3, 3, 9, 5, 1, 4, 3, 5, 1, 3, 1, 4]
line_R_coords_adj_txt_restart_15 = [5, 0, 6, 0, 4, 5, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 1, 1, 2, 6, 0, 1, 0, 1, 1, 0, 0, 0, 0, 3, 1, 2, 2, 0, 4, 0, 0, 4, 1, 2, 2, 3, 1, 2, 0, 1]
line_R_coords_adj_txt_reverse_search_15 = [3, 0, 1, 0, 3, 5, 0, 3, 0, 4, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1]
line_R_coords_adj_txt_step_by_step_15 = [0, 0, 8, 79, 0, 2, 2, 0, 69, 0, 63, 0, 61, 3, 0, 1, 1, 0, 18, 0, 20, 2, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 62, 0, 0, 0, 49, 13, 0, 1, 18, 4, 6, 12, 0, 0, 0, 65, 0]
line_R_coords_adj_txt_verification_15 = [7, 5, 3, 1, 2, 3, 12, 3, 15, 6, 1, 7, 3, 8, 6, 3, 3, 1, 7, 5, 2, 10, 8, 5, 8, 4, 2, 9, 6, 3, 9, 4, 8, 9, 1, 4, 3, 1, 2, 2, 10, 11, 7, 10, 7, 7, 4, 2, 8, 8]
line_R_coords_jpg_algorithm_15 = [1, 1, 4, 1, 1, 1, 1, 2, 3, 1, 2, 6, 1, 6, 0, 0, 0, 1, 3, 3, 2, 1, 2, 0, 8, 3, 1, 1, 2, 1, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 1, 1, 5, 3, 2, 1, 0]
line_R_coords_jpg_backtracking_15 = [13, 3, 5, 12, 4, 1, 10, 6, 8, 1, 8, 6, 10, 8, 2, 4, 13, 7, 8, 9, 9, 19, 10, 3, 8, 5, 12, 8, 5, 2, 13, 11, 14, 6, 5, 5, 4, 14, 9, 12, 5, 8, 4, 11, 13, 13, 6, 7, 7, 7]
line_R_coords_jpg_false_confidence_15 = [2, 4, 1, 1, 1, 0, 4, 3, 4, 0, 2, 1, 3, 2, 1, 1, 1, 2, 1, 4, 2, 1, 2, 0, 1, 2, 1, 0, 1, 1, 1, 0, 0, 7, 1, 1, 1, 1, 2, 2, 4, 0, 4, 3, 0, 2, 6, 2, 2, 1]
line_R_coords_jpg_frustration_15 = [2, 2, 2, 5, 1, 0, 1, 1, 2, 2, 3, 0, 2, 1, 0, 4, 4, 1, 5, 3, 2, 0, 0, 0, 1, 0, 4, 4, 3, 1, 0, 2, 4, 1, 1, 1, 3, 1, 1, 0, 0, 1, 0, 3, 4, 2, 1, 0, 3, 0]
line_R_coords_jpg_restart_15 = [4, 0, 0, 3, 0, 1, 1, 2, 0, 0, 2, 0, 3, 3, 0, 1, 3, 1, 0, 1, 0, 0, 1, 0, 0, 0, 3, 0, 1, 1, 1, 0, 2, 2, 1, 1, 1, 1, 0, 3, 0, 1, 1, 2, 3, 1, 0, 0, 2, 3]
line_R_coords_jpg_reverse_search_15 = [0, 0, 0, 5, 3, 0, 1, 0, 3, 1, 0, 0, 1, 0, 2, 1, 1, 0, 0, 6, 4, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 0, 4, 0, 0, 1, 0, 0, 3, 0, 5, 1, 0, 0, 0, 1, 1]
line_R_coords_jpg_step_by_step_15 = [0, 0, 0, 1, 0, 0, 1, 0, 46, 0, 0, 0, 53, 1, 13, 48, 0, 0, 0, 3, 1, 20, 0, 0, 3, 53, 43, 58, 0, 16, 46, 68, 46, 47, 0, 0, 0, 1, 0, 36, 38, 1, 79, 1, 26, 43, 0, 42, 0, 55]
line_R_coords_jpg_verification_15 = [5, 6, 3, 3, 3, 1, 3, 4, 5, 3, 2, 6, 2, 1, 0, 5, 3, 3, 4, 4, 5, 0, 5, 2, 3, 5, 3, 3, 4, 3, 0, 1, 6, 6, 3, 5, 2, 4, 5, 11, 3, 2, 2, 3, 3, 9, 3, 3, 2, 4]
line_R_coords_json_algorithm_15 = [15, 12, 0, 1, 1, 1, 0, 9, 5, 1, 8, 3, 4, 6, 1, 4, 1, 1, 2, 6, 5, 0, 0, 2, 0, 3, 1, 0, 1, 9, 2, 3, 0, 1, 1, 0, 1, 0, 8, 0, 30, 1, 2, 0, 2, 11, 1, 0, 4, 0]
line_R_coords_json_backtracking_15 = [4, 7, 0, 8, 9, 7, 8, 11, 8, 2, 11, 4, 12, 12, 9, 4, 12, 8, 8, 11, 5, 6, 2, 6, 6, 8, 7, 11, 5, 5, 6, 5, 7, 5, 7, 8, 5, 20, 7, 3, 3, 6, 6, 2, 9, 11, 7, 10, 9, 9]
line_R_coords_json_false_confidence_15 = [1, 3, 0, 1, 1, 4, 2, 0, 0, 1, 2, 4, 0, 3, 0, 0, 2, 0, 2, 1, 4, 1, 2, 1, 2, 1, 3, 0, 0, 1, 3, 0, 1, 3, 0, 2, 1, 1, 2, 4, 2, 0, 5, 2, 1, 1, 3, 2, 1, 3]
line_R_coords_json_frustration_15 = [2, 0, 0, 2, 5, 6, 2, 4, 2, 1, 9, 1, 4, 7, 2, 2, 5, 3, 3, 5, 4, 2, 0, 2, 1, 2, 3, 4, 2, 4, 7, 3, 3, 4, 5, 6, 2, 4, 3, 2, 1, 2, 2, 0, 2, 4, 3, 2, 3, 2]
line_R_coords_json_restart_15 = [0, 0, 0, 0, 0, 4, 0, 2, 2, 1, 0, 0, 2, 6, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 3, 0, 1, 0, 0, 2, 1, 3, 2, 1, 0, 1, 1, 2, 0, 1, 2, 0, 2, 0, 0, 3, 1, 2, 1, 0]
line_R_coords_json_reverse_search_15 = [0, 0, 0, 0, 1, 2, 1, 0, 1, 0, 1, 0, 0, 0, 4, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 4, 1, 0, 3, 0, 0, 0, 1, 3, 2, 2, 0, 4, 0, 3, 0, 0, 0, 2, 0, 1, 0, 2]
line_R_coords_json_step_by_step_15 = [8, 0, 61, 3, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 9, 6, 51, 0, 1, 0, 0, 0, 44, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 1, 9, 1, 0, 0, 36, 5, 0]
line_R_coords_json_verification_15 = [8, 8, 0, 1, 7, 7, 6, 5, 3, 2, 7, 3, 11, 10, 1, 3, 8, 3, 8, 6, 4, 2, 3, 1, 0, 2, 2, 7, 1, 6, 2, 6, 10, 7, 1, 6, 6, 8, 6, 13, 3, 1, 7, 1, 4, 5, 2, 6, 3, 11]
line_R_coords_tokenized_txt_algorithm_15 = [6, 1, 4, 2, 2, 2, 0, 1, 1, 0, 0, 4, 2, 0, 6, 3, 1, 2, 3, 6, 1, 3, 1, 2, 2, 0, 8, 0, 2, 4, 6, 2, 0, 5, 0, 4, 4, 4, 0, 5, 4, 2, 0, 3, 0, 0, 3, 0, 0, 3]
line_R_coords_tokenized_txt_backtracking_15 = [4, 2, 11, 3, 6, 13, 7, 5, 7, 3, 8, 6, 4, 3, 12, 6, 2, 5, 1, 1, 10, 2, 9, 5, 2, 6, 8, 0, 5, 4, 7, 0, 8, 4, 7, 4, 4, 0, 2, 3, 10, 12, 6, 2, 9, 2, 5, 4, 2, 14]
line_R_coords_tokenized_txt_false_confidence_15 = [2, 2, 3, 0, 3, 6, 2, 1, 2, 2, 1, 2, 3, 2, 2, 0, 0, 1, 2, 1, 1, 0, 2, 0, 4, 0, 2, 1, 0, 1, 0, 0, 3, 0, 1, 1, 5, 1, 1, 0, 1, 3, 2, 1, 2, 1, 1, 1, 4, 4]
line_R_coords_tokenized_txt_frustration_15 = [5, 1, 4, 2, 1, 5, 2, 2, 2, 1, 1, 4, 2, 1, 5, 4, 2, 4, 1, 1, 1, 1, 2, 4, 1, 2, 3, 1, 0, 0, 0, 0, 3, 6, 0, 0, 7, 1, 3, 1, 4, 2, 4, 1, 4, 2, 1, 0, 2, 6]
line_R_coords_tokenized_txt_restart_15 = [2, 0, 1, 0, 2, 0, 1, 1, 2, 0, 1, 0, 2, 1, 2, 1, 2, 3, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 1, 0, 0, 0, 3, 1, 2, 0, 1, 3, 0, 0, 1, 6]
line_R_coords_tokenized_txt_reverse_search_15 = [1, 0, 0, 0, 0, 5, 0, 3, 0, 0, 2, 3, 1, 0, 3, 3, 3, 0, 0, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
line_R_coords_tokenized_txt_step_by_step_15 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 91, 83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 78, 0, 1, 0, 1, 0, 1, 2, 0, 0, 10, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 73, 0]
line_R_coords_tokenized_txt_verification_15 = [2, 3, 4, 0, 2, 7, 3, 1, 3, 7, 2, 3, 4, 5, 2, 3, 7, 3, 12, 4, 6, 9, 3, 2, 6, 7, 3, 0, 4, 4, 1, 2, 7, 3, 5, 5, 3, 2, 1, 1, 8, 4, 4, 6, 5, 5, 6, 5, 1, 2]
occupancy_R_coords_adj_json_algorithm_15 = [0, 0, 0, 7, 3, 4, 0, 5, 5, 4, 5, 8, 2, 5, 8, 5, 3, 2, 5, 19, 5, 0, 0, 3, 2, 4, 13, 2, 2, 4, 6, 0, 5, 2, 6, 5, 4, 8, 7, 9, 0, 3, 6, 6, 7, 2, 0, 8, 9, 5]
occupancy_R_coords_adj_json_backtracking_15 = [0, 6, 0, 4, 4, 2, 3, 5, 8, 3, 7, 3, 3, 8, 8, 6, 10, 4, 3, 3, 6, 2, 5, 4, 3, 6, 5, 8, 1, 3, 3, 1, 0, 4, 8, 5, 1, 5, 7, 3, 0, 5, 2, 2, 5, 3, 0, 10, 2, 5]
occupancy_R_coords_adj_json_false_confidence_15 = [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 3, 1, 2, 0, 5, 0, 0, 0, 4, 0, 1, 1, 0, 0, 0, 4, 1, 0, 3, 3, 1, 0, 4, 0, 0, 0, 1, 0, 1, 3, 0, 4, 1, 1]
occupancy_R_coords_adj_json_frustration_15 = [0, 4, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 3, 1, 2, 3, 0, 4, 0, 3, 0, 1, 1, 0, 3, 0, 4, 0, 0, 1, 4, 1, 2, 1, 3, 0, 1, 1, 0, 0, 5, 1, 4, 2, 1, 0, 1, 0, 0]
occupancy_R_coords_adj_json_restart_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
occupancy_R_coords_adj_json_reverse_search_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
occupancy_R_coords_adj_json_step_by_step_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 54, 0, 0, 1, 0, 0, 101, 0, 0, 0, 0, 102, 0, 83, 5, 0, 13, 1, 15, 1, 2, 121, 5, 1, 0, 0, 108, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
occupancy_R_coords_adj_json_verification_15 = [0, 3, 0, 5, 3, 4, 0, 2, 4, 1, 2, 0, 5, 3, 4, 3, 4, 4, 7, 1, 2, 1, 1, 2, 8, 8, 4, 3, 1, 0, 4, 3, 3, 2, 7, 3, 2, 3, 3, 3, 0, 10, 1, 4, 1, 3, 1, 4, 1, 1]
occupancy_R_coords_adj_txt_algorithm_15 = [0, 8, 8, 0, 10, 3, 5, 4, 11, 10, 10, 0, 3, 2, 0, 10, 8, 2, 0, 7, 0, 4, 4, 2, 1, 4, 14, 2, 5, 0, 4, 4, 8, 0, 7, 23, 0, 8, 8, 2, 4, 0, 4, 4, 4, 8, 0, 6, 3, 6]
occupancy_R_coords_adj_txt_backtracking_15 = [0, 3, 3, 3, 7, 5, 8, 4, 6, 5, 6, 3, 2, 6, 8, 9, 7, 4, 3, 5, 10, 2, 0, 4, 4, 2, 12, 4, 1, 2, 5, 8, 4, 4, 6, 5, 4, 3, 1, 7, 5, 6, 7, 4, 6, 2, 2, 3, 0, 4]
occupancy_R_coords_adj_txt_false_confidence_15 = [0, 1, 1, 4, 3, 4, 2, 0, 1, 0, 1, 3, 2, 1, 3, 2, 0, 2, 1, 0, 1, 4, 2, 1, 3, 1, 0, 1, 1, 1, 1, 3, 1, 3, 0, 1, 1, 1, 2, 3, 2, 3, 2, 4, 2, 0, 0, 2, 0, 2]
occupancy_R_coords_adj_txt_frustration_15 = [0, 2, 0, 0, 3, 3, 5, 2, 4, 5, 2, 7, 0, 1, 1, 4, 2, 1, 0, 7, 1, 0, 1, 1, 2, 1, 2, 1, 0, 4, 1, 3, 1, 4, 3, 3, 0, 1, 1, 4, 2, 4, 2, 2, 0, 1, 3, 2, 0, 3]
occupancy_R_coords_adj_txt_restart_15 = [0, 1, 0, 2, 1, 2, 2, 2, 0, 0, 0, 1, 0, 1, 1, 1, 2, 2, 0, 2, 2, 0, 0, 0, 3, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 4, 0, 2, 0, 1, 2, 0, 0, 3, 0, 0]
occupancy_R_coords_adj_txt_reverse_search_15 = [0, 0, 0, 0, 2, 1, 0, 4, 0, 2, 1, 0, 0, 0, 2, 2, 2, 5, 0, 3, 6, 0, 0, 1, 3, 0, 2, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 1, 2, 0, 3, 1, 0, 1, 0, 0, 0]
occupancy_R_coords_adj_txt_step_by_step_15 = [0, 0, 0, 0, 4, 0, 0, 2, 1, 0, 2, 1, 5, 0, 2, 4, 0, 8, 2, 4, 3, 0, 2, 0, 54, 0, 6, 76, 7, 2, 11, 1, 0, 0, 1, 0, 1, 99, 0, 1, 2, 2, 4, 0, 1, 33, 20, 0, 0, 0]
occupancy_R_coords_adj_txt_verification_15 = [0, 1, 5, 4, 8, 3, 2, 3, 3, 1, 2, 2, 2, 6, 2, 7, 3, 4, 7, 2, 3, 7, 1, 0, 11, 5, 0, 1, 6, 1, 1, 3, 7, 6, 5, 0, 7, 2, 3, 3, 1, 7, 3, 3, 8, 3, 6, 5, 1, 4]
occupancy_R_coords_ascii_txt_algorithm_15 = [3, 3, 2, 0, 2, 1, 7, 0, 2, 0, 1, 1, 1, 2, 1, 3, 1, 3, 2, 0, 1, 0, 4, 1, 1, 0, 1, 1, 2, 5, 7, 1, 0, 0, 0, 3, 1, 0, 2, 4, 0, 2, 2, 1, 4, 3, 1, 1, 0, 4]
occupancy_R_coords_ascii_txt_backtracking_15 = [1, 12, 4, 4, 2, 5, 3, 9, 9, 6, 3, 12, 3, 6, 7, 6, 11, 12, 10, 6, 3, 2, 1, 5, 4, 4, 11, 6, 5, 5, 7, 2, 8, 11, 6, 3, 4, 4, 4, 5, 4, 7, 6, 0, 3, 5, 19, 5, 6, 3]
occupancy_R_coords_ascii_txt_false_confidence_15 = [6, 5, 0, 1, 1, 3, 3, 5, 3, 0, 1, 5, 0, 1, 1, 2, 1, 5, 1, 1, 1, 0, 1, 0, 1, 2, 0, 3, 2, 2, 1, 1, 3, 1, 1, 0, 4, 0, 0, 3, 0, 0, 3, 1, 0, 2, 3, 3, 2, 1]
occupancy_R_coords_ascii_txt_frustration_15 = [1, 5, 1, 2, 3, 4, 5, 6, 6, 4, 0, 4, 6, 3, 4, 1, 5, 3, 0, 2, 4, 1, 2, 4, 6, 5, 3, 5, 3, 10, 0, 0, 3, 4, 7, 0, 2, 1, 2, 2, 7, 1, 3, 2, 0, 2, 7, 1, 6, 4]
occupancy_R_coords_ascii_txt_restart_15 = [0, 0, 1, 1, 2, 0, 0, 0, 4, 0, 0, 2, 1, 2, 1, 3, 4, 3, 3, 1, 1, 0, 0, 1, 1, 0, 2, 3, 1, 2, 0, 0, 2, 1, 3, 2, 3, 0, 1, 1, 2, 0, 1, 0, 0, 3, 2, 0, 1, 1]
occupancy_R_coords_ascii_txt_reverse_search_15 = [0, 1, 0, 4, 0, 0, 0, 0, 2, 2, 0, 1, 1, 0, 3, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 4, 2, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
occupancy_R_coords_ascii_txt_step_by_step_15 = [8, 0, 0, 0, 79, 0, 3, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 5, 0, 18, 0, 0, 52, 1, 0, 0, 0, 75, 7, 1, 1, 118, 3, 0, 0, 0, 0, 39, 0, 0, 18, 0, 0, 116, 0, 0, 2, 2, 4, 1]
occupancy_R_coords_ascii_txt_verification_15 = [0, 3, 4, 2, 1, 2, 1, 7, 4, 0, 6, 6, 3, 7, 4, 0, 13, 3, 3, 2, 1, 0, 7, 5, 7, 6, 4, 6, 7, 5, 4, 3, 3, 4, 4, 2, 5, 0, 1, 2, 3, 5, 3, 0, 0, 2, 8, 1, 7, 0]
occupancy_R_coords_jpg_algorithm_15 = [2, 1, 3, 4, 5, 1, 1, 3, 2, 1, 2, 5, 2, 1, 4, 4, 1, 3, 2, 3, 7, 1, 4, 1, 0, 4, 5, 0, 5, 1, 1, 3, 11, 0, 2, 3, 1, 2, 1, 3, 2, 1, 6, 2, 2, 0, 2, 1, 2, 1]
occupancy_R_coords_jpg_backtracking_15 = [12, 1, 6, 2, 9, 1, 4, 13, 4, 7, 8, 7, 5, 16, 4, 4, 3, 8, 7, 2, 5, 9, 2, 8, 7, 10, 15, 17, 10, 4, 4, 12, 9, 11, 11, 1, 1, 12, 10, 6, 9, 5, 12, 11, 7, 0, 2, 11, 10, 8]
occupancy_R_coords_jpg_false_confidence_15 = [3, 0, 2, 4, 2, 0, 1, 3, 2, 1, 0, 4, 1, 3, 1, 2, 0, 1, 3, 0, 2, 2, 0, 2, 2, 2, 3, 0, 0, 0, 2, 5, 2, 2, 1, 1, 0, 0, 4, 2, 0, 0, 4, 5, 1, 0, 0, 0, 2, 1]
occupancy_R_coords_jpg_frustration_15 = [5, 2, 1, 2, 5, 0, 1, 4, 1, 1, 0, 2, 3, 3, 1, 2, 0, 2, 2, 0, 1, 0, 3, 2, 3, 7, 8, 0, 7, 1, 4, 5, 3, 2, 0, 2, 0, 2, 4, 1, 2, 2, 7, 4, 6, 0, 0, 3, 1, 5]
occupancy_R_coords_jpg_restart_15 = [0, 1, 0, 1, 3, 0, 0, 2, 0, 1, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 1, 5, 0, 3, 1, 0, 4, 2, 0, 0, 0, 0, 1, 3, 1, 0, 1, 2, 1, 0, 0, 0, 1, 1, 2]
occupancy_R_coords_jpg_reverse_search_15 = [0, 0, 2, 0, 3, 0, 1, 0, 0, 3, 0, 1, 1, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 4, 3, 3, 0, 0, 1, 0, 0, 5, 1, 3]
occupancy_R_coords_jpg_step_by_step_15 = [0, 74, 0, 1, 0, 0, 1, 0, 0, 1, 10, 0, 0, 0, 5, 0, 115, 0, 2, 0, 2, 6, 90, 0, 0, 1, 1, 38, 2, 3, 4, 0, 0, 0, 43, 0, 0, 16, 0, 0, 78, 2, 0, 1, 54, 0, 20, 0, 0, 77]
occupancy_R_coords_jpg_verification_15 = [2, 1, 2, 8, 3, 6, 2, 3, 5, 2, 0, 7, 1, 8, 2, 8, 3, 6, 3, 5, 1, 2, 0, 2, 2, 1, 8, 1, 2, 1, 6, 2, 4, 1, 2, 2, 1, 1, 1, 0, 4, 3, 11, 6, 4, 0, 0, 4, 5, 2]
occupancy_R_coords_json_algorithm_15 = [23, 0, 1, 1, 0, 1, 0, 3, 0, 1, 3, 2, 0, 2, 0, 1, 2, 0, 0, 3, 0, 3, 6, 0, 0, 1, 1, 2, 1, 3, 1, 0, 0, 1, 10, 1, 2, 1, 0, 0, 6, 0, 2, 0, 0, 1, 0, 0, 2, 0]
occupancy_R_coords_json_backtracking_15 = [1, 1, 9, 10, 6, 1, 5, 3, 3, 5, 4, 6, 3, 2, 7, 1, 7, 14, 5, 0, 3, 7, 9, 4, 4, 12, 8, 3, 11, 0, 2, 0, 1, 4, 7, 0, 4, 13, 8, 5, 8, 3, 8, 7, 5, 6, 2, 4, 11, 3]
occupancy_R_coords_json_false_confidence_15 = [1, 1, 1, 1, 0, 2, 3, 2, 1, 4, 0, 3, 1, 0, 4, 4, 4, 3, 0, 1, 0, 0, 1, 0, 2, 7, 3, 1, 2, 0, 2, 0, 1, 1, 1, 1, 0, 4, 1, 2, 0, 1, 3, 0, 2, 0, 1, 0, 0, 0]
occupancy_R_coords_json_frustration_15 = [2, 1, 4, 5, 1, 2, 2, 3, 0, 4, 2, 8, 0, 4, 2, 0, 3, 1, 4, 1, 2, 3, 1, 3, 1, 9, 4, 3, 1, 1, 2, 0, 9, 0, 5, 0, 5, 7, 1, 2, 0, 3, 4, 3, 2, 1, 2, 5, 9, 1]
occupancy_R_coords_json_restart_15 = [0, 0, 3, 0, 1, 0, 4, 0, 1, 0, 0, 1, 2, 1, 2, 0, 1, 2, 2, 1, 1, 2, 0, 2, 1, 0, 2, 1, 3, 0, 0, 0, 2, 1, 2, 0, 0, 2, 1, 1, 1, 0, 1, 0, 2, 1, 1, 0, 1, 1]
occupancy_R_coords_json_reverse_search_15 = [0, 0, 2, 1, 0, 3, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 1, 3, 2, 1, 0, 2, 1, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1, 2, 0, 0, 1, 0, 1, 1, 0, 2, 3]
occupancy_R_coords_json_step_by_step_15 = [0, 0, 0, 7, 0, 3, 1, 0, 0, 0, 0, 0, 0, 18, 1, 0, 1, 15, 2, 2, 0, 0, 8, 31, 5, 3, 0, 0, 60, 91, 9, 0, 0, 6, 0, 0, 0, 0, 56, 0, 1, 1, 0, 0, 8, 0, 0, 11, 3, 1]
occupancy_R_coords_json_verification_15 = [3, 2, 3, 2, 2, 4, 4, 8, 3, 7, 3, 5, 3, 0, 1, 7, 8, 1, 4, 6, 7, 2, 2, 10, 8, 7, 10, 2, 9, 2, 2, 2, 9, 0, 4, 2, 3, 3, 3, 2, 7, 3, 5, 5, 4, 5, 4, 2, 8, 7]
occupancy_R_coords_tokenized_txt_algorithm_15 = [8, 2, 1, 4, 0, 1, 0, 1, 1, 0, 2, 5, 2, 0, 0, 0, 6, 0, 1, 2, 4, 1, 0, 0, 0, 2, 1, 0, 9, 0, 0, 1, 1, 0, 5, 1, 0, 1, 0, 0, 5, 1, 5, 3, 4, 1, 2, 0, 0, 8]
occupancy_R_coords_tokenized_txt_backtracking_15 = [7, 5, 12, 6, 3, 1, 6, 5, 13, 9, 8, 6, 28, 5, 6, 0, 4, 2, 5, 4, 10, 6, 9, 11, 11, 3, 2, 5, 4, 8, 8, 10, 8, 9, 10, 2, 4, 5, 17, 12, 13, 7, 6, 5, 4, 9, 6, 5, 8, 10]
occupancy_R_coords_tokenized_txt_false_confidence_15 = [1, 0, 1, 5, 4, 0, 0, 2, 3, 1, 0, 2, 1, 1, 6, 0, 0, 2, 5, 0, 1, 0, 1, 2, 3, 0, 0, 2, 2, 5, 5, 3, 1, 2, 1, 1, 2, 1, 0, 1, 1, 0, 3, 1, 0, 2, 1, 2, 4, 2]
occupancy_R_coords_tokenized_txt_frustration_15 = [3, 4, 2, 6, 1, 2, 5, 3, 8, 5, 5, 0, 13, 4, 1, 0, 0, 1, 1, 4, 1, 3, 1, 3, 2, 3, 0, 3, 2, 12, 5, 8, 2, 6, 3, 5, 3, 4, 11, 4, 1, 5, 0, 5, 2, 2, 3, 1, 1, 5]
occupancy_R_coords_tokenized_txt_restart_15 = [0, 1, 1, 2, 1, 0, 1, 1, 1, 0, 1, 1, 4, 1, 1, 0, 2, 1, 1, 1, 1, 3, 3, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 3, 2, 1, 5, 4, 0, 1, 1, 3, 1, 2, 1, 2]
occupancy_R_coords_tokenized_txt_reverse_search_15 = [2, 0, 0, 0, 0, 0, 3, 0, 2, 3, 1, 0, 5, 2, 5, 0, 1, 3, 1, 1, 1, 2, 2, 4, 3, 0, 0, 0, 3, 3, 2, 6, 1, 7, 2, 1, 1, 2, 2, 3, 2, 0, 1, 3, 2, 3, 0, 2, 7, 0]
occupancy_R_coords_tokenized_txt_step_by_step_15 = [2, 1, 13, 0, 0, 23, 0, 1, 0, 1, 0, 0, 2, 101, 59, 0, 91, 2, 0, 0, 34, 0, 29, 4, 1, 99, 5, 0, 0, 2, 1, 1, 1, 1, 11, 1, 67, 43, 2, 1, 42, 42, 90, 1, 5, 2, 6, 0, 2, 0]
occupancy_R_coords_tokenized_txt_verification_15 = [3, 3, 4, 6, 3, 0, 3, 3, 6, 0, 4, 7, 3, 3, 3, 0, 2, 5, 2, 1, 3, 2, 3, 3, 5, 1, 5, 2, 4, 2, 4, 4, 0, 3, 6, 1, 2, 5, 2, 9, 7, 4, 2, 1, 0, 5, 7, 8, 5, 8]



occurrence_binary_algo_line_adj_json = binary_occurrence(line_R_coords_adj_json_algorithm_15)
occurrence_binary_algo_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_algorithm_15)
occurrence_binary_algo_line_json = binary_occurrence(line_R_coords_json_algorithm_15)
occurrence_binary_algo_line_jpg = binary_occurrence(line_R_coords_jpg_algorithm_15)
occurrence_binary_algo_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_algorithm_15)
occurrence_binary_algo_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_algorithm_15)
occurrence_binary_algo_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_algorithm_15)
occurrence_binary_algo_occ_json = binary_occurrence(occupancy_R_coords_json_algorithm_15)
occurrence_binary_algo_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_algorithm_15)
occurrence_binary_algo_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_algorithm_15)
occurrence_binary_algo_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_algorithm_15)



# List of (occurrence_vector, score_vector, label)
datasets_algorithm = [
    (occurrence_binary_algo_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_algo_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_algo_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_algo_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_algo_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_algo_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_algo_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_algo_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_algo_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_algo_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_algo_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]

occurrence_binary_backtracking_line_adj_json = binary_occurrence(line_R_coords_adj_json_backtracking_15)
occurrence_binary_backtracking_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_backtracking_15)
occurrence_binary_backtracking_line_json = binary_occurrence(line_R_coords_json_backtracking_15)
occurrence_binary_backtracking_line_jpg = binary_occurrence(line_R_coords_jpg_backtracking_15)
occurrence_binary_backtracking_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_backtracking_15)
occurrence_binary_backtracking_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_backtracking_15)
occurrence_binary_backtracking_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_backtracking_15)
occurrence_binary_backtracking_occ_json = binary_occurrence(occupancy_R_coords_json_backtracking_15)
occurrence_binary_backtracking_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_backtracking_15)
occurrence_binary_backtracking_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_backtracking_15)
occurrence_binary_backtracking_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_backtracking_15)


# List of (occurrence_vector, score_vector, label)
datasets_backtracking = [
    (occurrence_binary_backtracking_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_backtracking_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_backtracking_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_backtracking_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_backtracking_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_backtracking_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_backtracking_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_backtracking_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_backtracking_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_backtracking_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_backtracking_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]

occurrence_binary_false_confidence_line_adj_json = binary_occurrence(line_R_coords_adj_json_false_confidence_15)
occurrence_binary_false_confidence_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_false_confidence_15)
occurrence_binary_false_confidence_line_json = binary_occurrence(line_R_coords_json_false_confidence_15)
occurrence_binary_false_confidence_line_jpg = binary_occurrence(line_R_coords_jpg_false_confidence_15)
occurrence_binary_false_confidence_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_false_confidence_15)
occurrence_binary_false_confidence_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_false_confidence_15)
occurrence_binary_false_confidence_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_false_confidence_15)
occurrence_binary_false_confidence_occ_json = binary_occurrence(occupancy_R_coords_json_false_confidence_15)
occurrence_binary_false_confidence_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_false_confidence_15)
occurrence_binary_false_confidence_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_false_confidence_15)
occurrence_binary_false_confidence_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_false_confidence_15)



# List of (occurrence_vector, score_vector, label)
datasets_false_confidence = [
    (occurrence_binary_false_confidence_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_false_confidence_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_false_confidence_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_false_confidence_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_false_confidence_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_false_confidence_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_false_confidence_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_false_confidence_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_false_confidence_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_false_confidence_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_false_confidence_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]

occurrence_binary_frustration_line_adj_json = binary_occurrence(line_R_coords_adj_json_frustration_15)
occurrence_binary_frustration_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_frustration_15)
occurrence_binary_frustration_line_json = binary_occurrence(line_R_coords_json_frustration_15)
occurrence_binary_frustration_line_jpg = binary_occurrence(line_R_coords_jpg_frustration_15)
occurrence_binary_frustration_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_frustration_15)
occurrence_binary_frustration_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_frustration_15)
occurrence_binary_frustration_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_frustration_15)
occurrence_binary_frustration_occ_json = binary_occurrence(occupancy_R_coords_json_frustration_15)
occurrence_binary_frustration_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_frustration_15)
occurrence_binary_frustration_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_frustration_15)
occurrence_binary_frustration_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_frustration_15)


# List of (occurrence_vector, score_vector, label)
datasets_frustration = [
    (occurrence_binary_frustration_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_frustration_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_frustration_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_frustration_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_frustration_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_frustration_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_frustration_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_frustration_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_frustration_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_frustration_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_frustration_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]

occurrence_binary_restart_line_adj_json = binary_occurrence(line_R_coords_adj_json_restart_15)
occurrence_binary_restart_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_restart_15)
occurrence_binary_restart_line_json = binary_occurrence(line_R_coords_json_restart_15)
occurrence_binary_restart_line_jpg = binary_occurrence(line_R_coords_jpg_restart_15)
occurrence_binary_restart_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_restart_15)
occurrence_binary_restart_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_restart_15)
occurrence_binary_restart_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_restart_15)
occurrence_binary_restart_occ_json = binary_occurrence(occupancy_R_coords_json_restart_15)
occurrence_binary_restart_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_restart_15)
occurrence_binary_restart_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_restart_15)
occurrence_binary_restart_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_restart_15)


# List of (occurrence_vector, score_vector, label)
datasets_restart = [
    (occurrence_binary_restart_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_restart_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_restart_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_restart_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_restart_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_restart_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_restart_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_restart_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_restart_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_restart_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_restart_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]


occurrence_binary_reverse_search_line_adj_json = binary_occurrence(line_R_coords_adj_json_reverse_search_15)
occurrence_binary_reverse_search_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_reverse_search_15)
occurrence_binary_reverse_search_line_json = binary_occurrence(line_R_coords_json_reverse_search_15)
occurrence_binary_reverse_search_line_jpg = binary_occurrence(line_R_coords_jpg_reverse_search_15)
occurrence_binary_reverse_search_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_reverse_search_15)
occurrence_binary_reverse_search_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_reverse_search_15)
occurrence_binary_reverse_search_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_reverse_search_15)
occurrence_binary_reverse_search_occ_json = binary_occurrence(occupancy_R_coords_json_reverse_search_15)
occurrence_binary_reverse_search_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_reverse_search_15)
occurrence_binary_reverse_search_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_reverse_search_15)
occurrence_binary_reverse_search_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_reverse_search_15)


# List of (occurrence_vector, score_vector, label)
datasets_reverse_search = [
    (occurrence_binary_reverse_search_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_reverse_search_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_reverse_search_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_reverse_search_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_reverse_search_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_reverse_search_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_reverse_search_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_reverse_search_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_reverse_search_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_reverse_search_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_reverse_search_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]


occurrence_binary_step_by_step_line_adj_json = binary_occurrence(line_R_coords_adj_json_step_by_step_15)
occurrence_binary_step_by_step_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_step_by_step_15)
occurrence_binary_step_by_step_line_json = binary_occurrence(line_R_coords_json_step_by_step_15)
occurrence_binary_step_by_step_line_jpg = binary_occurrence(line_R_coords_jpg_step_by_step_15)
occurrence_binary_step_by_step_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_step_by_step_15)
occurrence_binary_step_by_step_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_step_by_step_15)
occurrence_binary_step_by_step_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_step_by_step_15)
occurrence_binary_step_by_step_occ_json = binary_occurrence(occupancy_R_coords_json_step_by_step_15)
occurrence_binary_step_by_step_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_step_by_step_15)
occurrence_binary_step_by_step_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_step_by_step_15)
occurrence_binary_step_by_step_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_step_by_step_15)


# List of (occurrence_vector, score_vector, label)
datasets_step_by_step = [
    (occurrence_binary_step_by_step_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_step_by_step_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_step_by_step_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_step_by_step_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_step_by_step_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_step_by_step_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_step_by_step_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_step_by_step_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_step_by_step_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_step_by_step_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_step_by_step_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]

occurrence_binary_verification_line_adj_json = binary_occurrence(line_R_coords_adj_json_verification_15)
occurrence_binary_verification_line_adj_txt = binary_occurrence(line_R_coords_adj_txt_verification_15)
occurrence_binary_verification_line_json = binary_occurrence(line_R_coords_json_verification_15)
occurrence_binary_verification_line_jpg = binary_occurrence(line_R_coords_jpg_verification_15)
occurrence_binary_verification_line_tokenized = binary_occurrence(line_R_coords_tokenized_txt_verification_15)
occurrence_binary_verification_occ_adj_json = binary_occurrence(occupancy_R_coords_adj_json_verification_15)
occurrence_binary_verification_occ_adj_txt = binary_occurrence(occupancy_R_coords_adj_txt_verification_15)
occurrence_binary_verification_occ_json = binary_occurrence(occupancy_R_coords_json_verification_15)
occurrence_binary_verification_occ_jpg = binary_occurrence(occupancy_R_coords_jpg_verification_15)
occurrence_binary_verification_occ_tokenized = binary_occurrence(occupancy_R_coords_tokenized_txt_verification_15)
occurrence_binary_verification_occ_ascii = binary_occurrence(occupancy_R_coords_ascii_txt_verification_15)


# List of (occurrence_vector, score_vector, label)
datasets_verification = [
    (occurrence_binary_verification_line_adj_json, r15.line_R_coords_adj_json_15, "Line Adjacency JSON", 'tab:blue', None),
    (occurrence_binary_verification_line_adj_txt, r15.line_R_coords_adj_txt_15, "Line Adjacency Txt", 'tab:orange',None),
    (occurrence_binary_verification_line_json, r15.line_R_coords_json_15, "Line JSON", 'tab:red',None),
    (occurrence_binary_verification_line_jpg, r15.line_R_coords_jpg_15, "Line JPG", 'tab:green',None),
    (occurrence_binary_verification_line_tokenized, r15.line_R_coords_tokenized_txt_15, "Line Tokenized", 'tab:purple',None),
    (occurrence_binary_verification_occ_adj_json, r15.occupancy_R_coords_adj_json_15, "Occupancy Adjacency JSON", 'tab:blue', 'black'),
    (occurrence_binary_verification_occ_adj_txt, r15.occupancy_R_coords_adj_txt_15, "Occupancy Adjacency Txt", 'tab:orange', 'black'),
    (occurrence_binary_verification_occ_json, r15.occupancy_R_coords_json_15, "Occupancy JSON", 'tab:red', 'black'),
    (occurrence_binary_verification_occ_jpg, r15.occupancy_R_coords_jpg_15, "Occupancy JPG", 'tab:green', 'black'),
    (occurrence_binary_verification_occ_tokenized, r15.occupancy_R_coords_tokenized_txt_15, "Occupancy Tokenized", 'tab:purple',  'black'),
    (occurrence_binary_verification_occ_ascii, r15.occupancy_R_coords_ascii_txt_15, "Occupancy ASCII", 'tab:brown', 'black'),
]


# plotting 1 fig with 8 subplots that show occurrence vs completion score

# Create 2x4 subplot grid (8 total)
fig, axes = plt.subplots(2, 4, figsize=(18, 8))
axes = axes.flatten()

def plot_keyword(ax, datasets, title, ylabel):

    x_vals = []
    y_vals = []

    for occurrence_vector, score_vector, label, color, mec in datasets:

        occurrence_vector = np.array(occurrence_vector)
        score_vector = np.array(score_vector)

        y_sum = np.mean(occurrence_vector)
        x_mean = np.mean(score_vector)

        x_vals.append(x_mean)
        y_vals.append(y_sum)

        ax.scatter(
            x_mean,
            y_sum,
            color=color,
            edgecolor=mec,
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

    ax.set_title(title, fontweight = 'bold', fontsize=10)
    ax.set_xlabel('Mean Completion Score (%)')
    ax.set_ylabel(ylabel)
    ax.grid(linestyle=':', alpha=0.6)



plot_keyword(axes[0], datasets_algorithm, "Algorithm",  "Presence (%)")
plot_keyword(axes[1], datasets_backtracking, "Backtracking", "Presence (%)")
plot_keyword(axes[2], datasets_false_confidence, "False Confidence", "Presence (%)")
plot_keyword(axes[3], datasets_frustration, "Frustration", "Presence (%)")
plot_keyword(axes[4], datasets_restart, "Restart", "Presence (%)")
plot_keyword(axes[5], datasets_reverse_search, "Reverse Search", "Presence (%)")
plot_keyword(axes[6], datasets_step_by_step, "Step-by-Step", "Presence (%)")
plot_keyword(axes[7], datasets_verification, "Verification", "Presence (%)")

plt.suptitle('Keyword Categories vs Completion Score \nCoordinates Output, 15x15', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()










# ----- Creates Bar charts comparing avg completion score for present/absent keywords ---
'''Does not show differences in scores achieved, regardless of keyword presence. 
Does show that verification and backtracking always occur. '''
# # Score vector
# scores = np.array(r15.line_R_coords_adj_txt_15)

# # Dictionary of occurrence vectors
# occurrence_dict = {
#     "Algorithm Naming": occurrences_binary_algorithm_15,
#     "Backtracking": occurrences_binary_backtracking_15,
#     "False Confidence": occurrences_binary_false_confidence_15,
#     "Frustration": occurrences_binary_frustration_15,
#     "Restart": occurrences_binary_restart_15,
#     "Reverse Search": occurrences_binary_reverse_search_15,
#     "Step-by-Step": occurrences_binary_step_by_step_15,
#     "Verification": occurrences_binary_verification_15,
# }

# # Create figure with 8 subplots (2 rows × 4 columns)
# fig, axes = plt.subplots(2, 4, figsize=(16, 8), sharex=True)
# axes = axes.flatten()

# for ax, (title, occurrence_vector) in zip(axes, occurrence_dict.items()):
    
#     occurrence_vector = np.array(occurrence_vector)

#     # Separate scores
#     yes_scores = scores[occurrence_vector == 1]
#     no_scores  = scores[occurrence_vector == 0]

#     # Compute means safely
#     mean_yes = np.mean(yes_scores) if len(yes_scores) > 0 else 0
#     mean_no  = np.mean(no_scores) if len(no_scores) > 0 else 0
#     stdev_yes = np.std(yes_scores) if len(yes_scores) >0 else 0
#     stdev_no = np.std(no_scores) if len(no_scores) >0 else 0

#     labels = ['Present, std = {:.1f}'.format(stdev_yes), 'Absent, std = {:.1f}'.format(stdev_no)]
#     means = [mean_yes, mean_no]

#     # Plot horizontal bars
#     ax.barh(labels, means, alpha=0.7)

#     ax.set_title(title, fontsize=10)
#     ax.set_xlim(0, 100)
#     ax.grid(axis='x', linestyle=':', alpha=0.6)

# # Common x-axis label
# fig.supxlabel('Average Completion Score (%)', fontsize=12)
# fig.supylabel('Keyword Occurrence', fontsize=12)

# plt.tight_layout()
# plt.show()



















# ----- Plotting number of used tokens vs number of output characters  - no interesting results. ---------

# # Number of thinking tokens
# # y= r15.line_R_coords_adj_txt_output_tokens_15 - r15.line_R_coords_adj_txt_final_answer_15 

# # Number of final answer tokens
# y=r15.line_R_coords_adj_txt_final_answer_15 

# line_R_coords_adj_txt_thoughts_characters  = np.array([4193, 1312, 1990, 2316, 2283, 2513, 1644, 2192, 2814, 2892])
# x = line_R_coords_adj_txt_thoughts_characters

# # Linear fit
# slope, intercept = np.polyfit(x, y, 1)

# x_fit = np.linspace(x.min(), x.max(), 200)
# y_fit = slope * x_fit + intercept

# # Plot
# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, edgecolor='black', label='data')
# plt.plot(x_fit, y_fit, linestyle='--', linewidth=2, label='trend')

# # Axis labels
# plt.ylabel('number of tokens (-)')
# plt.xlabel('number of characters (-)')

# # Grid
# plt.grid(alpha=0.3)

# # In-figure slope label
# plt.text(
#     0.05, 0.95,
#     f'slope = {slope:.2f} tokens/characters',
#     transform=plt.gca().transAxes,
#     fontsize=11,
#     verticalalignment='top',
#     bbox=dict(boxstyle='round', facecolor=None, alpha=0.8)
# )

# plt.tight_layout()
# # plt.show()





# # -------------------------------------------------------------------------------
# # thinking tokens
# thinking_tokens = r15.line_R_coords_adj_txt_output_tokens_15 - r15.line_R_coords_adj_txt_final_answer_15

# ratio = line_R_coords_adj_txt_thoughts_characters / thinking_tokens
# print(ratio)
# y= ratio

# completion_score = r15.line_R_coords_adj_txt_15
# x = completion_score
# # Linear fit
# slope, intercept = np.polyfit(x, y, 1)

# x_fit = np.linspace(x.min(), x.max(), 200)
# y_fit = slope * x_fit + intercept

# # Plot
# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, edgecolor='black', label='data')
# plt.plot(x_fit, y_fit, linestyle='--', linewidth=2, label='trend')

# # Axis labels
# plt.ylabel('ratio characters/token (-)')
# plt.xlabel('Completion score (%)')

# # Grid
# plt.grid(alpha=0.3)

# # In-figure slope label
# plt.text(
#     0.05, 0.95,
#     f'slope = {slope:.2f}',
#     transform=plt.gca().transAxes,
#     fontsize=11,
#     verticalalignment='top',
#     bbox=dict(boxstyle='round', facecolor=None, alpha=0.8)
# )

# plt.tight_layout()
# plt.show()