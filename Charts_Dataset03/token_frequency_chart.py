# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import numpy as np
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15
import matplotlib.pyplot as plt



coords_representations_3 = [r3.line_NR_coords_jpg_output_tokens_3,
                       r3.line_NR_coords_json_output_tokens_3,
                       r3.line_NR_coords_adj_json_output_tokens_3,
                       r3.line_NR_coords_adj_txt_output_tokens_3,
                       r3.line_NR_coords_tokenized_txt_output_tokens_3,
                       r3.occupancy_NR_coords_jpg_output_tokens_3,
                       r3.occupancy_NR_coords_json_output_tokens_3,
                       r3.occupancy_NR_coords_adj_json_output_tokens_3,
                       r3.occupancy_NR_coords_adj_txt_output_tokens_3,
                       r3.occupancy_NR_coords_tokenized_txt_output_tokens_3,
                       r3.occupancy_NR_coords_ascii_txt_output_tokens_3]
coords_scores_3 = [r3.line_NR_coords_jpg_3,
               r3.line_NR_coords_json_3,
               r3.line_NR_coords_adj_json_3,
               r3.line_NR_coords_adj_txt_3,
               r3.line_NR_coords_tokenized_txt_3,
               r3.occupancy_NR_coords_jpg_3,
               r3.occupancy_NR_coords_json_3,
               r3.occupancy_NR_coords_adj_json_3,
               r3.occupancy_NR_coords_adj_txt_3,
               r3.occupancy_NR_coords_tokenized_txt_3,
               r3.occupancy_NR_coords_ascii_txt_3]

coords_representations_6 = [r6.line_NR_coords_jpg_output_tokens_6,
                       r6.line_NR_coords_json_output_tokens_6,
                       r6.line_NR_coords_adj_json_output_tokens_6,
                       r6.line_NR_coords_adj_txt_output_tokens_6,
                       r6.line_NR_coords_tokenized_txt_output_tokens_6,
                       r6.occupancy_NR_coords_jpg_output_tokens_6,
                       r6.occupancy_NR_coords_json_output_tokens_6,
                       r6.occupancy_NR_coords_adj_json_output_tokens_6,
                       r6.occupancy_NR_coords_adj_txt_output_tokens_6,
                       r6.occupancy_NR_coords_tokenized_txt_output_tokens_6,
                       r6.occupancy_NR_coords_ascii_txt_output_tokens_6]
coords_scores_6 = [r6.line_NR_coords_jpg_6,
               r6.line_NR_coords_json_6,
               r6.line_NR_coords_adj_json_6,
               r6.line_NR_coords_adj_txt_6,
               r6.line_NR_coords_tokenized_txt_6,
               r6.occupancy_NR_coords_jpg_6,
               r6.occupancy_NR_coords_json_6,
               r6.occupancy_NR_coords_adj_json_6,
               r6.occupancy_NR_coords_adj_txt_6,
               r6.occupancy_NR_coords_tokenized_txt_6,
               r6.occupancy_NR_coords_ascii_txt_6]

coords_representations_15 = [r15.line_NR_coords_jpg_output_tokens_15,
                       r15.line_NR_coords_json_output_tokens_15,
                       r15.line_NR_coords_adj_json_output_tokens_15,
                       r15.line_NR_coords_adj_txt_output_tokens_15,
                       r15.line_NR_coords_tokenized_txt_output_tokens_15,
                       r15.occupancy_NR_coords_jpg_output_tokens_15,
                       r15.occupancy_NR_coords_json_output_tokens_15,
                       r15.occupancy_NR_coords_adj_json_output_tokens_15,
                       r15.occupancy_NR_coords_adj_txt_output_tokens_15,
                       r15.occupancy_NR_coords_tokenized_txt_output_tokens_15,
                       r15.occupancy_NR_coords_ascii_txt_output_tokens_15]
coords_scores_15 = [r15.line_NR_coords_jpg_15,
               r15.line_NR_coords_json_15,
               r15.line_NR_coords_adj_json_15,
               r15.line_NR_coords_adj_txt_15,
               r15.line_NR_coords_tokenized_txt_15,
               r15.occupancy_NR_coords_jpg_15,
               r15.occupancy_NR_coords_json_15,
               r15.occupancy_NR_coords_adj_json_15,
               r15.occupancy_NR_coords_adj_txt_15,
               r15.occupancy_NR_coords_tokenized_txt_15,
               r15.occupancy_NR_coords_ascii_txt_15]



