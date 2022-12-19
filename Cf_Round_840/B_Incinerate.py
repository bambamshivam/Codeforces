import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();h1=L();p1=L();f=0;c=0
    a=sorted([[p1[i],h1[i]] for i in range(n)])
    for i in range(n):
        p=a[i][0];h=a[i][1]-c
        if h<=0:continue
        if i!=0:k-=p
        if k<=0:f=1;continue
        if ((p+2*k)**2) - 8*p*h<0:f=1;break
        

        #x*k - p*(x*(x-1))/2 >= h

        #2*k*x - p*x*x + x*p >= 2*h

        #p*x*x - (p+2*k)*x + 2*h <= 0

        t=math.ceil((p+2*k - (((p+2*k)**2 - 8*p*h)**(0.5)))/(2*p))
        c+=t*k - (p*(t*(t-1))//2);k=k-(t-1)*p
    print("NO" if f else "YES")