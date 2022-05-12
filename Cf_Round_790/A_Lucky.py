import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=[int(i) for i in S()]
    print("YES" if sum(s[:3])==sum(s[3:]) else "NO")