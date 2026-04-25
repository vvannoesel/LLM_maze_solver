import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple



input_line_NR_coords = [[np.mean(r3.line_NR_coords_adj_json_input_tokens_3), np.mean(r6.line_NR_coords_adj_json_input_tokens_6), np.mean(r15.line_NR_coords_adj_json_input_tokens_15)],
                        [np.mean(r3.line_NR_coords_adj_txt_input_tokens_3), np.mean(r6.line_NR_coords_adj_txt_input_tokens_6), np.mean(r15.line_NR_coords_adj_txt_input_tokens_15)],
                        [np.mean(r3.line_NR_coords_jpg_input_tokens_3), np.mean(r6.line_NR_coords_jpg_input_tokens_6), np.mean(r15.line_NR_coords_jpg_input_tokens_15)],
                        [np.mean(r3.line_NR_coords_json_input_tokens_3), np.mean(r6.line_NR_coords_json_input_tokens_6), np.mean(r15.line_NR_coords_json_input_tokens_15)],
                        [np.mean(r3.line_NR_coords_tokenized_txt_input_tokens_3), np.mean(r6.line_NR_coords_tokenized_txt_input_tokens_6), np.mean(r15.line_NR_coords_tokenized_txt_input_tokens_15)]]

input_line_R_coords = [[np.mean(r3.line_R_coords_adj_json_input_tokens_3), np.mean(r6.line_R_coords_adj_json_input_tokens_6), np.mean(r15.line_R_coords_adj_json_input_tokens_15)],
                        [np.mean(r3.line_R_coords_adj_txt_input_tokens_3), np.mean(r6.line_R_coords_adj_txt_input_tokens_6), np.mean(r15.line_R_coords_adj_txt_input_tokens_15)],
                        [np.mean(r3.line_R_coords_jpg_input_tokens_3), np.mean(r6.line_R_coords_jpg_input_tokens_6), np.mean(r15.line_R_coords_jpg_input_tokens_15)],
                        [np.mean(r3.line_R_coords_json_input_tokens_3), np.mean(r6.line_R_coords_json_input_tokens_6), np.mean(r15.line_R_coords_json_input_tokens_15)],
                        [np.mean(r3.line_R_coords_tokenized_txt_input_tokens_3), np.mean(r6.line_R_coords_tokenized_txt_input_tokens_6), np.mean(r15.line_R_coords_tokenized_txt_input_tokens_15)]]


input_occupancy_NR_coords = [[np.mean(r3.occupancy_NR_coords_adj_json_input_tokens_3), np.mean(r6.occupancy_NR_coords_adj_json_input_tokens_6), np.mean(r15.occupancy_NR_coords_adj_json_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_coords_adj_txt_input_tokens_3), np.mean(r6.occupancy_NR_coords_adj_txt_input_tokens_6), np.mean(r15.occupancy_NR_coords_adj_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_coords_jpg_input_tokens_3), np.mean(r6.occupancy_NR_coords_jpg_input_tokens_6), np.mean(r15.occupancy_NR_coords_jpg_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_coords_json_input_tokens_3), np.mean(r6.occupancy_NR_coords_json_input_tokens_6), np.mean(r15.occupancy_NR_coords_json_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_coords_tokenized_txt_input_tokens_3), np.mean(r6.occupancy_NR_coords_tokenized_txt_input_tokens_6), np.mean(r15.occupancy_NR_coords_tokenized_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_coords_ascii_txt_input_tokens_3), np.mean(r6.occupancy_NR_coords_ascii_txt_input_tokens_6), np.mean(r15.occupancy_NR_coords_ascii_txt_input_tokens_15)]]

