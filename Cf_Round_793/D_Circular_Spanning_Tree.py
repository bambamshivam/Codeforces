import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S()
    if s.count('1')==0 or s.count('1')%2:print("NO");continue
    l=[[i,s[i]] for i in range(n)];i=n-1-s[::-1].index('1')+1;l=l[i:]+l[:i];i=1;print("YES");ans=[]
    while i<n:
        j=i+1;ans.append([l[0][0],l[i][0]])
        if l[i][1]=='1':i+=1;continue
        while j<n and l[j][1]=='0':ans.append([l[j-1][0],l[j][0]]);j+=1
        ans.append([l[j-1][0],l[j][0]]);i=j+1
    for i in ans:print(i[0]+1,i[1]+1)