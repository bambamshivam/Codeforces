import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import Counter
for _ in range(I()):
	n=I();a=L();ans,buffer=[],[];cnt=Counter(a);cost=flag=0
	for i in range(n+1):
		ans.append(cost+cnt[i])
		if i==n:break
		if cnt[i]==0:
			if not buffer:flag=1;break
			cost+=i-buffer.pop()
		else:
			buffer+=[i]*(cnt[i]-1)
	if flag==1:ans=ans+[-1]*(n+1-len(ans))
	print(*ans)