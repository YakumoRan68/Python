var = "var"
a = [1, 2, [1, 2], var] #값만 들어감.(참조가 들어가는게 아님)
b = a #오브젝트의 주소가 대입됨
print(id(b), id(a)) #주소가 같음
print("b = ", b) #즉 print([list])는 list 주소가 가리키는 요소의 값들을 형태에 맞춰서 출력하는 함수임을 알 수 있음.
b[2] = [1, 3]
print(a, b, end = "\n\n")

copied = a.copy() # 얕은 복사; 새로운 오브젝트가 생성되지만 그안의 값들은 같은 주소를 참조함
print(id(a), id(copied))
copied.append(1)
var = "changed" #안바뀜. 값만 들어갔었기 때문에
print(a, copied)

deepcopied = copy.deepcopy(a)

input()
