import math;import heapq
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())


#start here
n,m=M()
s=S()
t=S()
l,r=[0]*m,[0]*m
i,j=0,0
while j<m and i<n:
	if s[i]==t[j]:
		l[j]=i
		j+=1
	i+=1

i,j=n-1,m-1
while j>=0 and i>=0:
	if s[i]==t[j]:
		r[j]=i
		j-=1
	i-=1
a=[]
for i in range(m-1):
	a.append(r[i+1]-l[i])
print(max(a))




