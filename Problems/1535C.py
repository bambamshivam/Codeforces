import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(input())
def L():
	return list(map(int,input().split()))

for _ in range(I()):
	s=input()
	n=len(s)
	j=c=i=0
	while i<n:
		if i==0 and s[i]!='?':
			c+=1
			i+=1
		elif s[i]!='?' and s[i]==s[i-1]:
			j=i
			c+=1
			i+=1
		elif s[i]=='?':
			c+=(i-j+1)
			k=i+1
			while k<n and s[k]=='?':
				c+=(k-j+1)
				k+=1
			if k<n and s[k]==s[i-1] and (k-i)%2==0:
				j=i
			elif k<n and s[k]!=s[i-1] and (k-i)%2!=0:
				j=i
			i=k
		else:
			c+=(i-j+1)
			i+=1
	print(c)

