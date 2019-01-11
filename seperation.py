q=int(input())
li=[]
while q>0:
	t=q%10
	li.append(t)
	q=q//10
lii=li[::-1]
for i in range(len(lii)):
	if(i==len(lii)-1):
		print(lii[i],end="")
	else:
		print(lii[i],end=" ")
