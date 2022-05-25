import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=sorted(L());ans=[];f=0
    if n%2:print("NO");continue
    b=a[:n//2];c=a[n//2:]
    for i in range(n//2):ans.append(b[i]);ans.append(c[i])
    for i in range(n):
        p=i-1 if i>=1 else n-1
        q=i+1 if i<n-1 else 0
        if (not ans[p]<ans[i]>ans[q]) and (not ans[p]>ans[i]<ans[q]):f=1;break
    if f:print("NO");continue
    print("YES");print(*ans)