import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();c=sum(ord(i)-96 for i in s)
    if len(s)==1:print("Bob",ord(s[0])-96);continue
    if len(s)%2==0:print("Alice",c);continue
    print("Alice",max(c-2*ord(s[-1])+2*96,c-2*ord(s[0])+2*96))