import math;import heapq;import string;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i = 0    
    j = 0    
    k = l 
    while i < n1 and j < n2 :
        if L[i][0] <= R[j][0]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
  
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr,l,r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

for _ in range(I()):
	n=I()
	l=L()
	a=[]
	for i in range(n):
		a.append([l[i],i])
	mergeSort(a,0,n-1)
	f=0
	for i in range(n):
		if abs(a[i][1]-i)%2!=0:
			a[i].append(1)
		else:
			a[i].append(0)
	print(a)
	ar=[]
	k=c=0
	while k<n:
		j=k+1
		ar.append([a[k][2]])
		while j<n and a[j][0]==a[k][0]:
			ar[-1].append(a[j][2])
			j+=1
		k=j
		c+=1
	print(ar)
	for t in ar:
		for j in range(len(t)):
			if j+1<len(t) and t[j]==1 and t[j+1]!=1:
				f=1
				break
			elif j+1<len(t) and t[j]==1 and t[j+1]==1:
				t[j]=0
				t[j+1]=0
		if f==1:
			break

	if f==1:
		print("NO")
	else:
		for t in ar:
			if sum(t)!=0:
				f=1
				break
		if f==1:
			print("NO")
		else:
			print("YES")
