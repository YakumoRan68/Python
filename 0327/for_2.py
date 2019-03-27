for i in range(2,10) :
    print("=== %d단 ===" % i)
    for j in range(10) :
        print("%d * %d = %d"% (i, j, i * j))
    print()

for i in range(2,10) :
    for j in range(2, 10) :
        print("%d * %d = %2d" % (j, i, i*j), end = "   ")
    print()
