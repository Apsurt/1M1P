from time import time
from sudoku import *
from solver import *

example = [[3,0,6,4,5,0,0,0,0],
           [0,0,0,6,0,0,0,2,0],
           [1,8,0,0,7,0,0,0,5],
           [9,1,4,5,0,7,6,0,3],
           [0,0,0,1,0,3,0,4,0],
           [6,0,7,9,0,8,5,1,2],
           [4,6,0,0,0,0,2,7,0],
           [0,0,8,0,1,0,0,0,0],
           [0,0,0,7,0,0,8,0,6]]

start = time()

sudoku = Sudoku(example)
sudoku.print()
print()
solve(sudoku)
sudoku.print()
print(sudoku.is_win())

print(time() - start)