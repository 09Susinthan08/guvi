a,b=map(int,input().split(" "))
gcd=0
if a>b: 
     small = b
else: 
     small = a 
	for i in range(1, small+1): 
		if((a % i == 0) and (b % i == 0)): 
			gcd = i 
	print(gcd)
