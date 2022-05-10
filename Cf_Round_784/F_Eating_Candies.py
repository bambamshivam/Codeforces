import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();w=L();i=0;j=n-1;ans=s1=s2=0
    while i<j:
        if s1==s2:
            ans=i+n-j-1
            s1+=w[i];i+=1
            s2+=w[j];j-=1
        elif s1>s2:
            s2+=w[j];j-=1
        else:
            s1+=w[i];i+=1
    if s1==s2:ans=i+n-1-j
    if i==j and abs(s1-s2)==w[i]:ans=n
    print(ans)