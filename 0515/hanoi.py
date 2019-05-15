def hanoi(n, a, b, c) :
	global count
	if n == 1 :
		print("\n%c에서 %d의 원반으로 원반을 %c로 이동" % (a,n,c))
	else:
		hanoi(n-1, a,b,c)
		print("\n%c에서 %d의 원반으로 원반을 %c로 이동" % (a,n,c))
		count += 1
		hanoi(n-1, b,a,c)

cnt = int(input("원반 갯수 입력 : "))
count = 0
hanoi(cnt, 'a','b', 'c')
print("원반의 이동 횟수 : %d", count)