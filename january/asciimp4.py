from PIL import Image
import cv2
from os import remove, system
from asciipng import pic2ascii
from time import sleep, time

def clear():
    system('cls')

vidcap = cv2.VideoCapture("C:\\1M1P\\january\\files\\zerotwo.mp4")

width = 150

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        #IMPROVE !!!!!!
        cv2.imwrite("C:\\1M1P\\january\\temp\\temp.png", image)
        with open("C:\\1M1P\\january\\temp\\temp.txt", 'w') as f:
            f.write(pic2ascii(Image.open("C:\\1M1P\\january\\temp\\temp.png"), width))
        remove("C:\\1M1P\\january\\temp\\temp.png")
    return hasFrames

sec = 0
fps = 4
success = getFrame(sec)
while success:
    sec += (1/fps)
    sec = round(sec, 2)
    getFrame(sec)