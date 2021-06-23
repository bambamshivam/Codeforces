for _ in range(int(input())):
	n,k=map(int,input().split())
	str=input()
	ar=[0]*n
	for k in range(len(str)):
		ar[k]=int(str[k])
	str=ar
	l=list(map(int,input().split()))
	d=0
	for i in range(len(str)-1):
		if str[i]!=str[i+1]:
			d+=1
		else:
			d+=2
	for j in range(len(l)):
		str[l[j]-1]=1-str[l[j]-1]
		if l[j]-2>=0:
			if str[l[j]-2]!=str[l[j]-1]:
				d-=1
			else:
				d+=1
		if l[j]<len(str):
			if str[l[j]-1]!=str[l[j]]:
				d-=1
			else:
				d+=1
		print(d)