import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=L();d=L();l=[]
    for i in range(n):l.append([a[i],b[i],d[i]])
    l.sort(key=lambda x:x[0]);s=set();ans=1
    for i in range(n):
        if i not in s:
            d={};cur=i;f=0
            while True:
                d[l[cur][0]]=d.get(l[cur][0],0)+1
                d[l[cur][1]]=d.get(l[cur][1],0)+1
                s.add(cur)
                if l[cur][2]!=0 or l[cur][1]==l[cur][0]:f=1
                if d[l[cur][1]]==2:break
                cur=l[cur][1]-1
            if f!=1:ans=(ans*2)%mod1
    print(ans)