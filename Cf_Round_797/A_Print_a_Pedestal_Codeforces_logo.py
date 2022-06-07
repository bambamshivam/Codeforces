import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I()
    if n%3==0:n-=3;print(n//3 +1,n//3 +2,n//3)
    elif n%3==1:print(n//3 , n//3 +2, n//3 -1)
    else:print(n//3 +1,n//3 +2 , n//3 -1)