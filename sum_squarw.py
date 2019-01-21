a=int(input())
su=0
while a>0:
	temp=a%10
	q=temp**2
	su=su+q
	a=a//10
print(su)
