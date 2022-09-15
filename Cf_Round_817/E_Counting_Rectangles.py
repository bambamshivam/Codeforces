import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,q=M();l=[];ans=[]
    for i in range(n):l.append(L())
    for i in range(q):
        hs,ws,hb,wb=M();c=0
        for j in range(n):
            if hs<l[j][0]<hb and ws<l[j][1]<wb:c+=l[j][0]*l[j][1]
        print(c)