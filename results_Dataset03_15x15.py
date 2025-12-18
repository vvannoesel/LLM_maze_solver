import numpy as np
import pandas as pd
import dataframe_image as dfi

representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']


# NR - COORDS - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_coords_adj_json_15 = np.array([2.2900763358778624, 28.985507246376812, 31.654676258992804, 40.35087719298245, 3.937007874015748, 18.81188118811881, 7.462686567164178, 36.708860759493675, 11.278195488721805, 27.659574468085108])
line_NR_coords_adj_txt_15 = np.array([8.396946564885496, 27.536231884057973, 10.79136690647482, 15.789473684210526, 4.724409448818897, 23.762376237623762, 4.477611940298507, 3.79746835443038, 5.263157894736842, 34.04255319148936])
line_NR_coords_jpg_15 = np.array([3.0534351145038165, 1.4492753623188406, 2.158273381294964, 1.7543859649122806, 0.7874015748031495, 0.9900990099009901, 1.4925373134328357, 1.2658227848101267, 2.2556390977443606, 2.127659574468085])
line_NR_coords_json_15 = np.array([1.5267175572519083, 5.797101449275362, 1.4388489208633095, 1.7543859649122806, 3.937007874015748, 0.9900990099009901, 1.4925373134328357, 2.5316455696202533, 2.2556390977443606, 2.127659574468085])
line_NR_coords_tokenized_txt_15 = np.array([0.7633587786259541, 0.0, 0.0, 7.017543859649122, 1.574803149606299, 0.9900990099009901, 0.0, 0.0, 0.0, 2.127659574468085])
occupancy_NR_coords_adj_json_15 = np.array([25.67049808429119, 8.02919708029197, 3.2490974729241873, 54.86725663716814, 14.624505928853754, 42.28855721393035, 63.90977443609023, 14.64968152866242, 6.415094339622642, 13.978494623655912])
occupancy_NR_coords_adj_txt_15 = np.array([5.747126436781609, 6.569343065693431, 3.2490974729241873, 32.743362831858406, 9.881422924901186, 24.378109452736318, 26.31578947368421, 32.48407643312102, 26.037735849056602, 34.40860215053764])
occupancy_NR_coords_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_jpg_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_15 = np.array([0.38314176245210724, 0.7299270072992701, 0.36101083032490977, 6.1946902654867255, 3.557312252964427, 8.45771144278607, 3.7593984962406015, 3.1847133757961785, 0.37735849056603776, 9.67741935483871])
occupancy_NR_coords_tokenized_txt_15 = np.array([0.38314176245210724, 0.7299270072992701, 0.36101083032490977, 6.1946902654867255, 4.3478260869565215, 6.467661691542288, 8.270676691729323, 5.7324840764331215, 0.37735849056603776, 11.827956989247312])


# Raw Scores
line_NR_coords_adj_json_raw_score_15 = np.array([3.0, 20.0, 44.0, 23.0, 5.0, 19.0, 5.0, 29.0, 15.0, 13.0])
line_NR_coords_adj_txt_raw_score_15 = np.array([11.0, 19.0, 15.0, 9.0, 6.0, 24.0, 3.0, 3.0, 7.0, 16.0])
line_NR_coords_jpg_raw_score_15 = np.array([4.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0])
line_NR_coords_json_raw_score_15 = np.array([2.0, 4.0, 2.0, 1.0, 5.0, 1.0, 1.0, 2.0, 3.0, 1.0])
line_NR_coords_tokenized_txt_raw_score_15 = np.array([1.0, 0.0, 0.0, 4.0, 2.0, 1.0, 0.0, 0.0, 0.0, 1.0])
occupancy_NR_coords_adj_json_raw_score_15 = np.array([67.0, 11.0, 9.0, 62.0, 37.0, 85.0, 85.0, 23.0, 17.0, 13.0])
occupancy_NR_coords_adj_txt_raw_score_15 = np.array([15.0, 9.0, 9.0, 37.0, 25.0, 49.0, 35.0, 51.0, 69.0, 32.0])
occupancy_NR_coords_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_jpg_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_raw_score_15 = np.array([1.0, 1.0, 1.0, 7.0, 9.0, 17.0, 5.0, 5.0, 1.0, 9.0])
occupancy_NR_coords_tokenized_txt_raw_score_15 = np.array([1.0, 1.0, 1.0, 7, 11.0, 13.0, 11.0, 9.0, 1.0, 11.0])


# Prompt tokens
line_NR_coords_adj_json_input_tokens_15 = np.array([13491.0, 13493.0, 13492.0, 13497.0, 13491.0, 13495.0, 13493.0, 13493.0, 13494.0, 13498.0])
line_NR_coords_adj_txt_input_tokens_15 = np.array([3683.0, 3685.0, 3684.0, 3689.0, 3683.0, 3687.0, 3685.0, 3685.0, 3686.0, 3690.0])
line_NR_coords_jpg_input_tokens_15 = np.array([437.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0])
line_NR_coords_json_input_tokens_15 = np.array([9808.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0])
line_NR_coords_tokenized_txt_input_tokens_15 = np.array([3283.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0])
occupancy_NR_coords_adj_json_input_tokens_15 = np.array([27636.0, 27635.0, 27643.0, 27640.0, 27647.0, 27648.0, 27648.0, 27647.0, 27641.0, 27638.0])
occupancy_NR_coords_adj_txt_input_tokens_15 = np.array([7732.0, 7733.0, 7739.0, 7737.0, 7741.0, 7743.0, 7743.0, 7742.0, 7737.0, 7735.0])
occupancy_NR_coords_ascii_txt_input_tokens_15 = np.array([549.0, 548.0, 554.0, 541.0, 535.0, 536.0, 543.0, 556.0, 551.0, 547.0])
occupancy_NR_coords_jpg_input_tokens_15 = np.array([432.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0, 439.0])
occupancy_NR_coords_json_input_tokens_15 = np.array([4247.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0])
occupancy_NR_coords_tokenized_txt_input_tokens_15 = np.array([12136.0, 12142.0, 12142.0, 12142, 12142.0, 12142.0, 12142.0, 12142.0, 12142.0, 12142.0])


# Output tokens
line_NR_coords_adj_json_output_tokens_15 = np.array([256.0, 606.0, 648.0, 202.0, 637.0, 204.0, 650.0, 650.0, 650.0, 165.0])
line_NR_coords_adj_txt_output_tokens_15 = np.array([557.0, 418.0, 650.0, 387.0, 188.0, 310.0, 568.0, 603.0, 650.0, 254.0])
line_NR_coords_jpg_output_tokens_15 = np.array([147.0, 182.0, 153.0, 164.0, 219.0, 335.0, 174.0, 257.0, 174.0, 132.0])
line_NR_coords_json_output_tokens_15 = np.array([152.0, 141.0, 650.0, 213.0, 211.0, 300.0, 136.0, 260.0, 444.0, 220.0])
line_NR_coords_tokenized_txt_output_tokens_15 = np.array([172.0, 146.0, 350.0, 237.0, 149.0, 141.0, 230.0, 208.0, 130.0, 141.0])
occupancy_NR_coords_adj_json_output_tokens_15 = np.array([650.0, 515.0, 92.0, 615.0, 650.0, 650.0, 650.0, 650.0, 650.0, 429.0])
occupancy_NR_coords_adj_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 621.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_coords_ascii_txt_output_tokens_15 = np.array([329.0, 650.0, 649.0, 592.0, 339.0, 650.0, 582.0, 416.0, 321.0, 650.0])
occupancy_NR_coords_jpg_output_tokens_15 = np.array([583.0, 469.0, 472.0, 409.0, 457.0, 495.0, 419.0, 465.0, 310.0, 335.0])
occupancy_NR_coords_json_output_tokens_15 = np.array([297.0, 298.0, 302.0, 587.0, 339.0, 650.0, 410.0, 295.0, 313.0, 650.0])
occupancy_NR_coords_tokenized_txt_output_tokens_15 = np.array([302.0, 297.0, 650.0, 650, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])

