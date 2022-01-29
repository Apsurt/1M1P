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

def screen_box(name, box, click):
    moveTo(click[0], click[1])
    screenshot(region=(*box, 200, 200)).save('C:\\1M1P\january\Sudoku\\files\\'+str(name)+'st_sqr.png')

def get_sudoku():
    hotkey('alt', 'tab')
    screen_box(1, (370,200), (570, 400))
    screen_box(2, (550,200), (370, 400))
    hotkey('alt', 'tab')