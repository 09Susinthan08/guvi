n=int(input())
k=int(input())
su=0
li=[]
for i in range(n):
    t=int(input())
    li.append(t)
for j in range(k):
    t=li.pop(0)
    su=su+t
print(su)
