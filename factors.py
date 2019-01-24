# your code goes here
q=int(input())
li=[]
for i in range(1,q+1):
	if(q%i==0):
		li.append(i)
	else:
		continue
print(' '.join(map(str,li)))
