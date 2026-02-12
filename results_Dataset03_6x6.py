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
line_R_coords_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 51.61290322580645, 100.0, 100.0, 88.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_coords_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_coords_ascii_txt_6 = np.array([24.242424242424242, 32.432432432432435, 11.594202898550725, 1.7543859649122806, 31.03448275862069, 2.4390243902439024, 2.0408163265306123, 0.0, 27.27272727272727, 2.4390243902439024, 3.4482758620689653, 3.4482758620689653, 20.0, 44.0, 11.475409836065573, 28.57142857142857, 39.39393939393939, 24.489795918367346, 44.0, 8.108108108108109, 38.775510204081634, 15.555555555555555, 85.36585365853658, 2.0408163265306123, 0.0, 36.36363636363637, 2.2222222222222223, 36.0, 0.0, 40.0])
occupancy_R_coords_jpg_6 = np.array([0.0, 2.7027027027027026, 0.0, 0.0, 0.0, 2.4390243902439024, 0.0, 0.0, 0.0, 0.0, 0.0, 13.793103448275861, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.7027027027027026, 0.0, 4.444444444444445, 0.0, 0.0, 0.0, 0.0, 2.2222222222222223, 0.0, 2.0408163265306123, 0.0])
occupancy_R_coords_json_6 = np.array([27.27272727272727, 48.64864864864865, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 60.60606060606061, 100.0, 100.0, 100.0, 100.0, 100.0, 52.459016393442624, 100.0, 27.27272727272727, 34.69387755102041, 100.0, 18.91891891891892, 48.97959183673469, 33.33333333333333, 100.0, 100.0, 100.0, 51.515151515151516, 100.0, 100.0, 36.734693877551024, 100.0])
occupancy_R_coords_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])

# Raw Scores
line_R_coords_adj_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0, 15.0, 15.0, 13.0, 13.0, 31.0, 25.0, 17.0, 25.0, 13.0, 19.0, 25.0, 23.0, 21.0, 25.0, 25.0, 17.0, 23.0, 13.0, 25.0, 13.0])
line_R_coords_adj_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0, 15.0, 15.0, 13.0, 13.0, 31.0, 25.0, 17.0, 25.0, 13.0, 19.0, 25.0, 23.0, 21.0, 25.0, 25.0, 17.0, 23.0, 13.0, 25.0, 13.0])
line_R_coords_jpg_raw_score_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_R_coords_json_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0, 15.0, 15.0, 13.0, 13.0, 16.0, 25.0, 17.0, 22.0, 13.0, 19.0, 25.0, 23.0, 21.0, 25.0, 25.0, 17.0, 23.0, 13.0, 25.0, 13.0])
line_R_coords_tokenized_txt_raw_score_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0, 15.0, 15.0, 13.0, 13.0, 31.0, 25.0, 17.0, 25.0, 13.0, 19.0, 25.0, 23.0, 21.0, 25.0, 25.0, 17.0, 23.0, 13.0, 25.0, 13.0])
occupancy_R_coords_adj_json_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0, 29.0, 29.0, 25.0, 25.0, 61.0, 49.0, 33.0, 49.0, 25.0, 37.0, 49.0, 45.0, 41.0, 49.0, 49.0, 33.0, 45.0, 25.0, 49.0, 25.0])
occupancy_R_coords_adj_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0, 29.0, 29.0, 25.0, 25.0, 61.0, 49.0, 33.0, 49.0, 25.0, 37.0, 49.0, 45.0, 41.0, 49.0, 49.0, 33.0, 45.0, 25.0, 49.0, 25.0])
occupancy_R_coords_ascii_txt_raw_score_6 = np.array([8.0, 12.0, 8.0, 1.0, 9.0, 1.0, 1.0, 0.0, 9.0, 1.0, 1.0, 1.0, 5.0, 11.0, 7.0, 14.0, 13.0, 12.0, 11.0, 3.0, 19.0, 7.0, 35.0, 1.0, 0.0, 12.0, 1.0, 9.0, 0.0, 10.0])
occupancy_R_coords_jpg_raw_score_6 = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0])
occupancy_R_coords_json_raw_score_6 = np.array([9.0, 18.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 20.0, 41.0, 29.0, 29.0, 25.0, 25.0, 32.0, 49.0, 9.0, 17.0, 25.0, 7.0, 24.0, 15.0, 41.0, 49.0, 49.0, 17.0, 45.0, 25.0, 18.0, 25.0])
occupancy_R_coords_tokenized_txt_raw_score_6 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0, 29.0, 29.0, 25.0, 25.0, 61.0, 49.0, 33.0, 49.0, 25.0, 37.0, 49.0, 45.0, 41.0, 49.0, 49.0, 33.0, 45.0, 25.0, 49.0, 25])


