import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=[""];ans=0
    for i in range(n):l.append('0'+S())
    for i in range(1,n+1):
        for j in range(1,n+1):
            c=int(l[i][j]) + int(l[j][(n+1-i)]) + int(l[(n+1-i)][(n+1-j)]) + int(l[(n+1-j)][(i)])
            ans+=(min(c,4-c))
    print(ans//4)