def test0() :
	global a
	a = 100
	print(a)

def test1() :
	print(a) #전역 범위에있는 a를 출력. test0에서 전역범위의 a를 생성했기 때문에 존재함.

test0()
test1()