import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi


x_axis_line = ['3x3', '6x6', '15x15']
x_axis_occ = ['7x7', '13x13', '31x31']

def sample_size(sigma):
    """Calculates the required sample size for a given standard deviation and margin of error."""
    Z = 1.96  # Z-score for 95% confidence level
    E = 5.0   # Margin of error
    n = (Z * sigma / E) ** 2
    return np.ceil(n)


# # --- Statistical determination of sample size ----------

# NR -- Coords -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Coords 3x3
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 42.857142857142854, 100.0, 100.0])
line_jpg = np.array([40.0, 20.0, 40.0, 60.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_json = np.array([100.0, 20.0, 60.0, 20.0, 42.857142857142854, 100.0, 20.0, 14.285714285714285, 42.857142857142854, 20.0])
line_tokenized_txt = np.array([20.0, 0.0, 0.0, 60.0, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 20.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 110.00000000000001])
occupancy_jpg = np.array([0.0, 0.0, 55.55555555555556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json = np.array([100.0, 110.00000000000001, 100.0, 110.00000000000001, 7.6923076923076925, 100.0, 110.00000000000001, 100.0, 100.0, 110.00000000000001])
occupancy_tokenized_txt = np.array([11.11111111111111, 110.00000000000001, 100.0, 100.0, 7.6923076923076925, 11.11111111111111, 100.0, 100.0, 7.6923076923076925, 110.00000000000001])
# Averages and std deviation 3x3
avg_line_adj_json = np.mean(line_adj_json)
avg_line_adj_txt = np.mean(line_adj_txt)
avg_line_jpg = np.mean(line_jpg)
avg_line_json = np.mean(line_json)
avg_line_tokenized_txt = np.mean(line_tokenized_txt)
avg_occupancy_adj_json = np.mean(occupancy_adj_json)
avg_occupancy_adj_txt = np.mean(occupancy_adj_txt)
avg_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
avg_occupancy_jpg = np.mean(occupancy_jpg)
avg_occupancy_json = np.mean(occupancy_json)
avg_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_NR_coords_line_adj_json = np.std(line_adj_json)
# sd_NR_coords_line_adj_txt = np.std(line_adj_txt)
# sd_NR_coords_line_jpg = np.std(line_jpg)
# sd_NR_coords_line_json = np.std(line_json)
# sd_NR_coords_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_NR_coords_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_NR_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_NR_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_NR_coords_occupancy_jpg = np.std(occupancy_jpg)
# sd_NR_coords_occupancy_json = np.std(occupancy_json)
# sd_NR_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# Accuracy NR Coords 6x6
line_adj_json_6 = np.array([52.94117647058824, 100.0, 40.0, 44.827586206896555, 100.0, 76.19047619047619, 96.0, 81.81818181818183, 58.82352941176471, 76.19047619047619])
line_adj_txt_6 = np.array([52.94117647058824, 42.10526315789473, 14.285714285714285, 24.137931034482758, 100.0, 100.0, 96.0, 100.0, 58.82352941176471, 47.61904761904761])
line_jpg_6 = np.array([11.76470588235294, 10.526315789473683, 2.857142857142857, 3.4482758620689653, 26.666666666666668, 4.761904761904762, 8.0, 9.090909090909092, 11.76470588235294, 4.761904761904762])
line_json_6 = np.array([11.76470588235294, 10.526315789473683, 5.714285714285714, 13.793103448275861, 26.666666666666668, 14.285714285714285, 16.0, 36.36363636363637, 11.76470588235294, 4.761904761904762])
line_tokenized_txt_6 = np.array([35.294117647058826, 5.263157894736842, 2.857142857142857, 3.4482758620689653, 20.0, 4.761904761904762, 4.0, 9.090909090909092, 0.0, 4.761904761904762])
occupancy_adj_json_6 = np.array([100.0, 78.37837837837837, 100.0, 85.96491228070175, 100.0, 100.0, 100.0, 100.0, 75.75757575757575, 46.34146341463415])
occupancy_adj_txt_6 = np.array([51.515151515151516, 100.0, 24.637681159420293, 100.0, 100.0, 41.46341463414634, 42.857142857142854, 100.0, 57.57575757575758, 46.34146341463415])
occupancy_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 29.82456140350877, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 80.95238095238095, 3.0303030303030303, 12.195121951219512])
occupancy_tokenized_txt_6 = np.array([3.0303030303030303, 2.7027027027027026, 10.144927536231885, 22.807017543859647, 3.4482758620689653, 21.951219512195124, 2.0408163265306123, 52.38095238095239, 15.151515151515152, 12.195121951219512])
# Averages and std deviation 6x6
avg_line_adj_json_6 = np.mean(line_adj_json_6)
avg_line_adj_txt_6 = np.mean(line_adj_txt_6)
avg_line_jpg_6 = np.mean(line_jpg_6)
avg_line_json_6 = np.mean(line_json_6)
avg_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
avg_occupancy_json_6 = np.mean(occupancy_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_NR_coords_line_adj_json_6 = np.std(line_adj_json_6)
# sd_NR_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_NR_coords_line_jpg_6 = np.std(line_jpg_6)
# sd_NR_coords_line_json_6 = np.std(line_json_6)
# sd_NR_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_NR_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_NR_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_NR_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_NR_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_NR_coords_occupancy_json_6 = np.std(occupancy_json_6)
# sd_NR_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy NR Coords 15x15
line_adj_json_15 = np.array([2.2900763358778624, 28.985507246376812, 31.654676258992804, 40.35087719298245, 3.937007874015748, 18.81188118811881, 7.462686567164178, 36.708860759493675, 11.278195488721805, 27.659574468085108])
line_adj_txt_15 = np.array([8.396946564885496, 27.536231884057973, 10.79136690647482, 15.789473684210526, 4.724409448818897, 23.762376237623762, 4.477611940298507, 3.79746835443038, 5.263157894736842, 34.04255319148936])
line_jpg_15 = np.array([3.0534351145038165, 1.4492753623188406, 2.158273381294964, 1.7543859649122806, 0.7874015748031495, 0.9900990099009901, 1.4925373134328357, 1.2658227848101267, 2.2556390977443606, 2.127659574468085])
line_json_15 = np.array([1.5267175572519083, 5.797101449275362, 1.4388489208633095, 1.7543859649122806, 3.937007874015748, 0.9900990099009901, 1.4925373134328357, 2.5316455696202533, 2.2556390977443606, 2.127659574468085])
line_tokenized_txt_15 = np.array([0.7633587786259541, 0.0, 0.0, 7.017543859649122, 1.574803149606299, 0.9900990099009901, 0.0, 0.0, 0.0, 2.127659574468085])
occupancy_adj_json_15 = np.array([25.67049808429119, 8.02919708029197, 3.2490974729241873, 54.86725663716814, 14.624505928853754, 42.28855721393035, 63.90977443609023, 14.64968152866242, 6.415094339622642, 13.978494623655912])
occupancy_adj_txt_15 = np.array([5.747126436781609, 6.569343065693431, 3.2490974729241873, 32.743362831858406, 9.881422924901186, 24.378109452736318, 26.31578947368421, 32.48407643312102, 26.037735849056602, 34.40860215053764])
occupancy_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_15 = np.array([0.38314176245210724, 0.7299270072992701, 0.36101083032490977, 6.1946902654867255, 3.557312252964427, 8.45771144278607, 3.7593984962406015, 3.1847133757961785, 0.37735849056603776, 9.67741935483871])
occupancy_tokenized_txt_15 = np.array([0.38314176245210724, 0.7299270072992701, 0.36101083032490977, 6.1946902654867255, 4.3478260869565215, 6.467661691542288, 8.270676691729323, 5.7324840764331215, 0.37735849056603776, 11.827956989247312])
# Averages and std deviation 15x15
avg_line_adj_json_15 = np.mean(line_adj_json_15)
avg_line_adj_txt_15 = np.mean(line_adj_txt_15)
avg_line_jpg_15 = np.mean(line_jpg_15)
avg_line_json_15 = np.mean(line_json_15)
avg_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
avg_occupancy_json_15 = np.mean(occupancy_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_NR_coords_line_adj_json_15 = np.std(line_adj_json_15)
# sd_NR_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_NR_coords_line_jpg_15 = np.std(line_jpg_15)
# sd_NR_coords_line_json_15 = np.std(line_json_15)
# sd_NR_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_NR_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_NR_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_NR_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_NR_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_NR_coords_occupancy_json_15 = np.std(occupancy_json_15)
# sd_NR_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Flash-Lite, Coordinates Output", fontsize=16, pad=20)

sample_sizes_3x3_NR_coords = [
    sample_size(np.std(line_adj_json)),
    sample_size(np.std(line_adj_txt)),
    sample_size(np.std(line_jpg)),
    sample_size(np.std(line_json)),
    sample_size(np.std(line_tokenized_txt)),
    sample_size(np.std(occupancy_adj_json)),
    sample_size(np.std(occupancy_adj_txt)),
    sample_size(np.std(occupancy_ascii_txt)),
    sample_size(np.std(occupancy_jpg)),
    sample_size(np.std(occupancy_json)),
    sample_size(np.std(occupancy_tokenized_txt))
    ]
sample_sizes_6x6_NR_coords=[
    sample_size(np.std(line_adj_json_6)),
    sample_size(np.std(line_adj_txt_6)),
    sample_size(np.std(line_jpg_6)),
    sample_size(np.std(line_json_6)),
    sample_size(np.std(line_tokenized_txt_6)),
    sample_size(np.std(occupancy_adj_json_6)),
    sample_size(np.std(occupancy_adj_txt_6)),
    sample_size(np.std(occupancy_ascii_txt_6)),
    sample_size(np.std(occupancy_jpg_6)),
    sample_size(np.std(occupancy_json_6)),
    sample_size(np.std(occupancy_tokenized_txt_6)) ]
sample_sizes_15x15_NR_coords=[
    sample_size(np.std(line_adj_json_15)),
    sample_size(np.std(line_adj_txt_15)),
    sample_size(np.std(line_jpg_15)),
    sample_size(np.std(line_json_15)),
    sample_size(np.std(line_tokenized_txt_15)),
    sample_size(np.std(occupancy_adj_json_15)),
    sample_size(np.std(occupancy_adj_txt_15)),
    sample_size(np.std(occupancy_ascii_txt_15)),
    sample_size(np.std(occupancy_jpg_15)),
    sample_size(np.std(occupancy_json_15)),
    sample_size(np.std(occupancy_tokenized_txt_15)) ]

# NR -- Allo -- Accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Allo 3x3
line_adj_json = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 100.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_adj_txt = np.array([0.0, 100.0, 0.0, 100.0, 0.0, 0.0, 100.0, 33.33333333333333, 33.33333333333333, 100.0])
line_jpg = np.array([50.0, 0.0, 50.0, 100.0, 33.33333333333333, 50.0, 100.0, 0.0, 0.0, 0.0])
line_json = np.array([100.0, 0.0, 100.0, 0.0, 33.33333333333333, 100.0, 0.0, 0.0, 33.33333333333333, 0.0])
line_tokenized_txt = np.array([0.0, 100.0, 0.0, 25.0, 0.0, 0.0, 25.0, 33.33333333333333, 0.0, 25.0])
occupancy_adj_json = np.array([50.0, 25.0, 75.0, 110.00000000000001, 0.0, 50.0, 110.00000000000001, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_adj_txt = np.array([62.5, 25.0, 0.0, 37.5, 33.33333333333333, 25.0, 37.5, 33.33333333333333, 0.0, 110.00000000000001])
occupancy_ascii_txt = np.array([0.0, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 62.5, 33.33333333333333, 33.33333333333333, 0.0])
occupancy_jpg = np.array([12.5, 0.0, 12.5, 0.0, 8.333333333333332, 12.5, 12.5, 8.333333333333332, 8.333333333333332, 0.0])
occupancy_json = np.array([62.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 33.33333333333333, 0.0, 87.5])
occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 50.0, 8.333333333333332, 12.5, 0.0, 8.333333333333332, 0.0, 110.00000000000001])
# Averages and std deviation 3x3
avg_line_adj_json = np.mean(line_adj_json)
avg_line_adj_txt = np.mean(line_adj_txt)
avg_line_jpg = np.mean(line_jpg)
avg_line_json = np.mean(line_json)
avg_line_tokenized_txt = np.mean(line_tokenized_txt)
avg_occupancy_adj_json = np.mean(occupancy_adj_json)
avg_occupancy_adj_txt = np.mean(occupancy_adj_txt)
avg_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
avg_occupancy_jpg = np.mean(occupancy_jpg)
avg_occupancy_json = np.mean(occupancy_json)
avg_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_NR_allo_line_adj_json = np.std(line_adj_json)
# sd_NR_allo_line_adj_txt = np.std(line_adj_txt)
# sd_NR_allo_line_jpg = np.std(line_jpg)
# sd_NR_allo_line_json = np.std(line_json)
# sd_NR_allo_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_NR_allo_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_NR_allo_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_NR_allo_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_NR_allo_occupancy_jpg = np.std(occupancy_jpg)
# sd_NR_allo_occupancy_json = np.std(occupancy_json)
# sd_NR_allo_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# Accuracy NR Allo 6x6
line_adj_json_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 0.0, 20.0, 8.333333333333332, 110.00000000000001, 12.5, 15.0])
line_adj_txt_6 = np.array([25.0, 0.0, 11.76470588235294, 17.857142857142858, 21.428571428571427, 5.0, 0.0, 60.0, 0.0, 5.0])
line_jpg_6 = np.array([6.25, 0.0, 2.941176470588235, 0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 10.0])
line_json_6 = np.array([12.5, 5.555555555555555, 0.0, 17.857142857142858, 21.428571428571427, 0.0, 12.5, 0.0, 18.75, 0.0])
line_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 3.571428571428571, 21.428571428571427, 5.0, 0.0, 10.0, 0.0, 10.0])
occupancy_adj_json_6 = np.array([18.75, 5.555555555555555, 7.352941176470589, 17.857142857142858, 14.285714285714285, 5.0, 8.333333333333332, 50.0, 6.25, 5.0])
occupancy_adj_txt_6 = np.array([18.75, 5.555555555555555, 8.823529411764707, 17.857142857142858, 14.285714285714285, 17.5, 8.333333333333332, 90.0, 18.75, 0.0])
occupancy_ascii_txt_6 = np.array([6.25, 11.11111111111111, 0.0, 21.428571428571427, 0.0, np.nan, 2.083333333333333, 55.00000000000001, 0.0, 7.5])
occupancy_jpg_6 = np.array([0.0, 0.0, 1.4705882352941175, 10.714285714285714, 3.571428571428571, 2.5, 4.166666666666666, 5.0, 3.125, 0.0])
occupancy_json_6 = np.array([0.0, 0.0, 5.88235294117647, 14.285714285714285, 0.0, 10.0, 0.0, 80.0, 0.0, 10.0])
occupancy_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 14.285714285714285, np.nan, 0.0, 0.0, 40.0, 0.0, 2.5])
# Averages and std deviation 6x6
avg_line_adj_json_6 = np.mean(line_adj_json_6)
avg_line_adj_txt_6 = np.mean(line_adj_txt_6)
avg_line_jpg_6 = np.mean(line_jpg_6)
avg_line_json_6 = np.mean(line_json_6)
avg_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
avg_occupancy_json_6 = np.mean(occupancy_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_NR_allo_line_adj_json_6 = np.std(line_adj_json_6)
# sd_NR_allo_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_NR_allo_line_jpg_6 = np.std(line_jpg_6)
# sd_NR_allo_line_json_6 = np.std(line_json_6)
# sd_NR_allo_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_NR_allo_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_NR_allo_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_NR_allo_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_NR_allo_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_NR_allo_occupancy_json_6 = np.std(occupancy_json_6)
# sd_NR_allo_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy NR Allo 15x15
line_adj_json_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 3.1746031746031744, 8.0, 1.5151515151515151, 1.282051282051282, 0.0, 2.1739130434782608])
line_adj_txt_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 3.968253968253968, 10.0, 1.5151515151515151, 1.282051282051282, 0.0, 2.1739130434782608])
line_jpg_15 = np.array([np.nan, 0.0, 0.0, 3.571428571428571, 0.7936507936507936, np.nan, np.nan, np.nan, 0.0, 10.869565217391305])
line_json_15 = np.array([1.5384615384615385, 4.411764705882353, 0.7246376811594203, 1.7857142857142856, 1.5873015873015872, 8.0, 0.0, np.nan, 0.7575757575757576, np.nan])
line_tokenized_txt_15 = np.array([0.0, np.nan, 0.0, 0.0, 0.0, np.nan, 3.0303030303030303, 0.0, 0.0, np.nan])
occupancy_adj_json_15 = np.array([0.7692307692307693, 1.4705882352941175, 2.1739130434782608, np.nan, 2.380952380952381, 7.000000000000001, 2.272727272727273, 2.564102564102564, 1.5151515151515151, 8.695652173913043])
occupancy_adj_txt_15 = np.array([0.0, np.nan, 0.7246376811594203, 0.0, 0.0, 8.0, 3.0303030303030303, np.nan, 0.7575757575757576, 0.0])
occupancy_ascii_txt_15 = np.array([0.0, 0.0, 0.7246376811594203, 2.6785714285714284, 0.0, np.nan, 2.272727272727273, 1.9230769230769231, 0.0, 3.260869565217391])
occupancy_jpg_15 = np.array([0.0, 0.0, 0.0, 0.8928571428571428, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
occupancy_json_15 = np.array([0.0, 0.0, 0.0, 0.8928571428571428, 2.380952380952381, 0.0, 0.7575757575757576, 0.641025641025641, 0.0, 1.0869565217391304])
occupancy_tokenized_txt_15 = np.array([0.0, 0.0, 0.0, 1.7857142857142856, 2.380952380952381, 6.0, 3.0303030303030303, 1.9230769230769231, 0.0, 4.3478260869565215])
# Averages and std deviation 15x15
avg_line_adj_json_15 = np.mean(line_adj_json_15)
avg_line_adj_txt_15 = np.mean(line_adj_txt_15)
avg_line_jpg_15 = np.mean(line_jpg_15)
avg_line_json_15 = np.mean(line_json_15)
avg_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
avg_occupancy_json_15 = np.mean(occupancy_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_NR_allo_line_adj_json_15 = np.std(line_adj_json_15)
# sd_NR_allo_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_NR_allo_line_jpg_15 = np.std(line_jpg_15)
# sd_NR_allo_line_json_15 = np.std(line_json_15)
# sd_NR_allo_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_NR_allo_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_NR_allo_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_NR_allo_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_NR_allo_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_NR_allo_occupancy_json_15 = np.std(occupancy_json_15)
# sd_NR_allo_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Flash-Lite, Allocentric Output", fontsize=16, pad=20)

sample_sizes_3x3_NR_allo = [
    sample_size(np.std(line_adj_json)),
    sample_size(np.std(line_adj_txt)),
    sample_size(np.std(line_jpg)),
    sample_size(np.std(line_json)),
    sample_size(np.std(line_tokenized_txt)),
    sample_size(np.std(occupancy_adj_json)),
    sample_size(np.std(occupancy_adj_txt)),
    sample_size(np.std(occupancy_ascii_txt)),
    sample_size(np.std(occupancy_jpg)),
    sample_size(np.std(occupancy_json)),
    sample_size(np.std(occupancy_tokenized_txt))
    ]
sample_sizes_6x6_NR_allo=[
    sample_size(np.std(line_adj_json_6)),
    sample_size(np.std(line_adj_txt_6)),
    sample_size(np.std(line_jpg_6)),
    sample_size(np.std(line_json_6)),
    sample_size(np.std(line_tokenized_txt_6)),
    sample_size(np.std(occupancy_adj_json_6)),
    sample_size(np.std(occupancy_adj_txt_6)),
    sample_size(np.nanstd(occupancy_ascii_txt_6)),
    sample_size(np.std(occupancy_jpg_6)),
    sample_size(np.std(occupancy_json_6)),
    sample_size(np.nanstd(occupancy_tokenized_txt_6)) ]
sample_sizes_15x15_NR_allo=[
    sample_size(np.std(line_adj_json_15)),
    sample_size(np.std(line_adj_txt_15)),
    sample_size(np.nanstd(line_jpg_15)),
    sample_size(np.nanstd(line_json_15)),
    sample_size(np.nanstd(line_tokenized_txt_15)),
    sample_size(np.nanstd(occupancy_adj_json_15)),
    sample_size(np.nanstd(occupancy_adj_txt_15)),
    sample_size(np.nanstd(occupancy_ascii_txt_15)),
    sample_size(np.nanstd(occupancy_jpg_15)),
    sample_size(np.std(occupancy_json_15)),
    sample_size(np.std(occupancy_tokenized_txt_15)) ]

# NR -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy NR Ego 3x3
line_adj_json = np.array([25.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_jpg = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json = np.array([25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_adj_json = np.array([0.0, 0.0, 12.5, 0.0, 8.333333333333332, 0.0, 0.0, 0.0, 8.333333333333332, 0.0])
occupancy_adj_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg = np.array([0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# Averages and std deviation 3x3
avg_line_adj_json = np.mean(line_adj_json)
avg_line_adj_txt = np.mean(line_adj_txt)
avg_line_jpg = np.mean(line_jpg)
avg_line_json = np.mean(line_json)
avg_line_tokenized_txt = np.mean(line_tokenized_txt)
avg_occupancy_adj_json = np.mean(occupancy_adj_json)
avg_occupancy_adj_txt = np.mean(occupancy_adj_txt)
avg_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
avg_occupancy_jpg = np.mean(occupancy_jpg)
avg_occupancy_json = np.mean(occupancy_json)
avg_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_NR_ego_line_adj_json = np.std(line_adj_json)
# sd_NR_ego_line_adj_txt = np.std(line_adj_txt)
# sd_NR_ego_line_jpg = np.std(line_jpg)
# sd_NR_ego_line_json = np.std(line_json)
# sd_NR_ego_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_NR_ego_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_NR_ego_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_NR_ego_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_NR_ego_occupancy_jpg = np.std(occupancy_jpg)
# sd_NR_ego_occupancy_json = np.std(occupancy_json)
# sd_NR_ego_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# Accuracy NR Ego 6x6
line_adj_json_6 = np.array([18.75, 0.0, 0.0, 0.0, 14.285714285714285, 0.0, 0.0, 0.0, 0.0, 0.0])
line_adj_txt_6 = np.array([12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 0.0, 0.0, 4.166666666666666, 0.0, 0.0, 0.0])
line_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.25, 0.0])
occupancy_adj_json_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_adj_txt_6 = np.array([0.0, 2.7777777777777777, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_ascii_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg_6 = np.array([3.125, 2.7777777777777777, 0.0, 0.0, 3.571428571428571, 0.0, 2.083333333333333, 0.0, 0.0, 0.0])
occupancy_json_6 = np.array([0.0, 5.555555555555555, 0.0, 0.0, 3.571428571428571, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_tokenized_txt_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# Averages and std deviation 6x6
avg_line_adj_json_6 = np.mean(line_adj_json_6)
avg_line_adj_txt_6 = np.mean(line_adj_txt_6)
avg_line_jpg_6 = np.mean(line_jpg_6)
avg_line_json_6 = np.mean(line_json_6)
avg_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
avg_occupancy_json_6 = np.mean(occupancy_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_NR_ego_line_adj_json_6 = np.std(line_adj_json_6)
# sd_NR_ego_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_NR_ego_line_jpg_6 = np.std(line_jpg_6)
# sd_NR_ego_line_json_6 = np.std(line_json_6)
# sd_NR_ego_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_NR_ego_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_NR_ego_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_NR_ego_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_NR_ego_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_NR_ego_occupancy_json_6 = np.std(occupancy_json_6)
# sd_NR_ego_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy NR Ego 15x15
line_adj_json_15 = np.array([0.0, 0.0, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_adj_txt_15 = np.array([1.5384615384615385, 4.411764705882353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_jpg_15 = np.array([1.5384615384615385, 5.88235294117647, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_json_15 = np.array([1.5384615384615385, 0.0, 0.7246376811594203, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_tokenized_txt_15 = np.array([0.7692307692307693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_adj_json_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_adj_txt_15 = np.array([1.5384615384615385, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_jpg_15 = np.array([0.7692307692307693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
occupancy_json_15 = np.array([0.0, 0.0, 0.36231884057971014, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
occupancy_tokenized_txt_15 = np.array([0.38461538461538464, 4.411764705882353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3787878787878788, 0.0])
# Averages and std deviation 15x15
avg_line_adj_json_15 = np.mean(line_adj_json_15)
avg_line_adj_txt_15 = np.mean(line_adj_txt_15)
avg_line_jpg_15 = np.mean(line_jpg_15)
avg_line_json_15 = np.mean(line_json_15)
avg_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
avg_occupancy_json_15 = np.mean(occupancy_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_NR_ego_line_adj_json_15 = np.std(line_adj_json_15)
# sd_NR_ego_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_NR_ego_line_jpg_15 = np.std(line_jpg_15)
# sd_NR_ego_line_json_15 = np.std(line_json_15)
# sd_NR_ego_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_NR_ego_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_NR_ego_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_NR_ego_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_NR_ego_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_NR_ego_occupancy_json_15 = np.std(occupancy_json_15)
# sd_NR_ego_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Flash-Lite, Egocentric Output", fontsize=16, pad=20)

sample_sizes_3x3_NR_ego = [
    sample_size(np.std(line_adj_json)),
    sample_size(np.std(line_adj_txt)),
    sample_size(np.std(line_jpg)),
    sample_size(np.std(line_json)),
    sample_size(np.std(line_tokenized_txt)),
    sample_size(np.std(occupancy_adj_json)),
    sample_size(np.std(occupancy_adj_txt)),
    sample_size(np.std(occupancy_ascii_txt)),
    sample_size(np.std(occupancy_jpg)),
    sample_size(np.std(occupancy_json)),
    sample_size(np.std(occupancy_tokenized_txt))
    ]
sample_sizes_6x6_NR_ego=[
    sample_size(np.std(line_adj_json_6)),
    sample_size(np.std(line_adj_txt_6)),
    sample_size(np.std(line_jpg_6)),
    sample_size(np.std(line_json_6)),
    sample_size(np.std(line_tokenized_txt_6)),
    sample_size(np.std(occupancy_adj_json_6)),
    sample_size(np.std(occupancy_adj_txt_6)),
    sample_size(np.std(occupancy_ascii_txt_6)),
    sample_size(np.std(occupancy_jpg_6)),
    sample_size(np.std(occupancy_json_6)),
    sample_size(np.std(occupancy_tokenized_txt_6)) ]
sample_sizes_15x15_NR_ego=[
    sample_size(np.std(line_adj_json_15)),
    sample_size(np.std(line_adj_txt_15)),
    sample_size(np.std(line_jpg_15)),
    sample_size(np.std(line_json_15)),
    sample_size(np.std(line_tokenized_txt_15)),
    sample_size(np.std(occupancy_adj_json_15)),
    sample_size(np.std(occupancy_adj_txt_15)),
    sample_size(np.std(occupancy_ascii_txt_15)),
     sample_size(np.std(occupancy_jpg_15)),
    sample_size(np.std(occupancy_json_15)),
    sample_size(np.std(occupancy_tokenized_txt_15))]

# R -- Coords -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Coords 3x3
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg = np.array([40.0, 100.0, 100.0, 100.0, 28.57142857142857, 40.0, 40.0, 100.0, 100.0, 100.0])
line_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([22.22222222222222, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 46.15384615384615, 77.77777777777779])
occupancy_jpg = np.array([11.11111111111111, 22.22222222222222, 55.55555555555556, 0.0, 7.6923076923076925, 11.11111111111111, 33.33333333333333, 0.0, 7.6923076923076925, 100.0])
occupancy_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 3x3
avg_line_adj_json = np.mean(line_adj_json)
avg_line_adj_txt = np.mean(line_adj_txt)
avg_line_jpg = np.mean(line_jpg)
avg_line_json = np.mean(line_json)
avg_line_tokenized_txt = np.mean(line_tokenized_txt)
avg_occupancy_adj_json = np.mean(occupancy_adj_json)
avg_occupancy_adj_txt = np.mean(occupancy_adj_txt)
avg_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
avg_occupancy_jpg = np.mean(occupancy_jpg)
avg_occupancy_json = np.mean(occupancy_json)
avg_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_R_coords_line_adj_json = np.std(line_adj_json)
# sd_R_coords_line_adj_txt = np.std(line_adj_txt)
# sd_R_coords_line_jpg = np.std(line_jpg)
# sd_R_coords_line_json = np.std(line_json)
# sd_R_coords_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_R_coords_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_R_coords_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_R_coords_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_R_coords_occupancy_jpg = np.std(occupancy_jpg)
# sd_R_coords_occupancy_json = np.std(occupancy_json)
# sd_R_coords_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# Accuracy R Coords 6x6
line_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg_6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt_6 = np.array([24.242424242424242, 32.432432432432435, 11.594202898550725, 1.7543859649122806, 31.03448275862069, 2.4390243902439024, 2.0408163265306123, 0.0, 27.27272727272727, 2.4390243902439024])
occupancy_jpg_6 = np.array([0.0, 2.7027027027027026, 0.0, 0.0, 0.0, 2.4390243902439024, 0.0, 0.0, 0.0, 0.0])
occupancy_json_6 = np.array([27.27272727272727, 48.64864864864865, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 60.60606060606061, 100.0])
occupancy_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 6x6
avg_line_adj_json_6 = np.mean(line_adj_json_6)
avg_line_adj_txt_6 = np.mean(line_adj_txt_6)
avg_line_jpg_6 = np.mean(line_jpg_6)
avg_line_json_6 = np.mean(line_json_6)
avg_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
avg_occupancy_json_6 = np.mean(occupancy_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_R_coords_line_adj_json_6 = np.std(line_adj_json_6)
# sd_R_coords_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_R_coords_line_jpg_6 = np.std(line_jpg_6)
# sd_R_coords_line_json_6 = np.std(line_json_6)
# sd_R_coords_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_R_coords_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_R_coords_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_R_coords_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_R_coords_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_R_coords_occupancy_json_6 = np.std(occupancy_json_6)
# sd_R_coords_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy R Coords 15x15
line_adj_json_15 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt_15 = np.array([19.083969465648856, 14.492753623188406, 51.798561151079134, 100.0, 60.629921259842526, 92.07920792079209, 100.0, 56.9620253164557, 46.616541353383454, 100.0])
line_jpg_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
line_json_15 = np.array([23.66412213740458, 15.942028985507244, 7.194244604316546, 7.017543859649122, 12.598425196850393, 9.900990099009901, 56.71641791044776, 50.63291139240506, 1.5037593984962405, 42.5531914893617])
line_tokenized_txt_15 = np.array([96.18320610687023, 100.0, 100.0, 100.0, 92.1259842519685, 22.772277227722775, 100.0, 62.0253164556962, 100.0, 100.0])
occupancy_adj_json_15 = np.array([100.0, 100.0, 68.95306859205776, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt_15 = np.array([34.099616858237546, 15.328467153284672, 24.90974729241877, 29.20353982300885, 12.25296442687747, 42.28855721393035, 3.7593984962406015, 57.961783439490446, 46.41509433962264, 95.6989247311828])
occupancy_ascii_txt_15 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.301075268817205])
occupancy_jpg_15 = np.array([1.9157088122605364, 4.37956204379562, 1.083032490974729, 0.8849557522123894, 0.3952569169960474, 0.0, 0.7518796992481203, 0.0, 0.0, 0.0])
occupancy_json_15 = np.array([11.877394636015326, 35.03649635036496, 1.8050541516245486, 15.04424778761062, 3.557312252964427, 21.393034825870647, 30.075187969924812, 15.92356687898089, 7.169811320754717, 33.33333333333333])
occupancy_tokenized_txt_15 = np.array([39.46360153256705, 100.0, 7.581227436823104, 100.0, 7.905138339920949, 7.462686567164178, 100.0, 13.375796178343949, 6.415094339622642, 11.827956989247312])
# Averages and std deviation 15x15
avg_line_adj_json_15 = np.mean(line_adj_json_15)
avg_line_adj_txt_15 = np.mean(line_adj_txt_15)
avg_line_jpg_15 = np.mean(line_jpg_15)
avg_line_json_15 = np.mean(line_json_15)
avg_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
avg_occupancy_json_15 = np.mean(occupancy_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_R_coords_line_adj_json_15 = np.std(line_adj_json_15)
# sd_R_coords_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_R_coords_line_jpg_15 = np.std(line_jpg_15)
# sd_R_coords_line_json_15 = np.std(line_json_15)
# sd_R_coords_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_R_coords_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_R_coords_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_R_coords_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_R_coords_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_R_coords_occupancy_json_15 = np.std(occupancy_json_15)
# sd_R_coords_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Pro, Coordinates Output", fontsize=16, pad=20)

sample_sizes_3x3_R_coords = [
    sample_size(np.std(line_adj_json)),
    sample_size(np.std(line_adj_txt)),
    sample_size(np.std(line_jpg)),
    sample_size(np.std(line_json)),
    sample_size(np.std(line_tokenized_txt)),
    sample_size(np.std(occupancy_adj_json)),
    sample_size(np.std(occupancy_adj_txt)),
    sample_size(np.std(occupancy_ascii_txt)),
    sample_size(np.std(occupancy_jpg)),
    sample_size(np.std(occupancy_json)),
    sample_size(np.std(occupancy_tokenized_txt))
    ]
sample_sizes_6x6_R_coords=[
    sample_size(np.std(line_adj_json_6)),
    sample_size(np.std(line_adj_txt_6)),
    sample_size(np.std(line_jpg_6)),
    sample_size(np.std(line_json_6)),
    sample_size(np.std(line_tokenized_txt_6)),
    sample_size(np.std(occupancy_adj_json_6)),
    sample_size(np.std(occupancy_adj_txt_6)),
    sample_size(np.std(occupancy_ascii_txt_6)),
    sample_size(np.std(occupancy_jpg_6)),
    sample_size(np.std(occupancy_json_6)),
    sample_size(np.std(occupancy_tokenized_txt_6)) ]
sample_sizes_15x15_R_coords=[
    sample_size(np.std(line_adj_json_15)),
    sample_size(np.std(line_adj_txt_15)),
    sample_size(np.std(line_jpg_15)),
    sample_size(np.std(line_json_15)),
    sample_size(np.std(line_tokenized_txt_15)),
    sample_size(np.std(occupancy_adj_json_15)),
    sample_size(np.std(occupancy_adj_txt_15)),
    sample_size(np.std(occupancy_ascii_txt_15)),
     sample_size(np.std(occupancy_jpg_15)),
    sample_size(np.std(occupancy_json_15)),
    sample_size(np.std(occupancy_tokenized_txt_15)) ]


# # R -- Allo -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Allo 3x3
line_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg = np.array([0.0, 0.0, 100.0, 100.0, 33.33333333333333, 25.0, 100.0, 16.666666666666664, 100.0, 0.0])
line_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 41.66666666666667, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_jpg = np.array([0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 25.0, 16.666666666666664, 0.0, 37.5])
occupancy_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 3x3
avg_line_adj_json = np.mean(line_adj_json)
avg_line_adj_txt = np.mean(line_adj_txt)
avg_line_jpg = np.mean(line_jpg)
avg_line_json = np.mean(line_json)
avg_line_tokenized_txt = np.mean(line_tokenized_txt)
avg_occupancy_adj_json = np.mean(occupancy_adj_json)
avg_occupancy_adj_txt = np.mean(occupancy_adj_txt)
avg_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
avg_occupancy_jpg = np.mean(occupancy_jpg)
avg_occupancy_json = np.mean(occupancy_json)
avg_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_R_allo_line_adj_json = np.std(line_adj_json)
# sd_R_allo_line_adj_txt = np.std(line_adj_txt)
# sd_R_allo_line_jpg = np.std(line_jpg)
# sd_R_allo_line_json = np.std(line_json)
# sd_R_allo_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_R_allo_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_R_allo_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_R_allo_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_R_allo_occupancy_jpg = np.std(occupancy_jpg)
# sd_R_allo_occupancy_json = np.std(occupancy_json)
# sd_R_allo_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# Accuracy R Allo 6x6
line_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg_6 = np.array([6.25, 5.555555555555555, 0.0, 0.0, 28.57142857142857, 15.0, 4.166666666666666, 0.0, 18.75, 0.0])
line_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt_6 = np.array([6.25, 0.0, 0.0, 25.0, 14.285714285714285, 55.00000000000001, 12.5, 35.0, 25.0, 10.0])
occupancy_jpg_6 = np.array([18.75, 5.555555555555555, 4.411764705882353, 14.285714285714285, 7.142857142857142, 5.0, 4.166666666666666, 0.0, 9.375, 5.0])
occupancy_json_6 = np.array([56.25, 100.0, 100.0, 7.142857142857142, 100.0, 100.0, 100.0, 100.0, 100.0, 37.5])
occupancy_tokenized_txt_6 = np.array([100.0, 100.0, 51.470588235294116, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 6x6
avg_line_adj_json_6 = np.mean(line_adj_json_6)
avg_line_adj_txt_6 = np.mean(line_adj_txt_6)
avg_line_jpg_6 = np.mean(line_jpg_6)
avg_line_json_6 = np.mean(line_json_6)
avg_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
avg_occupancy_json_6 = np.mean(occupancy_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_R_allo_line_adj_json_6 = np.std(line_adj_json_6)
# sd_R_allo_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_R_allo_line_jpg_6 = np.std(line_jpg_6)
# sd_R_allo_line_json_6 = np.std(line_json_6)
# sd_R_allo_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_R_allo_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_R_allo_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_R_allo_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_R_allo_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_R_allo_occupancy_json_6 = np.std(occupancy_json_6)
# sd_R_allo_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy R Allo 15x15
line_adj_json_15 = np.array([46.92307692307692, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt_15 = np.array([7.6923076923076925, 100.0, 53.62318840579711, 100.0, 0.7936507936507936, 98.0, 100.0, 2.564102564102564, 58.333333333333336, 100.0])
line_jpg_15 = np.array([0.7692307692307693, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
line_json_15 = np.array([27.692307692307693, 14.705882352941178, 10.144927536231885, 12.5, 9.523809523809524, 26.0, 19.696969696969695, 29.48717948717949, 1.5151515151515151, 32.608695652173914])
line_tokenized_txt_15 = np.array([33.07692307692307, 39.705882352941174, 7.971014492753622, 5.357142857142857, 39.682539682539684, 100.0, 100.0, 50.0, 60.60606060606061, 100.0])
occupancy_adj_json_15 = np.array([46.15384615384615, 100.0, 38.405797101449274, 100.0, 34.523809523809526, 100.0, 100.0, 100.0, 71.21212121212122, 100.0])
occupancy_adj_txt_15 = np.array([27.692307692307693, 100.0, 7.246376811594203, 14.285714285714285, 9.126984126984127, 77.0, 25.757575757575758, 67.94871794871796, 39.39393939393939, 100.0])
occupancy_ascii_txt_15 = np.array([1.5384615384615385, 5.88235294117647, 0.0, 0.0, 0.0, 0.0, 3.0303030303030303, 1.282051282051282, 1.5151515151515151, 0.0])
occupancy_jpg_15 = np.array([1.153846153846154, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
occupancy_json_15 = np.array([0.38461538461538464, 27.941176470588236, 5.797101449275362, 39.285714285714285, 3.1746031746031744, 7.000000000000001, 3.0303030303030303, 0.0, 3.0303030303030303, 7.608695652173914])
occupancy_tokenized_txt_15 = np.array([25.384615384615383, 100.0, 4.3478260869565215, 100.0, 50.79365079365079, 10.0, 18.181818181818183, 61.53846153846154, 0.7575757575757576, 100.0])
# Averages and std deviation 15x15
avg_line_adj_json_15 = np.mean(line_adj_json_15)
avg_line_adj_txt_15 = np.mean(line_adj_txt_15)
avg_line_jpg_15 = np.mean(line_jpg_15)
avg_line_json_15 = np.mean(line_json_15)
avg_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
avg_occupancy_json_15 = np.mean(occupancy_json_15)
avg_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_R_allo_line_adj_json_15 = np.std(line_adj_json_15)
# sd_R_allo_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_R_allo_line_jpg_15 = np.std(line_jpg_15)
# sd_R_allo_line_json_15 = np.std(line_json_15)
# sd_R_allo_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_R_allo_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_R_allo_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_R_allo_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_R_allo_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_R_allo_occupancy_json_15 = np.std(occupancy_json_15)
# sd_R_allo_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Pro, Allocentric Output", fontsize=16, pad=20)

sample_sizes_3x3_R_allo = [
    sample_size(np.std(line_adj_json)),
    sample_size(np.std(line_adj_txt)),
    sample_size(np.std(line_jpg)),
    sample_size(np.std(line_json)),
    sample_size(np.std(line_tokenized_txt)),
    sample_size(np.std(occupancy_adj_json)),
    sample_size(np.std(occupancy_adj_txt)),
    sample_size(np.std(occupancy_ascii_txt)),
    sample_size(np.std(occupancy_jpg)),
    sample_size(np.std(occupancy_json)),
    sample_size(np.std(occupancy_tokenized_txt))
    ]
sample_sizes_6x6_R_allo=[
    sample_size(np.std(line_adj_json_6)),
    sample_size(np.std(line_adj_txt_6)),
    sample_size(np.std(line_jpg_6)),
    sample_size(np.std(line_json_6)),
    sample_size(np.std(line_tokenized_txt_6)),
    sample_size(np.std(occupancy_adj_json_6)),
    sample_size(np.std(occupancy_adj_txt_6)),
    sample_size(np.std(occupancy_ascii_txt_6)),
    sample_size(np.std(occupancy_jpg_6)),
    sample_size(np.std(occupancy_json_6)),
    sample_size(np.std(occupancy_tokenized_txt_6)) ]
sample_sizes_15x15_R_allo=[
    sample_size(np.std(line_adj_json_15)),
    sample_size(np.std(line_adj_txt_15)),
    sample_size(np.std(line_jpg_15)),
    sample_size(np.std(line_json_15)),
    sample_size(np.std(line_tokenized_txt_15)),
    sample_size(np.std(occupancy_adj_json_15)),
    sample_size(np.std(occupancy_adj_txt_15)),
    sample_size(np.std(occupancy_ascii_txt_15)),
     sample_size(np.std(occupancy_jpg_15)),
    sample_size(np.std(occupancy_json_15)),
    sample_size(np.std(occupancy_tokenized_txt_15)) ]

# # R -- Ego -- accuracy scores ----------- 3x3, 6x6 & 15x15 -----------------------------------
# Accuracy R Ego 3x3
line_adj_json = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt = np.array([25.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg = np.array([25.0, 0.0, 50.0, 50.0, 33.33333333333333, 0.0, 0.0, 100.0, 16.666666666666664, 110.00000000000001])
line_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 100.0, 100.0, 75.0])
occupancy_jpg = np.array([12.5, 0.0, 0.0, 50.0, 33.33333333333333, 0.0, 12.5, 91.66666666666666, 8.333333333333332, 37.5])
occupancy_json = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_tokenized_txt = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
# Averages and std deviation 3x3
avg_line_adj_json = np.mean(line_adj_json)
avg_line_adj_txt = np.mean(line_adj_txt)
avg_line_jpg = np.mean(line_jpg)
avg_line_json = np.mean(line_json)
avg_line_tokenized_txt = np.mean(line_tokenized_txt)
avg_occupancy_adj_json = np.mean(occupancy_adj_json)
avg_occupancy_adj_txt = np.mean(occupancy_adj_txt)
avg_occupancy_ascii_txt = np.mean(occupancy_ascii_txt)  
avg_occupancy_jpg = np.mean(occupancy_jpg)
avg_occupancy_json = np.mean(occupancy_json)
avg_occupancy_tokenized_txt = np.mean(occupancy_tokenized_txt)
# sd_R_ego_line_adj_json = np.std(line_adj_json)
# sd_R_ego_line_adj_txt = np.std(line_adj_txt)
# sd_R_ego_line_jpg = np.std(line_jpg)
# sd_R_ego_line_json = np.std(line_json)
# sd_R_ego_line_tokenized_txt = np.std(line_tokenized_txt)
# sd_R_ego_occupancy_adj_json = np.std(occupancy_adj_json)
# sd_R_ego_occupancy_adj_txt = np.std(occupancy_adj_txt)
# sd_R_ego_occupancy_ascii_txt = np.std(occupancy_ascii_txt)  
# sd_R_ego_occupancy_jpg = np.std(occupancy_jpg)
# sd_R_ego_occupancy_json = np.std(occupancy_json)
# sd_R_ego_occupancy_tokenized_txt = np.std(occupancy_tokenized_txt)
# Accuracy R Ego 6x6
line_adj_json_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_adj_txt_6 = np.array([100.0, 5.555555555555555, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
line_jpg_6 = np.array([12.5, 11.11111111111111, 0.0, 0.0, 21.428571428571427, 0.0, 4.166666666666666, 0.0, 31.25, 0.0])
line_json_6 = np.array([100.0, 16.666666666666664, 100.0, 100.0, 100.0, 100.0, 83.33333333333334, 100.0, 6.25, 100.0])
line_tokenized_txt_6 = np.array([100.0, 100.0, 38.23529411764706, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_adj_json_6 = np.array([100.0, 100.0, 110.00000000000001, 100.0, 100.0, 100.0, 100.0, 0.0, 100.0, 100.0])
occupancy_adj_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
occupancy_ascii_txt_6 = np.array([12.5, 33.33333333333333, 0.0, 17.857142857142858, 28.57142857142857, 5.0, 10.416666666666668, 35.0, 0.0, 10.0])
occupancy_jpg_6 = np.array([6.25, 16.666666666666664, 5.88235294117647, 0.0, 21.428571428571427, 2.5, 12.5, 50.0, 12.5, 0.0])
occupancy_json_6 = np.array([100.0, 100.0, 8.823529411764707, 17.857142857142858, 100.0, 90.0, 100.0, 100.0, 56.25, 10.0])
occupancy_tokenized_txt_6 = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 29.166666666666668, 100.0, 100.0, 100.0])
# Averages and std deviation 6x6
avg_line_adj_json_6 = np.mean(line_adj_json_6)
avg_line_adj_txt_6 = np.mean(line_adj_txt_6)
avg_line_jpg_6 = np.mean(line_jpg_6)
avg_line_json_6 = np.mean(line_json_6)
avg_line_tokenized_txt_6 = np.mean(line_tokenized_txt_6)
avg_occupancy_adj_json_6 = np.mean(occupancy_adj_json_6)
avg_occupancy_adj_txt_6 = np.mean(occupancy_adj_txt_6)
avg_occupancy_ascii_txt_6 = np.mean(occupancy_ascii_txt_6)  
avg_occupancy_jpg_6 = np.mean(occupancy_jpg_6)
avg_occupancy_json_6 = np.mean(occupancy_json_6)
avg_occupancy_tokenized_txt_6 = np.mean(occupancy_tokenized_txt_6)
# sd_R_ego_line_adj_json_6 = np.std(line_adj_json_6)
# sd_R_ego_line_adj_txt_6 = np.std(line_adj_txt_6)
# sd_R_ego_line_jpg_6 = np.std(line_jpg_6)
# sd_R_ego_line_json_6 = np.std(line_json_6)
# sd_R_ego_line_tokenized_txt_6 = np.std(line_tokenized_txt_6)
# sd_R_ego_occupancy_adj_json_6 = np.std(occupancy_adj_json_6)
# sd_R_ego_occupancy_adj_txt_6 = np.std(occupancy_adj_txt_6)
# sd_R_ego_occupancy_ascii_txt_6 = np.std(occupancy_ascii_txt_6)  
# sd_R_ego_occupancy_jpg_6 = np.std(occupancy_jpg_6)
# sd_R_ego_occupancy_json_6 = np.std(occupancy_json_6)
# sd_R_ego_occupancy_tokenized_txt_6 = np.std(occupancy_tokenized_txt_6)
# Accuracy R Ego 15x15
line_adj_json_15 = np.array([3.076923076923077, 100.0, 15.217391304347828, 100.0, 35.714285714285715, 100.0, 100.0, 100.0, 62.121212121212125, 100.0])
line_adj_txt_15 = np.array([2.307692307692308, 20.588235294117645, 0.7246376811594203, 100.0, 0.0, 11.0, 0.0, 0.0, 46.21212121212121, 0.0])
line_jpg_15 = np.array([0.7692307692307693, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5151515151515151, 0.0])
line_json_15 = np.array([3.076923076923077, 36.76470588235294, 9.420289855072465, 0.0, 14.285714285714285, 26.0, 18.181818181818183, 7.6923076923076925, 7.575757575757576, 30.434782608695656])
line_tokenized_txt_15 = np.array([1.5384615384615385, 29.411764705882355, 1.4492753623188406, 100.0, 0.0, 0.0, 100.0, 100.0, 0.7575757575757576, 100.0])
occupancy_adj_json_15 = np.array([34.23076923076923, 38.23529411764706, 10.869565217391305, 100.0, 0.0, 36.0, 65.15151515151516, 50.0, 0.7575757575757576, 100.0])
occupancy_adj_txt_15 = np.array([1.5384615384615385, 41.17647058823529, 13.768115942028986, 0.0, 0.0, 0.0, 26.515151515151516, 100.0, 5.303030303030303, 14.130434782608695])
occupancy_ascii_txt_15 = np.array([0.7692307692307693, 6.61764705882353, 0.36231884057971014, 4.464285714285714, 3.1746031746031744, 5.5, 0.0, 0.0, 0.3787878787878788, 4.3478260869565215])
occupancy_jpg_15 = np.array([1.5384615384615385, 1.4705882352941175, 1.4492753623188406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7575757575757576, 0.0])
occupancy_json_15 = np.array([3.8461538461538463, 5.88235294117647, 2.1739130434782608, 10.714285714285714, 15.873015873015872, 0.0, 10.606060606060606, 6.41025641025641, 1.5151515151515151, 10.869565217391305])
occupancy_tokenized_txt_15 = np.array([27.307692307692307, 48.529411764705884, 5.797101449275362, 0.0, 2.380952380952381, 3.5000000000000004, 39.39393939393939, 23.076923076923077, 6.0606060606060606, 15.217391304347828])
# Averages and std deviation 15x15
avg_line_adj_json_15 = np.mean(line_adj_json_15)
avg_line_adj_txt_15 = np.mean(line_adj_txt_15)
avg_line_jpg_15 = np.mean(line_jpg_15)
avg_line_json_15 = np.mean(line_json_15)
avg_line_tokenized_txt_15 = np.mean(line_tokenized_txt_15)
avg_occupancy_adj_json_15 = np.mean(occupancy_adj_json_15)
avg_occupancy_adj_txt_15 = np.mean(occupancy_adj_txt_15)
avg_occupancy_ascii_txt_15 = np.mean(occupancy_ascii_txt_15)  
avg_occupancy_jpg_15 = np.mean(occupancy_jpg_15)
avg_occupancy_json_15 = np.mean(occupancy_json_15)
# avg_occupancy_tokenized_txt_15 = np.mean(occupancy_tokenized_txt_15)
# sd_R_ego_line_adj_json_15 = np.std(line_adj_json_15)
# sd_R_ego_line_adj_txt_15 = np.std(line_adj_txt_15)
# sd_R_ego_line_jpg_15 = np.std(line_jpg_15)
# sd_R_ego_line_json_15 = np.std(line_json_15)
# sd_R_ego_line_tokenized_txt_15 = np.std(line_tokenized_txt_15)
# sd_R_ego_occupancy_adj_json_15 = np.std(occupancy_adj_json_15)
# sd_R_ego_occupancy_adj_txt_15 = np.std(occupancy_adj_txt_15)
# sd_R_ego_occupancy_ascii_txt_15 = np.std(occupancy_ascii_txt_15)  
# sd_R_ego_occupancy_jpg_15 = np.std(occupancy_jpg_15)
# sd_R_ego_occupancy_json_15 = np.std(occupancy_json_15)
# sd_R_ego_occupancy_tokenized_txt_15 = np.std(occupancy_tokenized_txt_15)

sample_sizes_3x3_R_ego = [
    sample_size(np.std(line_adj_json)),
    sample_size(np.std(line_adj_txt)),
    sample_size(np.std(line_jpg)),
    sample_size(np.std(line_json)),
    sample_size(np.std(line_tokenized_txt)),
    sample_size(np.std(occupancy_adj_json)),
    sample_size(np.std(occupancy_adj_txt)),
    sample_size(np.std(occupancy_ascii_txt)),
    sample_size(np.std(occupancy_jpg)),
    sample_size(np.std(occupancy_json)),
    sample_size(np.std(occupancy_tokenized_txt))
    ]
sample_sizes_6x6_R_ego=[
    sample_size(np.std(line_adj_json_6)),
    sample_size(np.std(line_adj_txt_6)),
    sample_size(np.std(line_jpg_6)),
    sample_size(np.std(line_json_6)),
    sample_size(np.std(line_tokenized_txt_6)),
    sample_size(np.std(occupancy_adj_json_6)),
    sample_size(np.std(occupancy_adj_txt_6)),
    sample_size(np.std(occupancy_ascii_txt_6)),
    sample_size(np.std(occupancy_jpg_6)),
    sample_size(np.std(occupancy_json_6)),
    sample_size(np.std(occupancy_tokenized_txt_6)) ]
sample_sizes_15x15_R_ego=[
    sample_size(np.std(line_adj_json_15)),
    sample_size(np.std(line_adj_txt_15)),
    sample_size(np.std(line_jpg_15)),
    sample_size(np.std(line_json_15)),
    sample_size(np.std(line_tokenized_txt_15)),
    sample_size(np.std(occupancy_adj_json_15)),
    sample_size(np.std(occupancy_adj_txt_15)),
    sample_size(np.std(occupancy_ascii_txt_15)),
     sample_size(np.std(occupancy_jpg_15)),
    sample_size(np.std(occupancy_json_15)),
    sample_size(np.std(occupancy_tokenized_txt_15)) ]


# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis("off")
# plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%) - Gemini 2.5 Pro, Egocentric Output", fontsize=16, pad=20)


# --------- Plot a table showing required sample sizes and standard deviations for all complexities, output types and  ----------------------

# n_line_jpg_3 = sample_size(sd_line_jpg)
# n_occupancy_jpg_3 = sample_size(sd_occupancy_jpg)
# n_line_tokenized_txt_3 = sample_size(sd_line_tokenized_txt)
# n_occupancy_tokenized_txt_3 = sample_size(sd_occupancy_tokenized_txt)
# n_line_json_3 = sample_size(sd_line_json)
# n_occupancy_json_3 = sample_size(sd_occupancy_json)
# n_line_adj_txt_3 = sample_size(sd_line_adj_txt)
# n_occupancy_adj_txt_3 = sample_size(sd_occupancy_adj_txt)
# n_line_adj_json_3 = sample_size(sd_line_adj_json)
# n_occupancy_adj_json_3 = sample_size(sd_occupancy_adj_json)
# n_occupancy_ascii_txt_3 = sample_size(sd_occupancy_ascii_txt)
# n_line_jpg_6 = sample_size(sd_line_jpg_6)
# n_occupancy_jpg_6 = sample_size(sd_occupancy_jpg_6)
# n_line_tokenized_txt_6 = sample_size(sd_line_tokenized_txt_6)
# n_occupancy_tokenized_txt_6 = sample_size(sd_occupancy_tokenized_txt_6)
# n_line_json_6 = sample_size(sd_line_json_6)
# n_occupancy_json_6 = sample_size(sd_occupancy_json_6)
# n_line_adj_txt_6 = sample_size(sd_line_adj_txt_6)
# n_occupancy_adj_txt_6 = sample_size(sd_occupancy_adj_txt_6)
# n_line_adj_json_6 = sample_size(sd_line_adj_json_6)
# n_occupancy_adj_json_6 = sample_size(sd_occupancy_adj_json_6)
# n_occupancy_ascii_txt_6 = sample_size(sd_occupancy_ascii_txt_6) 
# n_line_jpg_15 = sample_size(sd_line_jpg_15)
# n_occupancy_jpg_15 = sample_size(sd_occupancy_jpg_15)
# n_line_tokenized_txt_15 = sample_size(sd_line_tokenized_txt_15)
# n_occupancy_tokenized_txt_15 = sample_size(sd_occupancy_tokenized_txt_15)
# n_line_json_15 = sample_size(sd_line_json_15)
# n_occupancy_json_15 = sample_size(sd_occupancy_json_15)
# n_line_adj_txt_15 = sample_size(sd_line_adj_txt_15)
# n_occupancy_adj_txt_15 = sample_size(sd_occupancy_adj_txt_15)
# n_line_adj_json_15 = sample_size(sd_line_adj_json_15)
# n_occupancy_adj_json_15 = sample_size(sd_occupancy_adj_json_15)
# n_occupancy_ascii_txt_15 = sample_size(sd_occupancy_ascii_txt_15) 

representations = [
    "Line Adj JSON",
    "Line Adj TXT",
    "Line JPG",
    "Line JSON",
    "Line Tokenized TXT",
    "Occupancy Adj JSON",
    "Occupancy Adj TXT",
    "Occupancy ASCII TXT",
    "Occupancy JPG",
    "Occupancy JSON",
    "Occupancy Tokenized TXT"
]

# sample_sizes_3x3 = [
#     n_line_jpg_3 ,
#     n_line_json_3,
#     n_line_adj_json_3,
#     n_line_adj_txt_3,
#     n_line_tokenized_txt_3,
#     n_occupancy_jpg_3,
#     n_occupancy_json_3,
#     n_occupancy_adj_json_3,
#     n_occupancy_adj_txt_3,
#     n_occupancy_ascii_txt_3,
#     n_occupancy_tokenized_txt_3 
#     ]
# sample_sizes_6x6=[
#     n_line_jpg_6 ,
#     n_line_json_6,
#     n_line_adj_json_6,
#     n_line_adj_txt_6,
#     n_line_tokenized_txt_6,
#     n_occupancy_jpg_6,
#     n_occupancy_json_6,
#     n_occupancy_adj_json_6,
#     n_occupancy_adj_txt_6,
#     n_occupancy_ascii_txt_6,
#     n_occupancy_tokenized_txt_6 ]
# sample_sizes_15x15=[
#     n_line_jpg_15,
#     n_line_json_15,
#     n_line_adj_json_15,
#     n_line_adj_txt_15,
#     n_line_tokenized_txt_15,
#     n_occupancy_jpg_15,
#     n_occupancy_json_15,
#     n_occupancy_adj_json_15,
#     n_occupancy_adj_txt_15,
#     n_occupancy_ascii_txt_15,
#     n_occupancy_tokenized_txt_15 ]


# std_3x3 = [
#     sd_line_jpg,
#     sd_line_json,        
#     sd_line_adj_json,
#     sd_line_adj_txt,
#     sd_line_tokenized_txt,
#     sd_occupancy_jpg,
#     sd_occupancy_json,
#     sd_occupancy_adj_json,
#     sd_occupancy_adj_txt,
#     sd_occupancy_ascii_txt,
#     sd_occupancy_tokenized_txt]

# std_6x6 = [
#     sd_line_jpg_6,
#     sd_line_json_6,        
#     sd_line_adj_json_6,
#     sd_line_adj_txt_6,
#     sd_line_tokenized_txt_6,
#     sd_occupancy_jpg_6,
#     sd_occupancy_json_6,
#     sd_occupancy_adj_json_6,
#     sd_occupancy_adj_txt_6,
#     sd_occupancy_ascii_txt_6,
#     sd_occupancy_tokenized_txt_6]
# std_15x15 = [
#     sd_line_jpg_15,
#     sd_line_json_15,        
#     sd_line_adj_json_15,
#     sd_line_adj_txt_15,
#     sd_line_tokenized_txt_15,
#     sd_occupancy_jpg_15,
#     sd_occupancy_json_15,
#     sd_occupancy_adj_json_15,
#     sd_occupancy_adj_txt_15,
#     sd_occupancy_ascii_txt_15,
#     sd_occupancy_tokenized_txt_15]

df = pd.DataFrame({
    "Representation": representations,
    "Sample Size Coordinates, \n Reasoning": sample_sizes_3x3_R_coords,
    "Sample Size Allocentric, \n Reasoning": sample_sizes_3x3_R_allo,
    "Sample Size Egocentric, \n Reasoning": sample_sizes_3x3_R_ego,
    "Sample Size Coordinates, \n Non-Reasoning": sample_sizes_3x3_NR_coords,
    "Sample Size Allocentric, \n Non-Reasoning": sample_sizes_3x3_NR_allo,
    "Sample Size Egocentric, \n Non-Reasoning": sample_sizes_3x3_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 3x3 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Types", fontsize=16, pad=20)


table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.0)

plt.tight_layout()
plt.show()


df = pd.DataFrame({
    "Representation": representations,

    "Sample Size Coordinates, \n Reasoning": sample_sizes_6x6_R_coords,
    "Sample Size Allocentric, \n Reasoning": sample_sizes_6x6_R_allo,
    "Sample Size Egocentric, \n Reasoning": sample_sizes_6x6_R_ego,
    "Sample Size Coordinates, \n Non-Reasoning": sample_sizes_6x6_NR_coords,
    "Sample Size Allocentric, \n Non-Reasoning": sample_sizes_6x6_NR_allo,
    "Sample Size Egocentric, \n Non-Reasoning": sample_sizes_6x6_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 6x6 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Types", fontsize=16, pad=20)


table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.0)

plt.tight_layout()
plt.show()


df = pd.DataFrame({
    "Representation": representations,
    "Sample Size Coordinates, \n Reasoning": sample_sizes_15x15_R_coords,
    "Sample Size Allocentric, \n Reasoning": sample_sizes_15x15_R_allo,
    "Sample Size Egocentric, \n Reasoning": sample_sizes_15x15_R_ego,
    "Sample Size Coordinates, \n Non-Reasoning": sample_sizes_15x15_NR_coords,
    "Sample Size Allocentric, \n Non-Reasoning": sample_sizes_15x15_NR_allo,
    "Sample Size Egocentric, \n Non-Reasoning": sample_sizes_15x15_NR_ego
})

# Create table image
fig, ax = plt.subplots(figsize=(30, 8))
ax.axis("off")
plt.title("Required Sample Sizes for Desired Statistical Power (α=0.05, error margin = 5%), \n 15x15 Maze, Gemini 2.5 Pro and Flash-Lite, All Output Types", fontsize=16, pad=20)


table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(True)
# table.set_fontsize(10)
table.scale(1.2, 2.0)

plt.tight_layout()
plt.show()