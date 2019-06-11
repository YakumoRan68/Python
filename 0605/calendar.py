import calendar
import datetime
from tkinter import *
import tkinter.ttk

def GetTime() :
    return datetime.datetime.now()

calendar.setfirstweekday(calendar.SUNDAY) #달력 첫요일을 일요일로 설정
Today = calendar.monthcalendar(GetTime().year, GetTime().month)
DayofWeek = ("일", "월", "화", "수", "목", "금", "토")
Colors = dict(black = "#000000", white = "#FFFFFF", red = "#FF0000", blue = "#0000FF", highlighted = "#F3F781")

root = Tk()

root.title("달력")
root.geometry("800x600")
root.resizable(False, False)

MonthSetFrame = Frame(root, width = 540, height = 60, bd = 1, relief = SOLID, pady = 15)
MonthSetFrame.grid_propagate(False) #Frame안에 다른 위젯이 존재할경우 너비와 높이 설정을 무시하고 그 위젯의 크기에 프레임 크기를 맞추는데, 그것을 grid에 대해 비활성화
MonthSetFrame.place(x = 0, y = 0)
MonthSetFrame.pack(anchor = "nw")

CurrentYear = StringVar()
CurrentYear.set(GetTime().year)

def OnDateChanged(event) :
    CurrentMonth = calendar.monthcalendar(int(YearBox.get()), int(MonthBox.get()))
    CurrentMonth.append([0, 0, 0, 0, 0, 0, 0]) #인덱스 범위 초과문제 해결

    for i in range(6) :
        for j in range(7) :
            Day = CurrentMonth[i][j]
            Days[i + 1][j].DayLabel.configure(text = Day if Day > 0 else "")

YearBox = Spinbox(MonthSetFrame, width = 8, validate = 'key', textvariable = CurrentYear, to = 2100, wrap = True)
YearBox.grid(row = 0, column = 0, padx = (170, 0)) #grid의 패딩 설정은 2개의 튜플 값을 입력할 수도 있음. padx의 경우 (좌,우), pady의 경우(상,하)  

YearLabel = Label(MonthSetFrame, text = "년")
YearLabel.grid(row = 0, column = 1)

MonthBox = tkinter.ttk.Combobox(MonthSetFrame, width = 4, height = 12, values = [i+1 for i in range(12)])
MonthBox.current(GetTime().month - 1)
MonthBox.bind("<<ComboboxSelected>>", OnDateChanged) #값 선택했을때마다 콜백함수 실행
MonthBox.grid(row = 0, column = 2, padx = (20, 0))

MonthLabel = Label(MonthSetFrame, text = "월")
MonthLabel.grid(row = 0, column = 3)

CalendarFrame = Frame(root, width = 540, height = 540, padx = 20, bd = 1, relief = SOLID)
CalendarFrame.grid_propagate(False)
CalendarFrame.place(x = 0, y = 50)
CalendarFrame.pack(anchor = "sw")

Days = list()
Selected = (-1, 0)

def OnSelectDayCell(event) :
    info = event.widget.grid_info()
    global Selected
    if Selected[0] != -1 : #초기값이 아니면
        Before = Days[Selected[0]][Selected[1]]
        Before.configure(bd = 1, bg = Colors["white"])
        Before.DayLabel.configure(bg = Colors["white"])
        Before.DutyLabel.configure(bg = Colors["white"])

    event.widget.configure(bd = 2, bg = Colors["highlighted"])
    event.widget.DayLabel.configure(bg = Colors["highlighted"])
    event.widget.DutyLabel.configure(bg = Colors["highlighted"])
    Selected = (info["row"], info["column"])

for i in range(7) :
    Week = list()
    for j in range(7) :
        DayText = ""
        DayColor = Colors["black"]
        BgColor = Colors["white"]

        if i == 0 :
            DayText = DayofWeek[j]
            BgColor = "SystemButtonFace"
        else :
            Day = Today[i-1][j]
            DayText = Day if Day > 0 else ""
       
        if j == 0 :
            DayColor = Colors["red"]
        elif j == 6 :
            DayColor = Colors["blue"]

        Cell = Frame(CalendarFrame, width = 70, height = 70, bg = BgColor, bd = 1, relief = FLAT if i == 0 else GROOVE)
        Cell.grid_propagate(False)
        if i != 0 :
            Cell.bind("<Button-1>", OnSelectDayCell) #왼쪽 클릭 이벤트 바인딩
        Cell.grid(row = i, column = j)

        DayLabel = Label(Cell, text = DayText, bg = BgColor, fg = DayColor)
        DayLabel.grid(row = 0, column = 0, padx = 25, pady = (25 if i == 0 else 3, 0))

        DutyLabel = Label(Cell, text = "", bg = BgColor, fg = Colors["black"])
        DutyLabel.grid(row = 1, column = 0, padx = 25, pady = (10, 0))

        Cell.DayLabel = DayLabel #위젯끼리는 전부 상속 관계가 없이 동등한 관계이므로 참조를 남김.
        Cell.DutyLabel = DutyLabel

        Week.append(Cell)
        
    Days.append(Week)



root.mainloop()