# for loop in class disciuss 
# for i in range(5) matlab 0 se 4 tak print hoga 
# range(1,5) 1 se 4 tak
# range(1,10,2) me 1 ,3 ,5 ,7 , 9 tk print hoga 
# print() next line 
# print("*" * 3) means * ko 3 baar print karna hai 
# end= " " ye ye print me space ya next line me create karne ke liye use karte hai 


for i in range(5):
    print("My name is navin kumar")

# odd without using modulo operator 
for i in range(1,10,2):
    print (i)  
 
# even without using modulo operator 
for i in range(0,10,2):
    print(i)

for i in range(1,5):
    print("*"*3)

for i in range(2):
    print("navin kumar", end =" ")

# pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

for i in range(3):
    print("*"*3)
n=int(input("Enter any number:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

# pattern
for i in range(3):
    print("*"*i)
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=int(input("Enter any number:"))
for i in range(1,n):
    for j in range(i):
        print(j+1,end=" ")
    print()

for i in range(0,n):
    print(" "*(n-i), "*"*(2*i+1),end="\n")



