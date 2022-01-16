from msilib.schema import Error
from os import system
from time import sleep

def solve(sudoku):
    for y in range(len(sudoku.grid)):
        for x in range(len(sudoku.grid[0])):
            if sudoku.grid[y][x] == 0:
                a = sudoku.possible((x,y))
                _ = system('cls')
                sudoku.print()
                print(a)
                print(x,y)
                input()
                for i in a:
                    sudoku.set_cell((x,y), i)
                    if not(sudoku.is_win()):
                        solve(sudoku)
                        sudoku.set_cell((x,y), 0)