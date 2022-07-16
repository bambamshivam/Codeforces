import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=[];ans=[]
    for i in range(n):
        l.append(S())
    s=set(l)
    for i in l:
        for j in range(len(i)):
            if i[:j] in s and i[j:] in s:ans.append('1');break
        else:ans.append('0')
    print(''.join(ans))