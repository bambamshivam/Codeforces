import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=1;r=n
    while True:
        if l==r:print('!',l);sys.stdout.flush();break
        m=(l+r)//2
        print('?',l,m);sys.stdout.flush()
        a1=L();c1=0
        s1=set(list(range(l,m+1)))
        for i in a1:
            if i in s1:c1+=1
        if c1%2==1:
            r=m
        else:
            l=m+1