from time import time
from sudoku import *
from solver import *
from inputer import *

example = [[0,0,0,7,8,0,4,0,5],
           [0,5,0,4,0,9,0,0,0],
           [0,7,0,0,2,0,0,0,1],
           [0,0,0,2,0,0,1,9,0],
           [3,0,2,1,9,0,8,6,0],
           [0,0,7,8,0,3,0,0,0],
           [7,3,0,9,0,8,6,1,2],
           [0,1,0,0,7,0,3,5,0],
           [0,0,5,3,1,2,0,0,9]]

start = time()

sudoku = Sudoku(example)
sudoku.print()
print()
solve(sudoku)
sudoku.print()
print(sudoku.is_win())

print(time() - start)

input_nums(sudoku)