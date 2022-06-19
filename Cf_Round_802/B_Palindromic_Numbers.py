import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S()
    if s[0]!='9':
        l=['0']*n
        if int(s[0])+1>=int(s[-1]):l[0]='1';l[-1]=str(int(s[0])-int(s[-1])+1)
        else:l[0]=str(int(s[-1])-int(s[0]))
        for i in range(1,n//2):
            c=abs(int(s[i])-int(s[n-i-1]))
            if int(s[i])<=int(s[n-i-1]):l[i]=str(c)
            else:l[n-i-1]=str(c)
        print(''.join(l))
    else:
        l=['1']*(n+1)
        a=['0']+list(s)
        res=['0']*n
        for i in range(n,0,-1):
            if int(l[i])<int(a[i]):
                res[i-1]=str(10+int(l[i])-int(a[i]))
                l[i-1]='0'
            else:
                res[i-1]=str(int(l[i])-int(a[i]))
        print(''.join(res))
