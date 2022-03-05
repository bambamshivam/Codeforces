import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from itertools import combinations
for _ in range(I()):
	n=I();f=[0,6];l=[];ans=math.inf
	for i in range(4,15):
		if f[-1]*i>n:break
		f.append(f[-1]*i)
	for i in range(1,16):l+=list(combinations(f,i))
	for i in l:
		if sum(i)>n:continue
		s=bin(n-sum(i))[2:].count('1')
		ans=min(ans,s+len(i)-(0 in i))
	print(ans)