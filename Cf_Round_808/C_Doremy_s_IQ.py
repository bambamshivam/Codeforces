import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,q=M();a=L();ans=[];c=0
    for i in range(n-1,-1,-1):
        if a[i]<=c:ans.append('1')
        elif c<q:c+=1;ans.append('1')
        else:ans.append('0')
    print(''.join(ans[::-1]))