# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 10:08:42 2025

@author: valer and Gemini 2.5 Pro
"""
import random
import json
import collections
import math
from PIL import Image, ImageDraw

class Cell:
    """
    A class to represent a single cell in the maze with walls and visited status.
    """
    def __init__(self):
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.visited = False

class Maze:
    """
    A class to represent and generate a maze where walls are borders.

    Attributes:
        cols (int): The number of columns in the maze.
        rows (int): The number of rows in the maze.
        grid (list): A 2D list of Cell objects.
        start (tuple): The (row, col) coordinates for the maze start.
        end (tuple): The (row, col) coordinates for the maze end.
        solution (list): A list of (row, col) coordinates for the solution path.
    """

    def __init__(self, cols, rows, _generate=True):
        """
        Initializes the Maze object.

        Args:
            cols (int): The number of columns for the maze.
            rows (int): The number of rows for the maze.
            _generate (bool): If True, automatically generates and solves the maze.
        """
        if cols <= 0 or rows <= 0:
            raise ValueError("Columns and rows must be positive integers.")
        self.cols = cols
        self.rows = rows
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.start = (0, 0)
        self.end = (rows - 1, cols - 1)
        self.solution = None
        self.dfs_path = []  # Stores the path for tokenization
        if _generate:
            self._generate_maze()
            self._solve_maze()

    def _generate_maze(self):
        """
        Generates the maze structure using a randomized Depth-First Search algorithm.
        This ensures a unique maze with a single solution.
        """
        stack = []
        current_cell_coords = self.start
        self.grid[self.start[0]][self.start[1]].visited = True
        stack.append(current_cell_coords)
        self.dfs_path.append(current_cell_coords)

        while stack:
            current_row, current_col = stack[-1]
            neighbors = self._get_unvisited_neighbors(current_row, current_col)

            if neighbors:
                next_row, next_col = random.choice(neighbors)
                next_cell = self.grid[next_row][next_col]
                self._remove_walls(current_row, current_col, next_row, next_col)
                next_cell.visited = True
                stack.append((next_row, next_col))
                self.dfs_path.append((next_row, next_col))
            else:
                stack.pop()
                if stack:
                    self.dfs_path.append(stack[-1])

    def _get_unvisited_neighbors(self, row, col):
        """
        Gets the unvisited neighbors of a cell.
        """
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # E, W, S, N
        random.shuffle(directions)

        for dr, dc in directions:
            n_row, n_col = row + dr, col + dc
            if 0 <= n_row < self.rows and 0 <= n_col < self.cols and not self.grid[n_row][n_col].visited:
                neighbors.append((n_row, n_col))
        return neighbors

    def _remove_walls(self, r1, c1, r2, c2):
        """
        Removes the wall between two adjacent cells.
        """
        if r1 == r2:
            if c1 > c2:
                self.grid[r1][c1].walls['W'] = False
                self.grid[r2][c2].walls['E'] = False
            else:
                self.grid[r1][c1].walls['E'] = False
                self.grid[r2][c2].walls['W'] = False
        else:
            if r1 > r2:
                self.grid[r1][c1].walls['N'] = False
                self.grid[r2][c2].walls['S'] = False
            else:
                self.grid[r1][c1].walls['S'] = False
                self.grid[r2][c2].walls['N'] = False

    def _solve_maze(self):
        """
        Solves the maze using a Breadth-First Search (BFS) algorithm.
        """
        queue = collections.deque([(self.start, [self.start])])
        visited = {self.start}

        while queue:
            (current_row, current_col), path = queue.popleft()

            if (current_row, current_col) == self.end:
                self.solution = path
                return

            directions = [(0, 1, 'E'), (0, -1, 'W'), (1, 0, 'S'), (-1, 0, 'N')]
            for dr, dc, wall_dir in directions:
                n_row, n_col = current_row + dr, current_col + dc

                if (0 <= n_row < self.rows and
                        0 <= n_col < self.cols and
                        (n_row, n_col) not in visited and
                        not self.grid[current_row][current_col].walls[wall_dir]):
                    visited.add((n_row, n_col))
                    new_path = list(path)
                    new_path.append((n_row, n_col))
                    queue.append(((n_row, n_col), new_path))

    # def to_ascii(self): #THIS FUNCTION DRAWS ASCII CORRECT BUT WITHOUT START AND END MARKERS
    #     """
    #     Returns an ASCII string representation of the maze.
    #     """
    #     output = "+" + "---+" * self.cols + "\n"
    #     for r, row in enumerate(self.grid):
    #         line1 = "|"
    #         line2 = "+"
    #         for c, cell in enumerate(row):
    #             line1 += "   "
    #             if cell.walls['E']:
    #                 line1 += "|"
    #             else:
    #                 line1 += " "
    #             if cell.walls['S']:
    #                 line2 += "---"
    #             else:
    #                 line2 += "   "
    #             line2 += "+"
    #         output += line1 + "\n" + line2 + "\n"
    #     return output
    def to_ascii(self, show_markers=True):
        """
        Returns an ASCII string representation of the maze.
        
        Args:
            show_markers (bool): If True, shows 'O' for origin and 'T' for target.
                                 If False, shows the classic walls-only maze.
        """
        output = "+" + "-+" * self.cols + "\n"
        for r, row in enumerate(self.grid):
            line1 = "|"
            line2 = "+"
            for c, cell in enumerate(row):
                content = " "
                if show_markers:
                    if (r, c) == self.start:
                        content = "S"
                    elif (r, c) == self.end:
                        content = "E"
                line1 += content
                
                if cell.walls['E']:
                    line1 += "|"
                else:
                    line1 += " "
                if cell.walls['S']:
                    line2 += "-"
                else:
                    line2 += " "
                line2 += "+"
            output += line1 + "\n" + line2 + "\n"
        return output

    def _draw_star(self, draw, center_x, center_y, size, fill_color):
        """Helper function to draw a 5-pointed star."""
        points = []
        for i in range(5):
            angle_outer = (math.pi / 2) + (2 * math.pi * i / 5)
            points.append((
                center_x + size * math.cos(angle_outer),
                center_y - size * math.sin(angle_outer)
            ))
            angle_inner = (math.pi / 2) + (2 * math.pi * (i + 0.5) / 5)
            points.append((
                center_x + (size / 2.5) * math.cos(angle_inner),
                center_y - (size / 2.5) * math.sin(angle_inner)
            ))
        draw.polygon(points, fill=fill_color)

    def to_jpeg(self, filename="maze.jpg", total_width=800, total_height=800):
        """
        Saves the maze as a high-quality, anti-aliased JPEG image.
        """
        # 1. Set parameters for anti-aliasing
        upscale = 4

        # 2. Create the upscaled canvas for smooth drawing
        upscaled_width = total_width * upscale
        upscaled_height = total_height * upscale
        image = Image.new("RGB", (upscaled_width, upscaled_height), "white")
        draw = ImageDraw.Draw(image)

        # 3. Calculate dynamic, upscaled dimensions for drawing
        margin = int(min(upscaled_width, upscaled_height) * 0.05)
        drawing_area = min(upscaled_width, upscaled_height) - 2 * margin
        cell_size = drawing_area / max(self.rows, self.cols)
        wall_width = max(1 * upscale, int(cell_size / 12))

        maze_width = self.cols * cell_size
        maze_height = self.rows * cell_size
        offset_x = (upscaled_width - maze_width) / 2
        offset_y = (upscaled_height - maze_height) / 2

        # 4. Draw light-gray grid lines
        grid_color = "#9393938a"
        for r in range(self.rows + 1):
            y = r * cell_size + offset_y
            draw.line([(offset_x, y), (offset_x + maze_width, y)], fill=grid_color, width=1)
        for c in range(self.cols + 1):
            x = c * cell_size + offset_x
            draw.line([(x, offset_y), (x, offset_y + maze_height)], fill=grid_color, width=1)

        # 5. Draw Walls as Rectangles for continuous, uniform lines
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * cell_size + offset_x
                y1 = r * cell_size + offset_y
                x2 = (c + 1) * cell_size + offset_x
                y2 = (r + 1) * cell_size + offset_y

                if self.grid[r][c].walls['N']:
                    draw.rectangle([(x1 - wall_width/2, y1 - wall_width/2), (x2 + wall_width/2, y1 + wall_width/2)], fill="black")
                if self.grid[r][c].walls['S']:
                    draw.rectangle([(x1 - wall_width/2, y2 - wall_width/2), (x2 + wall_width/2, y2 + wall_width/2)], fill="black")
                if self.grid[r][c].walls['W']:
                    draw.rectangle([(x1 - wall_width/2, y1 - wall_width/2), (x1 + wall_width/2, y2 + wall_width/2)], fill="black")
                if self.grid[r][c].walls['E']:
                    draw.rectangle([(x2 - wall_width/2, y1 - wall_width/2), (x2 + wall_width/2, y2 + wall_width/2)], fill="black")

        # # 6. Draw solution path smoothly
        # if self.solution:
        #     solution_path_pixels = []
        #     for r, c in self.solution:
        #         center_x = c * cell_size + cell_size / 2 + offset_x
        #         center_y = r * cell_size + cell_size / 2 + offset_y
        #         solution_path_pixels.append((center_x, center_y))

        #     solution_width = max(2 * upscale, int(cell_size / 4))
        #     try:
        #         draw.line(solution_path_pixels, fill="red", width=solution_width, joint="curve")
        #     except TypeError:
        #         draw.line(solution_path_pixels, fill="red", width=solution_width)

        # 7. Draw logos (will be smoothed by downsampling)
        start_r, start_c = self.start
        start_center_x = start_c * cell_size + cell_size / 2 + offset_x
        start_center_y = start_r * cell_size + cell_size / 2 + offset_y
        radius = cell_size * 0.25
        draw.ellipse([(start_center_x - radius, start_center_y - radius), (start_center_x + radius, start_center_y + radius)], fill="black")

        end_r, end_c = self.end
        end_center_x = end_c * cell_size + cell_size / 2 + offset_x
        end_center_y = end_r * cell_size + cell_size / 2 + offset_y
        self._draw_star(draw, end_center_x, end_center_y, cell_size * 0.35, "black")

        # 8. Downsample for anti-aliasing and save
        final_image = image.resize((total_width, total_height), Image.Resampling.LANCZOS)
        final_image.save(filename, "JPEG", quality=95)


    def get_solution_coordinates(self):
        """Returns the solution path as a list of coordinates."""
        return self.solution
    
    def get_solution_steps(self):
        """Returns the solution as a sequence of directional steps."""
        if not self.solution:
            return []
        steps = []
        for i in range(len(self.solution) - 1):
            r1, c1 = self.solution[i]
            r2, c2 = self.solution[i+1]
            if r2 > r1:
                steps.append("down")
            elif r2 < r1:
                steps.append("up")
            elif c2 > c1:
                steps.append("right")
            elif c2 < c1:
                steps.append("left")
        return steps
    
    def get_occ_solution_coordinates(self):
        """
        Converts the maze to an occupancy grid and returns its solution path.

        This method provides the solution coordinates corresponding to the
        occupancy grid representation of the maze.

        Returns:
            list: A list of (row, col) coordinate tuples for the solution path
                in the occupancy grid maze.
        """
        occupancy_maze = OccupancyGridMaze(self)
        return occupancy_maze.solution

    def to_json(self, filename="maze.json"):
        """Saves the maze data to a JSON file."""
        grid_data = [[{"walls": cell.walls} for cell in row] for row in self.grid]
        maze_data = {
            "size": {"columns": self.cols, "rows": self.rows},
            "start": self.start, "end": self.end,
            "grid": grid_data #, "solution": self.solution
        }
        with open(filename, 'w') as f:
            json.dump(maze_data, f, indent=4)

    def to_adjacency_list(self, filename="maze_adj.json"):
        """Saves the maze as an adjacency list."""
        nodes = []
        for r in range(self.rows):
            for c in range(self.cols):
                node, neighbors, cell = [r, c], [], self.grid[r][c]
                if not cell.walls['N']: neighbors.append([r - 1, c])
                if not cell.walls['E']: neighbors.append([r, c + 1])
                if not cell.walls['S']: neighbors.append([r + 1, c])
                if not cell.walls['W']: neighbors.append([r, c - 1])
                nodes.append({"node": node, "neighbors": neighbors})
        adj_list = {
            "size": {"columns": self.cols, "rows": self.rows},
            "start": self.start, "end": self.end , "grid": nodes}
        with open(filename, 'w') as f:
            json.dump(adj_list, f, indent=2)

    def to_custom_adjacency_list(self, filename="maze_adj.txt"):
        """Saves the maze as a custom adjacency list format."""
        connections = []
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if not cell.walls['E']: connections.append(f"({r},{c}) <–> ({r},{c+1})")
                if not cell.walls['S']: connections.append(f"({r},{c}) <–> ({r+1},{c})")
        adj_list_str = " ; ".join(connections)
        path_coords = " ".join([f"({r},{c})" for r, c in self.solution])
        output = (f"<ADJLIST_START> {adj_list_str} <ADJLIST_END> "
                  f"<ORIGIN_START>({self.start[0]},{self.start[1]})<ORIGIN_END> "
                  f"<TARGET_START>({self.end[0]},{self.end[1]})<TARGET_END> ")
                #   f"<PATH_START>{path_coords}<PATH_END>")
        with open(filename, 'w') as f:
            f.write(output)

    def to_tokenized_representation(self, filename="maze_tokenized.txt"):
        """Generates a tokenized representation of the maze grid."""
        tokens = []
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                cell_tokens = [f"<|{r}-{c}|>"]
                wall_combo = [d for d, w in [('up', 'N'), ('down', 'S'), ('right', 'E'), ('left', 'W')] if cell.walls[w]]
                if not wall_combo: cell_tokens.append("<|no_wall|>")
                elif len(wall_combo) == 4: cell_tokens.append("<|up_down_left_right_wall|>")
                else: cell_tokens.append(f"<|{''.join(wall_combo)}_wall|>")
                if (r, c) == self.start: cell_tokens.append("<|origin|>")
                elif (r, c) == self.end: cell_tokens.append("<|target|>")
                tokens.extend(cell_tokens)
        with open(filename, 'w') as f:
            f.write(" ".join(tokens))


