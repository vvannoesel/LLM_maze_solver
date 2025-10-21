import numpy as np
import matplotlib.pyplot as plt


#------------- TEST 1 - NON REASONING, BEV ----------------------------------
type = 'BEV'
LLM = 'nonreasoning'
line_ascii = np.array([0.0, 5.0, 10.0, 37.5, 10.0, 12.5, 110.00000000000001, 0.0, 0.0, 13.636363636363635, 0.0, 0.0, 0.0, 10.0, 7.142857142857142, 4.545454545454546, 8.333333333333332, 0.0, 0.0, 5.555555555555555, 0.0, 0.0, 50.0, 0.0, 0.0, 8.333333333333332, 12.5, 0.0, 0.0, 0.0], dtype=float)
line_ascii_bewerkt = np.array([0.0, 5.0, 10.0, 37.5, 10.0, 12.5, 0, 0.0, 0.0, 13.636363636363635, 0.0, 0.0, 0.0, 10.0, 7.142857142857142, 4.545454545454546, 8.333333333333332, 0.0, 0.0, 5.555555555555555, 0.0, 0.0, 50.0, 0.0, 0.0, 8.333333333333332, 12.5, 0.0, 0.0, 0.0], dtype=float)
ascii_standardized = np.zeros(30)



#------------- TEST 2 - NON REASONING, EGO ----------------------------------
type = 'EGO'
LLM = 'nonreasoning'
line_ascii = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.333333333333332, 110.00000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
line_ascii_bewerkt = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.333333333333332, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
ascii_standardized = np.zeros(30)



#------------- TEST 3 - NON REASONING, COORDINATES ----------------------------------
# type = 'COORDS'
# LLM = 'nonreasoning'
# line_ascii = np.array([20.0, 14.285714285714285, 18.181818181818183, 11.11111111111111, 9.090909090909092, 22.22222222222222, 13.333333333333334, 7.6923076923076925, 7.6923076923076925, 17.391304347826086, 4.3478260869565215, 5.263157894736842, 20.0, 36.36363636363637, 13.333333333333334, 8.695652173913043, 7.6923076923076925, 11.76470588235294, 17.647058823529413, 5.263157894736842, 10.526315789473683, 61.53846153846154, 84.61538461538461, 21.052631578947366, 27.27272727272727, 7.6923076923076925, 17.647058823529413, 6.666666666666667, 9.090909090909092, 14.285714285714285], dtype=float)
# line_ascii_bewerkt = line_ascii
# ascii_standardized = np.zeros(30)

#------------- TEST 4 - REASONING, BEV ----------------------------------
# type = 'BEV'
# LLM = 'reasoning'
# line_ascii = np.array([14.29, 0.0, 0.0, 0.0, 20.0, 12.5, 28.57142857142857, 0.0, 0.0, 13.636363636363635, 0.0, 5.555555555555555, 28.57142857142857, 10.0, 14.285714285714285, 9.090909090909092, 25.0, 6.25, 6.25, 0.0, 5.555555555555555, 66.66666666666666, 75.0, 0.0, 0.0, 25.0, 25.0, 7.142857142857142, 10.0, 0.0], dtype=float)
# line_ascii_bewerkt = line_ascii
# ascii_standardized = np.zeros(30)

#------------- TEST 5 - REASONING, EGO ----------------------------------
# type = 'EGO'
# LLM = 'reasoning'
# line_ascii = np.array([0.0, 5.0, 0.0, 62.5, 10.0, 37.5, 7.14285714, 8.33333333, 8.33333333, 45.45454545, 4.54545455, 11.11111111, 0.0, 30.0, 42.857142856, 0.0, 0.0, 0.0, 100.0, 16.666666666666664, 0.0, 0.0, 0.0, 5.555555555555555, 10.0, 0.0, 6.25, 21.428571428571427, 0.0, 0.0], dtype=float)
# line_ascii_bewerkt = line_ascii
# ascii_standardized = np.zeros(30)


#------------- TEST 6 - REASONING, COORDINATES ----------------------------------
type = 'COORDS'
LLM = 'reasoning'
line_ascii = np.array([33.33333333333333, 4.761904761904762, 9.090909090909092, 44.44444444444444, 18.181818181818183, 22.22222222222222, 20.0, 7.6923076923076925, 7.6923076923076925, 4.3478260869565215, 43.47826086956522, 36.84210526315789, 33.33333333333333, 18.181818181818183, 6.666666666666667, 4.3478260869565215, 23.076923076923077, 100.0, 17.647058823529413, 5.263157894736842, 10.526315789473683, 38.46153846153847, 76.92307692307693, 5.263157894736842, 9.090909090909092, 7.6923076923076925, 11.76470588235294, 26.666666666666668, 18.181818181818183, 9.523809523809524], dtype=float)
line_ascii_bewerkt = line_ascii
ascii_standardized = np.zeros(30)

# Calculate std dev
mean = np.mean(line_ascii_bewerkt)
sigma = np.std(line_ascii_bewerkt)
z = 1.96
E = 5
n = (z*sigma/E)**2
print("mean:", mean)
print("std dev:", sigma)
print("necessary runs:",n)

def normalization(vector):
    for i in range(1,30):
        value = vector[i-1]
        z = (value-mean)/sigma
        ascii_standardized[i-1]=z
    return ascii_standardized

print('standardized:', normalization(line_ascii_bewerkt))
print('standardized mean:', np.mean(ascii_standardized))


# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(ascii_standardized, bins=40, edgecolor='black')  # adjust number of bins as you like

# Labels and title
plt.xlabel("Score Value (%)")
plt.ylabel("Frequency")
plt.title(f"Normalized Frequency Distribution of Scores (5x5 maze, 30 runs, line_ascii, {LLM}, {type})")

# Optional: grid and layout
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show chart
plt.show()

# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(line_ascii_bewerkt, bins=30, edgecolor='black')  # 10 bins — adjust as you like

# Labels and title
plt.xlabel("Score Value (%)")
plt.ylabel("Frequency")
plt.title(f"Frequency Distribution of Scores (5x5 maze, 30 runs, line_ascii, {LLM}, {type})")

# Optional: grid and layout
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show chart
plt.show()


# def score_probabilities(array: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
#     """
#     Computes the probability (frequency distribution) of each unique value in a NumPy array.

#     Args:
#         array (np.ndarray): Input array of numeric values.

#     Returns:
#         tuple[np.ndarray, np.ndarray]:
#             - unique_values: array of unique score values
#             - probabilities: array of probabilities corresponding to each unique value
#     """
#     # Remove NaN values
#     clean_array = array[~np.isnan(array)]

#     if len(clean_array) == 0:
#         return np.array([]), np.array([])

#     # Count occurrences of each unique value
#     unique_values, counts = np.unique(clean_array, return_counts=True)

#     # Compute probabilities
#     probabilities = counts / counts.sum()

#     return unique_values, probabilities


# def expected_value(values, weights):
#     values = np.asarray(values)
#     weights = np.asarray(weights)
#     return (values * weights).sum() / weights.sum()

# # unique_values, probabilities = score_probabilities(line_ascii_bewerkt)
# # print('unique values:', unique_values)
# # print('probabilities:', probabilities)
# # expectation = expected_value(unique_values, probabilities)
# # print ('exp:',expectation)