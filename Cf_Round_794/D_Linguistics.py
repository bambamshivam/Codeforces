import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    a,b,c,d=M();s=S();n=len(s);p=0
    if s.count('A')!=a+c+d or s.count('B')!=b+c+d:print("NO");continue
    i=0;l=[[],[],[]]
    while i<n:
        j=i+1;cur=[s[i]]
        while j<n and s[j]!=s[j-1]:cur.append(s[j]);j+=1
        if len(cur)%2==1:l[2].append(len(cur))
        else:l[ord(cur[0])-65].append(len(cur))
        i=j
    for i in l:i.sort()
    for i in range(len(l[0])):
        if c>=l[0][i]//2:c-=l[0][i]//2;l[0][i]=0
        else:l[0][i]-=(2*c+1);c=0;break
    for i in range(len(l[1])):
        if d>=l[1][i]//2:d-=l[1][i]//2;l[1][i]=0
        else:l[1][i]-=(2*d+1);d=0;break
    p=sum((j-1)//2 for i in range(3) for j in l[i] if j>0)
    print("YES" if c+d<=p else "NO")