class OccupancyGridMaze(Maze):
    """
    A class to represent and generate a maze where walls are occupied cells.
    """
    def __init__(self, original_maze):
        self.cols = original_maze.cols
        self.rows = original_maze.rows
        self.grid = [[1 for _ in range(2 * self.cols + 1)] for _ in range(2 * self.rows + 1)]
        self.start = (1, 1)
        self.end = (2 * self.rows - 1, 2 * self.cols - 1)
        self.original_maze = original_maze
        self._convert_from_line_maze()
        self._convert_solution()

    def _convert_from_line_maze(self):
        """Converts a line-based maze to an occupancy grid maze."""
        for r in range(self.original_maze.rows):
            for c in range(self.original_maze.cols):
                cell = self.original_maze.grid[r][c]
                self.grid[2*r + 1][2*c + 1] = 0
                if not cell.walls['N']: self.grid[2*r][2*c + 1] = 0
                if not cell.walls['E']: self.grid[2*r + 1][2*c + 2] = 0
                if not cell.walls['S']: self.grid[2*r + 2][2*c + 1] = 0
                if not cell.walls['W']: self.grid[2*r + 1][2*c] = 0

    def _convert_solution(self):
        """Converts the solution path to the occupancy grid representation."""
        if not self.original_maze.solution:
            self.solution = []
            return
        new_solution = []
        for i in range(len(self.original_maze.solution) - 1):
            r1, c1 = self.original_maze.solution[i]
            r2, c2 = self.original_maze.solution[i+1]
            current_cell_og = (2 * r1 + 1, 2 * c1 + 1)
            if not new_solution or new_solution[-1] != current_cell_og:
                 new_solution.append(current_cell_og)
            new_solution.append((r1 + r2 + 1, c1 + c2 + 1))
        final_r, final_c = self.original_maze.solution[-1]
        final_cell_og = (2 * final_r + 1, 2 * final_c + 1)
        if not new_solution or new_solution[-1] != final_cell_og:
            new_solution.append(final_cell_og)
        self.solution = new_solution

    def to_line_maze(self):
        """Converts the occupancy grid back to a line-based maze."""
        og_rows, og_cols = len(self.grid), len(self.grid[0])
        if og_rows % 2 == 0 or og_cols % 2 == 0:
            raise ValueError("Occupancy grid dimensions must be odd to be converted.")
        line_rows, line_cols = (og_rows - 1) // 2, (og_cols - 1) // 2
        restored_maze = Maze(line_cols, line_rows, _generate=False)
        for r in range(line_rows):
            for c in range(line_cols):
                restored_maze.grid[r][c].walls['N'] = (self.grid[2*r][2*c + 1] == 1)
                restored_maze.grid[r][c].walls['S'] = (self.grid[2*r + 2][2*c + 1] == 1)
                restored_maze.grid[r][c].walls['E'] = (self.grid[2*r + 1][2*c + 2] == 1)
                restored_maze.grid[r][c].walls['W'] = (self.grid[2*r + 1][2*c] == 1)
        restored_maze._solve_maze()
        return restored_maze

    # def to_ascii(self): #this function works but does not include start and end markers
    #     """Returns an ASCII string representation of the occupancy grid maze."""
    #     return "\n".join("".join("#" if cell " " for cell in row) for row in self.grid) + "\n"
    def to_ascii(self):
        """Returns an ASCII string representation of the occupancy grid maze with 'O' and 'T'."""
        # Create an empty list to hold each line of the maze string
        output_lines = []
        
        # Enumerate through the grid to get both the row index (r) and the row's data
        for r, row in enumerate(self.grid):
            # Create an empty list to build the characters for the current line
            line_chars = []
            
            # Enumerate through the row to get both the column index (c) and the cell's value
            for c, cell in enumerate(row):
                # 1. Check if the current coordinate is the start position
                if (r, c) == self.start:
                    line_chars.append('S')
                # 2. Else, check if it's the end position
                elif (r, c) == self.end:
                    line_chars.append('E')
                # 3. Else, check if the cell is a wall (value of 1)
                elif cell == 1:
                    line_chars.append('#')
                # 4. Otherwise, it's an empty path
                else:
                    line_chars.append(' ')
            
            # Join the characters to form the complete line string and add it to our list of lines
            output_lines.append("".join(line_chars))
            
        # Join all the lines with a newline character to form the final maze string
        return "\n".join(output_lines) + "\n"


    def to_jpeg(self, filename="maze_occupancy.jpg", total_width=800, total_height=800):
        """Saves the occupancy grid maze as a high-quality, anti-aliased JPEG image."""
        upscale = 4
        upscaled_width, upscaled_height = total_width * upscale, total_height * upscale
        image = Image.new("RGB", (upscaled_width, upscaled_height), "white")
        draw = ImageDraw.Draw(image)

        og_cols, og_rows = len(self.grid[0]), len(self.grid)
        margin = int(min(upscaled_width, upscaled_height) * 0.05)
        drawing_area = min(upscaled_width, upscaled_height) - 2 * margin
        cell_size = drawing_area / max(og_rows, og_cols)

        maze_width, maze_height = og_cols * cell_size, og_rows * cell_size
        offset_x = (upscaled_width - maze_width) / 2
        offset_y = (upscaled_height - maze_height) / 2


        for r, row in enumerate(self.grid):
            for c, cell_val in enumerate(row):
                x1, y1 = c * cell_size + offset_x, r * cell_size + offset_y
                x2, y2 = (c + 1) * cell_size + offset_x, (r + 1) * cell_size + offset_y
                if cell_val == 1:
                    draw.rectangle([(x1, y1), (x2, y2)], fill="black")

        grid_color = "#9393938a"
        line_width = 1

        # Draw vertical grid lines
        for c in range(og_cols + 1):
            x = c * cell_size + offset_x
            draw.line([(x, offset_y), (x, offset_y + maze_height)], fill=grid_color, width=line_width)

        # Draw horizontal grid lines
        for r in range(og_rows + 1):
            y = r * cell_size + offset_y
            draw.line([(offset_x, y), (offset_x + maze_width, y)], fill=grid_color, width=line_width)

        # if self.solution:
        #     for r, c in self.solution:
        #         x1, y1 = c * cell_size + offset_x, r * cell_size + offset_y
        #         x2, y2 = (c + 1) * cell_size + offset_x, (r + 1) * cell_size + offset_y
        #         draw.rectangle([(x1, y1), (x2, y2)], fill="red")

        start_r, start_c = self.start
        start_center_x = start_c * cell_size + cell_size / 2 + offset_x
        start_center_y = start_r * cell_size + cell_size / 2 + offset_y
        radius = cell_size * 0.4
        draw.ellipse([(start_center_x - radius, start_center_y - radius), (start_center_x + radius, start_center_y + radius)], fill="black")

        end_r, end_c = self.end
        end_center_x = end_c * cell_size + cell_size / 2 + offset_x
        end_center_y = end_r * cell_size + cell_size / 2 + offset_y
        self.original_maze._draw_star(draw, end_center_x, end_center_y, cell_size * 0.45, "black")

        final_image = image.resize((total_width, total_height), Image.Resampling.LANCZOS)
        final_image.save(filename, "JPEG", quality=95)

    def to_json(self, filename="maze_occupancy.json"):
        """Saves the occupancy grid maze data to a JSON file."""
        maze_data = {
            "size": {"columns": len(self.grid[0]), "rows": len(self.grid)},
            "start": self.start, "end": self.end,
            "grid": self.grid #, "solution": self.solution
        }
        with open(filename, 'w') as f:
            json.dump(maze_data, f, indent=4)

    def to_adjacency_list(self, filename="maze_occupancy_adj.json"):
        """Saves the occupancy grid maze as an adjacency list."""
        nodes = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:
                    node, neighbors = [r, c], []
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        n_r, n_c = r + dr, c + dc
                        if (0 <= n_r < len(self.grid) and 0 <= n_c < len(self.grid[0]) and self.grid[n_r][n_c] == 0):
                            neighbors.append([n_r, n_c])
                    nodes.append({"node": node, "neighbors": neighbors})
        adj_list = [{"size": {"columns": len(self.grid[0]), "rows": len(self.grid)},
            "start": self.start, "end": self.end, "grid": nodes}]
        with open(filename, 'w') as f:
            json.dump(adj_list, f, indent=2)

    def to_custom_adjacency_list(self, filename="maze_occupancy_adj.txt"):
        """Saves the occupancy grid maze as a custom adjacency list format."""
        connections = []
        rows_og, cols_og = len(self.grid), len(self.grid[0])
        for r in range(rows_og):
            for c in range(cols_og):
                if self.grid[r][c] == 0:
                    if c + 1 < cols_og and self.grid[r][c+1] == 0:
                        connections.append(f"({r},{c}) <–> ({r},{c+1})")
                    if r + 1 < rows_og and self.grid[r+1][c] == 0:
                        connections.append(f"({r},{c}) <–> ({r+1},{c})")
        adj_list_str = " ; ".join(connections)
        path_coords = " ".join([f"({r},{c})" for r, c in self.solution])
        output = (f"<ADJLIST_START> {adj_list_str} <ADJLIST_END> "
                  f"<ORIGIN_START>({self.start[0]},{self.start[1]})<ORIGIN_END> "
                  f"<TARGET_START>({self.end[0]},{self.end[1]})<TARGET_END> ")
                #   f"<PATH_START>{path_coords}<PATH_END>")
        with open(filename, 'w') as f:
            f.write(output)

    def to_tokenized_representation(self, filename="maze_occupancy_tokenized.txt"):
        """Generates a tokenized representation of the occupancy grid maze."""
        tokens = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                cell_tokens = [f"<|{r}-{c}|>"]
                if self.grid[r][c] == 1:
                    cell_tokens.append("<|occupied_wall|>")
                elif (r, c) == self.start:
                    cell_tokens.append("<|origin|>")
                elif (r, c) == self.end:
                    cell_tokens.append("<|target|>")
                else:
                    cell_tokens.append("<|blank|>")
                tokens.extend(cell_tokens)
        with open(filename, 'w') as f:
            f.write(" ".join(tokens))

