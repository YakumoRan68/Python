from tkinter import *
import sqlite3
import tkinter.messagebox
import tkinter.ttk
import math

def FCreateDataBase() :
    con = sqlite3.connect('.\\sawon')
    cur = con.cursor()
    cur.execute('create table sawon(sabun char(5) primary key, name char(10), part char(10))')
    cur.execute('create table siljuk(seq int primary key, yymmdd char(10), sabun char(5), sil int, bun int)')

    con.commit()
    con.close()
    

def FAutoDataInsert() :
    con = sqlite3.connect('.\\sawon')
    cur = con.cursor()
    cur.execute('delete from sawon')
    cur.execute('delete from siljuk')

    cur.execute('insert into sawon values("A0001", "홍길동", "영업1부")')
    cur.execute('insert into sawon values("A0002", "김말동", "영업1부")')
    cur.execute('insert into sawon values("A0003", "이기자", "영업2부")')
    cur.execute('insert into sawon values("A0004", "나잘해", "영업2부")')
    cur.execute('insert into sawon values("A0005", "최고야", "영업3부")')
    cur.execute('insert into sawon values("A0006", "에이쁠", "영업3부")')
    cur.execute('insert into sawon values("A0007", "나야나", "영업3부")')

    cur.execute('insert into siljuk values(1, "20190201", "A0001", 100000, 1)')
    cur.execute('insert into siljuk values(2, "20190215", "A0002", 30000,  1)')
    cur.execute('insert into siljuk values(3, "20190401", "A0002", 50000,  2)')
    cur.execute('insert into siljuk values(4, "20190401", "A0001", 70000,  2)')
    cur.execute('insert into siljuk values(5, "20190415", "A0002", 150000, 2)')
    cur.execute('insert into siljuk values(6, "20190505", "A0003", 70000,  2)')
    cur.execute('insert into siljuk values(7, "20190620", "A0005", 45000,  2)')
    cur.execute('insert into siljuk values(8, "20190717", "A0002", 250000, 3)')
    cur.execute('insert into siljuk values(9, "20190808", "A0002", 175000, 3)')
    cur.execute('insert into siljuk values(10,"20190825", "A0001", 50000,  3)')
    cur.execute('insert into siljuk values(11,"20190919", "A0001", 75000,  3)')
    cur.execute('insert into siljuk values(12,"20191101", "A0002", 150000, 4)')
    
    con.commit()
    con.close()

    initDBLoading()
  
def initDBLoading() :
    con = sqlite3.connect(".\\sawon")
    cur = con.cursor()
    cur.execute("select * from sawon")

    Saviewinx = 0
    lstSawon.delete(0,lstSawon.size())
    
    inx = 0
    while(True) :
        row = cur.fetchone()
        if row == None :
            break

        datastr = ("  {0:10s}.{1:15s}.{2:15s}".format(row[0],row[1],row[2]))
        lstSawon.insert(inx, datastr)
        if enSabun.get() == row[0] :
            Saviewinx = inx
        inx += 1

    cur.execute("select se.seq, se.yymmdd, se.bun, se.sabun, sa.name, se.sil from siljuk se, sawon sa where sa.sabun = se.sabun")
    
    Seviewinx = 0
    lstSale.delete(0,lstSale.size())
    
    inx = 0
    while(True) :
        row = cur.fetchone()
        if row == None :
            break

        datastr = ("{0:3d}.  {1:8s}.{2:3d}.  {3:5s}.  {4:5s}.{5:7d}".format(row[0],row[1],row[2], row[3], row[4], row[5]))
        lstSale.insert(inx, datastr)
        if enSeSeq['text'] == row[0] :
            Seviewinx = inx
        inx += 1



    con.close()

    lstSawon.see(Saviewinx)
    lstSale.see(Seviewinx)


window = Tk()
window.title="영업사원실적관리"
window.geometry("500x700")


