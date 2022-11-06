import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();s=sum(a);ans=n;z=max(a)
    def f(p):
        if p<z:return n
        i=0;cur=0;r=0;m=-1
        while i<n:
            if cur<p:cur+=a[i];r+=1;i+=1
            elif cur>p:return n
            else:cur=0;m=max(m,r);r=0
        return m if m!=-1 else n
    for i in range(1,int(s**(0.5))+1):
        if s%i==0:ans=min(ans,f(i),f(s//i))
    print(ans)