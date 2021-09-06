n,l=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
ar.append(l)
ar.reverse()
ar.append(0)
n+=2
m=-1
for i in range(1,n-2):
	m=max(m,ar[i]-ar[i+1])
print(max(m/2,ar[0]-ar[1],ar[-2]-ar[-1]))
