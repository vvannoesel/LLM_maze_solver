# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 10:08:42 2025

@author: valer

Made by Gemini 2.5 pro, prompt: 
"please write me a python script that takes as input a grid size as number of columns x number of rows. 
the output should be a unique, solvable maze with one solution. 
The maze should be outputted as jpeg, as ASCII representation, as coordinates and in JSON format."
follow up:
"If i want to create multiple mazes at once, such as easy_maze = Maze(10,10) and hard_maze = Maze(50,50)
how do i do this? and how do i make sure they get stored under these names? 
i want the number of rows and columns to be variable using easy_rows, easy_cols, hard_rows and hard_cols. 
I want to also use these variables in the printed statements and names of the files. Can you help me?"
"""
import random
import json
import collections
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

    def __init__(self, cols, rows):
        """
        Initializes the Maze object.

        Args:
            cols (int): The number of columns for the maze.
            rows (int): The number of rows for the maze.
        """
        if cols <= 0 or rows <= 0:
            raise ValueError("Columns and rows must be positive integers.")
        self.cols = cols
        self.rows = rows
        # Grid of Cell objects
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.start = (0, 0)
        self.end = (rows - 1, cols - 1)
        self.solution = None
        self.dfs_path = []  # Stores the path for tokenization
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
            current_cell = self.grid[current_row][current_col]

            neighbors = self._get_unvisited_neighbors(current_row, current_col)

            if neighbors:
                next_row, next_col = random.choice(neighbors)
                next_cell = self.grid[next_row][next_col]

                # Knock down walls between current and next cell
                self._remove_walls(current_row, current_col, next_row, next_col)

                next_cell.visited = True
                stack.append((next_row, next_col))
                self.dfs_path.append((next_row, next_col))
            else:
                stack.pop()
                if stack:
                    # Move back in the DFS path
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
        if r1 == r2:  # Same row, different columns
            if c1 > c2:  # Moving left (West)
                self.grid[r1][c1].walls['W'] = False
                self.grid[r2][c2].walls['E'] = False
            else:  # Moving right (East)
                self.grid[r1][c1].walls['E'] = False
                self.grid[r2][c2].walls['W'] = False
        else:  # Same column, different rows
            if r1 > r2:  # Moving up (North)
                self.grid[r1][c1].walls['N'] = False
                self.grid[r2][c2].walls['S'] = False
            else:  # Moving down (South)
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

            # Check neighbors and their walls
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
    
    def to_ascii(self):
        """
        Returns an ASCII string representation of the maze.
        
        Returns:
            str: The maze in ASCII format.
        """
        output = "+" + "---+" * self.cols + "\n"
        for r, row in enumerate(self.grid):
            line1 = "|"
            line2 = "+"
            for c, cell in enumerate(row):
                # Path/Cell part
                line1 += "   "
                if cell.walls['E']:
                    line1 += "|"
                else:
                    line1 += " "
                
                # Bottom wall part
                if cell.walls['S']:
                    line2 += "---"
                else:
                    line2 += "   "
                line2 += "+"
            output += line1 + "\n" + line2 + "\n"
        return output

    def to_jpeg(self, filename="maze.jpg", cell_size=20, total_width=None, total_height=None):
        """
        Saves the maze as a JPEG image.

        Args:
            filename (str): The name of the output file.
            cell_size (int): The size of each cell in pixels.
            total_width (int): The final image width in pixels.
            total_height (int): The final image height in pixels.
        """
        width = self.cols * cell_size
        height = self.rows * cell_size
        
        image = Image.new("RGB", (width + 1, height + 1), "white")
        draw = ImageDraw.Draw(image)

        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                x1, y1 = c * cell_size, r * cell_size
                x2, y2 = (c + 1) * cell_size, (r + 1) * cell_size

                if cell.walls['N']:
                    draw.line([(x1, y1), (x2, y1)], fill="black", width=2)
                if cell.walls['E']:
                    draw.line([(x2, y1), (x2, y2)], fill="black", width=2)
                if cell.walls['S']:
                    draw.line([(x1, y2), (x2, y2)], fill="black", width=2)
                if cell.walls['W']:
                    draw.line([(x1, y1), (x1, y2)], fill="black", width=2)
        
        # Draw solution path
        if self.solution:
            solution_path_pixels = []
            for r, c in self.solution:
                center_x = c * cell_size + cell_size // 2
                center_y = r * cell_size + cell_size // 2
                solution_path_pixels.append((center_x, center_y))
            
            draw.line(solution_path_pixels, fill="red", width=3)
        
        if total_width and total_height:
            resized_image = image.resize((total_width, total_height), Image.Resampling.NEAREST)
            resized_image.save(filename, "JPEG")
        else:
            image.save(filename, "JPEG")

    def get_solution_coordinates(self):
        """
        Returns the solution path as a list of coordinates.
        """
        return self.solution

    def to_json(self, filename="maze.json"):
        """
        Saves the maze data to a JSON file.
        """
        grid_data = []
        for row in self.grid:
            row_data = []
            for cell in row:
                row_data.append({"walls": cell.walls})
            grid_data.append(row_data)

        maze_data = {
            "size": {"columns": self.cols, "rows": self.rows},
            "start": self.start,
            "end": self.end,
            "grid": grid_data,
            "solution": self.solution
        }
        with open(filename, 'w') as f:
            json.dump(maze_data, f, indent=4)
    
    def to_adjacency_list(self, filename="maze_adj.json"):
        """
        Saves the maze as an adjacency list.
        """
        adj_list = []
        for r in range(self.rows):
            for c in range(self.cols):
                node = [r, c]
                neighbors = []
                cell = self.grid[r][c]
                if not cell.walls['N']:
                    neighbors.append([r - 1, c])
                if not cell.walls['E']:
                    neighbors.append([r, c + 1])
                if not cell.walls['S']:
                    neighbors.append([r + 1, c])
                if not cell.walls['W']:
                    neighbors.append([r, c - 1])
                
                adj_list.append({"node": node, "neighbors": neighbors})
        
        with open(filename, 'w') as f:
            json.dump(adj_list, f, indent=2)

    def to_tokenized_representation(self, filename="maze_tokenized.txt"):
        """
        Saves the maze as a tokenized string.
        """
        token_map = {
            (0, 1): 'E', (0, -1): 'W', (1, 0): 'S', (-1, 0): 'N'
        }
        tokens = []
        
        # The DFS path contains both forward and backward movements.
        for i in range(len(self.dfs_path) - 1):
            curr_r, curr_c = self.dfs_path[i]
            next_r, next_c = self.dfs_path[i+1]
            dr, dc = next_r - curr_r, next_c - curr_c
            
            if (dr, dc) in token_map:
                tokens.append(token_map[(dr, dc)])
            else:
                # Should not happen in a valid maze, but for safety
                tokens.append('BACK') 
        
        tokenized_string = " ".join(tokens)
        with open(filename, 'w') as f:
            f.write(tokenized_string)


class OccupancyGridMaze(Maze):
    """
    A class to represent and generate a maze where walls are occupied cells.
    Inherits from Maze to use the same generation algorithm.
    """
    def __init__(self, original_maze):
        self.cols = original_maze.cols
        self.rows = original_maze.rows
        # Create an expanded grid for occupancy representation
        self.grid = [[1 for _ in range(2 * self.cols + 1)] for _ in range(2 * self.rows + 1)]
        self.start = (1, 0)
        self.end = (2 * self.rows - 1, 2 * self.cols)
        self.solution = []
        
        self._convert_from_line_maze(original_maze)
        self._convert_solution(original_maze)

    def _convert_from_line_maze(self, line_maze):
        """
        Converts a line-based maze to an occupancy grid maze.
        """
        for r in range(line_maze.rows):
            for c in range(line_maze.cols):
                cell = line_maze.grid[r][c]
                # Carve out path for each cell
                self.grid[2*r + 1][2*c + 1] = 0
                
                # Carve out paths between cells if walls are down
                if not cell.walls['N']:
                    self.grid[2*r][2*c + 1] = 0
                if not cell.walls['E']:
                    self.grid[2*r + 1][2*c + 2] = 0
                if not cell.walls['S']:
                    self.grid[2*r + 2][2*c + 1] = 0
                if not cell.walls['W']:
                    self.grid[2*r + 1][2*c] = 0
        
        # Create entrance and exit
        self.grid[self.start[0]][self.start[1]] = 0
        self.grid[self.end[0]][self.end[1]] = 0

    def _convert_solution(self, line_maze):
        """
        Converts the solution path from the line-based maze to the
        occupancy grid representation.
        """
        if not line_maze.solution:
            return
        
        # Start and end
        self.solution.append(self.start)
        for i in range(len(line_maze.solution) - 1):
            r1, c1 = line_maze.solution[i]
            r2, c2 = line_maze.solution[i+1]
            
            # Add the path cell
            path_cell_r, path_cell_c = (r1 + r2) + 1, (c1 + c2) + 1
            self.solution.append((path_cell_r, path_cell_c))
            
            # Add the space between cells
            next_cell_r, next_cell_c = (2 * r2) + 1, (2 * c2) + 1
            self.solution.append((next_cell_r, next_cell_c))
        
        self.solution.append(self.end)
    
    def to_ascii(self):
        """
        Returns an ASCII string representation of the occupancy grid maze.
        """
        output = ""
        for row in self.grid:
            for cell in row:
                output += "#" if cell == 1 else " "
            output += "\n"
        return output
    
    def to_jpeg(self, filename="maze_occupancy.jpg", cell_size=10, total_width=None, total_height=None):
        """
        Saves the occupancy grid maze as a JPEG image.
        """
        width = (2 * self.cols + 1) * cell_size
        height = (2 * self.rows + 1) * cell_size
        
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)

        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    draw.rectangle(
                        [(c * cell_size, r * cell_size), ((c + 1) * cell_size, (r + 1) * cell_size)],
                        fill="black"
                    )
        
        if self.solution:
            for r, c in self.solution:
                draw.rectangle(
                    [(c * cell_size, r * cell_size), ((c + 1) * cell_size, (r + 1) * cell_size)],
                    fill="red"
                )
        
        if total_width and total_height:
            resized_image = image.resize((total_width, total_height), Image.Resampling.NEAREST)
            resized_image.save(filename, "JPEG")
        else:
            image.save(filename, "JPEG")
            
    def to_json(self, filename="maze_occupancy.json"):
        """
        Saves the occupancy grid maze data to a JSON file.
        """
        maze_data = {
            "size": {"columns": self.cols, "rows": self.rows},
            "start": self.start,
            "end": self.end,
            "grid": self.grid,
            "solution": self.solution
        }
        with open(filename, 'w') as f:
            json.dump(maze_data, f, indent=4)
    
    def to_adjacency_list(self, filename="maze_occupancy_adj.json"):
        """
        Saves the occupancy grid maze as an adjacency list.
        """
        adj_list = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:  # Only add nodes for paths
                    node = [r, c]
                    neighbors = []
                    # Check 4 directions
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        n_r, n_c = r + dr, c + dc
                        if (0 <= n_r < len(self.grid) and 
                            0 <= n_c < len(self.grid[0]) and
                            self.grid[n_r][n_c] == 0):
                            neighbors.append([n_r, n_c])
                    
                    adj_list.append({"node": node, "neighbors": neighbors})
        
        with open(filename, 'w') as f:
            json.dump(adj_list, f, indent=2)

    def to_tokenized_representation(self, filename="maze_occupancy_tokenized.txt"):
        """
        Generates a tokenized representation of the occupancy grid maze.
        
        This is a conceptual implementation as the paper's tokenization
        is based on a line-based DFS traversal. This version simply
        tokenizes the solution path.
        """
        token_map = {
            (0, 1): 'E', (0, -1): 'W', (1, 0): 'S', (-1, 0): 'N'
        }
        tokens = []
        
        for i in range(len(self.solution) - 1):
            curr_r, curr_c = self.solution[i]
            next_r, next_c = self.solution[i+1]
            dr, dc = next_r - curr_r, next_c - curr_c
            
            if (dr, dc) in token_map:
                tokens.append(token_map[(dr, dc)])
            else:
                tokens.append('BACK') 
        
        tokenized_string = " ".join(tokens)
        with open(filename, 'w') as f:
            f.write(tokenized_string)
            

if __name__ == "__main__":
    try:
        # --- Configuration for Maze Dimensions ---
        easy_cols, easy_rows = 4, 4
        hard_cols, hard_rows = 5, 5
        
        # Set a fixed image size for all JPEGs
        jpeg_width, jpeg_height = 500, 500

        # --- Create and Save the Easy Maze (Line-based) ---
        print(f"--- Generating Easy Maze ({easy_cols}x{easy_rows}) ---")
        easy_maze = Maze(easy_cols, easy_rows)
        
        print("Saving easy maze files (line-based)...")
        easy_maze.to_jpeg(f"maze_easy_line_{easy_cols}x{easy_rows}.jpg", total_width=jpeg_width, total_height=jpeg_height)
        print(f"Maze image saved to maze_easy_line_{easy_cols}x{easy_rows}.jpg")
        easy_maze.to_json(f"maze_easy_line_{easy_cols}x{easy_rows}.json")
        print(f"Maze data saved to maze_easy_line_{easy_cols}x{easy_rows}.json")
        easy_maze.to_adjacency_list(f"maze_easy_line_{easy_cols}x{easy_rows}_adj.json")
        print(f"Adjacency list saved to maze_easy_line_{easy_cols}x{easy_rows}_adj.json")
        easy_maze.to_tokenized_representation(f"maze_easy_line_{easy_cols}x{easy_rows}_tokenized.txt")
        print(f"Tokenized representation saved to maze_easy_line_{easy_cols}x{easy_rows}_tokenized.txt")
        with open(f"maze_easy_line_{easy_cols}x{easy_rows}.txt", "w") as f:
            f.write(easy_maze.to_ascii())
        print(f"ASCII maze saved to maze_easy_line_{easy_cols}x{easy_rows}.txt")
        with open(f"maze_easy_line_{easy_cols}x{easy_rows}_solution.txt", "w") as f:
            f.write(str(easy_maze.get_solution_coordinates()))
        print(f"Solution coordinates saved to maze_easy_line_{easy_cols}x{easy_rows}_solution.txt")
        print("Easy maze files (line-based) saved successfully.")
        
        # --- Convert to Occupancy Grid and Save Files ---
        print("\n--- Converting Easy Maze to Occupancy Grid ---")
        easy_occupancy_maze = OccupancyGridMaze(easy_maze)
        
        print("Saving easy maze files (occupancy grid)...")
        easy_occupancy_maze.to_jpeg(f"maze_easy_occupancy_{easy_cols}x{easy_rows}.jpg", total_width=jpeg_width, total_height=jpeg_height)
        print(f"Occupancy grid image saved to maze_easy_occupancy_{easy_cols}x{easy_rows}.jpg")
        easy_occupancy_maze.to_json(f"maze_easy_occupancy_{easy_cols}x{easy_rows}.json")
        print(f"Occupancy grid data saved to maze_easy_occupancy_{easy_cols}x{easy_rows}.json")
        easy_occupancy_maze.to_adjacency_list(f"maze_easy_occupancy_{easy_cols}x{easy_rows}_adj.json")
        print(f"Occupancy grid adjacency list saved to maze_easy_occupancy_{easy_cols}x{easy_rows}_adj.json")
        easy_occupancy_maze.to_tokenized_representation(f"maze_easy_occupancy_{easy_cols}x{easy_rows}_tokenized.txt")
        print(f"Occupancy grid tokenized representation saved to maze_easy_occupancy_{easy_cols}x{easy_rows}_tokenized.txt")
        with open(f"maze_easy_occupancy_{easy_cols}x{easy_rows}.txt", "w") as f:
            f.write(easy_occupancy_maze.to_ascii())
        print(f"Occupancy grid ASCII saved to maze_easy_occupancy_{easy_cols}x{easy_rows}.txt")
        print("All easy maze files saved successfully.")

        print("\n" + "="*40 + "\n") # Separator

        # --- Create and Save the Hard Maze (Line-based) ---
        print(f"--- Generating Hard Maze ({hard_cols}x{hard_rows}) ---")
        hard_maze = Maze(hard_cols, hard_rows)

        print("Saving hard maze files (line-based)...")
        hard_maze.to_jpeg(f"maze_hard_line_{hard_cols}x{hard_rows}.jpg", total_width=jpeg_width, total_height=jpeg_height)
        print(f"Maze image saved to maze_hard_line_{hard_cols}x{hard_rows}.jpg")
        hard_maze.to_json(f"maze_hard_line_{hard_cols}x{hard_rows}.json")
        print(f"Maze data saved to maze_hard_line_{hard_cols}x{hard_rows}.json")
        hard_maze.to_adjacency_list(f"maze_hard_line_{hard_cols}x{hard_rows}_adj.json")
        print(f"Adjacency list saved to maze_hard_line_{hard_cols}x{hard_rows}_adj.json")
        hard_maze.to_tokenized_representation(f"maze_hard_line_{hard_cols}x{hard_rows}_tokenized.txt")
        print(f"Tokenized representation saved to maze_hard_line_{hard_cols}x{hard_rows}_tokenized.txt")
        with open(f"maze_hard_line_{hard_cols}x{hard_rows}.txt", "w") as f:
            f.write(hard_maze.to_ascii())
        print(f"ASCII maze saved to maze_hard_line_{hard_cols}x{hard_rows}.txt")
        with open(f"maze_hard_line_{hard_cols}x{hard_rows}_solution.txt", "w") as f:
            f.write(str(hard_maze.get_solution_coordinates()))
        print(f"Solution coordinates saved to maze_hard_line_{hard_cols}x{hard_rows}_solution.txt")
        print("Hard maze files (line-based) saved successfully.")
        
        # --- Convert to Occupancy Grid and Save Files ---
        print("\n--- Converting Hard Maze to Occupancy Grid ---")
        hard_occupancy_maze = OccupancyGridMaze(hard_maze)
        
        print("Saving hard maze files (occupancy grid)...")
        hard_occupancy_maze.to_jpeg(f"maze_hard_occupancy_{hard_cols}x{hard_rows}.jpg", total_width=jpeg_width, total_height=jpeg_height)
        print(f"Occupancy grid image saved to maze_hard_occupancy_{hard_cols}x{hard_rows}.jpg")
        hard_occupancy_maze.to_json(f"maze_hard_occupancy_{hard_cols}x{hard_rows}.json")
        print(f"Occupancy grid data saved to maze_hard_occupancy_{hard_cols}x{hard_rows}.json")
        hard_occupancy_maze.to_adjacency_list(f"maze_hard_occupancy_{hard_cols}x{hard_rows}_adj.json")
        print(f"Occupancy grid adjacency list saved to maze_hard_occupancy_{hard_cols}x{hard_rows}_adj.json")
        hard_occupancy_maze.to_tokenized_representation(f"maze_hard_occupancy_{hard_cols}x{hard_rows}_tokenized.txt")
        print(f"Occupancy grid tokenized representation saved to maze_hard_occupancy_{hard_cols}x{hard_rows}_tokenized.txt")
        with open(f"maze_hard_occupancy_{hard_cols}x{hard_rows}.txt", "w") as f:
            f.write(hard_occupancy_maze.to_ascii())
        print(f"Occupancy grid ASCII saved to maze_hard_occupancy_{hard_cols}x{hard_rows}.txt")
        print("All hard maze files saved successfully.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")