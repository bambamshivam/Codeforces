import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k,x=M();s=S()[::-1];i=0;ans=[];x-=1
	while i<n:
		if s[i]=='a':ans.append('a');i+=1
		else:
			j=i+1
			while j<n and s[j]=='*':
				j+=1
			c=(j-i)*k +1
			ans.append('b'*(x%c))
			x//=c
			i=j
	print(''.join(ans[::-1]))