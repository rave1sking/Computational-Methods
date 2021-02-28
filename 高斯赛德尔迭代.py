import numpy as np

n = int(input())
A = np.zeros((n,n),dtype=np.double)
B = np.zeros((n,1),dtype=np.double)
for i in range(n):
    A[i:] =  np.array(input().split(),dtype = np.double)
for i in range(n):
    B[i] = np.array(input().split(),dtype=np.double)
delta = 1E-9
Max_iteration = 20
p =  np.zeros((n,1),dtype=np.double)
for i in range(n):
    p[i] = np.array(input().split(),dtype=np.double)
X = np.zeros((n,1),dtype=np.double)
X = p.copy()
for k in range(Max_iteration):
    for j in range(n):
         X[j] = (B[j] - np.delete(A[j, :], j) @ np.delete(X, j)) / A[j, j]
    err = np.linalg.norm(X - p)
    relerr = err / (np.linalg.norm(X) + np.finfo(np.float32).eps)
    p = X.copy()
    if err < delta or relerr < delta:
        print(k)
        print(X)
        break