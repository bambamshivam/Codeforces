def findClosest(arr, target):
    n=len(arr)
    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2
 
        if (arr[mid] == target):
            return arr[mid]
        if (target < arr[mid]) :
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)
            j = mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)
            i = mid + 1
    return arr[mid]
 
 
def getClosest(val1, val2, target):
 
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1



f=open("00.txt","w")
f1=open("3.txt")
li=f1.readlines()
p=1
for _ in range(int(li[0])):
    m,k,n=map(int,li[p].split())
    p+=1
    a=[]
    ms=list(map(float,li[p].split()))
    p+=1
    ad=list(map(float,li[p].split()))
    p+=1
    si=list(map(float,li[p].split()))
    
    for s in si:
        mi=10**9
        for i in range(len(ad)):
            p=s-ad[i]
            t=findClosest(ms,p)
            if t==p:
                break

    p+=1

