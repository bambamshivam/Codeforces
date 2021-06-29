import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

for _ in range(I()):
	n=I()
	l=L()
	s=0
	for i in l:
		s^=i
	if s==0:
		print("YES")
	else:
		c=0
		t=0
		for i in l:
			t^=i
			if t==s:
				c+=1
				t=0
		if c>=2:
			print("YES")
		else:
			print("NO")
