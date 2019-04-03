a = ['a','b',['c','b'], 'a', 2, 3]

print(a[1])     #specify

#slicinglist[first(0) index:last(1) index:step(1)]
print(a[0:3])   #by scope
print(type(a[0:2])) 
print(a[:2]) # ~ a[1], :인덱스 미만 범위
print(a[2:])
print(a[2:1:-1])
print(a[2::-1])

print(a.pop(), a)

doubled = a * 2 
print(doubled)

copy = a #배열의 원소가 복제됨
print("copy", copy) 

copy.append("a")
print(copy)

copy.append([1,2])
print(copy)

copy.extend([1,2])
print(copy)

intlist = [5,4,3,2,1]
print([elem*2 for elem in intlist if elem >= 3 >0]) #[<condition>index]

#a.sort() : cannot sort list emelement
print(intlist)
intlist.sort()
print(intlist)

