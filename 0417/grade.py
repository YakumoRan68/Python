import random

Record = []
GradeNum = 1

def GenScore() :
	return random.randrange(50, 101)

print("입력을 그만 두려면 -1 입력")
while(True) :
	name = input("이름 : ")
	if name == '-1' : 
		break
	elif name == '' :
		continue

	line = [GradeNum, name, GenScore(), GenScore(), GenScore()]

	total = line[2] + line[3] + line[4]
	line.extend([total, total / 3])

	GradeNum += 1
	Record.append(line)

print("*" * 28 + " 성적표 " + "*" *28 + "\n\n" +  
	"%3s\t" * 8 % ("학번", "이름", "국어", "영어", "수학", "총점", "평균", "순위") + "\n")

total = sorted([row[5] for row in Record])
[[row.append(total[n]) for total in total]

print(Record)

input()
