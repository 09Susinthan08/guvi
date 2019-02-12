w=input()
li=list(w)
a=[]
for i in range(0,len(li)):
	if(i==0):
		a.append(li[i])
	elif(i%3==0):
		a.append(li[i])
	else:
		continue
print(''.join(map(str,a)))
