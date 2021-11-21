import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import time
import imutils

# dimension of our app
setheight=350
setwidth=600

#tkinter 
window=tkinter.Tk()
window.title("Decision Review System")
cv2image=cv2.cvtColor(cv2.imread("drs.jpg"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=setwidth,height=setheight)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2image))
imageoncanvas=canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()


stream=cv2.VideoCapture("clip.mp4")

def play(speed):
    global stream
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed , frame=stream.read()
    frame=imutils.resize(frame,width=setwidth,height=setheight)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    
def refer(decision):
    #image of drs refered
    frame=cv2.cvtColor(cv2.imread("desicionpending.jpg"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=setwidth,height=setheight)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #2 sec wait
    time.sleep(2)

    #image of out or not out 
    if decision =="out":
        decision_img="out.jpg"
    else:
        decision_img="notout.jpg"
    frame=cv2.cvtColor(cv2.imread(decision_img),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=setwidth,height=setheight)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

def out():
    thread=threading.Thread(target=refer,args=("out",))
    thread.daemon=1
    thread.start()
    print("player is out")

def notout():
    thread=threading.Thread(target=refer,args=("not out",))
    thread.daemon=1
    thread.start()
    print("Player is Not Out")

#Desicion buttons
btn=tkinter.Button(window,text="Previous (SLOW)",width=30,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="Previous (Fast)",width=30,command=partial(play,-20))
btn.pack()

btn=tkinter.Button(window,text="  Next   (SLOW)",width=30,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text="  Next (Fast)",width=30,command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text="   GIve OUT",width=20,command=out)
btn.pack()

btn=tkinter.Button(window,text="  Give Not Out",width=20,command=notout)
btn.pack()

window.mainloop()