allo_representations_3 = [r3.line_NR_allo_jpg_output_tokens_3,
                       r3.line_NR_allo_json_output_tokens_3,
                       r3.line_NR_allo_adj_json_output_tokens_3,
                       r3.line_NR_allo_adj_txt_output_tokens_3,
                       r3.line_NR_allo_tokenized_txt_output_tokens_3,
                       r3.occupancy_NR_allo_jpg_output_tokens_3,
                       r3.occupancy_NR_allo_json_output_tokens_3,
                       r3.occupancy_NR_allo_adj_json_output_tokens_3,
                       r3.occupancy_NR_allo_adj_txt_output_tokens_3,
                       r3.occupancy_NR_allo_tokenized_txt_output_tokens_3,
                       r3.occupancy_NR_allo_ascii_txt_output_tokens_3]
allo_scores_3 = [r3.line_NR_allo_jpg_3,
               r3.line_NR_allo_json_3,
               r3.line_NR_allo_adj_json_3,
               r3.line_NR_allo_adj_txt_3,
               r3.line_NR_allo_tokenized_txt_3,
               r3.occupancy_NR_allo_jpg_3,
               r3.occupancy_NR_allo_json_3,
               r3.occupancy_NR_allo_adj_json_3,
               r3.occupancy_NR_allo_adj_txt_3,
               r3.occupancy_NR_allo_tokenized_txt_3,
               r3.occupancy_NR_allo_ascii_txt_3]



allo_representations_6 = [r6.line_NR_allo_jpg_output_tokens_6,
                       r6.line_NR_allo_json_output_tokens_6,
                       r6.line_NR_allo_adj_json_output_tokens_6,
                       r6.line_NR_allo_adj_txt_output_tokens_6,
                       r6.line_NR_allo_tokenized_txt_output_tokens_6,
                       r6.occupancy_NR_allo_jpg_output_tokens_6,
                       r6.occupancy_NR_allo_json_output_tokens_6,
                       r6.occupancy_NR_allo_adj_json_output_tokens_6,
                       r6.occupancy_NR_allo_adj_txt_output_tokens_6,
                       r6.occupancy_NR_allo_tokenized_txt_output_tokens_6,
                       r6.occupancy_NR_allo_ascii_txt_output_tokens_6]
allo_scores_6 = [r6.line_NR_allo_jpg_6,
               r6.line_NR_allo_json_6,
               r6.line_NR_allo_adj_json_6,
               r6.line_NR_allo_adj_txt_6,
               r6.line_NR_allo_tokenized_txt_6,
               r6.occupancy_NR_allo_jpg_6,
               r6.occupancy_NR_allo_json_6,
               r6.occupancy_NR_allo_adj_json_6,
               r6.occupancy_NR_allo_adj_txt_6,
               r6.occupancy_NR_allo_tokenized_txt_6,
               r6.occupancy_NR_allo_ascii_txt_6]

allo_representations_15 = [r15.line_NR_allo_jpg_output_tokens_15,
                       r15.line_NR_allo_json_output_tokens_15,
                       r15.line_NR_allo_adj_json_output_tokens_15,
                       r15.line_NR_allo_adj_txt_output_tokens_15,
                       r15.line_NR_allo_tokenized_txt_output_tokens_15,
                       r15.occupancy_NR_allo_jpg_output_tokens_15,
                       r15.occupancy_NR_allo_json_output_tokens_15,
                       r15.occupancy_NR_allo_adj_json_output_tokens_15,
                       r15.occupancy_NR_allo_adj_txt_output_tokens_15,
                       r15.occupancy_NR_allo_tokenized_txt_output_tokens_15,
                       r15.occupancy_NR_allo_ascii_txt_output_tokens_15]
allo_scores_15 = [r15.line_NR_allo_jpg_15,
               r15.line_NR_allo_json_15,
               r15.line_NR_allo_adj_json_15,
               r15.line_NR_allo_adj_txt_15,
               r15.line_NR_allo_tokenized_txt_15,
               r15.occupancy_NR_allo_jpg_15,
               r15.occupancy_NR_allo_json_15,
               r15.occupancy_NR_allo_adj_json_15,
               r15.occupancy_NR_allo_adj_txt_15,
               r15.occupancy_NR_allo_tokenized_txt_15,
               r15.occupancy_NR_allo_ascii_txt_15]




ego_representations_3 = [r3.line_NR_ego_jpg_output_tokens_3,
                       r3.line_NR_ego_json_output_tokens_3,
                       r3.line_NR_ego_adj_json_output_tokens_3,
                       r3.line_NR_ego_adj_txt_output_tokens_3,
                       r3.line_NR_ego_tokenized_txt_output_tokens_3,
                       r3.occupancy_NR_ego_jpg_output_tokens_3,
                       r3.occupancy_NR_ego_json_output_tokens_3,
                       r3.occupancy_NR_ego_adj_json_output_tokens_3,
                       r3.occupancy_NR_ego_adj_txt_output_tokens_3,
                       r3.occupancy_NR_ego_tokenized_txt_output_tokens_3,
                       r3.occupancy_NR_ego_ascii_txt_output_tokens_3]
