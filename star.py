# your code goes here
a=input()
li=[]
for i in a:
	li.append(i)
w=len(a)
if(w%2!=0):
	q=(w//2)
	li[q]='*'
	print(('').join(map(str,li)))
else:
	q=(w//2)
	e=q-1
	li[q]='*'
	li[e]='*'
	print(('').join(map(str,li)))
