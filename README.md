
# Prompting LLMs With Perfect Mazes To Investigate Their Ability For Reasoning, Spatial Understanding and Navigation
This project contains codes and datasets that were used to test LLM's ability of spatial reasoning. This knowledge was then used to research the reasoning mechanisms and limitations of a SOTA reasoning LLM, compared to performance of a non-reasoning LLM as a baseline. For this project I used Python version 3.11.4 . 

## Setup

### How to set up the virtual environment
This instruction is specifically tested in a Windows environment. All macOS/Linux instructions are to be used in the terminal and are copied from https://www.w3schools.com/python/python_virtualenv.asp . 
1. In an Anaconda prompt, make a directory and navigate to it
```
mkdir Codes
cd Codes
```
2. Create the environment, called myfirstproject 
```
Windows: C:\Users\Your_Name\Codes> python -m venv myfirstproject
macOS/Linux: $ python -m venv myfirstproject
```
3. To activate the environment, make sure to be within the folder where this environment was created ('C:\Users\Your_Name\Codes' in the previous steps)
```
Windows: C:\Users\Your_Name\Codes> .\myfirstproject\Scripts\activate
macOS/Linux: $ source myfirstproject/bin/activate
```
4. Install the Pillow library within the activated environment to be able to run the _maze_generator_ext_v3.py_ file.
```
Windows: (myfirstproject) C:\Users\Your_Name\Codes> pip install pillow
Linux: $ sudo apt install python3-pil
```
5. To deactivate the environment, run the following command
```
Windows: (myfirstproject) C:\Users\Your_Name\Codes> deactivate
macOS/Linux: (myfirstproject) ... $ deactivate
```
6. Create all your scripts within this folder. They will run within the same clean environment and can securely access the API key. 

### How to add an API key - Hier moet nog mac/linux instructies bij!
1. Inside your virtual environment, install the following libraries by running the following command in the Anaconda prompt while the environment is active
```
Windows: (myfirstproject) C:\Users\Your_Name\Codes> pip install google-generativeai python-dotenv google-genai
```
2. Inside your project folder ('C:\Users\Your_Name\Codes' in the previous steps), create a file called .env
3. Inside the .env file, add your key
```
API_KEY = "YOUR_SECRET_API_KEY_HERE"
```
4. Add the .env file to your .gitignore file. 
5. When a script needs access to your API key, add the following code in the script - DEZE MOET AANGEPAST ZODAT ER 2 KEYS WORDEN GEIMPORTEERD, EN DE NAMEN MOETEN OMSCHRIJVEND ZIJN. ZORG OOK DAT DEZE NAMEN KLOPPEN MET DE NAMEN IN HET VLGENDE HOOFDSTUK WAAR DE .ENV WORDT UITGELEGD.
```
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access your API key
my_api_key = os.getenv("API_KEY")

if not my_api_key:
    raise ValueError("API key not found. make sure it's in yout .env file.")

# ... rest of script
```


## Structure of this folder
```
    Codes
    |   README.md
    |   .env
    |   maze_generator_ext_v3.py
    |   create_dataset.py
    |   autoscore/mazellmcompare/IDK
    |───Dataset 01
    |   |   Dataset 01 2x2
    |   |   Dataset 01 3x3
    |   |   ...
```
* .env
    * A text file that is not included in the git because it contains my API-keys. Create your own and save your API key in the format of: 
    ```
    GEMINI_PRO_API_KEY= "YOUR_SECRET_KEY1"
    GEMINI_FL_API_KEY= "YUOR_SECRET_KEY2"
    ```
* maze_generator__ext_v3.py 
    * A python script that randomly generates perfect mazes of a specified gridsize. It contains three classes; Cell(), Maze() and OccupancyGridMaze(Maze). The Maze() class uses the Cell() object to generate mazes with lines for walls. The OccupancyGridMaze(Maze) class takes the previous Maze object and  transforms it into an occupancy grid maze. For both maze styles, the classes output a JPG, JSON, ASCII, tokenized, textual adjacency list and JSON adjacency list representation. 

* create_dataset.py
    * A python script that calls maze_generator_ext_v3.py to create datasets of mazes with various sizes and saves them in the predetermined 'Dataset 01' folder. 
    

* maze_llm_compare.py
    * a python file .......



# Notes voor Val
Wanneer je je hele code gaat testen, let dan vooral op het volgende:
- wordt de juiste folderstructuur gecreeerd en zijn alle paths relatief? ZORG DAT ALLE PADEN RELATIEF ZIJN !!!
- alle dependencies correct gelist worden in de instructies. Mis ik er geen??