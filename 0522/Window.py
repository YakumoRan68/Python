from tkinter import *

def add():
    label1["text"] = str(int(entry1.get()) + int(entry2.get()))

window = Tk()

window.title("윈도우 창 연습")
window.geometry("700x500")
window.resizable(width = FALSE, height = TRUE)

frame1 = Frame(window, width = 300, height = 200)
frame2 = Frame(window)

label1= Label(frame1, text= "서일대학교 축제", width = 30, height = 5, font = ("궁서체", 30), fg = "red", bg = "yellow", anchor = NE)

button1 = Button(frame2, text="버튼 연습", width = 10, height = 5, command= add)
entry1 = Entry(frame2)
entry2 = Entry(frame2)

frame1.pack()
frame2.pack()
label1.pack()
button1.pack(side = LEFT)
entry1.pack(side = LEFT)
entry2.pack(side = LEFT)

window.mainloop()
