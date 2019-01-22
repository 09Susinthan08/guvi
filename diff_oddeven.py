a,b=map(int,input().split(" "))
if a>b:
	su=a-b
else:
	su=b-a
if(su%2==0):
	print("even")
else:
	print("odd")
