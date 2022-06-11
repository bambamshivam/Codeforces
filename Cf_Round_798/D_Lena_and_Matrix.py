import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();a=[[-1,-1] for i in range(4)];ans=math.inf;x=y=0
    for i in range(n):
        s=S()
        for j in range(m):
            if s[j]=='B':
                if a[0][0]==-1 or sum(a[0])>i+j:a[0]=[i,j]
                if a[1][0]==-1 or sum(a[1])<i+j:a[1]=[i,j]
                if a[2][0]==-1 or a[2][0]-a[2][1]>i-j:a[2]=[i,j]
                if a[3][0]==-1 or a[3][0]-a[3][1]<i-j:a[3]=[i,j]
    for i in range(n):
        for j in range(m):
            m1=max(abs(i-a[k][0])+abs(j-a[k][1]) for k in range(4))
            if m1<ans:ans=m1;x=i+1;y=j+1
    print(x,y)