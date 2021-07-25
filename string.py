str1=input("enter the number")
if len(str1)> 2:
    if str1[-3:] == 'ing':
        str1 += 'ly'
    else:
        str1 += 'ing'
    print(str1)
