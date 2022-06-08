import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();p=L();v=[0]*n;l=[];ans=[];res=1
    for i in range(n):
        if v[i]==0:
            cur=p[i];v[i]=1;l.append([i])
            while v[cur-1]==0:l[-1].append(cur-1);v[cur-1]=1;cur=p[cur-1]
    for i in l:
        cur=''.join(s[j] for j in i);dup=cur
        for j in range(len(i)):
            dup=dup[1:]+dup[0]
            if cur==dup:ans.append(j+1);break
    for i in ans:res=res*i//math.gcd(res,i)
    print(res)