import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();l=sorted([i+a[i] for i in range(n)])[::-1]
    s=(n-1)*k - (k*(k-1)//2) + sum(a) - sum(l[:k])
    print(s)