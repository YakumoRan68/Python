from tkinter import *
import sqlite3

root = Tk()

root.title = "성적 처리"
root.geometry("400x500")
root.resizable(False, False)

MasterFrame = Frame(root, padx = 20, pady = 20)

Frames = dict()
Widgets = dict()

def CreateFrame(Name, RootFrame, **kwargs) :
    Frames[Name] = Frame(RootFrame, bd = 1, relief="solid", **kwargs)

    return Frames[Name]

def MakeLabeledEntry(Name, Width, Text, RootFrame, **kwargs) :
    Frame = CreateFrame(Name + "Frame", RootFrame)

    Widgets[Name] = Entry(Frame, width = Width, **kwargs)
    Widgets[Name].grid(row = 0, column = 0)
    Widgets[Name + "Label"] = Label(Frame, width = 6, text = Text)
    Widgets[Name + "Label"].grid(row = 0, column = 1)

def PackLabeledEntry(Name, **kwargs) :
    Frames[Name + "Frame"].pack(side = LEFT, fill = "x", expand = True)

IdFrame = CreateFrame("IdFrame", MasterFrame, height = 30, padx = 10)
MakeLabeledEntry("StudentId", 10, "학번", IdFrame)
MakeLabeledEntry("Name", 10, "성명", IdFrame)

PackLabeledEntry("StudentId")
PackLabeledEntry("Name")

IdFrame.pack(anchor = "n", side = LEFT, fill = "x", expand = True)

MasterFrame.pack(expand = True, fill = "both")

root.mainloop()