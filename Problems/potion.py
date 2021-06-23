import heapq
n=int(input())
l=list(map(int,input().split()))
d=[]
sum=0
for i in l:
	sum+=i
	heapq.heappush(d,i)
	if sum<0:
		c=heapq.heappop(d)
		sum-=c
print(len(d))


