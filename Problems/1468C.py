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
q=I()
a=[]
di={}
m=10000000
k=1
t=1
ar=[]
heapq.heapify(a)
for i in range(q):
	l=L()
	if len(l)==2:
		heapq.heappush(a,(m-l[1],l[1],k))
		di[k]=0
		k+=1
	elif l[0]==2:
		while di.get(t,0)==1:
			t+=1
		ar.append(t)
		di[t]=1
		t+=1
	else:
		p=heapq.heappop(a)
		while di.get(p[2])==1:
			p=heapq.heappop(a)
		di[p[2]]=1
		ar.append(p[2])
print(*ar)



