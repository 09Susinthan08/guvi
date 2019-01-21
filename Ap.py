s = 0
q,w,e = map(int,input().split(" "))
for i in range(0,q):
	s = s + w
	w = w + e
print(s)
