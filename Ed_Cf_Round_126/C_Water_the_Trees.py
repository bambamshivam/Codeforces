"""import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();m1=max(a)
    s=sum(m1-a[i] for i in range(n))
    l=0;r=s*2
    while l<=r:
        m=(l+r)//2
        e=m//2;o=m-e
        d=[m1-a[i] for i in range(n)]
        """
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0;m,n=[0,0,0],[0,0,0];t=max(a)
    for i in a:
        for j in range(3):
            m[j]+=((t+j-i)//2)
            n[j]+=((t+j-i)&1)
    ans=[]
    for i in range(3):
        if(m[i]>=n[i]):
            diff=m[i]-n[i]
            a=(diff+2)//3
            m[i]-=a;n[i]+=2*a
            ans.append(m[i]+n[i])
        else:
            ans.append((n[i]-1)*2+1)
    print(min(ans))