input_occupancy_R_coords = [[np.mean(r3.occupancy_R_coords_adj_json_input_tokens_3), np.mean(r6.occupancy_R_coords_adj_json_input_tokens_6), np.mean(r15.occupancy_R_coords_adj_json_input_tokens_15)],
                        [np.mean(r3.occupancy_R_coords_adj_txt_input_tokens_3), np.mean(r6.occupancy_R_coords_adj_txt_input_tokens_6), np.mean(r15.occupancy_R_coords_adj_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_R_coords_jpg_input_tokens_3), np.mean(r6.occupancy_R_coords_jpg_input_tokens_6), np.mean(r15.occupancy_R_coords_jpg_input_tokens_15)],
                        [np.mean(r3.occupancy_R_coords_json_input_tokens_3), np.mean(r6.occupancy_R_coords_json_input_tokens_6), np.mean(r15.occupancy_R_coords_json_input_tokens_15)],
                        [np.mean(r3.occupancy_R_coords_tokenized_txt_input_tokens_3), np.mean(r6.occupancy_R_coords_tokenized_txt_input_tokens_6), np.mean(r15.occupancy_R_coords_tokenized_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_R_coords_ascii_txt_input_tokens_3), np.mean(r6.occupancy_R_coords_ascii_txt_input_tokens_6), np.mean(r15.occupancy_R_coords_ascii_txt_input_tokens_15)]]




input_line_NR_allo = [[np.mean(r3.line_NR_allo_adj_json_input_tokens_3), np.mean(r6.line_NR_allo_adj_json_input_tokens_6), np.mean(r15.line_NR_allo_adj_json_input_tokens_15)],
                        [np.mean(r3.line_NR_allo_adj_txt_input_tokens_3), np.mean(r6.line_NR_allo_adj_txt_input_tokens_6), np.mean(r15.line_NR_allo_adj_txt_input_tokens_15)],
                        [np.mean(r3.line_NR_allo_jpg_input_tokens_3), np.mean(r6.line_NR_allo_jpg_input_tokens_6), np.mean(r15.line_NR_allo_jpg_input_tokens_15)],
                        [np.mean(r3.line_NR_allo_json_input_tokens_3), np.mean(r6.line_NR_allo_json_input_tokens_6), np.mean(r15.line_NR_allo_json_input_tokens_15)],
                        [np.mean(r3.line_NR_allo_tokenized_txt_input_tokens_3), np.mean(r6.line_NR_allo_tokenized_txt_input_tokens_6), np.mean(r15.line_NR_allo_tokenized_txt_input_tokens_15)]]

input_line_R_allo = [[np.mean(r3.line_R_allo_adj_json_input_tokens_3), np.mean(r6.line_R_allo_adj_json_input_tokens_6), np.mean(r15.line_R_allo_adj_json_input_tokens_15)],
                        [np.mean(r3.line_R_allo_adj_txt_input_tokens_3), np.mean(r6.line_R_allo_adj_txt_input_tokens_6), np.mean(r15.line_R_allo_adj_txt_input_tokens_15)],
                        [np.mean(r3.line_R_allo_jpg_input_tokens_3), np.mean(r6.line_R_allo_jpg_input_tokens_6), np.mean(r15.line_R_allo_jpg_input_tokens_15)],
                        [np.mean(r3.line_R_allo_json_input_tokens_3), np.mean(r6.line_R_allo_json_input_tokens_6), np.mean(r15.line_R_allo_json_input_tokens_15)],
                        [np.mean(r3.line_R_allo_tokenized_txt_input_tokens_3), np.mean(r6.line_R_allo_tokenized_txt_input_tokens_6), np.mean(r15.line_R_allo_tokenized_txt_input_tokens_15)]]


