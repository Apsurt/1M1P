from PIL import Image

def pic2ascii(img, width, height = 0):
    signs = "@%#*+=-:. "
    img = img.convert('L')
    if height == 0:
        oldWidth, oldHeight = img.size
        ratio = oldHeight / oldWidth
        height = int(width * ratio)
    img = img.resize((width, height))
    
    pixels = img.getdata()
    asciiString = "".join([signs[int(pixel // 25.5000001)] for pixel in pixels])
    asciiString = "\n".join([asciiString[i:i+width] for i in range(0, len(asciiString), width)])
    asciiString = " ".join(asciiString)
    
    return asciiString