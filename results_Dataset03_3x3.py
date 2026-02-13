import numpy as np
import pandas as pd
import dataframe_image as dfi
representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']
"""
List of 110:
occupancy_NR_coords_ascii_txt_3 run 2,3,10
occupancy_NR_coords_json_3 run 2,4, 7, 10
occupancy_NR_coords_tokenized_txt_3 run 2, 10
occupancy_NR_allo_adj_json_3 run 4,7,10
occupancy_NR_allo_ascii_txt_3 run 2
occupancy_NR_allo_tokenized_txt_3 run 10
line_R_ego_jpg_3 run 10
"""

# NR - COORDS - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_NR_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 42.857142857142854, 100.0, 100.0])
line_NR_coords_jpg_3 = np.array([40.0, 20.0, 40.0, 60.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_json_3 = np.array([100.0, 20.0, 60.0, 20.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_tokenized_txt_3 = np.array([20.0, 0.0, 0.0, 60.0, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 20.0])
occupancy_NR_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_ascii_txt_3 = np.array([0.0, 100.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0])
occupancy_NR_coords_jpg_3 = np.array([0.0, 0.0, 55.55555555555556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 7.6923076923076925, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_tokenized_txt_3 = np.array([11.11111111111111, 100.0, 100.0, 100.0, 7.6923076923076925, 11.11111111111111, 100.0, 100.0, 7.6923076923076925, 100.0])

# Raw scores
line_NR_coords_adj_json_raw_score_3 = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_NR_coords_adj_txt_raw_score_3 = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 3.0, 7.0, 5.0])
line_NR_coords_jpg_raw_score_3 = np.array([2.0, 1.0, 2.0, 3.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_NR_coords_json_raw_score_3 = np.array([5.0, 1.0, 3.0, 1.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_NR_coords_tokenized_txt_raw_score_3 = np.array([1.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0])
occupancy_NR_coords_adj_json_raw_score_3 = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_NR_coords_adj_txt_raw_score_3 = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_NR_coords_ascii_txt_raw_score_3 = np.array([0.0, 9.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.0])  
occupancy_NR_coords_jpg_raw_score_3 = np.array([0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_raw_score_3 = np.array([9.0, 9.0, 9.0, 9.0, 1.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_NR_coords_tokenized_txt_raw_score_3 = np.array([1.0, 9.0, 9.0, 9.0, 1.0, 1.0, 9.0, 13.0, 1.0, 9])

# Prompt tokens
line_NR_coords_adj_json_input_tokens_3 = np.array([714, 714, 714, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0])
line_NR_coords_adj_txt_input_tokens_3 = np.array([346, 346, 346, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0])
line_NR_coords_jpg_input_tokens_3 = np.array([429, 429, 429, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0])
line_NR_coords_json_input_tokens_3 = np.array([652, 652, 652, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0])
line_NR_coords_tokenized_txt_input_tokens_3 = np.array([317, 317, 317, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0])
occupancy_NR_coords_adj_json_input_tokens_3 = np.array([1176, 1176, 1176, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0])
occupancy_NR_coords_adj_txt_input_tokens_3 = np.array([458, 458, 458, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0])
occupancy_NR_coords_ascii_txt_input_tokens_3 = np.array([195, 195, 193, 201.0, 201.0, 201.0, 201.0, 201.0, 201.0, 199.0])
occupancy_NR_coords_jpg_input_tokens_3 = np.array([424, 424, 424, 430.0, 430.0, 430.0, 430.0, 430.0, 430.0, 430.0])
occupancy_NR_coords_json_input_tokens_3 = np.array([467, 467, 467, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0])
occupancy_NR_coords_tokenized_txt_input_tokens_3 = np.array([746, 746, 746, 752, 752.0, 752.0, 752.0, 752.0, 752.0, 752])


# Output tokens
line_NR_coords_adj_json_output_tokens_3 = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 29.0, 29.0, 21.0])
line_NR_coords_adj_txt_output_tokens_3 = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 21.0, 29.0, 21.0])
line_NR_coords_jpg_output_tokens_3 = np.array([21, 21, 33, 21.0, 21.0, 21.0, 29.0, 21.0, 21.0, 21.0])
line_NR_coords_json_output_tokens_3 = np.array([21, 21, 21, 17.0, 21.0, 21.0, 17.0, 29.0, 21.0, 21.0])
line_NR_coords_tokenized_txt_output_tokens_3 = np.array([21, 25, 13, 29.0, 17.0, 17.0, 25.0, 21.0, 17.0, 29.0])
occupancy_NR_coords_adj_json_output_tokens_3 = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_NR_coords_adj_txt_output_tokens_3 = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_NR_coords_ascii_txt_output_tokens_3 = np.array([57, 57, 125, 53.0, 41.0, 45.0, 57.0, 41.0, 57.0, 53.0])
occupancy_NR_coords_jpg_output_tokens_3 = np.array([45, 49, 41, 49.0, 73.0, 45.0, 65.0, 41.0, 53.0, 57.0])
occupancy_NR_coords_json_output_tokens_3 = np.array([37, 53, 37, 53.0, 69.0, 37.0, 53.0, 53.0, 53.0, 101.0])
occupancy_NR_coords_tokenized_txt_output_tokens_3 = np.array([41, 53, 37, 37, 49.0, 65.0, 37.0, 53.0, 53.0, 53])

avg_nr_coords_line_jpg_input = np.mean(line_NR_coords_jpg_input_tokens_3)
avg_nr_coords_line_json_input = np.mean(line_NR_coords_json_input_tokens_3)
avg_nr_coords_occupancy_jpg_input = np.mean(occupancy_NR_coords_jpg_input_tokens_3)
avg_nr_coords_occupancy_json_input = np.mean(occupancy_NR_coords_json_input_tokens_3)
avg_nr_coords_line_adj_json_input = np.mean(line_NR_coords_adj_json_input_tokens_3)
avg_nr_coords_line_adj_txt_input = np.mean(line_NR_coords_adj_txt_input_tokens_3)
avg_nr_coords_line_tokenized_txt_input = np.mean(line_NR_coords_tokenized_txt_input_tokens_3)
avg_nr_coords_occupancy_adj_json_input = np.mean(occupancy_NR_coords_adj_json_input_tokens_3)
avg_nr_coords_occupancy_adj_txt_input = np.mean(occupancy_NR_coords_adj_txt_input_tokens_3)
avg_nr_coords_occupancy_ascii_txt_input = np.mean(occupancy_NR_coords_ascii_txt_input_tokens_3)
avg_nr_coords_occupancy_tokenized_txt_input = np.mean(occupancy_NR_coords_tokenized_txt_input_tokens_3)
avg_nr_coords_line_jpg_output = np.mean(line_NR_coords_jpg_output_tokens_3)
avg_nr_coords_line_json_output = np.mean(line_NR_coords_json_output_tokens_3)
avg_nr_coords_occupancy_jpg_output = np.mean(occupancy_NR_coords_jpg_output_tokens_3)
avg_nr_coords_occupancy_json_output = np.mean(occupancy_NR_coords_json_output_tokens_3)
avg_nr_coords_line_adj_json_output = np.mean(line_NR_coords_adj_json_output_tokens_3)
avg_nr_coords_line_adj_txt_output = np.mean(line_NR_coords_adj_txt_output_tokens_3)
avg_nr_coords_line_tokenized_txt_output = np.mean(line_NR_coords_tokenized_txt_output_tokens_3)
avg_nr_coords_occupancy_adj_json_output = np.mean(occupancy_NR_coords_adj_json_output_tokens_3)
avg_nr_coords_occupancy_adj_txt_output = np.mean(occupancy_NR_coords_adj_txt_output_tokens_3)
avg_nr_coords_occupancy_ascii_txt_output = np.mean(occupancy_NR_coords_ascii_txt_output_tokens_3)
avg_nr_coords_occupancy_tokenized_txt_output = np.mean(occupancy_NR_coords_tokenized_txt_output_tokens_3)


# Set up runs for table
# x_axis = [1,2,3,4,5,6,7,8,9,10]
# complexities = [f"Run {x_axis[i]}" for i in range(10)]

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


# NR - ALLO - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_allo_adj_json_3 = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 100.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_adj_txt_3 = np.array([0.0, 100.0, 0.0, 100.0, 0.0, 0.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_jpg_3 = np.array([50.0, 0.0, 50.0, 100.0, 33.33333333333333, 50.0, 100.0, 0.0, 0.0, 0.0])
line_NR_allo_json_3 = np.array([100.0, 0.0, 100.0, 0.0, 33.33333333333333, 100.0, 0.0, 0.0, 33.33333333333333, 0.0])
line_NR_allo_tokenized_txt_3 = np.array([0.0, 100.0, 0.0, 25.0, 0.0, 0.0, 25.0, 33.33333333333333, 0.0, 25.0])
occupancy_NR_allo_adj_json_3 = np.array([50.0, 25.0, 75.0, 100.0, 0.0, 50.0, 100.0, 33.33333333333333, 0.0, 100.0])
occupancy_NR_allo_adj_txt_3 = np.array([62.5, 25.0, 0.0, 37.5, 33.33333333333333, 25.0, 37.5, 33.33333333333333, 0.0, 100.0])
occupancy_NR_allo_ascii_txt_3 = np.array([0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 62.5, 33.33333333333333, 33.33333333333333, 0.0])
occupancy_NR_allo_jpg_3 = np.array([12.5, 0.0, 12.5, 0.0, 8.333333333333332, 12.5, 12.5, 8.333333333333332, 8.333333333333332, 0.0])
occupancy_NR_allo_json_3 = np.array([62.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 33.33333333333333, 0.0, 87.5])
occupancy_NR_allo_tokenized_txt_3 = np.array([0.0, 0.0, 0.0, 50.0, 8.333333333333332, 12.5, 0.0, 8.333333333333332, 0.0, 100.0])


# Raw Scores
line_NR_allo_adj_json_raw_score_3 = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 4.0, 4.0, 2.0, 2.0, 4.0])
line_NR_allo_adj_txt_raw_score_3 = np.array([0.0, 4.0, 0.0, 4.0, 0.0, 0.0, 4.0, 2.0, 2.0, 4.0])
line_NR_allo_jpg_raw_score_3 = np.array([2.0, 0.0, 2.0, 4.0, 2.0, 2.0, 4.0, 0.0, 0.0, 0.0])
line_NR_allo_json_raw_score_3 = np.array([4.0, 0.0, 4.0, 0.0, 2.0, 4.0, 0.0, 0.0, 2.0, 0.0])
line_NR_allo_tokenized_txt_raw_score_3 = np.array([0.0, 4.0, 0.0, 1.0, 0.0, 0.0, 1.0, 2.0, 0.0, 1.0])
occupancy_NR_allo_adj_json_raw_score_3 = np.array([4.0, 2.0, 6.0, 8.0, 0.0, 4.0, 8.0, 4.0, 0.0, 8.0])
occupancy_NR_allo_adj_txt_raw_score_3 = np.array([5.0, 2.0, 0.0, 3.0, 4.0, 2.0, 3.0, 4.0, 0.0, 8.0])
occupancy_NR_allo_ascii_txt_raw_score_3 = np.array([0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 5.0, 4.0, 4.0, 0.0])
occupancy_NR_allo_jpg_raw_score_3 = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
occupancy_NR_allo_json_raw_score_3 = np.array([5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 7.0])
occupancy_NR_allo_tokenized_txt_raw_score_3 = np.array([0.0, 0.0, 0.0, 4.0, 1.0, 1.0, 0.0, 1.0, 0.0, 8.0])

# Prompt tokens
line_NR_allo_adj_json_input_tokens_3 = np.array([706.0, 706.0, 706.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0])
line_NR_allo_adj_txt_input_tokens_3 = np.array([338.0, 338.0, 338.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0])
line_NR_allo_jpg_input_tokens_3 = np.array([421.0, 421.0, 421.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0])
line_NR_allo_json_input_tokens_3 = np.array([644.0, 644.0, 644.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_allo_tokenized_txt_input_tokens_3 = np.array([309.0, 309.0, 309.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0])
occupancy_NR_allo_adj_json_input_tokens_3 = np.array([1168.0, 1168.0, 1168.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0])
occupancy_NR_allo_adj_txt_input_tokens_3 = np.array([450.0, 450.0, 450.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0])
occupancy_NR_allo_ascii_txt_input_tokens_3 = np.array([187.0, 187.0, 185.0, 193.0, 193.0, 193.0, 193.0, 193.0, 193.0, 191.0])
occupancy_NR_allo_jpg_input_tokens_3 = np.array([416.0, 416.0, 416.0, 422.0, 422.0, 422.0, 422.0, 422.0, 422.0, 422.0])
occupancy_NR_allo_json_input_tokens_3 = np.array([459.0, 459.0, 459.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0])
occupancy_NR_allo_tokenized_txt_input_tokens_3 = np.array([738.0, 738.0, 738.0, 744.0, 744.0, 744.0, 744.0, 744.0, 743.0, 743.0])


# Output tokens
line_NR_allo_adj_json_output_tokens_3 = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 5.0, 7.0])
line_NR_allo_adj_txt_output_tokens_3 = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_jpg_output_tokens_3 = np.array([7.0, 218.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_json_output_tokens_3 = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_tokenized_txt_output_tokens_3 = np.array([5.0, 7.0, 5.0, 7.0, 7.0, 7.0, 7.0, 7.0, 5.0, 7.0])
occupancy_NR_allo_adj_json_output_tokens_3 = np.array([17.0, 15.0, 21.0, 19.0, 21.0, 17.0, 19.0, 19.0, 650.0, 19.0])
occupancy_NR_allo_adj_txt_output_tokens_3 = np.array([21.0, 17.0, 1734.0, 15.0, 13.0, 17.0, 15.0, 15.0, 650.0, 19.0])
occupancy_NR_allo_ascii_txt_output_tokens_3 = np.array([43.0, 29.0, 43.0, 23.0, 39.0, 31.0, 25.0, 31.0, 21.0, 29.0])
occupancy_NR_allo_jpg_output_tokens_3 = np.array([21.0, 15.0, 15.0, 49.0, 21.0, 43.0, 19.0, 17.0, 21.0, 198.0])
occupancy_NR_allo_json_output_tokens_3 = np.array([17.0, 21.0, 45.0, 21.0, 29.0, 31.0, 21.0, 21.0, 650.0, 35.0])
occupancy_NR_allo_tokenized_txt_output_tokens_3 = np.array([33.0, 59.0, 4000.0, 650.0, 31.0, 650.0, 31.0, 25.0, 650.0, 650.0])

avg_nr_allo_line_jpg_input = np.mean(line_NR_allo_jpg_input_tokens_3)
avg_nr_allo_line_json_input = np.mean(line_NR_allo_json_input_tokens_3)
avg_nr_allo_occupancy_jpg_input = np.mean(occupancy_NR_allo_jpg_input_tokens_3)
avg_nr_allo_occupancy_json_input = np.mean(occupancy_NR_allo_json_input_tokens_3)
avg_nr_allo_line_adj_json_input = np.mean(line_NR_allo_adj_json_input_tokens_3)
avg_nr_allo_line_adj_txt_input = np.mean(line_NR_allo_adj_txt_input_tokens_3)
avg_nr_allo_line_tokenized_txt_input = np.mean(line_NR_allo_tokenized_txt_input_tokens_3)
avg_nr_allo_occupancy_adj_json_input = np.mean(occupancy_NR_allo_adj_json_input_tokens_3)
avg_nr_allo_occupancy_adj_txt_input = np.mean(occupancy_NR_allo_adj_txt_input_tokens_3)
avg_nr_allo_occupancy_ascii_txt_input = np.mean(occupancy_NR_allo_ascii_txt_input_tokens_3)
avg_nr_allo_occupancy_tokenized_txt_input = np.mean(occupancy_NR_allo_tokenized_txt_input_tokens_3)
avg_nr_allo_line_jpg_output = np.mean(line_NR_allo_jpg_output_tokens_3)
avg_nr_allo_line_json_output = np.mean(line_NR_allo_json_output_tokens_3)
avg_nr_allo_occupancy_jpg_output = np.mean(occupancy_NR_allo_jpg_output_tokens_3)
avg_nr_allo_occupancy_json_output = np.mean(occupancy_NR_allo_json_output_tokens_3)
avg_nr_allo_line_adj_json_output = np.mean(line_NR_allo_adj_json_output_tokens_3)
avg_nr_allo_line_adj_txt_output = np.mean(line_NR_allo_adj_txt_output_tokens_3)
avg_nr_allo_line_tokenized_txt_output = np.mean(line_NR_allo_tokenized_txt_output_tokens_3)
avg_nr_allo_occupancy_adj_json_output = np.mean(occupancy_NR_allo_adj_json_output_tokens_3)
avg_nr_allo_occupancy_adj_txt_output = np.mean(occupancy_NR_allo_adj_txt_output_tokens_3)
avg_nr_allo_occupancy_ascii_txt_output = np.mean(occupancy_NR_allo_ascii_txt_output_tokens_3)
avg_nr_allo_occupancy_tokenized_txt_output = np.mean(occupancy_NR_allo_tokenized_txt_output_tokens_3)


# Set up complexities for table
# x_axis = [1, 2, 3, 4,5,6,7,8,9,10]
# complexities = [f"Run {x_axis[i]}" for i in range(10)]

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

# NR - EGO - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_ego_adj_json_3 = np.array([25.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json_3 = np.array([25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json_3 = np.array([0.0, 0.0, 12.5, 0.0, 8.333333333333332, 0.0, 0.0, 0.0, 8.333333333333332, 0.0])
occupancy_NR_ego_adj_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_3 = np.array([0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_json_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])


# Raw Scores
line_NR_ego_adj_json_raw_score_3 = np.array([1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_raw_score_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg_raw_score_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json_raw_score_3 = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt_raw_score_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json_raw_score_3 = np.array([0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0])
occupancy_NR_ego_adj_txt_raw_score_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt_raw_score_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_raw_score_3 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_json_raw_score_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt_raw_score_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0])

# Prompt tokens
line_NR_ego_adj_json_input_tokens_3 = np.array([816.0, 816.0, 816.0, 836.0, 836.0, 836.0, 836.0, 836.0, 836.0, 836.0])
line_NR_ego_adj_txt_input_tokens_3 = np.array([448.0, 448.0, 448.0, 468.0, 468.0, 468.0, 468.0, 468.0, 468.0, 468.0])
line_NR_ego_jpg_input_tokens_3 = np.array([531.0, 531.0, 531.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0])
line_NR_ego_json_input_tokens_3 = np.array([754.0, 754.0, 754.0, 774.0, 774.0, 774.0, 774.0, 774.0, 774.0, 774.0])
line_NR_ego_tokenized_txt_input_tokens_3 = np.array([419.0, 419.0, 419.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0])
occupancy_NR_ego_adj_json_input_tokens_3 = np.array([1278.0, 1278.0, 1278.0, 1298.0, 1298.0, 1298.0, 1298.0, 1298.0, 1298.0, 1298.0])
occupancy_NR_ego_adj_txt_input_tokens_3 = np.array([560.0, 560.0, 560.0, 580.0, 580.0, 580.0, 580.0, 580.0, 580.0, 580.0])
occupancy_NR_ego_ascii_txt_input_tokens_3 = np.array([297.0, 297.0, 295.0, 317.0, 317.0, 317.0, 317.0, 317.0, 317.0, 315.0])
occupancy_NR_ego_jpg_input_tokens_3 = np.array([526.0, 526.0, 526.0, 546.0, 546.0, 546.0, 546.0, 546.0, 546.0, 546.0])
occupancy_NR_ego_json_input_tokens_3 = np.array([569.0, 569.0, 569.0, 589.0, 589.0, 589.0, 589.0, 589.0, 589.0, 589.0])
occupancy_NR_ego_tokenized_txt_input_tokens_3 = np.array([848.0, 848.0, 848.0, 868.0, 867.0, 867.0, 867.0, 867.0, 867.0, 867])


# Output tokens
line_NR_ego_adj_json_output_tokens_3 = np.array([13.0, 4000.0, 11.0, 15.0, 15.0, 13.0, 15.0, 13.0, 15.0, 15.0])
line_NR_ego_adj_txt_output_tokens_3 = np.array([15.0, 17.0, 13.0, 11.0, 13.0, 13.0, 15.0, 13.0, 13.0, 13.0])
line_NR_ego_jpg_output_tokens_3 = np.array([23.0, 17.0, 15.0, 15.0, 261.0, 15.0, 15.0, 650.0, 19.0, 19.0])
line_NR_ego_json_output_tokens_3 = np.array([11.0, 11.0, 13.0, 19.0, 13.0, 21.0, 17.0, 11.0, 11.0, 11.0])
line_NR_ego_tokenized_txt_output_tokens_3 = np.array([17.0, 4000.0, 17.0, 649.0, 650.0, 517.0, 650.0, 47.0, 650.0, 650.0])
occupancy_NR_ego_adj_json_output_tokens_3 = np.array([33.0, 4000.0, 31.0, 99.0, 49.0, 35.0, 41.0, 39.0, 47.0, 29.0])
occupancy_NR_ego_adj_txt_output_tokens_3 = np.array([4000.0, 49.0, 4000.0, 49.0, 650.0, 436.0, 49.0, 45.0, 650.0, 49.0])
occupancy_NR_ego_ascii_txt_output_tokens_3 = np.array([133.0, 4000.0, 4000.0, 35.0, 650.0, 51.0, 650.0, 51.0, 650.0, 47.0])
occupancy_NR_ego_jpg_output_tokens_3 = np.array([25.0, 27.0, 33.0, 23.0, 27.0, 650.0, 35.0, 27.0, 35.0, 43.0])
occupancy_NR_ego_json_output_tokens_3 = np.array([4000.0, 4000.0, 79.0, 55.0, 650.0, 650.0, 650.0, 650.0, 41.0, 650.0])
occupancy_NR_ego_tokenized_txt_output_tokens_3 = np.array([4000.0, 1561.0, 1029.0, 49.0, 650.0, 650.0, 650.0, 650.0, 45.0, 650])

avg_nr_ego_line_jpg_input = np.mean(line_NR_ego_jpg_input_tokens_3)
avg_nr_ego_line_json_input = np.mean(line_NR_ego_json_input_tokens_3)
avg_nr_ego_occupancy_jpg_input = np.mean(occupancy_NR_ego_jpg_input_tokens_3)
avg_nr_ego_occupancy_json_input = np.mean(occupancy_NR_ego_json_input_tokens_3)
avg_nr_ego_line_adj_json_input = np.mean(line_NR_ego_adj_json_input_tokens_3)
avg_nr_ego_line_adj_txt_input = np.mean(line_NR_ego_adj_txt_input_tokens_3)
avg_nr_ego_line_tokenized_txt_input = np.mean(line_NR_ego_tokenized_txt_input_tokens_3)
avg_nr_ego_occupancy_adj_json_input = np.mean(occupancy_NR_ego_adj_json_input_tokens_3)
avg_nr_ego_occupancy_adj_txt_input = np.mean(occupancy_NR_ego_adj_txt_input_tokens_3)
avg_nr_ego_occupancy_ascii_txt_input = np.mean(occupancy_NR_ego_ascii_txt_input_tokens_3)
avg_nr_ego_occupancy_tokenized_txt_input = np.mean(occupancy_NR_ego_tokenized_txt_input_tokens_3)
avg_nr_ego_line_jpg_output = np.mean(line_NR_ego_jpg_output_tokens_3)
avg_nr_ego_line_json_output = np.mean(line_NR_ego_json_output_tokens_3)
avg_nr_ego_occupancy_jpg_output = np.mean(occupancy_NR_ego_jpg_output_tokens_3)
avg_nr_ego_occupancy_json_output = np.mean(occupancy_NR_ego_json_output_tokens_3)
avg_nr_ego_line_adj_json_output = np.mean(line_NR_ego_adj_json_output_tokens_3)
avg_nr_ego_line_adj_txt_output = np.mean(line_NR_ego_adj_txt_output_tokens_3)
avg_nr_ego_line_tokenized_txt_output = np.mean(line_NR_ego_tokenized_txt_output_tokens_3)
avg_nr_ego_occupancy_adj_json_output = np.mean(occupancy_NR_ego_adj_json_output_tokens_3)
avg_nr_ego_occupancy_adj_txt_output = np.mean(occupancy_NR_ego_adj_txt_output_tokens_3)
avg_nr_ego_occupancy_ascii_txt_output = np.mean(occupancy_NR_ego_ascii_txt_output_tokens_3)
avg_nr_ego_occupancy_tokenized_txt_output = np.mean(occupancy_NR_ego_tokenized_txt_output_tokens_3)

# # Set up complexities for table
# x_axis = [1, 2, 3,4,5,6,7,8,9,10]
# complexities = [f"Run {x_axis[i]}" for i in range(10)]

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

# # R - COORDS -  - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_jpg_3 = np.array([40.0, 100.0, 100.0, 100.0, 28.57142857142857, 40.0, 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 28.57142857142857, 44.44444444444444, 20.0, 44.44444444444444, 57.14285714285714, 20.0, 110.00000000000001, 100.0, 14.285714285714285, 60.0, 100.0, 100.0, 0.0, 100.0, 44.44444444444444, 60.0, 100.0])
line_R_coords_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_ascii_txt_3 = np.array([22.22222222222222, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 46.15384615384615, 77.77777777777779, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 69.23076923076923, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_jpg_3 = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556, 0.0, 7.6923076923076925, 11.11111111111111, 33.33333333333333, 0.0, 7.6923076923076925, 100.0, 100.0, 66.66666666666666, 33.33333333333333, 30.76923076923077, 23.52941176470588, 100.0, 0.0, 53.84615384615385, 100.0, 11.11111111111111, 7.6923076923076925, 0.0, 11.11111111111111, 0.0, 11.11111111111111, 11.11111111111111, 33.33333333333333, 35.294117647058826, 11.11111111111111, 11.11111111111111])
occupancy_R_coords_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_R_coords_adj_json_raw_score_3 = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 5.0, 5.0, 5.0, 7.0, 9.0, 5.0, 9.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 9.0, 5.0, 5.0, 5.0, 9.0, 5.0, 5.0])
line_R_coords_adj_txt_raw_score_3 = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 5.0, 5.0, 5.0, 7.0, 9.0, 5.0, 9.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 9.0, 5.0, 5.0, 5.0, 9.0, 5.0, 5.0])
line_R_coords_jpg_raw_score_3 = np.array([2.0, 5.0, 5.0, 5.0, 2.0, 2.0, 2.0, 7.0, 7.0, 5.0, 5.0, 5.0, 5.0, 2.0, 4.0, 1.0, 4.0, 4.0, 1.0, 5.0, 7.0, 1.0, 3.0, 9.0, 5.0, 0.0, 5.0, 4.0, 3.0, 5.0])
line_R_coords_json_raw_score_3 = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 5.0, 5.0, 5.0, 7.0, 9.0, 5.0, 9.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 9.0, 5.0, 5.0, 5.0, 9.0, 5.0, 5.0])
line_R_coords_tokenized_txt_raw_score_3 = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 5.0, 5.0, 5.0, 7.0, 9.0, 5.0, 9.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 9.0, 5.0, 5.0, 5.0, 9.0, 5.0, 5.0])
occupancy_R_coords_adj_json_raw_score_3 = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 9.0, 9.0, 9.0, 13.0, 17.0, 9.0, 17.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 17.0, 9.0, 9.0, 9.0, 17.0, 9.0, 9.0])
occupancy_R_coords_adj_txt_raw_score_3 = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 9.0, 9.0, 9.0, 13.0, 17.0, 9.0, 17.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 17.0, 9.0, 9.0, 9.0, 17.0, 9.0, 9.0])
occupancy_R_coords_ascii_txt_raw_score_3 = np.array([2.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 6.0, 7.0, 9.0, 9.0, 9.0, 13.0, 17.0, 9.0, 17.0, 9.0, 9.0, 9.0, 13.0, 13.0, 9.0, 17.0, 9.0, 9.0, 9.0, 17.0, 9.0, 9.0])
occupancy_R_coords_jpg_raw_score_3 = np.array([1.0, 2.0, 5.0, 0.0, 1.0, 1.0, 3.0, 0.0, 1.0, 9.0, 9.0, 6.0, 3.0, 4.0, 4.0, 9.0, 0.0, 7.0, 9.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 3.0, 6.0, 1.0, 1.0])
occupancy_R_coords_json_raw_score_3 = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 9.0, 9.0, 9.0, 13.0, 17.0, 9.0, 17.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 17.0, 9.0, 9.0, 9.0, 17.0, 9.0, 9.0])
occupancy_R_coords_tokenized_txt_raw_score_3 = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 9.0, 9.0, 9.0, 13.0, 17.0, 9.0, 17.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0, 17.0, 9.0, 9.0, 9.0, 17.0, 9.0, 9])


