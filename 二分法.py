def DeFun():
    a,b,d=map(float,input().split())
    d=int(d)
    count = 0
    while(1):
      c =(a+b)/2
      if (b-a)/2<0.5*0.1**d :
         print(count)
         print(round(c,d))
         break
      else:
          if ((3600/a)*((1+a/12)**240-1)-500000)*((3600/c)*((1+c/12)**240-1)-500000) <0:
              b=c
          else:
              a=c
      count+=1

if __name__ == '__main__':
    DeFun()
