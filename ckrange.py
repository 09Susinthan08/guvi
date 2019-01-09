li=[1,2,3,4,5,6,7,8,9,10]
n=int(input())
c=0
for i in li:
	if(i==n):
		c=c+1
	else:
		continue
if(c==1):
	print("yes")
else:
	print("no")
