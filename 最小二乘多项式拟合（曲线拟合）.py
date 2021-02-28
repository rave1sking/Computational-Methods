#1、输入最高次
#2、输入数据点个数
#3、F是[x0**0 , x0**1 ,x0**2], [x1**0, x1**1, x1**2],……
#4、求F'F
#5、求F'Y
#6、F'F C = F'Y 求C 并逆向输出
#7、Yk = F @ C  err = np.linalg.norm(Y-Yk) 求误差

import numpy as np
M = int(input())
N = int(input())

Matrix_Input = np.zeros((N,2),dtype=np.double)

for i in range(N):
    Matrix_Input[i:] = input().split()

X = Matrix_Input[:,0]
Y = Matrix_Input[:,1]

F = np.zeros((N,M+1),dtype= np.double)

for i in range(N):
    for j in range(M+1):
        F[i,j] = X[i]**j

A = F.T@F
B = F.T@Y
# a = np.matrix(A)
# A_re=(a.I)
#
# C = A_re@B
C = np.linalg.inv(A) @ B
Yk = F@C
err = np.linalg.norm(Y-Yk)

print(C[::-1])
print("{:.7f}".format(err))







