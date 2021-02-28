import numpy as np
#import math 好像用不着
#直接按照PPT上的公式进行求解
def func(x):
    return 2+np.sin(2*np.sqrt(x))


a,b,m = map(int,(input().split()))

h = (b-a)/m
s = 0

s+=(h/2)*(func(a)+func(b))

for k in range(1,m):
    s+= h * func(a+k*h)

print("{:.8f}".format(s))