# Prompt Tokens
line_R_coords_adj_json_input_tokens_6 = np.array([2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2259.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0, 2266.0])
line_R_coords_adj_txt_input_tokens_6 = np.array([730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 730.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0, 737.0])
line_R_coords_jpg_input_tokens_6 = np.array([435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 435.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0])
line_R_coords_json_input_tokens_6 = np.array([1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1810.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0, 1817.0])
line_R_coords_tokenized_txt_input_tokens_6 = np.array([674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 674.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0, 681.0])
occupancy_R_coords_adj_json_input_tokens_6 = np.array([4350.0, 4351.0, 4349.0, 4347.0, 4350.0, 4349.0, 4346.0, 4343.0, 4346.0, 4343.0, 4354.0, 4350.0, 4357.0, 4354.0, 4353.0, 4353.0, 4353.0, 4353.0, 4354.0, 4350.0, 4353.0, 4355.0, 4353.0, 4353.0, 4347.0, 4350.0, 4348.0, 4348.0, 4345.0, 4348.0])
occupancy_R_coords_adj_txt_input_tokens_6 = np.array([1280.0, 1281.0, 1279.0, 1278.0, 1280.0, 1279.0, 1277.0, 1275.0, 1277.0, 1275.0, 1285.0, 1282.0, 1287.0, 1285.0, 1284.0, 1284.0, 1284.0, 1284.0, 1285.0, 1282.0, 1284.0, 1286.0, 1284.0, 1284.0, 1284.0, 1286.0, 1285.0, 1285.0, 1283.0, 1285.0])
occupancy_R_coords_ascii_txt_input_tokens_6 = np.array([252.0, 247.0, 250.0, 249.0, 252.0, 247.0, 254.0, 253.0, 252.0, 246.0, 248.0, 256.0, 261.0, 254.0, 253.0, 260.0, 260.0, 263.0, 255.0, 258.0, 247.0, 258.0, 254.0, 256.0, 255.0, 254.0, 253.0, 256.0, 256.0, 248.0])
occupancy_R_coords_jpg_input_tokens_6 = np.array([442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 442.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0, 449.0])
occupancy_R_coords_json_input_tokens_6 = np.array([989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 989.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0, 996.0])
occupancy_R_coords_tokenized_txt_input_tokens_6 = np.array([2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2163.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170.0, 2170])


