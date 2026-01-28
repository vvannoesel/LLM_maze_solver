import numpy as np
import pandas as pd
import dataframe_image as dfi
representations = ['line jpg', 'line json', 'line adjacency json', 'line adjacency txt', 'line tokenized txt', 
                   'occupancy jpg', 'occupancy json', 'occupancy adjacency json', 'occupancy adjacency txt', 'occupancy ascii txt', 'occupancy tokenized txt']

"""
List of 110:
line_NR_allo_adj_json_6 run 8
occupancy_R_ego_adj_json_6 run 3
"""

# NR - COORDS - 1-10 ----------------------------------------------------------------
# Accuracy
line_NR_coords_adj_json_6 = np.array([52.94117647058824, 100.0, 40.0, 44.827586206896555, 100.0, 76.19047619047619, 96.0, 81.81818181818183, 58.82352941176471, 76.19047619047619])
line_NR_coords_adj_txt_6 = np.array([52.94117647058824, 42.10526315789473, 14.285714285714285, 24.137931034482758, 100.0, 100.0, 96.0, 100.0, 58.82352941176471, 47.61904761904761])
line_NR_coords_jpg_6 = np.array([11.76470588235294, 10.526315789473683, 2.857142857142857, 3.4482758620689653, 26.666666666666668, 4.761904761904762, 8.0, 9.090909090909092, 11.76470588235294, 4.761904761904762])
line_NR_coords_json_6 = np.array([11.76470588235294, 10.526315789473683, 5.714285714285714, 13.793103448275861, 26.666666666666668, 14.285714285714285, 16.0, 36.36363636363637, 11.76470588235294, 4.761904761904762])
line_NR_coords_tokenized_txt_6 = np.array([35.294117647058826, 5.263157894736842, 2.857142857142857, 3.4482758620689653, 20.0, 4.761904761904762, 4.0, 9.090909090909092, 0.0, 4.761904761904762])
occupancy_NR_coords_adj_json_6 = np.array([100.0, 78.37837837837837, 100.0, 85.96491228070175, 100.0, 100.0, 100.0, 100.0, 75.75757575757575, 46.34146341463415])
occupancy_NR_coords_adj_txt_6 = np.array([51.515151515151516, 100.0, 24.637681159420293, 100.0, 100.0, 41.46341463414634, 42.857142857142854, 100.0, 57.57575757575758, 46.34146341463415])
occupancy_NR_coords_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 29.82456140350877, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 80.95238095238095, 3.0303030303030303, 12.195121951219512])
occupancy_NR_coords_tokenized_txt_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 22.807017543859647, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 52.38095238095239, 15.151515151515152, 12.195121951219512])


# Raw Scores
line_NR_coords_adj_json_raw_score_6 = np.array([9.0, 19.0, 14.0, 13.0, 15.0, 16.0, 24.0, 9.0, 10.0, 16.0])
line_NR_coords_adj_txt_raw_score_6 = np.array([9.0, 8.0, 5.0, 7.0, 15.0, 21.0, 24.0, 11.0, 10.0, 10.0])
line_NR_coords_jpg_raw_score_6 = np.array([2.0, 2.0, 1.0, 1.0, 4.0, 1.0, 2.0, 1.0, 2.0, 1.0])
line_NR_coords_json_raw_score_6 = np.array([2.0, 2.0, 2.0, 4.0, 4.0, 3.0, 4.0, 4.0, 2.0, 1.0])
line_NR_coords_tokenized_txt_raw_score_6 = np.array([6.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 1.0, 0.0, 1.0])
occupancy_NR_coords_adj_json_raw_score_6 = np.array([33.0, 29.0, 69.0, 49.0, 29.0, 41.0, 49.0, 21.0, 25.0, 19.0])
occupancy_NR_coords_adj_txt_raw_score_6 = np.array([17.0, 37.0, 17.0, 57.0, 29.0, 17.0, 21.0, 21.0, 19.0, 19.0])
occupancy_NR_coords_ascii_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_coords_json_raw_score_6 = np.array([1.0, 1.0, 7.0, 17.0, 1.0, 9.0, 1.0, 17.0, 1.0, 5.0])
occupancy_NR_coords_tokenized_txt_raw_score_6 = np.array([1.0, 1.0, 7.0, 13.0, 1.0, 9.0, 1.0, 11.0, 5.0, 5])


# Prompt Tokens
line_NR_coords_adj_json_input_tokens_6 = np.array([2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0])
line_NR_coords_adj_txt_input_tokens_6 = np.array([730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0])
line_NR_coords_jpg_input_tokens_6 = np.array([435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0])
line_NR_coords_json_input_tokens_6 = np.array([1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0])
line_NR_coords_tokenized_txt_input_tokens_6 = np.array([674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0])
occupancy_NR_coords_adj_json_input_tokens_6 = np.array([4350.0, 4351.0, 4349.0, 4347.0, 4350.0, 4349.0, 4346.0, 4343.0, 4346.0, 4343.0])
occupancy_NR_coords_adj_txt_input_tokens_6 = np.array([1280.0, 1281.0, 1279.0, 1278.0, 1280.0, 1279.0, 1277.0, 1275.0, 1277.0, 1275.0])
occupancy_NR_coords_ascii_txt_input_tokens_6 = np.array([253.0, 248.0, 251.0, 250.0, 253.0, 248.0, 255.0, 254.0, 253.0, 247.0])
occupancy_NR_coords_jpg_input_tokens_6 = np.array([432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0, 432.0])
occupancy_NR_coords_json_input_tokens_6 = np.array([989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0])
occupancy_NR_coords_tokenized_txt_input_tokens_6 = np.array([2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163])


# Output Tokens
line_NR_coords_adj_json_output_tokens_6 = np.array([45.0, 77.0, 69.0, 93.0, 61.0, 101.0, 141.0, 45.0, 53.0, 69.0])
line_NR_coords_adj_txt_output_tokens_6 = np.array([45.0, 45.0, 69.0, 61.0, 61.0, 85.0, 149.0, 45.0, 53.0, 650.0])
line_NR_coords_jpg_output_tokens_6 = np.array([41.0, 45.0, 45.0, 45.0, 45.0, 45.0, 53.0, 45.0, 45.0, 45.0])
line_NR_coords_json_output_tokens_6 = np.array([45.0, 45.0, 49.0, 45.0, 45.0, 45.0, 45.0, 53.0, 53.0, 45.0])
line_NR_coords_tokenized_txt_output_tokens_6 = np.array([45.0, 53.0, 45.0, 53.0, 45.0, 53.0, 61.0, 45.0, 89.0, 45.0])
occupancy_NR_coords_adj_json_output_tokens_6 = np.array([150.0, 184.0, 302.0, 236.0, 123.0, 181.0, 214.0, 91.0, 216.0, 267.0])
occupancy_NR_coords_adj_txt_output_tokens_6 = np.array([87.0, 163.0, 115.0, 244.0, 123.0, 115.0, 246.0, 91.0, 107.0, 284.0])
occupancy_NR_coords_ascii_txt_output_tokens_6 = np.array([119.0, 281.0, 157.0, 139.0, 120.0, 165.0, 117.0, 235.0, 182.0, 150.0])
occupancy_NR_coords_jpg_output_tokens_6 = np.array([152.0, 108.0, 192.0, 125.0, 107.0, 151.0, 296.0, 219.0, 283.0, 171.0])
occupancy_NR_coords_json_output_tokens_6 = np.array([99.0, 187.0, 162.0, 154.0, 136.0, 166.0, 172.0, 139.0, 149.0, 147.0])
occupancy_NR_coords_tokenized_txt_output_tokens_6 = np.array([269.0, 244.0, 171.0, 650.0, 229.0, 284.0, 232.0, 179.0, 269.0, 196])

