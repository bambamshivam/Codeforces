import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

n=I()
l=L()
ar=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
	j,k=i,i
	for t in range(l[i]):
		ar[j][k]=l[i]
		if k!=0 and ar[j][k-1]==0:
			k-=1
		else:
			j+=1
for i in range(n):
	print(*ar[i][:i+1])


