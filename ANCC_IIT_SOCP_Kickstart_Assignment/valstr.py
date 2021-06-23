def vals(s):
	k=-1
	c=0
	for i in range(len(s)):
		if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
			c+=(i+1)
			k=i
		else:
			c+=(k+1)
	return(c)


for _ in range(int(input())):
	s=input()
	print(vals(s))