avg_nr_coords_line_jpg_input = np.mean(line_NR_coords_jpg_input_tokens_6)
avg_nr_coords_line_json_input = np.mean(line_NR_coords_json_input_tokens_6)
avg_nr_coords_occupancy_jpg_input = np.mean(occupancy_NR_coords_jpg_input_tokens_6)
avg_nr_coords_occupancy_json_input = np.mean(occupancy_NR_coords_json_input_tokens_6)
avg_nr_coords_line_adj_json_input = np.mean(line_NR_coords_adj_json_input_tokens_6)
avg_nr_coords_line_adj_txt_input = np.mean(line_NR_coords_adj_txt_input_tokens_6)
avg_nr_coords_line_tokenized_txt_input = np.mean(line_NR_coords_tokenized_txt_input_tokens_6)
avg_nr_coords_occupancy_adj_json_input = np.mean(occupancy_NR_coords_adj_json_input_tokens_6)
avg_nr_coords_occupancy_adj_txt_input = np.mean(occupancy_NR_coords_adj_txt_input_tokens_6)
avg_nr_coords_occupancy_ascii_txt_input = np.mean(occupancy_NR_coords_ascii_txt_input_tokens_6)
avg_nr_coords_occupancy_tokenized_txt_input = np.mean(occupancy_NR_coords_tokenized_txt_input_tokens_6)
avg_nr_coords_line_jpg_output = np.mean(line_NR_coords_jpg_output_tokens_6)
avg_nr_coords_line_json_output = np.mean(line_NR_coords_json_output_tokens_6)
avg_nr_coords_occupancy_jpg_output = np.mean(occupancy_NR_coords_jpg_output_tokens_6)
avg_nr_coords_occupancy_json_output = np.mean(occupancy_NR_coords_json_output_tokens_6)
avg_nr_coords_line_adj_json_output = np.mean(line_NR_coords_adj_json_output_tokens_6)
avg_nr_coords_line_adj_txt_output = np.mean(line_NR_coords_adj_txt_output_tokens_6)
avg_nr_coords_line_tokenized_txt_output = np.mean(line_NR_coords_tokenized_txt_output_tokens_6)
avg_nr_coords_occupancy_adj_json_output = np.mean(occupancy_NR_coords_adj_json_output_tokens_6)
avg_nr_coords_occupancy_adj_txt_output = np.mean(occupancy_NR_coords_adj_txt_output_tokens_6)
avg_nr_coords_occupancy_ascii_txt_output = np.mean(occupancy_NR_coords_ascii_txt_output_tokens_6)
avg_nr_coords_occupancy_tokenized_txt_output = np.mean(occupancy_NR_coords_tokenized_txt_output_tokens_6)

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 6x6, Gemini 2.5 Flash Lite, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_NR_6x6_coords.png")


# NR - ALLO - 1-10 ----------------------------------------------------------------
# Accuracy
line_NR_allo_adj_json_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 0.0, 20.0, 8.333333333333332, 100.0, 12.5, 15.0])
line_NR_allo_adj_txt_6 = np.array([25.0, 0.0, 11.76470588235294, 17.857142857142858, 21.428571428571427, 5.0, 0.0, 60.0, 0.0, 5.0])
line_NR_allo_jpg_6 = np.array([6.25, 0.0, 2.941176470588235, 0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 10.0])
line_NR_allo_json_6 = np.array([12.5, 5.555555555555555, 0.0, 17.857142857142858, 21.428571428571427, 0.0, 12.5, 0.0, 18.75, 0.0])
line_NR_allo_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 3.571428571428571, 21.428571428571427, 5.0, 0.0, 10.0, 0.0, 10.0])
occupancy_NR_allo_adj_json_6 = np.array([18.75, 5.555555555555555, 7.352941176470589, 17.857142857142858, 14.285714285714285, 5.0, 8.333333333333332, 50.0, 6.25, 5.0])
occupancy_NR_allo_adj_txt_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 14.285714285714285, 17.5, 8.333333333333332, 90.0, 18.75, 0.0])
occupancy_NR_allo_ascii_txt_6 = np.array([6.25, 11.11111111111111, 0.0, 21.428571428571427, 0.0, np.nan, 2.083333333333333, 55.00000000000001, 0.0, 7.5])
occupancy_NR_allo_jpg_6 = np.array([0.0, 0.0, 1.4705882352941175, 10.714285714285714, 3.571428571428571, 2.5, 4.166666666666666, 5.0, 3.125, 0.0])
occupancy_NR_allo_json_6 = np.array([0.0, 0.0, 5.88235294117647, 14.285714285714285, 0.0, 10.0, 0.0, 80.0, 0.0, 10.0])
occupancy_NR_allo_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 14.285714285714285, np.nan, 0.0, 0.0, 40.0, 0.0, 2.5])


# Raw Scores
line_NR_allo_adj_json_raw_score_6 = np.array([3.0, 1.0, 3.0, 5.0, 0.0, 4.0, 2.0, 10.0, 2.0, 3.0])
line_NR_allo_adj_txt_raw_score_6 = np.array([4.0, 0.0, 4.0, 5.0, 3.0, 1.0, 0.0, 6.0, 0.0, 1.0])
line_NR_allo_jpg_raw_score_6 = np.array([1.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0])
line_NR_allo_json_raw_score_6 = np.array([2.0, 1.0, 0.0, 5.0, 3.0, 0.0, 3.0, 0.0, 3.0, 0.0])
line_NR_allo_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 1.0, 3.0, 1.0, 0.0, 1.0, 0.0, 2.0])
occupancy_NR_allo_adj_json_raw_score_6 = np.array([6.0, 2.0, 5.0, 10.0, 4.0, 2.0, 4.0, 10.0, 2.0, 2.0])
occupancy_NR_allo_adj_txt_raw_score_6 = np.array([6.0, 2.0, 6.0, 10.0, 4.0, 7.0, 4.0, 18.0, 6.0, 0.0])
occupancy_NR_allo_ascii_txt_raw_score_6 = np.array([2.0, 4.0, 0.0, 12.0, 0.0, 0.0, 1.0, 11.0, 0.0, 3.0])
occupancy_NR_allo_jpg_raw_score_6 = np.array([0.0, 0.0, 1.0, 6.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.0])
occupancy_NR_allo_json_raw_score_6 = np.array([0.0, 0.0, 4.0, 8.0, 0.0, 4.0, 0.0, 16.0, 0.0, 4.0])
occupancy_NR_allo_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 8.0, 0.0, 1])


# Prompt Tokens
line_NR_allo_adj_json_input_tokens_6 = np.array([2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0])
line_NR_allo_adj_txt_input_tokens_6 = np.array([722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0])
line_NR_allo_jpg_input_tokens_6 = np.array([427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0])
line_NR_allo_json_input_tokens_6 = np.array([1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0])
line_NR_allo_tokenized_txt_input_tokens_6 = np.array([666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0])
occupancy_NR_allo_adj_json_input_tokens_6 = np.array([4342.0, 4343.0, 4341.0, 4339.0, 4342.0, 4341.0, 4338.0, 4335.0, 4338.0, 4335.0])
occupancy_NR_allo_adj_txt_input_tokens_6 = np.array([1272.0, 1273.0, 1271.0, 1270.0, 1272.0, 1271.0, 1269.0, 1267.0, 1269.0, 1267.0])
occupancy_NR_allo_ascii_txt_input_tokens_6 = np.array([245.0, 240.0, 243.0, 242.0, 245.0, 240.0, 247.0, 246.0, 245.0, 239.0])
occupancy_NR_allo_jpg_input_tokens_6 = np.array([424.0, 424.0, 424.0, 424.0, 424.0, 424.0, 424.0, 424.0, 424.0, 424.0])
occupancy_NR_allo_json_input_tokens_6 = np.array([981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0])
occupancy_NR_allo_tokenized_txt_input_tokens_6 = np.array([2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155])


