class UI:
    def input(self):  
        n=int(input("Enter number of points: "))
        z=points()
        for i in range(n):        
            print("Enter details of point %d" %(i+1))
            x=int(input("Enter x cordinate of point: "))
            y=int(input("Enter y coodinate of point: "))
            g=point(x,y)
            z.add_point_to_points(g)
        return(z)

    def output(self,inp):
        j=0
        for i in inp.f_points:
            j=j+1
            print("X and Y co ordinate of point %d is (%d,%d)" %(j,i.a,i.b))
class point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class points:
    def __init__(self):
        self.f_points=[]
    def add_point_to_points(self,p):
        self.f_points.append(p)

a=UI()
b=a.input()
a.output(b)
