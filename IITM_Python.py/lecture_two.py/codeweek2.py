#chem_mark = 95#this varible contains chemistry marks 
#code2
# a=10
# print(type(a))

##code3

# a='india'
# print(type(a))

##code 4
# n=10
# print(n)
# print(type(n))
# n=n/2
# print(n)
# print(type(n))

##code5
# _0=5
# print(_0)

##code6
# roll=5
# ROLL=10
# Roll=15
# print(roll,ROLL,Roll)

##code7   ##multiple assignment

# x,y=1,2
# print("value of x is",x)
# print("Value of y is",y)

##code8
# x=y=z=1
# print(x,y,z)

##swapping the varible 
# x,y=1,2
# x,y=y,x
# print(x,y)

##deleting a vriable 
# x=5
# print(x)
# del(x)
# print(x)

##short hand operater 
# z = 0 
# z += 1
# z += 1
# z += 1
# print(z)

# ##code9
# a=2
# a*=2
# print(a)

#### use in operater 
# print('alpha' in 'we can use alpha-numberic characters.')
# print('alpha'in 'we canuse letters and number.')

## chaining operaters
# x=5
# print(1<x<10)
# print(10<x<20)
# print(x<10<x*10<100)
# print(10>x<=9)
# print(5==x>4)

## Escape characters
# #backslash(\)
# print("'It's a beautiful day.")
# print("My name is xyz.\nI am from abc")
# print('It\'s a beautiful day.')

##backslash t
# print('My name is xyz .I am from abc.')
# print('my name is xyz.\tI am from abc')

#3triple quotes
#we can use triple quotes to:-
# 1. store multiple strings.
# 2. To comment out more than 1 line .

# z= '''first line
# second line 
# third line'''
# print(z)


##string method 
# x='Python sTrIng mEtHod'
# print(x.upper())
# print(x.lower())
# print(x.capitalize())
# print(x.title())
# print(x.swapcase())

## importants
# X='python'
# print(X.islower())
# print(X.isupper())
# x='python String is title'
# print(x.istitle())
# x='123'
# print(x.isdigit())
# x='abcd123'
# print(x.isalpha())
# print(x.isalnum())

## code10
# x='___Python____'
# print(x.strip('_'))

##code11
# alpha='abcdefghijklmnopqrstuvwxyz'
# s='india'

# t=''
# i=0
# k=27
# t+=(alpha[(((alpha.index(s[i]))+k)%26)])
# t+=(alpha[(((alpha.index(s[i+1]))+k)%26)])
# t+=(alpha[(((alpha.index(s[i+2]))+k)%26)])
# t+=(alpha[(((alpha.index(s[i+3]))+k)%26)])
# t+=(alpha[(((alpha.index(s[i+4]))+k)%26)])

# print('original string',s)
# print('encrypted sting:',t)

## if statement 
# code
# birth_year = int(input('plese enter your date of birth:'))
# current_year = 2025
# age = current_year - birth_year
# if (age<13):
#     print('you are under age,you can not watch this movies.')
#     print('wait until you are old enough to watch the movies.')
# else:
#     print('you are old enough to watch average, Enjoy!')
#     print('Don\'t forget to watch sequeal and presequal.')

# print('Have a nice day')    

##if else and else-if(elif) conditions
#1.even or odd number
# num=int(input('Enter a number:'))

# if (num%2==0):
#     print('The given numbeu is evenNumber.')
# else:
#     print('The given numbe is odd Number.')    

## number end with 0 or 5 
# num=int(input('enter a number:'))

# if(num%5==0):
#     if(num%10==0):
#         print(' The given number end with 0')
#     else:
#         print('The given number end with 5')
# else:
#     print('Other')            


##3. find the average of the student based on the given mark from 0 to 100
# mark =int(input('Enter your marks:'))
# if (mark>=0 and mark<=100):
#     if(0<=mark<60):
#         print('grade E')
#     elif(60<=mark<70):
#         print('grade D')
#     elif(70<=mark<80):
#         print('Grade C')
#     elif(80<=mark<90):
#         print("grade B")
#     elif (90<=mark<100):
#         print("Grade A")
# else:
#     print("The output is invalid.")        
                
  ##4.

# print('Trave from City A to City B')
# Time= int(input('Enter time:'))
# Longer=int(input('Define longer:'))
# if(time>=Longer):
#     price=int(input('Enter price:'))
#     Higher=int(input('Define higher:'))
#     if(price>=Higher):
#         print('Train')
#     else:
#         print('Coach')

# else:
#     price = int(input('Enter price:'))
#     Higher =int(input('define higher:'))
#     if(price>=Higher):
#             print("Daytime flight.")
#     else:
#             print("red eye flight")
#     print('Arrive city B')                       




# ## Library function in python :-
# import math 
# print(math.log(10))
# print(math.sin(90))
# print(math.sqrt(4))
# print(math.factorial(5))
# print(math.pow(10,3))

# ##it imports the random library
# import random 
# print(random.random())


# ## let us simulate a coin toss-
# import random 
# a=random.random()
# if ( a<0.5):
#     print('Heads')
# else:
#     print('Tails')    

# ## let us simulate a six faced dice-
# import random 
# print(random.randrange(1,7))

# ## let us simulate the sum of 2 six faced die-
# import random 
# dice1 =(random.randrange(1,7))
# dice2 =(random.randrange(1,7))
# total=dice1+dice2
# print('You pair of dice is:',total)


##different way to import library :-
#first way:-
 
# import calendar
# print(calendar.month(2021,2))

# ##all months print import methode
# import calendar 
# print(calendar.calendar(2007))
import math
print(math.sin(135))