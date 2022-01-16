from tkinter import *

root = Tk()
root.resizable(False, False)
root.title("Sudoku")

menu=Menu(root)
file=Menu(menu)
file.add_command(label="Generate", command= lambda: Ellipsis)
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
        btn=Button(root, width = 10, height = 5, bg = color, text = 0, fg = "black", command = lambda: Ellipsis)   
        btn.grid(row=y, column=x, sticky=N+S+E+W)
        btn.grid(row=y, column=x, sticky=N+S+E+W)

root.mainloop()