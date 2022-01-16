from re import X
from sudoku import *
from numpy import random

def generate(sudoku):
    for box in sudoku.box:
        for cell in box:
            pass