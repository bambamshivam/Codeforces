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
for _ in range(I()):
	n=I()
	l=L()
	s,sr=[],[]
	h,hr=[],[]
	t=0
	for i in range(n):
		if i==0:
			s.append(l[i])
			h.append(l[i])
			for j in range(1,l[i]):
				sr.append(j)
				hr.append(j)
		elif l[i-1]==l[i]:
			s.append(sr[t])
			t+=1
			h.append(hr[-1])
			hr.pop(-1)
		else:
			s.append(l[i])
			h.append(l[i])
			for j in range(l[i-1]+1,l[i]):
				sr.append(j)
				hr.append(j)
	print(*s)
	print(*h)


