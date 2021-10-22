import turtle as tl # pip install turtle
from tkinter import * # pip install tk-tools
t = tl.Turtle()
s = tl.Screen()
s.title('Turtle Project')

colors = ["green","blue","red","yellow"]
img = Image('photo',file='./Scr/rainbow-scr.png')
tl._Screen._root.iconphoto(True,img)
for x in range(360):
    t.pencolor(colors[x % 4])
    t.width(x/5+1)
    t.forward(x)
    t.left(20)
tl.done()
