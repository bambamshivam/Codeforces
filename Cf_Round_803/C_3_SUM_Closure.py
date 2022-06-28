import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();c1=c2=c3=f=0;l=[]
    for i in range(n):
        if a[i]!=0:l.append(a[i])
        if a[i]>0:c1+=1
        if a[i]<0:c2+=1
        if a[i]==0:c3+=1
    if c1>=3 or c2>=3:print("NO");continue
    if c3>0:l.append(0)
    n1=len(l)
    for i in range(n1):
        for j in range(i+1,n1):
            for k in range(j+1,n1):
                if l[i]+l[j]+l[k] not in l:f=1
    print("NO" if f else "YES")