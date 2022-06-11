import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m,k=M();a=sorted(list(S()))[::-1];b=sorted(list(S()))[::-1];i=n-1;j=m-1;ans=[];k1=k2=k
    while i>=0 and j>=0:
        if ord(a[i])<ord(b[j]):
            if k1>0:ans.append(a[i]);i-=1;k1-=1;k2=k
            else:ans.append(b[j]);j-=1;k1=k;k2-=1
        else:
            if k2>0:ans.append(b[j]);j-=1;k2-=1;k1=k
            else:ans.append(a[i]);i-=1;k2=k;k1-=1
    print(''.join(ans))