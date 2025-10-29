import numpy as np
import matplotlib.pyplot as plt


def normalization(vector, mean, sigma):
    ascii_standardized= np.zeros(30)
    for i in range(1,30):
        value = vector[i-1]
        z = (value-mean)/sigma
        ascii_standardized[i-1]=z
    return ascii_standardized


#------------- TEST 1 - NON REASONING, BEV ----------------------------------
type = 'BEV'
LLM = 'nonreasoning'
line_ascii_1 = np.array([0.0, 5.0, 10.0, 37.5, 10.0, 12.5, 110.00000000000001, 0.0, 0.0, 13.636363636363635, 0.0, 0.0, 0.0, 10.0, 7.142857142857142, 4.545454545454546, 8.333333333333332, 0.0, 0.0, 5.555555555555555, 0.0, 0.0, 50.0, 0.0, 0.0, 8.333333333333332, 12.5, 0.0, 0.0, 0.0], dtype=float)
line_ascii_bewerkt_1 = np.array([0.0, 5.0, 10.0, 37.5, 10.0, 12.5, 0, 0.0, 0.0, 13.636363636363635, 0.0, 0.0, 0.0, 10.0, 7.142857142857142, 4.545454545454546, 8.333333333333332, 0.0, 0.0, 5.555555555555555, 0.0, 0.0, 50.0, 0.0, 0.0, 8.333333333333332, 12.5, 0.0, 0.0, 0.0], dtype=float)
mean_1 = np.mean(line_ascii_bewerkt_1)
sigma_1 = np.std(line_ascii_bewerkt_1)
standardized_1 = normalization(line_ascii_bewerkt_1, mean_1, sigma_1 )



#------------- TEST 2 - NON REASONING, EGO ----------------------------------
type = 'EGO'
LLM = 'nonreasoning'
line_ascii_2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.333333333333332, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
line_ascii_bewerkt_2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.333333333333332, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
test2_mean = np.mean(line_ascii_bewerkt_2)
mean_2 = np.mean(line_ascii_bewerkt_2)
sigma_2 = np.std(line_ascii_bewerkt_2)
standardized_2 = normalization(line_ascii_bewerkt_2, mean_2, sigma_2 )
count=0
for i in range(1,31):
    if line_ascii_bewerkt_2[i-1]==0:
        count+=1
# print ('zero count is:', count)
# print('mean test 2 is:', mean_2)

#------------- TEST 3 - NON REASONING, COORDINATES ----------------------------------
type = 'COORDS'
LLM = 'nonreasoning'
line_ascii_3 = np.array([20.0, 14.285714285714285, 18.181818181818183, 11.11111111111111, 9.090909090909092, 22.22222222222222, 13.333333333333334, 7.6923076923076925, 7.6923076923076925, 17.391304347826086, 4.3478260869565215, 5.263157894736842, 20.0, 36.36363636363637, 13.333333333333334, 8.695652173913043, 7.6923076923076925, 11.76470588235294, 17.647058823529413, 5.263157894736842, 10.526315789473683, 61.53846153846154, 84.61538461538461, 21.052631578947366, 27.27272727272727, 7.6923076923076925, 17.647058823529413, 6.666666666666667, 9.090909090909092, 14.285714285714285], dtype=float)
line_ascii_bewerkt_3 = line_ascii_3
mean_3 = np.mean(line_ascii_bewerkt_3)
sigma_3 = np.std(line_ascii_bewerkt_3)
standardized_3 = normalization(line_ascii_bewerkt_3, mean_3, sigma_3 )



#------------- TEST 4 - REASONING, BEV ----------------------------------
type = 'BEV'
LLM = 'reasoning'
line_ascii_4 = np.array([14.29, 0.0, 0.0, 0.0, 20.0, 12.5, 28.57142857142857, 0.0, 0.0, 13.636363636363635, 0.0, 5.555555555555555, 28.57142857142857, 10.0, 14.285714285714285, 9.090909090909092, 25.0, 6.25, 6.25, 0.0, 5.555555555555555, 66.66666666666666, 75.0, 0.0, 0.0, 25.0, 25.0, 7.142857142857142, 10.0, 0.0], dtype=float)
line_ascii_bewerkt_4 = line_ascii_4
mean_4 = np.mean(line_ascii_bewerkt_4)
sigma_4 = np.std(line_ascii_bewerkt_4)
standardized_4 = normalization(line_ascii_bewerkt_4, mean_4, sigma_4 )

