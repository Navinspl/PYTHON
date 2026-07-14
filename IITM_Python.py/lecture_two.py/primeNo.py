lower=int(input("enter lower range:"))
upper=int(input("Enter upper range:"))
print("Prime numbers between {} abd {} are:".format(lower,upper))
for num in range (lower,upper):
    if num > 1:
        for i in range (2,num):
            if(num%i)==0:
                break
        else:
            print(num)    