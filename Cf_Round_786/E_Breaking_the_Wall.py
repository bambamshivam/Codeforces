import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n=I();a=L()
b=sorted(a)[:2]
ans=math.ceil(b[0]/2)+math.ceil(b[1]/2)
for i in range(n-2):
    ans=min(ans,math.ceil((a[i]+a[i+2])/2))
for i in range(n-1):
    x=max(a[i],a[i+1]);y=min(a[i],a[i+1])
    if x>=2*y:ans=min(ans,math.ceil(x/2))
    else:ans=min(ans,math.ceil((4*y-2*x)/3)+x-y)
print(ans)