# Output Tokens
line_R_coords_adj_json_output_tokens_6 = np.array([8118.0, 7536.0, 8051.0, 10359.0, 7050.0, 7165.0, 8363.0, 5188.0, 8328.0, 8680.0, 2276.0, 5154.0, 2342.0, 6343.0, 7020.0, 4690.0, 5840.0, 4863.0, 2570.0, 7286.0, 5043.0, 3497.0, 3073.0, 4915.0, 3228.0, 5187.0, 4608.0, 3844.0, 6619.0, 3064.0])
line_R_coords_adj_txt_output_tokens_6 = np.array([9010.0, 6917.0, 8107.0, 12580.0, 8466.0, 11368.0, 8631.0, 6225.0, 7009.0, 6776.0, 3747.0, 3584.0, 5602.0, 2607.0, 4865.0, 4125.0, 2558.0, 3672.0, 4235.0, 4344.0, 5830.0, 5692.0, 4777.0, 4631.0, 3721.0, 2676.0, 4496.0, 5834.0, 10082.0, 3472.0])
line_R_coords_jpg_output_tokens_6 = np.array([2481.0, 1957.0, 3621.0, 2795.0, 3635.0, 2330.0, 1944.0, 2540.0, 2893.0, 1487.0, 3632.0, 1522.0, 1730.0, 2856.0, 2902.0, 4132.0, 1538.0, 1929.0, 1326.0, 5885.0, 2200.0, 1585.0, 2894.0, 1993.0, 1900.0, 1455.0, 2913.0, 3349.0, 2266.0, 1285.0])
line_R_coords_json_output_tokens_6 = np.array([7887.0, 10892.0, 12599.0, 11490.0, 4499.0, 12090.0, 8009.0, 5811.0, 7880.0, 7781.0, 4548.0, 3876.0, 2568.0, 3004.0, 9214.0, 10322.0, 6585.0, 8938.0, 5753.0, 8021.0, 6424.0, 4008.0, 2528.0, 4690.0, 7596.0, 2939.0, 3833.0, 4876.0, 11173.0, 2551.0])
line_R_coords_tokenized_txt_output_tokens_6 = np.array([7478.0, 5124.0, 7192.0, 6404.0, 7403.0, 5634.0, 6509.0, 4192.0, 5771.0, 8980.0, 5957.0, 6950.0, 3527.0, 5896.0, 5821.0, 5648.0, 4392.0, 5763.0, 3210.0, 5994.0, 4489.0, 4792.0, 5059.0, 6378.0, 4836.0, 6388.0, 7494.0, 5657.0, 7723.0, 3835.0])
occupancy_R_coords_adj_json_output_tokens_6 = np.array([15384.0, 9125.0, 16476.0, 7410.0, 8446.0, 6965.0, 8409.0, 6349.0, 7760.0, 6097.0, 3771.0, 4100.0, 5436.0, 6551.0, 7705.0, 5621.0, 5019.0, 6989.0, 6687.0, 11441.0, 5160.0, 5848.0, 5350.0, 6735.0, 4710.0, 5557.0, 5589.0, 4130.0, 8382.0, 4637.0])
occupancy_R_coords_adj_txt_output_tokens_6 = np.array([13139.0, 9709.0, 8620.0, 19753.0, 9188.0, 5554.0, 10526.0, 9994.0, 7690.0, 10978.0, 6407.0, 4570.0, 6626.0, 8040.0, 5491.0, 3747.0, 5549.0, 10590.0, 5621.0, 9426.0, 5907.0, 5776.0, 4026.0, 12699.0, 6279.0, 4653.0, 5172.0, 5149.0, 9654.0, 5049.0])
occupancy_R_coords_ascii_txt_output_tokens_6 = np.array([9580.0, 13563.0, 18661.0, 6554.0, 5994.0, 18625.0, 11382.0, 2098.0, 16252.0, 3579.0, 4888.0, 12545.0, 12205.0, 13628.0, 29387.0, 7492.0, 5979.0, 26559.0, 7886.0, 16546.0, 8780.0, 17195.0, 17945.0, 10237.0, 2972.0, 16838.0, 5063.0, 26549.0, 14715.0, 19511.0])
occupancy_R_coords_jpg_output_tokens_6 = np.array([3205.0, 12404.0, 4649.0, 23554.0, 2155.0, 5385.0, 10584.0, 9918.0, 3286.0, 2238.0, 2549.0, 10381.0, 3164.0, 1943.0, 2609.0, 2344.0, 3887.0, 2854.0, 7625.0, 4615.0, 3874.0, 3272.0, 2180.0, 2822.0, 3246.0, 3548.0, 4131.0, 5763.0, 5434.0, 2655.0])
occupancy_R_coords_json_output_tokens_6 = np.array([7036.0, 9541.0, 11979.0, 12481.0, 17432.0, 6230.0, 7207.0, 4910.0, 8837.0, 7369.0, 3733.0, 5022.0, 8208.0, 6107.0, 10382.0, 11918.0, 2298.0, 23841.0, 7890.0, 4702.0, 4970.0, 14533.0, 7485.0, 8450.0, 7318.0, 4227.0, 8085.0, 5603.0, 7655.0, 6100.0])
occupancy_R_coords_tokenized_txt_output_tokens_6 = np.array([6473.0, 6508.0, 16281.0, 8357.0, 4132.0, 5736.0, 7801.0, 6271.0, 6880.0, 7046.0, 8134.0, 3959.0, 5354.0, 2619.0, 13442.0, 5138.0, 4754.0, 5057.0, 4228.0, 3715.0, 5126.0, 6228.0, 4450.0, 2577.0, 9896.0, 3400.0, 3957.0, 4411.0, 7719.0, 5125])


