from tkinter import *

window = Tk()
window.geometry("1000x700")
lbListX = []
lbListY = []

inx = 0
for i in range(30, 1000, 35) :
    lbListX.append(Label(window, font = ("굴림체", 10), bg = "red", fg = "blue", text = str(i)))
    lbListX[inx].place(x = i, y = 0)
    inx += 1

inx = 0
for i in range(0, 700, 20) :
    lbListY.append(Label(window, font = ("굴림체", 10), bg = "red", fg = "blue", text = str(i)))
    lbListY[inx].place(x = 0, y = i)
    inx += 1

enX = Entry(window, font = ('굴림체', 10), width = 10)
enY = Entry(window, font = ('굴림체', 10), width = 10)
enText = Entry(window, font = ('굴림체', 10), width = 10)
enX.place(x = 50, y = 640)
enY.place(x = 150, y = 640)
enText.place(x = 250, y = 640)

def fXY() :
    x = enX.get()
    y = enY.get()
    text = enText.get()
    tx = "Ob_Name = Object(window, font = '굴림체', 10), bg = 'red', fg = 'blue', text ="+text+")"
    enCode.delete(0, len(enCode.get()))
    enCode.insert(0, tx)
    lbxy =  Label(window, font = ("굴림체", 10), bg = "red", fg = "blue", text = text)
    lbxy.place(x = x, y = y)

bt = Button(window, font = ("굴림체", 10), text = " go ", command = fXY)
bt.place(x = 350,  y = 640)

enCode = Entry(window, font=("굴림체", 10), width = 130)
enCode.place(x=50, y = 670)

window.mainloop()