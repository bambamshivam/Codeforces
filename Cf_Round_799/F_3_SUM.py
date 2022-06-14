import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();d={};l=[];z=0
    for i in range(n):a[i]%=10;d[a[i]]=d.get(a[i],0)+1
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if str(i+j+k)[-1]=='3':
                    f=0;p=[0]*10
                    p[i]+=1;p[j]+=1;p[k]+=1
                    for t in range(10):
                        if d.get(t,0)<p[t]:f=1;break
                    if f==0:z=1
    print("YES" if z else "NO")