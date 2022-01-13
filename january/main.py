import numpy as np
from PIL import Image

signs = "@%#*+=-:. "

def pic2ascii(path, width, height = 0):
    img = Image.open(path).convert('L')
    if height == 0:
        oldWidth, oldHeight = img.size
        ratio = oldHeight / oldWidth
        height = int(width * ratio)
    img = img.resize((width, height))
    
    pixels = img.getdata()
    print("".join([signs[int(pixel // 25.5000001)] for pixel in pixels]))
    #Image.fromarray(pixels).save("C:\\1M1P\\january\\test_gray.png")

pic2ascii("test.png", 50)