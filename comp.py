s=input()
maxi=0
li=s.split()
s1=li[0]
for i in li:
    a=len(i)
    if maxi<a:
        maxi=a
        s1=i
    else:
        continue
print(s1)
