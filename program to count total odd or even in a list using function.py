def count(a,n):
    odd=0
    even=0
    for i in range(n):
        if (a[i]%2==0):
            even=even+1
        else:
            odd=odd+1
    print("total even=",even,"total odd=",odd)
n=int(input("Enter size of list"))
a=[]
for i in range(n):
    val=int(input("enter number"))
    a.append(val)
count(a,n)
