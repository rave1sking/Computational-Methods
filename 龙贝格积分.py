import numpy as np


#逐列求R(J，n)
def func(x):
    return (x**2 + x + 1) * np.cos(x)

n = int(input())

# h = b - a
h = np.pi / 2      # h = PI/2
M = 1
arry = np.zeros((n, 4), dtype = np.double)

#R(J,0) = T(J)
#第一列，递推梯形公式
#M = 2^j / 2
arry[0, 0] = h * (func (0) + func (h)) / 2
for i in range(n-1):
    M *= 2
    h /= 2
    s= 0
    for k in range(1,int(M/2)+1):
        x =  h * (2*k - 1)
        s += func(x)
        arry[i + 1, 0] = arry[i, 0] / 2 + h*s
#第二列到第n列，
for j in range(1, n):
   for k in range(1, 4):
        if k > j:
          break
        arry[j, k] = arry[j, k - 1] + (arry[j, k - 1] - arry[j - 1, k - 1]) / (4 ** k - 1)
    # 输出
print(arry)