def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return 1
    else:
        return 0
n=int(input("enter num to check"))
z=prime(n)
if z==1:
    print("prime")

else:
    print("composite")
