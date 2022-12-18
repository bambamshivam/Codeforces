import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=list(S());ans=[];s=int(l[0])
    for i in range(1,n):
        if l[i]=='1' and s==1:ans.append('-');s-=1;continue
        if l[i]=='1' and s==0:ans.append('+');s+=1;continue
        if l[i]=='0':ans.append('+')
    print(''.join(ans))