import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();i=0;m=0;x=n;y=0
    while i<n:
        while i<n and a[i]==0:i+=1
        if i>=n:break
        j=i;p=1;q=0
        while i<n and a[i]!=0:
            if a[i]%2==0:q+=1
            p*=abs(a[i])//a[i];i+=1
        if p<0 and i-j>1:
            t1=k=j;q1=q
            while t1<i and a[t1]>=0:t1+=1
            while k<=t1:
                if a[k]%2==0:q1-=1
                k+=1
            t2=k=i-1;q2=q
            while t2>=j and a[t2]>=0:t2-=1
            while k>=t2:
                if a[k]%2==0:q2-=1
                k-=1
            if max(q1,q2)>m:
                if q1>=q2:
                    m=q1;x=t1+1;y=n-i
                else:
                    m=q2;x=j;y=n-t2
        else:
            if p>0 and q>m:m=q;x=j;y=n-i
    print(x,y)