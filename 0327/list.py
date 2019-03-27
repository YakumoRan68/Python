a = ['a','b',['c','b'], 'a', 2, 3]

print(a[1])     #specify

#slicinglist[first(0) index:last(1) index:step(1)]
print(a[0:3])   #by scope
print(type(a[0:2])) 
print(a[:2]) # ~ a[1], :인덱스 미만 범위
print(a[2:])
print(a[2:1:-1])
print(a[2::-1])

doubled = a * 2 
print(doubled)

intlist = [1,2,3,4,5]
print([elem*2 for elem in intlist if elem >= 3 >0]) #[<condition>index]

print(a.pop(), a)

#a.sort() : cannot sort list emelement
print(a)

