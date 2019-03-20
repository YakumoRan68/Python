def toint(a) :
    try :
        print(a + " : " + str(int(a)))
    except Exception:
        print(a + " : 형변환 에러")
    return

def tofloat(a) :
    try :
        print(a + " : " + str(float(a)))
    except Exception :
       print(a + " : 형변환 에러")
    return

toint("100a")
tofloat("100.5")
