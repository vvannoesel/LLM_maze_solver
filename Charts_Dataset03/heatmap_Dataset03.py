# Import parent directory to access results files 
import sys
import os
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)

import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import results_Dataset03_3x3 as r3
import results_Dataset03_6x6 as r6
import results_Dataset03_15x15 as r15

representations_line = np.array(['JPG', 'JSON', 'Adjacency JSON', 'Adjacency Text', 'Tokenized'])
representations_occupancy = np.array(['JPG', 'JSON', 'Adjacency JSON', 'Adjacency Text', 'Tokenized', 'ASCII'])

import numpy as np

def vector_from_indices(indices, source_array):
    """
    calls the results vectors and returns new array that 
    only contains the values of the listed indices
    """
    if indices is None:
        return None
    return np.array([source_array[i - 1] for i in indices])



indices_coords_line_jpg_3 = np.empty((0,0))
indices_coords_line_json_3 = np.array([5, 10])
indices_coords_line_adj_json_3  = np.array([2, 8])
indices_coords_line_adj_txt_3 = np.array([1,2,3,5,8,10])
indices_coords_line_tokenized_3 = np.array([10])
indices_coords_occ_jpg_3 = np.array([2])
indices_coords_occ_json_3 = np.array([2,3,5,8,10])
indices_coords_occ_adj_json_3 = np.array([2,3,5,8,10])
indices_coords_occ_adj_txt_3 = np.array([2,3,5,8,10])
indices_coords_occ_tokenized_3 = np.array([2,3,5,8,10])
indices_coords_occ_ascii_3 = np.array([1, 10])

indices_allo_line_jpg_3 = np.array([2])
indices_allo_line_json_3 = np.array([2,8,10])
indices_allo_line_adj_json_3  = np.array([2,3,5])
indices_allo_line_adj_txt_3 = np.array([2,3,5,10])
indices_allo_line_tokenized_3 = np.array([8])
indices_allo_occ_jpg_3 = np.array([2])
indices_allo_occ_json_3 = np.array([1, 2,5,10])
indices_allo_occ_adj_json_3 = np.array([2,3,5,8,10])
indices_allo_occ_adj_txt_3 = np.array([2,3,5,8,10])
indices_allo_occ_tokenized_3 = np.array([1, 5,8, 10])
indices_allo_occ_ascii_3 = np.array([1,2,8])

indices_ego_line_jpg_3 = np.array([2])
indices_ego_line_json_3 = np.empty((0,0))
indices_ego_line_adj_json_3  = np.array([1, 2, 3,8])
indices_ego_line_adj_txt_3 = np.array([1,2,8,10])
indices_ego_line_tokenized_3 = np.array([5])
indices_ego_occ_jpg_3 = np.array([10])
indices_ego_occ_json_3 = np.array([2,5,8])
indices_ego_occ_adj_json_3 = np.array([3, 5, 8,10])
indices_ego_occ_adj_txt_3 = np.array([2,3,5,8,10])
indices_ego_occ_tokenized_3 = np.array([5])
indices_ego_occ_ascii_3 = np.empty((0,0))


indices_coords_line_jpg_6 = np.array([2,5])
indices_coords_line_json_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_coords_line_adj_json_6  = np.array([1,2,3,4,5,6,7,8,9,10])
indices_coords_line_adj_txt_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_coords_line_tokenized_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_coords_occ_jpg_6 = np.array([2,6,7,10])
indices_coords_occ_json_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_coords_occ_adj_json_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_coords_occ_adj_txt_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_coords_occ_tokenized_6 = np.array([1,2,3,4,5,6,8,9,10])
indices_coords_occ_ascii_6 = np.array([2,3,4,5,10])

indices_allo_line_jpg_6 = np.array([2])
indices_allo_line_json_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_allo_line_adj_json_6  = np.array([1,2,3,4,5,6,7,8,9,10])
indices_allo_line_adj_txt_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_allo_line_tokenized_6 = np.array([1,2,3,4,6,9,10])
indices_allo_occ_jpg_6 = np.array([2])
indices_allo_occ_json_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_allo_occ_adj_json_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_allo_occ_adj_txt_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_allo_occ_tokenized_6 = np.array([1,2,4,5,6,7,8,9,10])
indices_allo_occ_ascii_6 = np.array([1,2,3,4,6,7])

