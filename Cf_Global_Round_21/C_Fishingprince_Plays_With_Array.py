import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();a=L();k=I();b=L()
    def f(a,n):
        l=[1]*n;res=[];c=[]
        for i in range(n):
            while a[i]%m==0:
                a[i]//=m;l[i]*=m
        i=0
        while i<n:
            j=i+1;s=l[i]
            while j<n and a[j]==a[i]:s+=l[j];j+=1
            res.append(a[i]);c.append(s-(s%m))
            res.append(a[i]);c.append(s%m);i=j
        return [res,c]
    t1=f(a,n);t2=f(b,k)
    print("Yes" if t1[0]==t2[0] and t1[1]==t2[1] else "No")