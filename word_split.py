s=input()
li=[]
li1=[]
for i in range(len(s)):
	if(i%2==0):
		li.append(s[i])
	else:
		li1.append(s[i])
for i in range(len(li)):
	if(i==len(li)-1):
		print(li[i],end=" ")
	else:
		print(li[i],end="")
for i in range(len(li1)):
	print(li1[i],end="")
