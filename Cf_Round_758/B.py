import math;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	n,a,b=M();a1,b1=a,b
	if max(a,b)>(n-1)//2 or abs(a-b)>1 or a+b>n-2:print(-1);continue
	i=1;j=n
	if a>=b:
		ans=[i,j];i+=1;j-=1;c=0
		while a>0 or b>0:
			if c%2==0:
				ans.append(i)
				a-=1;i+=1
			else:
				ans.append(j)
				b-=1;j-=1
			c+=1
	else:
		ans=[j,i];j-=1;i+=1;c=0
		while a>0 or b>0:
			if c%2==0:
				ans.append(j)
				b-=1;j-=1
			else:
				ans.append(i)
				a-=1;i+=1
			c+=1
	p=len(ans)
	for k in range(i,j+1):
		ans.append(k)
	if a1>b1:
		ans=ans[:p-1]+sorted(ans[p-1:],reverse=True)
	else:
		ans=ans[:p-1]+sorted(ans[p-1:])
	print(*ans)