#영업사원 관리
SawonMgFrame = Frame(window, width=500, height=150)
SawonMgFrame.place(x=0, y=0)
Sawon_Title = Label(SawonMgFrame, width=71, text='[영업사원관리]', font=('굴림체', 10), fg='black', bg='#CEFBC9', relief='ridge')
Sawon_Title.place(x=0, y=0)
lbSabun    = Label(SawonMgFrame,   width=10, font=('굴림체', 10), text = '사 번')
enSabun    = Entry(SawonMgFrame,   width=10, font=('굴림체', 10))
lbSaName   = Label(SawonMgFrame,   width=10, font=('굴림체', 10), text = '성 명')
enSaName   = Entry(SawonMgFrame,   width=10, font=('굴림체', 10))
lbSaPart   = Label(SawonMgFrame,   width=10, font=('굴림체', 10), text = '부 서')
enSaPart   = Entry(SawonMgFrame,   width=10, font=('굴림체', 10))
Sascrollbar  = tkinter.Scrollbar(SawonMgFrame)
lstSawon   = Listbox(SawonMgFrame, width=47, font=('굴림체', 10), selectmode='extended', height=5, yscrollcommand =Sascrollbar.set)
def ClearSa() :
    enSabun.delete(0, 'end')
    enSaName.delete(0, 'end')
    enSaPart.delete(0, 'end')

def OnClickSawon(event) :
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    data = value.split()

    ClearSa()
    enSabun.insert(0, data[0])
    enSaName.insert(0, data[1].replace(".", ""))
    enSaPart.insert(0, data[2].replace(".", ""))

def InsertSaData() :
    Input = [enSabun.get(), enSaName.get(), enSaPart.get()]
    if Input[0] == "" or Input[1] == "" or Input[2] == "" :
        tkinter.messagebox.showwarning("오류", "입력 칸이 비어있으면 안됩니다.")
        return

    con = sqlite3.connect(".\\sawon")
    cur = con.cursor()

    cur.execute("select * from sawon where sabun = '" + Input[0] + "'")
    if cur.fetchone() != None :
        cur.execute("update sawon set name = '" + Input[1] + "', part = '" + Input[2] + "' where sabun = '" + Input[0] + "'")
    else :
        cur.execute("insert into sawon values('" + Input[0] + "','" + Input[1] + "','" + Input[2] + "')")

    con.commit()
    con.close()

    initDBLoading()

def DeleteSaData() :
    Input = [enSabun.get()]
    if Input[0] == "" :
        tkinter.messagebox.showwarning("오류", "사번 칸이 비어있으면 안됩니다.")
        return

    con = sqlite3.connect(".\\sawon")
    cur = con.cursor()
    cur.execute("delete from sawon where sabun = '" + Input[0] + "'")

    con.commit()
    con.close()

    initDBLoading()

lstSawon.bind("<Double-Button-1>", OnClickSawon)
btSaNew    = Button(SawonMgFrame,  width=10, font=('굴림체', 10), text = '신규', command = ClearSa)
btSaInput  = Button(SawonMgFrame,  width=10, font=('굴림체', 10), text = '입력/수정', command = InsertSaData)
btSaDelete = Button(SawonMgFrame,  width=10, font=('굴림체', 10), text = '삭제', command = DeleteSaData)
btSaFind   = Button(SawonMgFrame,  width=10, font=('굴림체', 10), text = '    ')

lbSabun.place(x=30, y=30)
enSabun.place(x=30, y=50)
lbSaName.place(x=170, y=30)
enSaName.place(x=170, y=50)
lbSaPart.place(x=310, y=30)
enSaPart.place(x=310, y=50)

lstSawon.place(x=30, y=70)

btSaNew.place(x=400, y=30)
btSaInput.place(x=400, y=60)
btSaDelete.place(x=400, y=90)
btSaFind.place(x=400, y=120)

Sascrollbar.place(x=360, y=70,width=20, height=75)
Sascrollbar["command"]=lstSawon.yview



#영업실적 관리
SaleMgFrame = Frame(window, width=500, height=150)
SaleMgFrame.place(x=0, y=151)
Sale_Title = Label(SaleMgFrame, width=71, text='[영업실적관리]', font=('굴림체', 10), fg='black', bg='#CEFBC9', relief='ridge')
Sale_Title.place(x=0, y=0)

