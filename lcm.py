a,b=map(int,input().split(" "))
great,lcm=0,0
if a>b:
	great=a
else:
	great=b
while(True):
	if(great%a==0 and great%b==0):
		lcm=great
		break
	great=great+1
print(great)
