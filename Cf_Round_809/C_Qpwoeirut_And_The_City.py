import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    if n%2:
        ans=0
        for i in range(1,n-1,2):
            ans+=max(max(a[i-1],a[i+1])-a[i]+1,0)
        print(ans)
    else:
        ans=math.inf
        l1=[0]*(n//2);c=0
        for i in range(1,n-1,2):
            l1[c+1]=max(max(a[i-1],a[i+1])-a[i]+1,0)
            c+=1
        l2=[0]*(n//2);c=0
        for i in range(2,n-1,2):
            l2[c]=max(max(a[i-1],a[i+1])-a[i]+1,0)
            c+=1
        for i in range(len(l1)-1):
            l1[i+1]+=l1[i]
        for i in range(len(l2)-2,-1,-1):
            l2[i]+=l2[i+1]
        for i in range(1,n-1):
            ans=min(ans,l1[i//2]+l2[i//2])
        print(ans)