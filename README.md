
# Prompting LLMs With Perfect Mazes To Investigate Their Ability For Reasoning, Spatial Understanding and Navigation
This project contains codes and datasets that were used to test LLM's ability of spatial reasoning. This knowledge was then used to research the reasoning mechanisms and limitations of a SOTA reasoning LLM, compared to performance of a non-reasoning LLM as a baseline. For this project I used Python version 3.11.4.

## Index
* [Setup](#setup)
* [Structure of this project](#structure-of-this-project)
* [Creating a dataset](#creating-a-dataset)
* [Calling the API](#calling-the-api)

## Setup
This project uses Python version 3.11.4 and all instructions are specifically for Windows systems. If you are familiar with setting up environments and API keys, skip to the section [How to set up dependencies](#how-to-set-up-dependencies) for a full list of necessary installs. 


### How to set up the virtual environment
All instructions are for Windows.

1. In an Anaconda prompt window, navigate to the folder where you cloned or forked this repository to. We will refer to this folder as 'LLM_maze_solver'.
2. Create the environment, called 'my_env'. In the commandline type the following:
```
 conda create -n my_env python=3.11.4
```
reply 'yes' to complete the installation.


3. To activate the environment, again navigate to the folder that contains the environment ( C:\Users\Your_Name\LLM_maze_solver ) , and use:
```
conda acivate my_env
```
To deactivate the environment, use:
```
conda deactivate
```






### How to enable API calling
1. Inside your project folder ('C:\Users\Your_Name\LLM_maze_solver' in the previous steps), create a file called .env

2. Add the .env file to your .gitignore file. 
3. Inside the .env file, add your key. Make sure it is called 'GEMINI_API_KEY' as this is called in the tesT.py and tesT_2.py files. 
```
GEMINI_API_KEY = "YOUR_SECRET_API_KEY_HERE"
```




### How to set up dependencies
Inside your virtual environment, install the following libraries:

```
Python 3.11.4
NumPy 
Matplotlib 
Scipy 
Pandas 
PIL/Pillow: may be automatically included in the Matplotlib installation
Dataframe_image
Google Genai: to call Google Gemini API
```
by running the following Windows commands in the Anaconda prompt while the environment is active. PIL/Pillow may be automatically included in the Matplotlib installation.
```
pip install numpy
```
```
pip install matplotlib
```
```
pip install pillow
```
```
python -m pip install scipy
```
```
pip install pandas
```
```
pip install dataframe_image
```
```
pip install google-generativeai python-dotenv google-genai
```



## Structure of this project
```
    LLM_maze_solver
    |   my_env/ (optional, if you followed the setup instructions in full)
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
## Creating a Dataset
This project allows two ways to create a dataset. Either you create multiple mazes of the same size (row x col), or you create one square maze for each size, within specified size boundaries.
### One Size - Multiple Mazes
- Inputs: dataset directory, maze rows and columns
- Outputs: the specified directory (if it did not exist) containing separate folders for each maze. Each folder has the name "_directory_name_ _size_ _postfix_number_" (eg. "Dataset 01 3x3 1"). The postfix number is used to distinguish each maze, so you will have mazes 1,2,3,4,5,6,... of your desired size. 

Use **create_dataset_of_same_complexity.py**. This file uses the maze_generator_ext_v3.py file to recurrently create mazes. First, specify the directory you want to use, by including the name of the directory in the **create_test_directory(rows, cols, k)** function, as _give_your_dataset_a_name_. Then, in the **main()**, specify the number of rows and columns your mazes should have, and what the postfix numbers of the files should be. This would ordinarily start at 1, but if you want to append an existing dataset, set it to whatever value the existing dataset contains. 

### Many Sizes - One Maze for Each
- Inputs: dataset directory, lower bound for maze rows and columns, upper bound for maze rows and columns
- Outputs: the specified directory (if it did not exist) containing separate folders for each maze. Each folder has the name "_directory_name_ _size_" (eg. "Dataset 01 3x3").

Use **create_dataset_of_same_complexity.py**. This file uses the maze_generator_ext_v3.py file to recurrently create mazes. First, specify the directory you want to use, by including the name of the directory in the **create_test_directory(rows, cols, k)** function, as _give_your_dataset_a_name_. Then, in the **main()**, specify the minimum and maximum number of rows and columns your mazes should have, by changing the values for 'i' and 'j'. Note that this script only creates square mazes.   

## Calling the API
### How to run tests
Using the files tesT.py and tesT_2.py, we can run the mazes through the APIs of Gemini 2.5 Flash-Lite and Gemini 2.5 Pro, respectively. Before you run, specify the following: 
*   MAZE_ROWS and MAZE_COLS in lines 27 and 28, describing the nxn size of the mazes 
* Which output frame of reference (FoR) to use, by **selecting and deselecting specific sections of main()**. The sections are marked in the code, but the line numbers are also listed below. 
* Only if you want to run the test on a new dataset, replace the 'file_path' directory path in the import\_maze_file( ) function.

Lines to uncomment:

| Output frame of reference (FoR)  | tesT.py |tesT_2.py|
| -------- | ------- |--------|
| Coordinates  | 637-736   | 648-746 |
| Allocentric|  436-531 | 444-540 |
| Egocentric   | 534-631  |545-640 |


### How the results are stored
After running the test, the LLM output is saved in a file called comparison_report_{LLM}\_{FoR}_{n}.md. **BEWARE** : if you run the test on the existing dataset, your new comparison report will replace the existing report.

All quantitative data is stored in arrays in separate files. In all cases, nxn is replaced by the maze size.
* The comparison scores are saved in a file called _scores_Dataset03_nxn.py_.
* The number of input tokens as reported by Gemini's metadata are saved in a file called _prompt_tokens_Dataset03_nxn.py_.
* The number of output tokens as reported by Gemini's metadata are saved in a file called _output_tokens_Dataset03_nxn.py_.
* The number of consecutive correct steps counted from the start of the answer until the first mistake, is saved in a file called _raw_scores_Dataset03_nxn.py_.

# Notes voor Val
Wanneer je je hele code gaat testen, let dan vooral op het volgende:
- wordt de juiste folderstructuur gecreeerd en zijn alle paths relatief? ZORG DAT ALLE PADEN RELATIEF ZIJN !!!

