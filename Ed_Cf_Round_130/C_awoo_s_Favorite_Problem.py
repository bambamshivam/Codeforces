import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();t=S()
    if s.count('b')!=t.count('b'):print("NO");continue
    j=0
    for i in range(n):
        if s[i]=='b':continue
        while j<n and t[j]=='b':j+=1
        if (j<n and s[i]!=t[j]) or (s[i]=='a' and i>j) or (s[i]=='c' and j>i):print("NO");break
        j+=1
    else:print("YES")