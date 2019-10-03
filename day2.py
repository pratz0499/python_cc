class UI:
    def input(self):
        mealcost=float(input("Enter the cost of meal:"))
        tip=int(input("Enter the tip percent:"))
        tax=int(input("Enter the tax percent:"))
        return mealcost,tip,tax;
    

    def ret():
        return input()

class total_cost:
    def __init__(self,a,b):
        z=UI()
        z.ret()
        self.a=((tip/100)*mealcost)
        self.b=((tax/100)*mealcost)
        return a,b;

    def output(self,c):
        self.c=a+b
        print("The total cost of the meal is %d",c)


       

        
        
n=UI()
s=n.ret()
n.output(c)
