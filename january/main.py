from PIL import Image
from asciipng import pic2ascii

path = 'C:\\1M1P\\january\\files\\ferrari.png'
img = Image.open(path).convert('L')

asciiimg = pic2ascii(img, 200)

with open(path[:-4] + ".txt", "w") as f:
    f.write(asciiimg)