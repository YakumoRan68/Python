a = ['a','b',['c','b'], 'a', 2, 3]

print(a[1])     #specify

#slicinglist[first(0) index:last(1) index:step(1)]
print(a[0:3])   #by scope
print(type(a[0:2])) 
print(a[:2]) # ~ a[1], :인덱스 미만 범위
print(a[2:])
print(a[2:1:-1])
print(a[2::-1])


print("\n")
a = [1,2,3,4,5]

print(a.pop(), a)

doubled = a * 2 
print(doubled)
print(id(a), id(doubled)) #새로운 주소를 할당해서 복사한다는 것을 알 수 있음

a.append("a")
print(a)

a.append([1,2])
print("appeded", a)

a.extend([1,2])
print("extended", a)

a.reverse()
print("reversed ", a)

a.insert(3, "x") #n번째가 아니고 인덱스 번호임
print("inserted", a)

print("1's count is " + str(a.count(1)))

print("found", a.index([1,2])) #찾는 메소드

print("length of a = ", len(a))

a.clear()
print(a)
del(a)

intlist = [5,4,3,2,1]
print([elem*2 for elem in intlist if elem >= 3 >0]) #[<condition>index]

#a.sort() : cannot sort list emelement
print(intlist)
intlist.sort()
print(intlist)
