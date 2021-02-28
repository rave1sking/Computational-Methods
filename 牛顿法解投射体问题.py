import numpy as np

def r(t):
    return 2400 * (1 - np.exp(((0 - t) / 15.0)))
def f(t):
    return 9600 * (1 - np.exp((0 - t) / 15.0)) - 480 * t
def derivative_f(t):
    return 640 * np.exp((0 - t) / 15.0) - 480
p,eps1,eps2=map(float,input().split( ))
delta  = 10**(-eps1)
epsilon = 10**(-eps2)
previous_p = p
while(True):
    p_k = previous_p - f(previous_p)/derivative_f(previous_p)
    err= abs(p_k - previous_p)
    relerr = 2*err / (abs(p_k) + eps1/10)
    previous_p = p_k
    if(abs(f(p_k))<epsilon or abs(err) < delta  or relerr < delta):
        t=p_k
        break
print('%.5f' %t)
print('%.5f' %r(t))

