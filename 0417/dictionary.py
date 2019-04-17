import operator 

dic = dict(k = "v", x="5")
#print(dic['a'])    #해당 키에 값이 없으면 오류. 
print(dic.get('a')) #해당 키에 값이 없으면 None을 출력.

print(dic.items()) #튜플 형태로 출력
for v in dic :
	print(v)

print(sorted(dic.items(), key=operator.itemgetter(1))) #0은 key:val