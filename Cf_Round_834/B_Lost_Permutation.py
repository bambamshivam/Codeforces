import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    m,s=M();b=L();d=s+sum(b)
    if (int((1+8*d)**0.5)**2)!=(1+8*d):print("NO");continue
    t=int((1+8*d)**(0.5))
    if (t-1)%2:print("NO");continue
    n=(t-1)//2
    s1=set(b);p=0
    if len(s1)!=len(b):print("NO");continue
    for i in range(1,n+1):
        if i not in s1:p+=i
    print("YES" if p==s else "NO")