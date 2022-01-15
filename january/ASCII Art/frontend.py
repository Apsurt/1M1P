from PIL import Image 
import tkinter as tk
from tkinter import filedialog as fd, ttk
from asciipng import pic2ascii

#consts
fileimages = (('Images', '*.png'))
filevideos = (('Videos', '*.mp4'))
width = 300
title = "    ___   _____ ______________   ___    ____  ______\n   /   | / ___// ____/  _/  _/  /   |  / __ \/_  __/\n  / /| | \__ \/ /    / / / /   / /| | / /_/ / / /   \n / ___ |___/ / /____/ /_/ /   / ___ |/ _, _/ / /    \n/_/  |_/____/\____/___/___/  /_/  |_/_/ |_| /_/     \n"                                                    

class App:
    def __init__(self):
        #init root
        self.mainApp = tk.Tk()
        self.mainApp.title("ASCII Art")
        self.mainApp.resizable(False, False)
        self.mainApp.attributes('-fullscreen', True)
        self.mainApp.geometry('720x405')

    #button functions
    def displayImage(self):
        path = fd.askopenfilename(title='Open a file', initialdir='C:\\1M1P\\january\\ASCII Art\\files')
        print(path)
        
        screen = tk.Tk()
        screen.attributes('-fullscreen', True)
        screen.resizable(False, False)
        screen.title("Screen")
        
        asciiString = pic2ascii(Image.open(path), width)
        asciiLabel = tk.Label(screen, text=asciiString, font=("Courier", 3))
        asciiLabel.pack(expand=True)
        
        def buttonCommand():
            screen.destroy()
            self.__init__()
            self.show()
        
        button = ttk.Button(screen, text="Exit", command=buttonCommand)
        button.pack()
        
        self.mainApp.destroy()
        screen.mainloop()

    #main
    def show(self):        
        #init logo
        logo = tk.Label(self.mainApp, text=title, font=("Courier", 12), pady=20)
        logo.pack()

        #create buttons
        imgFrame = tk.Frame(self.mainApp)
        imgFrame.pack(expand=True)
        buttonImg = ttk.Button(imgFrame, text="Set image path", command=self.displayImage)
        buttonImg.pack()
        
        buttonExit = ttk.Button(self.mainApp, text="Exit", command=self.mainApp.destroy)
        buttonExit.pack(side="bottom")

        self.mainApp.mainloop()