s = "."
print(s.isdigit(), s.isalpha(), s.isalnum(), s.islower(), s.isupper())

us = s.upper() #한글은 isupper()도 아니고 islower()도 아님. 즉 모든 영어알파벳은 여기서 걸러짐.
if s.isalpha() and not us.isupper() :
	print("한글로만 구성돼있습니다.")