# Prompt tokens
line_R_coords_adj_json_input_tokens_3 = np.array([714.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0, 727.0])
line_R_coords_adj_txt_input_tokens_3 = np.array([346.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0, 359.0])
line_R_coords_jpg_input_tokens_3 = np.array([429.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0])
line_R_coords_json_input_tokens_3 = np.array([652.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0, 665.0])
line_R_coords_tokenized_txt_input_tokens_3 = np.array([317.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0, 330.0])
occupancy_R_coords_adj_json_input_tokens_3 = np.array([1176.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1183.0, 1183.0, 1183.0, 1189.0, 1189.0, 1189.0, 1183.0, 1189.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0, 1183.0])
occupancy_R_coords_adj_txt_input_tokens_3 = np.array([458.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0, 471.0])
occupancy_R_coords_ascii_txt_input_tokens_3 = np.array([194.0, 200.0, 198.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 198.0, 208.0, 207.0, 208.0, 209.0, 203.0, 207.0, 210.0, 205.0, 207.0, 205.0, 207.0, 207.0, 205.0, 210.0, 208.0, 205.0, 207.0, 210.0, 205.0, 205.0])
occupancy_R_coords_jpg_input_tokens_3 = np.array([434.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0, 447.0])
occupancy_R_coords_json_input_tokens_3 = np.array([467.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0, 480.0])
occupancy_R_coords_tokenized_txt_input_tokens_3 = np.array([746.0, 752.0, 752.0, 752.0, 751.0, 751.0, 751.0, 751.0, 751.0, 751.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758.0, 758])


