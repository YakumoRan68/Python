money = int(input("돈을 입력하세요 : "))

print("\n")
print("=" * 15)
print("%7s" % "5000 : " + str(money//5000))
money %= 5000
print("%7s" % "1000 : " + str(money//1000))
money %= 1000
print("%7s" % "500 : " + str(money//500))
money %= 500
print("%7s" % "100 : " + str(money//100))
money %= 100
print("%7s" % "50 : " + str(money//50))
money %= 50
print("%7s" % "10 : " + str(money//10))
money %= 10
print("%7s" % "1 : " + str(money))
print("=" * 15)