# Final answer only output tokens
line_R_coords_jpg_final_answer_6 = np.array([45.0, 77.0, 37.0, 37.0, 45.0, 53.0, 41.0, 61.0, 69.0, 37.0])
line_R_coords_json_final_answer_6 = np.array([69.0, 77.0, 141.0, 117.0, 61.0, 85.0, 101.0, 45.0, 69.0, 85.0])
line_R_coords_adj_json_final_answer_6 = np.array([69.0, 77.0, 141.0, 117.0, 61.0, 85.0, 101.0, 45.0, 69.0, 85.0])
line_R_coords_adj_txt_final_answer_6 = np.array([69.0, 77.0, 141.0, 117.0, 61.0, 85.0, 101.0, 45.0, 69.0, 85.0])
line_R_coords_tokenized_txt_final_answer_6 = np.array([69.0, 77.0, 141.0, 117.0, 61.0, 85.0, 101.0, 45.0, 69.0, 85.0])
occupancy_R_coords_jpg_final_answer_6 = np.array([160.0, 184.0, 175.0, 137.0, 125.0, 91.0, 120.0, 93.0, 246.0, 180.0])
occupancy_R_coords_json_final_answer_6 = np.array([145.0, 155.0, 302.0, 244.0, 123.0, 181.0, 214.0, 91.0, 140.0, 178.0])
occupancy_R_coords_adj_json_final_answer_6 = np.array([150.0, 163.0, 302.0, 244.0, 123.0, 181.0, 214.0, 91.0, 144.0, 178.0])
occupancy_R_coords_adj_txt_final_answer_6 = np.array([150.0, 163.0, 302.0, 244.0, 123.0, 181.0, 214.0, 91.0, 144.0, 178.0])
occupancy_R_coords_tokenized_txt_final_answer_6 = np.array([150.0, 163.0, 302.0, 244.0, 123.0, 181.0, 214.0, 91.0, 144.0, 178.0])
occupancy_R_coords_ascii_txt_final_answer_6 = np.array([107.0, 91.0, 161.0, 107.0, 147.0, 109.0, 117.0, 130.0, 107.0, 86.0])


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
line_R_allo_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_jpg_6 = np.array([6.25, 5.555555555555555, 0.0, 0.0, 28.57142857142857, 15.0, 4.166666666666666, 0.0, 18.75, 0.0, 0.0, 14.285714285714285, 16.666666666666664, 33.33333333333333, 0.0, 4.166666666666666, 12.5, 0.0, 8.333333333333332, 5.555555555555555, 12.5, 4.545454545454546, 0.0, 8.333333333333332, 0.0, 12.5, 4.545454545454546, 0.0, 0.0, 16.666666666666664])
line_R_allo_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 87.5, 100.0, 100.0, 100.0, 100.0, 100.0])
line_R_allo_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 56.666666666666664, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_R_allo_ascii_txt_6 = np.array([6.25, 0.0, 0.0, 25.0, 14.285714285714285, 55.00000000000001, 12.5, 35.0, 25.0, 10.0, 35.714285714285715, 100.0, 25.0, 0.0, 6.666666666666667, 6.25, 25.0, 4.166666666666666, 33.33333333333333, 0.0, 37.5, 0.0, 42.5, 0.0, 8.333333333333332, 6.25, 0.0, 0.0, 33.33333333333333, 20.833333333333336])
occupancy_R_allo_jpg_6 = np.array([18.75, 5.555555555555555, 4.411764705882353, 14.285714285714285, 7.142857142857142, 5.0, 4.166666666666666, 0.0, 9.375, 5.0, 28.57142857142857, 7.142857142857142, 4.166666666666666, 12.5, 0.0, 0.0, 15.625, 2.083333333333333, 33.33333333333333, 11.11111111111111, 4.166666666666666, 2.272727272727273, 0.0, 2.083333333333333, 18.75, 3.125, 2.272727272727273, 0.0, 0.0, 25.0])
occupancy_R_allo_json_6 = np.array([56.25, 100.0, 100.0, 7.142857142857142, 100.0, 100.0, 100.0, 100.0, 100.0, 37.5, 100.0, 100.0, 100.0, 100.0, 100.0, 31.25, 100.0, 4.166666666666666, 100.0, 100.0, 14.583333333333334, 100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 100.0, 100.0, 100.0])
occupancy_R_allo_tokenized_txt_6 = np.array([100.0, 100.0, 51.470588235294116, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])


