import sqlite3
from tkinter import *
from tkinter import messagebox

def insertData() :
    connect = sqlite3.connect("D:\\201804011\\sqlite3\\test")
    cursor = connect.cursor()
    data = list(range(4))

    for i in range(4) :
        data[i] = Edts[i]
    
    try :
        cursor.execute("INSERT INTO student VALUES('" + data[0] + "','" + data[1] + "','" + data[2] + "','" + data[3] + "')")
    except :
        messagebox.showerror('오류', '데이터 입력 오류 발생')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    
    connect.commit()
    connect.close()

def selectData() :
    connect = sqlite3.connect("D:\\201804011\\sqlite3\\test")
    cursor = connect.cursor()
    

window = Tk()
window.geometry("600x300")
window.title("GUI 데이터 입력")

edtFrame = Frame(window)
edtFrame.pack()

listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1)

Edts = list()
for i in range(4) :
    Edts.append(Entry(edtFrame, width = 10))
    Edts[i].pack(side = LEFT, padx = 10, pady = 10)

Button(edtFrame, text = "입력", command = insertData).pack(side = LEFT, padx = 10, pady = 10)
Button(edtFrame, text = "조회", command = selectData).pack(side = LEFT, padx = 10, pady = 10)

DataList = list()
for i in range(4) :
    DataList.append(Listbox(listFrame, bg = "white"))
    DataList[i].pack(side = LEFT , fill = BOTH, expand = 1)

window.mainloop()