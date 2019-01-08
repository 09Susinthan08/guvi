fin=[]
def chk(a):
	a1=str(a)
	alen=len(a1)
	ams=0
	a2=a
	while(a>0):
		t=a%10
		t1=(t**alen)
		ams=ams+t1
		a=a//10
	if(a2==ams):
		fin.append(ams)
l1,l2=map(int,input().split(" "))
for i in range(l1+1,l2):
	chk(i)
for i in range(len(fin)):
	if(i==len(fin)-1):
		print(fin[i],end="")
	else:
		print(fin[i],end=" ")
