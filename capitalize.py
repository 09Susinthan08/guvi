a=input()
lii=a.split()
li=[]
for i in lii:
	b=i.capitalize()
	li.append(b)
for i in range(len(li)):
	if(i==len(li)-1):
		print(li[i],end="")
	else:
		print(li[i],end=" ")
