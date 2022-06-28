import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:c^=a[j]
        if c==a[i]:print(c);break