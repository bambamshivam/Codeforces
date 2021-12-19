import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):w,h=M();x1=L();x2=L();y1=L();y2=L();print(max(max(x1[-1]-x1[1],x2[-1]-x2[1])*h,max(y1[-1]-y1[1],y2[-1]-y2[1])*w))