indices_ego_line_jpg_6 = np.array([2,5])
indices_ego_line_json_6 = np.array([1,2,3,4,5,6,7,9,10])
indices_ego_line_adj_json_6  = np.array([1,2,3,4,5,6,7,8,9,10])
indices_ego_line_adj_txt_6 = np.array([1,2,4,5,6,7,8,9,10])
indices_ego_line_tokenized_6 = np.array([1,3,4,5,6,7,9,10])
indices_ego_occ_jpg_6 = np.empty((0,0))
indices_ego_occ_json_6 = np.array([2,3,4,5,6,7,9,10])
indices_ego_occ_adj_json_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_ego_occ_adj_txt_6 = np.array([1,2,3,4,5,6,7,8,9,10])
indices_ego_occ_tokenized_6 = np.array([2,4,6,9])
indices_ego_occ_ascii_6 = np.array([1,2,5,7,9,10])


indices_coords_line_jpg_15 = np.array([3])
indices_coords_line_json_15 = np.array([1,2,6,8,9])
indices_coords_line_adj_json_15  = np.array([1,2,5,6,7,8,9,10])
indices_coords_line_adj_txt_15 = np.array([1,2,3,5,6,7,8,9])
indices_coords_line_tokenized_15 = np.array([1,4])
indices_coords_occ_jpg_15 = np.array([8,9])
indices_coords_occ_json_15 = np.array([1])
indices_coords_occ_adj_json_15 = np.array([5,6, 8, 9, 10])
indices_coords_occ_adj_txt_15 = np.array([2,3,4,5,6,7,8,9,10])
indices_coords_occ_tokenized_15 = np.array([1,2,4])
indices_coords_occ_ascii_15 = np.array([1,2,3,7])

indices_allo_line_jpg_15 = np.array([9])
indices_allo_line_json_15 = np.array([1,2,3,8,9,10])
indices_allo_line_adj_json_15  = np.array([1,2,4,5,6,7,8,9,10])
indices_allo_line_adj_txt_15 = np.array([1,2,3,7,10])
indices_allo_line_tokenized_15 = np.array([1,2,3,5,6])
indices_allo_occ_jpg_15 = np.empty((0,0))
indices_allo_occ_json_15 = np.array([1,4,6,7])
indices_allo_occ_adj_json_15 = np.array([1,3,4,5,7,8,10])
indices_allo_occ_adj_txt_15 = np.array([1,3,5,7,8,9,10])
indices_allo_occ_tokenized_15 = np.array([1,3,5,6,8])
indices_allo_occ_ascii_15 = np.array([1,7])

indices_ego_line_jpg_15 = np.array([10])
indices_ego_line_json_15 = np.array([1,2,3,4,7,10])
indices_ego_line_adj_json_15  = np.array([1,2,3,4,5,6,7,8,9,10])
indices_ego_line_adj_txt_15 = np.array([1,2,5,6,7,8,9,10])
indices_ego_line_tokenized_15 = np.array([1,7,9])
indices_ego_occ_jpg_15 = np.empty((0,0))
indices_ego_occ_json_15 = np.array([1])
indices_ego_occ_adj_json_15 = np.array([1,2,4,7,8,10])
indices_ego_occ_adj_txt_15 = np.array([2,3,4,5,6,9,8,10])
indices_ego_occ_tokenized_15 = np.array([1,7,10])
indices_ego_occ_ascii_15 = np.array([2])

