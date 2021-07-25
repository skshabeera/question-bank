a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a==b and b==c and c==a:
    print("it is triangle")
elif a==b and b==c and c!=a:
    print("it is eqilater")
elif a!=b and b!=c and c!=a:
    print("it is  isolatetr")
else:
    pass