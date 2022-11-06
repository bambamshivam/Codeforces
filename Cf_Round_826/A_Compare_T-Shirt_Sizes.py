import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    l=list(S().split())
    if l[0]==l[1]:print('=')
    elif l[0][-1]==l[1][-1]:
        if l[0][-1]=='S':
            if l[0].count('X')>l[1].count('X'):print('<')
            else:print('>')
        else:
            if l[0].count('X')>l[1].count('X'):print('>')
            else:print('<')
    else:
        if l[0][-1]=='L':print('>')
        elif l[1][-1]=='L':print('<')
        elif l[0][-1]=='M':print('>')
        elif l[1][-1]=='M':print('<')