#------------- TEST 5 - REASONING, EGO ----------------------------------
type = 'EGO'
LLM = 'reasoning'
line_ascii_5 = np.array([0.0, 5.0, 0.0, 62.5, 10.0, 37.5, 7.14285714, 8.33333333, 8.33333333, 45.45454545, 4.54545455, 11.11111111, 0.0, 30.0, 42.857142856, 0.0, 0.0, 0.0, 100.0, 16.666666666666664, 0.0, 0.0, 0.0, 5.555555555555555, 10.0, 0.0, 6.25, 21.428571428571427, 0.0, 0.0], dtype=float)
line_ascii_bewerkt_5 = line_ascii_5
mean_5 = np.mean(line_ascii_bewerkt_5)
sigma_5 = np.std(line_ascii_bewerkt_5)
standardized_5 = normalization(line_ascii_bewerkt_5, mean_5, sigma_5 )
print('stddev 5:', sigma_5)


#------------- TEST 6 - REASONING, COORDINATES ----------------------------------
type = 'COORDS'
LLM = 'reasoning'
line_ascii_6 = np.array([33.33333333333333, 4.761904761904762, 9.090909090909092, 44.44444444444444, 18.181818181818183, 22.22222222222222, 20.0, 7.6923076923076925, 7.6923076923076925, 4.3478260869565215, 43.47826086956522, 36.84210526315789, 33.33333333333333, 18.181818181818183, 6.666666666666667, 4.3478260869565215, 23.076923076923077, 100.0, 17.647058823529413, 5.263157894736842, 10.526315789473683, 38.46153846153847, 76.92307692307693, 5.263157894736842, 9.090909090909092, 7.6923076923076925, 11.76470588235294, 26.666666666666668, 18.181818181818183, 9.523809523809524], dtype=float)
line_ascii_bewerkt_6 = line_ascii_6
mean_6 = np.mean(line_ascii_bewerkt_6)
sigma_6 = np.std(line_ascii_bewerkt_6)
standardized_6 = normalization(line_ascii_bewerkt_6, mean_6, sigma_6 )
print('differences:', line_ascii_bewerkt_6 - line_ascii_bewerkt_5)
#------------- Accuracy - Output Token Count grapher ----------------------------------
# Test_1_tokencount = np.array([ 35.0,  41.0,  25.0,  39.0,  37.0,  23.0, 4000.0,  21.0,  27.0,  39.0, 4000.0,  79.0, 4000.0,  21.0,  27.0,  23.0,  25.0,  19.0,  23.0,  31.0,  23.0,  53.0,  23.0, 4000.0, 39.0,  37.0,  19.0,  21.0,  27.0,  65.0], dtype=float)
# Test_2_tokencount = np.array([ 27.0,  27.0,  39.0,4000.0,4000.0,4000.0,  53.0,  35.0,  63.0,  23.0,  37.0,  53.0, 29.0,  35.0,4000.0,  31.0,  31.0,  37.0,4000.0,  35.0,4000.0,4000.0,  45.0,  31.0, 29.0,  51.0,  33.0,  33.0,  41.0,  35.0], dtype=float)
# Test_3_tokencount = np.array([ 53.0, 37.0, 45.0, 37.0, 37.0, 45.0, 53.0, 37.0, 37.0, 37.0, 37.0, 53.0, 37.0, 37.0, 45.0, 53.0, 37.0, 37.0, 37.0, 45.0, 45.0, 77.0, 97.0, 37.0, 37.0, 37.0, 37.0, 45.0, 37.0, 37.0], dtype=float)
# Test_4_tokencount = np.array([ 3841.0,  4167.0,  1223.0, 17898.0,  9577.0,  1142.0,  1155.0, 12058.0,  6796.0,  6787.0, 15697.0,   794.0,  1474.0,  1175.0,  5727.0,  3981.0,  1627.0,  1499.0,  2577.0,  1389.0, 2304.0,  4567.0,  3502.0, 10176.0,  2755.0,  4811.0,  3994.0,  2262.0,  2060.0,  3109.0], dtype=float)
# Test_5_tokencount = np.array([ 5467.0,  9446.0,  2525.0,  1681.0, 10656.0,  9506.0,  2900.0,  6304.0,  3111.0, 18679.0, 2624.0,  8272.0,  4353.0, 10793.0,  8148.0,  2906.0,  2325.0,  5675.0, 12708.0,  3044.0,  6816.0,  3265.0,  4806.0,  5164.0,  3844.0,  3319.0,  7215.0,  1845.0,  7101.0, 18284.0], dtype=float)
# Test_6_tokencount = np.array([ 6544.0,  856.0, 1832.0, 2077.0, 6442.0,  869.0, 4030.0, 3655.0, 1325.0, 3833.0, 5885.0,  887.0, 1485.0, 1808.0, 2421.0, 2865.0, 2349.0, 9657.0, 4168.0, 2373.0, 6373.0, 1462.0, 12117.0, 4654.0,21185.0, 4464.0, 1781.0,  955.0, 5615.0, 1528.0], dtype=float)

