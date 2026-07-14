print("Enter any num:\n")
num=int(input())
fact=1
for i in range (1,num):
    fact=fact*i
    print("Factorial of num",num,"is:",fact)