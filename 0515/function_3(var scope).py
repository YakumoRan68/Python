b = 10

def test0() :
	global a
	a = 100
	print(a)

def test1() :
	try :
		print("b = " + b) #인터프리터는 b를 현재 지역변수 b로 생각하고 선언되지 않았다고 생각함.
	except Exception :
		print("전역변수 b는 존재하지 않음.")

	print(a) #전역 범위에있는 a를 출력. test0에서 전역범위의 a를 생성했기 때문에 존재함.

#b = 10

test0()
test1()