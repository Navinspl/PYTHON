n = int(input("Entre any number:"))

for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1))

# reverse pyramid

for i in range(n,0,-1):
    print(" "*(n-i),"*"*(2*i-1))

# factorial
fact=1
for i in range(1,n+1):
    fact *=i

print(fact)

# f string use c
print(f'{"name "}')

# prime number

if n<=1:
    print("Not a prime number.")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            print("Not a prime number.")
    else:
        print("Prime Number.")    


count = 0 

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Prime Number.") 

else:
    print("Not a prime Number.") 

# fibbonaci series 
a,b=0,1

print("Fibonnaci series")
for i in range(n):
    print(a,end=" ")
    c = a+b
    a=b
    b=c 

for i in range(n):
    print(i)
    if i==5:
        break
# print 1 to 50 skip 20
for i in range(n):
    if i==20:
        continue
    if i%2 ==0:
        print(i)
   

for i in range(1,11):
    n=2
    print(f"{n}*{i} = {n*i}")
 
for i in range(1,11):
    n1,n2,n=3,4,2
    print(f"{n}*{i} = {n*i} ,{n1}*{i} = {n1*i},{n2}*{i} = {n2*i}")
 
for i in range(1,11):
    n2=4
    print(f"{n}*{i} = {n*i}")


