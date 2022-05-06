import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();l=[abs(i) for i in a]
    s=sum(1 for i in a if i<0)
    for i in range(s):l[i]*=-1
    print("YES" if l==sorted(l) else "NO")