input_occupancy_NR_allo = [[np.mean(r3.occupancy_NR_allo_adj_json_input_tokens_3), np.mean(r6.occupancy_NR_allo_adj_json_input_tokens_6), np.mean(r15.occupancy_NR_allo_adj_json_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_allo_adj_txt_input_tokens_3), np.mean(r6.occupancy_NR_allo_adj_txt_input_tokens_6), np.mean(r15.occupancy_NR_allo_adj_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_allo_jpg_input_tokens_3), np.mean(r6.occupancy_NR_allo_jpg_input_tokens_6), np.mean(r15.occupancy_NR_allo_jpg_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_allo_json_input_tokens_3), np.mean(r6.occupancy_NR_allo_json_input_tokens_6), np.mean(r15.occupancy_NR_allo_json_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_allo_tokenized_txt_input_tokens_3), np.mean(r6.occupancy_NR_allo_tokenized_txt_input_tokens_6), np.mean(r15.occupancy_NR_allo_tokenized_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_allo_ascii_txt_input_tokens_3), np.mean(r6.occupancy_NR_allo_ascii_txt_input_tokens_6), np.mean(r15.occupancy_NR_allo_ascii_txt_input_tokens_15)]]

input_occupancy_R_allo = [[np.mean(r3.occupancy_R_allo_adj_json_input_tokens_3), np.mean(r6.occupancy_R_allo_adj_json_input_tokens_6), np.mean(r15.occupancy_R_allo_adj_json_input_tokens_15)],
                        [np.mean(r3.occupancy_R_allo_adj_txt_input_tokens_3), np.mean(r6.occupancy_R_allo_adj_txt_input_tokens_6), np.mean(r15.occupancy_R_allo_adj_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_R_allo_jpg_input_tokens_3), np.mean(r6.occupancy_R_allo_jpg_input_tokens_6), np.mean(r15.occupancy_R_allo_jpg_input_tokens_15)],
                        [np.mean(r3.occupancy_R_allo_json_input_tokens_3), np.mean(r6.occupancy_R_allo_json_input_tokens_6), np.mean(r15.occupancy_R_allo_json_input_tokens_15)],
                        [np.mean(r3.occupancy_R_allo_tokenized_txt_input_tokens_3), np.mean(r6.occupancy_R_allo_tokenized_txt_input_tokens_6), np.mean(r15.occupancy_R_allo_tokenized_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_R_allo_ascii_txt_input_tokens_3), np.mean(r6.occupancy_R_allo_ascii_txt_input_tokens_6), np.mean(r15.occupancy_R_allo_ascii_txt_input_tokens_15)]]




input_line_NR_ego = [[np.mean(r3.line_NR_ego_adj_json_input_tokens_3), np.mean(r6.line_NR_ego_adj_json_input_tokens_6), np.mean(r15.line_NR_ego_adj_json_input_tokens_15)],
                        [np.mean(r3.line_NR_ego_adj_txt_input_tokens_3), np.mean(r6.line_NR_ego_adj_txt_input_tokens_6), np.mean(r15.line_NR_ego_adj_txt_input_tokens_15)],
                        [np.mean(r3.line_NR_ego_jpg_input_tokens_3), np.mean(r6.line_NR_ego_jpg_input_tokens_6), np.mean(r15.line_NR_ego_jpg_input_tokens_15)],
                        [np.mean(r3.line_NR_ego_json_input_tokens_3), np.mean(r6.line_NR_ego_json_input_tokens_6), np.mean(r15.line_NR_ego_json_input_tokens_15)],
                        [np.mean(r3.line_NR_ego_tokenized_txt_input_tokens_3), np.mean(r6.line_NR_ego_tokenized_txt_input_tokens_6), np.mean(r15.line_NR_ego_tokenized_txt_input_tokens_15)]]

input_line_R_ego = [[np.mean(r3.line_R_ego_adj_json_input_tokens_3), np.mean(r6.line_R_ego_adj_json_input_tokens_6), np.mean(r15.line_R_ego_adj_json_input_tokens_15)],
                        [np.mean(r3.line_R_ego_adj_txt_input_tokens_3), np.mean(r6.line_R_ego_adj_txt_input_tokens_6), np.mean(r15.line_R_ego_adj_txt_input_tokens_15)],
                        [np.mean(r3.line_R_ego_jpg_input_tokens_3), np.mean(r6.line_R_ego_jpg_input_tokens_6), np.mean(r15.line_R_ego_jpg_input_tokens_15)],
                        [np.mean(r3.line_R_ego_json_input_tokens_3), np.mean(r6.line_R_ego_json_input_tokens_6), np.mean(r15.line_R_ego_json_input_tokens_15)],
                        [np.mean(r3.line_R_ego_tokenized_txt_input_tokens_3), np.mean(r6.line_R_ego_tokenized_txt_input_tokens_6), np.mean(r15.line_R_ego_tokenized_txt_input_tokens_15)]]


