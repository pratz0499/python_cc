
m=[[" "," "," "],[" "," "," "],[" "," "," "]]


def checkandplace(m,a,b,x):
    if m[a][b]=="x" or m[a][b]=="o":
        return 4
    else:
        m[a][b]=x
    
def board(m):
    for i in m:
        print(i)

def winner(m,a,b,x):
    if m[0][0]==m[0][1]==m[0][2]==x or m[1][0]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[1][0]==m[2][0]==x\
    or m[0][1]==m[1][1]==m[2][1]==x or m[0][2]==m[1][2]==m[2][2]==x or m[0][0]==m[1][1]==m[2][2]==x or m[0][2]==m[1][1]==m[2][0]==x:
        return True

def draw(m,a,b,x):
    if m[0][0]=="" or m[0][1]=="" or m[0][2]=="" or m[1][0]=="" or m[1][1]=="" or m[1][2]=="" or m[2][0]=="" or m[2][1]=="" or m[2][2]=="" :
        return 1
    else :
        return 0
        
while True:
    print("Player A turn")
    a=int(input("X="))
    b=int(input("Y="))
    w=checkandplace(m,a,b,"x")
    if w==4:
        print (" overlap is not allowed ")
    board(m)


    p=winner(m,a,b,"x")
    if p==True:
        print ("A IS THE WINNER")
        exit(0)

    k=draw(m,a,b,"x")
    if k==1:
        print ("THE GAME IS DRAW")
        exit(0)
        

    

    print("Player B turn")
    a=int(input("X="))
    b=int(input("Y="))
    w=checkandplace(m,a,b,"o")
    if w==4:
        print(" overlap is not allowed ")

    board(m)

    p=winner(m,a,b,"o")
    if p==True:
        print ("B IS THE WINNER")
        exit(0)

    k=draw(m,a,b,"o")
    if k==1:
        print ("THE GAME IS DRAW")
        exit(0)
        


   
