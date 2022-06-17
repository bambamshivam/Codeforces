import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();c=0
    if sum(a)!=0:print("No");continue
    while a and a[-1]==0:a.pop()
    if len(a)==0:print("Yes");continue
    if (len(a)==1 and a[0]!=0) or (len(a)>1 and (a[-1]>0 or a[0]<=0)):print("No");continue
    for i in range(len(a)-1,0,-1):
        c+=a[i]
        if c>=0:print("No");break
    else:print("Yes")