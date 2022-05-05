import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();p=L();d=[0]*n;r=0;l=[];v=[0]*n
    if n==1:print(1);print(1);print(1);continue
    for i in range(n):d[i]+=1;d[p[i]-1]+=1
    l=[i for i in range(n) if d[i]==1]
    print(len(l))
    for i in l:
        cur=i;l1=[]
        while v[cur]==0:
            l1.append(cur+1);v[cur]=1;cur=p[cur]-1
        print(len(l1));print(*l1[::-1])
    print()