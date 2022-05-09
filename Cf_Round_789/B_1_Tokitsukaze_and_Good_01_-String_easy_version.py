import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();i=ans=0;l=[]
    while i<n:
        j=i+1
        while j<n and s[j]==s[i]:j+=1
        l.append(j-i);i=j
    for i in range(len(l)-1):
        if l[i]%2==1:ans+=1;l[i]+=1;l[i+1]-=1
    print(ans)