avg_nr_coords_line_jpg_input = np.mean(line_NR_coords_jpg_input_tokens_15)
avg_nr_coords_line_json_input = np.mean(line_NR_coords_json_input_tokens_15)
avg_nr_coords_occupancy_jpg_input = np.mean(occupancy_NR_coords_jpg_input_tokens_15)
avg_nr_coords_occupancy_json_input = np.mean(occupancy_NR_coords_json_input_tokens_15)
avg_nr_coords_line_adj_json_input = np.mean(line_NR_coords_adj_json_input_tokens_15)
avg_nr_coords_line_adj_txt_input = np.mean(line_NR_coords_adj_txt_input_tokens_15)
avg_nr_coords_line_tokenized_txt_input = np.mean(line_NR_coords_tokenized_txt_input_tokens_15)
avg_nr_coords_occupancy_adj_json_input = np.mean(occupancy_NR_coords_adj_json_input_tokens_15)
avg_nr_coords_occupancy_adj_txt_input = np.mean(occupancy_NR_coords_adj_txt_input_tokens_15)
avg_nr_coords_occupancy_ascii_txt_input = np.mean(occupancy_NR_coords_ascii_txt_input_tokens_15)
avg_nr_coords_occupancy_tokenized_txt_input = np.mean(occupancy_NR_coords_tokenized_txt_input_tokens_15)
avg_nr_coords_line_jpg_output = np.mean(line_NR_coords_jpg_output_tokens_15)
avg_nr_coords_line_json_output = np.mean(line_NR_coords_json_output_tokens_15)
avg_nr_coords_occupancy_jpg_output = np.mean(occupancy_NR_coords_jpg_output_tokens_15)
avg_nr_coords_occupancy_json_output = np.mean(occupancy_NR_coords_json_output_tokens_15)
avg_nr_coords_line_adj_json_output = np.mean(line_NR_coords_adj_json_output_tokens_15)
avg_nr_coords_line_adj_txt_output = np.mean(line_NR_coords_adj_txt_output_tokens_15)
avg_nr_coords_line_tokenized_txt_output = np.mean(line_NR_coords_tokenized_txt_output_tokens_15)
avg_nr_coords_occupancy_adj_json_output = np.mean(occupancy_NR_coords_adj_json_output_tokens_15)
avg_nr_coords_occupancy_adj_txt_output = np.mean(occupancy_NR_coords_adj_txt_output_tokens_15)
avg_nr_coords_occupancy_ascii_txt_output = np.mean(occupancy_NR_coords_ascii_txt_output_tokens_15)
avg_nr_coords_occupancy_tokenized_txt_output = np.mean(occupancy_NR_coords_tokenized_txt_output_tokens_15)

# # Set up runs for table
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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Flash Lite, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_NR_coords.png")




# NR - ALLO - 1-10 ----------------------------------------------------------------

# Accuracy
line_NR_allo_adj_json_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 3.1746031746031744, 8.0, 1.5151515151515151, 1.282051282051282, 0.0, 2.1739130434782608])
line_NR_allo_adj_txt_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 3.968253968253968, 10.0, 1.5151515151515151, 1.282051282051282, 0.0, 2.1739130434782608])
line_NR_allo_jpg_15 = np.array([np.nan, 0.0, 0.0, 3.571428571428571, 0.7936507936507936, np.nan, np.nan, np.nan, 0.0, 10.869565217391305])
line_NR_allo_json_15 = np.array([1.5384615384615385, 4.411764705882353, 0.7246376811594203, 1.7857142857142856, 1.5873015873015872, 8.0, 0.0, np.nan, 0.7575757575757576, np.nan])
line_NR_allo_tokenized_txt_15 = np.array([0.0, np.nan, 0.0, 0.0, 0.0, np.nan, 3.0303030303030303, 0.0, 0.0, np.nan])
occupancy_NR_allo_adj_json_15 = np.array([0.7692307692307693, 1.4705882352941175, 2.1739130434782608, np.nan, 2.380952380952381, 7.000000000000001, 2.272727272727273, 2.564102564102564, 1.5151515151515151, 8.695652173913043])
occupancy_NR_allo_adj_txt_15 = np.array([0.0, np.nan, 0.7246376811594203, 0.0, 0.0, 8.0, 3.0303030303030303, np.nan, 0.7575757575757576, 0.0])
occupancy_NR_allo_ascii_txt_15 = np.array([0.0, 0.0, 0.7246376811594203, 2.6785714285714284, 0.0, np.nan, 2.272727272727273, 1.9230769230769231, 0.0, 3.260869565217391])
occupancy_NR_allo_jpg_15 = np.array([0.0, 0.0, 0.0, 0.8928571428571428, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
occupancy_NR_allo_json_15 = np.array([0.0, 0.0, 0.0, 0.8928571428571428, 2.380952380952381, 0.0, 0.7575757575757576, 0.641025641025641, 0.0, 1.0869565217391304])
occupancy_NR_allo_tokenized_txt_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 2.380952380952381, 6.0, 3.0303030303030303, 1.9230769230769231, 0.0, 4.3478260869565215])


# Raw Scores
line_NR_allo_adj_json_raw_score_15 = np.array([0.0, 0.0, 0.0, 1.0, 4.0, 8.0, 1.0, 1.0, 0.0, 1.0])
line_NR_allo_adj_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 1.0, 5.0, 10.0, 1.0, 1.0, 0.0, 1.0])
line_NR_allo_jpg_raw_score_15 = np.array([0.0, 0.0, 0.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, 5.0])
line_NR_allo_json_raw_score_15 = np.array([2.0, 3.0, 1.0, 1.0, 2.0, 8.0, 0.0, 0.0, 1.0, 0.0])
line_NR_allo_tokenized_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0])
occupancy_NR_allo_adj_json_raw_score_15 = np.array([2.0, 2.0, 6.0, 0.0, 6.0, 14.0, 3.0, 4.0, 4.0, 8.0])
occupancy_NR_allo_adj_txt_raw_score_15 = np.array([0.0, 0.0, 2.0, 0.0, 0.0, 16.0, 4.0, 0.0, 2.0, 0.0])
occupancy_NR_allo_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 2.0, 3.0, 0.0, 0.0, 3.0, 3.0, 0.0, 3.0])
occupancy_NR_allo_jpg_raw_score_15 = np.array([0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_allo_json_raw_score_15 = np.array([0.0, 0.0, 0.0, 1.0, 6.0, 0.0, 1.0, 1.0, 0.0, 1.0])
occupancy_NR_allo_tokenized_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 2.0, 6.0, 12.0, 4.0, 3.0, 0.0, 4.0])


# Prompt tokens
line_NR_allo_adj_json_input_tokens_15 = np.array([13483.0, 13485.0, 13484.0, 13489.0, 13483.0, 13487.0, 13485.0, 13485.0, 13486.0, 13490.0])
line_NR_allo_adj_txt_input_tokens_15 = np.array([3675.0, 3677.0, 3676.0, 3681.0, 3675.0, 3679.0, 3677.0, 3677.0, 3678.0, 3682.0])
line_NR_allo_jpg_input_tokens_15 = np.array([436.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0])
line_NR_allo_json_input_tokens_15 = np.array([9800.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0])
line_NR_allo_tokenized_txt_input_tokens_15 = np.array([3275.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0])
occupancy_NR_allo_adj_json_input_tokens_15 = np.array([27628.0, 27627.0, 27635.0, 27632.0, 27639.0, 27640.0, 27640.0, 27639.0, 27633.0, 27630.0])
occupancy_NR_allo_adj_txt_input_tokens_15 = np.array([7724, 7725.0, 7731.0, 7729.0, 7733.0, 7735.0, 7735.0, 7734.0, 7729.0, 7727.0])
occupancy_NR_allo_ascii_txt_input_tokens_15 = np.array([541.0, 540.0, 546.0, 533.0, 527.0, 528.0, 535.0, 548.0, 543.0, 539.0])
occupancy_NR_allo_jpg_input_tokens_15 = np.array([431, 431.0, 431.0, 431.0, 431.0, 431.0, 431.0, 431.0, 431.0, 431.0])
occupancy_NR_allo_json_input_tokens_15 = np.array([4239.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0])
occupancy_NR_allo_tokenized_txt_input_tokens_15 = np.array([12128.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0])


