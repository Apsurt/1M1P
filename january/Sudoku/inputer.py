from pyautogui import *
from time import sleep

def input_nums(sudoku):
    sleep(2)
    press('left', presses=9)
    press('up', presses=9)
    
    for y in range(len(sudoku.grid)):
        if y%2 == 0:
            for x in range(len(sudoku.grid)):
                press(str(sudoku.grid[y][x]))
                press('right')
        else:
            for x in range(len(sudoku.grid)-1, -1, -1):
                press(str(sudoku.grid[y][x]))
                press('left')
        press('down')