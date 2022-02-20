import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n,p=M();a=sorted(L());ans=0;c=200005;fi=[0]*c;fi[1]=1
for i in range(2,c):fi[i]=(fi[i-2]+fi[i-1])%mod1
s=set()
for i in range(n):
	j=a[i];f=0
	while j>0:
		t=j
		if j%4==0:t=j//4
		if j%2==1:t=(j-1)//2
		if t<a[i] and t in s:f=1;break
		if t==j:break
		j=t
	l=p+1-len(bin(a[i])[2:])
	if f or l<=0:continue
	s.add(a[i])
	ans=(ans+fi[l+2]-1)%mod1
print(ans)