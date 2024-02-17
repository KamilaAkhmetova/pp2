import math
def r(d):
    rad=d*math.pi/180
    return rad

d=int(input("Input degree: "))
res=r(d)
print("Output radian:", res)