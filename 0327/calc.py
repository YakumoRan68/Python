operand = "" #숫자 문자열
operator = "" #연산자
formula = input("수식을 입력하세요 : ")
x, y = 0, 0

def toint(x) :
    try :
        return int(x)
    except ValueError :
        return None

def calculate(x, y, op) :
    if op == "+" :
        return str(x+y)
    else :
        return str(x-y) #일단 +랑 -만 호환 

for i in range(len(formula)) :
    if toint(formula[i]) != None : #현재 인덱스가 숫자면
        operand = operand + formula[i]
    else :
        if x != 0 and y != 0 :
            print("calc!")
            x, y = calculate(x, y, operator), 0
            operator = formula[i]
            
        if x == 0 : #첫번째 피연산자 입력
            print("x in")
            x = toint(operand)
            operand = ""
            operator = formula[i]
        elif y == 0 : #두번째 피연산자 입력
            print("y in")
            y = toint(operand)
            operand = ""
            operator = formula[i]
            

y = toint(operand)

print(x, y, operator)
result = calculate(x, y, operator)

print("답은 "+result+" 입니다.")
