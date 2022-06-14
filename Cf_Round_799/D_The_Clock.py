import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    l=list(S().split());t=l[0];k=int(l[1]);ans=0
    a,b=map(int,t.split(':'));m=a*60+b;s1=set()
    while True:
        m%=1440
        p=str(m//60)
        if len(p)==1:p='0'+p
        q=str(m%60)
        if len(q)==1:q='0'+q
        s=p+':'+q
        if s in s1:break
        s1.add(s);m+=k
    for i in s1:
        if i==i[::-1]:ans+=1
    print(ans)