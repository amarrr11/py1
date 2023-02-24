def palin (n):
    rev=0
    z=n
    while(z>0):
        rev=rev*10+z%10
        z=z//10
    if rev==n:
        print("palindrome")
    else:
        print("not palindrome")
n=int(input("enter num to check"))
palin(n)
