for _ in range(int(input())):
	s=input()
	n=len(s)
	di={}
	f=0
	for i in range(n):
		if di.get(s[i],0)!=0:
			f=1
			break
		else:
			di[s[i]]=1
	l=list(s)
	l.sort()
	for i in range(n):
		if ord(l[i])!=97+i:
			f=1
			break
	if f==1:
		print("NO")
	else:
		f=0
		if 'a' not in s:
			print("NO")
		else:
			i=s.index('a')
			j=k=i
			while j<n-1:
				if s[j]>s[j+1]:
					f=1
					break
				j+=1
			while k>0:
				if s[k]>s[k-1]:
					f=1
					break
				k-=1
			if f==1:
				print("NO")
			else:
				print("YES")

