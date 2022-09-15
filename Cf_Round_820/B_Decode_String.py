import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=S();ans=[];i=n-1
    while i>=0:
        if l[i]=='0':ans.append(chr(96+int(l[i-2]+l[i-1])));i-=3
        else:ans.append(chr(96+int(l[i])));i-=1
    print(''.join(ans[::-1]))