# Output tokens
line_R_coords_adj_json_output_tokens_3 = np.array([1625.0, 1289.0, 898.0, 1267.0, 1428.0, 1180.0, 890.0, 1952.0, 4861.0, 1630.0, 1085.0, 992.0, 968.0, 1573.0, 1496.0, 765.0, 1524.0, 1056.0, 1774.0, 1290.0, 1433.0, 2353.0, 743.0, 1573.0, 1138.0, 1578.0, 966.0, 2042.0, 1101.0, 1315.0])
line_R_coords_adj_txt_output_tokens_3 = np.array([2264.0, 2798.0, 2034.0, 1651.0, 2376.0, 2688.0, 1336.0, 2837.0, 3894.0, 2971.0, 2175.0, 1768.0, 1098.0, 2180.0, 1539.0, 1966.0, 1558.0, 1550.0, 1839.0, 3780.0, 1569.0, 1707.0, 1266.0, 1609.0, 3359.0, 1929.0, 1542.0, 2421.0, 3654.0, 1855.0])
line_R_coords_jpg_output_tokens_3 = np.array([16131.0, 5588.0, 3890.0, 10788.0, 4661.0, 11346.0, 3181.0, 1811.0, 1099.0, 4869.0, 3700.0, 758.0, 2510.0, 871.0, 1049.0, 1528.0, 2918.0, 5317.0, 1127.0, 6011.0, 7404.0, 1509.0, 1524.0, 3826.0, 1877.0, 2627.0, 725.0, 1980.0, 1299.0, 1037.0])
line_R_coords_json_output_tokens_3 = np.array([1475.0, 1115.0, 1274.0, 1052.0, 2496.0, 1404.0, 1518.0, 1683.0, 1329.0, 2682.0, 1519.0, 1900.0, 1341.0, 1828.0, 1753.0, 1370.0, 2804.0, 1297.0, 1791.0, 1158.0, 1452.0, 1339.0, 935.0, 2425.0, 1364.0, 938.0, 894.0, 2180.0, 1404.0, 1116.0])
line_R_coords_tokenized_txt_output_tokens_3 = np.array([1408.0, 1207.0, 1637.0, 1361.0, 2974.0, 1260.0, 1333.0, 1614.0, 1760.0, 1755.0, 1724.0, 2298.0, 1432.0, 1921.0, 1792.0, 1957.0, 1680.0, 1387.0, 1689.0, 1205.0, 1556.0, 1663.0, 1745.0, 1925.0, 1246.0, 1495.0, 1135.0, 3553.0, 1177.0, 1015.0])
occupancy_R_coords_adj_json_output_tokens_3 = np.array([2077.0, 2469.0, 3461.0, 3086.0, 3367.0, 1825.0, 4614.0, 3247.0, 5275.0, 2957.0, 1421.0, 1349.0, 3812.0, 2482.0, 2724.0, 2267.0, 3325.0, 1996.0, 2246.0, 1502.0, 2188.0, 4942.0, 1634.0, 2623.0, 2824.0, 2489.0, 1829.0, 2937.0, 1803.0, 1926.0])
occupancy_R_coords_adj_txt_output_tokens_3 = np.array([3621.0, 4114.0, 3696.0, 3970.0, 6715.0, 3728.0, 3978.0, 2455.0, 6534.0, 1944.0, 1999.0, 2945.0, 2044.0, 2654.0, 2013.0, 2042.0, 2559.0, 2189.0, 2109.0, 2249.0, 4403.0, 2068.0, 2342.0, 3067.0, 1647.0, 2582.0, 2958.0, 2696.0, 1724.0, 2476.0])
occupancy_R_coords_ascii_txt_output_tokens_3 = np.array([9407.0, 8884.0, 1926.0, 6484.0, 2357.0, 3312.0, 2518.0, 2395.0, 2447.0, 2544.0, 1784.0, 1895.0, 5777.0, 5528.0, 4056.0, 3448.0, 1057.0, 2042.0, 3344.0, 9948.0, 2094.0, 1862.0, 4474.0, 845.0, 3115.0, 3647.0, 1847.0, 902.0, 2787.0, 1525.0])
occupancy_R_coords_jpg_output_tokens_3 = np.array([1713.0, 1428.0, 7030.0, 3242.0, 1008.0, 1835.0, 832.0, 2965.0, 1402.0, 3035.0, 9810.0, 1027.0, 2436.0, 1690.0, 904.0, 3272.0, 4644.0, 1810.0, 5602.0, 1156.0, 1221.0, 1808.0, 1164.0, 3322.0, 1902.0, 761.0, 1137.0, 6462.0, 1217.0, 1298.0])
occupancy_R_coords_json_output_tokens_3 = np.array([3193.0, 2760.0, 4692.0, 5823.0, 2167.0, 3396.0, 4635.0, 2380.0, 4836.0, 3947.0, 2745.0, 2889.0, 1875.0, 2511.0, 1490.0, 2129.0, 2468.0, 2140.0, 6451.0, 3743.0, 2748.0, 2496.0, 1595.0, 1363.0, 3925.0, 1729.0, 2649.0, 2010.0, 1831.0, 1398.0])
occupancy_R_coords_tokenized_txt_output_tokens_3 = np.array([4248.0, 2453.0, 2759.0, 3372.0, 5675.0, 4171.0, 2481.0, 4070.0, 1732.0, 5926.0, 2053.0, 4045.0, 2233.0, 2795.0, 1785.0, 7201.0, 2948.0, 2573.0, 9093.0, 2902.0, 2474.0, 1349.0, 3788.0, 3215.0, 1508.0, 1547.0, 4213.0, 2389.0, 2301.0, 2783])

