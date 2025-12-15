import numpy as np
import pandas as pd
import dataframe_image as dfi
representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']


# NR - COORDS - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_NR_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 42.857142857142854, 100.0, 100.0])
line_NR_coords_jpg = np.array([40.0, 20.0, 40.0, 60.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_json = np.array([100.0, 20.0, 60.0, 20.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_NR_coords_tokenized_txt = np.array([20.0, 0.0, 0.0, 60.0, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 20.0])
occupancy_NR_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_NR_coords_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 110.00000000000001])
occupancy_NR_coords_jpg = np.array([0.0, 0.0, 55.55555555555556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json = np.array([100.0, 110.00000000000001, 100.0, 110.00000000000001, 7.6923076923076925, 100.0, 110.00000000000001, 100.0, 100.0, 110.00000000000001])
occupancy_NR_coords_tokenized_txt = np.array([11.11111111111111, 110.00000000000001, 100.0, 100.0, 7.6923076923076925, 11.11111111111111, 100.0, 100.0, 7.6923076923076925, 110.00000000000001])

# Raw scores
line_NR_coords_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_NR_coords_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 3.0, 7.0, 5.0])
line_NR_coords_jpg_raw_score = np.array([2.0, 1.0, 2.0, 3.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_NR_coords_json_raw_score = np.array([5.0, 1.0, 3.0, 1.0, 3.0, 5.0, 1.0, 1.0, 3.0, 1.0])
line_NR_coords_tokenized_txt_raw_score = np.array([1.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0])
occupancy_NR_coords_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_NR_coords_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_NR_coords_ascii_txt_raw_score = np.array([0.0, 9.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.0])  
occupancy_NR_coords_jpg_raw_score = np.array([0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 1.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_NR_coords_tokenized_txt_raw_score = np.array([1.0, 9.0, 9.0, 9.0, 1.0, 1.0, 9.0, 13.0, 1.0, 9])

# Prompt tokens
line_NR_coords_adj_json_input_tokens = np.array([714, 714, 714, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0])
line_NR_coords_adj_txt_input_tokens = np.array([346, 346, 346, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0])
line_NR_coords_jpg_input_tokens = np.array([429, 429, 429, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0])
line_NR_coords_json_input_tokens = np.array([652, 652, 652, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0])
line_NR_coords_tokenized_txt_input_tokens = np.array([317, 317, 317, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0])
occupancy_NR_coords_adj_json_input_tokens = np.array([1176, 1176, 1176, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0])
occupancy_NR_coords_adj_txt_input_tokens = np.array([458, 458, 458, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0])
occupancy_NR_coords_ascii_txt_input_tokens = np.array([195, 195, 193, 201.0, 201.0, 201.0, 201.0, 201.0, 201.0, 199.0])
occupancy_NR_coords_jpg_input_tokens = np.array([424, 424, 424, 430.0, 430.0, 430.0, 430.0, 430.0, 430.0, 430.0])
occupancy_NR_coords_json_input_tokens = np.array([467, 467, 467, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0])
occupancy_NR_coords_tokenized_txt_input_tokens = np.array([746, 746, 746, 752, 752.0, 752.0, 752.0, 752.0, 752.0, 752])


# Output tokens
line_NR_coords_adj_json_output_tokens = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 29.0, 29.0, 21.0])
line_NR_coords_adj_txt_output_tokens = np.array([21, 21, 21, 21.0, 29.0, 21.0, 21.0, 21.0, 29.0, 21.0])
line_NR_coords_jpg_output_tokens = np.array([21, 21, 33, 21.0, 21.0, 21.0, 29.0, 21.0, 21.0, 21.0])
line_NR_coords_json_output_tokens = np.array([21, 21, 21, 17.0, 21.0, 21.0, 17.0, 29.0, 21.0, 21.0])
line_NR_coords_tokenized_txt_output_tokens = np.array([21, 25, 13, 29.0, 17.0, 17.0, 25.0, 21.0, 17.0, 29.0])
occupancy_NR_coords_adj_json_output_tokens = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_NR_coords_adj_txt_output_tokens = np.array([37, 37, 37, 37.0, 53.0, 37.0, 37.0, 53.0, 53.0, 37.0])
occupancy_NR_coords_ascii_txt_output_tokens = np.array([57, 57, 125, 53.0, 41.0, 45.0, 57.0, 41.0, 57.0, 53.0])
occupancy_NR_coords_jpg_output_tokens = np.array([45, 49, 41, 49.0, 73.0, 45.0, 65.0, 41.0, 53.0, 57.0])
occupancy_NR_coords_json_output_tokens = np.array([37, 53, 37, 53.0, 69.0, 37.0, 53.0, 53.0, 53.0, 101.0])
occupancy_NR_coords_tokenized_txt_output_tokens = np.array([41, 53, 37, 37, 49.0, 65.0, 37.0, 53.0, 53.0, 53])

avg_nr_coords_line_jpg_input = np.mean(line_NR_coords_jpg_input_tokens)
avg_nr_coords_line_json_input = np.mean(line_NR_coords_json_input_tokens)
avg_nr_coords_occupancy_jpg_input = np.mean(occupancy_NR_coords_jpg_input_tokens)
avg_nr_coords_occupancy_json_input = np.mean(occupancy_NR_coords_json_input_tokens)
avg_nr_coords_line_adj_json_input = np.mean(line_NR_coords_adj_json_input_tokens)
avg_nr_coords_line_adj_txt_input = np.mean(line_NR_coords_adj_txt_input_tokens)
avg_nr_coords_line_tokenized_txt_input = np.mean(line_NR_coords_tokenized_txt_input_tokens)
avg_nr_coords_occupancy_adj_json_input = np.mean(occupancy_NR_coords_adj_json_input_tokens)
avg_nr_coords_occupancy_adj_txt_input = np.mean(occupancy_NR_coords_adj_txt_input_tokens)
avg_nr_coords_occupancy_ascii_txt_input = np.mean(occupancy_NR_coords_ascii_txt_input_tokens)
avg_nr_coords_occupancy_tokenized_txt_input = np.mean(occupancy_NR_coords_tokenized_txt_input_tokens)
avg_nr_coords_line_jpg_output = np.mean(line_NR_coords_jpg_output_tokens)
avg_nr_coords_line_json_output = np.mean(line_NR_coords_json_output_tokens)
avg_nr_coords_occupancy_jpg_output = np.mean(occupancy_NR_coords_jpg_output_tokens)
avg_nr_coords_occupancy_json_output = np.mean(occupancy_NR_coords_json_output_tokens)
avg_nr_coords_line_adj_json_output = np.mean(line_NR_coords_adj_json_output_tokens)
avg_nr_coords_line_adj_txt_output = np.mean(line_NR_coords_adj_txt_output_tokens)
avg_nr_coords_line_tokenized_txt_output = np.mean(line_NR_coords_tokenized_txt_output_tokens)
avg_nr_coords_occupancy_adj_json_output = np.mean(occupancy_NR_coords_adj_json_output_tokens)
avg_nr_coords_occupancy_adj_txt_output = np.mean(occupancy_NR_coords_adj_txt_output_tokens)
avg_nr_coords_occupancy_ascii_txt_output = np.mean(occupancy_NR_coords_ascii_txt_output_tokens)
avg_nr_coords_occupancy_tokenized_txt_output = np.mean(occupancy_NR_coords_tokenized_txt_output_tokens)


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
line_NR_allo_adj_json = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 100.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_adj_txt = np.array([0.0, 100.0, 0.0, 100.0, 0.0, 0.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_NR_allo_jpg = np.array([50.0, 0.0, 50.0, 100.0, 33.33333333333333, 50.0, 100.0, 0.0, 0.0, 0.0])
line_NR_allo_json = np.array([100.0, 0.0, 100.0, 0.0, 33.33333333333333, 100.0, 0.0, 0.0, 33.33333333333333, 0.0])
line_NR_allo_tokenized_txt = np.array([0.0, 100.0, 0.0, 25.0, 0.0, 0.0, 25.0, 33.33333333333333, 0.0, 25.0])
occupancy_NR_allo_adj_json = np.array([50.0, 25.0, 75.0, 110.00000000000001, 0.0, 50.0, 110.00000000000001, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_NR_allo_adj_txt = np.array([62.5, 25.0, 0.0, 37.5, 33.33333333333333, 25.0, 37.5, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_NR_allo_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 62.5, 33.33333333333333, 33.33333333333333, 0.0])
occupancy_NR_allo_jpg = np.array([12.5, 0.0, 12.5, 0.0, 8.333333333333332, 12.5, 12.5, 8.333333333333332, 8.333333333333332, 0.0])
occupancy_NR_allo_json = np.array([62.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 33.33333333333333, 0.0, 87.5])
occupancy_NR_allo_tokenized_txt = np.array([0.0, 0.0, 0.0, 50.0, 8.333333333333332, 12.5, 0.0, 8.333333333333332, 0.0, 110.00000000000001])


# Raw Scores
line_NR_allo_adj_json_raw_score = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 4.0, 4.0, 2.0, 2.0, 4.0])
line_NR_allo_adj_txt_raw_score = np.array([0.0, 4.0, 0.0, 4.0, 0.0, 0.0, 4.0, 2.0, 2.0, 4.0])
line_NR_allo_jpg_raw_score = np.array([2.0, 0.0, 2.0, 4.0, 2.0, 2.0, 4.0, 0.0, 0.0, 0.0])
line_NR_allo_json_raw_score = np.array([4.0, 0.0, 4.0, 0.0, 2.0, 4.0, 0.0, 0.0, 2.0, 0.0])
line_NR_allo_tokenized_txt_raw_score = np.array([0.0, 4.0, 0.0, 1.0, 0.0, 0.0, 1.0, 2.0, 0.0, 1.0])
occupancy_NR_allo_adj_json_raw_score = np.array([4.0, 2.0, 6.0, 8.0, 0.0, 4.0, 8.0, 4.0, 0.0, 8.0])
occupancy_NR_allo_adj_txt_raw_score = np.array([5.0, 2.0, 0.0, 3.0, 4.0, 2.0, 3.0, 4.0, 0.0, 8.0])
occupancy_NR_allo_ascii_txt_raw_score = np.array([0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 5.0, 4.0, 4.0, 0.0])
occupancy_NR_allo_jpg_raw_score = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
occupancy_NR_allo_json_raw_score = np.array([5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 7.0])
occupancy_NR_allo_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 4.0, 1.0, 1.0, 0.0, 1.0, 0.0, 8])

# Prompt tokens
line_NR_allo_adj_json_input_tokens = np.array([706.0, 706.0, 706.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0])
line_NR_allo_adj_txt_input_tokens = np.array([338.0, 338.0, 338.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0])
line_NR_allo_jpg_input_tokens = np.array([421.0, 421.0, 421.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0])
line_NR_allo_json_input_tokens = np.array([644.0, 644.0, 644.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_allo_tokenized_txt_input_tokens = np.array([309.0, 309.0, 309.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0])
occupancy_NR_allo_adj_json_input_tokens = np.array([1168.0, 1168.0, 1168.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0])
occupancy_NR_allo_adj_txt_input_tokens = np.array([450.0, 450.0, 450.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0])
occupancy_NR_allo_ascii_txt_input_tokens = np.array([187.0, 187.0, 185.0, 193.0, 193.0, 193.0, 193.0, 193.0, 193.0, 191.0])
occupancy_NR_allo_jpg_input_tokens = np.array([416.0, 416.0, 416.0, 422.0, 422.0, 422.0, 422.0, 422.0, 422.0, 422.0])
occupancy_NR_allo_json_input_tokens = np.array([459.0, 459.0, 459.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0])
occupancy_NR_allo_tokenized_txt_input_tokens = np.array([738.0, 738.0, 738.0, 744.0, 744.0, 744.0, 744.0, 744.0, 743.0, 743])


# Output tokens
line_NR_allo_adj_json_output_tokens = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 5.0, 7.0])
line_NR_allo_adj_txt_output_tokens = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_jpg_output_tokens = np.array([7.0, 218.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_json_output_tokens = np.array([7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0])
line_NR_allo_tokenized_txt_output_tokens = np.array([5.0, 7.0, 5.0, 7.0, 7.0, 7.0, 7.0, 7.0, 5.0, 7.0])
occupancy_NR_allo_adj_json_output_tokens = np.array([17.0, 15.0, 21.0, 19.0, 21.0, 17.0, 19.0, 19.0, 650.0, 19.0])
occupancy_NR_allo_adj_txt_output_tokens = np.array([21.0, 17.0, 1734.0, 15.0, 13.0, 17.0, 15.0, 15.0, 650.0, 19.0])
occupancy_NR_allo_ascii_txt_output_tokens = np.array([43.0, 29.0, 43.0, 23.0, 39.0, 31.0, 25.0, 31.0, 21.0, 29.0])
occupancy_NR_allo_jpg_output_tokens = np.array([21.0, 15.0, 15.0, 49.0, 21.0, 43.0, 19.0, 17.0, 21.0, 198.0])
occupancy_NR_allo_json_output_tokens = np.array([17.0, 21.0, 45.0, 21.0, 29.0, 31.0, 21.0, 21.0, 650.0, 35.0])
occupancy_NR_allo_tokenized_txt_output_tokens = np.array([33.0, 59.0, 4000.0, 650.0, 31.0, 650.0, 31.0, 25.0, 650.0, 650])

avg_nr_allo_line_jpg_input = np.mean(line_NR_allo_jpg_input_tokens)
avg_nr_allo_line_json_input = np.mean(line_NR_allo_json_input_tokens)
avg_nr_allo_occupancy_jpg_input = np.mean(occupancy_NR_allo_jpg_input_tokens)
avg_nr_allo_occupancy_json_input = np.mean(occupancy_NR_allo_json_input_tokens)
avg_nr_allo_line_adj_json_input = np.mean(line_NR_allo_adj_json_input_tokens)
avg_nr_allo_line_adj_txt_input = np.mean(line_NR_allo_adj_txt_input_tokens)
avg_nr_allo_line_tokenized_txt_input = np.mean(line_NR_allo_tokenized_txt_input_tokens)
avg_nr_allo_occupancy_adj_json_input = np.mean(occupancy_NR_allo_adj_json_input_tokens)
avg_nr_allo_occupancy_adj_txt_input = np.mean(occupancy_NR_allo_adj_txt_input_tokens)
avg_nr_allo_occupancy_ascii_txt_input = np.mean(occupancy_NR_allo_ascii_txt_input_tokens)
avg_nr_allo_occupancy_tokenized_txt_input = np.mean(occupancy_NR_allo_tokenized_txt_input_tokens)
avg_nr_allo_line_jpg_output = np.mean(line_NR_allo_jpg_output_tokens)
avg_nr_allo_line_json_output = np.mean(line_NR_allo_json_output_tokens)
avg_nr_allo_occupancy_jpg_output = np.mean(occupancy_NR_allo_jpg_output_tokens)
avg_nr_allo_occupancy_json_output = np.mean(occupancy_NR_allo_json_output_tokens)
avg_nr_allo_line_adj_json_output = np.mean(line_NR_allo_adj_json_output_tokens)
avg_nr_allo_line_adj_txt_output = np.mean(line_NR_allo_adj_txt_output_tokens)
avg_nr_allo_line_tokenized_txt_output = np.mean(line_NR_allo_tokenized_txt_output_tokens)
avg_nr_allo_occupancy_adj_json_output = np.mean(occupancy_NR_allo_adj_json_output_tokens)
avg_nr_allo_occupancy_adj_txt_output = np.mean(occupancy_NR_allo_adj_txt_output_tokens)
avg_nr_allo_occupancy_ascii_txt_output = np.mean(occupancy_NR_allo_ascii_txt_output_tokens)
avg_nr_allo_occupancy_tokenized_txt_output = np.mean(occupancy_NR_allo_tokenized_txt_output_tokens)


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
line_NR_ego_adj_json = np.array([25.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json = np.array([25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json = np.array([0.0, 0.0, 12.5, 0.0, 8.333333333333332, 0.0, 0.0, 0.0, 8.333333333333332, 0.0])
occupancy_NR_ego_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg = np.array([0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_json = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])


# Raw Scores
line_NR_ego_adj_json_raw_score = np.array([1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json_raw_score = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json_raw_score = np.array([0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0])
occupancy_NR_ego_adj_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_raw_score = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_json_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt_raw_score = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0])

# Prompt tokens
line_NR_ego_adj_json_input_tokens = np.array([816.0, 816.0, 816.0, 836.0, 836.0, 836.0, 836.0, 836.0, 836.0, 836.0])
line_NR_ego_adj_txt_input_tokens = np.array([448.0, 448.0, 448.0, 468.0, 468.0, 468.0, 468.0, 468.0, 468.0, 468.0])
line_NR_ego_jpg_input_tokens = np.array([531.0, 531.0, 531.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0])
line_NR_ego_json_input_tokens = np.array([754.0, 754.0, 754.0, 774.0, 774.0, 774.0, 774.0, 774.0, 774.0, 774.0])
line_NR_ego_tokenized_txt_input_tokens = np.array([419.0, 419.0, 419.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0])
occupancy_NR_ego_adj_json_input_tokens = np.array([1278.0, 1278.0, 1278.0, 1298.0, 1298.0, 1298.0, 1298.0, 1298.0, 1298.0, 1298.0])
occupancy_NR_ego_adj_txt_input_tokens = np.array([560.0, 560.0, 560.0, 580.0, 580.0, 580.0, 580.0, 580.0, 580.0, 580.0])
occupancy_NR_ego_ascii_txt_input_tokens = np.array([297.0, 297.0, 295.0, 317.0, 317.0, 317.0, 317.0, 317.0, 317.0, 315.0])
occupancy_NR_ego_jpg_input_tokens = np.array([526.0, 526.0, 526.0, 546.0, 546.0, 546.0, 546.0, 546.0, 546.0, 546.0])
occupancy_NR_ego_json_input_tokens = np.array([569.0, 569.0, 569.0, 589.0, 589.0, 589.0, 589.0, 589.0, 589.0, 589.0])
occupancy_NR_ego_tokenized_txt_input_tokens = np.array([848.0, 848.0, 848.0, 868.0, 867.0, 867.0, 867.0, 867.0, 867.0, 867])


# Output tokens
line_NR_ego_adj_json_output_tokens = np.array([13.0, 4000.0, 11.0, 15.0, 15.0, 13.0, 15.0, 13.0, 15.0, 15.0])
line_NR_ego_adj_txt_output_tokens = np.array([15.0, 17.0, 13.0, 11.0, 13.0, 13.0, 15.0, 13.0, 13.0, 13.0])
line_NR_ego_jpg_output_tokens = np.array([23.0, 17.0, 15.0, 15.0, 261.0, 15.0, 15.0, 650.0, 19.0, 19.0])
line_NR_ego_json_output_tokens = np.array([11.0, 11.0, 13.0, 19.0, 13.0, 21.0, 17.0, 11.0, 11.0, 11.0])
line_NR_ego_tokenized_txt_output_tokens = np.array([17.0, 4000.0, 17.0, 649.0, 650.0, 517.0, 650.0, 47.0, 650.0, 650.0])
occupancy_NR_ego_adj_json_output_tokens = np.array([33.0, 4000.0, 31.0, 99.0, 49.0, 35.0, 41.0, 39.0, 47.0, 29.0])
occupancy_NR_ego_adj_txt_output_tokens = np.array([4000.0, 49.0, 4000.0, 49.0, 650.0, 436.0, 49.0, 45.0, 650.0, 49.0])
occupancy_NR_ego_ascii_txt_output_tokens = np.array([133.0, 4000.0, 4000.0, 35.0, 650.0, 51.0, 650.0, 51.0, 650.0, 47.0])
occupancy_NR_ego_jpg_output_tokens = np.array([25.0, 27.0, 33.0, 23.0, 27.0, 650.0, 35.0, 27.0, 35.0, 43.0])
occupancy_NR_ego_json_output_tokens = np.array([4000.0, 4000.0, 79.0, 55.0, 650.0, 650.0, 650.0, 650.0, 41.0, 650.0])
occupancy_NR_ego_tokenized_txt_output_tokens = np.array([4000.0, 1561.0, 1029.0, 49.0, 650.0, 650.0, 650.0, 650.0, 45.0, 650])

avg_nr_ego_line_jpg_input = np.mean(line_NR_ego_jpg_input_tokens)
avg_nr_ego_line_json_input = np.mean(line_NR_ego_json_input_tokens)
avg_nr_ego_occupancy_jpg_input = np.mean(occupancy_NR_ego_jpg_input_tokens)
avg_nr_ego_occupancy_json_input = np.mean(occupancy_NR_ego_json_input_tokens)
avg_nr_ego_line_adj_json_input = np.mean(line_NR_ego_adj_json_input_tokens)
avg_nr_ego_line_adj_txt_input = np.mean(line_NR_ego_adj_txt_input_tokens)
avg_nr_ego_line_tokenized_txt_input = np.mean(line_NR_ego_tokenized_txt_input_tokens)
avg_nr_ego_occupancy_adj_json_input = np.mean(occupancy_NR_ego_adj_json_input_tokens)
avg_nr_ego_occupancy_adj_txt_input = np.mean(occupancy_NR_ego_adj_txt_input_tokens)
avg_nr_ego_occupancy_ascii_txt_input = np.mean(occupancy_NR_ego_ascii_txt_input_tokens)
avg_nr_ego_occupancy_tokenized_txt_input = np.mean(occupancy_NR_ego_tokenized_txt_input_tokens)
avg_nr_ego_line_jpg_output = np.mean(line_NR_ego_jpg_output_tokens)
avg_nr_ego_line_json_output = np.mean(line_NR_ego_json_output_tokens)
avg_nr_ego_occupancy_jpg_output = np.mean(occupancy_NR_ego_jpg_output_tokens)
avg_nr_ego_occupancy_json_output = np.mean(occupancy_NR_ego_json_output_tokens)
avg_nr_ego_line_adj_json_output = np.mean(line_NR_ego_adj_json_output_tokens)
avg_nr_ego_line_adj_txt_output = np.mean(line_NR_ego_adj_txt_output_tokens)
avg_nr_ego_line_tokenized_txt_output = np.mean(line_NR_ego_tokenized_txt_output_tokens)
avg_nr_ego_occupancy_adj_json_output = np.mean(occupancy_NR_ego_adj_json_output_tokens)
avg_nr_ego_occupancy_adj_txt_output = np.mean(occupancy_NR_ego_adj_txt_output_tokens)
avg_nr_ego_occupancy_ascii_txt_output = np.mean(occupancy_NR_ego_ascii_txt_output_tokens)
avg_nr_ego_occupancy_tokenized_txt_output = np.mean(occupancy_NR_ego_tokenized_txt_output_tokens)

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
line_R_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_jpg = np.array([40.0, 100.0, 100.0, 100.0, 28.57142857142857, 40.0, 40.0, 100.0, 100.0, 100.0])
line_R_coords_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_ascii_txt = np.array([22.22222222222222, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 46.15384615384615, 77.77777777777779])
occupancy_R_coords_jpg = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556, 0.0, 7.6923076923076925, 11.11111111111111, 33.33333333333333, 0.0, 7.6923076923076925, 100.0])
occupancy_R_coords_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_R_coords_adj_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_R_coords_adj_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_R_coords_jpg_raw_score = np.array([2.0, 5.0, 5.0, 5.0, 2.0, 2.0, 2.0, 7.0, 7.0, 5.0])
line_R_coords_json_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
line_R_coords_tokenized_txt_raw_score = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
occupancy_R_coords_adj_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_R_coords_adj_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_R_coords_ascii_txt_raw_score = np.array([2.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 6.0, 7.0])
occupancy_R_coords_jpg_raw_score = np.array([1.0, 2.0, 5.0, 0.0, 1.0, 1.0, 3.0, 0.0, 1.0, 9.0])
occupancy_R_coords_json_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
occupancy_R_coords_tokenized_txt_raw_score = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9])


# Prompt tokens
line_R_coords_adj_json_input_tokens = np.array([714.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0, 720.0])
line_R_coords_adj_txt_input_tokens = np.array([346.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0, 352.0])
line_R_coords_jpg_input_tokens = np.array([429.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0])
line_R_coords_json_input_tokens = np.array([652.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0, 658.0])
line_R_coords_tokenized_txt_input_tokens = np.array([317.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0, 323.0])
occupancy_R_coords_adj_json_input_tokens = np.array([1176.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0, 1182.0])
occupancy_R_coords_adj_txt_input_tokens = np.array([458.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0, 464.0])
occupancy_R_coords_ascii_txt_input_tokens = np.array([194.0, 200.0, 198.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 198.0])
occupancy_R_coords_jpg_input_tokens = np.array([434.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0])
occupancy_R_coords_json_input_tokens = np.array([467.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0, 473.0])
occupancy_R_coords_tokenized_txt_input_tokens = np.array([746.0, 752.0, 752.0, 752.0, 751.0, 751.0, 751.0, 751.0, 751.0, 751])


# Output tokens
line_R_coords_adj_json_output_tokens = np.array([1625.0, 1289.0, 898.0, 1267.0, 1428.0, 1180.0, 890.0, 1952.0, 4861.0, 1630.0])
line_R_coords_adj_txt_output_tokens = np.array([2264.0, 2798.0, 2034.0, 1651.0, 2376.0, 2688.0, 1336.0, 2837.0, 3894.0, 2971.0])
line_R_coords_jpg_output_tokens = np.array([16131.0, 5588.0, 3890.0, 10788.0, 4661.0, 11346.0, 3181.0, 1811.0, 1099.0, 4869.0])
line_R_coords_json_output_tokens = np.array([1475.0, 1115.0, 1274.0, 1052.0, 2496.0, 1404.0, 1518.0, 1683.0, 1329.0, 2682.0])
line_R_coords_tokenized_txt_output_tokens = np.array([1408.0, 1207.0, 1637.0, 1361.0, 2974.0, 1260.0, 1333.0, 1614.0, 1760.0, 1755.0])
occupancy_R_coords_adj_json_output_tokens = np.array([2077.0, 2469.0, 3461.0, 3086.0, 3367.0, 1825.0, 4614.0, 3247.0, 5275.0, 2957.0])
occupancy_R_coords_adj_txt_output_tokens = np.array([3621.0, 4114.0, 3696.0, 3970.0, 6715.0, 3728.0, 3978.0, 2455.0, 6534.0, 1944.0])
occupancy_R_coords_ascii_txt_output_tokens = np.array([9407.0, 8884.0, 1926.0, 6484.0, 2357.0, 3312.0, 2518.0, 2395.0, 2447.0, 2544.0])
occupancy_R_coords_jpg_output_tokens = np.array([1713.0, 1428.0, 7030.0, 3242.0, 1008.0, 1835.0, 832.0, 2965.0, 1402.0, 3035.0])
occupancy_R_coords_json_output_tokens = np.array([3193.0, 2760.0, 4692.0, 5823.0, 2167.0, 3396.0, 4635.0, 2380.0, 4836.0, 3947.0])
occupancy_R_coords_tokenized_txt_output_tokens = np.array([4248.0, 2453.0, 2759.0, 3372.0, 5675.0, 4171.0, 2481.0, 4070.0, 1732.0, 5926])

avg_r_coords_line_jpg_input = np.mean(line_R_coords_jpg_input_tokens)
avg_r_coords_line_json_input = np.mean(line_R_coords_json_input_tokens)
avg_r_coords_occupancy_jpg_input = np.mean(occupancy_R_coords_jpg_input_tokens)
avg_r_coords_occupancy_json_input = np.mean(occupancy_R_coords_json_input_tokens)
avg_r_coords_line_adj_json_input = np.mean(line_R_coords_adj_json_input_tokens)
avg_r_coords_line_adj_txt_input = np.mean(line_R_coords_adj_txt_input_tokens)
avg_r_coords_line_tokenized_txt_input = np.mean(line_R_coords_tokenized_txt_input_tokens)
avg_r_coords_occupancy_adj_json_input = np.mean(occupancy_R_coords_adj_json_input_tokens)
avg_r_coords_occupancy_adj_txt_input = np.mean(occupancy_R_coords_adj_txt_input_tokens)
avg_r_coords_occupancy_ascii_txt_input = np.mean(occupancy_R_coords_ascii_txt_input_tokens)
avg_r_coords_occupancy_tokenized_txt_input = np.mean(occupancy_R_coords_tokenized_txt_input_tokens)
avg_r_coords_line_jpg_output = np.mean(line_R_coords_jpg_output_tokens)
avg_r_coords_line_json_output = np.mean(line_R_coords_json_output_tokens)
avg_r_coords_occupancy_jpg_output = np.mean(occupancy_R_coords_jpg_output_tokens)
avg_r_coords_occupancy_json_output = np.mean(occupancy_R_coords_json_output_tokens)
avg_r_coords_line_adj_json_output = np.mean(line_R_coords_adj_json_output_tokens)
avg_r_coords_line_adj_txt_output = np.mean(line_R_coords_adj_txt_output_tokens)
avg_r_coords_line_tokenized_txt_output = np.mean(line_R_coords_tokenized_txt_output_tokens)
avg_r_coords_occupancy_adj_json_output = np.mean(occupancy_R_coords_adj_json_output_tokens)
avg_r_coords_occupancy_adj_txt_output = np.mean(occupancy_R_coords_adj_txt_output_tokens)
avg_r_coords_occupancy_ascii_txt_output = np.mean(occupancy_R_coords_ascii_txt_output_tokens)
avg_r_coords_occupancy_tokenized_txt_output = np.mean(occupancy_R_coords_tokenized_txt_output_tokens)


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
line_R_allo_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_jpg = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 25.0, 100.0, 16.666666666666664, 100.0, 0.0])
line_R_allo_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 41.66666666666667, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_jpg = np.array([0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 25.0, 16.666666666666664, 0.0, 37.5])
occupancy_R_allo_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_R_allo_adj_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_allo_adj_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_allo_jpg_raw_score = np.array([0.0, 0.0, 4.0, 4.0, 2.0, 1.0, 4.0, 1.0, 6.0, 0.0])
line_R_allo_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_allo_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
occupancy_R_allo_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_allo_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_allo_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 5.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_allo_jpg_raw_score = np.array([0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 2.0, 2.0, 0.0, 3.0])
occupancy_R_allo_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_allo_tokenized_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8])


# Prompt tokens
line_R_allo_adj_json_input_tokens = np.array([712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0, 712.0])
line_R_allo_adj_txt_input_tokens = np.array([344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0, 344.0])
line_R_allo_jpg_input_tokens = np.array([427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0])
line_R_allo_json_input_tokens = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_R_allo_tokenized_txt_input_tokens = np.array([315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0, 315.0])
occupancy_R_allo_adj_json_input_tokens = np.array([1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0, 1174.0])
occupancy_R_allo_adj_txt_input_tokens = np.array([456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0, 456.0])
occupancy_R_allo_ascii_txt_input_tokens = np.array([192.0, 192.0, 190.0, 192.0, 192.0, 192.0, 192.0, 192.0, 192.0, 190.0])
occupancy_R_allo_jpg_input_tokens = np.array([432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0])
occupancy_R_allo_json_input_tokens = np.array([465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0, 465.0])
occupancy_R_allo_tokenized_txt_input_tokens = np.array([744.0, 744.0, 744.0, 744.0, 743.0, 743.0, 743.0, 743.0, 743.0, 743])


# Output tokens
line_R_allo_adj_json_output_tokens = np.array([1729.0, 1338.0, 1698.0, 1356.0, 2081.0, 1839.0, 1446.0, 3182.0, 2031.0, 1978.0])
line_R_allo_adj_txt_output_tokens = np.array([2080.0, 4596.0, 2232.0, 1912.0, 3297.0, 1257.0, 2799.0, 1641.0, 2194.0, 2137.0])
line_R_allo_jpg_output_tokens = np.array([14536.0, 2225.0, 1313.0, 1583.0, 565.0, 743.0, 1530.0, 7230.0, 6033.0, 1339.0])
line_R_allo_json_output_tokens = np.array([1366.0, 1420.0, 1475.0, 1144.0, 1807.0, 1492.0, 1762.0, 1599.0, 1682.0, 2604.0])
line_R_allo_tokenized_txt_output_tokens = np.array([1403.0, 1250.0, 1290.0, 933.0, 2456.0, 2327.0, 1276.0, 3675.0, 2060.0, 1521.0])
occupancy_R_allo_adj_json_output_tokens = np.array([4853.0, 3989.0, 3209.0, 3350.0, 7269.0, 3599.0, 5583.0, 5676.0, 3584.0, 3374.0])
occupancy_R_allo_adj_txt_output_tokens = np.array([7175.0, 7839.0, 4911.0, 8476.0, 7901.0, 4069.0, 6469.0, 5701.0, 6608.0, 4476.0])
occupancy_R_allo_ascii_txt_output_tokens = np.array([3455.0, 3764.0, 4552.0, 3401.0, 1849.0, 6728.0, 2600.0, 4200.0, 3523.0, 3007.0])
occupancy_R_allo_jpg_output_tokens = np.array([9275.0, 2057.0, 17922.0, 2315.0, 1158.0, 3392.0, 5907.0, 7009.0, 8449.0, 991.0])
occupancy_R_allo_json_output_tokens = np.array([4247.0, 3624.0, 3078.0, 3722.0, 7561.0, 3847.0, 2845.0, 2169.0, 10791.0, 3687.0])
occupancy_R_allo_tokenized_txt_output_tokens = np.array([2474.0, 2171.0, 1444.0, 3519.0, 3134.0, 4225.0, 3933.0, 3277.0, 3956.0, 2010])

avg_r_allo_line_jpg_input = np.mean(line_R_allo_jpg_input_tokens)
avg_r_allo_line_json_input = np.mean(line_R_allo_json_input_tokens)
avg_r_allo_occupancy_jpg_input = np.mean(occupancy_R_allo_jpg_input_tokens)
avg_r_allo_occupancy_json_input = np.mean(occupancy_R_allo_json_input_tokens)
avg_r_allo_line_adj_json_input = np.mean(line_R_allo_adj_json_input_tokens)
avg_r_allo_line_adj_txt_input = np.mean(line_R_allo_adj_txt_input_tokens)
avg_r_allo_line_tokenized_txt_input = np.mean(line_R_allo_tokenized_txt_input_tokens)
avg_r_allo_occupancy_adj_json_input = np.mean(occupancy_R_allo_adj_json_input_tokens)
avg_r_allo_occupancy_adj_txt_input = np.mean(occupancy_R_allo_adj_txt_input_tokens)
avg_r_allo_occupancy_ascii_txt_input = np.mean(occupancy_R_allo_ascii_txt_input_tokens)
avg_r_allo_occupancy_tokenized_txt_input = np.mean(occupancy_R_allo_tokenized_txt_input_tokens)
avg_r_allo_line_jpg_output = np.mean(line_R_allo_jpg_output_tokens)
avg_r_allo_line_json_output = np.mean(line_R_allo_json_output_tokens)
avg_r_allo_occupancy_jpg_output = np.mean(occupancy_R_allo_jpg_output_tokens)
avg_r_allo_occupancy_json_output = np.mean(occupancy_R_allo_json_output_tokens)
avg_r_allo_line_adj_json_output = np.mean(line_R_allo_adj_json_output_tokens)
avg_r_allo_line_adj_txt_output = np.mean(line_R_allo_adj_txt_output_tokens)
avg_r_allo_line_tokenized_txt_output = np.mean(line_R_allo_tokenized_txt_output_tokens)
avg_r_allo_occupancy_adj_json_output = np.mean(occupancy_R_allo_adj_json_output_tokens)
avg_r_allo_occupancy_adj_txt_output = np.mean(occupancy_R_allo_adj_txt_output_tokens)
avg_r_allo_occupancy_ascii_txt_output = np.mean(occupancy_R_allo_ascii_txt_output_tokens)
avg_r_allo_occupancy_tokenized_txt_output = np.mean(occupancy_R_allo_tokenized_txt_output_tokens)


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
line_R_ego_adj_json = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_adj_txt = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_jpg = np.array([25.0, 0.0, 50.0, 50.0, 33.33333333333333, 0.0, 0.0, 100.0, 16.666666666666664, 110.00000000000001])
line_R_ego_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 100.0, 100.0, 75.0])
occupancy_R_ego_jpg = np.array([12.5, 0.0, 0.0, 50.0, 33.33333333333333, 0.0, 12.5, 91.66666666666666, 8.333333333333332, 37.5])
occupancy_R_ego_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])