# mean_tc1 = np.mean(Test_1_tokencount)
# mean_tc2 = np.mean(Test_2_tokencount)
# mean_tc3 = np.mean(Test_3_tokencount)
# mean_tc4 = np.mean(Test_4_tokencount)
# mean_tc5 = np.mean(Test_5_tokencount)
# mean_tc6 = np.mean(Test_6_tokencount)

# sigma_tc1 = np.std(Test_1_tokencount)
# sigma_tc2 = np.std(Test_2_tokencount)
# sigma_tc3 = np.std(Test_3_tokencount)
# sigma_tc4 = np.std(Test_4_tokencount)
# sigma_tc5 = np.std(Test_5_tokencount)
# sigma_tc6 = np.std(Test_6_tokencount)


# print(f'test1: ({mean_tc1}, {mean_1}), deviations: ({sigma_tc1},{sigma_1})')
# print(f'test2: ({mean_tc2}, {mean_2}), deviations: ({sigma_tc2},{sigma_2})')
# print(f'test3: ({mean_tc3}, {mean_3}), deviations: ({sigma_tc3},{sigma_3})')
# print(f'test4: ({mean_tc4}, {mean_4}), deviations: ({sigma_tc4},{sigma_4})')
# print(f'test5: ({mean_tc5}, {mean_5}), deviations: ({sigma_tc5},{sigma_5})')
# print(f'test6: ({mean_tc6}, {mean_6}), deviations: ({sigma_tc6},{sigma_6})')

# # Combine for easy looping
# tests = [
#     (mean_tc1, mean_1, sigma_tc1, sigma_1, 'g', 'Test 1: Gemini 2.5 Flash Lite'),
#     (mean_tc2, mean_2, sigma_tc2, sigma_2, 'b', 'Test 2: Gemini 2.5 Flash Lite'),
#     (mean_tc3, mean_3, sigma_tc3, sigma_3, 'c', 'Test 3: Gemini 2.5 Flash Lite'),
#     (mean_tc4, mean_4, sigma_tc4, sigma_4, 'm', 'Test 4: Gemini 2.5 Pro'),
#     (mean_tc5, mean_5, sigma_tc5, sigma_5, 'y', 'Test 5: Gemini 2.5 Pro'),
#     (mean_tc6, mean_6, sigma_tc6, sigma_6, 'k', 'Test 6: Gemini 2.5 Pro'),
# ]

# # === Plot setup ===
# plt.figure(figsize=(7, 5))

# # Plot each test with horizontal and vertical error bars
# for mean_tc, mean_acc, sigma_tc, sigma_acc, color, label in tests:
#     # Create the errorbar (both xerr and yerr)
#     (_, _, bars) = plt.errorbar(
#         mean_tc, mean_acc,
#         xerr=sigma_tc, yerr=sigma_acc,
#         fmt='o', markersize=8, markeredgecolor='black',
#         color=color, ecolor=color,
#         elinewidth=1.5, capsize=4,
#         alpha=0.7, label=label
#     )
#     # Make both vertical and horizontal error bars dashed and transparent
#     for bar in bars:
#         bar.set_linestyle(':')
#         bar.set_alpha(0.5)

# # === Labels, title, grid, legend ===
# plt.title('Mean Accuracy vs Mean Output Token Count (30 Runs Per Test)', fontsize=13)
# plt.xlabel('Mean Output Token Count', fontsize=11)
# plt.ylabel('Mean Accuracy (%)', fontsize=11)

# plt.grid(linestyle=':', linewidth=0.6, alpha=0.8)
# plt.legend(
#     loc='center left',
#     bbox_to_anchor=(1.02, 0.5),
#     frameon=False,
#     title='Tests',
#     fontsize=9,
#     title_fontsize=10
# )
# plt.tight_layout()
# plt.show()



