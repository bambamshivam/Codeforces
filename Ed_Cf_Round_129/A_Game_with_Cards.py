import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();m=I();b=L();p="Bob";q="Alice"
    if max(a)>=max(b):p="Alice"
    if max(b)>=max(a):q="Bob"
    print(p);print(q)