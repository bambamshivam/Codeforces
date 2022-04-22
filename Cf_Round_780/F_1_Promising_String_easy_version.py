import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();p=[0]*(n+1);d=[0]*(n+1);c=0;ans=0
    for i in range(1,n):
        if s[i]==s[i-1]=='-' and c==0:p[i+1]=p[i]+1;c=1
        else:p[i+1]=p[i];c=0
    for i in range(n):d[i+1]=d[i]+(s[i]=='+')
    for i in range(n):
        for j in range(i+1,n):
            a=d[j+1]-d[i];b=j-i+1-a
            if (a==b) or (b>a and (b-a)%3==0 and (b-a)//3<=p[j+1]-p[i]):ans+=1
    print(ans)