def search(a,n,key):
    flag=0
    for i in range(n):
        if a[i]==key:
            flag=1
            position=i
            break
    if flag==1:
        print("value found at=",position+1,"position")
    else:
        print("not found")
n=int(input("enter size"))
a=[]
for i in range(n):
    val=int(input("enter num"))
    a.append(val)
key=int(input("enter num to search"))
search(a,n,key)
