import numpy as np
n = int(input())

a = np.array([input().split() for i in range(n)],dtype=np.double)

b = np.array([input() for i in range(n)],dtype=np.double).reshape(n, 1)

Matr = np.hstack((a, b))

#高斯消去

#找最大元并交换
for i in range(n):    #i列
  max = Matr[i][i]
  flag = 0
  for j in range(i+1,n):
    if(Matr[j][i]>max):
      max = Matr[j][i]
      c = j
      flag = 1
  if(flag == 1):
   Matr[[i,c],:] = Matr[[c,i],:]
  for j in range(i+1,n):           #交换后立刻进行运算。等全部交换完毕后再计算：会造成矩阵不同
    m = Matr[j][i]/Matr[i][i]
    Matr[j,0:n+1] -= m*Matr[i,0:n+1]
print(Matr)
a = Matr[:, :n]
b = Matr[:, n]

x = np.zeros((n, 1))
x[n-1] = b[n-1] / a[n-1, n-1]

for k in range(n-2, -1, -1):      #步长为-1
    x[k] = (b[k] - a[k, k+1:n] @ x[k+1:n]) / a[k, k]
print(x)