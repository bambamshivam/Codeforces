import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();l=list(map(str,input().split()));k=int(l.pop(0))
    i=0;m=0
    while i<n:
        j=i
        while j<n and s[j] not in l:j+=1
        if j==n:break
        if i==0:m=max(m,j-i)
        else:m=max(m,j-i+1)
        i=j+1
    print(m)