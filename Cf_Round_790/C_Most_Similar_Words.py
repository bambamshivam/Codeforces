import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=[S() for i in range(n)];ans=math.inf
    for i in range(n):
        for j in range(i+1,n):
            c=0
            for k in range(m):
                c+=abs(ord(l[i][k])-ord(l[j][k]))
            ans=min(ans,c)
    print(ans)