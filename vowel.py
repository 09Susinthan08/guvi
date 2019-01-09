q=input()
c=0
for i in q:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        c=c+1
    else:
        continue
if(c>0):
    print("yes")
else:
    print("no")
