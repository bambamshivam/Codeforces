for _ in range(int(input())):
	l=list(map(str,input().split()))
	x=int(l[0])
	for i in range(1,x+1):
		s=l[i]
		a=0
		b=0
		c=0
		if ord(s[0])>=97 and ord(s[0])<=109:
			a=97
			b=109
		elif ord(s[0])>=78 and ord(s[0])<=90:
			a=78
			b=109
		else:
			c=1
			print("NO")
			break
		for j in range(len(s)):
			if ord(s[j])>=a and ord(s[j])<=b: 
				continue
			else:
				c=1;
				break
		if(c==1):
			print("NO")
			break
	if(c==0):
		print("YES")
