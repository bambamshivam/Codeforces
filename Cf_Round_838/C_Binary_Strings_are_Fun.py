import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
fact=[1]*200010
for i in range(1,200010):fact[i]=((fact[i-1]*i)%mod2)
for _ in range(I()):
    n=I();s=S();a=[0,0];ans=1;a[int(s[0])]+=1;f=0
    for i in range(1,n):
        j=int(s[i])
        a[j]+=1
        f+=1
        t=max(i+1-a[j],0)
        p=(((fact[f]*pow(fact[t],-1,mod2)*pow(fact[f-t],-1,mod2))%mod2)*pow(2,f-t,mod2))%mod2
        f-=t
        a[j]+=t
        ans=(ans+p)%mod2
    print(ans)