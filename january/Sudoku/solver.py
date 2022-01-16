def solve(sudoku):
    for y in range(len(sudoku.grid)):
        for x in range(len(sudoku.grid[0])):
            if sudoku.grid[y][x] == 0:
                a = sudoku.possible((x,y))
                if a == []:
                    return
                for i in a:
                    sudoku.set_cell((x,y), i)
                    solve(sudoku)
                    if (sudoku.is_win()):
                        return
                    sudoku.set_cell((x,y), 0)
                return