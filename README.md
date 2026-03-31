
# Prompting LLMs With Perfect Mazes To Investigate Their Ability For Reasoning, Spatial Understanding and Navigation
This project contains codes and datasets that were used to test LLM's ability of spatial reasoning. This knowledge was then used to research the reasoning mechanisms and limitations of a SOTA reasoning LLM, compared to performance of a non-reasoning LLM as a baseline. For this project I used Python version 3.11.4 . 

## Setup

### How to set up the virtual environment
All instructions are for Windows.
1. In an Anaconda prompt, make a directory and navigate to it
```
mkdir Codes
cd Codes
```
2. Create the environment, called myfirstproject 
```
Windows: C:\Users\Your_Name\Codes> python -m venv myfirstproject
```
3. To activate the environment, make sure to be within the folder where this environment was created ('C:\Users\Your_Name\Codes' in the previous steps)
```
Windows: C:\Users\Your_Name\Codes> .\myfirstproject\Scripts\activate
```

4. To deactivate the environment, run the following command
```
Windows: (myfirstproject) C:\Users\Your_Name\Codes> deactivate
```
5. Create all your scripts within this folder. They will run within the same clean environment and can securely access the API key. 

### How to set up dependencies
1. Inside your virtual environment, install the following libraries:

```
NumPy - to support large arrays and mathematical operations
Matplotlib - to create charts
Scipy - for data analysis
Pandas - for making tables
PIL/Pillow: to create maze images
Google Genai: to call Google Gemini API
```

 by running the following command in the Anaconda prompt while the environment is active
```
Windows: 
(myfirstproject) C:\Users\Your_Name\Codes> pip install numpy
(myfirstproject) C:\Users\Your_Name\Codes> pip install matplotlib
(myfirstproject) C:\Users\Your_Name\Codes> python -m pip install scipy
(myfirstproject) C:\Users\Your_Name\Codes> pip install pandas
(myfirstproject) C:\Users\Your_Name\Codes> pip install pillow
(myfirstproject) C:\Users\Your_Name\Codes> pip install google-generativeai python-dotenv google-genai
```
2. Inside your project folder ('C:\Users\Your_Name\Codes' in the previous steps), create a file called .env

3. Add the .env file to your .gitignore file. 
4. Inside the .env file, add your key
```
API_KEY = "YOUR_SECRET_API_KEY_HERE"
```



## Structure of this project
```
    Codes
    |   README.md
    |   .env
    |   maze_generator_ext_v3.py    (file that generates all mazes)
    |   create_dataset.py           
    |   create_dataset_of_same_complexity.py  
    |   tesT.py                     
    |   tesT_2.py   
    |   results_Dataset03_3x3.py    
    |   results_Dataset03_6x6.py
    |   results_Dataset03_15x15.py  
    |   keyword_search.py          
    |   score_saver.py
    |   token_count_extracter.py
    |───Charts_Dataset03/   (directory that contains all chart-plotting code)
    |───Results_charts      (contains all resulting chart images)
    |───Dataset 01\
    |───Dataset 02 - Statistical analysis\
    |───Dataset 03
    |   |   Dataset 03 3x3 01
    |   |   Dataset 03 3x3 02
    |   |   ... 
```

* maze_generator__ext_v3.py 
    * A python script that randomly generates perfect mazes of a specified gridsize. It contains three classes; Cell(), Maze() and OccupancyGridMaze(Maze). The Maze() class uses the Cell() object to generate mazes with lines for walls. The OccupancyGridMaze(Maze) class takes the previous Maze object and  transforms it into an occupancy grid maze. For both maze styles, the classes output a JPG, JSON, ASCII, tokenized, textual adjacency list and JSON adjacency list representation. \n
    The Maze() class uses Randomized Depth-First Search (DFS) is used to generate the mazes, and Breadth-First Search (BFS) is used to solve the mazes. The solution to the maze is saved and output as a text file, optionally also as a red line in the image output. 

* create_dataset.py
    * A python script that calls maze_generator_ext_v3.py to create datasets of mazes with various sizes and saves them in the predetermined 'Dataset 01' folder. The maximum complexity of the mazes can be modified in the main() function. 

