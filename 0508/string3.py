ss = "Python is Easy. 그래서 programming이 재밌습니다."

st = ""

for v in ss :
	if ord(v) >= ord('a') and ord(v) <= ord('z') :
		st = chr(ord(v)+ 32)
		
print(chr(66))
print(ss.upper(), ss.lower(), ss.swapcase(), ss.title(), sep="\n")