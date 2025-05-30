from tkinter import *
window = Tk()

photo1 = PhotoImage(file = 'gif/1.gif')
photo2 = PhotoImage(file = 'gif/2.gif')

Label1 = Label(window, image = photo1)
Label2 = Label(window, image = photo2)

Label1.pack(side=LEFT)
Label2.pack(side=LEFT)

window.mainloop()