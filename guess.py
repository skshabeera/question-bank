n=int(input("enter the number"))
i=0
while i<=n:
    guess=int(input("enter the number"))
    if n==guess:
        print("guess is correct")
        break
    else:
        print("your guess is not correct")
    i=i+1