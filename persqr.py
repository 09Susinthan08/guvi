import math
n,m = map(int,input().split(" "))
pro = n * m
if (int(pro + 0.5) ** 2) == pro:
	print("yes")
else:
	print("no")
