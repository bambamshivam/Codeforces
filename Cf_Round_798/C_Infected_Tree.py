import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import deque
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
    n=I();adj=[[] for i in range(n)]
    for i in range(n-1):u,v=M();adj[u-1].append(v-1);adj[v-1].append(u-1)
    v=[0]*n;d=[0]*n
    @bootstrap
    def dfs(i):
        c=1;v[i]=1
        for j in adj[i]:
            if v[j]==0:c+=yield dfs(j)
        d[i]=c;yield c
    dfs(0);v=[0]*n;dp=[0]*n
    @bootstrap
    def dfs(i):
        v[i]=1;a=[];c=0
        for j in adj[i]:
            if v[j]==0:a.append(j)
        if len(a)==1:dp[i]=d[a[0]]-1
        elif len(a)==2:m1=yield dfs(a[0]);m2=yield dfs(a[1]);dp[i]=max(m1+d[a[1]]-1,m2+d[a[0]]-1)
        else:yield 0
        yield dp[i]
    dfs(0);print(dp[0])