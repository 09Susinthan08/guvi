n = int(input())
h = 0
m = 0
if n < 60:
	print(h,end=" ")
	print(n)
else:
	h = n // 60
	m = n % 60
	print(h,end=" ")
	print(m)
