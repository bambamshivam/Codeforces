import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    x=I();s='0'+bin(x)[2:];s=s[::-1]
    i=s.index('1');j=s.index('0')
    if s.count('1')==1:print(2**i+2**j)
    else:print(2**i)