import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();l=[];f=0;s={}
	for i in range(n):l.append(S());s[l[-1]]=s.get(l[-1],0)+1
	for i in l:
		if i[::-1] in s or (len(i)==3 and s.get(i[1::-1],0)>0):f=1;break
		s[i]-=1
	s={};l.reverse()
	for i in l:s[i]=s.get(i,0)+1
	for i in l:
		if i[::-1] in s or (len(i)==3 and s.get(i[:0:-1],0)>0):f=1;break
		s[i]-=1
	print("YES" if f else "NO")