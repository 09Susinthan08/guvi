q=int(input())
a=0
li=list(map(int,input().split(" ")))
temp=li.copy()
li.sort()
li1=li.copy()
for i in range(len(li1)):
	if(li1[i]==temp[i]):
		a=a+1
	else:
		break
print(a)
