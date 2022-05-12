import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
"""from types import GeneratorType
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
    return wrappedfunc"""
import threading
sys.setrecursionlimit(4010)
threading.stack_size(10**8)
def solve():
    for _ in range(I()):
        n=I();a=L();adj=[[] for i in range(n)];s=S();ans=[0]
        for i in range(n-1):adj[i+1].append(a[i]-1);adj[a[i]-1].append(i+1)
        def dfs(r):
            c1=c2=0;t=-1 if r==0 else a[r-1]-1
            for j in adj[r]:
                if j!=t:
                    l=dfs(j);c1+=l[0];c2+=l[1]
            c1+=1;c2+=1 if s[r]=='B' else 0
            if c1==2*c2:ans[0]+=1
            return [c1,c2]
        dfs(0);print(ans[0])

threading.Thread(target=solve).start()