# Final answer only output tokens
line_R_coords_jpg_final_answer_3 = np.array([21.0, 21.0, 21.0, np.nan, 21.0, np.nan, np.nan,29.0, np.nan, 21.0])
line_R_coords_json_final_answer_3 = np.array([21.0, 21.0, 21.0, np.nan, 29.0, np.nan, np.nan, 29.0, np.nan, 21.0])
line_R_coords_adj_json_final_answer_3 = np.array([21.0, 21.0, 21.0, np.nan, 29.0, np.nan, np.nan, 29.0, np.nan, 21.0])
line_R_coords_adj_txt_final_answer_3 = np.array([21.0, 21.0, 21.0, np.nan, 29.0, np.nan, np.nan, 29.0, np.nan, 21.0])
line_R_coords_tokenized_txt_final_answer_3 = np.array([21.0, 21.0, 21.0, np.nan, 29.0, np.nan, np.nan, 29.0, np.nan, 21.0])
occupancy_R_coords_jpg_final_answer_3 = np.array([45.0, 45.0, 33.0, np.nan, 57.0, np.nan, np.nan, 41.0, np.nan ,37.0])
occupancy_R_coords_json_final_answer_3 = np.array([37.0, 37.0, 37.0, np.nan, 53.0, np.nan, np.nan, 53.0, np.nan, 37.0])
occupancy_R_coords_adj_json_final_answer_3 = np.array([37.0, 37.0, 37.0, np.nan, 53.0, np.nan, np.nan, 53.0, np.nan, 37.0])
occupancy_R_coords_adj_txt_final_answer_3 = np.array([37.0, 37.0, 37.0, np.nan, 53.0, np.nan, np.nan, 53.0, np.nan, 37.0])
occupancy_R_coords_tokenized_txt_final_answer_3 = np.array([37.0, 37.0, 37.0, np.nan, 53.0, np.nan, np.nan, 53.0, np.nan, 37.0])
occupancy_R_coords_ascii_txt_final_answer_3 = np.array([37.0, 37.0, 37.0, np.nan , 53.0, np.nan, np.nan, 53.0, np.nan, 45.0])


