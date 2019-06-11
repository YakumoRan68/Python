from tkinter import *
import sqlite3
import tkinter.messagebox

def GetGrade(num) :
    if num >= 90:
        return 'A'
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    elif num >= 60:
        return "D"
    elif num >= 50:
        return 'E'
    elif num >= 40:
        return "F"

def fDataLoading():
    con = sqlite3.connect("student")
    cur = con.cursor()
    sqlstr = 'select * from std order by s_hakbun'
    cur.execute(sqlstr)
    inx = 0
    while(True):
        row = cur.fetchone()
        if row == None:
            break
        total = row[2] + row[3] + row[4]

        ListStr = ("{0:5s}|{1:5s}|{2:3d}|{3:3d}|{4:3d}|{5:3d}|{6:3s}". format(row[0], row[1], row[2], row[3], row[4], total, GetGrade(total)))
        ViewList.insert(inx, ListStr)
        inx += 1
    con.close()

def fJumsuTot(event):
    middle = enMiddle.get()
    last = enLast.get()
    attend = enAttend.get()
    if middle.isdigit() and last.isdigit() and attend.isdigit():
        tot = int(middle) + int(last) + int(attend)
        lbTotView['text'] = str(tot)
        lbHakView['text'] = GetGrade(tot)

def fInput():
    hakbun = enHakbun.get()
    name = enName.get()
    middle = enMiddle.get()
    last = enLast.get()
    attend = enAttend.get()
    if (hakbun == '' or name == '' or middle == '' or last == '' or attend == ''):
        tkinter.messagebox.showwarning('입력오류', '입력항목이 부족합니다.')
        return
    if not (middle.isdigit() and last.isdigit() and attend.isdigit()):
        tkinter.messagebox.showwarning('점수오류', '점수는 정수여야 합니다.')
        return
    con = sqlite3.connect("student")
    cur = con.cursor()
    sqlstr = 'insert into std values("' + hakbun + '","' + name + '",' + middle + ',' + last + ',' + attend + ')'
    cur.execute(sqlstr)
    con.commit()
    con.close()

window = Tk()

window.title("성적처리")
window.geometry("500x500")
window.resizable(width=FALSE, height=FALSE)

frmTop = Frame(window, width=500, height=170)
frmMiddle = Frame(window, width=500, height=50)
frmBottom = Frame(window, width=500, height=280)

lbLineBlue1 = Label(window, width=500, height=1, font=('굴림체', 1), bg='blue')
lbLineBlue2 = Label(window, width=500, height=1, font=('굴림체', 1), bg='blue')

frmTop.pack(side=TOP)
lbLineBlue1.pack(side=TOP)
frmMiddle.pack(side=TOP)
lbLineBlue2.pack(side=TOP)
frmBottom.pack(side=TOP)

lbHakbun  =Label(frmTop, text="학  번", font=('굴림체',10), width=8, bg='#EAEAEA')
lbMiddle = Label(frmTop, text = "중  간", font=('굴림체', 10), width = 8, bg = '#EAEAEA')
lbName   = Label(frmTop, text = "성  명", font=('굴림체', 10), width=8, bg = '#EAEAEA')
lbLast   = Label(frmTop, text = "기  말", font=('굴림체', 10), width = 8, bg = '#EAEAEA')
lbAttend = Label(frmTop, text = "출  석", font=('굴림체', 10), width = 8, bg = '#EAEAEA')
lbtotal  = Label(frmTop, text = "총  점", font=('굴림체', 10), width = 8, bg = '#EAEAEA')
lbHakjum = Label(frmTop, text = "학  점", font=('굴림체', 10), width = 8, bg = '#EAEAEA')

enHakbun= Entry(frmTop, font=('굴림체', 10), width = 10)
enName  = Entry(frmTop, font=('굴림체', 10), width = 10)
enMiddle= Entry(frmTop, font=('굴림체', 10), width = 10)
enLast  = Entry(frmTop, font=('굴림체', 10), width = 10)
enAttend= Entry(frmTop, font=('굴림체', 10), width = 10)
lbTotView = Label(frmTop, text = '      ', font=('굴림체', 10), width=8, bg='#CEFBC9')
lbHakView = Label(frmTop, text = '      ', font=('굴림체', 10), width=8, bg='#CEFBC9')

btInput = Button(frmMiddle, text='입  력', font=('굴림체', 12), width=6, height=1, command = fInput)
btModity = Button(frmMiddle, text='수  정', font=('굴림체', 12), width=6, height=1)
btDelete = Button(frmMiddle, text='삭  제', font=('굴림체', 12), width=6, height=1)

ViewList = Listbox(frmBottom, font=('굴림체', 10), selectmode='extended', height=16, width=62)

lbHakbun.place(x=30,y= 50)
enHakbun.place(x=100, y=50)
lbName.place(x=340, y=50)
enName.place(x=410, y=50)
lbMiddle.place(x=30, y=90)
enMiddle.place(x=100, y=90)
lbLast.place(x=180, y=90)
enLast.place(x=250, y=90)
lbAttend.place(x=340, y=90)
enAttend.place(x=410, y=90)
lbtotal.place(x=100, y=130)
lbTotView.place(x=170, y=130)
lbHakjum.place(x=250, y=130)
lbHakView.place(x=320, y=130)
btInput.place(x=100, y=10)
btModity.place(x=220, y=10)
btDelete.place(x=340, y=10)
ViewList.place(x=30, y=20)

enMiddle.bind("<FocusOut>", fJumsuTot)
enLast.bind("<FocusOut>", fJumsuTot)
enAttend.bind("<FocusOut>", fJumsuTot)

fDataLoading()

window.mainloop()
