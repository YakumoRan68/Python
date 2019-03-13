a = int(input(("변환할 숫자 : ")))

print("%d" % a,
      "\n%x" % a,
      "\n%o" % a,
      "\n%u" % a,
      "\n%d %d" % (a, 600), #format의 argument갯수를 맞춰야함.
      "\n%d" % 1.5,
      "\n%.2s" % "두글자",
      "\n%7.3f" % 12345.12,)
