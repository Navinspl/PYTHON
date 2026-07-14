def mini(L):

    mini=L[0]

    for i in L:

        if(i<mini):
            mini=i
    return mini

def sort(L):

    if(L==[]) or (len(L)==0):
        return L
    m=mini(L)

    L.remove(m)

    return [m]+sort(L)
L=[5,56,45,87,2,8,5,885,5,25686,554,552,0]
print(sort(L))
