import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();p=q=-1;ans=[]
    for i in range(n-1):
        
        if s[i]=='0':
            p=i
            if p!=-1 and q!=-1:ans.append(i+2-(i-q))
        else:
            q=i
            if p!=-1 and q!=-1:ans.append(i+2-(i-p))
        if p==-1 or q==-1:ans.append(1)
    print(*ans)