occurrence_coords_3_line = np.array([len(indices_coords_line_jpg_3), len(indices_coords_line_json_3), len(indices_coords_line_adj_json_3), len(indices_coords_line_adj_txt_3), len(indices_coords_line_tokenized_3)])/6*100   # make percentage by dividing by number of runs
occurrence_coords_6_line = np.array([len(indices_coords_line_jpg_6), len(indices_coords_line_json_6), len(indices_coords_line_adj_json_6), len(indices_coords_line_adj_txt_6), len(indices_coords_line_tokenized_6)])*10 #np.array([1, 10, 10, 10, 8])*10
occurrence_coords_15_line = np.array([len(indices_coords_line_jpg_15), len(indices_coords_line_json_15), len(indices_coords_line_adj_json_15), len(indices_coords_line_adj_txt_15), len(indices_coords_line_tokenized_15)])*10
occurrence_coords_3_occ = np.array([len(indices_coords_occ_jpg_3), len(indices_coords_occ_json_3), len(indices_coords_occ_adj_json_3), len(indices_coords_occ_adj_txt_3), len(indices_coords_occ_tokenized_3), len(indices_coords_occ_ascii_3)])/6*100
occurrence_coords_6_occ = np.array([len(indices_coords_occ_jpg_6), len(indices_coords_occ_json_6), len(indices_coords_occ_adj_json_6), len(indices_coords_occ_adj_txt_6), len(indices_coords_occ_tokenized_6), len(indices_coords_occ_ascii_6)])*10
occurrence_coords_15_occ = np.array([len(indices_coords_occ_jpg_15), len(indices_coords_occ_json_15), len(indices_coords_occ_adj_json_15), len(indices_coords_occ_adj_txt_15), len(indices_coords_occ_tokenized_15), len(indices_coords_occ_ascii_15)])*10

occurrence_allo_3_line = np.array([len(indices_allo_line_jpg_3), len(indices_allo_line_json_3), len(indices_allo_line_adj_json_3), len(indices_allo_line_adj_txt_3), len(indices_allo_line_tokenized_3)])/6*100
occurrence_allo_6_line = np.array([len(indices_allo_line_jpg_6), len(indices_allo_line_json_6), len(indices_allo_line_adj_json_6), len(indices_allo_line_adj_txt_6), len(indices_allo_line_tokenized_6)])*10
occurrence_allo_15_line = np.array([len(indices_allo_line_jpg_15), len(indices_allo_line_json_15), len(indices_allo_line_adj_json_15), len(indices_allo_line_adj_txt_15), len(indices_allo_line_tokenized_15)])*10
occurrence_allo_3_occ = np.array([len(indices_allo_occ_jpg_3), len(indices_allo_occ_json_3), len(indices_allo_occ_adj_json_3), len(indices_allo_occ_adj_txt_3), len(indices_allo_occ_tokenized_3), len(indices_allo_occ_ascii_3)])/6*100
occurrence_allo_6_occ = np.array([len(indices_allo_occ_jpg_6), len(indices_allo_occ_json_6), len(indices_allo_occ_adj_json_6), len(indices_allo_occ_adj_txt_6), len(indices_allo_occ_tokenized_6), len(indices_allo_occ_ascii_6)])*10
occurrence_allo_15_occ = np.array([len(indices_allo_occ_jpg_15), len(indices_allo_occ_json_15), len(indices_allo_occ_adj_json_15), len(indices_allo_occ_adj_txt_15), len(indices_allo_occ_tokenized_15), len(indices_allo_occ_ascii_15)])*10

occurrence_ego_3_line = np.array([len(indices_ego_line_jpg_3), len(indices_ego_line_json_3), len(indices_ego_line_adj_json_3), len(indices_ego_line_adj_txt_3), len(indices_ego_line_tokenized_3)])/6*100
occurrence_ego_6_line = np.array([len(indices_ego_line_jpg_6), len(indices_ego_line_json_6), len(indices_ego_line_adj_json_6), len(indices_ego_line_adj_txt_6), len(indices_ego_line_tokenized_6)])*10
occurrence_ego_15_line = np.array([len(indices_ego_line_jpg_15), len(indices_ego_line_json_15), len(indices_ego_line_adj_json_15), len(indices_ego_line_adj_txt_15), len(indices_ego_line_tokenized_15)])*10
occurrence_ego_3_occ = np.array([len(indices_ego_occ_jpg_3), len(indices_ego_occ_json_3), len(indices_ego_occ_adj_json_3), len(indices_ego_occ_adj_txt_3), len(indices_ego_occ_tokenized_3), len(indices_ego_occ_ascii_3)])/6*100
occurrence_ego_6_occ = np.array([len(indices_ego_occ_jpg_6), len(indices_ego_occ_json_6), len(indices_ego_occ_adj_json_6), len(indices_ego_occ_adj_txt_6), len(indices_ego_occ_tokenized_6), len(indices_ego_occ_ascii_6)])*10
occurrence_ego_15_occ = np.array([len(indices_ego_occ_jpg_15), len(indices_ego_occ_json_15), len(indices_ego_occ_adj_json_15), len(indices_ego_occ_adj_txt_15), len(indices_ego_occ_tokenized_15), len(indices_ego_occ_ascii_15)])*10


