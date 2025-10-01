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
        self._generate_maze()
        self._solve_maze()

    def _generate_maze(self):
        """
        Generates the maze structure using a randomized Depth-First Search algorithm.
        This ensures a unique maze with a single solution.
        """
        stack = []
        current_cell = self.grid[self.start[0]][self.start[1]]
        current_cell.visited = True
        stack.append(self.start)

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
            else:
                stack.pop()
    
    def _get_unvisited_neighbors(self, row, col):
        """
        Gets the unvisited neighbors of a cell.

        Args:
            row (int): The row of the cell.
            col (int): The column of the cell.

        Returns:
            list: A list of (row, col) tuples for unvisited neighbors.
        """
        neighbors = []
        # Check neighbors in random order
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # E, W, S, N
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
        if r1 == r2: # Same row, different columns
            if c1 > c2: # Moving left (West)
                self.grid[r1][c1].walls['W'] = False
                self.grid[r2][c2].walls['E'] = False
            else: # Moving right (East)
                self.grid[r1][c1].walls['E'] = False
                self.grid[r2][c2].walls['W'] = False
        else: # Same column, different rows
            if r1 > r2: # Moving up (North)
                self.grid[r1][c1].walls['N'] = False
                self.grid[r2][c2].walls['S'] = False
            else: # Moving down (South)
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

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # E, W, S, N
                n_row, n_col = current_row + dr, current_col + dc

                if (0 <= n_row < self.rows and
                        0 <= n_col < self.cols and
                        (n_row, n_col) not in visited):

                    # Check if there is a wall between the current and neighbor cell
                    if (dr == 0 and dc == 1 and not self.grid[current_row][current_col].walls['E']) or \
                       (dr == 0 and dc == -1 and not self.grid[current_row][current_col].walls['W']) or \
                       (dr == 1 and dc == 0 and not self.grid[current_row][current_col].walls['S']) or \
                       (dr == -1 and dc == 0 and not self.grid[current_row][current_col].walls['N']):
                        
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
        output = ""
        # Top border
        output += " " + "_ " * self.cols + "\n"
        
        for r, row in enumerate(self.grid):
            line = "|"
            for c, cell in enumerate(row):
                if cell.walls['S']:
                    line += "_"
                else:
                    line += " "
                
                if cell.walls['E']:
                    line += "|"
                else:
                    line += " "
            
            output += line + "\n"
        return output

    def to_jpeg(self, filename="maze.jpg", cell_size=20):
        """
        Saves the maze as a JPEG image.

        Args:
            filename (str): The name of the output file.
            cell_size (int): The size of each cell in pixels.
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

        image.save(filename, "JPEG")

    def get_solution_coordinates(self):
        """
        Returns the solution path as a list of coordinates.

        Returns:
            list: A list of (row, col) tuples for the solution path.
        """
        return self.solution

    def to_json(self, filename="maze.json"):
        """
        Saves the maze data to a JSON file.

        Args:
            filename (str): The name of the output file.
        """
        grid_data = []
        for row in self.grid:
            row_data = []
            for cell in row:
                row_data.append({"walls": cell.walls, "visited": cell.visited})
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

if __name__ == "__main__":
    try:
        # --- Configuration for Maze Dimensions ---
        easy_cols, easy_rows = 3, 3
        hard_cols, hard_rows = 5, 5

        # --- Create and Save the Easy Maze ---
        print(f"--- Generating Easy Maze ({easy_cols}x{easy_rows}) ---")
        easy_maze = Maze(easy_cols, easy_rows)
        
        print("Saving easy maze files...")
        easy_maze.to_jpeg(f"maze_easy_{easy_cols}x{easy_rows}.jpg")
        print(f"Maze image saved to maze_easy_{easy_cols}x{easy_rows}.jpg")
        easy_maze.to_json(f"maze_easy_{easy_cols}x{easy_rows}.json")
        print(f"Maze data saved to maze_easy_{easy_cols}x{easy_rows}.json")
        with open(f"maze_easy_{easy_cols}x{easy_rows}.txt", "w") as f:
            f.write(easy_maze.to_ascii())
        print(f"ASCII maze saved to maze_easy_{easy_cols}x{easy_rows}.txt")
        with open(f"maze_easy_{easy_cols}x{easy_rows}_solution.txt", "w") as f:
            f.write(str(easy_maze.get_solution_coordinates()))
        print(f"Solution coordinates saved to maze_easy_{easy_cols}x{easy_rows}_solution.txt")
        print("Easy maze files saved successfully.")

        print("\n" + "="*40 + "\n") # Separator

        # --- Create and Save the Hard Maze ---
        print(f"--- Generating Hard Maze ({hard_cols}x{hard_rows}) ---")
        hard_maze = Maze(hard_cols, hard_rows)

        print("Saving hard maze files...")
        hard_maze.to_jpeg(f"maze_hard_{hard_cols}x{hard_rows}.jpg")
        print(f"Maze image saved to maze_hard_{hard_cols}x{hard_rows}.jpg")
        hard_maze.to_json(f"maze_hard_{hard_cols}x{hard_rows}.json")
        print(f"Maze data saved to maze_hard_{hard_cols}x{hard_rows}.json")
        with open(f"maze_hard_{hard_cols}x{hard_rows}.txt", "w") as f:
            f.write(hard_maze.to_ascii())
        print(f"ASCII maze saved to maze_hard_{hard_cols}x{hard_rows}.txt")
        with open(f"maze_hard_{hard_cols}x{hard_rows}_solution.txt", "w") as f:
            f.write(str(hard_maze.get_solution_coordinates()))
        print(f"Solution coordinates saved to maze_hard_{hard_cols}x{hard_rows}_solution.txt")
        print("All hard maze files saved successfully.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")