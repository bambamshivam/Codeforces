import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
for _ in range(I()):
    n=I();a=L();ans=f=0
    for i in range(n):
        if a[i]==0:a[i]+=1;ans+=1
    def check():
        m=0;v=[0]*31
        if 0 in a:return False
        for i in range(n):m|=a[i]
        adj=[[] for i in range(31)]
        for i in a:
            l=-1
            for j in range(31):
                if (1<<j)&i:
                    if l!=-1:adj[l].append(j);adj[j].append(l)
                    l=j
        @bootstrap
        def dfs(i):
            if v[i]:yield 0
            v[i]=1
            for j in adj[i]:yield dfs(j)
            yield 0
        for i in range(31):
            if m&(1<<i):dfs(i);break
        for i in range(31):
            if (1<<i)&m and v[i]==0:return False
        return True
    if check():print(ans);print(*a);continue
    for i in range(n):
        a[i]+=1
        if check():print(ans+1);print(*a);f=1;break
        a[i]-=1
    if f:continue
    for i in range(n):
        a[i]-=1
        if check():print(ans+1);print(*a);f=1;break
        a[i]+=1
    if f:continue
    m=max(i&(-i) for i in a);l=[]
    for i in range(n):
        if a[i]&(-a[i])==m:a[i]-=1;break
    for i in range(n):
        if a[i]&(-a[i])==m:a[i]+=1;break
    print(ans+2);print(*a)