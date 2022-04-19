import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();s=list(S());c=0;ans=[0]*n
    for i in range(n):
        if c==k:break
        if s[i]=='0' and k%2==0:ans[i]=1;c+=1
        if s[i]=='1' and k%2==1:ans[i]=1;c+=1
    ans[-1]+=k-c
    for i in range(n):
        if (k-ans[i])%2==1:s[i]=str(1-int(s[i]))
    print("".join(s));print(*ans)