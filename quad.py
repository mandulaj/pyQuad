
import math

class QuadFunction(object):
    
    def __init__(self,function):
        self.parseFunction(function)

    def parseFunction(self,function):
        args = []
        for i in function:
            pass

    def expand(self):
        pass

    def factor(self):
        pass

    def __str__(self):
        return self.printF()

    def printF(self):
        pass

    def solve(self):
        self.expand()

    def quad(self,a,b,c):
        root = b**2-4*a*c

        if root < 0:
            root = abs(complex(root))
            j = complex(0,1)

            x1 = (-b+j+math.sqrt(root))/(2*a)
            x2 = (-b-j+math.sqrt(root))/(2*a)
        else:
            x1 = (-b+math.sqrt(root))/(2*a)
            x2 = (-b-math.sqrt(root))/(2*a)

        return x1,x2

if __name__ == "__main__":
    q = QuadFunction("2x^2+2x+")
    print q.quad(1,2,3)
