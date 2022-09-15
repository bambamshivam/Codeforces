import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();a=[[] for i in range(26)];ans=[];p=-1
    for i in range(len(s)):a[ord(s[i])-97].append(i)
    if ord(s[0])-97<ord(s[-1])-97:p=1
    for i in range(ord(s[0])-97,ord(s[-1])-97+p,p):
        for j in a[i]:ans.append(j+1)
    print(abs(ord(s[-1])-ord(s[0])),len(ans));print(*ans)