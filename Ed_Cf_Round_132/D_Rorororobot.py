import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n,m=M();a=L();q=I()

t=[0]*(2*m)
# a is the array of initial values
def build(t,n,a):
    for i in range(n):t[i+n]=a[i]
    for i in range(n-1,0,-1):t[i]=max(t[i<<1],t[(i<<1)|1])

# change value at position p to v
def modify(t,n,p,v):
    p+=n
    t[p]=v
    while p>1:
        t[p>>1]=max(t[p],t[p^1])
        p>>=1

# find the combined value of range [l,r)
def query(t,n,l,r):
    resl=resr=0
    l+=n;r+=n
    while l<r:
        if (l&1):resl=max(resl,t[l]);l+=1
        if (r&1):r-=1;resr=max(t[r],resr)
        l>>=1;r>>=1
    return max(resl,resr)

build(t,m,a)

for i in range(q):
    xs,ys,xf,yf,k=M()
    if abs(xs-xf)%k or abs(ys-yf)%k:print("NO");continue
    p=query(t,m,min(ys,yf)-1,max(ys,yf))
    z=min(xs,xf)+((n-min(xs,xf))//k)*k
    if z<=p:print("NO")
    else:print("YES")
