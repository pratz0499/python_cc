class UI():
    def input(self):
        n=int(input("Enter the number of strings to be ananlysed: "))
        for i in range (n):
            l=int(input("Enter the length of the string: "))
            a=str(input("Enter the string: "))

            if len(a)==l:
                print("The entered string is fine")

            else:
                print("The string length and the string entered does not match")
        z=list_of_strings()
        
        return z

    def output(self,inp):
        j=0
        for i in inp.los:
            j=j+1
         

class string:
    def __init__(self,a):
        self.a=a

class list_of_strings:
    def __init__(self):
        self.los=[]
        

    def add_str_to_los(self,a):
        self.los.append(a)
        print(self.los)
    

b=UI()
s=b.input()
