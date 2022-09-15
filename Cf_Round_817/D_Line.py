import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=list(S());s='R'*(n//2) + 'L'*(n-n//2);ans=[];c=0;res=[]
    for i in range(n):
        if l[i]=='L':c+=i
        else:c+=n-i-1
    p=0;q=n-1
    for i in range(n):
        if i%2==0:
            if s[p]!=l[p]:
                if s[p]=='R':c=c-p+n-p-1;l[p]='R'
                else:c=c-(n-p-1)+p;l[p]='L'
                ans.append(c)
            p+=1
        else:
            if s[q]!=l[q]:
                if s[q]=='R':c=c-q+(n-q-1);l[q]='R'
                else:c=c-(n-q-1)+q;l[q]='L'
                ans.append(c)
            q-=1
    t=len(ans)
    for i in range(n-t):ans.append(c)
    print(*ans)