import numpy as np

#Initialize

x  = float(input())
xx = np.array(input().split(),dtype = np.double)

y = np.cos(xx)
n = xx.size

##计算差商表：
d = np.zeros((n, n), np.double)
d[:,0] = y
for j in range(1,n):
    for k in range(j,n):
        d[k,j] = (d[k,j-1] - d[k-1,j-1]) / (xx[k] - xx[k-j])  #按照书中的公式逐列进行计算

#嵌套成发求多项式s 其中s(n-1) = d[n-1][n-1] 且 s(n-2) = s(n-1)*(x - x(n-2)) + d[n-2][n-2] 以此类推。
s = d[n-1,n-1]

for j in range(n-2,-1,-1):
    s= np.polymul(s,np.poly1d([1,-xx[j]]))
    s+=d[j][j]

print(s.coeffs) #取系数
#print(s)
print(d)


print("P{}({})={:.6f}".format(n-1,x,np.polyval(s,x))) #np.polyval计算s(x)



