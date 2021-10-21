import turtle as tl # pip install turtle
from tkinter import * # pip install tk-tools
t = tl.Turtle()
s = tl.Screen()
s.title('Star')
s.cv._rootwindow.resizable(0,0)
t.color("green")
img = Image("photo",file='./Scr/star-logo.png')
tl._Screen._root.iconphoto(True,img)
t.right(75)
t.forward(100)

for i in range(4):
    t.right(144)
    t.forward(100)

tl.done()
