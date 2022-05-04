import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n,m,q=M();l=[];c=0;s="";ans=0
for i in range(n):l.append(list(S()));c+=l[-1].count('*')
for i in range(n):
    for j in range(m):
        if l[i][j]=='*' and j*n+i+1>c:ans+=1
for _ in range(q):
    i,j=M()
    if l[i-1][j-1]=='*':
        l[i-1][j-1]='.'
        x=c%n if c%n else n;y=math.ceil(c/n)
        if (j-1)*n+i>(y-1)*n+x and l[x-1][y-1]=='.':ans-=1
        elif (j-1)*n+i<(y-1)*n+x and l[x-1][y-1]=='*':ans+=1
        c-=1
    else:
        l[i-1][j-1]='*';c+=1
        x=c%n if c%n else n;y=math.ceil(c/n)
        if (j-1)*n+i>(y-1)*n+x and l[x-1][y-1]=='.':ans+=1
        elif (j-1)*n+i<(y-1)*n+x and l[x-1][y-1]=='*':ans-=1
    print(ans)