input_occupancy_NR_ego = [[np.mean(r3.occupancy_NR_ego_adj_json_input_tokens_3), np.mean(r6.occupancy_NR_ego_adj_json_input_tokens_6), np.mean(r15.occupancy_NR_ego_adj_json_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_ego_adj_txt_input_tokens_3), np.mean(r6.occupancy_NR_ego_adj_txt_input_tokens_6), np.mean(r15.occupancy_NR_ego_adj_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_ego_jpg_input_tokens_3), np.mean(r6.occupancy_NR_ego_jpg_input_tokens_6), np.mean(r15.occupancy_NR_ego_jpg_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_ego_json_input_tokens_3), np.mean(r6.occupancy_NR_ego_json_input_tokens_6), np.mean(r15.occupancy_NR_ego_json_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_ego_tokenized_txt_input_tokens_3), np.mean(r6.occupancy_NR_ego_tokenized_txt_input_tokens_6), np.mean(r15.occupancy_NR_ego_tokenized_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_NR_ego_ascii_txt_input_tokens_3), np.mean(r6.occupancy_NR_ego_ascii_txt_input_tokens_6), np.mean(r15.occupancy_NR_ego_ascii_txt_input_tokens_15)]]

input_occupancy_R_ego = [[np.mean(r3.occupancy_R_ego_adj_json_input_tokens_3), np.mean(r6.occupancy_R_ego_adj_json_input_tokens_6), np.mean(r15.occupancy_R_ego_adj_json_input_tokens_15)],
                        [np.mean(r3.occupancy_R_ego_adj_txt_input_tokens_3), np.mean(r6.occupancy_R_ego_adj_txt_input_tokens_6), np.mean(r15.occupancy_R_ego_adj_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_R_ego_jpg_input_tokens_3), np.mean(r6.occupancy_R_ego_jpg_input_tokens_6), np.mean(r15.occupancy_R_ego_jpg_input_tokens_15)],
                        [np.mean(r3.occupancy_R_ego_json_input_tokens_3), np.mean(r6.occupancy_R_ego_json_input_tokens_6), np.mean(r15.occupancy_R_ego_json_input_tokens_15)],
                        [np.mean(r3.occupancy_R_ego_tokenized_txt_input_tokens_3), np.mean(r6.occupancy_R_ego_tokenized_txt_input_tokens_6), np.mean(r15.occupancy_R_ego_tokenized_txt_input_tokens_15)],
                        [np.mean(r3.occupancy_R_ego_ascii_txt_input_tokens_3), np.mean(r6.occupancy_R_ego_ascii_txt_input_tokens_6), np.mean(r15.occupancy_R_ego_ascii_txt_input_tokens_15)]]




plot_configs = [
    # Top-Left: line coords
    (input_line_NR_coords, input_line_R_coords,  
     "Line-Wall Maze"),
    
    # Top-Middle: line allo
    # (input_line_NR_allo, input_line_R_allo, 
    #  "Line-Wall Maze, Allocentric Output"),
    
    # # Top-Right: line ego
    # (input_line_NR_ego, input_line_R_ego, 
    #  "Line-Wall Maze, Egocentric Output"),
    
    # Bottom-Left: occupancy coords
    (input_occupancy_NR_coords, input_occupancy_R_coords, 
     "Occupancy Grid Maze"),
    
    # # Bottom-Middle: occupancy allo
    # (input_occupancy_NR_allo, input_occupancy_R_allo, 
    #  "Occupancy Grid Maze, Allocentric Output"),
    
    # # Bottom-Right: occupancy ego
    # (input_occupancy_NR_ego, input_occupancy_R_ego, 
    #  "Occupancy Grid Maze, Egocentric Output"),
]