# Raw Scores
line_R_allo_adj_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0, 14.0, 14.0, 12.0, 12.0, 30.0, 24.0, 16.0, 24.0, 12.0, 18.0, 24.0, 22.0, 20.0, 24.0, 24.0, 16.0, 22.0, 12.0, 24.0, 12.0])
line_R_allo_adj_txt_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0, 14.0, 14.0, 12.0, 12.0, 30.0, 24.0, 16.0, 24.0, 12.0, 18.0, 24.0, 22.0, 20.0, 24.0, 24.0, 16.0, 22.0, 12.0, 24.0, 12.0])
line_R_allo_jpg_raw_score_6 = np.array([1.0, 1.0, 0.0, 0.0, 4.0, 3.0, 1.0, 0.0, 3.0, 0.0, 0.0, 2.0, 2.0, 4.0, 0.0, 1.0, 2.0, 0.0, 1.0, 1.0, 3.0, 1.0, 0.0, 2.0, 0.0, 2.0, 1.0, 0.0, 0.0, 2.0])
line_R_allo_json_raw_score_6 = np.array([16.0, 18.0, 34.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0, 14.0, 14.0, 12.0, 12.0, 30.0, 24.0, 16.0, 24.0, 12.0, 18.0, 24.0, 22.0, 20.0, 24.0, 21.0, 16.0, 22.0, 12.0, 24.0, 12.0])
line_R_allo_tokenized_txt_raw_score_6 = np.array([16.0, 18.0, 13.0, 28.0, 14.0, 20.0, 24.0, 10.0, 16.0, 20.0, 14.0, 14.0, 12.0, 12.0, 17.0, 24.0, 16.0, 24.0, 12.0, 18.0, 24.0, 22.0, 20.0, 24.0, 24.0, 16.0, 22.0, 12.0, 24.0, 12.0])
occupancy_R_allo_adj_json_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0, 28.0, 28.0, 24.0, 24.0, 60.0, 48.0, 32.0, 48.0, 24.0, 36.0, 48.0, 44.0, 40.0, 48.0, 48.0, 32.0, 44.0, 24.0, 48.0, 24.0])
occupancy_R_allo_adj_txt_raw_score_6 = np.array([32.0, 36.0, 68.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0, 28.0, 28.0, 24.0, 24.0, 60.0, 48.0, 32.0, 48.0, 24.0, 36.0, 48.0, 44.0, 40.0, 48.0, 48.0, 32.0, 44.0, 24.0, 48.0, 24.0])
occupancy_R_allo_ascii_txt_raw_score_6 = np.array([2.0, 0.0, 0.0, 14.0, 4.0, 22.0, 6.0, 7.0, 8.0, 4.0, 10.0, 28.0, 6.0, 0.0, 4.0, 3.0, 8.0, 2.0, 8.0, 0.0, 18.0, 0.0, 17.0, 0.0, 4.0, 2.0, 0.0, 0.0, 16.0, 5.0])
occupancy_R_allo_jpg_raw_score_6 = np.array([6.0, 2.0, 3.0, 8.0, 2.0, 2.0, 2.0, 0.0, 3.0, 2.0, 8.0, 2.0, 1.0, 3.0, 0.0, 0.0, 5.0, 1.0, 8.0, 4.0, 2.0, 1.0, 0.0, 1.0, 9.0, 1.0, 1.0, 0.0, 0.0, 6.0])
occupancy_R_allo_json_raw_score_6 = np.array([18.0, 36.0, 68.0, 4.0, 28.0, 40.0, 48.0, 20.0, 32.0, 15.0, 28.0, 28.0, 24.0, 24.0, 60.0, 15.0, 32.0, 2.0, 24.0, 36.0, 7.0, 44.0, 40.0, 48.0, 48.0, 32.0, 0.0, 24.0, 48.0, 24.0])
occupancy_R_allo_tokenized_txt_raw_score_6 = np.array([32.0, 36.0, 35.0, 56.0, 28.0, 40.0, 48.0, 20.0, 32.0, 40.0, 28.0, 28.0, 24.0, 24.0, 60.0, 48.0, 32.0, 48.0, 24.0, 36.0, 48.0, 44.0, 40.0, 48.0, 48.0, 32.0, 44.0, 24.0, 48.0, 24])


