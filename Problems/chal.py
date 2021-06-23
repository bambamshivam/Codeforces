for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    m=abs(l[0]-l[1])
    t=(0,1)
    for i in range(1,n-1):
        k=abs(l[i]-l[i+1])
        if k<m:
            m=k
            t=(i,i+1)
        if m==0:
            break
    i=t[0]
    j=t[1]
    if j+1<n:
        l1=[l[i]]+l[j+1:]+l[:i]+[l[j]]
    else:
        l1=[l[i]]+l[:i]+[l[j]]
    for i in l1:
        print(i,end=" ")
    print()