class UI:
    def input(self):
        n=int(input("Enter the number of instances: "))
        z=list_of_distinct_integers()
        for i in range (n):
            m=int(input("Enter the number of elements instance %d: " %(i+1)))
            a=distinct_integers()
            for i in range (m):
                k=int(input("Enter the element: "))
                b=distinct_int(k)
                a.add_k_to_ks(b)

            z.add_DI_to_lodi(a)
        return z

    def output(self,inp):
        j=0
        for i in inp.loc:
            j=j+1
            print("The entered numbers for instance %d is " %(j))
            print("%d" %(i.loks))
        

class distinct_int:
    def __init__(self,k):
        self.k=k

class distinct_integers:
    def __init__(self):
        self.loks=[]

    def add_k_to_ks(self,k):
        self.loks.append(k)

class list_of_distinct_integers:
    def __init__(self):
        self.loc=[]

    def add_DI_to_lodi(self,DI):
        self.loc.append(DI)

                         
    

        
              
p=UI()
s=p.input()
p.output(s)
