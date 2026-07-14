def num_is_even_num(n):
    evens=[]

    for i in n:
         
         if i%2==0:
          
          evens.append(i)

    for i in range(len(evens)):

        evens[i]=evens[i]**2

    return sum(evens)
x=[1,2,3,4,6,7]
print(num_is_even_num(x))