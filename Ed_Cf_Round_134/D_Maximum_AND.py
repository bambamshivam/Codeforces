import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=L();s=list(range(n));l=[[s,s]];ans=0
    for j in range(30,-1,-1):
        t=(1<<j);p=[];c=0
        for s1,s2 in l:
            s10=[];s11=[];s20=[];s21=[]
            for i in s1:
                if (a[i]&t):s11.append(i)
                else:s10.append(i)
            for i in s2:
                if (b[i]&t):s21.append(i)
                else:s20.append(i)
            if len(s10)==len(s21):
                c+=1;p.append([s10,s21]);p.append([s11,s20])
        if c==len(l):l=p;ans+=t
    print(ans)