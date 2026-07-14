def sum(n):
   if(n==1):
     return 1
   else:
      return sum(n-1)+n
   
print(sum(5))

def comp(p,n):
   if(n==1):
      return p*1
   else:
      return (comp(p,n-1))*(1.1)
   
print(comp(2000,3))
def fact(n):
   if(n==1):
      return 1
   else:
      return (fact(n-1)*n)
   
print(fact(5))
def check0(L):
   if (len(L)==0):
      return False
   if L[0]==0:
      return True
   else:
      return check0(L[1:len(L)])
   
print(check0([2,1,3,4,50,1]))