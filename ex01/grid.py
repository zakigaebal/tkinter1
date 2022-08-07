import tkinter
from tkinter import messagebox

def btnClick():
    txt = text.get()
    messagebox.showwarning("test", txt)

win = tkinter.Tk()
win.geometry('300x150')
label = tkinter.Label(win, text="라벨 입니다.")
label.grid(row=0, column=0, pady=10)
text = tkinter.Entry(win)
text.grid(row=1, column=0, padx=10)
button = tkinter.Button(win, text="버튼 입니다.", command=btnClick)
button.grid(row=1, column=1)
win.mainloop()
