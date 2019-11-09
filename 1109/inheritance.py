class People :
    def __init__(self) :
        self.x = 1
    
    def P(self, x) :
        self.__P(x)

    def _P(self, x) :
        print(x)

    def __P(self, x) :
        print(x)

    def _sleep(self) :
        self.P("자다")

class Student(People) :
    def study(self) :
        self.P("공부하다")

P1 = People()
P1.P("말하다")
P1._sleep()

P2 = Student()
P2.P("말하다")
P2._P("ㅁ")
P2.study()