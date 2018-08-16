n=int(input("Enter number of elements:"))
a=[]
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
largest=a[0]
for i in range(n):
    if largest<a[i]:
        largest=a[i]

print("largest",largest)

