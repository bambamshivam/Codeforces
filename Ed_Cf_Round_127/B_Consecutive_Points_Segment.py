import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    def f(p):
        for i in range(1,n):
            p+=1
            if p not in [a[i],a[i]+1,a[i]-1]:return False
        return True
    print("YES" if f(a[0]) or f(a[0]+1) or f(a[0]-1) else "NO")