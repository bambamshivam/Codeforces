import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();prev=-1;ans1=ans2=0
    for i in range(0,n,2):
        if s[i]!=s[i+1]:ans1+=1
        else:
            if prev!=s[i]:ans2+=1
            prev=s[i]
    print(ans1,max(ans2,1))