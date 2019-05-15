def test(arg1, arg2, arg3, *args, **kwargs) :
	arglist = [arg1, arg2, arg3] #3번째로 받는 인수들(fargs; formal arguments)까진 arglist에 들어감.
	argslist = [*args] #4번째부터 받는 인수는 받는 순서대로 argslist에 들어감. *args의 자료형은 튜플임. 
	kwargslist = {**kwargs} #딕셔너리 타입으로 들어온 인수들은 kwardslist에 들어감. 단 인수를 받는 순서가 다른 인수들의 순서와 맞아야함.
	return [arglist, argslist, kwargslist]

def n(*args, **kwargs) :
	return [args, {**kwargs}]

print(test(1, None, 2, 3, 4, 5, x = 6, y = 7, z = 8))
# print(n(x = 3, 3)) 순서가 맞지않아서 오류
