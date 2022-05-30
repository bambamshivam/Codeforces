import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    b,q,y=M();c,r,z=M();ans=0
    if r%q!=0 or c<b or c>b+(y-1)*q or (c-b)%q!=0 or c+(z-1)*r>b+(y-1)*q:print(0);continue
    if c+z*r>b+(y-1)*q or c-r<b:print(-1);continue
    for i in range(1,int(r**0.5)+1):
        if r%i==0:
            p=i
            if p*q//math.gcd(p,q)==r:ans=(ans+((r//p)**2))%mod1
            if i*i!=r:
                p=r//i
                if p*q//math.gcd(p,q)==r:ans=(ans+((r//p)**2))%mod1
    print(ans)