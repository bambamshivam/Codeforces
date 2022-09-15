import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l1=list(S().split());l2=list(S().split());l3=list(S().split())
    s1=set(l1);s2=set(l2);s3=set(l3);ans=[0]*3
    for i in l1:
        if i in s1 and (i not in s2 and i not in s3):ans[0]+=3
        if (i in s1 and i in s2 and i not in s3):ans[0]+=1
        if (i in s1 and i in s3 and i not in s2):ans[0]+=1
    for i in l2:
        if i in s2 and (i not in s1 and i not in s3):ans[1]+=3
        if (i in s1 and i in s2 and i not in s3):ans[1]+=1
        if (i in s2 and i in s3 and i not in s1):ans[1]+=1
    for i in l3:
        if i in s3 and (i not in s2 and i not in s1):ans[2]+=3
        if (i in s3 and i in s2 and i not in s1):ans[2]+=1
        if (i in s3 and i in s1 and i not in s2):ans[2]+=1
    print(*ans)