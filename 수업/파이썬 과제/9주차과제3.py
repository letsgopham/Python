from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    if event.keycode == 37:
        direction = "왼쪽 화살표"
    elif event.keycode == 38:
        direction = "위쪽 화살표"
    elif event.keycode == 39:
        direction = "오른쪽 화살표"
    elif event.keycode == 40:
        direction = "아래쪽 화살표"
    else:
        direction = f"알 수 없는 키 코드 {event.keycode}"
    messagebox.showinfo("키보드 이벤트", f"눌린 키 : Shift + {direction}")

window = Tk()

window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)

window.mainloop()