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
import collections #this module is needed to use 'deque' for the BFS solver
from PIL import Image, ImageDraw

class Maze:
    """
    A class to represent and generate a maze.

    Attributes:
        cols (int): The number of columns in the maze.
        rows (int): The number of rows in the maze.
        grid (list): A 2D list representing the maze structure.
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
        # The grid is initialized to be twice the size to accommodate walls
        self.grid = [[1 for _ in range(2 * cols + 1)] for _ in range(2 * rows + 1)]
        self.start = (1, 0)
        self.end = (2 * rows - 1, 2 * cols)
        self.solution = None
        self._generate_maze()
        self._solve_maze()

    def _generate_maze(self):
        """
        Generates the maze structure using a randomized Depth-First Search algorithm.
        This ensures a unique maze with a single solution.
        """
        # Stack for the DFS algorithm
        stack = [(1, 1)]
        self.grid[1][1] = 0  # Start cell

        while stack:
            current_row, current_col = stack[-1]
            neighbors = self._get_unvisited_neighbors(current_row, current_col)

            if neighbors:
                next_row, next_col = random.choice(neighbors)

                # Carve path to the neighbor
                self.grid[next_row][next_col] = 0
                self.grid[(current_row + next_row) // 2][(current_col + next_col) // 2] = 0
                
                stack.append((next_row, next_col))
            else:
                stack.pop()
        
        # Create entrance and exit
        self.grid[self.start[0]][self.start[1]] = 0
        self.grid[self.end[0]][self.end[1]] = 0

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
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            n_row, n_col = row + dr, col + dc
            if 0 < n_row < 2 * self.rows and 0 < n_col < 2 * self.cols and self.grid[n_row][n_col] == 1:
                neighbors.append((n_row, n_col))
        return neighbors
    
    def _solve_maze(self): #BFS!!!
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

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                n_row, n_col = current_row + dr, current_col + dc

                if (0 <= n_row < 2 * self.rows + 1 and
                        0 <= n_col < 2 * self.cols + 1 and
                        self.grid[n_row][n_col] == 0 and
                        (n_row, n_col) not in visited):
                    
                    visited.add((n_row, n_col))
                    new_path = list(path)
                    new_path.append((n_row, n_col))
                    queue.append(((n_row, n_col), new_path))

    # def _solve_maze(self): #DFS!
    #     """
    #     Solves the maze using a Depth-First Search algorithm.
    #     """
    #     stack = [(self.start, [self.start])]
    #     visited = {self.start}

    #     while stack:
    #         (current_row, current_col), path = stack.pop()

    #         if (current_row, current_col) == self.end:
    #             self.solution = path
    #             return

    #         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #             n_row, n_col = current_row + dr, current_col + dc

    #             if (0 <= n_row < 2 * self.rows + 1 and
    #                     0 <= n_col < 2 * self.cols + 1 and
    #                     self.grid[n_row][n_col] == 0 and
    #                     (n_row, n_col) not in visited):
                    
    #                 visited.add((n_row, n_col))
    #                 new_path = list(path)
    #                 new_path.append((n_row, n_col))
    #                 stack.append(((n_row, n_col), new_path))
    
    def to_ascii(self):
        """
        Returns an ASCII string representation of the maze.
        
        Returns:
            str: The maze in ASCII format.
        """
        output = ""
        for row in self.grid:
            for cell in row:
                output += "#" if cell == 1 else " "
            output += "\n"
        return output

    def to_jpeg(self, filename="maze.jpg", cell_size=10):
        """
        Saves the maze as a JPEG image.

        Args:
            filename (str): The name of the output file.
            cell_size (int): The size of each cell in pixels.
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
        
        # # Draw solution path if it exists
        # if self.solution:
        #     for r, c in self.solution:
        #         draw.rectangle(
        #             [(c * cell_size, r * cell_size), ((c + 1) * cell_size, (r + 1) * cell_size)],
        #             fill="red"
        #         )

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
        maze_data = {
            "size": {"columns": self.cols, "rows": self.rows},
            "start": self.start,
            "end": self.end,
            "grid": self.grid,
            "solution": self.solution
        }
        with open(filename, 'w') as f:
            json.dump(maze_data, f, indent=4)

#For creating multiple mazes at once and saving them under different names, us this code
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





##For creating one maze at a time, use this code
# if __name__ == "__main__":
#     try:
#         # --- Configuration ---
#         # You can change the number of columns and rows here
#         COLS = 5
#         ROWS = 5
        
#         # --- Maze Generation ---
#         print(f"Generating a {COLS}x{ROWS} maze...")
#         maze = Maze(COLS, ROWS)
#         print("Maze generation complete.")

#         # --- ASCII Output ---
#         print("\n--- ASCII Representation ---")
#         ascii_maze = maze.to_ascii()
#         print(ascii_maze)
#         with open("maze.txt", "w") as f:
#             f.write(ascii_maze)
#         print("ASCII maze saved to maze.txt")

#         # --- JPEG Output ---
#         print("\n--- JPEG Output ---")
#         maze.to_jpeg("maze.jpg")
#         print("Maze image saved to maze.jpg")

#         # --- Coordinates Output ---
#         print("\n--- Solution Coordinates ---")
#         solution_coords = maze.get_solution_coordinates()
#         print(f"Solution path has {len(solution_coords)} steps.")
#         # print(solution_coords) # Uncomment to see all coordinates
#         with open("solution_coordinates.txt", "w") as f:
#             f.write(str(solution_coords))
#         print("Solution coordinates saved to solution_coordinates.txt")


#         # --- JSON Output ---
#         print("\n--- JSON Output ---")
#         maze.to_json("maze.json")
#         print("Maze data saved to maze.json")

#     except ValueError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
