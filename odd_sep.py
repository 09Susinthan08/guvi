q=int(input())
li=[]
while q>0:
	t=q%10
	if(t%2!=0):
		li.append(t)
	q=q//10
li=li[::-1]
print(' '.join(map(str,li)))
