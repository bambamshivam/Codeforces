import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();t=S()
    if t=='a':print(1)
    elif 'a' in t:print(-1)
    else:print(2**s.count('a'))