# 3. Setup Plotting Parameters
x_vals = np.arange(3)
x_tick_lbls_line = ["3x3", "6x6", "15x15"] # Complexity levels
x_tick_lbls_occupancy = ["7x7", "13x13", "31x31"] # Complexity levels
# Define a color palette for the 6 distinct methods (ignoring model version)
# We have 6 base methods (Adj Json, Adj Text, JPG, JSON, Tok, ASCII)
colors = plt.cm.tab10(np.linspace(0, 1, 10))[:6] 

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(5,8), sharey=True, sharex=False)

# Container to grab handles/labels for the global legend later
handles_for_legend = []
labels_for_legend = []

# 4. Main Plotting Loop
for idx, ax in enumerate(axes.flat):
    means_nr, means_r, title = plot_configs[idx]
    
    # Convert to numpy arrays just in case
    means_nr = np.array(means_nr)
    means_r = np.array(means_r)


    # Determine number of lines (5 for top row, 6 for bottom row)
    n_rows = means_nr.shape[0] 
    
    # Calculate jitter
    # We have n_rows. We spread them slightly around x.
    total_lines = n_rows 
    jitter_arr = np.linspace(-0.1, 0.1, total_lines)
    
    # # --- Plot NR Lines (Solid) ---
    # # These correspond to the first 'n_rows' of the single_legend
    # for i in range(n_rows):
    #     # Specific jitter for this line
    #     x_shifted = x_vals + jitter_arr[i]
        
    #     ax.plot(
    #         x_shifted,
    #         means_nr[i],
    #         # yerr=err_nr[i],
    #         marker='o',  
    #         linestyle = '-'     ,     # Solid line with markers
    #         linewidth=2,
    #         # capsize=4,
    #         # label=single_legend[i],
    #         color=colors[i],      # Assign color based on method type
    #         alpha=0.9
    #     )

    # --- Plot R Lines (Dotted) ---
    # These correspond to the second half of the single_legend, adjusted by offset
    # Legend structure is [6 items FL] + [6 items Pro]. 
    # Index for R corresponds to i + 6.
    for i in range(n_rows):
        # Specific jitter for this line (offset from NR lines)
        x_shifted = x_vals + jitter_arr[i ]
        
        # Calculate legend index (jump over the 6 FL items)
        leg_idx = i 
        
        ax.plot(
            x_shifted,
            means_r[i],
            # yerr=err_r[i],
            marker='o',
            linestyle = ':' ,            # Dotted line (:) with markers
            linewidth=2,
            # capsize=4,
            # mfc='none',
            # mec=colors[i],
            # label=single_legend[leg_idx],
            color=colors[i],      # Same color as the NR counterpart
            alpha=0.9
        )


    # Formatting
    if idx < 1:
        x_tick_lbls = x_tick_lbls_line
    else:
        pass
        x_tick_lbls = x_tick_lbls_occupancy
        ax.set_xlabel("Maze Size (-)", fontsize=11)
    ax.set_title(title, fontsize=11)
    ax.set_xticks(x_vals)
    ax.set_xticklabels(x_tick_lbls)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # if idx == 0:
    #     ax.set_ylabel("Mean Input Tokens")

    fig.supylabel("Mean Input Tokens (tokens)", fontsize=11)
    # fig.supxlabel("Maze Size")
    


    
    # Save handles from the last plot (Bottom-Right) because it contains all 12 lines
    # if idx == 5:
    #     handles_for_legend, labels_for_legend = ax.get_legend_handles_labels()



plt.suptitle("Mean Input Tokens Per Representation,\nMaze Style, and Maze Size", x=0.96*0.5, fontweight='bold')
# Position the legend within that white space
# legend=fig.legend(
#     handles_for_legend, 
#     labels_for_legend, 
#     loc='center left',           # Align the LEFT side of the legend...
#     bbox_to_anchor=(0.78, 0.5),  # ...to the point just after the plots (0.72)
#     title="Input Formats & Models",
#     borderaxespad=0.
# )
# Make the legend title bold
# legend.get_title().set_fontweight('bold')