ego_scores_3 = [r3.line_NR_ego_jpg_3,
               r3.line_NR_ego_json_3,
               r3.line_NR_ego_adj_json_3,
               r3.line_NR_ego_adj_txt_3,
               r3.line_NR_ego_tokenized_txt_3,
               r3.occupancy_NR_ego_jpg_3,
               r3.occupancy_NR_ego_json_3,
               r3.occupancy_NR_ego_adj_json_3,
               r3.occupancy_NR_ego_adj_txt_3,
               r3.occupancy_NR_ego_tokenized_txt_3,
               r3.occupancy_NR_ego_ascii_txt_3]

ego_representations_6 = [r6.line_NR_ego_jpg_output_tokens_6,
                       r6.line_NR_ego_json_output_tokens_6,
                       r6.line_NR_ego_adj_json_output_tokens_6,
                       r6.line_NR_ego_adj_txt_output_tokens_6,
                       r6.line_NR_ego_tokenized_txt_output_tokens_6,
                       r6.occupancy_NR_ego_jpg_output_tokens_6,
                       r6.occupancy_NR_ego_json_output_tokens_6,
                       r6.occupancy_NR_ego_adj_json_output_tokens_6,
                       r6.occupancy_NR_ego_adj_txt_output_tokens_6,
                       r6.occupancy_NR_ego_tokenized_txt_output_tokens_6,
                       r6.occupancy_NR_ego_ascii_txt_output_tokens_6]
ego_scores_6 = [r6.line_NR_ego_jpg_6,
               r6.line_NR_ego_json_6,
               r6.line_NR_ego_adj_json_6,
               r6.line_NR_ego_adj_txt_6,
               r6.line_NR_ego_tokenized_txt_6,
               r6.occupancy_NR_ego_jpg_6,
               r6.occupancy_NR_ego_json_6,
               r6.occupancy_NR_ego_adj_json_6,
               r6.occupancy_NR_ego_adj_txt_6,
               r6.occupancy_NR_ego_tokenized_txt_6,
               r6.occupancy_NR_ego_ascii_txt_6]

ego_representations_15 = [r15.line_NR_ego_jpg_output_tokens_15,
                       r15.line_NR_ego_json_output_tokens_15,
                       r15.line_NR_ego_adj_json_output_tokens_15,
                       r15.line_NR_ego_adj_txt_output_tokens_15,
                       r15.line_NR_ego_tokenized_txt_output_tokens_15,
                       r15.occupancy_NR_ego_jpg_output_tokens_15,
                       r15.occupancy_NR_ego_json_output_tokens_15,
                       r15.occupancy_NR_ego_adj_json_output_tokens_15,
                       r15.occupancy_NR_ego_adj_txt_output_tokens_15,
                       r15.occupancy_NR_ego_tokenized_txt_output_tokens_15,
                       r15.occupancy_NR_ego_ascii_txt_output_tokens_15]
ego_scores_15 = [r15.line_NR_ego_jpg_15,
               r15.line_NR_ego_json_15,
               r15.line_NR_ego_adj_json_15,
               r15.line_NR_ego_adj_txt_15,
               r15.line_NR_ego_tokenized_txt_15,
               r15.occupancy_NR_ego_jpg_15,
               r15.occupancy_NR_ego_json_15,
               r15.occupancy_NR_ego_adj_json_15,
               r15.occupancy_NR_ego_adj_txt_15,
               r15.occupancy_NR_ego_tokenized_txt_15,
               r15.occupancy_NR_ego_ascii_txt_15]



coords_empty_accuracy_list = []
allo_empty_accuracy_list = []
ego_empty_accuracy_list = []


def occurrence_extractor(input_vector_name, input_vector_accuracy_vector, empty_accuracy_list):
    '''
    This function checks which positions in the final_answer_token_output vector contain the maximum value of tokens (650 or 4000).
    Then it takes the corresponding completion scores and saves them to a new list. Used to show that high token output is a 
    sign of giving up on the task. 
    '''
    for a in range(len(input_vector_name)):
        # print(a)
        if input_vector_name[a] == 650.0 or input_vector_name[a] == 4000.0:
            # print(input_vector_accuracy_vector[a])
            empty_accuracy_list.append(input_vector_accuracy_vector[a] ) #takes the completion score from the position where final answer token output was 650
    return empty_accuracy_list





for i in range(len(coords_representations_3)):
    list=occurrence_extractor(coords_representations_3[i], coords_scores_3[i], coords_empty_accuracy_list)