#------------- Output Token Count - Output Type grapher ----------------------------------
# Test_1_tokencount = np.array([ 35.0,  41.0,  25.0,  39.0,  37.0,  23.0, 4000.0,  21.0,  27.0,  39.0, 4000.0,  79.0, 4000.0,  21.0,  27.0,  23.0,  25.0,  19.0,  23.0,  31.0,  23.0,  53.0,  23.0, 4000.0, 39.0,  37.0,  19.0,  21.0,  27.0,  65.0], dtype=float)
# Test_2_tokencount = np.array([ 27.0,  27.0,  39.0,4000.0,4000.0,4000.0,  53.0,  35.0,  63.0,  23.0,  37.0,  53.0, 29.0,  35.0,4000.0,  31.0,  31.0,  37.0,4000.0,  35.0,4000.0,4000.0,  45.0,  31.0, 29.0,  51.0,  33.0,  33.0,  41.0,  35.0], dtype=float)
# Test_3_tokencount = np.array([ 53.0, 37.0, 45.0, 37.0, 37.0, 45.0, 53.0, 37.0, 37.0, 37.0, 37.0, 53.0, 37.0, 37.0, 45.0, 53.0, 37.0, 37.0, 37.0, 45.0, 45.0, 77.0, 97.0, 37.0, 37.0, 37.0, 37.0, 45.0, 37.0, 37.0], dtype=float)
# Test_4_tokencount = np.array([ 3841.0,  4167.0,  1223.0, 17898.0,  9577.0,  1142.0,  1155.0, 12058.0,  6796.0,  6787.0, 15697.0,   794.0,  1474.0,  1175.0,  5727.0,  3981.0,  1627.0,  1499.0,  2577.0,  1389.0, 2304.0,  4567.0,  3502.0, 10176.0,  2755.0,  4811.0,  3994.0,  2262.0,  2060.0,  3109.0], dtype=float)
# Test_5_tokencount = np.array([ 5467.0,  9446.0,  2525.0,  1681.0, 10656.0,  9506.0,  2900.0,  6304.0,  3111.0, 18679.0, 2624.0,  8272.0,  4353.0, 10793.0,  8148.0,  2906.0,  2325.0,  5675.0, 12708.0,  3044.0,  6816.0,  3265.0,  4806.0,  5164.0,  3844.0,  3319.0,  7215.0,  1845.0,  7101.0, 18284.0], dtype=float)
# Test_6_tokencount = np.array([ 6544.0,  856.0, 1832.0, 2077.0, 6442.0,  869.0, 4030.0, 3655.0, 1325.0, 3833.0, 5885.0,  887.0, 1485.0, 1808.0, 2421.0, 2865.0, 2349.0, 9657.0, 4168.0, 2373.0, 6373.0, 1462.0, 12117.0, 4654.0,21185.0, 4464.0, 1781.0,  955.0, 5615.0, 1528.0], dtype=float)

# x_axis = ["Allocentric" , "Egocentric" , "Fixed-World"]
# mean_tc1 = [np.mean(Test_1_tokencount) , np.nan , np.nan]
# mean_tc2 = [np.nan , np.mean(Test_2_tokencount) , np.nan]
# mean_tc3 = [np.nan , np.nan , np.mean(Test_3_tokencount)]
# mean_tc4 = [np.mean(Test_4_tokencount) , np.nan , np.nan]
# mean_tc5 = [np.nan , np.mean(Test_5_tokencount) , np.nan]
# mean_tc6 = [np.nan , np.nan , np.mean(Test_6_tokencount)]

# sigma_tc1 = [np.std(Test_1_tokencount) , np.nan , np.nan]
# sigma_tc2 = [np.nan , np.std(Test_2_tokencount) , np.nan]
# sigma_tc3 = [np.nan , np.nan , np.std(Test_3_tokencount)]
# sigma_tc4 = [np.std(Test_4_tokencount) , np.nan , np.nan]
# sigma_tc5 = [np.nan , np.std(Test_5_tokencount) , np.nan]
# sigma_tc6 = [np.nan , np.nan , np.std(Test_6_tokencount)]


# plt.figure(figsize=(8,5))


