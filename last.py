n,m=input().split(" ")
m=int(m)
li=[]
print(len(n))
for i in range(len(n)-1,len(n)-m-2,-1):
	li.append(n[i])
li=li[::-1]
for i in range (len(li)):
	if(len(li)-1==i):
		print(li[i],end="")
	else:
		print(li[i],end="")