# Prompt Tokens
line_R_allo_adj_json_input_tokens_6 = np.array([2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2251.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0, 2258.0])
line_R_allo_adj_txt_input_tokens_6 = np.array([722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 722.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0, 729.0])
line_R_allo_jpg_input_tokens_6 = np.array([427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 427.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0])
line_R_allo_json_input_tokens_6 = np.array([1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1802.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0, 1809.0])
line_R_allo_tokenized_txt_input_tokens_6 = np.array([666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 666.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0, 673.0])
occupancy_R_allo_adj_json_input_tokens_6 = np.array([4342.0, 4343.0, 4341.0, 4339.0, 4342.0, 4341.0, 4338.0, 4335.0, 4338.0, 4335.0, 4346.0, 4342.0, 4349.0, 4346.0, 4345.0, 4345.0, 4345.0, 4345.0, 4346.0, 4342.0, 4345.0, 4347.0, 4345.0, 4345.0, 4339.0, 4342.0, 4340.0, 4340.0, 4337.0, 4340.0])
occupancy_R_allo_adj_txt_input_tokens_6 = np.array([1272.0, 1273.0, 1271.0, 1270.0, 1272.0, 1271.0, 1269.0, 1267.0, 1269.0, 1267.0, 1277.0, 1274.0, 1279.0, 1277.0, 1276.0, 1276.0, 1276.0, 1276.0, 1277.0, 1274.0, 1276.0, 1278.0, 1276.0, 1276.0, 1276.0, 1278.0, 1277.0, 1277.0, 1275.0, 1277.0])
occupancy_R_allo_ascii_txt_input_tokens_6 = np.array([244.0, 239.0, 242.0, 241.0, 244.0, 239.0, 246.0, 245.0, 244.0, 238.0, 240.0, 248.0, 253.0, 246.0, 245.0, 252.0, 252.0, 255.0, 247.0, 250.0, 239.0, 250.0, 246.0, 248.0, 247.0, 246.0, 245.0, 248.0, 248.0, 240.0])
occupancy_R_allo_jpg_input_tokens_6 = np.array([434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 434.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0, 441.0])
occupancy_R_allo_json_input_tokens_6 = np.array([981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 981.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0, 988.0])
occupancy_R_allo_tokenized_txt_input_tokens_6 = np.array([2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2155.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162.0, 2162])


