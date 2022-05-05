import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();s=S();a=[0]*26
    for i in s:a[ord(i)-97]+=1
    i=25;c=0
    while i>=0 and a[i]==0:i-=1;c=i
    if k>=i:print('a'*n);continue
    b=[0]*27;ans=[];d={};b[1]=1
    for i in range(n):
        t=ord(s[i])-96;p=t
        if b[t]>0:ans+=chr(b[t]+96);continue
        while t>=1 and b[t]==0 and k>0:k-=1;t-=1
        if b[t]==0:b[t]=t
        while p>=t:b[p]=b[t];p-=1
        ans.append(chr(96+b[t]))
    print("".join(ans))