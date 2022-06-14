import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    S();l=[S() for i in range(8)];x=y=m=0
    for i in range(8):
        for j in range(8):
            if l[i][j]=='#':
                c=0
                if i-1>=0 and j-1>=0 and l[i-1][j-1]=='#':c+=1
                if i+1<8 and j-1>=0 and l[i+1][j-1]=='#':c+=1
                if i+1<8 and j+1<8 and l[i+1][j+1]=='#':c+=1
                if i-1>=0 and j+1<8 and l[i-1][j+1]=='#':c+=1
                if c>m:x=i+1;y=j+1;m=c
    print(x,y)