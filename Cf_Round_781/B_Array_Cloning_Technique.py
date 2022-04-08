import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import Counter
for _ in range(I()):n=I();a=L();c=Counter(a);print(n-max(list(c.values()))+math.ceil(math.log2(n/max(list(c.values())))))