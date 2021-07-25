p=int(input("enter num"))
t=int(input("enter num"))
r=int(input("enter num"))
amount=p*(pow((1+r/100),t))
ci=amount-p
print(ci)