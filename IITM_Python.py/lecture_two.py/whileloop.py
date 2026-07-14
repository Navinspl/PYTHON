# import time
# f= 10
# t=0
# while t<f:
#     print(f)
#     time.sleep(1)
#     f-=1
# print("Go!")
lower=0
upper=300
step=20
fahr=lower
while fahr < upper:
    celsius=5*(fahr-32)/9
    print("{} F\t {}C".format(fahr,celsius))
    fahr=fahr+step