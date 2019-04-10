import re

op = "" #연산자
formula = "33*5" #input("수식을 입력하세요 : ")
result = 0
stack = list()

def ToInt(x) :
    try :
        return int(x)
    except ValueError :
        return None

def TryCalc() :
    return str(op == "+" and (x+y) or op == "-" and (x-y) or op == "*" and (x*y) or op == "+" and (x/y))  

for i in range(len(formula)) :
    x = formula[i]
    if x == " " :
        continue
    #elif ToInt(x) != None :
pattern = re.compile('(\d+|[^ 0-9])') #(숫자 0~9(\d) 가 2개이상인 패턴) 또는 숫자 0~9가 아닌 패턴
print(re.findall(pattern, formula))

#print("답은 " + result + " 입니다.")
