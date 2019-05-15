string = "12:34:56&78"
obj = list()

tmp = ""
for c in string :
	if c == ":" or c == "&" :
		obj.append(tmp)
		tmp = ""
	else :
		tmp = tmp + c

if tmp != "" :
	obj.append(tmp)

print(obj)
print((string.replace("&", ":")).split(":"))