avg_r_coords_line_jpg_input = np.mean(line_R_coords_jpg_input_tokens_3)
avg_r_coords_line_json_input = np.mean(line_R_coords_json_input_tokens_3)
avg_r_coords_occupancy_jpg_input = np.mean(occupancy_R_coords_jpg_input_tokens_3)
avg_r_coords_occupancy_json_input = np.mean(occupancy_R_coords_json_input_tokens_3)
avg_r_coords_line_adj_json_input = np.mean(line_R_coords_adj_json_input_tokens_3)
avg_r_coords_line_adj_txt_input = np.mean(line_R_coords_adj_txt_input_tokens_3)
avg_r_coords_line_tokenized_txt_input = np.mean(line_R_coords_tokenized_txt_input_tokens_3)
avg_r_coords_occupancy_adj_json_input = np.mean(occupancy_R_coords_adj_json_input_tokens_3)
avg_r_coords_occupancy_adj_txt_input = np.mean(occupancy_R_coords_adj_txt_input_tokens_3)
avg_r_coords_occupancy_ascii_txt_input = np.mean(occupancy_R_coords_ascii_txt_input_tokens_3)
avg_r_coords_occupancy_tokenized_txt_input = np.mean(occupancy_R_coords_tokenized_txt_input_tokens_3)
avg_r_coords_line_jpg_output = np.mean(line_R_coords_jpg_output_tokens_3)
avg_r_coords_line_json_output = np.mean(line_R_coords_json_output_tokens_3)
avg_r_coords_occupancy_jpg_output = np.mean(occupancy_R_coords_jpg_output_tokens_3)
avg_r_coords_occupancy_json_output = np.mean(occupancy_R_coords_json_output_tokens_3)
avg_r_coords_line_adj_json_output = np.mean(line_R_coords_adj_json_output_tokens_3)
avg_r_coords_line_adj_txt_output = np.mean(line_R_coords_adj_txt_output_tokens_3)
avg_r_coords_line_tokenized_txt_output = np.mean(line_R_coords_tokenized_txt_output_tokens_3)
avg_r_coords_occupancy_adj_json_output = np.mean(occupancy_R_coords_adj_json_output_tokens_3)
avg_r_coords_occupancy_adj_txt_output = np.mean(occupancy_R_coords_adj_txt_output_tokens_3)
avg_r_coords_occupancy_ascii_txt_output = np.mean(occupancy_R_coords_ascii_txt_output_tokens_3)
avg_r_coords_occupancy_tokenized_txt_output = np.mean(occupancy_R_coords_tokenized_txt_output_tokens_3)


# # Set up complexities for table
# x_axis = [1, 2, 3,4,5,6,7,8,9,10]
# complexities = [f"Run {x_axis[i]}" for i in range(10)]

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


# # R - ALLO -  - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_allo_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_jpg_3 = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 25.0, 100.0, 16.666666666666664, 100.0, 0.0, 75.0, 25.0, 100.0, 50.0, 37.5, 0.0, 37.5, 0.0, 25.0, 100.0, 33.33333333333333, 100.0, 100.0, 37.5, 75.0, 100.0, 100.0, 100.0, 50.0, 100.0])
line_R_allo_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_ascii_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 41.66666666666667, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 93.75, 100.0, 100.0, 25.0, 100.0, 62.5, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 12.5, 100.0, 100.0, 100.0])
occupancy_R_allo_jpg_3 = np.array([0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 25.0, 16.666666666666664, 0.0, 37.5, 75.0, 75.0, 25.0, 0.0, 31.25, 62.5, 31.25, 41.66666666666667, 0.0, 0.0, 16.666666666666664, 16.666666666666664, 0.0, 31.25, 0.0, 0.0, 25.0, 68.75, 0.0, 0.0])
occupancy_R_allo_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_R_allo_adj_json_raw_score_3 = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 4.0, 4.0, 4.0, 6.0, 8.0, 4.0, 8.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 8.0, 4.0, 4.0, 4.0, 8.0, 4.0, 4.0])
line_R_allo_adj_txt_raw_score_3 = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 4.0, 4.0, 4.0, 6.0, 8.0, 4.0, 8.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 8.0, 4.0, 4.0, 4.0, 8.0, 4.0, 4.0])
line_R_allo_jpg_raw_score_3 = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 1.0, 4.0, 1.0, 6.0, 0.0, 3.0, 1.0, 4.0, 3.0, 3.0, 0.0, 3.0, 0.0, 1.0, 4.0, 2.0, 6.0, 4.0, 3.0, 3.0, 4.0, 4.0, 8.0, 2.0, 4.0])
line_R_allo_json_raw_score_3 = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 4.0, 4.0, 4.0, 6.0, 8.0, 4.0, 8.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 8.0, 4.0, 4.0, 4.0, 8.0, 4.0, 4.0])
line_R_allo_tokenized_txt_raw_score_3 = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 4.0, 4.0, 4.0, 6.0, 8.0, 4.0, 8.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0, 8.0, 4.0, 4.0, 4.0, 8.0, 4.0, 4.0])
occupancy_R_allo_adj_json_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 8.0, 8.0, 8.0, 12.0, 16.0, 8.0, 16.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 16.0, 8.0, 8.0, 8.0, 16.0, 8.0, 8.0])
occupancy_R_allo_adj_txt_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 8.0, 8.0, 8.0, 12.0, 16.0, 8.0, 16.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 16.0, 8.0, 8.0, 8.0, 16.0, 8.0, 8.0])
occupancy_R_allo_ascii_txt_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 5.0, 8.0, 8.0, 12.0, 12.0, 8.0, 8.0, 8.0, 8.0, 6.0, 15.0, 8.0, 16.0, 3.0, 8.0, 5.0, 12.0, 12.0, 8.0, 16.0, 8.0, 8.0, 1.0, 16.0, 8.0, 8.0])
occupancy_R_allo_jpg_raw_score_3 = np.array([0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 2.0, 2.0, 0.0, 3.0, 6.0, 6.0, 2.0, 0.0, 5.0, 5.0, 5.0, 5.0, 0.0, 0.0, 2.0, 2.0, 0.0, 5.0, 0.0, 0.0, 2.0, 11.0, 0.0, 0.0])
occupancy_R_allo_json_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 8.0, 8.0, 8.0, 12.0, 16.0, 8.0, 16.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 16.0, 8.0, 8.0, 8.0, 16.0, 8.0, 8.0])
occupancy_R_allo_tokenized_txt_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 8.0, 8.0, 8.0, 12.0, 16.0, 8.0, 16.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0, 16.0, 8.0, 8.0, 8.0, 16.0, 8.0, 8])

# Prompt tokens
line_R_allo_adj_json_input_tokens_3 = np.array([712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0, 719.0])
line_R_allo_adj_txt_input_tokens_3 = np.array([344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0, 351.0])
line_R_allo_jpg_input_tokens_3 = np.array([427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0])
line_R_allo_json_input_tokens_3 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0, 657.0])
line_R_allo_tokenized_txt_input_tokens_3 = np.array([315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0, 322.0])
occupancy_R_allo_adj_json_input_tokens_3 = np.array([1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1175.0, 1175.0, 1175.0, 1181.0, 1181.0, 1181.0, 1175.0, 1181.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0, 1175.0])
occupancy_R_allo_adj_txt_input_tokens_3 = np.array([456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0, 463.0])
occupancy_R_allo_ascii_txt_input_tokens_3 = np.array([192.0, 192.0, 190.0, 192.0, 192.0, 192.0, 192.0, 192.0, 192.0, 190.0, 200.0, 199.0, 200.0, 201.0, 195.0, 199.0, 202.0, 197.0, 199.0, 197.0, 199.0, 199.0, 197.0, 202.0, 200.0, 197.0, 199.0, 202.0, 197.0, 197.0])
occupancy_R_allo_jpg_input_tokens_3 = np.array([432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0])
occupancy_R_allo_json_input_tokens_3 = np.array([465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0, 472.0])
occupancy_R_allo_tokenized_txt_input_tokens_3 = np.array([744.0, 744.0, 744.0, 744.0, 743.0, 743.0, 743.0, 743.0, 743.0, 743.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750.0, 750])


