dic = dict(k = "v", x="5")
#dic = {'k':'v', 2:1, 1:2, 3:{1,2,3}}

print(dic)

dic[5] = 5
dic['key'] = 'value'
print(dic)

#del(dic[2])
print(dic)
print(dic['key'])
print("length =", len(dic)) #값이있는 갯수

print(dic.keys(), "\n",dic.values(), "\n",dic.items())
a = dic.values()

Key = 3
if dic.get(Key) : #없으면 None 호출
	print("dic[%s] = " % Key, dic[Key])
else:
	print("dic[%s] doesn't exist" % Key)