def OnYearChanged(*args) :
    print(enSeymd.get())

Year = StringVar()

def GetBun():
    month = int(Year.get()[4:6])
    enSebun.configure(text = str(math.ceil(month / 3)))
    return True

Sabun = StringVar()

def GetName() :
    Input = enSeSabun.get()
    con = sqlite3.connect(".\\sawon")
    cur = con.cursor()

    cur.execute("select name from sawon where sabun = '" + Input + "'")
    if cur.fetchone() != None :
        for v in cur.fetchone() :
            lbSeName1.configure(text = v)
    else :
        cur.execute("select sabun from sawon where name = '" + Input + "'")
        now = cur.fetchone()
        if now == None :
            return

        for v in cur.fetchone() :
            enSeSabun.configure(text = v)





lbSeSeq   = Label(SaleMgFrame, width= 3, font=('굴림체', 10), text = ' Key ')
enSeSeq   = Label(SaleMgFrame, width= 3, font=('굴림체', 10), bg='#FFD9FA')
lbSeymd   = Label(SaleMgFrame, width= 8, font=('굴림체', 10), text = '년월일')
enSeymd   = Entry(SaleMgFrame, width= 8, font=('굴림체', 10), textvariable = Year, validate="focusout", validatecommand=GetBun)
lbSebun   = Label(SaleMgFrame, width= 3, font=('굴림체', 10), text = '분기')
enSebun   = Label(SaleMgFrame, width= 3, font=('굴림체', 10), bg='#FFD9FA')
lbSeSabun = Label(SaleMgFrame, width= 7, font=('굴림체', 10), text = '사번')
enSeSabun = Entry(SaleMgFrame, width= 7, font=('굴림체', 10), textvariable = Sabun, validate="focusout", validatecommand=GetName)
lbSeName0 = Label(SaleMgFrame, width= 7, font=('굴림체', 10), text = '성명')
lbSeName1 = Label(SaleMgFrame, width= 7, font=('굴림체', 10), bg='#FFD9FA')
lbSeMoney = Label(SaleMgFrame, width=10, font=('굴림체', 10), text = '금액')
enSeMoney = Entry(SaleMgFrame, width=10, font=('굴림체', 10)) 

Sescrollbar  = tkinter.Scrollbar(SaleMgFrame)
lstSale    = Listbox(SaleMgFrame, width=47, font=('굴림체', 10), selectmode='extended', height=5, yscrollcommand =Sescrollbar.set)

def OnNewbt() :
    con = sqlite3.connect(".\\sawon")
    cur = con.cursor()
    cur.execute("select * from siljuk")

    index = 1
    for v in cur.fetchall() :
        index += 1

    enSeSeq.configure(text = str(index))

    con.close()

def ModifyNewbt() :
    Input = [enSeSeq.get(), enSeymd.get(), enSeSabun.get(), enSeMoney.get(), enSebun.get()]
    if Input[0] == "" or Input[1] == "" or Input[2] == "" or Input[3] == "" or Input[4] == "" :
        tkinter.messagebox.showwarning("오류", "입력 칸이 비어있으면 안됩니다.")
        return

    con = sqlite3.connect(".\\sawon")
    cur = con.cursor()

    cur.execute("select * from siljuk where seq = '" + Input[0] + "'")
    if cur.fetchone() != None :
        cur.execute("update siljuk set yymmdd = '" + Input[1] + "', sabun = '" + Input[2] + "', sil = " + Input[3] + ", bun = " + Input[4] + " where sabun = '" + Input[0] + "'")
    else :
        cur.execute("insert into siljuk values('" + Input[0] + "','" + Input[1] + "','" + Input[2] + "','" + Input[3] + "','" + Input[4] + "')")

    con.commit()
    con.close()

    initDBLoading()

