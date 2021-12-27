import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
fact=[1]*5005
for i in range(1,5005):
	fact[i]=(fact[i-1]*i)%mod2
n,k=M();s=S()
if k==0 or k>s.count('1'):
	print(1)
else:
	ans=0;a=[]
	for i in range(n):
		if s[i]=='1':a.append(i)
	for i in range(len(a)-k+1):
		l=a[i]-1;r=a[i+k-1]+1;p=r-1
		while l>=0 and s[l]=='0':l-=1
		while r<n and s[r]=='0':r+=1
		l+=1;r-=1;t=(r-l+1)
		f1=(fact[t]*pow(fact[t-k],mod2-2,mod2)*pow(fact[k],mod2-2,mod2))%mod2
		ans=(ans+f1)%mod2
		t1=t-(r-p+1);k1=k-1
		if i==0:continue
		f2=(fact[t1]*pow(fact[t1-k1],mod2-2,mod2)*pow(fact[k1],mod2-2,mod2))%mod2
		ans=(ans-f2)%mod2
	print(ans)