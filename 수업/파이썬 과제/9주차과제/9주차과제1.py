from tkinter import *
from random import *

btnList = [None]*9
fnameList = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]
photoList = [None]*9
i,k = 0,0
xPos,yPos = 0,0
num = 0

window = Tk()
window.geometry("810x810")
shuffle(photoList)

for i in range(0,9):
    photoList[i] = PhotoImage(file= "gif/"+fnameList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num] = Button(window, image=photoList[num], width=270, height=270)
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 270
    xPos = 0
    yPos += 270

window.mainloop()