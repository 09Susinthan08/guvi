q,r=map(int,input().split(" "))
li=list(map(int,input().split(" ")))
c=0
for i in range(len(li)):
	if(li[i]==r):
		c=c+1
	else:
		continue
print(c)
