import ctypes
import time
import os
def pausecds():
    pause=input("DELAY >>>")
    try:
        pause=float(pause)
    except:
        pause=pausecds()
    if pause<1:
        print("test")
        pausecds()
    return pause
pause=pausecds()
def getpath(path):
    i=0
    v=False
    while i<=len(path) and v==False:
        if path[len(path)-i-1]== "\\":
            v=True
        else:
            i+=1
    return path[:len(path)-i-1]
path=getpath(os.path.abspath(__file__)) 
print(path+r"\images") 
images=os.listdir(path+r"\images")
for i in range(len(images)):
    os.rename(path+r"\images\{}".format(images[i]),path+r"\images\image{}.jpg".format(i))
images=os.listdir(path+"/images")
for i in range(len(images)):
    os.rename(path+r"\images\{}".format(images[i]),path+r"\images\image{}.jpeg".format(i))
images=os.listdir(path+r"\images")
SPI_SETDESKWALLPAPER = 20 
try:
    f=open(path+r"\save.txt","r")
    i=int(f.readline())
    f.close()
except:
    i=0
print(i)
while True:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path+r"\images\image{}.jpeg".format(i) , 0)
    if i>=(len(images)-1):
       i=0
    else:
        i+=1
    f=open(path+r"\save.txt","w")
    f.write("{}".format(i))
    f.close()
    time.sleep(pause)