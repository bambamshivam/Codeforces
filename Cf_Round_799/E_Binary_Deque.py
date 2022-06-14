import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,s=M();a=L();ans=-1
    i=j=c=0
    while j<n and i<n:
        while j<n and c+a[j]<=s:c+=a[j];j+=1
        if c==s:ans=max(ans,j-i)
        while i<n and a[i]==0:i+=1
        i+=1;c-=1
    print(n-ans if ans!=-1 else -1)