if __name__ == "__main__":
    try:
        # --- Configuration for Maze Dimensions ---
        easy_rows, easy_cols = 5 , 5
        # hard_cols, hard_rows = 6 , 6

        # Set a fixed, high-quality image size for all JPEGs
        jpeg_width, jpeg_height = 800, 800

        # --- Process Easy Maze ---
        print(f"--- Generating Easy Maze ({easy_cols}x{easy_rows}) ---")
        easy_maze = Maze(easy_cols, easy_rows)
        easy_occupancy_maze = OccupancyGridMaze(easy_maze)

        # Save all file types for easy maze
        for maze_obj, maze_type in [(easy_maze, "line"), (easy_occupancy_maze, "occupancy")]:
            print(f"\nSaving easy maze files ({maze_type})...")
            maze_obj.to_jpeg(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}.jpg", total_width=jpeg_width, total_height=jpeg_height)
            maze_obj.to_json(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}.json")
            maze_obj.to_adjacency_list(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}_adj.json")
            maze_obj.to_custom_adjacency_list(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}_adj.txt")
            maze_obj.to_tokenized_representation(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}_tokenized.txt")
            with open(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}.txt", "w") as f:
                f.write(maze_obj.to_ascii())
        
            # Save the solution as a string of coordinates
        #     def get_solution_coordinates(self):
        # """Returns the solution path as a list of coordinates."""
        # return self.solution
            # print("before coords")
            # with open(f"maze_easy_line_{easy_rows}x{easy_cols}_solution.txt", "w") as f:
            # f.write(str(hard_maze.get_solution_coordinates()))

            # with open(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}_solution_coordinates.txt", "w") as f:
            #     f.write(", ".join(solution_coords))
            # print("after coords")

            # Save the solution as a sequence of steps

            solution_steps = maze_obj.get_solution_steps()
            with open(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}_solution_steps.txt", "w") as f:
                f.write(", ".join(solution_steps))
            
            # Save the ASCII representation
            # with open(f"maze_easy_{maze_type}_{easy_rows}x{easy_cols}.txt", "w") as f:
            #     f.write(maze_obj.to_ascii())
        
        # Save solution for line-based maze
        with open(f"maze_easy_line_{easy_rows}x{easy_cols}_solution_coords.txt", "w") as f:
            f.write(str(easy_maze.get_solution_coordinates()))

        # Save solution for occupancy grid maze, which is created inside the Maze() class. 
        with open(f"maze_easy_occupancy_{easy_rows}x{easy_cols}_solution_coords.txt", "w") as f:
            f.write(str(easy_maze.get_occ_solution_coordinates()))


        # Save restored file for line-maze
        # restored_easy_maze = easy_occupancy_maze.to_line_maze()   #This is only useful when validating conversions
        # with open(f"maze_easy_line_{easy_rows}x{easy_cols}_restored.txt", "w") as f:
        #     f.write(restored_easy_maze.to_ascii())
        print("\nAll easy maze files saved successfully.")

        # print("\n" + "="*40 + "\n") # Separator

        # # --- Process Hard Maze ---
        # print(f"--- Generating Hard Maze ({hard_rows}x{hard_cols}) ---")
        # hard_maze = Maze(hard_cols, hard_rows)
        # hard_occupancy_maze = OccupancyGridMaze(hard_maze)

        # for maze_obj, maze_type in [(hard_maze, "line"), (hard_occupancy_maze, "occupancy")]:
        #     print(f"\nSaving hard maze files ({maze_type})...")
        #     maze_obj.to_jpeg(f"maze_hard_{maze_type}_{hard_rows}x{hard_cols}.jpg", total_width=jpeg_width, total_height=jpeg_height)
        #     maze_obj.to_json(f"maze_hard_{maze_type}_{hard_rows}x{hard_cols}.json")
        #     maze_obj.to_adjacency_list(f"maze_hard_{maze_type}_{hard_rows}x{hard_cols}_adj.json")
        #     maze_obj.to_custom_adjacency_list(f"maze_hard_{maze_type}_{hard_rows}x{hard_cols}_adj.txt")
        #     maze_obj.to_tokenized_representation(f"maze_hard_{maze_type}_{hard_rows}x{hard_cols}_tokenized.txt")
        #     with open(f"maze_hard_{maze_type}_{hard_rows}x{hard_cols}.txt", "w") as f:
        #         f.write(maze_obj.to_ascii())

        # with open(f"maze_hard_line_{hard_rows}x{hard_cols}_solution.txt", "w") as f:
        #     f.write(str(hard_maze.get_solution_coordinates()))
        # restored_hard_maze = hard_occupancy_maze.to_line_maze()
        # with open(f"maze_hard_line_{hard_rows}x{hard_cols}_restored.txt", "w") as f:
        #     f.write(restored_hard_maze.to_ascii())
        # print("\nAll hard maze files saved successfully.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")