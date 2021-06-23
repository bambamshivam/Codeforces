def pat(s):
	n=len(s)
	if n==1 or n==0:
		return True
	else:
		if not pal(s):
			return False
		else:
			return pat(s[:n//2]) and pat(s[(n-n//2):])


def pal(s):
	for i in range(len(s)):
		if s[i]!=s[len(s)-i-1]:
			return False
	return True


for _ in range(int(input())):
	s=input()
	if pat(s):
		print("YES")
	else:
		print("NO")



