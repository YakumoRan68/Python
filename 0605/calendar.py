import calendar
import datetime
from tkinter import *
import tkinter.ttk

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.monthcalendar(2020, 8))

def GetTime() :
    return datetime.datetime.now()

root = Tk()

root.title("달력")
root.geometry("800x600")
root.resizable(False, False)

MonthSetFrame = Frame(root, width = 540, height = 60, bd = 1, relief = SOLID, pady = 15)
MonthSetFrame.grid_propagate(False) #Frame안에 다른 위젯이 존재할경우 너비와 높이 설정을 무시하고 그 위젯의 크기에 프레임 크기를 맞추는데, 그것을 grid에 대해 비활성화
MonthSetFrame.place(x = 0, y = 0)
MonthSetFrame.pack(anchor = "nw")

YearBox = Spinbox(MonthSetFrame, width = 8, validate = 'key', to = 2100, wrap = True )
YearBox.grid(row = 0, column = 0, padx = (170, 0)) #패딩 설정은 2개의 튜플 값을 입력할 수도 있음. padx의 경우 (좌,우), pady의 경우(상,하)  

YearLabel = Label(MonthSetFrame, text = "년")
YearLabel.grid(row = 0, column = 1)

def IsValidMonth(self) :
    text = self.get()
    return text.isdigit() and text >= 1 and text >= 12

def value_error(self):
    label.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")

MonthBoxCallBack = StringVar()

MonthBox = tkinter.ttk.Combobox(MonthSetFrame, width = 4, height = 12, values = [i+1 for i in range(12)], textvariable = MonthBoxCallBack, validate = "key", validatecommand = IsValidMonth)
MonthBox.current(GetTime().month - 1)
MonthBox.grid(row = 0, column = 2, padx = (20, 0))

MonthLabel = Label(MonthSetFrame, text = "월")
MonthLabel.grid(row = 0, column = 3)

CalendarFrame = Frame(root, width = 540, height = 540, padx = 20, pady = 20, bd = 1, relief = SOLID)
CalendarFrame.grid_propagate(False)
CalendarFrame.place(x = 0, y = 50)
CalendarFrame.pack(anchor = "sw")

Days = list()

def OnClickDayCell(Event) :
    print(Event.widget)

for i in range(7) :
    Week = list()
    for j in range(7) :
        Obj = Frame(CalendarFrame, width = 70, height = 70, bg = "#FFFFFF", bd = 1, relief = GROOVE)
        Obj.bind("<Button-1>", OnClickDayCell) #왼쪽 클릭 이벤트 바인딩
        Obj.grid(row = i, column = j)
        Week.append(Obj)
    Days.append(Week)

root.mainloop()