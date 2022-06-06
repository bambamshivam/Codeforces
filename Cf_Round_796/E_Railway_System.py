import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n,m=M();a=[]
for i in range(m):print('?','0'*i+'1'+'0'*(m-i-1),flush=1);a.append([I(),i])
a.sort();j=0;s=['0']*m;ans=0
for i in range(m):
    s[a[j][1]]='1';print('?',''.join(s),flush=1)
    if ans+a[j][0]==I():ans+=a[j][0]
    else:s[a[j][1]]='0'
    j+=1
print('!',ans,flush=1)