from PIL import Image 
import tkinter as tk
from tkinter import filedialog as fd, ttk
from asciipng import pic2ascii

filetypes = (('Images', '*.png'), ('Videos', '*.mp4'))

def setPath():
    path = fd.askopenfilename(title='Open a file', initialdir='C:\\1M1P\\january\\files', filetypes=filetypes)
    setPathRoot.destroy()
    
    screen = tk.Tk()
    screen.attributes('-fullscreen', True)

    asciitext = tk.Label(screen, font = ("Courier", 3), text=pic2ascii(Image.open(path), 400))
    asciitext.pack(expand=True)

    screen.mainloop()

setPathRoot = tk.Tk()
setPathRoot.title('Set path')
setPathRoot.resizable(False, False)
setPathRoot.geometry('300x150')

button = ttk.Button(setPathRoot, text='Set path', command=setPath)
button.pack(expand=True)

setPathRoot.mainloop()