import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    k,n=M();ans=[1];c=1
    for i in range(k-1):
        if ans[-1]+c<=n and n-ans[-1]-c>=k-(i+2):ans.append(ans[-1]+c);c+=1
        else:ans.append(ans[-1]+1)
    print(*ans)