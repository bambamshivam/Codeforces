import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=L();m=max(a);d={};c={};f=0
    for i in a:
        j=i
        while j%2==0:j//=2
        d[j]=0;c[j]=c.get(j,0)+1
    for i in b:
        p=i
        while p>=1:
            if p in d:
                d[p]+=1
            p//=2
    for i in b:
        p=i;z=[]
        cur=-1;m=math.inf
        while p>=1:
            if c.get(p,0)>0:
                if d[p]<m:m=d[p];cur=p
                z.append(p);d[p]-=1
            p//=2
        if cur!=-1:
            c[cur]-=1
    for i in c:
        if c[i]>0:f=1;break
    print("NO" if f else "YES")