# Output Tokens
line_R_allo_adj_json_output_tokens_6 = np.array([10641.0, 14090.0, 10868.0, 8676.0, 9407.0, 8748.0, 9268.0, 6268.0, 7776.0, 10410.0, 2201.0, 6995.0, 2514.0, 3071.0, 5135.0, 4671.0, 3281.0, 5402.0, 4443.0, 8822.0, 5005.0, 3683.0, 2849.0, 4882.0, 3061.0, 6881.0, 3880.0, 5060.0, 6811.0, 2245.0])
line_R_allo_adj_txt_output_tokens_6 = np.array([9343.0, 10961.0, 14119.0, 7126.0, 8186.0, 8730.0, 16201.0, 7605.0, 9852.0, 9724.0, 2021.0, 3565.0, 4763.0, 2505.0, 8419.0, 6202.0, 3481.0, 3858.0, 1951.0, 5510.0, 7171.0, 4418.0, 6123.0, 12364.0, 10660.0, 3453.0, 5589.0, 2832.0, 4567.0, 2457.0])
line_R_allo_jpg_output_tokens_6 = np.array([1839.0, 2913.0, 1991.0, 1423.0, 1177.0, 1452.0, 9757.0, 1935.0, 2147.0, 1590.0, 1684.0, 3028.0, 2921.0, 1794.0, 1968.0, 2833.0, 1142.0, 1853.0, 1919.0, 5547.0, 1194.0, 5132.0, 6738.0, 1281.0, 1510.0, 2520.0, 1141.0, 2593.0, 1171.0, 2581.0])
line_R_allo_json_output_tokens_6 = np.array([5597.0, 11044.0, 9192.0, 9277.0, 3700.0, 9559.0, 7836.0, 7537.0, 7277.0, 6526.0, 7054.0, 4071.0, 2730.0, 1981.0, 5035.0, 4433.0, 3773.0, 3592.0, 3500.0, 8779.0, 4391.0, 6272.0, 11180.0, 4876.0, 3935.0, 4483.0, 6325.0, 3680.0, 6862.0, 2296.0])
line_R_allo_tokenized_txt_output_tokens_6 = np.array([5793.0, 5608.0, 7936.0, 6865.0, 5683.0, 5279.0, 4705.0, 5013.0, 8851.0, 4439.0, 3542.0, 4699.0, 3239.0, 5451.0, 5829.0, 6014.0, 5699.0, 8472.0, 12674.0, 6643.0, 4258.0, 8192.0, 4048.0, 4313.0, 3752.0, 9328.0, 6894.0, 3486.0, 7091.0, 4060.0])
occupancy_R_allo_adj_json_output_tokens_6 = np.array([7474.0, 9524.0, 6529.0, 11801.0, 11052.0, 6205.0, 7602.0, 5525.0, 12079.0, 5873.0, 5301.0, 7315.0, 3576.0, 4825.0, 8855.0, 5666.0, 5557.0, 6112.0, 7106.0, 8047.0, 8399.0, 5464.0, 4502.0, 6550.0, 7229.0, 6139.0, 5323.0, 3610.0, 7648.0, 4815.0])
occupancy_R_allo_adj_txt_output_tokens_6 = np.array([13306.0, 13157.0, 13986.0, 16671.0, 11294.0, 8513.0, 7497.0, 11042.0, 9924.0, 11305.0, 4608.0, 8050.0, 8012.0, 9672.0, 9970.0, 6082.0, 7424.0, 7391.0, 7299.0, 13940.0, 6288.0, 6315.0, 5293.0, 9151.0, 6177.0, 5467.0, 5675.0, 9970.0, 7262.0, 4666.0])
occupancy_R_allo_ascii_txt_output_tokens_6 = np.array([4481.0, 3359.0, 20039.0, 22024.0, 18930.0, 15800.0, 14766.0, 14579.0, 12277.0, 22136.0, 2283.0, 13275.0, 2328.0, 7230.0, 4039.0, 23697.0, 5247.0, 21313.0, 4102.0, 19225.0, 5043.0, 8201.0, 20472.0, 10303.0, 17234.0, 18197.0, 20230.0, 9956.0, 9127.0, 7188.0])
occupancy_R_allo_jpg_output_tokens_6 = np.array([5419.0, 2450.0, 1883.0, 2165.0, 2629.0, 2649.0, 1955.0, 2538.0, 1897.0, 2900.0, 11539.0, 1667.0, 2160.0, 2046.0, 1999.0, 2765.0, 2514.0, 3668.0, 3001.0, 2062.0, 4842.0, 5828.0, 2872.0, 6512.0, 12653.0, 5101.0, 3583.0, 2055.0, 3040.0, 7372.0])
occupancy_R_allo_json_output_tokens_6 = np.array([12925.0, 8580.0, 17443.0, 27933.0, 8077.0, 14011.0, 12393.0, 4414.0, 10960.0, 15358.0, 3146.0, 3481.0, 6025.0, 6531.0, 9261.0, 8750.0, 6261.0, 22810.0, 5497.0, 5845.0, 9640.0, 14959.0, 16474.0, 10289.0, 11345.0, 4998.0, 21743.0, 9990.0, 12132.0, 6541.0])
occupancy_R_allo_tokenized_txt_output_tokens_6 = np.array([6708.0, 6990.0, 7499.0, 11540.0, 3074.0, 4217.0, 14502.0, 6598.0, 6265.0, 8402.0, 5884.0, 3723.0, 3521.0, 7285.0, 5450.0, 5992.0, 4379.0, 6929.0, 6695.0, 4751.0, 3556.0, 3740.0, 10103.0, 4932.0, 9487.0, 7353.0, 3545.0, 7766.0, 10605.0, 4241])

