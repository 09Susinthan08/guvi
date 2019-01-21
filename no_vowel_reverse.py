a=int(input())
s=input()
s=s[::-1]
li=[]
for i in s:
	li.append(i)
for i in li:
	 if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
	 	continue
	 else:
	 	print(i,end="")
