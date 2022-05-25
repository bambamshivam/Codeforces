import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from bisect import bisect_right
for _ in range(I()):
    n=I();p=L();i=ans=0
    while i<n:
        j=i+1
        while j<n and p[j]>p[j-1]:j+=1
        if j==n:break
        ans+=1;i=j+1
    print(ans)