import numpy as np

n = int(input())

x = np.zeros((n,1),dtype = np.float)
y = np.zeros((n,1),dtype = np.float)

for i in range(n):
    x[i, :], y[i, :] = map(int, input().split())

averageX = sum(x)/n
averageY = sum(y)/n

C = 0
for i in range(n):
    C+=(x[i,0] - averageX)**2

A = 0
for i in range(n):
    A += (x[i,0]-averageX)*(y[i,0]-averageY)

A/=C

B=averageY - A*averageX

print("y={:.7f}x+{:.7f}".format(float(A),float(B)))

# E = 0
# for i in range(n):
#     E += (abs(A*x[i,0]+B-y[i,0]))**2
# E/=n
# E = E**(1/2)
#norm2范数：距离
E = np.linalg.norm(y-(A*x+B))
print("{:.7f}".format(float(E)))