# Raw Scores
line_R_ego_adj_json_raw_score = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_ego_adj_txt_raw_score = np.array([1.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_ego_jpg_raw_score = np.array([1.0, 0.0, 2.0, 2.0, 2.0, 0.0, 0.0, 6.0, 1.0, 4.0])
line_R_ego_json_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
line_R_ego_tokenized_txt_raw_score = np.array([4.0, 4.0, 4.0, 4.0, 6.0, 4.0, 4.0, 6.0, 6.0, 4.0])
occupancy_R_ego_adj_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_ego_adj_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_ego_ascii_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 4.0, 12.0, 12.0, 6.0])
occupancy_R_ego_jpg_raw_score = np.array([1.0, 0.0, 0.0, 4.0, 4.0, 0.0, 1.0, 11.0, 1.0, 3.0])
occupancy_R_ego_json_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8.0])
occupancy_R_ego_tokenized_txt_raw_score = np.array([8.0, 8.0, 8.0, 8.0, 12.0, 8.0, 8.0, 12.0, 12.0, 8])

# Prompt tokens
line_R_ego_adj_json_input_tokens = np.array([822.0, 822.0, 829.0, 829.0, 829.0, 829.0, 829.0, 829.0, 829.0, 829.0])
line_R_ego_adj_txt_input_tokens = np.array([454.0, 454.0, 461.0, 461.0, 461.0, 461.0, 461.0, 461.0, 461.0, 461.0])
line_R_ego_jpg_input_tokens = np.array([537.0, 537.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0])
line_R_ego_json_input_tokens = np.array([760.0, 760.0, 767.0, 767.0, 767.0, 767.0, 767.0, 767.0, 767.0, 767.0])
line_R_ego_tokenized_txt_input_tokens = np.array([425.0, 425.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0])
occupancy_R_ego_adj_json_input_tokens = np.array([1284.0, 1284.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0, 1291.0])
occupancy_R_ego_adj_txt_input_tokens = np.array([566.0, 566.0, 573.0, 573.0, 573.0, 573.0, 573.0, 573.0, 573.0, 573.0])
occupancy_R_ego_ascii_txt_input_tokens = np.array([302.0, 302.0, 307.0, 309.0, 309.0, 309.0, 309.0, 309.0, 309.0, 307.0])
occupancy_R_ego_jpg_input_tokens = np.array([542.0, 542.0, 549.0, 549.0, 549.0, 549.0, 549.0, 549.0, 549.0, 549.0])
occupancy_R_ego_json_input_tokens = np.array([575.0, 575.0, 582.0, 582.0, 582.0, 582.0, 582.0, 582.0, 582.0, 582.0])
occupancy_R_ego_tokenized_txt_input_tokens = np.array([854.0, 854.0, 861.0, 861.0, 860.0, 860.0, 860.0, 860.0, 860.0, 860])


