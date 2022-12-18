import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    l=[L(),L()]
    if l[0][0]<l[0][1] and l[1][0]<l[1][1] and l[0][0]<l[1][0] and l[0][1]<l[1][1]:print("YES");continue
    if l[0][0]<l[0][1] and l[1][0]<l[1][1] and l[0][0]>l[1][0] and l[0][1]>l[1][1]:print("YES");continue
    if l[0][0]>l[0][1] and l[1][0]>l[1][1] and l[0][0]>l[1][0] and l[0][1]>l[1][1]:print("YES");continue
    if l[0][0]>l[0][1] and l[1][0]>l[1][1] and l[0][0]<l[1][0] and l[0][1]<l[1][1]:print("YES");continue
    print("NO")