from time import time
from sudoku import *
from solver import *
from inputer import *
from generator import *

example = [[3,4,0,7,0,6,0,0,1],
           [8,7,0,0,0,0,9,0,6],
           [0,0,0,8,9,1,0,0,3],
           [0,0,0,0,0,3,5,6,8],
           [6,8,0,0,5,4,0,0,7],
           [9,1,0,6,0,0,0,0,0],
           [0,3,0,4,0,0,0,8,0],
           [5,9,0,0,0,0,7,3,0],
           [7,0,0,5,3,8,0,1,9]]

sudoku = Sudoku(example)
sudoku.print()
print()
solve(sudoku)
sudoku.print()
print(sudoku.is_win())

input_nums(sudoku)