class UI:
    def input(self):
        n=int(input("Enter the number of sequences:"))
        z=list_of_lists()

        for i in range(n):
            m=int(input("Enter the size of the sequence:"))
            a=list_of_integers()
            for j in range(m):
                k=int(input("Enter the element:"))
                a.loi.append(k)
            z.list_1.append(a.loi)
        return z





class list_of_integers:
    def __init__ (self):
        self.loi=[]

    def add(self,k):
        self.loi.append(k)

class list_of_lists:
    def __init__(self):
        self.list_1=[]

    def add(self,loi):
        self.list_1.append(loi)



x=UI()
s=x.input()

for i in range(len(s.list_1)):
    seq = s.list_1[i]
    decomp_seq = list()
    j =0
    while j < len(seq):
        if j<=(len(seq)-2):
            if (seq[j] == 0) and (seq[j+1] == 0):
                print('0', end=' ')
                decomp_seq.append(int(0))
                j=j+1
            elif (seq[j] == 0) and j<=(len(seq)-3):
                rep = seq[j+1]
                val = seq[j+2]
                for k in range (rep):
                    decomp_seq.append(int(val))
                    print(val, end=' ')
                j = j + 2
            else:
                decomp_seq.append(int(seq[j]))
                print(seq[j], end=' ')
        else:
            decomp_seq.append(int(seq[j]))
            print(seq[j], end=' ')
        j = j+1
