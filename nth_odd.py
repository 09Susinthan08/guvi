q,e=map(int,input().split(" "))
li=list(map(int,input().split(" ")))
c=0
for i in range(len(li)):
	if(i%2!=0):
		c=c+1
		if(c==e):
			break
	else:
		continue
print(li[c])
