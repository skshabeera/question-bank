n=int(input("enter the number"))
if n%4==0 and n%100!=0:
    print(n,"leap year")
else:
    print(n,"not leap year")