#2) создать класс точка(поля x, y координаты, методы вернуть в какой четверти лежит, вернуть координату x, y, и в виде
#"(x, y)")(3б)
class point:
    def __init__(self, x , y):
        self.v = x
        self.w = y

    def s1(self):
        return 1 , 'частина'

    def s2(self):
        return 2 , 'частина'

    def s3(self):
        return 3 , 'частина'

    def s4(self):
        return 4 , 'частина'

    def s5(self):
        return 'кордината 0' 

x = int(input(':'))
y = int(input(':'))        
c1 = point(x,y)        
if x > 0 and y > 0:
    print(c1.s1())
if x < 0 and y > 0:
    print(c1.s2())
if x < 0 and y < 0:
    print(c1.s3())
if x > 0 and y < 0:
    print(c1.s4())
if x == 0 and y == 0:
    print(c1.s5())