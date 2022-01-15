from PIL import Image
import cv2
from os import remove, system
from asciipng import pic2ascii
from time import sleep, time

def clear():
    system('cls')

vidcap = cv2.VideoCapture("C:\\1M1P\\january\\files\\zerotwo.mp4")

width = 50

frameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidcap.get(cv2.CAP_PROP_FPS)
duration = frameCount/fps

targetfps = 10
targetFrameCount = int(duration*targetfps)
print(targetfps, targetFrameCount)

def saveFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        #IMPROVE !!!!!!
        cv2.imwrite("C:\\1M1P\\january\\buffer\\frame"+str(i)+".png", image)
        with open("C:\\1M1P\\january\\buffer\\frame"+str(i)+".txt", 'w') as f:
            f.write(pic2ascii(Image.open("C:\\1M1P\\january\\buffer\\frame"+str(i)+".png"), width))
        remove("C:\\1M1P\\january\\buffer\\frame"+str(i)+".png")
    return hasFrames

#start = time()
#
#sec = 0
#for i in range(targetFrameCount):
#    print(str(round(i/targetFrameCount * 100, 2))+"%")
#    saveFrame(sec)
#    sec += 1/targetfps
#    sec = round(sec, 2)
#    
#print(time() - start)

for i in range(targetFrameCount):
    frameStartTime = time()
    with open ("C:\\1M1P\\january\\screen.txt", "w") as screen:
        with open("C:\\1M1P\\january\\buffer\\frame"+str(i)+".txt", 'r') as f:
            screen.write(f.read())
            sleep(1/targetfps - (time() - frameStartTime))