# Build heatmap matrices (rows = representations, cols = maze sizes)
heatmap_coords_line = np.column_stack([occurrence_coords_3_line , occurrence_coords_6_line , occurrence_coords_15_line])
heatmap_allo_line   = np.column_stack([occurrence_allo_3_line,  occurrence_allo_6_line, occurrence_allo_15_line])
heatmap_ego_line = np.column_stack([occurrence_ego_3_line, occurrence_ego_6_line, occurrence_ego_15_line])
heatmap_coords_occ = np.column_stack([occurrence_coords_3_occ, occurrence_coords_6_occ, occurrence_coords_15_occ])
heatmap_allo_occ   = np.column_stack([occurrence_allo_3_occ, occurrence_allo_6_occ, occurrence_allo_15_occ])
heatmap_ego_occ   = np.column_stack([occurrence_ego_3_occ,  occurrence_ego_6_occ, occurrence_ego_15_occ])

maze_sizes_line = ['3x3', '6x6', '15x15']
maze_sizes_occ = ['7x7', '13x13', '31x31']



# Create figure with subplots
fig, axes = plt.subplots(
    nrows=2,
    ncols=3,
    figsize=(14, 8),
    sharex=False,
    sharey=False
)

# Map heatmaps to axes explicitly
plot_map = {
    (0, 0): (heatmap_coords_line, "Line-Walled Maze \nCoordinates Output"),
    (0, 1): (heatmap_allo_line,   "Line-Walled Maze \nAllocentric Output"),
    (0, 2): (heatmap_ego_line,   "Line-Walled Maze \nEgocentric Output"),
    (1, 0): (heatmap_coords_occ,  "Occupancy Grid Maze \nCoordinates Output"),
    (1, 1): (heatmap_allo_occ,    "Occupancy Grid Maze \nAllocentric Output"),
    (1, 2): (heatmap_ego_occ,   "Occupancy Grid Maze \nEgocentric Output"),
}

# settings for plotting
for (row, col), (data, title) in plot_map.items():
    ax = axes[row, col]

    im = ax.imshow(
        data,
        cmap="coolwarm",
        aspect="auto",
        vmin=0,
        vmax=100
    )

    ax.set_title(title)

    # Setting x-axis settings
    if row == 0:
        ax.set_xticks(np.arange(len(maze_sizes_line)))
        ax.set_xticklabels(maze_sizes_line)
        ax.set_xlabel("Maze Size")
    else:
        ax.set_xticks(np.arange(len(maze_sizes_occ)))
        ax.set_xticklabels(maze_sizes_occ)
        ax.set_xlabel("Maze Size")

    # Setting y-axis settings
    if col == 0:
        if row == 0:
            ax.set_yticks(np.arange(len(representations_line)))
            ax.set_yticklabels(representations_line)
        else:
            ax.set_yticks(np.arange(len(representations_occupancy)))
            ax.set_yticklabels(representations_occupancy)

        ax.set_ylabel("Maze Representation")
    else:
        ax.set_yticks([])

    # Add values in the cells
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(
                j, i, f"{data[i, j]:.0f}",
                ha="center",
                va="center",
                fontsize=10,
                color="black"
            )

# COlorbar settings
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
cbar = fig.colorbar(im, cax=cbar_ax)
cbar.set_label("Percentual Number of Occurrences")
cbar.ax.yaxis.set_major_formatter(mtick.PercentFormatter(100))

# Figure title and layout
fig.suptitle(
    "Occurrences of Gemini 2.5 Pro Mentioning Using Graph Solving Algorithms", # This is only done for reasoning because the NR does not show their work.
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 0.9, 0.95])
plt.show()
