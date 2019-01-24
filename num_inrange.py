# your code goes here
a=int(input())
b,c=map(int,input().split(" "))
flag=0
for i in range(b+1,c):
	if(i==a):
		print("yes")
		flag=1
		break
	else:
		continue
if(flag==0):
	print("no")
