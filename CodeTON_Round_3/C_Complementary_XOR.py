import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=list(S());b=list(S());c=0;ans=[]
    for i in range(n):
        if a[i]=='1':a[i]='0';b[i]=str(1-int(b[i]));c=(c+1)%2;ans.append([i+1,i+1])
    if c==1:
        for i in range(n):b[i]=str(1-int(b[i]))
    if ''.join(b)=='0'*n:
        print("YES");print(len(ans))
        for i in ans:print(*i)
    elif ''.join(b)=='1'*n:
        ans.append([1,n])
        ans.append([1,1])
        if n>1:ans.append([2,n])
        print("YES");print(len(ans))
        for i in ans:print(*i)
    else:print("NO")