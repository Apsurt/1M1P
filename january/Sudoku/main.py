from sudoku import Sudoku

example = [[0,0,9,0,6,5,0,2,0],
           [0,6,0,0,0,4,5,8,0],
           [5,0,8,0,2,9,7,0,0],
           [9,0,0,6,0,8,4,7,2],
           [0,0,0,9,1,7,0,0,8],
           [6,0,0,0,0,0,9,0,1],
           [0,4,5,0,0,0,8,0,0],
           [7,0,0,5,8,1,3,0,4],
           [0,0,0,7,0,3,2,0,0]]

def fill_ones():
    for y in range(len(sudoku.grid)):
        for x in range(len(sudoku.grid[0])):
            possible = sudoku.possible((x,y))
            if len(possible) == 1:
                sudoku.set_cell((x,y), possible[0])
                #print(x,y,possible)
                
sudoku = Sudoku(example)
sudoku.print()
print(sudoku.check())