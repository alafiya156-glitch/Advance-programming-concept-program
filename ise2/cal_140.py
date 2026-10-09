class calculator:
   
    def add(self):

        c1=a+b
        print("addition is:",c1)

    def sub(self):
        s=a-b
        print("substraction is:",s)
    def mul(self):
        m=a*b
        print("multiplication is:",m)
    def division(self):
        d=a/b
        print("divison is:",d)
    def floor(self):
        f=a//b
        print("floor division :",f)
    def expo(self):
        e=a**b
c=calculator()
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c.add()
c.sub()
c.mul()
c.division()
c.division()
c.floor()
c.expo()
        
