dic = dict(trifle = "낭비하다", brief = "짧은", cascade = "폭포")

while(True) :
	word = input("단어 입력 : ")
	if word == '0' :
		break
	elif dic.get(word) :
		print("%.10s : %s" % (word, dic[word]))
	else :
		found = False
		for key, value in dic.items() :
			if value == word :
				found = True
				print(".%10s : %s" % (value, key))
		if not found :
			print("찾지 못했습니다.")