from tkinter import *
from time import *

fnameList = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]

photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file= 'gif/' + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    label1.configure(text=fnameList[num])
    label1.pack()

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file= 'gif/' + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    label1.configure(text=fnameList[num])
    label1.pack()
    
window = Tk()
window.geometry('700x500')
window.title('사진 앨범 보기')

btnPrev = Button(window, text = '<< 이전', command = clickPrev)
btnNext = Button(window, text = '다음 >>', command = clickNext)

photo = PhotoImage(file = 'gif/' + fnameList[0])
pLabel = Label(window, image = photo)
label1 = Label(window, text=fnameList[num])

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)
label1.place(x = 350, y = 10)

window.mainloop()