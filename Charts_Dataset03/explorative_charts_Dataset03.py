# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import numpy as np
import matplotlib.pyplot as plt
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple




# Number of thinking tokens
# y= r15.line_R_coords_adj_txt_output_tokens_15 - r15.line_R_coords_adj_txt_final_answer_15 

# Number of final answer tokens
y=r15.line_R_coords_adj_txt_final_answer_15 

line_R_coords_adj_txt_thoughts_characters  = np.array([4193, 1312, 1990, 2316, 2283, 2513, 1644, 2192, 2814, 2892])
x = line_R_coords_adj_txt_thoughts_characters

# Linear fit
slope, intercept = np.polyfit(x, y, 1)

x_fit = np.linspace(x.min(), x.max(), 200)
y_fit = slope * x_fit + intercept

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, edgecolor='black', label='data')
plt.plot(x_fit, y_fit, linestyle='--', linewidth=2, label='trend')

# Axis labels
plt.ylabel('number of tokens (-)')
plt.xlabel('number of characters (-)')

# Grid
plt.grid(alpha=0.3)

# In-figure slope label
plt.text(
    0.05, 0.95,
    f'slope = {slope:.2f} tokens/characters',
    transform=plt.gca().transAxes,
    fontsize=11,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
)

plt.tight_layout()
# plt.show()





# -------------------------------------------------------------------------------
# thinking tokens
thinking_tokens = r15.line_R_coords_adj_txt_output_tokens_15 - r15.line_R_coords_adj_txt_final_answer_15

ratio = line_R_coords_adj_txt_thoughts_characters / thinking_tokens
print(ratio)
y= ratio

completion_score = r15.line_R_coords_adj_txt_15
x = completion_score
# Linear fit
slope, intercept = np.polyfit(x, y, 1)

x_fit = np.linspace(x.min(), x.max(), 200)
y_fit = slope * x_fit + intercept

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, edgecolor='black', label='data')
plt.plot(x_fit, y_fit, linestyle='--', linewidth=2, label='trend')

# Axis labels
plt.ylabel('ratio characters/token (-)')
plt.xlabel('Completion score (%)')

# Grid
plt.grid(alpha=0.3)

# In-figure slope label
plt.text(
    0.05, 0.95,
    f'slope = {slope:.2f}',
    transform=plt.gca().transAxes,
    fontsize=11,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
)

plt.tight_layout()
plt.show()