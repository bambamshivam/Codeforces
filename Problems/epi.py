f=open("n.txt","w")
f1=open("2.txt")
li=f1.readlines()
p=1
for _ in range(int(li[0])):
	n,l=map(int,li[p].split())
	p+=1
	a=[]
	arr=[]
	for i in range(n):
		a.append(li[p+i])
	di={}
	k=0
	for i in range(l):
		s=""
		for j in range(n):
			s+=a[j][i]
		if s not in di:
			di[s]=k
			k+=1
		arr.append(di[s]+1)
	f.write(str(len(di))+"\n")
	for i in range(len(arr)):
		f.write(str(arr[i])+" ")
	f.write("\n")
	p+=n