# Output tokens
line_NR_allo_adj_json_output_tokens_15 = np.array([650.0, 99.0, 57.0, 55.0, 57.0, 650.0, 57.0, 57.0, 57.0, 85.0])
line_NR_allo_adj_txt_output_tokens_15 = np.array([57.0, 650.0, 650.0, 533.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_allo_jpg_output_tokens_15 = np.array([0.0, 113.0, 650.0, 81.0, 650.0, 0.0, 0.0, 0.0, 103.0, 650.0])
line_NR_allo_json_output_tokens_15 = np.array([55.0, 53.0, 55.0, 650.0, 650.0, 650.0, 650.0, 0.0, 55.0, 0.0])
line_NR_allo_tokenized_txt_output_tokens_15 = np.array([650.0, 0.0, 650.0, 650.0, 650.0, 0.0, 650.0, 650.0, 650.0, 0.0])
occupancy_NR_allo_adj_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 0.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_adj_txt_output_tokens_15 = np.array([650.0, 0.0, 115.0, 117.0, 650.0, 650.0, 59.0, 0.0, 113.0, 650.0])
occupancy_NR_allo_ascii_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 0.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_jpg_output_tokens_15 = np.array([650, 650.0, 650.0, 650.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_allo_json_output_tokens_15 = np.array([650.0, 57.0, 650.0, 650.0, 650.0, 119.0, 650.0, 650.0, 57.0, 650.0])
occupancy_NR_allo_tokenized_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])


avg_nr_allo_line_jpg_input = np.mean(line_NR_allo_jpg_input_tokens_15)
avg_nr_allo_line_json_input = np.mean(line_NR_allo_json_input_tokens_15)
avg_nr_allo_occupancy_jpg_input = np.mean(occupancy_NR_allo_jpg_input_tokens_15)
avg_nr_allo_occupancy_json_input = np.mean(occupancy_NR_allo_json_input_tokens_15)
avg_nr_allo_line_adj_json_input = np.mean(line_NR_allo_adj_json_input_tokens_15)
avg_nr_allo_line_adj_txt_input = np.mean(line_NR_allo_adj_txt_input_tokens_15)
avg_nr_allo_line_tokenized_txt_input = np.mean(line_NR_allo_tokenized_txt_input_tokens_15)
avg_nr_allo_occupancy_adj_json_input = np.mean(occupancy_NR_allo_adj_json_input_tokens_15)
avg_nr_allo_occupancy_adj_txt_input = np.mean(occupancy_NR_allo_adj_txt_input_tokens_15)
avg_nr_allo_occupancy_ascii_txt_input = np.mean(occupancy_NR_allo_ascii_txt_input_tokens_15)
avg_nr_allo_occupancy_tokenized_txt_input = np.mean(occupancy_NR_allo_tokenized_txt_input_tokens_15)
avg_nr_allo_line_jpg_output = np.mean(line_NR_allo_jpg_output_tokens_15)
avg_nr_allo_line_json_output = np.mean(line_NR_allo_json_output_tokens_15)
avg_nr_allo_occupancy_jpg_output = np.mean(occupancy_NR_allo_jpg_output_tokens_15)
avg_nr_allo_occupancy_json_output = np.mean(occupancy_NR_allo_json_output_tokens_15)
avg_nr_allo_line_adj_json_output = np.mean(line_NR_allo_adj_json_output_tokens_15)
avg_nr_allo_line_adj_txt_output = np.mean(line_NR_allo_adj_txt_output_tokens_15)
avg_nr_allo_line_tokenized_txt_output = np.mean(line_NR_allo_tokenized_txt_output_tokens_15)
avg_nr_allo_occupancy_adj_json_output = np.mean(occupancy_NR_allo_adj_json_output_tokens_15)
avg_nr_allo_occupancy_adj_txt_output = np.mean(occupancy_NR_allo_adj_txt_output_tokens_15)
avg_nr_allo_occupancy_ascii_txt_output = np.mean(occupancy_NR_allo_ascii_txt_output_tokens_15)
avg_nr_allo_occupancy_tokenized_txt_output = np.mean(occupancy_NR_allo_tokenized_txt_output_tokens_15)

# # Set up runs for table
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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Flash Lite, Allocentric Output  ** nan = no answer given").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_NR_allo.png")



# NR - EGO - 1-10 ----------------------------------------------------------------

# Accuracy

line_NR_ego_adj_json_15 = np.array([0.0, 0.0, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_15 = np.array([1.5384615384615385, 4.411764705882353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_NR_ego_jpg_15 = np.array([1.5384615384615385, 5.88235294117647, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_NR_ego_json_15 = np.array([1.5384615384615385, 0.0, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_NR_ego_tokenized_txt_15 = np.array([0.7692307692307693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_NR_ego_adj_txt_15 = np.array([1.5384615384615385, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_NR_ego_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_15 = np.array([0.7692307692307693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
occupancy_NR_ego_json_15 = np.array([0.0, 0.0, 0.36231884057971014, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
occupancy_NR_ego_tokenized_txt_15 = np.array([0.38461538461538464, 4.411764705882353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])


# Raw Scores
line_NR_ego_adj_json_raw_score_15 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_raw_score_15 = np.array([2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
line_NR_ego_jpg_raw_score_15 = np.array([2.0, 4.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
line_NR_ego_json_raw_score_15 = np.array([2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
line_NR_ego_tokenized_txt_raw_score_15 = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_json_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
occupancy_NR_ego_adj_txt_raw_score_15 = np.array([4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
occupancy_NR_ego_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_raw_score_15 = np.array([2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
occupancy_NR_ego_json_raw_score_15 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
occupancy_NR_ego_tokenized_txt_raw_score_15 = np.array([1.0, 6.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 1.0, 0.0])


# Prompt tokens
line_NR_ego_adj_json_input_tokens_15 = np.array([13607.0, 13609.0, 13608.0, 13613.0, 13607.0, 13611.0, 13609.0, 13609.0, 13610.0, 13614.0])
line_NR_ego_adj_txt_input_tokens_15 = np.array([3799.0, 3801.0, 3800.0, 3805.0, 3799.0, 3803.0, 3801.0, 3801.0, 3802.0, 3806.0])
line_NR_ego_jpg_input_tokens_15 = np.array([553.0, 560.0, 560.0, 560.0, 560.0, 560.0, 560.0, 560.0, 560.0, 560.0])
line_NR_ego_json_input_tokens_15 = np.array([9924.0, 9931.0, 9931.0, 9931.0, 9931.0, 9931.0, 9931.0, 9931.0, 9931.0, 9931.0])
line_NR_ego_tokenized_txt_input_tokens_15 = np.array([3399.0, 3406.0, 3406.0, 3406.0, 3406.0, 3406.0, 3406.0, 3406.0, 3406.0, 3406.0])
occupancy_NR_ego_adj_json_input_tokens_15 = np.array([27752.0, 27751.0, 27759.0, 27756.0, 27763.0, 27764.0, 27764.0, 27763.0, 27757.0, 27754.0])
occupancy_NR_ego_adj_txt_input_tokens_15 = np.array([7848.0, 7849.0, 7855.0, 7853.0, 7857.0, 7859.0, 7859.0, 7858.0, 7853.0, 7851.0])
occupancy_NR_ego_ascii_txt_input_tokens_15 = np.array([665.0, 664.0, 670.0, 657.0, 651.0, 652.0, 659.0, 672.0, 667.0, 663.0])
occupancy_NR_ego_jpg_input_tokens_15 = np.array([548.0, 555.0, 555.0, 555.0, 555.0, 555.0, 555.0, 555.0, 555.0, 555.0])
occupancy_NR_ego_json_input_tokens_15 = np.array([4363.0, 4370.0, 4370.0, 4370.0, 4370.0, 4370.0, 4370.0, 4370.0, 4370.0, 4370.0])
occupancy_NR_ego_tokenized_txt_input_tokens_15 = np.array([12252.0, 12258.0, 12258.0, 12258.0, 12258.0, 12258, 12258.0, 12258.0, 12258.0, 12258.0])


# Output tokens
line_NR_ego_adj_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_adj_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_jpg_output_tokens_15 = np.array([133.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
line_NR_ego_tokenized_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_ascii_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_jpg_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_json_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_tokenized_txt_output_tokens_15 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650, 650.0, 650.0, 650.0, 650.0])

avg_nr_ego_line_jpg_input = np.mean(line_NR_ego_jpg_input_tokens_15)
avg_nr_ego_line_json_input = np.mean(line_NR_ego_json_input_tokens_15)
avg_nr_ego_occupancy_jpg_input = np.mean(occupancy_NR_ego_jpg_input_tokens_15)
avg_nr_ego_occupancy_json_input = np.mean(occupancy_NR_ego_json_input_tokens_15)
avg_nr_ego_line_adj_json_input = np.mean(line_NR_ego_adj_json_input_tokens_15)
avg_nr_ego_line_adj_txt_input = np.mean(line_NR_ego_adj_txt_input_tokens_15)
avg_nr_ego_line_tokenized_txt_input = np.mean(line_NR_ego_tokenized_txt_input_tokens_15)
avg_nr_ego_occupancy_adj_json_input = np.mean(occupancy_NR_ego_adj_json_input_tokens_15)
avg_nr_ego_occupancy_adj_txt_input = np.mean(occupancy_NR_ego_adj_txt_input_tokens_15)
avg_nr_ego_occupancy_ascii_txt_input = np.mean(occupancy_NR_ego_ascii_txt_input_tokens_15)
avg_nr_ego_occupancy_tokenized_txt_input = np.mean(occupancy_NR_ego_tokenized_txt_input_tokens_15)
avg_nr_ego_line_jpg_output = np.mean(line_NR_ego_jpg_output_tokens_15)
avg_nr_ego_line_json_output = np.mean(line_NR_ego_json_output_tokens_15)
avg_nr_ego_occupancy_jpg_output = np.mean(occupancy_NR_ego_jpg_output_tokens_15)
avg_nr_ego_occupancy_json_output = np.mean(occupancy_NR_ego_json_output_tokens_15)
avg_nr_ego_line_adj_json_output = np.mean(line_NR_ego_adj_json_output_tokens_15)
avg_nr_ego_line_adj_txt_output = np.mean(line_NR_ego_adj_txt_output_tokens_15)
avg_nr_ego_line_tokenized_txt_output = np.mean(line_NR_ego_tokenized_txt_output_tokens_15)
avg_nr_ego_occupancy_adj_json_output = np.mean(occupancy_NR_ego_adj_json_output_tokens_15)
avg_nr_ego_occupancy_adj_txt_output = np.mean(occupancy_NR_ego_adj_txt_output_tokens_15)
avg_nr_ego_occupancy_ascii_txt_output = np.mean(occupancy_NR_ego_ascii_txt_output_tokens_15)
avg_nr_ego_occupancy_tokenized_txt_output = np.mean(occupancy_NR_ego_tokenized_txt_output_tokens_15)


# # Set up runs for table
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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Flash Lite, Egocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_NR_ego.png")





# R - COORDS - 1-10  ----------------------------------------------------------------

# Accuracy
line_R_coords_adj_json_15 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt_15 = np.array([19.083969465648856, 14.492753623188406, 51.798561151079134, 100.0, 60.629921259842526, 92.07920792079209, 100.0, 56.9620253164557, 46.616541353383454, 100.0])
line_R_coords_jpg_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_15 = np.array([23.66412213740458, 15.942028985507244, 7.194244604316546, 7.017543859649122, 12.598425196850393, 9.900990099009901, 56.71641791044776, 50.63291139240506, 1.5037593984962405, 42.5531914893617])
line_R_coords_tokenized_txt_15 = np.array([96.18320610687023, 100.0, 100.0, 100.0, 92.1259842519685, 22.772277227722775, 100.0, 62.0253164556962, 100.0, 100.0])
occupancy_R_coords_adj_json_15 = np.array([100.0, 100.0, 68.95306859205776, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt_15 = np.array([34.099616858237546, 15.328467153284672, 24.90974729241877, 29.20353982300885, 12.25296442687747, 42.28855721393035, 3.7593984962406015, 57.961783439490446, 46.41509433962264, 95.6989247311828])
occupancy_R_coords_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.301075268817205])
occupancy_R_coords_jpg_15 = np.array([1.9157088122605364, 4.37956204379562, 1.083032490974729, 0.8849557522123894, 0.3952569169960474, 0.0, 0.7518796992481203, 0.0, 0.0, 0.0])
occupancy_R_coords_json_15 = np.array([11.877394636015326, 35.03649635036496, 1.8050541516245486, 15.04424778761062, 3.557312252964427, 21.393034825870647, 30.075187969924812, 15.92356687898089, 7.169811320754717, 33.33333333333333])
occupancy_R_coords_tokenized_txt_15 = np.array([39.46360153256705, 100.0, 7.581227436823104, 100.0, 7.905138339920949, 7.462686567164178, 100.0, 13.375796178343949, 6.415094339622642, 11.827956989247312])


# Raw scores
line_R_coords_adj_json_raw_score_15 = np.array([131.0, 69.0, 139.0, 57.0, 127.0, 101.0, 67.0, 79.0, 133.0, 47.0])
line_R_coords_adj_txt_raw_score_15 = np.array([25.0, 10.0, 72.0, 57.0, 77.0, 93.0, 67.0, 45.0, 62.0, 47.0])
line_R_coords_jpg_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_raw_score_15 = np.array([31.0, 11.0, 10.0, 4.0, 16.0, 10.0, 38.0, 40.0, 2.0, 20.0])
line_R_coords_tokenized_txt_raw_score_15 = np.array([126.0, 69.0, 139.0, 57.0, 117.0, 23.0, 67.0, 49.0, 133.0, 47.0])
occupancy_R_coords_adj_json_raw_score_15 = np.array([261.0, 137.0, 191.0, 113.0, 253.0, 201.0, 133.0, 157.0, 265.0, 93.0])
occupancy_R_coords_adj_txt_raw_score_15 = np.array([89.0, 21.0, 69.0, 33.0, 31.0, 85.0, 5.0, 91.0, 123.0, 89.0])
occupancy_R_coords_ascii_txt_raw_score_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0])
occupancy_R_coords_jpg_raw_score_15 = np.array([5.0, 6.0, 3.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0])
occupancy_R_coords_json_raw_score_15 = np.array([31.0, 48.0, 5.0, 17.0, 9.0, 43.0, 40.0, 25.0, 19.0, 31.0])
occupancy_R_coords_tokenized_txt_raw_score_15 = np.array([103.0, 137.0, 21.0, 113.0, 20, 15.0, 133.0, 21.0, 17.0, 11.0])


# Prompt tokens
line_R_coords_adj_json_input_tokens_15 = np.array([13491.0, 13493.0, 13492.0, 13497.0, 13491.0, 13495.0, 13493.0, 13493.0, 13494.0, 13498.0])
line_R_coords_adj_txt_input_tokens_15 = np.array([3683.0, 3685.0, 3684.0, 3689.0, 3683.0, 3687.0, 3685.0, 3685.0, 3686.0, 3690.0])
line_R_coords_jpg_input_tokens_15 = np.array([437.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0, 444.0])
line_R_coords_json_input_tokens_15 = np.array([9808.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0, 9815.0])
line_R_coords_tokenized_txt_input_tokens_15 = np.array([3283.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0, 3290.0])
occupancy_R_coords_adj_json_input_tokens_15 = np.array([27636.0, 27635.0, 27643.0, 27640.0, 27647.0, 27648.0, 27648.0, 27647.0, 27641.0, 27638.0])
occupancy_R_coords_adj_txt_input_tokens_15 = np.array([7732.0, 7733.0, 7739.0, 7737.0, 7741.0, 7743.0, 7743.0, 7742.0, 7737.0, 7735.0])
occupancy_R_coords_ascii_txt_input_tokens_15 = np.array([548.0, 547.0, 553.0, 540.0, 534.0, 535.0, 542.0, 555.0, 550.0, 546.0])
occupancy_R_coords_jpg_input_tokens_15 = np.array([442.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0])
occupancy_R_coords_json_input_tokens_15 = np.array([4247.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0, 4254.0])
occupancy_R_coords_tokenized_txt_input_tokens_15 = np.array([12136.0, 12142.0, 12142.0, 12142.0, 12142, 12142.0, 12142.0, 12142.0, 12142.0, 12142.0])


# Output tokens
line_R_coords_adj_json_output_tokens_15 = np.array([24319.0, 16225.0, 24616.0, 8139.0, 19260.0, 12408.0, 7826.0, 15115.0, 20876.0, 5314.0])
line_R_coords_adj_txt_output_tokens_15 = np.array([33577.0, 24330.0, 25615.0, 20071.0, 19655.0, 28924.0, 10897.0, 23268.0, 7706.0, 14201.0])
line_R_coords_jpg_output_tokens_15 = np.array([4504.0, 3944.0, 10750.0, 16490.0, 5091.0, 4180.0, 6718.0, 7549.0, 14674.0, 6569.0])
line_R_coords_json_output_tokens_15 = np.array([14877.0, 21134.0, 24389.0, 22863.0, 26197.0, 20740.0, 29735.0, 15855.0, 23004.0, 19638.0])
line_R_coords_tokenized_txt_output_tokens_15 = np.array([27012.0, 8104.0, 16779.0, 5941.0, 17585.0, 22661.0, 10570.0, 24814.0, 14842.0, 7821.0])
occupancy_R_coords_adj_json_output_tokens_15 = np.array([38108.0, 12526.0, 44759.0, 8955.0, 18015.0, 11288.0, 13758.0, 17437.0, 30188.0, 9741.0])
occupancy_R_coords_adj_txt_output_tokens_15 = np.array([35979.0, 29317.0, 27858.0, 29722.0, 32951.0, 27173.0, 32997.0, 27944.0, 33251.0, 22642.0])
occupancy_R_coords_ascii_txt_output_tokens_15 = np.array([10674.0, 7006.0, 14414.0, 10515.0, 9263.0, 11732.0, 19721.0, 10736.0, 16575.0, 19719.0])
occupancy_R_coords_jpg_output_tokens_15 = np.array([10193.0, 12494.0, 13728.0, 8963.0, 9955.0, 5758.0, 8949.0, 16009.0, 6946.0, 17182.0])
occupancy_R_coords_json_output_tokens_15 = np.array([17287.0, 13432.0, 24426.0, 19069.0, 20997.0, 19289.0, 25754.0, 15716.0, 18421.0, 19336.0])
occupancy_R_coords_tokenized_txt_output_tokens_15 = np.array([27461.0, 12623.0, 26548.0, 17015.0, 24129, 26580.0, 19448.0, 25165.0, 27684.0, 22137.0])

avg_r_coords_line_jpg_input = np.mean(line_R_coords_jpg_input_tokens_15)
avg_r_coords_line_json_input = np.mean(line_R_coords_json_input_tokens_15)
avg_r_coords_occupancy_jpg_input = np.mean(occupancy_R_coords_jpg_input_tokens_15)
avg_r_coords_occupancy_json_input = np.mean(occupancy_R_coords_json_input_tokens_15)
avg_r_coords_line_adj_json_input = np.mean(line_R_coords_adj_json_input_tokens_15)
avg_r_coords_line_adj_txt_input = np.mean(line_R_coords_adj_txt_input_tokens_15)
avg_r_coords_line_tokenized_txt_input = np.mean(line_R_coords_tokenized_txt_input_tokens_15)
avg_r_coords_occupancy_adj_json_input = np.mean(occupancy_R_coords_adj_json_input_tokens_15)
avg_r_coords_occupancy_adj_txt_input = np.mean(occupancy_R_coords_adj_txt_input_tokens_15)
avg_r_coords_occupancy_ascii_txt_input = np.mean(occupancy_R_coords_ascii_txt_input_tokens_15)
avg_r_coords_occupancy_tokenized_txt_input = np.mean(occupancy_R_coords_tokenized_txt_input_tokens_15)
avg_r_coords_line_jpg_output = np.mean(line_R_coords_jpg_output_tokens_15)
avg_r_coords_line_json_output = np.mean(line_R_coords_json_output_tokens_15)
avg_r_coords_occupancy_jpg_output = np.mean(occupancy_R_coords_jpg_output_tokens_15)
avg_r_coords_occupancy_json_output = np.mean(occupancy_R_coords_json_output_tokens_15)
avg_r_coords_line_adj_json_output = np.mean(line_R_coords_adj_json_output_tokens_15)
avg_r_coords_line_adj_txt_output = np.mean(line_R_coords_adj_txt_output_tokens_15)
avg_r_coords_line_tokenized_txt_output = np.mean(line_R_coords_tokenized_txt_output_tokens_15)
avg_r_coords_occupancy_adj_json_output = np.mean(occupancy_R_coords_adj_json_output_tokens_15)
avg_r_coords_occupancy_adj_txt_output = np.mean(occupancy_R_coords_adj_txt_output_tokens_15)
avg_r_coords_occupancy_ascii_txt_output = np.mean(occupancy_R_coords_ascii_txt_output_tokens_15)
avg_r_coords_occupancy_tokenized_txt_output = np.mean(occupancy_R_coords_tokenized_txt_output_tokens_15)


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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15, Gemini 2.5 Pro, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_R_15x15_coords.png")



# R - ALLO - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_allo_adj_json_15 = np.array([46.92307692307692, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt_15 = np.array([7.6923076923076925, 100.0, 53.62318840579711, 100.0, 0.7936507936507936, 98.0, 100.0, 2.564102564102564, 58.333333333333336, 100.0])
line_R_allo_jpg_15 = np.array([0.7692307692307693, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_R_allo_json_15 = np.array([27.692307692307693, 14.705882352941178, 10.144927536231885, 12.5, 9.523809523809524, 26.0, 19.696969696969695, 29.48717948717949, 1.5151515151515151, 32.608695652173914])
line_R_allo_tokenized_txt_15 = np.array([33.07692307692307, 39.705882352941174, 7.971014492753622, 5.357142857142857, 39.682539682539684, 100.0, 100.0, 50.0, 60.60606060606061, 100.0])
occupancy_R_allo_adj_json_15 = np.array([46.15384615384615, 100.0, 38.405797101449274, 100.0, 34.523809523809526, 100.0, 100.0, 100.0, 71.21212121212122, 100.0])
occupancy_R_allo_adj_txt_15 = np.array([27.692307692307693, 100.0, 7.246376811594203, 14.285714285714285, 9.126984126984127, 77.0, 25.757575757575758, 67.94871794871796, 39.39393939393939, 100.0])
occupancy_R_allo_ascii_txt_15 = np.array([1.5384615384615385, 5.88235294117647, 0.0, 0.0, 0.0, 0.0, 3.0303030303030303, 1.282051282051282, 1.5151515151515151, 0.0])
occupancy_R_allo_jpg_15 = np.array([1.153846153846154, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_R_allo_json_15 = np.array([0.38461538461538464, 27.941176470588236, 5.797101449275362, 39.285714285714285, 3.1746031746031744, 7.000000000000001, 3.0303030303030303, 0.0, 3.0303030303030303, 7.608695652173914])
occupancy_R_allo_tokenized_txt_15 = np.array([25.384615384615383, 100.0, 4.3478260869565215, 100.0, 50.79365079365079, 10.0, 18.181818181818183, 61.53846153846154, 0.7575757575757576, 100.0])



# Raw Scores
line_R_allo_adj_json_raw_score_15 = np.array([61.0, 68.0, 138.0, 56.0, 126.0, 100.0, 66.0, 78.0, 132.0, 46.0])
line_R_allo_adj_txt_raw_score_15 = np.array([10.0, 68.0, 74.0, 56.0, 1.0, 98.0, 66.0, 2.0, 77.0, 46.0])
line_R_allo_jpg_raw_score_15 = np.array([1.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
line_R_allo_json_raw_score_15 = np.array([36.0, 10.0, 14.0, 7.0, 12.0, 26.0, 13.0, 23.0, 2.0, 15.0])
line_R_allo_tokenized_txt_raw_score_15 = np.array([43.0, 27.0, 11.0, 3.0, 50.0, 100.0, 66.0, 39.0, 80.0, 46.0])
occupancy_R_allo_adj_json_raw_score_15 = np.array([120.0, 136.0, 106.0, 112.0, 87.0, 200.0, 132.0, 156.0, 188.0, 92.0])
occupancy_R_allo_adj_txt_raw_score_15 = np.array([72.0, 136.0, 20.0, 16.0, 23.0, 154.0, 34.0, 106.0, 104.0, 92.0])
occupancy_R_allo_ascii_txt_raw_score_15 = np.array([4.0, 8.0, 0.0, 0.0, 0.0, 0.0, 4.0, 2.0, 4.0, 0.0])
occupancy_R_allo_jpg_raw_score_15 = np.array([3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_R_allo_json_raw_score_15 = np.array([1.0, 38.0, 16.0, 44.0, 8.0, 14.0, 4.0, 0.0, 8.0, 7.0])
occupancy_R_allo_tokenized_txt_raw_score_15 = np.array([66.0, 136.0, 12.0, 112.0, 128.0, 20.0, 24.0, 96.0, 2.0, 92])


# Prompt tokens
line_R_allo_adj_json_input_tokens_15 = np.array([13483.0, 13485.0, 13484.0, 13489.0, 13483.0, 13487.0, 13485.0, 13485.0, 13486.0, 13490.0])
line_R_allo_adj_txt_input_tokens_15 = np.array([3675.0, 3677.0, 3676.0, 3681.0, 3675.0, 3679.0, 3677.0, 3677.0, 3678.0, 3682.0])
line_R_allo_jpg_input_tokens_15 = np.array([429.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0, 436.0])
line_R_allo_json_input_tokens_15 = np.array([9800.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0, 9807.0])
line_R_allo_tokenized_txt_input_tokens_15 = np.array([3275.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0, 3282.0])
occupancy_R_allo_adj_json_input_tokens_15 = np.array([27628.0, 27627.0, 27635.0, 27632.0, 27639.0, 27640.0, 27640.0, 27639.0, 27633.0, 27630.0])
occupancy_R_allo_adj_txt_input_tokens_15 = np.array([7724.0, 7725.0, 7731.0, 7729.0, 7733.0, 7735.0, 7735.0, 7734.0, 7729.0, 7727.0])
occupancy_R_allo_ascii_txt_input_tokens_15 = np.array([540.0, 539.0, 545.0, 532.0, 526.0, 527.0, 534.0, 547.0, 542.0, 538.0])
occupancy_R_allo_jpg_input_tokens_15 = np.array([434.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0])
occupancy_R_allo_json_input_tokens_15 = np.array([4239.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0, 4246.0])
occupancy_R_allo_tokenized_txt_input_tokens_15 = np.array([12128.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134.0, 12134])


# Output tokens
line_R_allo_adj_json_output_tokens_15 = np.array([22587.0, 10727.0, 22842.0, 9131.0, 11767.0, 19558.0, 9256.0, 16737.0, 20988.0, 11533.0])
line_R_allo_adj_txt_output_tokens_15 = np.array([31007.0, 23644.0, 9234.0, 11180.0, 22655.0, 17180.0, 10782.0, 21815.0, 19407.0, 19985.0])
line_R_allo_jpg_output_tokens_15 = np.array([6803.0, 4423.0, 6075.0, 2966.0, 4505.0, 8598.0, 8694.0, 4345.0, 9458.0, 4858.0])
line_R_allo_json_output_tokens_15 = np.array([23638.0, 6698.0, 18380.0, 4923.0, 20808.0, 20562.0, 21221.0, 12816.0, 22590.0, 13677.0])
line_R_allo_tokenized_txt_output_tokens_15 = np.array([24874.0, 5662.0, 29110.0, 19105.0, 16818.0, 14950.0, 6263.0, 20016.0, 21413.0, 7500.0])
occupancy_R_allo_adj_json_output_tokens_15 = np.array([21385.0, 13601.0, 25273.0, 12155.0, 24470.0, 15482.0, 18116.0, 26090.0, 29201.0, 11509.0])
occupancy_R_allo_adj_txt_output_tokens_15 = np.array([26432.0, 17327.0, 27365.0, 33199.0, 27635.0, 34064.0, 27374.0, 28281.0, 26462.0, 10218.0])
occupancy_R_allo_ascii_txt_output_tokens_15 = np.array([6953.0, 5720.0, 3744.0, 11475.0, 7697.0, 4759.0, 9551.0, 18615.0, 11527.0, 4246.0])
occupancy_R_allo_jpg_output_tokens_15 = np.array([14420.0, 16069.0, 7911.0, 10028.0, 9050.0, 6771.0, 8747.0, 11031.0, 17497.0, 14351.0])
occupancy_R_allo_json_output_tokens_15 = np.array([18136.0, 20884.0, 15988.0, 24608.0, 18119.0, 7607.0, 12994.0, 18491.0, 22347.0, 20437.0])
occupancy_R_allo_tokenized_txt_output_tokens_15 = np.array([25641.0, 12698.0, 22502.0, 19036.0, 24018.0, 23182.0, 25434.0, 23742.0, 20451.0, 10015])

avg_r_allo_line_jpg_input = np.mean(line_R_allo_jpg_input_tokens_15)
avg_r_allo_line_json_input = np.mean(line_R_allo_json_input_tokens_15)
avg_r_allo_occupancy_jpg_input = np.mean(occupancy_R_allo_jpg_input_tokens_15)
avg_r_allo_occupancy_json_input = np.mean(occupancy_R_allo_json_input_tokens_15)
avg_r_allo_line_adj_json_input = np.mean(line_R_allo_adj_json_input_tokens_15)
avg_r_allo_line_adj_txt_input = np.mean(line_R_allo_adj_txt_input_tokens_15)
avg_r_allo_line_tokenized_txt_input = np.mean(line_R_allo_tokenized_txt_input_tokens_15)
avg_r_allo_occupancy_adj_json_input = np.mean(occupancy_R_allo_adj_json_input_tokens_15)
avg_r_allo_occupancy_adj_txt_input = np.mean(occupancy_R_allo_adj_txt_input_tokens_15)
avg_r_allo_occupancy_ascii_txt_input = np.mean(occupancy_R_allo_ascii_txt_input_tokens_15)
avg_r_allo_occupancy_tokenized_txt_input = np.mean(occupancy_R_allo_tokenized_txt_input_tokens_15)
avg_r_allo_line_jpg_output = np.mean(line_R_allo_jpg_output_tokens_15)
avg_r_allo_line_json_output = np.mean(line_R_allo_json_output_tokens_15)
avg_r_allo_occupancy_jpg_output = np.mean(occupancy_R_allo_jpg_output_tokens_15)
avg_r_allo_occupancy_json_output = np.mean(occupancy_R_allo_json_output_tokens_15)
avg_r_allo_line_adj_json_output = np.mean(line_R_allo_adj_json_output_tokens_15)
avg_r_allo_line_adj_txt_output = np.mean(line_R_allo_adj_txt_output_tokens_15)
avg_r_allo_line_tokenized_txt_output = np.mean(line_R_allo_tokenized_txt_output_tokens_15)
avg_r_allo_occupancy_adj_json_output = np.mean(occupancy_R_allo_adj_json_output_tokens_15)
avg_r_allo_occupancy_adj_txt_output = np.mean(occupancy_R_allo_adj_txt_output_tokens_15)
avg_r_allo_occupancy_ascii_txt_output = np.mean(occupancy_R_allo_ascii_txt_output_tokens_15)
avg_r_allo_occupancy_tokenized_txt_output = np.mean(occupancy_R_allo_tokenized_txt_output_tokens_15)


# # Set up runs for table
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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Pro, Allocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_R_allo.png")


# R - EGO - 1-10 ----------------------------------------------------------------

# Accuracy
line_R_ego_adj_json_15 = np.array([3.076923076923077, 100.0, 15.217391304347828, 100.0, 35.714285714285715, 100.0, 100.0, 100.0, 62.121212121212125, 100.0])
line_R_ego_adj_txt_15 = np.array([2.307692307692308, 20.588235294117645, 0.7246376811594203, 100.0, 0.0, 11.0, 0.0, 0.0, 46.21212121212121, 0.0])
line_R_ego_jpg_15 = np.array([0.7692307692307693, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5151515151515151, 0.0])
line_R_ego_json_15 = np.array([3.076923076923077, 36.76470588235294, 9.420289855072465, 0.0, 14.285714285714285, 26.0, 18.181818181818183, 7.6923076923076925, 7.575757575757576, 30.434782608695656])
line_R_ego_tokenized_txt_15 = np.array([1.5384615384615385, 29.411764705882355, 1.4492753623188406, 100.0, 0.0, 0.0, 100.0, 100.0, 0.7575757575757576, 100.0])
occupancy_R_ego_adj_json_15 = np.array([34.23076923076923, 38.23529411764706, 10.869565217391305, 100.0, 0.0, 36.0, 65.15151515151516, 50.0, 0.7575757575757576, 100.0])
occupancy_R_ego_adj_txt_15 = np.array([1.5384615384615385, 41.17647058823529, 13.768115942028986, 0.0, 0.0, 0.0, 26.515151515151516, 100.0, 5.303030303030303, 14.130434782608695])
occupancy_R_ego_ascii_txt_15 = np.array([0.7692307692307693, 6.61764705882353, 0.36231884057971014, 4.464285714285714, 3.1746031746031744, 5.5, 0.0, 0.0, 0.3787878787878788, 4.3478260869565215])
occupancy_R_ego_jpg_15 = np.array([1.5384615384615385, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_R_ego_json_15 = np.array([3.8461538461538463, 5.88235294117647, 2.1739130434782608, 10.714285714285714, 15.873015873015872, 0.0, 10.606060606060606, 6.41025641025641, 1.5151515151515151, 10.869565217391305])
occupancy_R_ego_tokenized_txt_15 = np.array([27.307692307692307, 48.529411764705884, 5.797101449275362, 0.0, 2.380952380952381, 3.5000000000000004, 39.39393939393939, 23.076923076923077, 6.0606060606060606, 15.217391304347828])


# Raw Scores
line_R_ego_adj_json_raw_score_15 = np.array([4.0, 68.0, 21.0, 56.0, 45.0, 100.0, 66.0, 78.0, 82.0, 46.0])
line_R_ego_adj_txt_raw_score_15 = np.array([3.0, 14.0, 1.0, 56.0, 0.0, 11.0, 0.0, 0.0, 61.0, 0.0])
line_R_ego_jpg_raw_score_15 = np.array([1.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
line_R_ego_json_raw_score_15 = np.array([4.0, 25.0, 13.0, 0.0, 18.0, 26.0, 12.0, 6.0, 10.0, 14.0])
line_R_ego_tokenized_txt_raw_score_15 = np.array([2.0, 20.0, 2.0, 56.0, 0.0, 0.0, 66.0, 78.0, 1.0, 46.0])
occupancy_R_ego_adj_json_raw_score_15 = np.array([89.0, 52.0, 30.0, 112.0, 0.0, 72.0, 86.0, 78.0, 2.0, 92.0])
occupancy_R_ego_adj_txt_raw_score_15 = np.array([4.0, 56.0, 38.0, 0.0, 0.0, 0.0, 35.0, 156.0, 14.0, 13.0])
occupancy_R_ego_ascii_txt_raw_score_15 = np.array([2.0, 9.0, 1.0, 5.0, 8.0, 11.0, 0.0, 0.0, 1.0, 4.0])
occupancy_R_ego_jpg_raw_score_15 = np.array([4.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0])
occupancy_R_ego_json_raw_score_15 = np.array([10.0, 8.0, 6.0, 12.0, 40.0, 0.0, 14.0, 10.0, 4.0, 10.0])
occupancy_R_ego_tokenized_txt_raw_score_15 = np.array([71.0, 66.0, 16.0, 0.0, 6.0, 7.0, 52.0, 36.0, 16.0, 14])



# Prompt tokens
line_R_ego_adj_json_input_tokens_15 = np.array([13600.0, 13602.0, 13601.0, 13606.0, 13600.0, 13604.0, 13602.0, 13602.0, 13603.0, 13607.0])
line_R_ego_adj_txt_input_tokens_15 = np.array([3792.0, 3794.0, 3793.0, 3798.0, 3792.0, 3796.0, 3794.0, 3794.0, 3795.0, 3799.0])
line_R_ego_jpg_input_tokens_15 = np.array([546.0, 553.0, 553.0, 553.0, 553.0, 553.0, 553.0, 553.0, 553.0, 553.0])
line_R_ego_json_input_tokens_15 = np.array([9917.0, 9924.0, 9924.0, 9924.0, 9924.0, 9924.0, 9924.0, 9924.0, 9924.0, 9924.0])
line_R_ego_tokenized_txt_input_tokens_15 = np.array([3392.0, 3399.0, 3399.0, 3399.0, 3399.0, 3399.0, 3399.0, 3399.0, 3399.0, 3399.0])
occupancy_R_ego_adj_json_input_tokens_15 = np.array([27745.0, 27744.0, 27752.0, 27749.0, 27756.0, 27757.0, 27757.0, 27756.0, 27750.0, 27747.0])
occupancy_R_ego_adj_txt_input_tokens_15 = np.array([7841.0, 7842.0, 7848.0, 7846.0, 7850.0, 7852.0, 7852.0, 7851.0, 7846.0, 7844.0])
occupancy_R_ego_ascii_txt_input_tokens_15 = np.array([657.0, 656.0, 662.0, 649.0, 643.0, 644.0, 651.0, 664.0, 659.0, 655.0])
occupancy_R_ego_jpg_input_tokens_15 = np.array([551.0, 558.0, 558.0, 558.0, 558.0, 558.0, 558.0, 558.0, 558.0, 558.0])
occupancy_R_ego_json_input_tokens_15 = np.array([4356.0, 4363.0, 4363.0, 4363.0, 4363.0, 4363.0, 4363.0, 4363.0, 4363.0, 4363.0])
occupancy_R_ego_tokenized_txt_input_tokens_15 = np.array([12245.0, 12251.0, 12251.0, 12251.0, 12251.0, 12251.0, 12251.0, 12251.0, 12251.0, 12251])

# Output tokens
line_R_ego_adj_json_output_tokens_15 = np.array([23590.0, 12603.0, 22603.0, 10547.0, 23935.0, 17924.0, 18562.0, 17955.0, 29135.0, 7887.0])
line_R_ego_adj_txt_output_tokens_15 = np.array([31340.0, 13936.0, 22702.0, 10531.0, 21926.0, 27592.0, 10754.0, 21051.0, 13892.0, 13337.0])
line_R_ego_jpg_output_tokens_15 = np.array([5694.0, 10838.0, 8056.0, 7726.0, 8044.0, 4165.0, 6490.0, 7053.0, 6032.0, 5382.0])
line_R_ego_json_output_tokens_15 = np.array([22185.0, 22400.0, 10695.0, 12779.0, 26711.0, 22117.0, 22326.0, 18744.0, 19329.0, 26979.0])
line_R_ego_tokenized_txt_output_tokens_15 = np.array([26034.0, 23176.0, 30332.0, 14776.0, 26266.0, 19001.0, 9542.0, 12020.0, 17727.0, 6311.0])
occupancy_R_ego_adj_json_output_tokens_15 = np.array([18870.0, 19262.0, 33481.0, 14313.0, 37418.0, 22595.0, 25233.0, 23782.0, 35780.0, 17694.0])
occupancy_R_ego_adj_txt_output_tokens_15 = np.array([38830.0, 24530.0, 29628.0, 30868.0, 24143.0, 25473.0, 24312.0, 24105.0, 31731.0, 23472.0])
occupancy_R_ego_ascii_txt_output_tokens_15 = np.array([18233.0, 21823.0, 12927.0, 20916.0, 9998.0, 12138.0, 12549.0, 13949.0, 17702.0, 17755.0])
occupancy_R_ego_jpg_output_tokens_15 = np.array([18405.0, 15913.0, 23382.0, 8448.0, 12519.0, 12638.0, 12785.0, 10682.0, 10414.0, 12349.0])
occupancy_R_ego_json_output_tokens_15 = np.array([10282.0, 17161.0, 29684.0, 21330.0, 13550.0, 26301.0, 15134.0, 8967.0, 18473.0, 8937.0])
occupancy_R_ego_tokenized_txt_output_tokens_15 = np.array([31644.0, 23772.0, 23668.0, 29242.0, 27743.0, 21539.0, 9479.0, 29551.0, 26594.0, 18002])


avg_r_ego_line_jpg_input = np.mean(line_R_ego_jpg_input_tokens_15)
avg_r_ego_line_json_input = np.mean(line_R_ego_json_input_tokens_15)
avg_r_ego_occupancy_jpg_input = np.mean(occupancy_R_ego_jpg_input_tokens_15)
avg_r_ego_occupancy_json_input = np.mean(occupancy_R_ego_json_input_tokens_15)
avg_r_ego_line_adj_json_input = np.mean(line_R_ego_adj_json_input_tokens_15)
avg_r_ego_line_adj_txt_input = np.mean(line_R_ego_adj_txt_input_tokens_15)
avg_r_ego_line_tokenized_txt_input = np.mean(line_R_ego_tokenized_txt_input_tokens_15)
avg_r_ego_occupancy_adj_json_input = np.mean(occupancy_R_ego_adj_json_input_tokens_15)
avg_r_ego_occupancy_adj_txt_input = np.mean(occupancy_R_ego_adj_txt_input_tokens_15)
avg_r_ego_occupancy_ascii_txt_input = np.mean(occupancy_R_ego_ascii_txt_input_tokens_15)
avg_r_ego_occupancy_tokenized_txt_input = np.mean(occupancy_R_ego_tokenized_txt_input_tokens_15)
avg_r_ego_line_jpg_output = np.mean(line_R_ego_jpg_output_tokens_15)
avg_r_ego_line_json_output = np.mean(line_R_ego_json_output_tokens_15)
avg_r_ego_occupancy_jpg_output = np.mean(occupancy_R_ego_jpg_output_tokens_15)
avg_r_ego_occupancy_json_output = np.mean(occupancy_R_ego_json_output_tokens_15)
avg_r_ego_line_adj_json_output = np.mean(line_R_ego_adj_json_output_tokens_15)
avg_r_ego_line_adj_txt_output = np.mean(line_R_ego_adj_txt_output_tokens_15)
avg_r_ego_line_tokenized_txt_output = np.mean(line_R_ego_tokenized_txt_output_tokens_15)
avg_r_ego_occupancy_adj_json_output = np.mean(occupancy_R_ego_adj_json_output_tokens_15)
avg_r_ego_occupancy_adj_txt_output = np.mean(occupancy_R_ego_adj_txt_output_tokens_15)
avg_r_ego_occupancy_ascii_txt_output = np.mean(occupancy_R_ego_ascii_txt_output_tokens_15)
avg_r_ego_occupancy_tokenized_txt_output = np.mean(occupancy_R_ego_tokenized_txt_output_tokens_15)



# # Set up runs for table
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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 15x15 Gemini 2.5 Pro, Egocentric Outputn   ** nan = run not yet complete").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_15x15_R_ego.png")





# print("average input NR line jpg 15x15:", np.mean(np.array([avg_nr_coords_line_jpg_input, avg_nr_allo_line_jpg_input, avg_nr_ego_line_jpg_input])))
# print("average input NR line json 15x15:", np.mean(np.array([avg_nr_coords_line_json_input, avg_nr_allo_line_json_input, avg_nr_ego_line_json_input])))
# print("average input NR line adj json 15x15:", np.mean(np.array([avg_nr_coords_line_adj_json_input, avg_nr_allo_line_adj_json_input, avg_nr_ego_line_adj_json_input])))
# print("average input NR line adj txt 15x15:", np.mean(np.array([avg_nr_coords_line_adj_txt_input, avg_nr_allo_line_adj_txt_input, avg_nr_ego_line_adj_txt_input])))
# print("average input NR line tokeninzed 15x15:", np.mean(np.array([avg_nr_coords_line_tokenized_txt_input, avg_nr_allo_line_tokenized_txt_input, avg_nr_ego_line_tokenized_txt_input])))
# print("average input NR occ jpg 15x15:", np.mean(np.array([avg_nr_coords_occupancy_jpg_input, avg_nr_allo_occupancy_jpg_input, avg_nr_ego_occupancy_jpg_input])))
# print("average input NR occ json 15x15:", np.mean(np.array([avg_nr_coords_occupancy_json_input, avg_nr_allo_occupancy_json_input, avg_nr_ego_occupancy_json_input])))
# print("average input NR occ adj json 15x15:", np.mean(np.array([avg_nr_coords_occupancy_adj_json_input, avg_nr_allo_occupancy_adj_json_input, avg_nr_ego_occupancy_adj_json_input])))
# print("average input NR occ adj txt 15x15:", np.mean(np.array([avg_nr_coords_occupancy_adj_txt_input, avg_nr_allo_occupancy_adj_txt_input, avg_nr_ego_occupancy_adj_txt_input])))
# print("average input NR occ ascii txt 15x15:", np.mean(np.array([avg_nr_coords_occupancy_ascii_txt_input, avg_nr_allo_occupancy_ascii_txt_input, avg_nr_ego_occupancy_ascii_txt_input])))
# print("average input NR occ tokenized txt 15x15:", np.mean(np.array([avg_nr_coords_occupancy_tokenized_txt_input, avg_nr_allo_occupancy_tokenized_txt_input, avg_nr_ego_occupancy_tokenized_txt_input])))

# print("average input R line jpg 15x15:", np.mean(np.array([avg_r_coords_line_jpg_input, avg_r_allo_line_jpg_input, avg_r_ego_line_jpg_input])))
# print("average input R line json 15x15:", np.mean(np.array([avg_r_coords_line_json_input, avg_r_allo_line_json_input, avg_r_ego_line_json_input])))
# print("average input R line adj json 15x15:", np.mean(np.array([avg_r_coords_line_adj_json_input, avg_r_allo_line_adj_json_input, avg_r_ego_line_adj_json_input])))
# print("average input R line adj txt 15x15:", np.mean(np.array([avg_r_coords_line_adj_txt_input, avg_r_allo_line_adj_txt_input, avg_r_ego_line_adj_txt_input])))
# print("average input R line tokeninzed 15x15:", np.mean(np.array([avg_r_coords_line_tokenized_txt_input, avg_r_allo_line_tokenized_txt_input, avg_r_ego_line_tokenized_txt_input])))
# print("average input R occ jpg 15x15:", np.mean(np.array([avg_r_coords_occupancy_jpg_input, avg_r_allo_occupancy_jpg_input, avg_r_ego_occupancy_jpg_input])))
# print("average input R occ json 15x15:", np.mean(np.array([avg_r_coords_occupancy_json_input, avg_r_allo_occupancy_json_input, avg_r_ego_occupancy_json_input])))
# print("average input R occ adj json 15x15:", np.mean(np.array([avg_r_coords_occupancy_adj_json_input, avg_r_allo_occupancy_adj_json_input, avg_r_ego_occupancy_adj_json_input])))
# print("average input R occ adj txt 15x15:", np.mean(np.array([avg_r_coords_occupancy_adj_txt_input, avg_r_allo_occupancy_adj_txt_input, avg_r_ego_occupancy_adj_txt_input])))
# print("average input R occ ascii txt 15x15:", np.mean(np.array([avg_r_coords_occupancy_ascii_txt_input, avg_r_allo_occupancy_ascii_txt_input, avg_r_ego_occupancy_ascii_txt_input])))
# print("average input R occ tokenized txt 15x15:", np.mean(np.array([avg_r_coords_occupancy_tokenized_txt_input, avg_r_allo_occupancy_tokenized_txt_input, avg_r_ego_occupancy_tokenized_txt_input])))


# print("average output NR line jpg 15x15:", np.mean(np.array([avg_nr_coords_line_jpg_output, avg_nr_allo_line_jpg_output, avg_nr_ego_line_jpg_output])))
# print("average output NR line json 15x15:", np.mean(np.array([avg_nr_coords_line_json_output, avg_nr_allo_line_json_output, avg_nr_ego_line_json_output])))
# print("average output NR line adj json 15x15:", np.mean(np.array([avg_nr_coords_line_adj_json_output, avg_nr_allo_line_adj_json_output, avg_nr_ego_line_adj_json_output])))
# print("average output NR line adj txt 15x15:", np.mean(np.array([avg_nr_coords_line_adj_txt_output, avg_nr_allo_line_adj_txt_output, avg_nr_ego_line_adj_txt_output])))
# print("average output NR line tokeninzed 15x15:", np.mean(np.array([avg_nr_coords_line_tokenized_txt_output, avg_nr_allo_line_tokenized_txt_output, avg_nr_ego_line_tokenized_txt_output])))
# print("average output NR occ jpg 15x15:", np.mean(np.array([avg_nr_coords_occupancy_jpg_output, avg_nr_allo_occupancy_jpg_output, avg_nr_ego_occupancy_jpg_output])))
# print("average output NR occ json 15x15:", np.mean(np.array([avg_nr_coords_occupancy_json_output, avg_nr_allo_occupancy_json_output, avg_nr_ego_occupancy_json_output])))
# print("average output NR occ adj json 15x15:", np.mean(np.array([avg_nr_coords_occupancy_adj_json_output, avg_nr_allo_occupancy_adj_json_output, avg_nr_ego_occupancy_adj_json_output])))
# print("average output NR occ adj txt 15x15:", np.mean(np.array([avg_nr_coords_occupancy_adj_txt_output, avg_nr_allo_occupancy_adj_txt_output, avg_nr_ego_occupancy_adj_txt_output])))
# print("average output NR occ ascii txt 15x15:", np.mean(np.array([avg_nr_coords_occupancy_ascii_txt_output, avg_nr_allo_occupancy_ascii_txt_output, avg_nr_ego_occupancy_ascii_txt_output])))
# print("average output NR occ tokenized txt 15x15:", np.mean(np.array([avg_nr_coords_occupancy_tokenized_txt_output, avg_nr_allo_occupancy_tokenized_txt_output, avg_nr_ego_occupancy_tokenized_txt_output])))

# print("average output R line jpg 15x15:", np.mean(np.array([avg_r_coords_line_jpg_output, avg_r_allo_line_jpg_output, avg_r_ego_line_jpg_output])))
# print("average output R line json 15x15:", np.mean(np.array([avg_r_coords_line_json_output, avg_r_allo_line_json_output, avg_r_ego_line_json_output])))
# print("average output R line adj json 15x15:", np.mean(np.array([avg_r_coords_line_adj_json_output, avg_r_allo_line_adj_json_output, avg_r_ego_line_adj_json_output])))
# print("average output R line adj txt 15x15:", np.mean(np.array([avg_r_coords_line_adj_txt_output, avg_r_allo_line_adj_txt_output, avg_r_ego_line_adj_txt_output])))
# print("average output R line tokeninzed 15x15:", np.mean(np.array([avg_r_coords_line_tokenized_txt_output, avg_r_allo_line_tokenized_txt_output, avg_r_ego_line_tokenized_txt_output])))
# print("average output R occ jpg 15x15:", np.mean(np.array([avg_r_coords_occupancy_jpg_output, avg_r_allo_occupancy_jpg_output, avg_r_ego_occupancy_jpg_output])))
# print("average output R occ json 15x15:", np.mean(np.array([avg_r_coords_occupancy_json_output, avg_r_allo_occupancy_json_output, avg_r_ego_occupancy_json_output])))
# print("average output R occ adj json 15x15:", np.mean(np.array([avg_r_coords_occupancy_adj_json_output, avg_r_allo_occupancy_adj_json_output, avg_r_ego_occupancy_adj_json_output])))
# print("average output R occ adj txt 15x15:", np.mean(np.array([avg_r_coords_occupancy_adj_txt_output, avg_r_allo_occupancy_adj_txt_output, avg_r_ego_occupancy_adj_txt_output])))
# print("average output R occ ascii txt 15x15:", np.mean(np.array([avg_r_coords_occupancy_ascii_txt_output, avg_r_allo_occupancy_ascii_txt_output, avg_r_ego_occupancy_ascii_txt_output])))
# print("average output R occ tokenized txt 15x15:", np.mean(np.array([avg_r_coords_occupancy_tokenized_txt_output, avg_r_allo_occupancy_tokenized_txt_output, avg_r_ego_occupancy_tokenized_txt_output])))