import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();p=I();c=0;d={};f=0
    for i in s:c+=ord(i)-96
    for i in s:d[i]=d.get(i,0)+1
    for i in range(26,0,-1):
        for j in range(d.get(chr(96+i),0)):
            if c<=p:f=1;break
            d[chr(96+i)]-=1;c-=i
        if f:break
    ans=[]
    for i in s:
        if d.get(i,0)>0:
            ans.append(i);d[i]-=1
    print(''.join(ans))