# Output tokens
line_R_allo_adj_json_output_tokens_3 = np.array([1729.0, 1338.0, 1698.0, 1356.0, 2081.0, 1839.0, 1446.0, 3182.0, 2031.0, 1978.0, 1602.0, 1203.0, 1560.0, 1378.0, 1874.0, 1419.0, 1740.0, 1043.0, 1480.0, 1179.0, 1657.0, 1457.0, 1588.0, 2045.0, 1377.0, 860.0, 2082.0, 1991.0, 863.0, 2068.0])
line_R_allo_adj_txt_output_tokens_3 = np.array([2080.0, 4596.0, 2232.0, 1912.0, 3297.0, 1257.0, 2799.0, 1641.0, 2194.0, 2137.0, 2341.0, 1702.0, 2246.0, 1897.0, 2061.0, 2787.0, 2097.0, 2086.0, 1246.0, 1532.0, 2127.0, 1090.0, 1311.0, 2687.0, 2366.0, 1745.0, 1647.0, 2053.0, 1466.0, 1378.0])
line_R_allo_jpg_output_tokens_3 = np.array([14536.0, 2225.0, 1313.0, 1583.0, 565.0, 743.0, 1530.0, 7230.0, 6033.0, 1339.0, 3599.0, 1188.0, 847.0, 2171.0, 1763.0, 749.0, 1027.0, 926.0, 1303.0, 1051.0, 2058.0, 983.0, 1365.0, 796.0, 1265.0, 1221.0, 1556.0, 1530.0, 1696.0, 1095.0])
line_R_allo_json_output_tokens_3 = np.array([1366.0, 1420.0, 1475.0, 1144.0, 1807.0, 1492.0, 1762.0, 1599.0, 1682.0, 2604.0, 2304.0, 1389.0, 1278.0, 1420.0, 1181.0, 1540.0, 2641.0, 1627.0, 1220.0, 989.0, 2623.0, 1553.0, 1438.0, 1725.0, 2375.0, 774.0, 2115.0, 1589.0, 1358.0, 1219.0])
line_R_allo_tokenized_txt_output_tokens_3 = np.array([1403.0, 1250.0, 1290.0, 933.0, 2456.0, 2327.0, 1276.0, 3675.0, 2060.0, 1521.0, 1977.0, 1059.0, 1748.0, 2475.0, 1712.0, 2826.0, 1771.0, 1264.0, 2614.0, 2387.0, 1435.0, 1438.0, 3088.0, 3002.0, 2363.0, 1828.0, 2719.0, 1325.0, 2609.0, 1463.0])
occupancy_R_allo_adj_json_output_tokens_3 = np.array([4853.0, 3989.0, 3209.0, 3350.0, 7269.0, 3599.0, 5583.0, 5676.0, 3584.0, 3374.0, 1612.0, 1617.0, 1798.0, 1747.0, 2815.0, 2005.0, 2102.0, 1974.0, 2211.0, 1659.0, 2421.0, 2594.0, 1691.0, 2015.0, 1764.0, 1570.0, 1544.0, 2426.0, 1572.0, 2017.0])
occupancy_R_allo_adj_txt_output_tokens_3 = np.array([7175.0, 7839.0, 4911.0, 8476.0, 7901.0, 4069.0, 6469.0, 5701.0, 6608.0, 4476.0, 2318.0, 2593.0, 1238.0, 2050.0, 1513.0, 2221.0, 2309.0, 1948.0, 2574.0, 1787.0, 2706.0, 1993.0, 1836.0, 2270.0, 2803.0, 2235.0, 2446.0, 3383.0, 2067.0, 2019.0])
occupancy_R_allo_ascii_txt_output_tokens_3 = np.array([3455.0, 3764.0, 4552.0, 3401.0, 1849.0, 6728.0, 2600.0, 4200.0, 3523.0, 3007.0, 6622.0, 3979.0, 1978.0, 3077.0, 1853.0, 2288.0, 1510.0, 1783.0, 1507.0, 2273.0, 2159.0, 3607.0, 1578.0, 836.0, 2370.0, 1558.0, 8655.0, 2174.0, 2278.0, 3380.0])
occupancy_R_allo_jpg_output_tokens_3 = np.array([9275.0, 2057.0, 17922.0, 2315.0, 1158.0, 3392.0, 5907.0, 7009.0, 8449.0, 991.0, 979.0, 1038.0, 4430.0, 1914.0, 804.0, 2131.0, 981.0, 971.0, 1326.0, 1073.0, 4250.0, 2026.0, 992.0, 879.0, 719.0, 1273.0, 1315.0, 1172.0, 1127.0, 979.0])
occupancy_R_allo_json_output_tokens_3 = np.array([4247.0, 3624.0, 3078.0, 3722.0, 7561.0, 3847.0, 2845.0, 2169.0, 10791.0, 3687.0, 4535.0, 3577.0, 1649.0, 2354.0, 1800.0, 3900.0, 1596.0, 2570.0, 2760.0, 2165.0, 2819.0, 1313.0, 3988.0, 1711.0, 1568.0, 2606.0, 3663.0, 1696.0, 2426.0, 2094.0])
occupancy_R_allo_tokenized_txt_output_tokens_3 = np.array([2474.0, 2171.0, 1444.0, 3519.0, 3134.0, 4225.0, 3933.0, 3277.0, 3956.0, 2010.0, 1892.0, 4439.0, 2494.0, 1926.0, 2005.0, 4169.0, 4977.0, 1859.0, 4340.0, 2379.0, 2647.0, 2079.0, 2973.0, 1750.0, 3076.0, 2699.0, 2981.0, 1978.0, 3006.0, 2485])


# Final answer only output tokens
line_R_allo_jpg_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 7.0, np.nan, np.nan, 7.0, np.nan, 5.0])
line_R_allo_json_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 7.0, np.nan, np.nan, 11.0, np.nan, 7.0])
line_R_allo_adj_json_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 7.0, np.nan, np.nan, 11.0, np.nan, 7.0])
line_R_allo_adj_txt_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 7.0, np.nan, np.nan, 11.0, np.nan, 7.0])
line_R_allo_tokenized_txt_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 7.0, np.nan, np.nan, 11.0, np.nan, 7.0])
occupancy_R_allo_jpg_final_answer_3 = np.array([27.0, 17.0,  31.0, np.nan, 31.0, np.nan, np.nan, 29.0, np.nan, 25.0])
occupancy_R_allo_json_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan,  15.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_allo_adj_json_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 15.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_allo_adj_txt_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 15.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_allo_tokenized_txt_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 15.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_allo_ascii_txt_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan,  15.0, np.nan, np.nan, 23.0, np.nan, 15.0])


avg_r_allo_line_jpg_input = np.mean(line_R_allo_jpg_input_tokens_3)
avg_r_allo_line_json_input = np.mean(line_R_allo_json_input_tokens_3)
avg_r_allo_occupancy_jpg_input = np.mean(occupancy_R_allo_jpg_input_tokens_3)
avg_r_allo_occupancy_json_input = np.mean(occupancy_R_allo_json_input_tokens_3)
avg_r_allo_line_adj_json_input = np.mean(line_R_allo_adj_json_input_tokens_3)
avg_r_allo_line_adj_txt_input = np.mean(line_R_allo_adj_txt_input_tokens_3)
avg_r_allo_line_tokenized_txt_input = np.mean(line_R_allo_tokenized_txt_input_tokens_3)
avg_r_allo_occupancy_adj_json_input = np.mean(occupancy_R_allo_adj_json_input_tokens_3)
avg_r_allo_occupancy_adj_txt_input = np.mean(occupancy_R_allo_adj_txt_input_tokens_3)
avg_r_allo_occupancy_ascii_txt_input = np.mean(occupancy_R_allo_ascii_txt_input_tokens_3)
avg_r_allo_occupancy_tokenized_txt_input = np.mean(occupancy_R_allo_tokenized_txt_input_tokens_3)
avg_r_allo_line_jpg_output = np.mean(line_R_allo_jpg_output_tokens_3)
avg_r_allo_line_json_output = np.mean(line_R_allo_json_output_tokens_3)
avg_r_allo_occupancy_jpg_output = np.mean(occupancy_R_allo_jpg_output_tokens_3)
avg_r_allo_occupancy_json_output = np.mean(occupancy_R_allo_json_output_tokens_3)
avg_r_allo_line_adj_json_output = np.mean(line_R_allo_adj_json_output_tokens_3)
avg_r_allo_line_adj_txt_output = np.mean(line_R_allo_adj_txt_output_tokens_3)
avg_r_allo_line_tokenized_txt_output = np.mean(line_R_allo_tokenized_txt_output_tokens_3)
avg_r_allo_occupancy_adj_json_output = np.mean(occupancy_R_allo_adj_json_output_tokens_3)
avg_r_allo_occupancy_adj_txt_output = np.mean(occupancy_R_allo_adj_txt_output_tokens_3)
avg_r_allo_occupancy_ascii_txt_output = np.mean(occupancy_R_allo_ascii_txt_output_tokens_3)
avg_r_allo_occupancy_tokenized_txt_output = np.mean(occupancy_R_allo_tokenized_txt_output_tokens_3)


# # Set up complexities for table
# x_axis = [1, 2, 3,4,5,6,7,8,9,10]
# complexities = [f"Run {x_axis[i]}" for i in range(10)]

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 3x3, Gemini 2.5 Pro, Allocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_R_allo.png")