# Output tokens
line_R_ego_adj_json_output_tokens = np.array([3560.0, 2534.0, 2248.0, 5136.0, 2161.0, 1990.0, 2845.0, 3926.0, 3096.0, 2119.0])
line_R_ego_adj_txt_output_tokens = np.array([2930.0, 3587.0, 1933.0, 2641.0, 3112.0, 4863.0, 2100.0, 3512.0, 4410.0, 4022.0])
line_R_ego_jpg_output_tokens = np.array([8539.0, 4203.0, 1105.0, 6439.0, 2083.0, 1169.0, 2926.0, 6573.0, 956.0, 3620.0])
line_R_ego_json_output_tokens = np.array([2401.0, 3116.0, 2388.0, 2223.0, 1786.0, 2653.0, 2229.0, 2922.0, 2328.0, 1745.0])
line_R_ego_tokenized_txt_output_tokens = np.array([3418.0, 3481.0, 2694.0, 2831.0, 5562.0, 1329.0, 3137.0, 4427.0, 4192.0, 4997.0])
occupancy_R_ego_adj_json_output_tokens = np.array([2912.0, 2264.0, 2449.0, 5428.0, 3254.0, 5593.0, 4609.0, 9388.0, 2930.0, 3499.0])
occupancy_R_ego_adj_txt_output_tokens = np.array([5534.0, 2162.0, 5607.0, 3270.0, 3786.0, 5441.0, 6224.0, 8755.0, 7211.0, 3472.0])
occupancy_R_ego_ascii_txt_output_tokens = np.array([7469.0, 3371.0, 3412.0, 9243.0, 4083.0, 2292.0, 3412.0, 8108.0, 6947.0, 3962.0])
occupancy_R_ego_jpg_output_tokens = np.array([4816.0, 9362.0, 2226.0, 1635.0, 2873.0, 10455.0, 10761.0, 2276.0, 3848.0, 3554.0])
occupancy_R_ego_json_output_tokens = np.array([4612.0, 5353.0, 4658.0, 4597.0, 4898.0, 3064.0, 3409.0, 4365.0, 4804.0, 4792.0])
occupancy_R_ego_tokenized_txt_output_tokens = np.array([3530.0, 4654.0, 2890.0, 4121.0, 5383.0, 4001.0, 7766.0, 3142.0, 3579.0, 3581])


