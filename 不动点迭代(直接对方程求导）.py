import numpy as np

def fun(x):
    return x**5 - 2*x -1
def fun1(x):
    return np.sign(2 * x + 1) * abs((2 * x + 1)) ** (1 / 5)
def fun2(x):
    return (x ** 5 - 1) / 2
def derivative_fun1(x):
     return  (2/5)*np.sign(2*x+1)*abs((2*x+1))**(-4/5)     # 对fun1求导
def derivative_fun2(x):
    return 5*(x**4)/2                                      # 对fun2求导
a, b, d= map(float, input().split()) #输入
d = int(d)
epsilon = 10 ** (-d)
x = np.linspace(a, b, 9)   # 构造一个8等分数列
y = fun(x)
arr = []                   # arr 用来存放可疑解
def Trial():               # 找到可疑解 可疑解的判断方法：y[i-1]*y[i]<0 or (y[i]-y[i-1])*(y[i+1]-y[i])<0 and abs(y[i])<0.01
    for i in range(1,len(x)):
        if(y[i-1]*y[i]<0):
             arr.append((x[i] + x[i - 1]) / 2)
        elif((y[i]-y[i-1])*(y[i+1]-y[i])<0 and abs(y[i])<0.01):
            arr.append(x[i])
def Fixed_point_iteration(): #不动点迭代
    for i in arr:
        if abs(derivative_fun1(i))<1 :
            while True:
                previous_i = i
                i = fun1(i)  # 迭代
                if abs(i - previous_i) < epsilon:
                    print('%.3f' % i)
                    break
        else:
            if derivative_fun2(i)<1 :
                while True:
                    previous_i = i
                    i = fun2(i)  # 迭代
                    if abs(i - previous_i) < epsilon:
                        print('%.3f' % i)
                        break
if __name__ =='__main__':
    Trial()
    Fixed_point_iteration()