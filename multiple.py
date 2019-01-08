a=int(input())
li=[]
for i in range (1,6):
	t=a*i
	li.append(t)
for i in range(len(li)):
	if(i==len(li)-1):
		print(li[i],end="")
	else:
		print(li[i],end=" ")
