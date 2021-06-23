n = int(input())
arr = []
for i in range(n):
    a,b = list(map(int,input().split()))
    arr.append([b,a])
arr.sort()
i,j = 0,n-1
ans = 0
cnt = 0
while i<=j:
    if arr[i][0]<=cnt:
        cnt+=arr[i][1]
        ans+=arr[i][1]
        i+=1
    else:
        req = min(arr[i][0]-cnt,arr[j][1])
        cnt+=req
        arr[j][1]-=req
        ans+=2*req
        if arr[j][1]==0:
            j-=1
print(ans)