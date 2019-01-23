s=input()
li=[]
for i in s:
	if(i.isnumeric()):
		li.append(i)
	else:
		continue
for i in range(len(li)):
	print(li[i],end="")
