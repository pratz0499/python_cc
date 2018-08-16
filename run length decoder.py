class UI:
    def input(self):
        n=int(input("Enter the number of sequence: "))
        z=list_of_list_integers()
        for i in range(n):
            q=list_of_integers()
            m=int(input("Enter the length of sequence:"))
            k=input("Enter the integers: ")
            q.add(k)
            
        if len(str(k))==m:
            return z 

        else:
            print("The entered integers and the length of sequence does not match")
    


class list_of_integers:
    def __init__(self):
        self.loi=[]

    def add(self,k):
        self.loi.append(k)

class list_of_list_integers:
    def __init__(self):
        self.list_of_list=[]

    def add_lists(self,DI):
        self.list_of_list.append(DI)
        
    


p=UI()
s=p.input()