* create_dataset_of_same_complexity.py  
    * A python script that calls maze_generator_ext_v3.py to create a whole dataset of nxn mazes and saves them in the predetermined 'Dataset 01' folder. The maximum complexity of the mazes can be modified in the main() function.
    
* tesT.py
    * A python file that is used to import an existing maze from a child directory called 'Dataset 01/Dataset 01 {Maze rows}x{Maze cols}'. This maze is iteratively used to prompt a non-reasoning LLM to solve the maze. The LLM's response is saved and automatically scored against the ground-truth solution and saved in a single .md file inside the maze's folder. 

* tesT_2.py
    * A python file that is used to import an existing maze from a child directory called 'Dataset 01/Dataset 01 {Maze rows}x{Maze cols}'. This maze is iteratively used to prompt a reasoning LLM to solve the maze. The LLM's response is saved as a tuple of [final answer (str), thought summary (str)] and automatically scored against the ground-truth solution and saved in a single .md file inside the maze's folder. 
* score_saver.py
    * A python script that stores the scores from tesT.py and tesT_2.py in a numpy array in a file called 'scores_nonreasoning_Dataset01.py. These arrays can be used to create charts. The score is saved to an array with a name similar to the tested file's name.  The score is saved to the [row-2]'nd index of the array, so a 2x2 maze score is saved on the 0th index, 3x3 score on the 1st index, etc. This file is called within the tesT.py and tesT_2.py files. 
* Dataset01 and Dataset02
    * Directories containing the datasets that were used in preliminary orientation tests. 
* Dataset03
    * **Final Dataset**. Used for the final tests and results. Directory contains all input mazes and output LLM answers. 
* results_Dataset03_nxn.py
    * Files containing arrays of completion score, token counts, and absolute number of correct steps counted until the first mistake. These are the final quantitative results that are used in the Charts_Dataset03\ files.
* keyword_search.py
    * A file that contains all keyword search terms and the code to perform the analysis. Uses all LLM outputs in Dataset03, and creates file 'category_occurrence.py' to generate arrays with keyword occurrences. Can specify which maze size and output frame of reference to use in the main() function. 
* score_saver.py and token_count_extracter.py
    * Files that score the LLMs' output, save their scores and filter the metadata to save the number of input and output tokens as arrays.
# Creating a Dataset
This project allows two ways to create a dataset. Either you create multiple mazes of the same size (row x col), or you create one square maze for each size, within specified size boundaries.
## One Size - Multiple Mazes
- Inputs: dataset directory, maze rows and columns
- Outputs: the specified directory (if it did not exist) containing separate folders for each maze. Each folder has the name "_directory_name_ _size_ _postfix_number_" (eg. "Dataset 01 3x3 1"). The postfix number is used to distinguish each maze, so you will have mazes 1,2,3,4,5,6,... of your desired size. 

Use **create_dataset_of_same_complexity.py**. This file uses the maze_generator_ext_v3.py file to recurrently create mazes. First, specify the directory you want to use, by including the name of the directory in the **create_test_directory(rows, cols, k)** function, as _give_your_dataset_a_name_. Then, in the **main()**, specify the number of rows and columns your mazes should have, and what the postfix numbers of the files should be. This would ordinarily start at 1, but if you want to append an existing dataset, set it to whatever value the existing dataset contains. 

## Many Sizes - One Maze for Each
- Inputs: dataset directory, lower bound for maze rows and columns, upper bound for maze rows and columns
- Outputs: the specified directory (if it did not exist) containing separate folders for each maze. Each folder has the name "_directory_name_ _size_" (eg. "Dataset 01 3x3").

Use **create_dataset_of_same_complexity.py**. This file uses the maze_generator_ext_v3.py file to recurrently create mazes. First, specify the directory you want to use, by including the name of the directory in the **create_test_directory(rows, cols, k)** function, as _give_your_dataset_a_name_. Then, in the **main()**, specify the minimum and maximum number of rows and columns your mazes should have, by changing the values for 'i' and 'j'. Note that this script only creates square mazes.   

# Calling the API


# Notes voor Val
Wanneer je je hele code gaat testen, let dan vooral op het volgende:
- wordt de juiste folderstructuur gecreeerd en zijn alle paths relatief? ZORG DAT ALLE PADEN RELATIEF ZIJN !!!

