cnt = 0

for i in range(2, 100) :
	IsPrime = True
	for j in range(2, i) : 
		if i % j == 0  :
			IsPrime = False
			break
	if IsPrime :
		print("%2d"%i, end = " ")
		cnt += 1
		if cnt % 5 == 0 :
			print()
print()

cnt = 0
for i in range(2, 100) :
	x = list(filter(lambda j: i % j == 0, range(2, i + 1)))
	if len(x) == 1 :
		print("%2d" % x[0], end = " ")
		cnt += 1
		if cnt % 5 == 0 : 
			print()