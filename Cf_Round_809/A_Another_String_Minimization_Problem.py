import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=['B']*m;a=L()
    for i in range(n):
        if l[min(a[i],m-a[i]+1)-1]!='A':
            l[min(a[i],m-a[i]+1)-1]='A'
        else:
            l[max(a[i],m-a[i]+1)-1]='A'
    print(''.join(l))