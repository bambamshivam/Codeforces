import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for i in range(2,27):
    print('?',1,i);sys.stdout.flush()
    x=I()
    print('?',i,1);sys.stdout.flush()
    y=I()
    if x==-1:print('!',i-1);sys.stdout.flush();break
    if x!=y:print('!',x+y);sys.stdout.flush();break