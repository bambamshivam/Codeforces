import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();l=[[i+1,a[i]] for i in range(n)];ans=0
    for i in range(n):
        for j in range(i+1,n):
            if (l[i][0]<=l[j][0] and l[i][1]>=l[j][1]) or (l[i][0]>=l[j][0] and l[i][1]<=l[j][1]):ans+=1
    print(ans)