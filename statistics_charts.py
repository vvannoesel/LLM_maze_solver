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


#------------- TEST 6 - REASONING, COORDINATES ----------------------------------
type = 'COORDS'
LLM = 'reasoning'
line_ascii_6 = np.array([33.33333333333333, 4.761904761904762, 9.090909090909092, 44.44444444444444, 18.181818181818183, 22.22222222222222, 20.0, 7.6923076923076925, 7.6923076923076925, 4.3478260869565215, 43.47826086956522, 36.84210526315789, 33.33333333333333, 18.181818181818183, 6.666666666666667, 4.3478260869565215, 23.076923076923077, 100.0, 17.647058823529413, 5.263157894736842, 10.526315789473683, 38.46153846153847, 76.92307692307693, 5.263157894736842, 9.090909090909092, 7.6923076923076925, 11.76470588235294, 26.666666666666668, 18.181818181818183, 9.523809523809524], dtype=float)
line_ascii_bewerkt_6 = line_ascii_6
mean_6 = np.mean(line_ascii_bewerkt_6)
sigma_6 = np.std(line_ascii_bewerkt_6)
standardized_6 = normalization(line_ascii_bewerkt_6, mean_6, sigma_6 )

x_axis = ["BEV" , "EGO" , "COORDS"]

mean_fl = [mean_1, mean_2, mean_3]
mean_pro = [mean_4, mean_5, mean_6]

empty = [np.nan , np.nan , np.nan]

meanv_1 = [np.nan , np.nan , np.nan]
meanv_1[0] = mean_1

meanv_2 = [np.nan , np.nan , np.nan]
meanv_2[1] = mean_2

meanv_3 = [np.nan , np.nan , np.nan]
meanv_3[2] = mean_3

meanv_4 = [np.nan , np.nan , np.nan]
meanv_4[0] = mean_4

meanv_5 = [np.nan , np.nan , np.nan]
meanv_5[1] = mean_5

meanv_6 = [np.nan , np.nan , np.nan]
meanv_6[2] = mean_6





plt.figure(figsize=(8,5))


# Plot style for each test
tests = [
    (meanv_1, sigma_1, 'g', 'Test 1: Gemini 2.5 Flash Lite'),
    (meanv_2, sigma_2, 'b', 'Test 2: Gemini 2.5 Flash Lite'),
    (meanv_3, sigma_3, 'c', 'Test 3: Gemini 2.5 Flash Lite'),
    (meanv_4, sigma_4, 'm', 'Test 4: Gemini 2.5 Pro'),
    (meanv_5, sigma_5, 'y', 'Test 5: Gemini 2.5 Pro'),
    (meanv_6, sigma_6, 'k', 'Test 6: Gemini 2.5 Pro'),
]

# Plot all tests
for meanv, sigma, color, label in tests:
    (line, caps, bars) = plt.errorbar(
        x_axis, meanv, yerr=sigma,
        fmt='o', markersize=8, markeredgecolor='black',
        color=color, ecolor=color,
        elinewidth=1.5, capsize=4,
        alpha=0.7, label=label  # transparency + legend label
    )
    # Make error bars dashed and transparent
    for b in bars:
        b.set_linestyle(':')
        b.set_alpha(0.6)

# Labels, title, and grid
plt.title('Mean Accuracy of Varying Prompts and Models (30 Runs Each)', fontsize=13)
plt.xlabel('Response Type', fontsize=11)
plt.ylabel('Mean Accuracy (%)', fontsize=11)
plt.grid(linestyle=':', linewidth=0.6, alpha=0.8)

# Legend outside the plot
plt.legend(
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    frameon=False,
    title='Tests',
    fontsize=9,
    title_fontsize=10
)

plt.tight_layout()
plt.show()


