import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    l=list(S());l[0]='(';l[-1]=')';n=len(l);a=[]
    for i in range(n):
        if l[i]=='?':a.append(i)
    p=n//2-l.count('(');q=n//2-l.count(')')
    if 0 in [p,q]:print("YES");continue
    j=a[p-1];k=a[p]
    for i in range(j+1):
        if l[i]=='?':l[i]='('
    for i in range(j+1):
        if l[i]=='?':l[i]=')'
    l[j]=')';l[k]='('
    c=d=0
    for i in range(n):
        if l[i]=='(':c+=1
        if l[i]==')':d+=1
        if d>c:print("YES");break
    else:print("NO")