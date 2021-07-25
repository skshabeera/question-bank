n=int(input("enter the number"))
if n%5==0 and n%11==0:
    print(n,"5 and 11 is divisible")
elif n%5==0:
    print(n,"is divisible by 5")
elif n%11==0:
    print(n,"is divisible by11")
else:
    pass