q=int(input())
flag=0
for i in range(1,q):
	if(q%i==0):
		flag=flag+1
	else:
		continue
if(flag>1):
	print("yes")
else:
	print("no")