# Output Tokens
line_NR_allo_adj_json_output_tokens_6 = np.array([19.0, 19.0, 23.0, 29.0, 29.0, 21.0, 19.0, 27.0, 31.0, 19.0])
line_NR_allo_adj_txt_output_tokens_6 = np.array([25.0, 19.0, 21.0, 29.0, 23.0, 23.0, 27.0, 27.0, 29.0, 23.0])
line_NR_allo_jpg_output_tokens_6 = np.array([31.0, 23.0, 21.0, 23.0, 31.0, 25.0, 45.0, 15.0, 27.0, 51.0])
line_NR_allo_json_output_tokens_6 = np.array([21.0, 49.0, 19.0, 29.0, 23.0, 23.0, 21.0, 21.0, 21.0, 21.0])
line_NR_allo_tokenized_txt_output_tokens_6 = np.array([43.0, 29.0, 117.0, 21.0, 650.0, 59.0, 27.0, 33.0, 650.0, 57.0])
occupancy_NR_allo_adj_json_output_tokens_6 = np.array([65.0, 53.0, 51.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_adj_txt_output_tokens_6 = np.array([650.0, 650.0, 189.0, 650.0, 53.0, 650.0, 650.0, 47.0, 650.0, 43.0])
occupancy_NR_allo_ascii_txt_output_tokens_6 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 0.0, 137.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_jpg_output_tokens_6 = np.array([61.0, 41.0, 65.0, 650.0, 650.0, 31.0, 41.0, 650.0, 41.0, 37.0])
occupancy_NR_allo_json_output_tokens_6 = np.array([650.0, 650.0, 650.0, 51.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_allo_tokenized_txt_output_tokens_6 = np.array([650.0, 650.0, 85.0, 650.0, 0.0, 650.0, 650.0, 650.0, 650.0, 650])

avg_nr_allo_line_jpg_input = np.mean(line_NR_allo_jpg_input_tokens_6)
avg_nr_allo_line_json_input = np.mean(line_NR_allo_json_input_tokens_6)
avg_nr_allo_occupancy_jpg_input = np.mean(occupancy_NR_allo_jpg_input_tokens_6)
avg_nr_allo_occupancy_json_input = np.mean(occupancy_NR_allo_json_input_tokens_6)
avg_nr_allo_line_adj_json_input = np.mean(line_NR_allo_adj_json_input_tokens_6)
avg_nr_allo_line_adj_txt_input = np.mean(line_NR_allo_adj_txt_input_tokens_6)
avg_nr_allo_line_tokenized_txt_input = np.mean(line_NR_allo_tokenized_txt_input_tokens_6)
avg_nr_allo_occupancy_adj_json_input = np.mean(occupancy_NR_allo_adj_json_input_tokens_6)
avg_nr_allo_occupancy_adj_txt_input = np.mean(occupancy_NR_allo_adj_txt_input_tokens_6)
avg_nr_allo_occupancy_ascii_txt_input = np.mean(occupancy_NR_allo_ascii_txt_input_tokens_6)
avg_nr_allo_occupancy_tokenized_txt_input = np.mean(occupancy_NR_allo_tokenized_txt_input_tokens_6)
avg_nr_allo_line_jpg_output = np.mean(line_NR_allo_jpg_output_tokens_6)
avg_nr_allo_line_json_output = np.mean(line_NR_allo_json_output_tokens_6)
avg_nr_allo_occupancy_jpg_output = np.mean(occupancy_NR_allo_jpg_output_tokens_6)
avg_nr_allo_occupancy_json_output = np.mean(occupancy_NR_allo_json_output_tokens_6)
avg_nr_allo_line_adj_json_output = np.mean(line_NR_allo_adj_json_output_tokens_6)
avg_nr_allo_line_adj_txt_output = np.mean(line_NR_allo_adj_txt_output_tokens_6)
avg_nr_allo_line_tokenized_txt_output = np.mean(line_NR_allo_tokenized_txt_output_tokens_6)
avg_nr_allo_occupancy_adj_json_output = np.mean(occupancy_NR_allo_adj_json_output_tokens_6)
avg_nr_allo_occupancy_adj_txt_output = np.mean(occupancy_NR_allo_adj_txt_output_tokens_6)
avg_nr_allo_occupancy_ascii_txt_output = np.mean(occupancy_NR_allo_ascii_txt_output_tokens_6)
avg_nr_allo_occupancy_tokenized_txt_output = np.mean(occupancy_NR_allo_tokenized_txt_output_tokens_6)

# # Set up complexities for table
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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 6x6, Gemini 2.5 Flash Lite, Allocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_NR_6x6_allo.png")


# NR - EGO - 1-10 ----------------------------------------------------------------
# Accuracy
line_NR_ego_adj_json_6 = np.array([18.75, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_6 = np.array([12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 0.0, 0.0, 4.166666666666666, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.25, 0.0])
occupancy_NR_ego_adj_json_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_txt_6 = np.array([0.0, 2.7777777777777777, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_6 = np.array([3.125, 2.7777777777777777, 0.0, 0.0, 3.571428571428571, 0.0, 2.083333333333333, 0.0, 0.0, 0.0])
occupancy_NR_ego_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 3.571428571428571, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# Raw Scores
line_NR_ego_adj_json_raw_score_6 = np.array([3.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_adj_txt_raw_score_6 = np.array([2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_NR_ego_json_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
line_NR_ego_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])
occupancy_NR_ego_adj_json_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_adj_txt_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_ascii_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_jpg_raw_score_6 = np.array([1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_json_raw_score_6 = np.array([0.0, 2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_NR_ego_tokenized_txt_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0])


# Prompt Tokens
line_NR_ego_adj_json_input_tokens_6 = np.array([2375.0, 2375.0, 2375.0, 2375.0, 2375.0, 2375.0, 2375.0, 2375.0, 2375.0, 2375.0])
line_NR_ego_adj_txt_input_tokens_6 = np.array([846.0, 846.0, 846.0, 846.0, 846.0, 846.0, 846.0, 846.0, 846.0, 846.0])
line_NR_ego_jpg_input_tokens_6 = np.array([551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0])
line_NR_ego_json_input_tokens_6 = np.array([1926.0, 1926.0, 1926.0, 1926.0, 1926.0, 1926.0, 1926.0, 1926.0, 1926.0, 1926.0])
line_NR_ego_tokenized_txt_input_tokens_6 = np.array([790.0, 790.0, 790.0, 790.0, 790.0, 790.0, 790.0, 790.0, 790.0, 790.0])
occupancy_NR_ego_adj_json_input_tokens_6 = np.array([4466.0, 4467.0, 4465.0, 4463.0, 4466.0, 4465.0, 4462.0, 4459.0, 4462.0, 4459.0])
occupancy_NR_ego_adj_txt_input_tokens_6 = np.array([1396.0, 1397.0, 1395.0, 1394.0, 1396.0, 1395.0, 1393.0, 1391.0, 1393.0, 1391.0])
occupancy_NR_ego_ascii_txt_input_tokens_6 = np.array([369.0, 364.0, 367.0, 366.0, 369.0, 364.0, 371.0, 370.0, 369.0, 363.0])
occupancy_NR_ego_jpg_input_tokens_6 = np.array([548.0, 548.0, 548.0, 548.0, 548.0, 548.0, 548.0, 548.0, 548.0, 548.0])
occupancy_NR_ego_json_input_tokens_6 = np.array([1105.0, 1105.0, 1105.0, 1105.0, 1105.0, 1105.0, 1105.0, 1105.0, 1105.0, 1105.0])
occupancy_NR_ego_tokenized_txt_input_tokens_6 = np.array([2279.0, 2279.0, 2279.0, 2279.0, 2279.0, 2279.0, 2279.0, 2279.0, 2279.0, 2279])


# Output Tokens
line_NR_ego_adj_json_output_tokens_6 = np.array([57.0, 43.0, 47.0, 59.0, 43.0, 650.0, 111.0, 111.0, 59.0, 97.0])
line_NR_ego_adj_txt_output_tokens_6 = np.array([43.0, 650.0, 650.0, 105.0, 39.0, 53.0, 35.0, 81.0, 650.0, 650.0])
line_NR_ego_jpg_output_tokens_6 = np.array([51.0, 42.0, 80.0, 57.0, 650.0, 37.0, 411.0, 74.0, 31.0, 33.0])
line_NR_ego_json_output_tokens_6 = np.array([83.0, 51.0, 51.0, 47.0, 650.0, 49.0, 49.0, 35.0, 129.0, 47.0])
line_NR_ego_tokenized_txt_output_tokens_6 = np.array([296.0, 650.0, 650.0, 650.0, 650.0, 41.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_json_output_tokens_6 = np.array([650.0, 221.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_adj_txt_output_tokens_6 = np.array([650.0, 650.0, 650.0, 417.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_ascii_txt_output_tokens_6 = np.array([650.0, 211.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_jpg_output_tokens_6 = np.array([71.0, 650.0, 93.0, 650.0, 650.0, 650.0, 79.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_json_output_tokens_6 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0])
occupancy_NR_ego_tokenized_txt_output_tokens_6 = np.array([650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650.0, 650])

avg_nr_ego_line_jpg_input = np.mean(line_NR_ego_jpg_input_tokens_6)
avg_nr_ego_line_json_input = np.mean(line_NR_ego_json_input_tokens_6)
avg_nr_ego_occupancy_jpg_input = np.mean(occupancy_NR_ego_jpg_input_tokens_6)
avg_nr_ego_occupancy_json_input = np.mean(occupancy_NR_ego_json_input_tokens_6)
avg_nr_ego_line_adj_json_input = np.mean(line_NR_ego_adj_json_input_tokens_6)
avg_nr_ego_line_adj_txt_input = np.mean(line_NR_ego_adj_txt_input_tokens_6)
avg_nr_ego_line_tokenized_txt_input = np.mean(line_NR_ego_tokenized_txt_input_tokens_6)
avg_nr_ego_occupancy_adj_json_input = np.mean(occupancy_NR_ego_adj_json_input_tokens_6)
avg_nr_ego_occupancy_adj_txt_input = np.mean(occupancy_NR_ego_adj_txt_input_tokens_6)
avg_nr_ego_occupancy_ascii_txt_input = np.mean(occupancy_NR_ego_ascii_txt_input_tokens_6)
avg_nr_ego_occupancy_tokenized_txt_input = np.mean(occupancy_NR_ego_tokenized_txt_input_tokens_6)
avg_nr_ego_line_jpg_output = np.mean(line_NR_ego_jpg_output_tokens_6)
avg_nr_ego_line_json_output = np.mean(line_NR_ego_json_output_tokens_6)
avg_nr_ego_occupancy_jpg_output = np.mean(occupancy_NR_ego_jpg_output_tokens_6)
avg_nr_ego_occupancy_json_output = np.mean(occupancy_NR_ego_json_output_tokens_6)
avg_nr_ego_line_adj_json_output = np.mean(line_NR_ego_adj_json_output_tokens_6)
avg_nr_ego_line_adj_txt_output = np.mean(line_NR_ego_adj_txt_output_tokens_6)
avg_nr_ego_line_tokenized_txt_output = np.mean(line_NR_ego_tokenized_txt_output_tokens_6)
avg_nr_ego_occupancy_adj_json_output = np.mean(occupancy_NR_ego_adj_json_output_tokens_6)
avg_nr_ego_occupancy_adj_txt_output = np.mean(occupancy_NR_ego_adj_txt_output_tokens_6)
avg_nr_ego_occupancy_ascii_txt_output = np.mean(occupancy_NR_ego_ascii_txt_output_tokens_6)
avg_nr_ego_occupancy_tokenized_txt_output = np.mean(occupancy_NR_ego_tokenized_txt_output_tokens_6)

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 6x6, Gemini 2.5 Flash Lite, Egocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_NR_6x6_ego.png")

# R - COORDS - 1-10 ----------------------------------------------------------------
# Accuracy
line_R_coords_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_ascii_txt_6 = np.array([24.242424242424242, 32.432432432432435, 11.594202898550725, 1.7543859649122806, 31.03448275862069, 2.4390243902439024, 2.0408163265306123, 0.0, 27.27272727272727, 2.4390243902439024])
occupancy_R_coords_jpg_6 = np.array([0.0, 2.7027027027027026, 0.0, 0.0, 0.0, 2.4390243902439024, 0.0, 0.0, 0.0, 0.0])
occupancy_R_coords_json_6 = np.array([27.27272727272727, 48.64864864864865, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 60.60606060606061, 100.0])
occupancy_R_coords_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_R_coords_adj_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
line_R_coords_adj_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
line_R_coords_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
line_R_coords_tokenized_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
occupancy_R_coords_adj_json_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0])
occupancy_R_coords_adj_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0])
occupancy_R_coords_ascii_txt_raw_score_6 = np.array([8.0, 12.0, 8.0, 1.0, 9.0, 1.0, 1.0, 0.0, 9.0, 1.0])
occupancy_R_coords_jpg_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0])
occupancy_R_coords_json_raw_score_6 = np.array([9.0, 18.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 20.0, 41.0])
occupancy_R_coords_tokenized_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41])


# Prompt Tokens
line_R_coords_adj_json_input_tokens_6 = np.array([2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0])
line_R_coords_adj_txt_input_tokens_6 = np.array([730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0])
line_R_coords_jpg_input_tokens_6 = np.array([435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0])
line_R_coords_json_input_tokens_6 = np.array([1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0])
line_R_coords_tokenized_txt_input_tokens_6 = np.array([674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0])
occupancy_R_coords_adj_json_input_tokens_6 = np.array([4350.0, 4351.0, 4349.0, 4347.0, 4350.0, 4349.0, 4346.0, 4343.0, 4346.0, 4343.0])
occupancy_R_coords_adj_txt_input_tokens_6 = np.array([1280.0, 1281.0, 1279.0, 1278.0, 1280.0, 1279.0, 1277.0, 1275.0, 1277.0, 1275.0])
occupancy_R_coords_ascii_txt_input_tokens_6 = np.array([252.0, 247.0, 250.0, 249.0, 252.0, 247.0, 254.0, 253.0, 252.0, 246.0])
occupancy_R_coords_jpg_input_tokens_6 = np.array([442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0])
occupancy_R_coords_json_input_tokens_6 = np.array([989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0])
occupancy_R_coords_tokenized_txt_input_tokens_6 = np.array([2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163])


# Output Tokens
line_R_coords_adj_json_output_tokens_6 = np.array([8118.0, 7536.0, 8051.0, 10359.0, 7050.0, 7165.0, 8363.0, 5188.0, 8328.0, 8680.0])
line_R_coords_adj_txt_output_tokens_6 = np.array([9010.0, 6917.0, 8107.0, 12580.0, 8466.0, 11368.0, 8631.0, 6225.0, 7009.0, 6776.0])
line_R_coords_jpg_output_tokens_6 = np.array([2481.0, 1957.0, 3621.0, 2795.0, 3635.0, 2330.0, 1944.0, 2540.0, 2893.0, 1487.0])
line_R_coords_json_output_tokens_6 = np.array([7887.0, 10892.0, 12599.0, 11490.0, 4499.0, 12090.0, 8009.0, 5811.0, 7880.0, 7781.0])
line_R_coords_tokenized_txt_output_tokens_6 = np.array([7478.0, 5124.0, 7192.0, 6404.0, 7403.0, 5634.0, 6509.0, 4192.0, 5771.0, 8980.0])
occupancy_R_coords_adj_json_output_tokens_6 = np.array([15384.0, 9125.0, 16476.0, 7410.0, 8446.0, 6965.0, 8409.0, 6349.0, 7760.0, 6097.0])
occupancy_R_coords_adj_txt_output_tokens_6 = np.array([13139.0, 9709.0, 8620.0, 19753.0, 9188.0, 5554.0, 10526.0, 9994.0, 7690.0, 10978.0])
occupancy_R_coords_ascii_txt_output_tokens_6 = np.array([9580.0, 13563.0, 18661.0, 6554.0, 5994.0, 18625.0, 11382.0, 2098.0, 16252.0, 3579.0])
occupancy_R_coords_jpg_output_tokens_6 = np.array([3205.0, 12404.0, 4649.0, 23554.0, 2155.0, 5385.0, 10584.0, 9918.0, 3286.0, 2238.0])
occupancy_R_coords_json_output_tokens_6 = np.array([7036.0, 9541.0, 11979.0, 12481.0, 17432.0, 6230.0, 7207.0, 4910.0, 8837.0, 7369.0])
occupancy_R_coords_tokenized_txt_output_tokens_6 = np.array([6473.0, 6508.0, 16281.0, 8357.0, 4132.0, 5736.0, 7801.0, 6271.0, 6880.0, 7046])


# Final answer only output tokens
line_R_coords_jpg_final_answer_6 = np.array([45, 77, 37, 37, 45, 53, 41, 61, 69, 37])
line_R_coords_json_final_answer_6 = np.array([69, 77, 141, 117, 61, 85, 101, 45, 69, 85])
line_R_coords_adj_json_final_answer_6 = np.array([69, 77, 141, 117, 61, 85, 101, 45, 69, 85])
line_R_coords_adj_txt_final_answer_6 = np.array([69, 77, 141, 117, 61, 85, 101, 45, 69, 85])
line_R_coords_tokenized_txt_final_answer_6 = np.array([69, 77, 141, 117, 61, 85, 101, 45, 69, 85])
occupancy_R_coords_jpg_final_answer_6 = np.array([160, 184, 175, 137, 125, 91, 120, 93, 246, 180])
occupancy_R_coords_json_final_answer_6 = np.array([145, 155, 302, 244, 123, 181, 214, 91, 140, 178])
occupancy_R_coords_adj_json_final_answer_6 = np.array([150, 163, 302, 244, 123, 181, 214, 91, 144, 178])
occupancy_R_coords_adj_txt_final_answer_6 = np.array([150, 163, 302, 244, 123, 181, 214, 91, 144, 178])
occupancy_R_coords_tokenized_txt_final_answer_6 = np.array([150, 163, 302, 244, 123, 181, 214, 91, 144, 178])
occupancy_R_coords_ascii_txt_final_answer_6 = np.array([107, 91, 161, 107, 147, 109, 117, 130, 107, 86])


avg_r_coords_line_jpg_input = np.mean(line_R_coords_jpg_input_tokens_6)
avg_r_coords_line_json_input = np.mean(line_R_coords_json_input_tokens_6)
avg_r_coords_occupancy_jpg_input = np.mean(occupancy_R_coords_jpg_input_tokens_6)
avg_r_coords_occupancy_json_input = np.mean(occupancy_R_coords_json_input_tokens_6)
avg_r_coords_line_adj_json_input = np.mean(line_R_coords_adj_json_input_tokens_6)
avg_r_coords_line_adj_txt_input = np.mean(line_R_coords_adj_txt_input_tokens_6)
avg_r_coords_line_tokenized_txt_input = np.mean(line_R_coords_tokenized_txt_input_tokens_6)
avg_r_coords_occupancy_adj_json_input = np.mean(occupancy_R_coords_adj_json_input_tokens_6)
avg_r_coords_occupancy_adj_txt_input = np.mean(occupancy_R_coords_adj_txt_input_tokens_6)
avg_r_coords_occupancy_ascii_txt_input = np.mean(occupancy_R_coords_ascii_txt_input_tokens_6)
avg_r_coords_occupancy_tokenized_txt_input = np.mean(occupancy_R_coords_tokenized_txt_input_tokens_6)
avg_r_coords_line_jpg_output = np.mean(line_R_coords_jpg_output_tokens_6)
avg_r_coords_line_json_output = np.mean(line_R_coords_json_output_tokens_6)
avg_r_coords_occupancy_jpg_output = np.mean(occupancy_R_coords_jpg_output_tokens_6)
avg_r_coords_occupancy_json_output = np.mean(occupancy_R_coords_json_output_tokens_6)
avg_r_coords_line_adj_json_output = np.mean(line_R_coords_adj_json_output_tokens_6)
avg_r_coords_line_adj_txt_output = np.mean(line_R_coords_adj_txt_output_tokens_6)
avg_r_coords_line_tokenized_txt_output = np.mean(line_R_coords_tokenized_txt_output_tokens_6)
avg_r_coords_occupancy_adj_json_output = np.mean(occupancy_R_coords_adj_json_output_tokens_6)
avg_r_coords_occupancy_adj_txt_output = np.mean(occupancy_R_coords_adj_txt_output_tokens_6)
avg_r_coords_occupancy_ascii_txt_output = np.mean(occupancy_R_coords_ascii_txt_output_tokens_6)
avg_r_coords_occupancy_tokenized_txt_output = np.mean(occupancy_R_coords_tokenized_txt_output_tokens_6)

# # # Set up complexities for table
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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 6x6, Gemini 2.5 Pro, Coordinates Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_R_6x6_coords.png")


# R - ALLO - 1-10 ----------------------------------------------------------------
# Accuracy
line_R_allo_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_jpg_6 = np.array([6.25, 5.555555555555555, 0.0, 0.0, 28.57142857142857, 15.0, 4.166666666666666, 0.0, 18.75, 0.0])
line_R_allo_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_ascii_txt_6 = np.array([6.25, 0.0, 0.0, 25.0, 14.285714285714285, 55.00000000000001, 12.5, 35.0, 25.0, 10.0])
occupancy_R_allo_jpg_6 = np.array([18.75, 5.555555555555555, 4.411764705882353, 14.285714285714285, 7.142857142857142, 5.0, 4.166666666666666, 0.0, 9.375, 5.0])
occupancy_R_allo_json_6 = np.array([56.25, 100.0, 100.0, 7.142857142857142, 100.0, 100.0, 100.0, 100.0, 100.0, 37.5])
occupancy_R_allo_tokenized_txt_6 = np.array([100.0, 100.0, 51.470588235294116, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])


# Raw Scores
line_R_allo_adj_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_R_allo_adj_txt_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_R_allo_jpg_raw_score_6 = np.array([1.0, 1.0, 0.0, 0.0, 4.0, 3.0, 1.0, 0.0, 3.0, 0.0])
line_R_allo_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_R_allo_tokenized_txt_raw_score_6 = np.array([16.0, 18.0, 13.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
occupancy_R_allo_adj_json_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
occupancy_R_allo_adj_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
occupancy_R_allo_ascii_txt_raw_score_6 = np.array([2.0, 0.0, 0.0, 14.0, 4.0, 22.0, 6.0, 7.0, 8.0, 4.0])
occupancy_R_allo_jpg_raw_score_6 = np.array([6.0, 2.0, 3.0, 8.0, 2.0, 2.0, 2.0, 0.0, 3.0, 2.0])
occupancy_R_allo_json_raw_score_6 = np.array([18.0, 36.0, 68.0, 4.0, 28.0, 40.0, 48.0, 20.0, 32.0, 15.0])
occupancy_R_allo_tokenized_txt_raw_score_6 = np.array([32.0, 36.0, 35.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40])


# Prompt Tokens
line_R_allo_adj_json_input_tokens_6 = np.array([2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0])
line_R_allo_adj_txt_input_tokens_6 = np.array([722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0])
line_R_allo_jpg_input_tokens_6 = np.array([427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0])
line_R_allo_json_input_tokens_6 = np.array([1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0])
line_R_allo_tokenized_txt_input_tokens_6 = np.array([666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0])
occupancy_R_allo_adj_json_input_tokens_6 = np.array([4342.0, 4343.0, 4341.0, 4339.0, 4342.0, 4341.0, 4338.0, 4335.0, 4338.0, 4335.0])
occupancy_R_allo_adj_txt_input_tokens_6 = np.array([1272.0, 1273.0, 1271.0, 1270.0, 1272.0, 1271.0, 1269.0, 1267.0, 1269.0, 1267.0])
occupancy_R_allo_ascii_txt_input_tokens_6 = np.array([244.0, 239.0, 242.0, 241.0, 244.0, 239.0, 246.0, 245.0, 244.0, 238.0])
occupancy_R_allo_jpg_input_tokens_6 = np.array([434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0])
occupancy_R_allo_json_input_tokens_6 = np.array([981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0])
occupancy_R_allo_tokenized_txt_input_tokens_6 = np.array([2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155])


# Output Tokens
line_R_allo_adj_json_output_tokens_6 = np.array([10641.0, 14090.0, 10868.0, 8676.0, 9407.0, 8748.0, 9268.0, 6268.0, 7776.0, 10410.0])
line_R_allo_adj_txt_output_tokens_6 = np.array([9343.0, 10961.0, 14119.0, 7126.0, 8186.0, 8730.0, 16201.0, 7605.0, 9852.0, 9724.0])
line_R_allo_jpg_output_tokens_6 = np.array([1839.0, 2913.0, 1991.0, 1423.0, 1177.0, 1452.0, 9757.0, 1935.0, 2147.0, 1590.0])
line_R_allo_json_output_tokens_6 = np.array([5597.0, 11044.0, 9192.0, 9277.0, 3700.0, 9559.0, 7836.0, 7537.0, 7277.0, 6526.0])
line_R_allo_tokenized_txt_output_tokens_6 = np.array([5793.0, 5608.0, 7936.0, 6865.0, 5683.0, 5279.0, 4705.0, 5013.0, 8851.0, 4439.0])
occupancy_R_allo_adj_json_output_tokens_6 = np.array([7474.0, 9524.0, 6529.0, 11801.0, 11052.0, 6205.0, 7602.0, 5525.0, 12079.0, 5873.0])
occupancy_R_allo_adj_txt_output_tokens_6 = np.array([13306.0, 13157.0, 13986.0, 16671.0, 11294.0, 8513.0, 7497.0, 11042.0, 9924.0, 11305.0])
occupancy_R_allo_ascii_txt_output_tokens_6 = np.array([4481.0, 3359.0, 20039.0, 22024.0, 18930.0, 15800.0, 14766.0, 14579.0, 12277.0, 22136.0])
occupancy_R_allo_jpg_output_tokens_6 = np.array([5419.0, 2450.0, 1883.0, 2165.0, 2629.0, 2649.0, 1955.0, 2538.0, 1897.0, 2900.0])
occupancy_R_allo_json_output_tokens_6 = np.array([12925.0, 8580.0, 17443.0, 27933.0, 8077.0, 14011.0, 12393.0, 4414.0, 10960.0, 15358.0])
occupancy_R_allo_tokenized_txt_output_tokens_6 = np.array([6708.0, 6990.0, 7499.0, 11540.0, 3074.0, 4217.0, 14502.0, 6598.0, 6265.0, 8402])

# Final answer only output tokens
line_R_allo_jpg_final_answer_6 = np.array([15, 15, 19, 23, 19, 19, 19, 19, 23, 23])
line_R_allo_json_final_answer_6 = np.array([31, 35, 67, 55, 27, 39, 47, 19, 31, 39])
line_R_allo_adj_json_final_answer_6 = np.array([31, 35, 67, 55, 27, 39, 47, 19, 31, 39])
line_R_allo_adj_txt_final_answer_6 = np.array([31, 35, 67, 55, 27, 39, 47, 19, 31, 39])
line_R_allo_tokenized_txt_final_answer_6 = np.array([31, 35, 31, 55, 27, 39, 47, 19, 31, 39])
occupancy_R_allo_jpg_final_answer_6 = np.array([111, 37, 67, 91, 83, 91, 55, 35, 59, 87])
occupancy_R_allo_json_final_answer_6 = np.array([79, 71, 135, 87, 55, 79, 95, 39, 63, 79])
occupancy_R_allo_adj_json_final_answer_6 = np.array([63, 71, 135, 111, 55, 79, 95, 39, 63, 79])
occupancy_R_allo_adj_txt_final_answer_6 = np.array([63, 71, 135, 111, 55, 79, 95, 39, 63, 79])
occupancy_R_allo_tokenized_txt_final_answer_6 = np.array([63, 71, 133, 111, 55, 79, 95, 39, 63, 79])
occupancy_R_allo_ascii_txt_final_answer_6 = np.array([39, 63, 39, 47, 39, 67, 47, 93, 47, 71])


avg_r_allo_line_jpg_input = np.mean(line_R_allo_jpg_input_tokens_6)
avg_r_allo_line_json_input = np.mean(line_R_allo_json_input_tokens_6)
avg_r_allo_occupancy_jpg_input = np.mean(occupancy_R_allo_jpg_input_tokens_6)
avg_r_allo_occupancy_json_input = np.mean(occupancy_R_allo_json_input_tokens_6)
avg_r_allo_line_adj_json_input = np.mean(line_R_allo_adj_json_input_tokens_6)
avg_r_allo_line_adj_txt_input = np.mean(line_R_allo_adj_txt_input_tokens_6)
avg_r_allo_line_tokenized_txt_input = np.mean(line_R_allo_tokenized_txt_input_tokens_6)
avg_r_allo_occupancy_adj_json_input = np.mean(occupancy_R_allo_adj_json_input_tokens_6)
avg_r_allo_occupancy_adj_txt_input = np.mean(occupancy_R_allo_adj_txt_input_tokens_6)
avg_r_allo_occupancy_ascii_txt_input = np.mean(occupancy_R_allo_ascii_txt_input_tokens_6)
avg_r_allo_occupancy_tokenized_txt_input = np.mean(occupancy_R_allo_tokenized_txt_input_tokens_6)
avg_r_allo_line_jpg_output = np.mean(line_R_allo_jpg_output_tokens_6)
avg_r_allo_line_json_output = np.mean(line_R_allo_json_output_tokens_6)
avg_r_allo_occupancy_jpg_output = np.mean(occupancy_R_allo_jpg_output_tokens_6)
avg_r_allo_occupancy_json_output = np.mean(occupancy_R_allo_json_output_tokens_6)
avg_r_allo_line_adj_json_output = np.mean(line_R_allo_adj_json_output_tokens_6)
avg_r_allo_line_adj_txt_output = np.mean(line_R_allo_adj_txt_output_tokens_6)
avg_r_allo_line_tokenized_txt_output = np.mean(line_R_allo_tokenized_txt_output_tokens_6)
avg_r_allo_occupancy_adj_json_output = np.mean(occupancy_R_allo_adj_json_output_tokens_6)
avg_r_allo_occupancy_adj_txt_output = np.mean(occupancy_R_allo_adj_txt_output_tokens_6)
avg_r_allo_occupancy_ascii_txt_output = np.mean(occupancy_R_allo_ascii_txt_output_tokens_6)
avg_r_allo_occupancy_tokenized_txt_output = np.mean(occupancy_R_allo_tokenized_txt_output_tokens_6)

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 6x6, Gemini 2.5 Pro, Allocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_R_6x6_allo.png")


# R - EGO - 1-10 ----------------------------------------------------------------
# # Accuracy
line_R_ego_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_adj_txt_6 = np.array([100.0, 5.555555555555555, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_ego_jpg_6 = np.array([12.5, 11.11111111111111, 0.0, 0.0, 21.428571428571427, 0.0, 4.166666666666666, 0.0, 31.25, 0.0])
line_R_ego_json_6 = np.array([100.0, 16.666666666666664, 100.0, 100.0, 100.0, 100.0, 83.33333333333334, 100.0, 6.25, 100.0])
line_R_ego_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 100.0, 100.0])
occupancy_R_ego_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_ego_ascii_txt_6 = np.array([12.5, 33.33333333333333, 0.0, 17.857142857142858, 28.57142857142857, 5.0, 10.416666666666668, 35.0, 0.0, 10.0])
occupancy_R_ego_jpg_6 = np.array([6.25, 16.666666666666664, 5.88235294117647, 0.0, 21.428571428571427, 2.5, 12.5, 50.0, 12.5, 0.0])
occupancy_R_ego_json_6 = np.array([100.0, 100.0, 8.823529411764707, 17.857142857142858, 100.0, 90.0, 100.0, 100.0, 56.25, 10.0])
occupancy_R_ego_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 29.166666666666668, 100.0, 100.0, 100.0])


# Raw Scores
line_R_ego_adj_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_R_ego_adj_txt_raw_score_6 = np.array([16.0, 1.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
line_R_ego_jpg_raw_score_6 = np.array([2.0, 2.0, 0.0, 0.0, 3.0, 0.0, 1.0, 0.0, 5.0, 0.0])
line_R_ego_json_raw_score_6 = np.array([16.0, 3.0, 34.0, 28.0, 14.0, 20.0, 20.0, 10.0, 1.0, 20.0])
line_R_ego_tokenized_txt_raw_score_6 = np.array([16.0, 18.0, 13.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0])
occupancy_R_ego_adj_json_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 0.0, 32.0, 40.0])
occupancy_R_ego_adj_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0])
occupancy_R_ego_ascii_txt_raw_score_6 = np.array([4.0, 12.0, 0.0, 10.0, 8.0, 2.0, 5.0, 7.0, 0.0, 4.0])
occupancy_R_ego_jpg_raw_score_6 = np.array([2.0, 6.0, 4.0, 0.0, 6.0, 1.0, 6.0, 10.0, 4.0, 0.0])
occupancy_R_ego_json_raw_score_6 = np.array([32.0, 36.0, 6.0, 10.0, 28.0, 36.0, 48.0, 20.0, 18.0, 4.0])
occupancy_R_ego_tokenized_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 14.0, 20.0, 32.0, 40])


# Prompt Tokens
line_R_ego_adj_json_input_tokens_6 = np.array([2368.0, 2368.0, 2368.0, 2368.0, 2368.0, 2368.0, 2368.0, 2368.0, 2368.0, 2368.0])
line_R_ego_adj_txt_input_tokens_6 = np.array([839.0, 839.0, 839.0, 839.0, 839.0, 839.0, 839.0, 839.0, 839.0, 839.0])
line_R_ego_jpg_input_tokens_6 = np.array([544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0, 544.0])
line_R_ego_json_input_tokens_6 = np.array([1919.0, 1919.0, 1919.0, 1919.0, 1919.0, 1919.0, 1919.0, 1919.0, 1919.0, 1919.0])
line_R_ego_tokenized_txt_input_tokens_6 = np.array([783.0, 783.0, 783.0, 783.0, 783.0, 783.0, 783.0, 783.0, 783.0, 783.0])
occupancy_R_ego_adj_json_input_tokens_6 = np.array([4459.0, 4460.0, 4458.0, 4456.0, 4459.0, 4458.0, 4455.0, 4452.0, 4455.0, 4452.0])
occupancy_R_ego_adj_txt_input_tokens_6 = np.array([1389.0, 1390.0, 1388.0, 1387.0, 1389.0, 1388.0, 1386.0, 1384.0, 1386.0, 1384.0])
occupancy_R_ego_ascii_txt_input_tokens_6 = np.array([361.0, 356.0, 359.0, 358.0, 361.0, 356.0, 363.0, 362.0, 361.0, 355.0])
occupancy_R_ego_jpg_input_tokens_6 = np.array([551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0, 551.0])
occupancy_R_ego_json_input_tokens_6 = np.array([1098.0, 1098.0, 1098.0, 1098.0, 1098.0, 1098.0, 1098.0, 1098.0, 1098.0, 1098.0])
occupancy_R_ego_tokenized_txt_input_tokens_6 = np.array([2272.0, 2272.0, 2272.0, 2272.0, 2272.0, 2272.0, 2272.0, 2272.0, 2272.0, 2272])


# Output Tokens
line_R_ego_adj_json_output_tokens_6 = np.array([6390.0, 10668.0, 12437.0, 12920.0, 6567.0, 8281.0, 10218.0, 5101.0, 10020.0, 7362.0])
line_R_ego_adj_txt_output_tokens_6 = np.array([6467.0, 6319.0, 6035.0, 9648.0, 7523.0, 10133.0, 12011.0, 5569.0, 8592.0, 7937.0])
line_R_ego_jpg_output_tokens_6 = np.array([2398.0, 3132.0, 3318.0, 3813.0, 2187.0, 1674.0, 2857.0, 1577.0, 2172.0, 2070.0])
line_R_ego_json_output_tokens_6 = np.array([3994.0, 5758.0, 13995.0, 9986.0, 8931.0, 12105.0, 8791.0, 3930.0, 15025.0, 15241.0])
line_R_ego_tokenized_txt_output_tokens_6 = np.array([8429.0, 6664.0, 10667.0, 9767.0, 5029.0, 10211.0, 13849.0, 5052.0, 6737.0, 12532.0])
occupancy_R_ego_adj_json_output_tokens_6 = np.array([11970.0, 13702.0, 17330.0, 19841.0, 12415.0, 8618.0, 10500.0, 9725.0, 10587.0, 8333.0])
occupancy_R_ego_adj_txt_output_tokens_6 = np.array([9861.0, 19222.0, 14460.0, 23064.0, 15292.0, 17620.0, 9997.0, 6948.0, 17158.0, 11736.0])
occupancy_R_ego_ascii_txt_output_tokens_6 = np.array([22762.0, 9003.0, 2806.0, 16200.0, 17916.0, 7652.0, 16613.0, 8111.0, 6627.0, 7386.0])
occupancy_R_ego_jpg_output_tokens_6 = np.array([5468.0, 3335.0, 6321.0, 7905.0, 8185.0, 7207.0, 5149.0, 5087.0, 10110.0, 5163.0])
occupancy_R_ego_json_output_tokens_6 = np.array([12945.0, 10590.0, 14452.0, 26708.0, 10656.0, 7456.0, 8722.0, 8159.0, 22047.0, 12086.0])
occupancy_R_ego_tokenized_txt_output_tokens_6 = np.array([8801.0, 9813.0, 12147.0, 7806.0, 8871.0, 14289.0, 4835.0, 4969.0, 8420.0, 7251])


# Final answer only output tokens
line_R_ego_jpg_final_answer_6 = np.array([19, 19, 23, 15, 19, 15, 19, 19, 15, 15])
line_R_ego_json_final_answer_6 = np.array([31, 23, 67, 55, 27, 39, 51, 19, 31, 39])
line_R_ego_adj_json_final_answer_6 = np.array([31, 35, 67, 55, 27, 39, 47, 19, 31, 39])
line_R_ego_adj_txt_final_answer_6 = np.array([31, 19, 67, 55, 27, 39, 47, 19, 31, 39])
line_R_ego_tokenized_txt_final_answer_6 = np.array([31, 35, 31, 55, 27, 39, 47, 19, 31, 39])
occupancy_R_ego_jpg_final_answer_6 = np.array([59, 55, 95, 75, 39, 63, 63, 83, 69, 51])
occupancy_R_ego_json_final_answer_6 = np.array([63, 71, 65, 39, 55, 79, 95, 39, 47, 77])
occupancy_R_ego_adj_json_final_answer_6 = np.array([63, 71, 139, 111, 55, 79, 95, 37, 63, 79])
occupancy_R_ego_adj_txt_final_answer_6 = np.array([63, 71, 135, 111, 55, 79, 95, 39, 63, 79])
occupancy_R_ego_tokenized_txt_final_answer_6 = np.array([63, 71, 135, 111, 55, 79, 99, 39, 63, 79])
occupancy_R_ego_ascii_txt_final_answer_6 = np.array([107, 63, 51, 39, 67, 35, 55, 65, 55, 37])


avg_r_ego_line_jpg_input = np.mean(line_R_ego_jpg_input_tokens_6)
avg_r_ego_line_json_input = np.mean(line_R_ego_json_input_tokens_6)
avg_r_ego_occupancy_jpg_input = np.mean(occupancy_R_ego_jpg_input_tokens_6)
avg_r_ego_occupancy_json_input = np.mean(occupancy_R_ego_json_input_tokens_6)
avg_r_ego_line_adj_json_input = np.mean(line_R_ego_adj_json_input_tokens_6)
avg_r_ego_line_adj_txt_input = np.mean(line_R_ego_adj_txt_input_tokens_6)
avg_r_ego_line_tokenized_txt_input = np.mean(line_R_ego_tokenized_txt_input_tokens_6)
avg_r_ego_occupancy_adj_json_input = np.mean(occupancy_R_ego_adj_json_input_tokens_6)
avg_r_ego_occupancy_adj_txt_input = np.mean(occupancy_R_ego_adj_txt_input_tokens_6)
avg_r_ego_occupancy_ascii_txt_input = np.mean(occupancy_R_ego_ascii_txt_input_tokens_6)
avg_r_ego_occupancy_tokenized_txt_input = np.mean(occupancy_R_ego_tokenized_txt_input_tokens_6)
avg_r_ego_line_jpg_output = np.mean(line_R_ego_jpg_output_tokens_6)
avg_r_ego_line_json_output = np.mean(line_R_ego_json_output_tokens_6)
avg_r_ego_occupancy_jpg_output = np.mean(occupancy_R_ego_jpg_output_tokens_6)
avg_r_ego_occupancy_json_output = np.mean(occupancy_R_ego_json_output_tokens_6)
avg_r_ego_line_adj_json_output = np.mean(line_R_ego_adj_json_output_tokens_6)
avg_r_ego_line_adj_txt_output = np.mean(line_R_ego_adj_txt_output_tokens_6)
avg_r_ego_line_tokenized_txt_output = np.mean(line_R_ego_tokenized_txt_output_tokens_6)
avg_r_ego_occupancy_adj_json_output = np.mean(occupancy_R_ego_adj_json_output_tokens_6)
avg_r_ego_occupancy_adj_txt_output = np.mean(occupancy_R_ego_adj_txt_output_tokens_6)
avg_r_ego_occupancy_ascii_txt_output = np.mean(occupancy_R_ego_ascii_txt_output_tokens_6)
avg_r_ego_occupancy_tokenized_txt_output = np.mean(occupancy_R_ego_tokenized_txt_output_tokens_6)

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
# table_img = table.style.set_caption("Accuracy (%) of All Representations at 6x6, Gemini 2.5 Pro, Egocentric Output").format(precision=3)
# dfi.export(table_img, "table_accuracy_Dataset03_R_6x6_ego.png")



# print("average input NR line jpg 6x6:", np.mean(np.array([avg_nr_coords_line_jpg_input, avg_nr_allo_line_jpg_input, avg_nr_ego_line_jpg_input])))
# print("average input NR line json 6x6:", np.mean(np.array([avg_nr_coords_line_json_input, avg_nr_allo_line_json_input, avg_nr_ego_line_json_input])))
# print("average input NR line adj json 6x6:", np.mean(np.array([avg_nr_coords_line_adj_json_input, avg_nr_allo_line_adj_json_input, avg_nr_ego_line_adj_json_input])))
# print("average input NR line adj txt 6x6:", np.mean(np.array([avg_nr_coords_line_adj_txt_input, avg_nr_allo_line_adj_txt_input, avg_nr_ego_line_adj_txt_input])))
# print("average input NR line tokeninzed 6x6:", np.mean(np.array([avg_nr_coords_line_tokenized_txt_input, avg_nr_allo_line_tokenized_txt_input, avg_nr_ego_line_tokenized_txt_input])))
# print("average input NR occ jpg 6x6:", np.mean(np.array([avg_nr_coords_occupancy_jpg_input, avg_nr_allo_occupancy_jpg_input, avg_nr_ego_occupancy_jpg_input])))
# print("average input NR occ json 6x6:", np.mean(np.array([avg_nr_coords_occupancy_json_input, avg_nr_allo_occupancy_json_input, avg_nr_ego_occupancy_json_input])))
# print("average input NR occ adj json 6x6:", np.mean(np.array([avg_nr_coords_occupancy_adj_json_input, avg_nr_allo_occupancy_adj_json_input, avg_nr_ego_occupancy_adj_json_input])))
# print("average input NR occ adj txt 6x6:", np.mean(np.array([avg_nr_coords_occupancy_adj_txt_input, avg_nr_allo_occupancy_adj_txt_input, avg_nr_ego_occupancy_adj_txt_input])))
# print("average input NR occ ascii txt 6x6:", np.mean(np.array([avg_nr_coords_occupancy_ascii_txt_input, avg_nr_allo_occupancy_ascii_txt_input, avg_nr_ego_occupancy_ascii_txt_input])))
# print("average input NR occ tokenized txt 6x6:", np.mean(np.array([avg_nr_coords_occupancy_tokenized_txt_input, avg_nr_allo_occupancy_tokenized_txt_input, avg_nr_ego_occupancy_tokenized_txt_input])))

# print("average input R line jpg 6x6:", np.mean(np.array([avg_r_coords_line_jpg_input, avg_r_allo_line_jpg_input, avg_r_ego_line_jpg_input])))
# print("average input R line json 6x6:", np.mean(np.array([avg_r_coords_line_json_input, avg_r_allo_line_json_input, avg_r_ego_line_json_input])))
# print("average input R line adj json 6x6:", np.mean(np.array([avg_r_coords_line_adj_json_input, avg_r_allo_line_adj_json_input, avg_r_ego_line_adj_json_input])))
# print("average input R line adj txt 6x6:", np.mean(np.array([avg_r_coords_line_adj_txt_input, avg_r_allo_line_adj_txt_input, avg_r_ego_line_adj_txt_input])))
# print("average input R line tokeninzed 6x6:", np.mean(np.array([avg_r_coords_line_tokenized_txt_input, avg_r_allo_line_tokenized_txt_input, avg_r_ego_line_tokenized_txt_input])))
# print("average input R occ jpg 6x6:", np.mean(np.array([avg_r_coords_occupancy_jpg_input, avg_r_allo_occupancy_jpg_input, avg_r_ego_occupancy_jpg_input])))
# print("average input R occ json 6x6:", np.mean(np.array([avg_r_coords_occupancy_json_input, avg_r_allo_occupancy_json_input, avg_r_ego_occupancy_json_input])))
# print("average input R occ adj json 6x6:", np.mean(np.array([avg_r_coords_occupancy_adj_json_input, avg_r_allo_occupancy_adj_json_input, avg_r_ego_occupancy_adj_json_input])))
# print("average input R occ adj txt 6x6:", np.mean(np.array([avg_r_coords_occupancy_adj_txt_input, avg_r_allo_occupancy_adj_txt_input, avg_r_ego_occupancy_adj_txt_input])))
# print("average input R occ ascii txt 6x6:", np.mean(np.array([avg_r_coords_occupancy_ascii_txt_input, avg_r_allo_occupancy_ascii_txt_input, avg_r_ego_occupancy_ascii_txt_input])))
# print("average input R occ tokenized txt 6x6:", np.mean(np.array([avg_r_coords_occupancy_tokenized_txt_input, avg_r_allo_occupancy_tokenized_txt_input, avg_r_ego_occupancy_tokenized_txt_input])))


# print("average output NR line jpg 6x6:", np.mean(np.array([avg_nr_coords_line_jpg_output, avg_nr_allo_line_jpg_output, avg_nr_ego_line_jpg_output])))
# print("average output NR line json 6x6:", np.mean(np.array([avg_nr_coords_line_json_output, avg_nr_allo_line_json_output, avg_nr_ego_line_json_output])))
# print("average output NR line adj json 6x6:", np.mean(np.array([avg_nr_coords_line_adj_json_output, avg_nr_allo_line_adj_json_output, avg_nr_ego_line_adj_json_output])))
# print("average output NR line adj txt 6x6:", np.mean(np.array([avg_nr_coords_line_adj_txt_output, avg_nr_allo_line_adj_txt_output, avg_nr_ego_line_adj_txt_output])))
# print("average output NR line tokeninzed 6x6:", np.mean(np.array([avg_nr_coords_line_tokenized_txt_output, avg_nr_allo_line_tokenized_txt_output, avg_nr_ego_line_tokenized_txt_output])))
# print("average output NR occ jpg 6x6:", np.mean(np.array([avg_nr_coords_occupancy_jpg_output, avg_nr_allo_occupancy_jpg_output, avg_nr_ego_occupancy_jpg_output])))
# print("average output NR occ json 6x6:", np.mean(np.array([avg_nr_coords_occupancy_json_output, avg_nr_allo_occupancy_json_output, avg_nr_ego_occupancy_json_output])))
# print("average output NR occ adj json 6x6:", np.mean(np.array([avg_nr_coords_occupancy_adj_json_output, avg_nr_allo_occupancy_adj_json_output, avg_nr_ego_occupancy_adj_json_output])))
# print("average output NR occ adj txt 6x6:", np.mean(np.array([avg_nr_coords_occupancy_adj_txt_output, avg_nr_allo_occupancy_adj_txt_output, avg_nr_ego_occupancy_adj_txt_output])))
# print("average output NR occ ascii txt 6x6:", np.mean(np.array([avg_nr_coords_occupancy_ascii_txt_output, avg_nr_allo_occupancy_ascii_txt_output, avg_nr_ego_occupancy_ascii_txt_output])))
# print("average output NR occ tokenized txt 6x6:", np.mean(np.array([avg_nr_coords_occupancy_tokenized_txt_output, avg_nr_allo_occupancy_tokenized_txt_output, avg_nr_ego_occupancy_tokenized_txt_output])))

# print("average output R line jpg 6x6:", np.mean(np.array([avg_r_coords_line_jpg_output, avg_r_allo_line_jpg_output, avg_r_ego_line_jpg_output])))
# print("average output R line json 6x6:", np.mean(np.array([avg_r_coords_line_json_output, avg_r_allo_line_json_output, avg_r_ego_line_json_output])))
# print("average output R line adj json 6x6:", np.mean(np.array([avg_r_coords_line_adj_json_output, avg_r_allo_line_adj_json_output, avg_r_ego_line_adj_json_output])))
# print("average output R line adj txt 6x6:", np.mean(np.array([avg_r_coords_line_adj_txt_output, avg_r_allo_line_adj_txt_output, avg_r_ego_line_adj_txt_output])))
# print("average output R line tokeninzed 6x6:", np.mean(np.array([avg_r_coords_line_tokenized_txt_output, avg_r_allo_line_tokenized_txt_output, avg_r_ego_line_tokenized_txt_output])))
# print("average output R occ jpg 6x6:", np.mean(np.array([avg_r_coords_occupancy_jpg_output, avg_r_allo_occupancy_jpg_output, avg_r_ego_occupancy_jpg_output])))
# print("average output R occ json 6x6:", np.mean(np.array([avg_r_coords_occupancy_json_output, avg_r_allo_occupancy_json_output, avg_r_ego_occupancy_json_output])))
# print("average output R occ adj json 6x6:", np.mean(np.array([avg_r_coords_occupancy_adj_json_output, avg_r_allo_occupancy_adj_json_output, avg_r_ego_occupancy_adj_json_output])))
# print("average output R occ adj txt 6x6:", np.mean(np.array([avg_r_coords_occupancy_adj_txt_output, avg_r_allo_occupancy_adj_txt_output, avg_r_ego_occupancy_adj_txt_output])))
# print("average output R occ ascii txt 6x6:", np.mean(np.array([avg_r_coords_occupancy_ascii_txt_output, avg_r_allo_occupancy_ascii_txt_output, avg_r_ego_occupancy_ascii_txt_output])))
# print("average output R occ tokenized txt 6x6:", np.mean(np.array([avg_r_coords_occupancy_tokenized_txt_output, avg_r_allo_occupancy_tokenized_txt_output, avg_r_ego_occupancy_tokenized_txt_output])))