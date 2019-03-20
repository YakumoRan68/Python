num = 1;
array = [];

def getnum():
    array.append(int(input( str(num) + " 번째 숫자를 입력하세요 : ")))
    return

while num <= 2:
    getnum()
    num += 1

print(array)
a = array[0]
b = array[1]

print("두 수의 합 : ", a+b,
      "\n두 수의 차 : ", a-b,
      "\n두 수의 곱 : ", a*b,
      "\na를 b로 나눈 몫 : ", a//b,
      "\na를 b로 나눈 나머지 : ", a%b,
      "\na를 b번 거듭제곱 : ", a**b)

