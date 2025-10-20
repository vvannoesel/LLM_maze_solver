import numpy as np
import matplotlib.pyplot as plt


#------------- TEST 1 - NON REASONING, BEV ----------------------------------
line_ascii = np.array([0.0, 5.0, 10.0, 37.5, 10.0, 12.5, 110.00000000000001, 0.0, 0.0, 13.636363636363635, 0.0, 0.0, 0.0, 10.0, 7.142857142857142, 4.545454545454546, 8.333333333333332, 0.0, 0.0, 5.555555555555555, 0.0, 0.0, 50.0, 0.0, 0.0, 8.333333333333332, 12.5, 0.0, 0.0, 0.0], dtype=float)
line_ascii_bewerkt = np.array([0.0, 5.0, 10.0, 37.5, 10.0, 12.5, 0, 0.0, 0.0, 13.636363636363635, 0.0, 0.0, 0.0, 10.0, 7.142857142857142, 4.545454545454546, 8.333333333333332, 0.0, 0.0, 5.555555555555555, 0.0, 0.0, 50.0, 0.0, 0.0, 8.333333333333332, 12.5, 0.0, 0.0, 0.0], dtype=float)
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
plt.hist(ascii_standardized, bins=30, edgecolor='black')  # 10 bins — adjust as you like

# Labels and title
plt.xlabel("Score Value (%)")
plt.ylabel("Frequency")
plt.title("Normalized Frequency Distribution of Scores (line_ascii)")

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
plt.title("Frequency Distribution of Scores (line_ascii)")

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