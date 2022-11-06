import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();ans=i=0
    while i<n:
        j=i+1
        while j<n and s[j]==s[i]:j+=1
        ans=max(ans,(j-i)**2);i=j
    print(max(ans,s.count('0')*s.count('1')))