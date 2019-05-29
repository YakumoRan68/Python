from tkinter import *
import tkinter.messagebox

def parse() :
    try : 
        int(Op[0].get())
        int(Op[1].get())
    except Exception:
        tkinter.messagebox.showinfo("오류", "잘못된 입력입니다.")
        return -1

def add() :
    result["text"] = str(int(Op[0].get()) + int(Op[1].get()))

def sub() :
    result["text"] = str(int(Op[0].get()) - int(Op[1].get()))

def mul() :
    result["text"] = str(int(Op[0].get()) * int(Op[1].get()))

def div() :
    result["text"] = str(int(Op[0].get()) / int(Op[1].get()))

window = Tk()

window.title("계산기")
window.resizable(width = FALSE, height = TRUE)

opFrame = Frame(window)
buttonsFrame = Frame(window)
resultFrame = Frame(window)

opFrame.pack()

Op = list()
for i in range(2) :
    Op.append(Entry(opFrame))
    Op[i].pack(side = LEFT)

result = Label(resultFrame, width = 5, height = 1, anchor = NE)

buttonsFrame.pack()
Buttons = dict()
for v in ["add", "sub", "mul", "div"] :
    Buttons[v] = Button(buttonsFrame, text = v, width = 3, height = 3, command = globals()[v])
    Buttons[v].pack(side = LEFT)

resultFrame.pack()
result.pack()

window.mainloop()