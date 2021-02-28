import numpy as np

n  = int(input())

a = np.zeros((n,n),dtype= np.double)
for i in range(n):
  a[i,:] = np.array(input().split(),dtype=np.double)
b = np.zeros((n,1),dtype = np.double)
for i in range(n):
  b[i] = np.array(input(),dtype=np.double)

#r为置换矩阵
r = np.arange(n)

for i in range(n-1): #i为列
    max  = a[i][i]
    local = i
    flag = 0
    for j in range(i+1,n):
      if(max < a[j][i]):
        max  = a[j][i]
        local = j
        flag = 1                                 #local为最大元素所在位置
    if(flag==1):
      a[[i, local], :] = a[[local, i], :]
      r[local],r[i] = r[i],r[local]                #高斯消去换行
    for j in range(i+1,n):
       m  = a[j][i]/a[i][i]
       a[j][i] = m
       a[j,i+1:] = a[j,i+1:]-m*a[i,i+1:]    #将a写成L+U
#用a求y(程序3.3),回代求x
x = np.zeros((n, 1), np.double)
y = np.zeros((n, 1), np.double)
for k in range(n):
    y[k] = b[r[k]] - a[k, :k] @ y[:k]
for k in range(n-1, -1, -1):
    x[k] = (y[k] - a[k, k+1:n] @ x[k+1:n]) / a[k, k]

print(a)
print(x)