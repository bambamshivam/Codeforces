import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	S();n,m=M();have={};pos={};dp=[0]*(m+1);pr=[0]*(m+1);dp[0]=1
	for i in range(n):
		cur=S()
		for j in range(m):
			t=cur[j]
			for k in range(1,3):
				if k+j>=m:break
				t+=cur[j+k]
				if not have.get(t,0):
					have[t]=1
					pos[t]=(j,j+k,i)	
	s=S()
	for i in range(m):
		t=s[i]
		for k in range(1,3):
			if i-k<0:break
			t=s[i-k]+t
			if have.get(t,0) and dp[i-k]:
				dp[i+1]=1
				pr[i+1]=i-k
			if dp[i+1]:break
	if not dp[m]:print(-1);continue
	k=m;ans=[]
	while k>0:
		p=pr[k]	
		t=s[p:k]
		ans.append(pos[t])
		k=p
	print(len(ans));ans.reverse()
	for i in ans:print(i[0]+1,i[1]+1,i[2]+1)