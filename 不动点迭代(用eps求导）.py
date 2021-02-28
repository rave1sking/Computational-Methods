import numpy as np

def fun(x):
    return x**5 - 2*x -1
def fun1(x):
     return  np.sign(2*x+1)*abs((2*x+1))**(1/5)
     # return  (2*x+1)**(1/5)
def fun2(x):
    return (x**5-1)/2
a, b, d= map(float, input().split()) #输入
d = int(d)
epsilon = 10 ** (-d)
x = np.linspace(a, b, 9)   # 构造一个8等分数列
print(x)
y = fun(x)
arr = []                   # arr 用来存放可疑解
def Trial():
    #找到可疑解
    for i in range(1,len(x)):
        if(y[i-1]*y[i]<0):
            arr.append((x[i] + x[i - 1]) / 2)
        elif((y[i]-y[i-1])*(y[i+1]-y[i])<0 and abs(y[i])<0.01):
            arr.append(x[i])
eps = np.finfo(np.float).eps
def Fixed_point_iteration():
    for i in arr:
        if abs(fun1(i) - fun1(i-eps)) / eps < 1 :
            while True:
                previous_i = i
                i = fun1(i)  # 迭代
                if abs(i - previous_i) < epsilon:
                    x=float(i)
                    print('%.3f' % i)
                    break
        else:
            x=fun2(i)
            if  abs(fun2(i) - fun2(i-eps)) / eps<1:
                while True:
                    previous_i = i
                    i = fun2(i)  # 迭代
                    if abs(i - previous_i) < epsilon:
                        x=float(i)
                        print('%.3f' % i)
                        break
if __name__ =='__main__':
    Trial()
    Fixed_point_iteration()