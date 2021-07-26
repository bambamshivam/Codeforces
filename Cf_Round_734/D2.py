import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m,k=M()
	def pri(dp,n,m):
		for i in range(n):
			s=""
			for j in range(m):
				s+=dp[i][j]
			print(s)
	def trans(dp,n,m):
		dp1=[[0 for i in range(n)] for j in range(m)]
		for j in range(m):
			for i in range(n):
				dp1[j][i]=dp[i][j]
		return dp1
	def solve(a,n,m,k,dp,c):
		i=a
		j=0
		for i in range(a,n,2):
			for j in range(0,m,2):
				if c>=k:
					break
				s=(i//2 + j//2)%2
				dp[i][j]=chr(2*s+97)
				dp[i][j+1]=chr(2*s+97)
				dp[i+1][j]=chr(2*s+1+97)
				dp[i+1][j+1]=chr(2*s+1+97)
				c+=2
			if c>=k:
				break
		if i<n and j<m and dp[i][j]==0:
			for r in range(j,m,2):
				if c>=(n*m)//2:
					break
				s=(i//2 + r//2)%2
				dp[i][r]=chr(2*s+97)
				dp[i+1][r]=chr(2*s+97)
				dp[i][r+1]=chr(2*s+1+97)
				dp[i+1][r+1]=chr(2*s+1+97)
				s^=1
				c+=2
		for t in range(i+2,n,2):
			for j in range(0,m,2):
				if c>=(n*m)//2:
					break
				s=(t//2 + j//2)%2
				dp[t][j]=chr(2*s+97)
				dp[t+1][j]=chr(2*s+97)
				dp[t][j+1]=chr(2*s+1+97)
				dp[t+1][j+1]=chr(2*s+1+97)
				s^=1
				c+=2
			if c>=(n*m)//2:
				break
	if n%2==0 and m%2==0:
		dp=[[0 for i in range(m)] for j in range(n)]
		if k%2==0:
			print("YES")
			solve(0,n,m,k,dp,0)
			pri(dp,n,m)
		else:
			print("NO")
	elif n%2==0 and m%2==1:
		k=(n*m)//2 - k
		n,m=m,n
		dp=[[0 for i in range(m)] for j in range(n)]
		if k>=(m//2) and (k-(m//2))%2==0:
			print("YES")
			s=c=0
			for j in range(0,m,2):
				dp[0][j]=chr(s+121)
				dp[0][j+1]=chr(s+121)
				s^=1
				c+=1
			solve(1,n,m,k,dp,c)
			dp1=trans(dp,n,m)
			pri(dp1,m,n)
		else:
			print("NO")
	else:
		dp=[[0 for i in range(m)] for j in range(n)]
		if k>=(m//2) and (k-(m//2))%2==0:
			print("YES")
			s=c=0
			for j in range(0,m,2):
				dp[0][j]=chr(s+121)
				dp[0][j+1]=chr(s+121)
				s^=1
				c+=1
			solve(1,n,m,k,dp,c)
			pri(dp,n,m)
		else:
			print("NO")

