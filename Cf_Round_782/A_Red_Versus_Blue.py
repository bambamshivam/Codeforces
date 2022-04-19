import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,r,b=M()
    t=r//(b+1)
    p=r%(b+1)
    ans=(t*"R"+"B")*(b+1-p) + ((t+1)*"R"+"B")*p
    print(ans[:-1][::-1])