import random
num = []
dic = {}

for i in range(6) :
	num.append(random.randrange(1,46))

dic = set(num)
print(dic)