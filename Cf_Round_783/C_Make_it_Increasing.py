import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n=I();a=L();ans=math.inf
for i in range(n):
    c=0;prev=0
    for j in range(i-1,-1,-1):
        cur=((prev//a[j])+1)*a[j]
        c+=(prev//a[j])+1
        prev=cur
    prev=0
    for j in range(i+1,n):
        cur=((prev//a[j])+1)*a[j]
        c+=(prev//a[j])+1
        prev=cur
    ans=min(ans,c)
print(ans)