# # R - EGO -  - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_ego_adj_json_3 = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_adj_txt_3 = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_jpg_3 = np.array([25.0, 0.0, 50.0, 50.0, 33.33333333333333, 0.0, 0.0, 100.0, 16.666666666666664, 100.0])
line_R_ego_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_ascii_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 100.0, 100.0, 75.0])
occupancy_R_ego_jpg_3 = np.array([12.5, 0.0, 0.0, 50.0, 33.33333333333333, 0.0, 12.5, 91.66666666666666, 8.333333333333332, 37.5])
occupancy_R_ego_json_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_tokenized_txt_3 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])


# Raw Scores
line_R_ego_adj_json_raw_score_3 = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_ego_adj_txt_raw_score_3 = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_ego_jpg_raw_score_3 = np.array([1.0, 0.0, 2.0, 2.0, 2.0, 0.0, 0.0, 6.0, 1.0, 4.0])
line_R_ego_json_raw_score_3 = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_ego_tokenized_txt_raw_score_3 = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
occupancy_R_ego_adj_json_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_ego_adj_txt_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_ego_ascii_txt_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 4.0, 12.0, 12.0, 6.0])
occupancy_R_ego_jpg_raw_score_3 = np.array([1.0, 0.0, 0.0, 4.0, 4.0, 0.0, 1.0, 11.0, 1.0, 3.0])
occupancy_R_ego_json_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_ego_tokenized_txt_raw_score_3 = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8])

# Prompt tokens
line_R_ego_adj_json_input_tokens_3 = np.array([822.0, 822.0, 829.0, 829.0, 829.0, 829.0, 829.0, 829.0, 829.0, 829.0])
line_R_ego_adj_txt_input_tokens_3 = np.array([454.0, 454.0, 461.0, 461.0, 461.0, 461.0, 461.0, 461.0, 461.0, 461.0])
line_R_ego_jpg_input_tokens_3 = np.array([537.0, 537.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0])
line_R_ego_json_input_tokens_3 = np.array([760.0, 760.0, 767.0, 767.0, 767.0, 767.0, 767.0, 767.0, 767.0, 767.0])
line_R_ego_tokenized_txt_input_tokens_3 = np.array([425.0, 425.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0])
occupancy_R_ego_adj_json_input_tokens_3 = np.array([1284.0, 1284.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0])
occupancy_R_ego_adj_txt_input_tokens_3 = np.array([566.0, 566.0, 573.0, 573.0, 573.0, 573.0, 573.0, 573.0, 573.0, 573.0])
occupancy_R_ego_ascii_txt_input_tokens_3 = np.array([302.0, 302.0, 307.0, 309.0, 309.0, 309.0, 309.0, 309.0, 309.0, 307.0])
occupancy_R_ego_jpg_input_tokens_3 = np.array([542.0, 542.0, 549.0, 549.0, 549.0, 549.0, 549.0, 549.0, 549.0, 549.0])
occupancy_R_ego_json_input_tokens_3 = np.array([575.0, 575.0, 582.0, 582.0, 582.0, 582.0, 582.0, 582.0, 582.0, 582.0])
occupancy_R_ego_tokenized_txt_input_tokens_3 = np.array([854.0, 854.0, 861.0, 861.0, 860.0, 860.0, 860.0, 860.0, 860.0, 860])


# Output tokens
line_R_ego_adj_json_output_tokens_3 = np.array([3560.0, 2534.0, 2248.0, 5136.0, 2161.0, 1990.0, 2845.0, 3926.0, 3096.0, 2119.0])
line_R_ego_adj_txt_output_tokens_3 = np.array([2930.0, 3587.0, 1933.0, 2641.0, 3112.0, 4863.0, 2100.0, 3512.0, 4410.0, 4022.0])
line_R_ego_jpg_output_tokens_3 = np.array([8539.0, 4203.0, 1105.0, 6439.0, 2083.0, 1169.0, 2926.0, 6573.0, 956.0, 3620.0])
line_R_ego_json_output_tokens_3 = np.array([2401.0, 3116.0, 2388.0, 2223.0, 1786.0, 2653.0, 2229.0, 2922.0, 2328.0, 1745.0])
line_R_ego_tokenized_txt_output_tokens_3 = np.array([3418.0, 3481.0, 2694.0, 2831.0, 5562.0, 1329.0, 3137.0, 4427.0, 4192.0, 4997.0])
occupancy_R_ego_adj_json_output_tokens_3 = np.array([2912.0, 2264.0, 2449.0, 5428.0, 3254.0, 5593.0, 4609.0, 9388.0, 2930.0, 3499.0])
occupancy_R_ego_adj_txt_output_tokens_3 = np.array([5534.0, 2162.0, 5607.0, 3270.0, 3786.0, 5441.0, 6224.0, 8755.0, 7211.0, 3472.0])
occupancy_R_ego_ascii_txt_output_tokens_3 = np.array([7469.0, 3371.0, 3412.0, 9243.0, 4083.0, 2292.0, 3412.0, 8108.0, 6947.0, 3962.0])
occupancy_R_ego_jpg_output_tokens_3 = np.array([4816.0, 9362.0, 2226.0, 1635.0, 2873.0, 10455.0, 10761.0, 2276.0, 3848.0, 3554.0])
occupancy_R_ego_json_output_tokens_3 = np.array([4612.0, 5353.0, 4658.0, 4597.0, 4898.0, 3064.0, 3409.0, 4365.0, 4804.0, 4792.0])
occupancy_R_ego_tokenized_txt_output_tokens_3 = np.array([3530.0, 4654.0, 2890.0, 4121.0, 5383.0, 4001.0, 7766.0, 3142.0, 3579.0, 3581])


# Final answer only output tokens
line_R_ego_jpg_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 7.0, np.nan, np.nan, 11.0, np.nan, 9.0 ])
line_R_ego_json_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 11.0, np.nan, np.nan, 11.0, np.nan, 7.0])
line_R_ego_adj_json_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 11.0, np.nan, np.nan, 11.0, np.nan, 7.0])
line_R_ego_adj_txt_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 11.0, np.nan, np.nan, 11.0, np.nan, 7.0])
line_R_ego_tokenized_txt_final_answer_3 = np.array([7.0, 7.0, 7.0, np.nan, 11.0, np.nan, np.nan, 11.0, np.nan, 7.0])
occupancy_R_ego_jpg_final_answer_3 = np.array([15.0, 13.0, 31.0, np.nan, 15.0, np.nan, np.nan, 21.0, np.nan, 13.0])
occupancy_R_ego_json_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 23.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_ego_adj_json_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 23.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_ego_adj_txt_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 23.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_ego_tokenized_txt_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 23.0, np.nan, np.nan, 23.0, np.nan, 15.0])
occupancy_R_ego_ascii_txt_final_answer_3 = np.array([15.0, 15.0, 15.0, np.nan, 23.0, np.nan, np.nan, 23.0, np.nan, 31.0])


avg_r_ego_line_jpg_input = np.mean(line_R_ego_jpg_input_tokens_3)
avg_r_ego_line_json_input = np.mean(line_R_ego_json_input_tokens_3)
avg_r_ego_occupancy_jpg_input = np.mean(occupancy_R_ego_jpg_input_tokens_3)
avg_r_ego_occupancy_json_input = np.mean(occupancy_R_ego_json_input_tokens_3)
avg_r_ego_line_adj_json_input = np.mean(line_R_ego_adj_json_input_tokens_3)
avg_r_ego_line_adj_txt_input = np.mean(line_R_ego_adj_txt_input_tokens_3)
avg_r_ego_line_tokenized_txt_input = np.mean(line_R_ego_tokenized_txt_input_tokens_3)
avg_r_ego_occupancy_adj_json_input = np.mean(occupancy_R_ego_adj_json_input_tokens_3)
avg_r_ego_occupancy_adj_txt_input = np.mean(occupancy_R_ego_adj_txt_input_tokens_3)
avg_r_ego_occupancy_ascii_txt_input = np.mean(occupancy_R_ego_ascii_txt_input_tokens_3)
avg_r_ego_occupancy_tokenized_txt_input = np.mean(occupancy_R_ego_tokenized_txt_input_tokens_3)
avg_r_ego_line_jpg_output = np.mean(line_R_ego_jpg_output_tokens_3)
avg_r_ego_line_json_output = np.mean(line_R_ego_json_output_tokens_3)
avg_r_ego_occupancy_jpg_output = np.mean(occupancy_R_ego_jpg_output_tokens_3)
avg_r_ego_occupancy_json_output = np.mean(occupancy_R_ego_json_output_tokens_3)
avg_r_ego_line_adj_json_output = np.mean(line_R_ego_adj_json_output_tokens_3)
avg_r_ego_line_adj_txt_output = np.mean(line_R_ego_adj_txt_output_tokens_3)
avg_r_ego_line_tokenized_txt_output = np.mean(line_R_ego_tokenized_txt_output_tokens_3)
avg_r_ego_occupancy_adj_json_output = np.mean(occupancy_R_ego_adj_json_output_tokens_3)
avg_r_ego_occupancy_adj_txt_output = np.mean(occupancy_R_ego_adj_txt_output_tokens_3)
avg_r_ego_occupancy_ascii_txt_output = np.mean(occupancy_R_ego_ascii_txt_output_tokens_3)
avg_r_ego_occupancy_tokenized_txt_output = np.mean(occupancy_R_ego_tokenized_txt_output_tokens_3)


# # Set up complexities for table
# x_axis = [1, 2, 3,4,5,6,7,8,9,10]
# complexities = [f"Run {x_axis[i]}" for i in range(10)]

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




