days=int(input("enter the number"))
year=days/365
weeks=(days%365)/7
days=(days%365)%7
print(year)
print(weeks)
print(days)