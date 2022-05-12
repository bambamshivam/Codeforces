import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353



for _ in range(I()):
    n=I();a=L();ans=[0]
    def merge(arr, l, m, r):
        n1 = m - l + 1;n2 = r - m;L = [0] * (n1);R = [0] * (n2)
        for i in range(0, n1):L[i] = arr[l + i]
        for j in range(0, n2):R[j] = arr[m + 1 + j]
        i=j=0;k=l
        while i < n1 and j < n2:
            if L[i] < R[j]:arr[k] = L[i];i += 1
            else:ans[0]+=n1-i;arr[k] = R[j];j += 1
            k += 1
        while i < n1:arr[k] = L[i];i += 1;k += 1
        while j < n2:arr[k] = R[j];j += 1;k += 1
    def mergeSort(arr, l, r):
        if l < r:m = l+(r-l)//2;mergeSort(arr, l, m);mergeSort(arr, m+1, r);merge(arr, l, m, r)
    mergeSort(a,0,n-1);print(ans[0])