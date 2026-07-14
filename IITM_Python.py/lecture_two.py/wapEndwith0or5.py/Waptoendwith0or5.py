num=input()
if num[len(num)-1] in '105':
    print('end with either 0,1 or 5')
    print(num[len(num)-1])
else :
    print('any other number')