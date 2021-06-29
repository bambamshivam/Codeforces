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
	n,u,r,d,l=M()
	u1,r1,d1,l1=u,r,d,l
	if u>n-2:
		if u==n-1:
			if r<l:
				l-=1
			else:
				r-=1
		else:
			r-=1
			l-=1
	if r<0 or l<0:
		print("NO")
	else:
		if d>n-2:
			if d==n-1:
				if r<l:
					l-=1
				else:
					r-=1
			else:
				l-=1
				r-=1
		if r<0 or l<0:
			print("NO")
		else:
			u=r1
			d=l1
			l=u1
			r=d1
			if u>n-2:
				if u==n-1:
					if r<l:
						l-=1
					else:
						r-=1
				else:
					r-=1
					l-=1
			if r<0 or l<0:
				print("NO")
			else:
				if d>n-2:
					if d==n-1:
						if r<l:
							l-=1
						else:
							r-=1
					else:
						l-=1
						r-=1
				if r<0 or l<0:
					print("NO")
				else:
					print("YES")
