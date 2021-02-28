def fun(a):
    return (3600/a)*((1+a/12)**240-1)-500000
def Defun():
    a,b,d=map(float,input().split())
    count = 0
    d=int(d)
    while(1):
        c=b- (fun(b)*(b-a))/(fun(b)-fun(a))
        x= abs(fun(c))
        if x<0.0001 or ((b-a)< 0.5 * 10 ** (-d)):
            print(count)
            print(round(c,d))
            break
        else:
            if fun(a)*fun(c) < 0 :
                b=c
            else:
                a=c
        count+=1
if __name__ == '__main__':
    Defun()