# # Plot style for each test
# tests = [
#     (mean_tc1, sigma_tc1, 'g', 'Test 1: Gemini 2.5 Flash Lite'),
#     (mean_tc2, sigma_tc2, 'b', 'Test 2: Gemini 2.5 Flash Lite'),
#     (mean_tc3, sigma_tc3, 'c', 'Test 3: Gemini 2.5 Flash Lite'),
#     (mean_tc4, sigma_tc4, 'm', 'Test 4: Gemini 2.5 Pro'),
#     (mean_tc5, sigma_tc5, 'y', 'Test 5: Gemini 2.5 Pro'),
#     (mean_tc6, sigma_tc6, 'k', 'Test 6: Gemini 2.5 Pro'),
# ]

# # Plot all tests
# for mean_tc, sigma, color, label in tests:
#     (line, caps, bars) = plt.errorbar(
#         x_axis, mean_tc, yerr=sigma,
#         fmt='o', markersize=8, markeredgecolor='black',
#         color=color, ecolor=color,
#         elinewidth=1.5, capsize=4,
#         alpha=0.7, label=label  # transparency + legend label
#     )
#     # Make error bars dashed and transparent
#     for b in bars:
#         b.set_linestyle(':')
#         b.set_alpha(0.6)

# # Labels, title, and grid
# plt.title('Mean Token Output of Varying Prompts and Models (30 Runs Each)', fontsize=13)
# plt.xlabel('Response Type', fontsize=11)
# plt.ylabel('Mean token output', fontsize=11)
# plt.grid(linestyle=':', linewidth=0.6, alpha=0.8)

# # Legend outside the plot
# plt.legend(
#     loc='center left',
#     bbox_to_anchor=(1, 0.5),
#     frameon=False,
#     title='Tests',
#     fontsize=9,
#     title_fontsize=10
# )

# plt.tight_layout()
# plt.show()




#------------- Accuracy - Output Type grapher ----------------------------------

# save all means and stddevs as vectors that can be used in an acc-type graph
# x_axis = ["Allocentric" , "Egocentric" , "Fixed-World"]

# meanv_1 = [np.nan , np.nan , np.nan]
# meanv_1[0] = mean_1

# meanv_2 = [np.nan , np.nan , np.nan]
# meanv_2[1] = mean_2

# meanv_3 = [np.nan , np.nan , np.nan]
# meanv_3[2] = mean_3

# meanv_4 = [np.nan , np.nan , np.nan]
# meanv_4[0] = mean_4

# meanv_5 = [np.nan , np.nan , np.nan]
# meanv_5[1] = mean_5

# meanv_6 = [np.nan , np.nan , np.nan]
# meanv_6[2] = mean_6





# plt.figure(figsize=(8,5))


# # Plot style for each test
# tests = [
#     (meanv_1, sigma_1, 'g', 'Test 1: Gemini 2.5 Flash Lite'),
#     (meanv_2, sigma_2, 'b', 'Test 2: Gemini 2.5 Flash Lite'),
#     (meanv_3, sigma_3, 'c', 'Test 3: Gemini 2.5 Flash Lite'),
#     (meanv_4, sigma_4, 'm', 'Test 4: Gemini 2.5 Pro'),
#     (meanv_5, sigma_5, 'y', 'Test 5: Gemini 2.5 Pro'),
#     (meanv_6, sigma_6, 'k', 'Test 6: Gemini 2.5 Pro'),
# ]

# # Plot all tests
# for meanv, sigma, color, label in tests:
#     (line, caps, bars) = plt.errorbar(
#         x_axis, meanv, yerr=sigma,
#         fmt='o', markersize=8, markeredgecolor='black',
#         color=color, ecolor=color,
#         elinewidth=1.5, capsize=4,
#         alpha=0.7, label=label  # transparency + legend label
#     )
#     # Make error bars dashed and transparent
#     for b in bars:
#         b.set_linestyle(':')
#         b.set_alpha(0.6)

# # Labels, title, and grid
# plt.title('Mean Accuracy of Varying Prompts and Models (30 Runs Each)', fontsize=13)
# plt.xlabel('Response Type', fontsize=11)
# plt.ylabel('Mean Accuracy (%)', fontsize=11)
# plt.grid(linestyle=':', linewidth=0.6, alpha=0.8)

# # Legend outside the plot
# plt.legend(
#     loc='center left',
#     bbox_to_anchor=(1, 0.5),
#     frameon=False,
#     title='Tests',
#     fontsize=9,
#     title_fontsize=10
# )

# plt.tight_layout()
# plt.show()