final_coords_list_3 = np.array(list,dtype=float)

for i in range(len(coords_representations_6)):
    list=occurrence_extractor(coords_representations_6[i], coords_scores_6[i], coords_empty_accuracy_list)
final_coords_list_6 = np.array(list,dtype=float)

# each iteration, the list is appended with more values. Output of this list will be the total of all previous maze sizes. 
for i in range(len(coords_representations_15)):
    list=occurrence_extractor(coords_representations_15[i], coords_scores_15[i], coords_empty_accuracy_list)
final_coords_list_15 = np.array(list,dtype=float)

# occurrence_extractor(r3.occupancy_NR_coords_json_output_tokens_3, r3.occupancy_NR_coords_json_3, empty_accuracy_list)
print('coords 15:',final_coords_list_15, 'shape coords:', final_coords_list_15.shape,)

avg_coords = np.mean([final_coords_list_15]) # the values that comes out is the total average over all sizes, so ALL occurrences of max token output in NR coords. 
print(avg_coords)





for i in range(len(allo_representations_3)):
    list=occurrence_extractor(allo_representations_3[i], allo_scores_3[i], allo_empty_accuracy_list)
final_allo_list_3 = np.array(list,dtype=float)

for i in range(len(allo_representations_6)):
    list=occurrence_extractor(allo_representations_6[i], allo_scores_6[i], allo_empty_accuracy_list)
final_allo_list_6 = np.array(list,dtype=float)

# each iteration, the list is appended with more values. Output of this list will be the total of all previous maze sizes. 
for i in range(len(allo_representations_15)):
    list=occurrence_extractor(allo_representations_15[i], allo_scores_15[i], allo_empty_accuracy_list)
final_allo_list_15 = np.array(list,dtype=float)

# occurrence_extractor(r3.occupancy_NR_coords_json_output_tokens_3, r3.occupancy_NR_coords_json_3, empty_accuracy_list)
print('allo 15:',final_allo_list_15, 'shape coords:', final_allo_list_15.shape,)

avg_allo = np.mean([final_allo_list_15]) # the values that comes out is the total average over all sizes, so ALL occurrences of max token output in NR allo. 
print(avg_allo)





for i in range(len(ego_representations_3)):
    list=occurrence_extractor(ego_representations_3[i], ego_scores_3[i], ego_empty_accuracy_list)
final_ego_list_3 = np.array(list,dtype=float)

for i in range(len(ego_representations_6)):
    list=occurrence_extractor(ego_representations_6[i], ego_scores_6[i], ego_empty_accuracy_list)
final_ego_list_6 = np.array(list,dtype=float)

# each iteration, the list is appended with more values. Output of this list will be the total of all previous maze sizes. 
for i in range(len(ego_representations_15)):
    list=occurrence_extractor(ego_representations_15[i], ego_scores_15[i], ego_empty_accuracy_list)
final_ego_list_15 = np.array(list,dtype=float)

# occurrence_extractor(r3.occupancy_NR_coords_json_output_tokens_3, r3.occupancy_NR_coords_json_3, empty_accuracy_list)
print('ego 15:',final_ego_list_15, 'shape ego:', final_ego_list_15.shape,)

avg_ego = np.mean([final_ego_list_15]) # the values that comes out is the total average over all sizes, so ALL occurrences of max token output in NR ego. 
print(avg_ego)



# create figure of frequency histogram
vectors = [final_coords_list_15, final_allo_list_15, final_ego_list_15]
titles = ['Coordinates Output', 'Allocentric Output', 'Egocentric Output']

# Define bins: 0–5, 6–10, ..., 96–100
bins = np.arange(0, 105, 5)

fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

for ax, vec, title in zip(axes, vectors, titles):
    ax.hist(vec, bins=bins, color='tomato', edgecolor = 'black', alpha = 0.5)
    ax.set_ylabel('Frequency (-)', fontsize = 16)
    ax.set_title(title, fontsize = 18)
    ax.grid(axis='y', alpha=0.3)

# X-axis labeling
axes[-1].set_xlabel('Completion Score (%)', fontsize=16)
axes[-1].set_xticks(bins)
axes[-1].set_xlim(0, 100)

# Adjust tick text size
axes[0].tick_params(axis='both', which='major', labelsize=14)
axes[1].tick_params(axis='both', which='major', labelsize=14)
axes[-1].tick_params(axis='both', which='major', labelsize=14)

plt.suptitle('Completion Score Frequency at Maximum Final Answer Token Output, Gemini 2.5 Flash-Lite', fontweight = 'bold', fontsize=20)

plt.tight_layout()
plt.show()