# Final answer only output tokens
line_R_allo_jpg_final_answer_6 = np.array([15.0, 15.0, 19.0, 23.0, 19.0, 19.0, 19.0, 19.0, 23.0, 23.0])
line_R_allo_json_final_answer_6 = np.array([31.0, 35.0, 67.0, 55.0, 27.0, 39.0, 47.0, 19.0, 31.0, 39.0])
line_R_allo_adj_json_final_answer_6 = np.array([31.0, 35.0, 67.0, 55.0, 27.0, 39.0, 47.0, 19.0, 31.0, 39.0])
line_R_allo_adj_txt_final_answer_6 = np.array([31.0, 35.0, 67.0, 55.0, 27.0, 39.0, 47.0, 19.0, 31.0, 39.0])
line_R_allo_tokenized_txt_final_answer_6 = np.array([31.0, 35.0, 31.0, 55.0, 27.0, 39.0, 47.0, 19.0, 31.0, 39.0])
occupancy_R_allo_jpg_final_answer_6 = np.array([111.0, 37.0, 67.0, 91.0, 83.0, 91.0, 55.0, 35.0, 59.0, 87.0])
occupancy_R_allo_json_final_answer_6 = np.array([79.0, 71.0, 135.0, 87.0, 55.0, 79.0, 95.0, 39.0, 63.0, 79.0])
occupancy_R_allo_adj_json_final_answer_6 = np.array([63.0, 71.0, 135.0, 111.0, 55.0, 79.0, 95.0, 39.0, 63.0, 79.0])
occupancy_R_allo_adj_txt_final_answer_6 = np.array([63.0, 71.0, 135.0, 111.0, 55.0, 79.0, 95.0, 39.0, 63.0, 79.0])
occupancy_R_allo_tokenized_txt_final_answer_6 = np.array([63.0, 71.0, 133.0, 111.0, 55.0, 79.0, 95.0, 39.0, 63.0, 79.0])
occupancy_R_allo_ascii_txt_final_answer_6 = np.array([39.0, 63.0, 39.0, 47.0, 39.0, 67.0, 47.0, 93.0, 47.0, 71.0])


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
line_R_ego_jpg_final_answer_6 = np.array([19.0, 19.0, 23.0, 15.0, 19.0, 15.0, 19.0, 19.0, 15.0, 15.0])
line_R_ego_json_final_answer_6 = np.array([31.0, 23.0, 67.0, 55.0, 27.0, 39.0, 51.0, 19.0, 31.0, 39.0])
line_R_ego_adj_json_final_answer_6 = np.array([31.0, 35.0, 67.0, 55.0, 27.0, 39.0, 47.0, 19.0, 31.0, 39.0])
line_R_ego_adj_txt_final_answer_6 = np.array([31.0, 19.0, 67.0, 55.0, 27.0, 39.0, 47.0, 19.0, 31.0, 39.0])
line_R_ego_tokenized_txt_final_answer_6 = np.array([31.0, 35.0, 31.0, 55.0, 27.0, 39.0, 47.0, 19.0, 31.0, 39.0])
occupancy_R_ego_jpg_final_answer_6 = np.array([59.0, 55.0, 95.0, 75.0, 39.0, 63.0, 63.0, 83.0, 69.0, 51.0])
occupancy_R_ego_json_final_answer_6 = np.array([63.0, 71.0, 65.0, 39.0, 55.0, 79.0, 95.0, 39.0, 47.0, 77.0])
occupancy_R_ego_adj_json_final_answer_6 = np.array([63.0, 71.0, 139.0, 111.0, 55.0, 79.0, 95.0, 37.0, 63.0, 79.0])
occupancy_R_ego_adj_txt_final_answer_6 = np.array([63.0, 71.0, 135.0, 111.0, 55.0, 79.0, 95.0, 39.0, 63.0, 79.0])
occupancy_R_ego_tokenized_txt_final_answer_6 = np.array([63.0, 71.0, 135.0, 111.0, 55.0, 79.0, 99.0, 39.0, 63.0, 79.0])
occupancy_R_ego_ascii_txt_final_answer_6 = np.array([107.0, 63.0, 51.0, 39.0, 67.0, 35.0, 55.0, 65.0, 55.0, 37.0])


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