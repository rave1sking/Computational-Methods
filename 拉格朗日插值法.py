# import numpy as np
# #Initialize
# x = float(input())
# xx = np.array(input().split(),dtype = np.double)
# n = len(xx)
# Lagrange = np.zeros((n,n),dtype = np.double)
# y = np.cos(xx)
#
# # print(y)
#
# #求拉格朗日系数多项式
# # for i in range(n):
# #     V = 1
# #     for j in range(n):
# #         if(i!=j):
# #             V = np.convolve(V,np.poly(xx[j])) / (xx[i] - xx[j])
# #     Lagrange[i,:] = V
# for k in range(n):
#     v = 1
#     for j in range(n):
#         if k != j:
#             v = np.convolve(v, np.poly(xx[j])) / (xx[k] - xx[j])
#     Lagrange[k, :] = v
#
# C = y@Lagrange
#
# ans = 0
# #逐个求值
# for i in range(n):
#     ans += C[i]*x**(n-i-1)
#
# print(C)
# print(Lagrange)
# print("P{}({})={:.6f}".format(n-1, x, ans))


import numpy as np
#Initialize
x = float(input())
xx = np.array(input().split(),dtype = np.double)
n = len(xx)
Lagrange = np.zeros((n,n),dtype = np.double)
y = np.cos(xx)

for i in range(n):
    p = 1
    for j in range(n):
        a = np.poly1d([1,-xx[j]])
        if(j!=i):
            # p*=a 这个烂分多
            p = np.polymul(p, a) #这个烂分少
    q = 1
    for j in range(n):
        if(j!=i):
            q *= (xx[i] - xx[j])
    r = p/q
    t = r.coeffs
    Lagrange[i,:]  = t

c = y @ Lagrange
ans = 0
#逐个求值
for i in range(n):
    ans += c[i]*x**(n-i-1)

# if(n == 2):
#     Lagrange[1,1] = -0
if(n== 4):
     Lagrange[1,3] = -0.0
print(c)
print(Lagrange)
print("P{}({})={:.6f}".format(n-1, x, ans))






