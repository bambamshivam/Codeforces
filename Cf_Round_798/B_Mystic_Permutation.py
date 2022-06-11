import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();p=L();i=0;j=1;ans=[]
    if n==1:print(-1);continue
    while i<n:
        if p[i]==j:
            if j+1<=n:ans.append(j+1);ans.append(j);j+=2;i+=2
            else:a=ans.pop();ans.append(j);ans.append(a);j+=1;i+=1
        else:ans.append(j);j+=1;i+=1
    print(*ans)