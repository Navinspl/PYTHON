# word = input()
# valid =False 
# #both 'a' and 'z' arein lower case 
# if 'a' <= word[0] <= 'z':
#     if word[0] == word[-1]:
#         valid=True
# print(valid)        

# ##Q3
# word = input()
# space = ' '
# if len(word) < 4:
#     print()



# ###Q4
# num = input()
# first,middle,third =num[0],num[1],num[2]
# if first+third == middle:
#     print("sandwhich")
# else:
#     print("plain")    


# ###q5,6,7,8
# x =int(input())
# y =int(input())
# z =int(input())
# #block -1 start
# if x > 0 or y > 0 or z > 0:
#     if (x>0 and y>0) or (y>0 and z>0) or (z>0 and x>0) :
#         if x>0 and y>0 and z>0:
#             print('P3')
#         else:
#             print('P2')
#     else:
#         print('p1')
# #block-2 start
        
# if x < 0 or y < 0 or z < 0:
#     if (x<0 and y<0) or (y<0 and z<0) or (z<0 and x<0) :
#         if x<0 and y>0 and z>0:
#             print('N3')
#         else:
#             print('N2')
#     else:
#         print('N1')
# #block-2 start

##
sentence = input()
space=''
num_word =sentence.count(sentence)
print(num_word)