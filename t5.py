class fraction:
    def __init__(self,int,int2,int3,int4):

        self.num = int
        self.den = int2
        self.num2 = int3
        self.den2 = int4

    def add (self):
        a = (self.num*self.den2)+(self.den*self.num2)
        b=  self.den*self.den2
        c = a / b
        print ("add:",c)
#sub
    def sub (self):
        a = (self.num*self.den2)-(self.den*self.num2)
        b=  self.den*self.den2
        c = a / b
        print ("sub:",c)

#mul
    def mul (self):
        a = self.num*self.num2
        b=  self.den*self.den2
        c = a / b
        print ("mul:",c)
#div
    def div (self):
        a = self.num*self.den2
        b=  self.den*self.num2
        c = a / b
        print ("div:",c)

    def show (self):
        classrunner.add()
        classrunner.sub()
        classrunner.mul()
        classrunner.div()

classrunner = fraction (8,4,5,3)
classrunner.show()