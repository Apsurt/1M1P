import numpy as np
from os import system
from sudoku import *
from solver import *

def generate(difficulty='easy'):
    if difficulty == 'easy': k = 43
    if difficulty == 'medium': k = 51
    if difficulty == 'hard': k = np.random.randint(53,58)
    #if difficulty == 'expert': k =
    #if difficulty == 'evil': k =
    sudoku = Sudoku()
    #generate diagonal
    for y in range(len(sudoku.grid)):
        for x in range(len(sudoku.grid[0])):
            if y//3 == x//3:
                pos = sudoku.possible((x,y))
                sudoku.set_cell((x,y) ,pos[np.random.randint(0,len(pos))])
    solve(sudoku)
    while k != 0:
        x, y = np.random.randint(0,9, (2))
        if sudoku.grid[y][x] != 0:
            sudoku.set_cell((x,y) ,0)
            k -= 1
    return sudoku