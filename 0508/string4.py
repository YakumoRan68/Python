ss = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠."
print(ss.count("공부"), 
	ss.find("공부"), ss.find("공부", 5), #find(v, start, end) start위치부터 end까지 첫번째로 찾은 인덱스
	ss.rfind("공부"), ss.rfind("공부", 5, 1)) #rfind (v, start, end)뒤에부터 find 

print(ss.find("없다"), ss.index("공부")) #ss.index() index는 값이 없다면 오류
print(ss.count(" "))
print(ss.startswith("파"), ss.endswith("."))

ss = "          공백이 많은 문자             "
print(ss.strip(), ss.lstrip(), ss.rstrip(), ss.replace(" ", ""))

stripped = "" #사용자 정의 
for v in ss :
	if v != ' ' :
		stripped = stripped + v
print(stripped)