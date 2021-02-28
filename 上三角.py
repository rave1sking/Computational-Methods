import numpy as np

n  = int(input())

a = np.array([input().split() for i in range(n)], np.double)

b = np.array([input() for i in range(n)], dtype=np.double).reshape(n, 1)

Matr = np.hstack((a, b))
#以下方法不提倡
# A = np.matrix(a)
#
# e = (A.I)
#
# ans = np.dot(e,b)
#
# print(ans)

#a = Matr[:, :n]
#b = Matr[:, n]

x = np.zeros((n, 1))     #初始化n行矩阵
x[n-1] = b[n-1] / a[n-1, n-1]  #最后一项

for k in range(n-2, -1, -1):      #步长为-1
    x[k] = (b[k] - a[k, k+1:n] @ x[k+1:n]) / a[k, k]
print(x)
