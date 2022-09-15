import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();x=L();y=L();a=[]
    for i in range(n):a.append(y[i]-x[i])
    a.sort();p=[];q=[]
    for i in a:
        if i>=0:p.append(i)
        else:q.append(i)
    i=0;j=0;k=len(p)-1;ans=0
    while True:
        if i<len(q) and k>=j:
            if p[k]+q[i]>=0:ans+=1;i+=1;k-=1
            else:i+=1
        elif k-j+1>1:j+=1;k-=1;ans+=1
        else:break
    print(ans)