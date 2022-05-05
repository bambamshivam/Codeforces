import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    a,b,c,x,y=M()
    p=max(x-a,0);q=max(y-b,0)
    print("YES" if p+q<=c else "NO")