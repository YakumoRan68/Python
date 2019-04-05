tup = (5,4,3,2,1)
for i in tup :
	print(tup[i -1])

#tup[1] = 5 값을 변경할 수 없음.

x = 5
if x in tup :
	print("%d exists"%x)

try :
	y = tup.index(x)
	print("%d exists at %d"%(x,y))
except Exception :
	print("%d not exists"%x)

print(tup * 2)
print(len(tup))

del tup