# -----------------------
# Make a legend

# --- Legend Group Definitions ---
spacer_handle = (
Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
pro_handle = (
Line2D([], [], marker='none', color='grey', linestyle = ':'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
),
flashlite_handle = (
Line2D([], [], marker='none', color='grey', linestyle = '-'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
)


handles = [
# spacer_handle,
# pro_handle,
# flashlite_handle,
spacer_handle,

Line2D([], [], marker='o', color=colors[0], linestyle='None', markersize = 10),  # Adjacency JSON
Line2D([], [], marker='o', color=colors[1], linestyle='None', markersize = 10),  # Adjacency Text
Line2D([], [], marker='o', color=colors[2], linestyle='None', markersize = 10),  # JPG
Line2D([], [], marker='o', color=colors[3], linestyle='None', markersize = 10),  # JSON
Line2D([], [], marker='o', color=colors[4], linestyle='None', markersize = 10),  # Tokenized
Line2D([], [], marker='o', color=colors[5], linestyle='None', markersize = 10),  # ASCII

]
labels = [
# r"$\bf{Models}$",
# "Gemini 2.5 Pro", "Gemini 2.5 Flash-Lite",
r"$\bf{Input\ Formats}$",
"Adjacency List JSON", "Adjacency List Text", "JPG", "JSON", "Tagged per-cell", "ASCII"
]
# axes[1].legend(
# handles,
# labels,
# handler_map={tuple: HandlerTuple(ndivide=None)},
# loc='center left',
# bbox_to_anchor=(1.02, 0.5),
# title="Legend"
# )
plt.legend(
handles,
labels,
handler_map={tuple: HandlerTuple(ndivide=None)},
loc='upper left',
# bbox_to_anchor=(1.02, 0.5),
title="Legend"
)


plt.tight_layout()
# Adjust right margin to make room for the legend
plt.subplots_adjust(right=0.85) 
plt.show()









# -------------------------------- PLOT FIGS NEXT TO EACH OTHER ---------------------------------------------

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,5), sharey=True, sharex=False)

# Container to grab handles/labels for the global legend later
handles_for_legend = []
labels_for_legend = []

# 4. Main Plotting Loop
for idx, ax in enumerate(axes.flat):
    means_nr, means_r, title = plot_configs[idx]
    
    # Convert to numpy arrays just in case
    means_nr = np.array(means_nr)
    means_r = np.array(means_r)


    # Determine number of lines (5 for top row, 6 for bottom row)
    n_rows = means_nr.shape[0] 
    
    # Calculate jitter
    # We have n_rows. We spread them slightly around x.
    total_lines = n_rows 
    jitter_arr = np.linspace(-0.1, 0.1, total_lines)
    
    # # --- Plot NR Lines (Solid) ---
    # # These correspond to the first 'n_rows' of the single_legend
    # for i in range(n_rows):
    #     # Specific jitter for this line
    #     x_shifted = x_vals + jitter_arr[i]
        
    #     ax.plot(
    #         x_shifted,
    #         means_nr[i],
    #         # yerr=err_nr[i],
    #         marker='o',  
    #         linestyle = '-'     ,     # Solid line with markers
    #         linewidth=2,
    #         # capsize=4,
    #         # label=single_legend[i],
    #         color=colors[i],      # Assign color based on method type
    #         alpha=0.9
    #     )

    # --- Plot R Lines (Dotted) ---
    # These correspond to the second half of the single_legend, adjusted by offset
    # Legend structure is [6 items FL] + [6 items Pro]. 
    # Index for R corresponds to i + 6.
    for i in range(n_rows):
        # Specific jitter for this line (offset from NR lines)
        x_shifted = x_vals + jitter_arr[i ]
        
        # Calculate legend index (jump over the 6 FL items)
        leg_idx = i 
        
        ax.plot(
            x_shifted,
            means_r[i],
            # yerr=err_r[i],
            marker='o',
            linestyle = ':' ,            # Dotted line (:) with markers
            linewidth=2,
            # capsize=4,
            # mfc='none',
            # mec=colors[i],
            # label=single_legend[leg_idx],
            color=colors[i],      # Same color as the NR counterpart
            alpha=0.9
        )


    # Formatting
    if idx < 1:
        x_tick_lbls = x_tick_lbls_line
    else:
        pass
        x_tick_lbls = x_tick_lbls_occupancy
        # ax.set_xlabel("Maze Size", fontsize=11)
    ax.set_title(title, fontsize=11)
    ax.set_xticks(x_vals)
    ax.set_xticklabels(x_tick_lbls)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    if idx == 0:
        ax.set_ylabel("Mean Input Tokens (tokens)", fontsize=11)

    # fig.supylabel("Mean Input Tokens", fontsize=11)
    fig.supxlabel("Maze Size (-)", fontsize=11)
    


    
    # Save handles from the last plot (Bottom-Right) because it contains all 12 lines
    # if idx == 5:
    #     handles_for_legend, labels_for_legend = ax.get_legend_handles_labels()



plt.suptitle("Mean Input Tokens Per Representation,\nMaze Style, and Maze Size", x=0.94*0.5, fontweight='bold')
# Position the legend within that white space
# legend=fig.legend(
#     handles_for_legend, 
#     labels_for_legend, 
#     loc='center left',           # Align the LEFT side of the legend...
#     bbox_to_anchor=(0.78, 0.5),  # ...to the point just after the plots (0.72)
#     title="Input Formats & Models",
#     borderaxespad=0.
# )
# Make the legend title bold
# legend.get_title().set_fontweight('bold')



# -----------------------
# Make a legend

# --- Legend Group Definitions ---
spacer_handle = (
Line2D([], [], marker='o', color='none', markerfacecolor='none', markersize=10)
)
pro_handle = (
Line2D([], [], marker='none', color='grey', linestyle = ':'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
),
flashlite_handle = (
Line2D([], [], marker='none', color='grey', linestyle = '-'),
# Line2D([], [], marker='o', color='none', mec= 'none', markerfacecolor=red[1], markersize=10)
)


handles = [
# spacer_handle,
# pro_handle,
# flashlite_handle,
spacer_handle,

Line2D([], [], marker='o', color=colors[0], linestyle='None', markersize = 10),  # Adjacency JSON
Line2D([], [], marker='o', color=colors[1], linestyle='None', markersize = 10),  # Adjacency Text
Line2D([], [], marker='o', color=colors[2], linestyle='None', markersize = 10),  # JPG
Line2D([], [], marker='o', color=colors[3], linestyle='None', markersize = 10),  # JSON
Line2D([], [], marker='o', color=colors[4], linestyle='None', markersize = 10),  # Tagged
Line2D([], [], marker='o', color=colors[5], linestyle='None', markersize = 10),  # ASCII

]
labels = [
# r"$\bf{Models}$",
# "Gemini 2.5 Pro", "Gemini 2.5 Flash-Lite",
r"$\bf{Input\ Representations}$",
"Adjacency List JSON", "Adjacency List Text", "JPG", "JSON", "Tagged per-cell", "ASCII"
]
axes[1].legend(
handles,
labels,
handler_map={tuple: HandlerTuple(ndivide=None)},
loc='center left',
bbox_to_anchor=(1.02, 0.5),
title="Legend"
)
# plt.legend(
# handles,
# labels,
# handler_map={tuple: HandlerTuple(ndivide=None)},
# loc='upper left',
# # bbox_to_anchor=(1.02, 0.5),
# title="Legend"
# )


plt.tight_layout()
# Adjust right margin to make room for the legend
plt.subplots_adjust(right=0.85) 
plt.show()











