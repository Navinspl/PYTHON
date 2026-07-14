def fact_cal(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact_cal(n-1)
    numb=input("Enter any number:")
num=fact_cal(6) 
print(num)   