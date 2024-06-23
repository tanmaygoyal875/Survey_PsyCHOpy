# PsychoPy Quiz Project

## Overview
This project is a simple quiz application developed using PsychoPy, a library for creating psychology experiments in Python. The quiz consists of a series of questions where participants are required to write the correct word for given jumbled ones. The participant's responses, response times, and correctness of answers are recorded and saved to a CSV file.

## Installation
To run this project, you'll need to have the following installed:

- Python 3.x
- PsychoPy (`pip install psychopy`)

## Files
- `main.py`: The main script to run the quiz.
- `participant_responses.csv`: A CSV file to store participant responses.

## Usage
1. Ensure you have Python and PsychoPy installed.
2. Place the script (`main.py`) and the CSV file (`participant_responses.csv`) in the desired directory.
3. Run the script using a Python interpreter.

## Instructions
1. Upon running the script, a window will appear with instructions.
2. Press `Enter` to start the quiz.
3. For each question, type your answer in the response box and press `Enter` to submit.
4. The quiz consists of 17 questions.
5. At the end of the quiz, a message will appear thanking you for your participation.
6. Your responses, response times, and correctness will be saved in `participant_responses.csv`.

## Code Explanation

### Imports
```python
import csv
import os.path
import time
from psychopy import visual, core, event, gui
```
