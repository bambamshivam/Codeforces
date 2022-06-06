import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=[0]*26
    for t in range(2*n +1):
        s=S()
        for i in s:a[ord(i)-97]+=1
    for i in range(26):
        if a[i]%2:print(chr(i+97));break