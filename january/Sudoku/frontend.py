from generator import *
from sudoku import *
from tkinter import *

def gen_btns(difficulty):
    sudoku = generate(difficulty)
    print(len(btns))
    for btn in range(len(btns)):
        btns[btn].text = sudoku.grid[btn//9][btn%9]
        btns[btn].destroy()
        #btns[-1].grid(row=btn//9, column=btn%9, sticky=N+S+E+W)
        btns[-1].grid(row=btn//9, column=btn%9, sticky=N+S+E+W)

def set_difficulty(diff):
    difficulty = diff

sudoku = Sudoku()
btns = []
difficulty = 'easy'

root = Tk()
root.resizable(False, False)
root.title("Sudoku")

menu=Menu(root)
file=Menu(menu)
file.add_command(label="Generate", command= lambda: gen_btns(difficulty))
file.add_command(label="Easy", command= lambda: set_difficulty('easy'))
file.add_command(label="Medium", command= lambda: set_difficulty('medium'))
file.add_command(label="Hard", command= lambda: set_difficulty('hard'))
file.add_command(label="Reset", command= lambda: Ellipsis)
file.add_command(label="Exit", command= root.quit)

menu.add_cascade(label="Menu", menu=file)
root.config(menu=menu)

for y in range (9):
    for x in range (9):
        if (y in (0,1,2,6,7,8) and x in (3,4,5) or (y in (3,4,5) and x in (0,1,2,6,7,8))):
            color="light gray"
        else:
            color="white"
        btns.append(Button(root, width = 10, height = 5, bg = color, text = 0, fg = "black", font=('Courier', 10), command = lambda: Ellipsis))
        btns[-1].grid(row=y, column=x, sticky=N+S+E+W)
        btns[-1].grid(row=y, column=x, sticky=N+S+E+W)

root.mainloop()