# print("average input NR line jpg 3x3:", np.mean(np.array([avg_nr_coords_line_jpg_input, avg_nr_allo_line_jpg_input, avg_nr_ego_line_jpg_input])))
# print("average input NR line json 3x3:", np.mean(np.array([avg_nr_coords_line_json_input, avg_nr_allo_line_json_input, avg_nr_ego_line_json_input])))
# print("average input NR line adj json 3x3:", np.mean(np.array([avg_nr_coords_line_adj_json_input, avg_nr_allo_line_adj_json_input, avg_nr_ego_line_adj_json_input])))
# print("average input NR line adj txt 3x3:", np.mean(np.array([avg_nr_coords_line_adj_txt_input, avg_nr_allo_line_adj_txt_input, avg_nr_ego_line_adj_txt_input])))
# print("average input NR line tokeninzed 3x3:", np.mean(np.array([avg_nr_coords_line_tokenized_txt_input, avg_nr_allo_line_tokenized_txt_input, avg_nr_ego_line_tokenized_txt_input])))
# print("average input NR occ jpg 3x3:", np.mean(np.array([avg_nr_coords_occupancy_jpg_input, avg_nr_allo_occupancy_jpg_input, avg_nr_ego_occupancy_jpg_input])))
# print("average input NR occ json 3x3:", np.mean(np.array([avg_nr_coords_occupancy_json_input, avg_nr_allo_occupancy_json_input, avg_nr_ego_occupancy_json_input])))
# print("average input NR occ adj json 3x3:", np.mean(np.array([avg_nr_coords_occupancy_adj_json_input, avg_nr_allo_occupancy_adj_json_input, avg_nr_ego_occupancy_adj_json_input])))
# print("average input NR occ adj txt 3x3:", np.mean(np.array([avg_nr_coords_occupancy_adj_txt_input, avg_nr_allo_occupancy_adj_txt_input, avg_nr_ego_occupancy_adj_txt_input])))
# print("average input NR occ ascii txt 3x3:", np.mean(np.array([avg_nr_coords_occupancy_ascii_txt_input, avg_nr_allo_occupancy_ascii_txt_input, avg_nr_ego_occupancy_ascii_txt_input])))
# print("average input NR occ tokenized txt 3x3:", np.mean(np.array([avg_nr_coords_occupancy_tokenized_txt_input, avg_nr_allo_occupancy_tokenized_txt_input, avg_nr_ego_occupancy_tokenized_txt_input])))

# print("average input R line jpg 3x3:", np.mean(np.array([avg_r_coords_line_jpg_input, avg_r_allo_line_jpg_input, avg_r_ego_line_jpg_input])))
# print("average input R line json 3x3:", np.mean(np.array([avg_r_coords_line_json_input, avg_r_allo_line_json_input, avg_r_ego_line_json_input])))
# print("average input R line adj json 3x3:", np.mean(np.array([avg_r_coords_line_adj_json_input, avg_r_allo_line_adj_json_input, avg_r_ego_line_adj_json_input])))
# print("average input R line adj txt 3x3:", np.mean(np.array([avg_r_coords_line_adj_txt_input, avg_r_allo_line_adj_txt_input, avg_r_ego_line_adj_txt_input])))
# print("average input R line tokeninzed 3x3:", np.mean(np.array([avg_r_coords_line_tokenized_txt_input, avg_r_allo_line_tokenized_txt_input, avg_r_ego_line_tokenized_txt_input])))
# print("average input R occ jpg 3x3:", np.mean(np.array([avg_r_coords_occupancy_jpg_input, avg_r_allo_occupancy_jpg_input, avg_r_ego_occupancy_jpg_input])))
# print("average input R occ json 3x3:", np.mean(np.array([avg_r_coords_occupancy_json_input, avg_r_allo_occupancy_json_input, avg_r_ego_occupancy_json_input])))
# print("average input R occ adj json 3x3:", np.mean(np.array([avg_r_coords_occupancy_adj_json_input, avg_r_allo_occupancy_adj_json_input, avg_r_ego_occupancy_adj_json_input])))
# print("average input R occ adj txt 3x3:", np.mean(np.array([avg_r_coords_occupancy_adj_txt_input, avg_r_allo_occupancy_adj_txt_input, avg_r_ego_occupancy_adj_txt_input])))
# print("average input R occ ascii txt 3x3:", np.mean(np.array([avg_r_coords_occupancy_ascii_txt_input, avg_r_allo_occupancy_ascii_txt_input, avg_r_ego_occupancy_ascii_txt_input])))
# print("average input R occ tokenized txt 3x3:", np.mean(np.array([avg_r_coords_occupancy_tokenized_txt_input, avg_r_allo_occupancy_tokenized_txt_input, avg_r_ego_occupancy_tokenized_txt_input])))


# print("average output NR line jpg 3x3:", np.mean(np.array([avg_nr_coords_line_jpg_output, avg_nr_allo_line_jpg_output, avg_nr_ego_line_jpg_output])))
# print("average output NR line json 3x3:", np.mean(np.array([avg_nr_coords_line_json_output, avg_nr_allo_line_json_output, avg_nr_ego_line_json_output])))
# print("average output NR line adj json 3x3:", np.mean(np.array([avg_nr_coords_line_adj_json_output, avg_nr_allo_line_adj_json_output, avg_nr_ego_line_adj_json_output])))
# print("average output NR line adj txt 3x3:", np.mean(np.array([avg_nr_coords_line_adj_txt_output, avg_nr_allo_line_adj_txt_output, avg_nr_ego_line_adj_txt_output])))
# print("average output NR line tokeninzed 3x3:", np.mean(np.array([avg_nr_coords_line_tokenized_txt_output, avg_nr_allo_line_tokenized_txt_output, avg_nr_ego_line_tokenized_txt_output])))
# print("average output NR occ jpg 3x3:", np.mean(np.array([avg_nr_coords_occupancy_jpg_output, avg_nr_allo_occupancy_jpg_output, avg_nr_ego_occupancy_jpg_output])))
# print("average output NR occ json 3x3:", np.mean(np.array([avg_nr_coords_occupancy_json_output, avg_nr_allo_occupancy_json_output, avg_nr_ego_occupancy_json_output])))
# print("average output NR occ adj json 3x3:", np.mean(np.array([avg_nr_coords_occupancy_adj_json_output, avg_nr_allo_occupancy_adj_json_output, avg_nr_ego_occupancy_adj_json_output])))
# print("average output NR occ adj txt 3x3:", np.mean(np.array([avg_nr_coords_occupancy_adj_txt_output, avg_nr_allo_occupancy_adj_txt_output, avg_nr_ego_occupancy_adj_txt_output])))
# print("average output NR occ ascii txt 3x3:", np.mean(np.array([avg_nr_coords_occupancy_ascii_txt_output, avg_nr_allo_occupancy_ascii_txt_output, avg_nr_ego_occupancy_ascii_txt_output])))
# print("average output NR occ tokenized txt 3x3:", np.mean(np.array([avg_nr_coords_occupancy_tokenized_txt_output, avg_nr_allo_occupancy_tokenized_txt_output, avg_nr_ego_occupancy_tokenized_txt_output])))

# print("average output R line jpg 3x3:", np.mean(np.array([avg_r_coords_line_jpg_output, avg_r_allo_line_jpg_output, avg_r_ego_line_jpg_output])))
# print("average output R line json 3x3:", np.mean(np.array([avg_r_coords_line_json_output, avg_r_allo_line_json_output, avg_r_ego_line_json_output])))
# print("average output R line adj json 3x3:", np.mean(np.array([avg_r_coords_line_adj_json_output, avg_r_allo_line_adj_json_output, avg_r_ego_line_adj_json_output])))
# print("average output R line adj txt 3x3:", np.mean(np.array([avg_r_coords_line_adj_txt_output, avg_r_allo_line_adj_txt_output, avg_r_ego_line_adj_txt_output])))
# print("average output R line tokeninzed 3x3:", np.mean(np.array([avg_r_coords_line_tokenized_txt_output, avg_r_allo_line_tokenized_txt_output, avg_r_ego_line_tokenized_txt_output])))
# print("average output R occ jpg 3x3:", np.mean(np.array([avg_r_coords_occupancy_jpg_output, avg_r_allo_occupancy_jpg_output, avg_r_ego_occupancy_jpg_output])))
# print("average output R occ json 3x3:", np.mean(np.array([avg_r_coords_occupancy_json_output, avg_r_allo_occupancy_json_output, avg_r_ego_occupancy_json_output])))
# print("average output R occ adj json 3x3:", np.mean(np.array([avg_r_coords_occupancy_adj_json_output, avg_r_allo_occupancy_adj_json_output, avg_r_ego_occupancy_adj_json_output])))
# print("average output R occ adj txt 3x3:", np.mean(np.array([avg_r_coords_occupancy_adj_txt_output, avg_r_allo_occupancy_adj_txt_output, avg_r_ego_occupancy_adj_txt_output])))
# print("average output R occ ascii txt 3x3:", np.mean(np.array([avg_r_coords_occupancy_ascii_txt_output, avg_r_allo_occupancy_ascii_txt_output, avg_r_ego_occupancy_ascii_txt_output])))
# print("average output R occ tokenized txt 3x3:", np.mean(np.array([avg_r_coords_occupancy_tokenized_txt_output, avg_r_allo_occupancy_tokenized_txt_output, avg_r_ego_occupancy_tokenized_txt_output])))


