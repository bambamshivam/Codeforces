n=int(input())
a=list(map(int,input().split()))
p=[1];t=32768
x=2
for i in range(15):
    p.append(x)
    x<<=1
ans=[]
for i in a:
    m=t-i
    for j in range(1,16):
        temp=((i+p[j]-1)//p[j])*p[j]
        temp=temp-i+15-j
        m=min(m,temp)
    ans.append(m)
print(*ans)