from tkinter import *
import sqlite3

window = Tk()

window.title = "성적 처리"
window.geometry("400x500")
window.resizable(False, False)

Objects = dict()

def MakeLabledEntry(name, root, **kwargs) :
    Objects[name] = Entry(root, **kwargs)

    ObjectPosition = Objects[name].coor 
    Objects[name + "Lable"] = Lable(root, width = 30, )

MasterFrame = Frame(window, padx = 20, pady = 20)

StudentId = Entry(IdFrame)
StudentId.pack(anchor = "w")

MasterFrame.pack(expand = True, fill = "both")

window.mainloop()