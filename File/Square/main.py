import turtle as tl
from tkinter import *
t = tl.Turtle()
s = tl.Screen()
s.title('Square')
s.cv._rootwindow.resizable(0,0)
t.width(4)
t.color("green")
t.fillcolor("green")
t.begin_fill()
img = Image('photo',file = './Scr/Square-logo.png')
tl._Screen._root.iconphoto(True,img)
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
tl.done()
