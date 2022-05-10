import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=[S() for i in range(n)]
    ans=[[] for i in range(n)]
    for j in range(m):
        a=[l[i][j] for i in range(n)]
        i=0;p=[]
        while i<n:
            j=i;c=0
            while j<n and a[j]!='o':
                if a[j]=='*':c+=1
                j+=1
            for k in range(j-i-c):p.append('.')
            for k in range(c):p.append('*')
            if j!=n:p.append('o')
            i=j+1
        for i in range(n):ans[i].append(p[i])
    for i in ans:print("".join(i))