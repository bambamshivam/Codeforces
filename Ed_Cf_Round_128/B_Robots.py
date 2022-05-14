import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=[S() for i in range(n)];p=n;c=f=0
    for i in range(m):
        for j in range(n):
            if l[j][i]=='R':
                if f==0:c=j;f=1
                p=min(p,j)
    print("YES" if p==c else "NO")