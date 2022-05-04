import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S()
    t=(ord(s[0])-97)*26+(ord(s[1])-97)
    t-=(ord(s[0])-97)
    if ord(s[1])>ord(s[0]):t-=1
    print(t+1)