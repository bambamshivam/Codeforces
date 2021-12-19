import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

q=I();l=[];ans=[]
for i in range(q):l.append(L())
l.reverse();d=[i for i in range(500001)]
for j in l:
	if j[0]==1:ans.append(d[j[1]])
	else:
		d[j[1]]=d[j[2]]
print(*ans[::-1])