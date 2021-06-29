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
s=S()
f=0
for i in range(2,len(s)):
	if (ord(s[i-2])+ord(s[i-1])-130)%26!=(ord(s[i])-65)%26:
		f=1
		print("NO")
		break
if f==0:
	print("YES")