avg_r_ego_line_jpg_input = np.mean(line_R_ego_jpg_input_tokens)
avg_r_ego_line_json_input = np.mean(line_R_ego_json_input_tokens)
avg_r_ego_occupancy_jpg_input = np.mean(occupancy_R_ego_jpg_input_tokens)
avg_r_ego_occupancy_json_input = np.mean(occupancy_R_ego_json_input_tokens)
avg_r_ego_line_adj_json_input = np.mean(line_R_ego_adj_json_input_tokens)
avg_r_ego_line_adj_txt_input = np.mean(line_R_ego_adj_txt_input_tokens)
avg_r_ego_line_tokenized_txt_input = np.mean(line_R_ego_tokenized_txt_input_tokens)
avg_r_ego_occupancy_adj_json_input = np.mean(occupancy_R_ego_adj_json_input_tokens)
avg_r_ego_occupancy_adj_txt_input = np.mean(occupancy_R_ego_adj_txt_input_tokens)
avg_r_ego_occupancy_ascii_txt_input = np.mean(occupancy_R_ego_ascii_txt_input_tokens)
avg_r_ego_occupancy_tokenized_txt_input = np.mean(occupancy_R_ego_tokenized_txt_input_tokens)
avg_r_ego_line_jpg_output = np.mean(line_R_ego_jpg_output_tokens)
avg_r_ego_line_json_output = np.mean(line_R_ego_json_output_tokens)
avg_r_ego_occupancy_jpg_output = np.mean(occupancy_R_ego_jpg_output_tokens)
avg_r_ego_occupancy_json_output = np.mean(occupancy_R_ego_json_output_tokens)
avg_r_ego_line_adj_json_output = np.mean(line_R_ego_adj_json_output_tokens)
avg_r_ego_line_adj_txt_output = np.mean(line_R_ego_adj_txt_output_tokens)
avg_r_ego_line_tokenized_txt_output = np.mean(line_R_ego_tokenized_txt_output_tokens)
avg_r_ego_occupancy_adj_json_output = np.mean(occupancy_R_ego_adj_json_output_tokens)
avg_r_ego_occupancy_adj_txt_output = np.mean(occupancy_R_ego_adj_txt_output_tokens)
avg_r_ego_occupancy_ascii_txt_output = np.mean(occupancy_R_ego_ascii_txt_output_tokens)
avg_r_ego_occupancy_tokenized_txt_output = np.mean(occupancy_R_ego_tokenized_txt_output_tokens)


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