import random

arr = []
num = input("발행할 난 수 갯수 : ")
x, y = input("범위 1"), input("범위 2")

if x > y : 
	x, y = y, x

for i in range(num + 1) :
	arr.append(random.randrange(x, y + 1))

arr.sort()

print(arr)
