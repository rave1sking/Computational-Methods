import numpy as np
#跟组合梯形公式差别不大
def func(x):
    return 2+np.sin(2*np.sqrt(x))


a,b,m = map(int,(input().split()))


h = (b-a)/(2*m)
s = 0

s+=(h/3)*(func(a)+func(b))

for k in range(1,m):
    s+= (2*h/3)*func(a+2*k*h)
for k in range(1,m+1):
    s+=(4*h/3)*func(a+(2*k-1)*h)

print("{:.8f}".format(s))