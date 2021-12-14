import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

x,y=M()
s=set();s.add(x);f=0
for i in range(30):
	new_s=set()
	for ele in s:
		if ele==y:f=1;break
		b=bin(ele)[2:]
		new_s.add(int(b[::-1],2))
		new_s.add(int('1'+b[::-1],2))
	if f:break
	s=new_s
print("YES" if f else "NO")