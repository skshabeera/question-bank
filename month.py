m=int(input("enter the number"))
if m==1 or m==3 or  m==5 or m==7 or m==8 or m==10  or m==12:
    print(m," month number of days 31")
elif m==4 or m==6 or m==9 or m==11:
    print(m,"month number of days 30")
elif m==2:
    print(m,"month number if days 28")
else:
    pass