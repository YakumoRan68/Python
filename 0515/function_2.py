def add(a, b) :
	return a + b

def sub(a, b) :
	return a - b

def mul(a, b) :
	return a * b

def div(a, b) :
	return a / b 

def calc(x, y, iterator) :
	try :
		return globals()[iterator](x, y)
	except Exception:
		print("잘못된 입력입니다.")
		return

print(calc(10, 20, 'add'))
