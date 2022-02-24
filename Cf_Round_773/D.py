import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();j=0;ans1=[];ans2=[];l=f=0
	while 1:
		if len(a)==0:break
		if a[0] not in a[1:]:f=1;break
		j=a[1:].index(a[0])+1
		b=a[1:j]
		for i in range(len(b)):ans1.append([l+j+i+1,b[i]])
		a=b[::-1]+a[j+1:]
		ans2.append(2*j);l+=2*j
	if f:print(-1);continue
	print(len(ans1))
	for i in ans1:print(*i)
	print(len(ans2));print(*ans2)