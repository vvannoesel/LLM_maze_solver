import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import results_Dataset03_3x3 as h
import results_Dataset03_6x6 as i
import results_Dataset03_15x15 as j

representations_line = np.array(['JPG Line', 'JSON Line', 'JSON Adj Line', 'TXT Adj Line', 'Tokenized Line'])
representations_occupancy = np.array(['JPG Occupancy', 'JSON Occupancy', 'JSON Adj Occupancy', 'TXT Adj Occupancy', 'Tokenized Occupancy', 'ASCII Occupancy'])

occurrence_coords_3_line = np.array([0, 1, 1, 6, 0])/6*100   # make percentage by dividing by number of runs
occurrence_coords_6_line = np.array([1, 10, 10, 10, 8])*10

occurrence_coords_3_occ = np.array([ 0, 2, 5, 5, 4, 1])/6*100
occurrence_coords_6_occ = np.array([ 2, 9, 10, 10, 8, 3])*10

occurrence_allo_3_line = np.array([0, 3, 3, 4, 1])/6*100
occurrence_allo_6_line = np.array([0, 10, 10, 10, 5])*10
occurrence_allo_3_occ = np.array([ 0, 3, 5, 5, 2, 2])/6*100
occurrence_allo_6_occ = np.array([ 0, 10, 10, 10, 8, 4])*10

occurrence_ego_3_line = np.array([0, 0, 2, 4, 1])/6*100
occurrence_ego_6_line = np.array([0, 9, 10, 9, 8])*10
occurrence_ego_3_occ = np.array([0, 2, 3, 4, 1, 0])/6*100
occurrence_ego_6_occ = np.array([0, 6, 10, 10, 1, 5])*10



# Build heatmap matrices (rows = representations, cols = maze sizes)
heatmap_coords_line = np.column_stack([occurrence_coords_3_line, occurrence_coords_6_line])
heatmap_allo_line   = np.column_stack([occurrence_allo_3_line,  occurrence_allo_6_line])
heatmap_ego_line = np.column_stack([occurrence_ego_3_line, occurrence_ego_6_line])
heatmap_coords_occ = np.column_stack([occurrence_coords_3_occ, occurrence_coords_6_occ])
heatmap_allo_occ   = np.column_stack([occurrence_allo_3_occ,  occurrence_allo_6_occ])
heatmap_ego_occ   = np.column_stack([occurrence_ego_3_occ,  occurrence_ego_6_occ])



maze_sizes_line = ['3x3', '6x6']
maze_sizes_occ = ['7x7', '13x13']



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
cbar.set_label("Number of Occurrences")
cbar.ax.yaxis.set_major_formatter(mtick.PercentFormatter(100))

# Figure title and layout
fig.suptitle(
    "Heatmaps of Reasoning Occurrences by Representation",
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 0.9, 0.95])
plt.show()
