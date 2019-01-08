a,b=map(int,input().split(" "))
li=[]
for i in range (a+1,b):
	if(i%2==0):
		li.append(i)
for i in range (len(li)):
	if(i==(len(li)-1)):
		print(li[i],end="")
	else:
		print(li[i],end=" ")
