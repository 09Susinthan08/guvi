s = 0
a,d,n = map(int,input().split(" "))
for i in range(0,n):
	s = s + a
	a = a + d
print(s)
