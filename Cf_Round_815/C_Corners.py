import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=[];s=set();a=[];ans=0;f=1
    for i in range(n):l.append(list(S()));ans+=l[-1].count('1')
    for i in range(n):
        for j in range(m):
            if l[i][j]=='0':
                c=0
                if i-1>=0 and l[i-1][j]=='0':c+=1
                if i+1<n and l[i+1][j]=='0':c+=1
                if j-1>=0 and l[i][j-1]=='0':c+=1
                if j+1<m and l[i][j+1]=='0':c+=1
                if i-1>=0 and j-1>=0 and l[i-1][j-1]=='0':c+=1
                if i+1<n and j+1<m and l[i+1][j+1]=='0':c+=1
                if i-1>=0 and j+1<m and l[i-1][j+1]=='0':c+=1
                if i+1<n and j-1>=0 and l[i+1][j-1]=='0':c+=1
                if c>0:f=0
    if ans==n*m:ans-=1
    print(max(0,ans-f))