btSeNew    = Button(SaleMgFrame,  width=10, font=('굴림체', 10), text = '신규', command = OnNewbt)
btSeInput  = Button(SaleMgFrame,  width=10, font=('굴림체', 10), text = '입력/수정', command = ModifyNewbt)
btSeDelete = Button(SaleMgFrame,  width=10, font=('굴림체', 10), text = '삭제')
btSeFind   = Button(SaleMgFrame,  width=10, font=('굴림체', 10), text = '    ')


lbSeSeq.place(x=30, y=30)
enSeSeq.place(x=30, y=50)
lbSeymd.place(x=70, y=30)
enSeymd.place(x=70, y=50)
lbSebun.place(x=135, y=30)
enSebun.place(x=135, y=50)
lbSeSabun.place(x=180, y=30)
enSeSabun.place(x=180, y=50)
lbSeName0.place(x=240, y=30)
lbSeName1.place(x=240, y=50)
lbSeMoney.place(x=310, y=30)
enSeMoney.place(x=310, y=50)

lstSale.place(x=30, y=70)
btSeNew.place(x=400, y=30)
btSeInput.place(x=400, y=60)
btSeDelete.place(x=400, y=90)
btSeFind.place(x=400, y=120)
Sescrollbar.place(x=360, y=70,width=20, height=75)
Sescrollbar["command"]=lstSale.yview


# 영업실적 조회
SearchFrame = Frame(window, width=500, height=360)
SearchFrame.place(x=0, y=301)
Search_Title = Label(SearchFrame, width=71, text='[영업실적조회]', font=('굴림체', 10), fg='black', bg='#CEFBC9', relief='ridge')
Search_Title.place(x=0, y=0)

lbFindName  = Label(SearchFrame, width= 8, font=('굴림체', 10), text = ' 성명 ')
enFindName  = Entry(SearchFrame, width= 8, font=('굴림체', 10))
lbFindSabun = Label(SearchFrame, width= 8, font=('굴림체', 10), text = ' 사번 ')
enFindSabun = Label(SearchFrame, width= 8, font=('굴림체', 10), bg='#FFD9FA')
lbFindPart  = Label(SearchFrame, width= 8, font=('굴림체', 10), text = ' 부서 ')
enFindPart  = Label(SearchFrame, width= 8, font=('굴림체', 10), bg='#FFD9FA')

btFind      = Button(SearchFrame,  width=10, font=('굴림체', 10), text = '검색')

lbListTitle = Label(SearchFrame, width= 40, font=('굴림체', 10), bg='#D9E5FF', text = '년/월/일            금  액')
lstFind     = Listbox(SearchFrame, width=40, font=('굴림체', 10), selectmode='extended', height=19)

lbFindName.place(x=30, y=30)
enFindName.place(x=80, y=30)
lbFindSabun.place(x=150, y=30)
enFindSabun.place(x=200, y=30)
lbFindPart.place(x=270, y=30)
enFindPart.place(x=320, y=30)
btFind.place(x=400, y=30)

lbListTitle.place(x=100, y= 60)
lstFind.place(x=100, y=80)

#DB 생성 및 데이터 자동생성
CreateDBFrame = Frame(window, width=500, height=20, bg='#B2EBF4')
CreateDBFrame.place(x=0, y=661)
CreateDBBt = Button(CreateDBFrame,       text = '   Create DataBase   ', bg='#B2CCFF', font=('굴림체', 10), command = FCreateDataBase)
CreateDBBt.place(x=80, y=0)
AutoDataCreateBt = Button(CreateDBFrame, text = '   Auto Data Insert  ', bg='#B2CCFF', font=('굴림체', 10), command = FAutoDataInsert)
AutoDataCreateBt.place(x=250, y=0)



# 상태바
StateFrame = Frame(window, width=500, height=20, bg = '#F6F6F6')
StateFrame.place(x=0, y=681)
StateMessage = Label(StateFrame, width=70, text= 'message', font=('굴림체', 10), bg='#F6F6F6', relief='ridge')
StateMessage.place(x=1, y=0)

# DB에서 초기값 가져오기
initDBLoading()  
              

window.mainloop()
